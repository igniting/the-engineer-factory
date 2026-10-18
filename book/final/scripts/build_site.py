"""Build the reader-facing manuscript and a static website from the book files.

Usage: python3 book/final/scripts/build_site.py  (run from the repository root)

Outputs:
  book/final/manuscript.md   one Markdown file: front matter, chapters, back matter (notes collected
                             in one 'Notes' section at the back, grouped by chapter)
  docs/                      static HTML site (GitHub Pages), one page per part of the book
                             (the EPUB and PDF are built by build_downloads.py and copied here)
Requires pandoc on PATH. Drafting notes are never published.
"""
import os, re, subprocess, html, shutil

ROOT = os.getcwd()
B = os.path.join(ROOT, 'book')
F = os.path.join(B, 'final')
DOCS = os.path.join(ROOT, 'docs')
TITLE = 'The Engineer Factory'
SUBTITLE = 'How India Priced Its Engineers by the Hour, and What AI Does to That Bargain'
PIECES = ['prologue'] + [f'ch{i:02d}' for i in range(1, 20)] + ['epilogue']
PARTS = {'ch01': 'Part I: Before software (1940s-1977)', 'ch05': 'Part II: Bodies and wires (1977-1991)',
         'ch09': 'Part III: The export machine (1991-2008)', 'ch15': 'Part IV: Beyond services? (1985-2024)',
         'ch19': 'Part V: The break (2022-2026)'}
BACK = [('appendix-timeline', 'Timeline'), ('appendix-data', 'Data appendix'), ('notes', 'Notes'),
        ('bibliography', 'Bibliography'), ('index-terms', 'Index of terms')]


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def body_of(name):
    """Chapter text up to the draft's notes; drafting notes are excluded."""
    t = read(os.path.join(B, 'drafts', name + '.md'))
    return t.split('\n## Notes')[0].rstrip() + '\n'


def notes_of(name):
    p = os.path.join(F, 'notes', name + '.md')
    if os.path.exists(p):
        t = read(p).strip()
        t = re.sub(r'^#+ .*\n', '', t, count=1).strip()
    else:  # fall back to the draft's own notes
        t = read(os.path.join(B, 'drafts', name + '.md')).split('\n## Notes', 1)[1].split('\n---')[0].strip()
    lines = [l for l in t.split('\n') if l.strip()]
    return '\n\n'.join(lines) + '\n'


def heading(name):
    return body_of(name).split('\n', 1)[0].lstrip('# ').strip()


def link_markers(text, name):
    # turn [n] markers into superscript links to the chapter's notes on the Notes page
    return re.sub(r'\[(\d+)\]', lambda m: f'<sup id="r{m.group(1)}"><a href="notes.html#{name}-{m.group(1)}">{m.group(1)}</a></sup>', text)


def anchor_notes(notes, name):
    # number each note as a link back to its marker in the chapter page
    return re.sub(r'^\[(\d+)\]', lambda m: f'<a id="{name}-{m.group(1)}" href="{name}.html#r{m.group(1)}">{m.group(1)}.</a>', notes, flags=re.M)


def md2html(md):
    # smart typography would turn '--' (only found inside URLs) into a dash; keep it literal
    md = '\n'.join(l if re.match(r'^\s*(\|.*|-{3,})\s*$', l) else l.replace('--', '-\\-') for l in md.split('\n'))
    r = subprocess.run(['pandoc', '-f', 'markdown+smart', '-t', 'html5', '--wrap=none'],
                       input=md.encode('utf-8'), capture_output=True, check=True)
    return r.stdout.decode('utf-8')


CSS = """
@font-face{font-family:"CMU Serif";font-style:normal;font-weight:400;src:url(fonts/cmu-serif-500-roman.woff2) format("woff2")}
@font-face{font-family:"CMU Serif";font-style:italic;font-weight:400;src:url(fonts/cmu-serif-500-italic.woff2) format("woff2")}
@font-face{font-family:"CMU Serif";font-style:normal;font-weight:700;src:url(fonts/cmu-serif-700-roman.woff2) format("woff2")}
@font-face{font-family:"CMU Serif";font-style:italic;font-weight:700;src:url(fonts/cmu-serif-700-italic.woff2) format("woff2")}
:root{--bg:#fffffe;--fg:#111;--muted:#555;--accent:#7a1f1f;--rule:#d8d6d0}
@media (prefers-color-scheme:dark){:root{--bg:#1a1a18;--fg:#e8e6e0;--muted:#a8a59c;--accent:#e39b8f;--rule:#3a3935}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:19px/1.55 "CMU Serif","Latin Modern Roman","Computer Modern",Georgia,serif;font-kerning:normal;text-rendering:optimizeLegibility}
main{max-width:36rem;margin:0 auto;padding:2.5rem 1rem 4rem}
header.site{border-bottom:1px solid var(--rule);padding:.7rem 1rem;font-variant:small-caps;letter-spacing:.06em;text-align:center}
header.site a{color:var(--fg);text-decoration:none}
p{margin:0;text-align:justify;hyphens:auto;-webkit-hyphens:auto}
p+p{text-indent:1.5em}
h1+p,h2+p,h3+p,blockquote+p,table+p,ul+p{text-indent:0}
h1{font-size:1.75rem;font-weight:normal;line-height:1.25;text-align:center;margin:2rem 0 2.5rem}
h2{font-size:1.15rem;font-weight:bold;margin:2.2rem 0 .8rem}
h3{font-size:1rem;font-weight:bold;font-style:italic;margin:1.6rem 0 .6rem}
a{color:var(--accent)}
sup{font-size:.68em;line-height:0}sup a{text-decoration:none}
nav.pager{display:flex;justify-content:space-between;gap:1rem;margin-top:3rem;padding-top:1rem;border-top:1px solid var(--rule);font-size:.9rem}
nav.pager a{text-decoration:none}
.notes{font-size:.85rem}.notes p{text-indent:0;text-align:left;margin:.3rem 0;hyphens:manual}
.notes h2{font-size:1rem;margin-top:2rem}.notes h2 a{color:var(--fg);text-decoration:none}
table{border-collapse:collapse;width:100%;font-size:.8rem;display:block;overflow-x:auto;margin:1rem 0;border-top:1.5px solid var(--fg);border-bottom:1.5px solid var(--fg)}
th{border-bottom:.8px solid var(--fg)}td,th{padding:.25rem .5rem;text-align:left;vertical-align:top}
ul,ol{padding-left:1.4rem}li{margin:.2rem 0}
.toc{list-style:none;padding-left:0}.toc li{margin:.35rem 0}.toc a{color:var(--fg);text-decoration:none}
.part{font-variant:small-caps;letter-spacing:.06em;color:var(--muted);margin-top:1.8rem;text-align:left}
@media (max-width:600px){body{font-size:17px}p{text-align:left}}
.subtitle{font-size:1.1rem;font-style:italic;text-align:center;color:var(--muted);margin:-1.5rem 0 2rem}
"""


def page(title, inner, prev=None, nxt=None):
    pager = ''
    if prev or nxt:
        left = f'<a href="{prev[0]}">&larr; {html.escape(prev[1])}</a>' if prev else '<span></span>'
        right = f'<a href="{nxt[0]}">{html.escape(nxt[1])} &rarr;</a>' if nxt else '<span></span>'
        pager = f'<nav class="pager">{left}{right}</nav>'
    return f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | {TITLE}</title><link rel="stylesheet" href="style.css"></head>
<body><header class="site"><a href="index.html">{TITLE}</a></header><main>{inner}{pager}</main></body></html>
"""


def main():
    os.makedirs(DOCS, exist_ok=True)
    with open(os.path.join(DOCS, 'style.css'), 'w') as f:
        f.write(CSS)
    with open(os.path.join(DOCS, '.nojekyll'), 'w') as f:
        f.write('')
    order = [(n, heading(n)) for n in PIECES]
    back = [(n, t) for n, t in BACK if n == 'notes' or os.path.exists(os.path.join(F, n + '.md'))]
    seq = [('about', 'About this book')] + order + back

    # manuscript
    ms = [read(os.path.join(F, 'front-matter.md')).strip(), '']
    for n, h in order:
        if n in PARTS:
            ms += ['', f'# {PARTS[n]}', '']
        ms += [body_of(n), '']
    for n, t in back:
        if n == 'notes':
            ms += ['', '# Notes', '']
            for p, h in order:
                ms += [f'## {h}', '', notes_of(p), '']
        else:
            ms += ['', read(os.path.join(F, n + '.md')).strip(), '']
    with open(os.path.join(F, 'manuscript.md'), 'w') as f:
        f.write('\n'.join(ms) + '\n')

    # site pages
    def fname(n):
        return 'index.html' if n == 'index' else n + '.html'
    for i, (n, t) in enumerate(seq):
        prev = (fname(seq[i - 1][0]), seq[i - 1][1]) if i > 0 else None
        nxt = (fname(seq[i + 1][0]), seq[i + 1][1]) if i + 1 < len(seq) else None
        if n == 'about':
            fm = read(os.path.join(F, 'front-matter.md'))
            fm = fm.split('## Contents')[0]
            fm = re.sub(r'^# .*\n+## .*\n+---\n', '', fm)
            inner = '<h1>About this book</h1>' + md2html(fm)
        elif n in PIECES:
            inner = md2html(link_markers(body_of(n), n))
        elif n == 'notes':
            inner = '<h1>Notes</h1><div class="notes">'
            for p, h in order:
                inner += f'<h2 id="{p}"><a href="{p}.html">{html.escape(h)}</a></h2>' + md2html(anchor_notes(notes_of(p), p))
            inner += '</div>'
        else:
            inner = md2html(read(os.path.join(F, n + '.md')))
        with open(os.path.join(DOCS, fname(n)), 'w') as f:
            f.write(page(t, inner, prev, nxt))

    # index (title page and contents)
    items = ['<li><a href="about.html">About this book</a></li>']
    for n, h in order:
        if n in PARTS:
            items.append(f'</ul><p class="part">{html.escape(PARTS[n])}</p><ul class="toc">')
        items.append(f'<li><a href="{n}.html">{html.escape(h)}</a></li>')
    items.append('</ul><p class="part">Back matter</p><ul class="toc">')
    items += [f'<li><a href="{n}.html">{html.escape(t)}</a></li>' for n, t in back]
    inner = (f'<h1>{TITLE}</h1><p class="subtitle">{SUBTITLE}</p>'
             f'<p>A narrative history of how India built a software profession, and what AI coding tools now do to it. '
             f'Every source is listed in the notes and bibliography; the research files, data and checking logs are in '
             f'<a href="https://github.com/igniting/the-engineer-factory">the repository</a>.</p>'
             f'<p>Download: <a href="the-engineer-factory.epub">EPUB</a> (e-readers) · <a href="the-engineer-factory.pdf">PDF</a> (print layout)</p>'
             f'<h2>Contents</h2><ul class="toc">' + ''.join(items) + '</ul>')
    with open(os.path.join(DOCS, 'index.html'), 'w') as f:
        f.write(page('Contents', inner, None, ('about.html', 'About this book')))
    for ext in ('epub', 'pdf'):
        src = os.path.join(F, 'the-engineer-factory.' + ext)
        if os.path.exists(src):
            shutil.copy(src, DOCS)
    print('pages:', len(seq) + 1)


if __name__ == '__main__':
    main()
