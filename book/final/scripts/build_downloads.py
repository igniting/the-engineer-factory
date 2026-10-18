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

FONTS = os.path.join(F, 'fonts')
FACES = [('500-roman', 'normal', 400), ('500-italic', 'italic', 400), ('700-roman', 'normal', 700), ('700-italic', 'italic', 700)]


def font_faces(prefix):
    return ''.join('@font-face { font-family: "CMU Serif"; font-style: %s; font-weight: %d; src: url("%scmu-serif-%s.ttf"); }\n'
                   % (style, weight, prefix, name) for name, style, weight in FACES)


# Shared book typography (LaTeX-like): Computer Modern, justified and hyphenated, indented paragraphs.
BOOK = """
html { font-family: "CMU Serif", "Latin Modern Roman", serif; font-kerning: normal; }
p { margin: 0; text-align: justify; hyphens: auto; -webkit-hyphens: auto; orphans: 2; widows: 2; }
p + p { text-indent: 1.5em; }
h1 + p, h2 + p, h3 + p, table + p, ul + p, div + p { text-indent: 0; }
h1 { font-weight: normal; text-align: center; line-height: 1.2; }
h2 { font-weight: bold; }
sup { font-size: 0.68em; line-height: 0; }
a { color: inherit; text-decoration: none; }
table { border-collapse: collapse; width: 100%; border-top: 1.2pt solid #000; border-bottom: 1.2pt solid #000; }
th { border-bottom: 0.6pt solid #000; }
td, th { padding: 2pt 4pt; text-align: left; vertical-align: top; }
.notes-block p { text-indent: 0; text-align: left; hyphens: manual; }
.titlepage { text-align: center; }
.titlepage .s { font-style: italic; }
"""

CSS = BOOK + """
@page { size: 6in 9in; margin: 0.8in 0.75in 0.9in 0.75in; }
html { font-size: 10.5pt; line-height: 1.38; color: #000; }
body { margin: 0; }
h1 { font-size: 20pt; margin: 1.5in 0 0.55in; break-before: page; }
h2 { font-size: 11pt; margin: 1.3em 0 0.5em; break-after: avoid; }
h1 + p, h2 + p { text-indent: 0; }
table { font-size: 8pt; margin: 0.8em 0; break-inside: auto; }
tr { break-inside: avoid; }
ul, ol { margin: 0.4em 0 0.4em 1.2em; padding: 0; }
li { margin: 0.1em 0; text-align: left; }
hr { border: 0; break-after: page; }
.notes-block h2 { font-size: 10pt; margin: 1.2em 0 0.4em; }
.notes-block p { font-size: 8.5pt; line-height: 1.3; margin: 0 0 0.25em; }
.titlepage { break-after: page; padding-top: 2.3in; }
.titlepage .t { font-size: 28pt; line-height: 1.15; }
.titlepage .s { font-size: 12.5pt; margin-top: 0.35in; }
nav#TOC { break-after: page; }
nav#TOC ul { list-style: none; margin-left: 0; }
nav#TOC li { margin: 0.25em 0; }
nav#TOC::before { content: 'Contents'; display: block; font-size: 16pt; text-align: center; margin: 0.6in 0 0.35in; }
"""

EPUB_CSS = BOOK + """
body { line-height: 1.45; }
h1 { font-size: 1.6em; margin: 2em 0 1.2em; }
h2 { font-size: 1.1em; margin: 1.4em 0 0.5em; }
.notes-block p { font-size: 0.85em; margin: 0 0 0.3em; }
table { font-size: 0.8em; }
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
    footerTemplate: '<div style="width:100%;text-align:center;font-family:\'CMU Serif\',serif;font-size:8pt;color:#444"><span class="pageNumber"></span></div>',
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
    with open(os.path.join(BUILD, 'print.css'), 'w') as f:
        f.write(font_faces('file://' + FONTS + '/') + CSS)
    epub_css = os.path.join(BUILD, 'epub.css')
    with open(epub_css, 'w') as f:
        f.write(font_faces('../fonts/') + EPUB_CSS)
    fonts = [os.path.join(FONTS, 'cmu-serif-%s.ttf' % n) for n, _, _ in FACES]
    # Smart typography would turn '--' (only found inside URLs) into a dash; keep it literal.
    page = '\n'.join(l if re.match(r'^\s*(\|.*|-{3,})\s*$', l) else l.replace('--', '-\\-') for l in page.split('\n'))
    epub_md = os.path.join(BUILD, 'epub.md')
    with open(epub_md, 'w', encoding='utf-8') as f:
        f.write(page)
    subprocess.run(['pandoc', '-f', 'markdown+smart', epub_md, '-o', EPUB, '--toc', '--split-level=1',
                    '--metadata', 'title=' + title, '--metadata', 'subtitle=' + sub,
                    '--metadata', 'lang=en-GB', '--css', epub_css]
                   + sum([['--epub-embed-font', p] for p in fonts], []), check=True, capture_output=True)
    tp = os.path.join(BUILD, 'titlepage.html')
    with open(tp, 'w', encoding='utf-8') as f:
        f.write(f'<div class="titlepage"><div class="t">{title}</div><div class="s">{sub}</div></div>\n')
    subprocess.run(['pandoc', '-f', 'markdown+smart', '-t', 'html5', '-s', '--toc', '--toc-depth=1',
                    '--metadata', 'pagetitle=' + title, '--metadata', 'lang=en-GB',
                    '-c', 'print.css', '--include-before-body', tp, '-o', HTML], input=page.encode('utf-8'), check=True)
    js = os.path.join(BUILD, 'print.js')
    with open(js, 'w') as f:
        f.write(JS)
    # The page-number footer is drawn outside the page, so the font must also be installed for fontconfig.
    user_fonts = os.path.expanduser('~/.local/share/fonts')
    os.makedirs(user_fonts, exist_ok=True)
    for p in fonts:
        dst = os.path.join(user_fonts, os.path.basename(p))
        if not os.path.exists(dst):
            with open(p, 'rb') as a, open(dst, 'wb') as b:
                b.write(a.read())
    subprocess.run(['fc-cache', '-f', user_fonts], check=False)
    env = dict(os.environ)
    env.setdefault('PW_MODULE', '/opt/node-tools/node_modules/playwright')
    subprocess.run(['node', js, HTML, PDF], check=True, env=env)
    print('pdf:', os.path.getsize(PDF) // 1024, 'KB; epub:', os.path.getsize(EPUB) // 1024, 'KB')


if __name__ == '__main__':
    main()
