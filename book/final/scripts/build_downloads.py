"""Build the reader downloads (EPUB and PDF) from book/final/manuscript.md.

Usage: python3 book/final/scripts/build_downloads.py  (run from the repository root, after build_site.py;
then run build_site.py again to copy the files into docs/)

Note markers [n] in the text become superscripts; the notes themselves keep their numbers.

Pandoc turns the manuscript into one HTML file with a print stylesheet; headless Chromium
(via the Playwright package for Node) prints it to book/final/the-engineer-factory.pdf
at 6 x 9 inches with page numbers. Requires pandoc, node and Playwright's Chromium.
"""
import os, re, subprocess

ROOT = os.getcwd()
F = os.path.join(ROOT, 'book', 'final')
BUILD = os.path.join(F, 'build')
HTML = os.path.join(BUILD, 'book.html')
PDF = os.path.join(F, 'the-engineer-factory.pdf')
EPUB = os.path.join(F, 'the-engineer-factory.epub')
SUB = 'How India Priced Its Engineers by the Hour, and What AI Does to That Bargain'

CSS = """
@page { size: 6in 9in; margin: 0.75in 0.7in 0.85in 0.7in; }
html { font-family: 'Bitstream Charter', 'Caladea', 'DejaVu Serif', serif; font-size: 10.5pt; line-height: 1.45; color: #111; }
body { margin: 0; }
p { margin: 0; text-align: justify; hyphens: auto; orphans: 2; widows: 2; }
p + p { text-indent: 1.4em; }
h1 { font-size: 19pt; line-height: 1.2; font-weight: normal; margin: 1.6in 0 0.5in; break-before: page; text-align: left; }
h2 { font-size: 12pt; font-weight: bold; margin: 1.4em 0 0.5em; break-after: avoid; }
h3 + p, h2 + p, h1 + p { text-indent: 0; }
sup { font-size: 0.7em; line-height: 0; }
a { color: inherit; text-decoration: none; }
table { border-collapse: collapse; width: 100%; font-size: 8pt; margin: 0.8em 0; break-inside: auto; }
td, th { border-bottom: 0.4pt solid #999; padding: 2pt 3pt; text-align: left; vertical-align: top; }
tr { break-inside: avoid; }
ul, ol { margin: 0.4em 0 0.4em 1.2em; padding: 0; }
li { margin: 0.1em 0; text-align: left; }
hr { border: 0; break-after: page; }
.notes-block h2 { font-size: 10pt; margin: 1.2em 0 0.4em; }
.notes-block p { font-size: 8.5pt; line-height: 1.35; text-indent: 0; text-align: left; margin: 0 0 0.25em; }
.titlepage { break-after: page; text-align: center; padding-top: 2.2in; }
.titlepage .t { font-size: 26pt; line-height: 1.15; }
.titlepage .s { font-size: 12.5pt; margin-top: 0.35in; font-style: italic; }
nav#TOC { break-after: page; }
nav#TOC ul { list-style: none; margin-left: 0; }
nav#TOC li { margin: 0.25em 0; }
nav#TOC::before { content: 'Contents'; display: block; font-size: 15pt; margin: 0.6in 0 0.3in; }
"""

JS = r"""
const { chromium } = require(process.env.PW_MODULE || 'playwright');
(async () => {
  const [html, pdf] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + html, { waitUntil: 'load' });
  await page.pdf({
    path: pdf, width: '6in', height: '9in', printBackground: false, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;text-align:center;font-family:serif;font-size:8pt;color:#444"><span class="pageNumber"></span></div>',
  });
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
"""


def main():
    os.makedirs(BUILD, exist_ok=True)
    with open(os.path.join(F, 'manuscript.md'), encoding='utf-8') as f:
        md = f.read()
    # The manuscript opens with '# Title' and '## Subtitle'; replace them with a title page.
    lines = md.split('\n')
    title = lines[0].lstrip('# ').strip()
    sub = next(l for l in lines[1:6] if l.startswith('## ')).lstrip('# ').strip()
    body = md.split('\n', 1)[1].split('## ' + sub, 1)[1]
    # The pandoc table of contents replaces the front matter's hand-written list.
    if '\n## Contents\n' in body:
        a = body.index('\n## Contents\n')
        b = body.index('\n# ', a)
        body = body[:a] + body[b:]
    # Chapters keep their text; the notes sit in one '# Notes' section near the back, with a '## heading'
    # per chapter. Link each marker to its note and each note back to its marker, keyed by chapter order.
    is_piece = lambda h: re.match(r'^(Prologue|Chapter \d+|Epilogue)\b', h)
    out, k, in_notes = [], 0, False
    for l in body.split('\n'):
        if l.startswith('# '):
            if in_notes:
                out += ['', '</div>', '']
                in_notes = False
            if l == '# Notes':
                out += [l, '', '<div class="notes-block">', '']
                in_notes, k = True, 0
                continue
            if is_piece(l[2:]):
                k += 1
            out.append(l)
        elif in_notes and l.startswith('## ') and is_piece(l[3:]):
            k += 1
            out.append(l)
        elif in_notes and re.match(r'^\[\d+\] ', l):
            out.append(re.sub(r'^\[(\d+)\] ', lambda m: f'<a id="n{k}-{m.group(1)}" href="#r{k}-{m.group(1)}">{m.group(1)}.</a> ', l))
        elif not in_notes:
            out.append(re.sub(r'\[(\d+)\]', lambda m: f'<sup id="r{k}-{m.group(1)}"><a href="#n{k}-{m.group(1)}">{m.group(1)}</a></sup>', l))
        else:
            out.append(l)
    if in_notes:
        out.append('</div>')
    page = '\n'.join(out)
    epub_md = os.path.join(BUILD, 'epub.md')
    with open(epub_md, 'w', encoding='utf-8') as f:
        f.write(page)
    subprocess.run(['pandoc', '-f', 'markdown-smart', epub_md, '-o', EPUB, '--toc', '--split-level=1',
                    '--metadata', 'title=' + title, '--metadata', 'subtitle=' + sub,
                    '--metadata', 'lang=en-GB'], check=True, capture_output=True)
    tp = os.path.join(BUILD, 'titlepage.html')
    with open(tp, 'w', encoding='utf-8') as f:
        f.write(f'<div class="titlepage"><div class="t">{title}</div><div class="s">{sub}</div></div>\n')
    with open(os.path.join(BUILD, 'print.css'), 'w') as f:
        f.write(CSS)
    subprocess.run(['pandoc', '-f', 'markdown-smart', '-t', 'html5', '-s', '--toc', '--toc-depth=1',
                    '--metadata', 'pagetitle=' + title, '--metadata', 'lang=en-GB',
                    '-c', 'print.css', '--include-before-body', tp, '-o', HTML], input=page.encode('utf-8'), check=True)
    js = os.path.join(BUILD, 'print.js')
    with open(js, 'w') as f:
        f.write(JS)
    env = dict(os.environ)
    env.setdefault('PW_MODULE', '/opt/node-tools/node_modules/playwright')
    subprocess.run(['node', js, HTML, PDF], check=True, env=env)
    print('pdf:', os.path.getsize(PDF) // 1024, 'KB; epub:', os.path.getsize(EPUB) // 1024, 'KB')


if __name__ == '__main__':
    main()
