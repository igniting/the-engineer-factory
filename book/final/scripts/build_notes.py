#!/usr/bin/env python3
"""Build publication endnotes and a bibliography from the chapter drafts.

Stdlib only. Run from anywhere:  python3 book/final/scripts/build_notes.py

Inputs (read-only):
  book/drafts/{prologue,ch01..ch19,epilogue}.md   '## Notes' section up to the next '---'
  book/research/sources.md                         source register (markdown table)
Curated inputs (in book/final/):
  short_citations.csv        id,short       hand-reviewed short form for every cited ID
  note_overrides.csv         piece,n,text   hand-edited note text (still in S-ID form) for
                                             notes whose internal remarks need rewording
  bibliography_overrides.csv id,citation,url  cleaned full citation / URL where the register
                                             entry carries internal working text
Outputs (book/final/):
  notes/<piece>.md, bibliography.md, and a check report printed to stdout
  (also written to scripts/build_report.txt).
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FINAL = os.path.dirname(HERE)
BOOK = os.path.dirname(FINAL)
DRAFTS = os.path.join(BOOK, 'drafts')
REGISTER = os.path.join(BOOK, 'research', 'sources.md')

PIECES = ['prologue'] + ['ch%02d' % i for i in range(1, 20)] + ['epilogue']
ID_RE = re.compile(r'S\d{4}')


# ---------------------------------------------------------------- register
def load_register():
    reg = {}
    with open(REGISTER, encoding='utf-8') as fh:
        for line in fh:
            if not re.match(r'\|\s*S\d{4}\s*\|', line):
                continue
            cells = [c.strip() for c in line.strip().strip('|').split(' | ')]
            if len(cells) != 7:
                sys.exit('register row with %d cells: %s' % (len(cells), line[:60]))
            sid, cit, loc, typ, rel, acc, chs = cells
            reg[sid] = dict(id=sid, citation=cit, location=loc, type=typ,
                            withdrawn='WITHDRAWN' in (cit + acc))
    return reg


def group_of(typ):
    """P/D/S from the register's free-text type field (first code wins: 'P/S' -> P)."""
    m = re.match(r'\s*([PDS])', typ)
    return m.group(1) if m else '?'


def derive_short(entry):
    """Best-effort short citation parsed from a register citation.
    Used only as a fallback/diagnostic; short_citations.csv is authoritative."""
    cit = entry['citation']
    year = None
    ys = re.findall(r'\b(1[89]\d\d|20\d\d)\b', cit)
    if ys:
        year = ys[0]
    author = cit.split(',')[0].split('.')[0].strip()
    title = None
    m = re.search(r'\*([^*]+)\*', cit)
    q = re.search(r"'([^']+?)[.,]?'", cit)
    if q and (not m or q.start() < m.start()):
        title = "'%s'" % q.group(1).split(':')[0]
    elif m:
        title = '*%s*' % m.group(1).split(':')[0]
    if not title:
        return None
    return '%s, %s%s' % (author, title, ' (%s)' % year if year else '')


def load_shorts(reg, cited):
    path = os.path.join(FINAL, 'short_citations.csv')
    shorts = {}
    if os.path.exists(path):
        with open(path, encoding='utf-8', newline='') as fh:
            for row in csv.DictReader(fh):
                shorts[row['id'].strip()] = row['short'].strip()
    fallback = []
    for sid in sorted(cited):
        if sid not in shorts:
            d = derive_short(reg[sid]) if sid in reg else None
            shorts[sid] = d or sid
            fallback.append(sid)
    return shorts, fallback


def load_note_overrides():
    """Rows (piece, n, match, text). An override applies to the note in its piece
    whose draft text starts with `match`; `n` is only a fallback when `match` is
    empty, so renumbering a chapter's notes does not misapply overrides."""
    path = os.path.join(FINAL, 'note_overrides.csv')
    rows = []
    if os.path.exists(path):
        with open(path, encoding='utf-8', newline='') as fh:
            for row in csv.DictReader(fh):
                rows.append((row['piece'].strip(), int(row['n']),
                             (row.get('match') or '').strip(), row['text'].strip()))
    return rows


def resolve_overrides(rows, pieces):
    """Map (piece, n) -> text, matching each override to its note by draft text."""
    ov, stale = {}, []
    for piece, n, match, text in rows:
        notes = dict(pieces[piece][2]) if piece in pieces else {}
        if match:
            hits = [k for k, v in notes.items() if v.startswith(match)]
            if len(hits) == 1:
                ov[(piece, hits[0])] = text
            elif len(hits) > 1 and n in hits:
                ov[(piece, n)] = text
            else:
                stale.append((piece, n))
        elif n in notes:
            ov[(piece, n)] = text
        else:
            stale.append((piece, n))
    return ov, stale


def load_bib_overrides():
    path = os.path.join(FINAL, 'bibliography_overrides.csv')
    ov = {}
    if os.path.exists(path):
        with open(path, encoding='utf-8', newline='') as fh:
            for row in csv.DictReader(fh):
                ov[row['id'].strip()] = (row['citation'].strip(), row['url'].strip())
    return ov


# ---------------------------------------------------------------- drafts
def read_piece(piece):
    with open(os.path.join(DRAFTS, piece + '.md'), encoding='utf-8') as fh:
        text = fh.read()
    heading = text.split('\n', 1)[0].lstrip('#').strip()
    body, rest = text.split('\n## Notes', 1)
    notes_block = rest.split('\n---\n', 1)[0]   # drafting notes after '---' are dropped
    notes = []
    for line in notes_block.split('\n'):
        m = re.match(r'\[(\d+)\]\s+(.*\S)\s*$', line)
        if m:
            notes.append((int(m.group(1)), m.group(2)))
        elif line.strip():
            sys.exit('%s: unparsed notes line: %s' % (piece, line[:80]))
    markers = [int(x) for x in re.findall(r'\[(\d+)\]', body)]
    return heading, markers, notes


# ---------------------------------------------------------------- cleaning
DATE = r'\d{4}-\d{2}-\d{2}'
CLEAN_RULES = [
    # '†' explanations are internal; keep only the factual 'paraphrased'
    (re.compile(r'\s*†\s*paraphrased[^.]*\.?', re.I), ' Paraphrased.'),
    (re.compile(r'\s*†[^.]*\.?'), ''),
    # verification-process remarks
    (re.compile(r'\s*(?:S\d{4}(?: and S\d{4})? )?[Oo]riginals? (?:\([^)]*\) )?re-read ' + DATE
                + r'; rests on one source\.'), ' Rests on one source.'),
    (re.compile(r'\s*(?:S\d{4}(?: and S\d{4})? )?[Oo]riginals? (?:\([^)]*\) )?re-read ' + DATE
                + r'\.'), ''),
    (re.compile(r'\s*Review re-read ' + DATE + r'\.'), ''),
    (re.compile(r'[;,]\s*(?:full text read|page re-read in full|read in full|figures re-checked|'
                r'original text verified|original text checked|read) ' + DATE), ''),
    (re.compile(r'\s*\((?:original text verified|page re-read in full|read in full) ' + DATE
                + r'(?:; re-checked ' + DATE + r')?\)'), ''),
    # internal dispute-log references
    (re.compile(r'\s*Dispute \(?[a-z0-9]+\)?(?: \([^)]*\))?\.'), ''),
    (re.compile(r';\s*dispute [a-z0-9]+'), ''),
]


def clean(text):
    for rx, rep in CLEAN_RULES:
        text = rx.sub(rep, text)
    text = re.sub(r'\(\s*\)', '', text)
    text = re.sub(r'\s+([.;,)])', r'\1', text)
    text = re.sub(r'\.\.+$', '.', text)
    text = re.sub(r'\s{2,}', ' ', text).strip()
    if not text.endswith(('.', ')', "'")):
        text += '.'
    return text


SUSPECT = re.compile(r'register|re-read|re-checked|dispute|\.csv|Phase \d|blocked|unreachable|'
                     r'summariser|†|coordinator|reviewer|TODO|to confirm|could not be retrieved|'
                     r'from here|book/research', re.I)


def convert(text, shorts):
    return ID_RE.sub(lambda m: shorts.get(m.group(0), m.group(0)), text)


# ---------------------------------------------------------------- bibliography
def clean_url(loc):
    urls = re.findall(r'(?:https?://|www\.)[^\s;,]+(?:\([^\s)]*\))?', loc)
    urls = [u.rstrip('.,;') for u in urls]
    urls = [u[:-1] if u.endswith(')') and u.count(')') > u.count('(') else u for u in urls]
    return '; '.join(urls)


def sort_key(cit):
    s = re.sub(r"[*'\"\[\]‘’“”]", '', cit).lower()
    s = re.sub(r'^(the|a|an) ', '', s)
    return s


def main():
    reg = load_register()
    pieces = {}
    cited = set()
    for p in PIECES:
        heading, markers, notes = read_piece(p)
        pieces[p] = (heading, markers, notes)
        for _, t in notes:
            cited |= set(ID_RE.findall(t))
    unknown = sorted(i for i in cited if i not in reg)
    withdrawn = sorted(i for i in cited if i in reg and reg[i]['withdrawn'])
    shorts, fallback = load_shorts(reg, cited)
    if '--compare' in sys.argv:
        # review aid: parser output beside the curated short form for every cited ID
        for sid in sorted(cited):
            print('%s\tparsed: %s\n\tcurated: %s' % (sid, derive_short(reg[sid]), shorts[sid]))
        return
    note_ov, stale_rows = resolve_overrides(load_note_overrides(), pieces)
    bib_ov = load_bib_overrides()

    report = []
    os.makedirs(os.path.join(FINAL, 'notes'), exist_ok=True)
    total_markers = total_notes = 0
    suspects = []
    ids_in_notes = set()
    used_overrides = set()
    for p in PIECES:
        heading, markers, notes = pieces[p]
        out = ['# Notes to %s' % heading, '']
        for n, t in notes:
            src = note_ov.get((p, n))
            if src is not None:
                used_overrides.add((p, n))
            else:
                src = clean(t)
            ids_in_notes |= set(ID_RE.findall(src))
            if SUSPECT.search(src):
                suspects.append('%s [%d] %s' % (p, n, src))
            out.append('[%d] %s' % (n, convert(src, shorts)))
            out.append('')
        with open(os.path.join(FINAL, 'notes', p + '.md'), 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(out).rstrip() + '\n')
        nums = [n for n, _ in notes]
        missing = sorted(set(markers) - set(nums))
        orphans = sorted(set(nums) - set(markers))
        dup = sorted({n for n in nums if nums.count(n) > 1})
        total_markers += len(set(markers))
        total_notes += len(notes)
        status = 'OK' if not (missing or orphans or dup) else 'MISMATCH'
        report.append('%-9s markers %3d  notes %3d  %s%s%s%s' % (
            p, len(set(markers)), len(notes), status,
            ' missing=%s' % missing if missing else '',
            ' orphans=%s' % orphans if orphans else '',
            ' dup=%s' % dup if dup else ''))
    stale = sorted(set(k for k in note_ov if k not in used_overrides) | set(stale_rows))

    # bibliography
    groups = {'P': [], 'D': [], 'S': []}
    for sid in sorted(cited):
        if sid not in reg:
            continue
        e = reg[sid]
        cit, url = e['citation'], clean_url(e['location'])
        if sid in bib_ov:
            c2, u2 = bib_ov[sid]
            cit = c2 or cit
            url = u2 or url
        cit = cit.rstrip()
        line = cit + ('' if cit.endswith('.') else '.')
        if url:
            line += ' ' + url + '.' if not url.endswith('.') else ' ' + url
        line += ' [%s]' % sid
        groups.setdefault(group_of(e['type']), []).append((sort_key(cit), line, sid))
    titles = [('P', 'Primary sources'), ('D', 'Datasets'), ('S', 'Secondary sources')]
    out = ['# Bibliography', '',
           'Every source cited in the notes appears once below. The bracketed identifier at the end '
           'of each entry is the source\'s permanent number in the research register.', '']
    bib_ids = []
    for code, title in titles:
        out += ['## %s' % title, '']
        for _, line, sid in sorted(groups.get(code, [])):
            out += ['- ' + line]
            bib_ids.append(sid)
        out.append('')
    other = groups.get('?', [])
    if other:
        sys.exit('ungrouped types: %s' % [s for _, _, s in other])
    with open(os.path.join(FINAL, 'bibliography.md'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out).rstrip() + '\n')

    # internal-text leak check on bibliography
    bib_suspects = [l for l in out if re.search(
        r'to confirm|to find|to fetch|find original|check current|\bS\d{4}\b(?!\])|inferred|e\.g\.', l)]

    missing_bib = sorted(ids_in_notes - set(bib_ids))
    dup_bib = sorted({i for i in bib_ids if bib_ids.count(i) > 1})
    leftover_ids = []
    for p in PIECES:
        with open(os.path.join(FINAL, 'notes', p + '.md'), encoding='utf-8') as fh:
            for i, l in enumerate(fh, 1):
                if ID_RE.search(l):
                    leftover_ids.append('%s:%d' % (p, i))

    report += ['',
               'Total markers %d, total converted notes %d' % (total_markers, total_notes),
               'Distinct S-IDs cited: %d (P %d, D %d, S %d)' % (
                   len(cited), len(groups['P']), len(groups['D']), len(groups['S'])),
               'Bibliography entries: %d; duplicates: %s' % (len(bib_ids), dup_bib or 'none'),
               'IDs in notes missing from bibliography: %s' % (missing_bib or 'none'),
               'Unknown IDs (not in register): %s' % (unknown or 'none'),
               'Withdrawn IDs cited: %s' % (withdrawn or 'none'),
               'IDs without curated short form (parser fallback): %s' % (fallback or 'none'),
               'Note overrides applied: %d; stale overrides: %s' % (len(used_overrides), stale or 'none'),
               'Raw S-IDs left in converted notes: %s' % (leftover_ids or 'none'),
               'Notes with possible internal remarks: %d' % len(suspects)]
    report += ['  ' + s for s in suspects]
    report += ['Bibliography lines with possible internal text: %d' % len(bib_suspects)]
    report += ['  ' + s for s in bib_suspects]
    text = '\n'.join(report)
    print(text)
    with open(os.path.join(HERE, 'build_report.txt'), 'w', encoding='utf-8') as fh:
        fh.write(text + '\n')
    ok = (total_markers == total_notes and not missing_bib and not unknown and not withdrawn
          and not dup_bib and not leftover_ids and all('MISMATCH' not in r for r in report))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
