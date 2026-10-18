"""Recompute the locations in book/final/index-terms.md from the current drafts.

Usage: python3 book/final/scripts/build_index.py  (run from the repository root)

Each term's locations are the parts of the book whose body text (above '## Notes') mentions it.
Matching rules:
  people ('Surname, Given'): the surname must appear, and either a given name or initial must
  appear in the same part or the part was already listed for the term (guards against shared surnames);
  'Name (Variant)': either form; laws and policies ending ', 1986': the name without the year;
  anything else: the term itself, case-insensitive (except short acronyms), singular or plural.
Terms with no remaining mention are dropped and reported. New terms go in ADD below.
"""
import os, re

ROOT = os.getcwd()
F = os.path.join(ROOT, 'book', 'final', 'index-terms.md')
PIECES = ['prologue'] + [f'ch{i:02d}' for i in range(1, 20)] + ['epilogue']
LABEL = {'prologue': 'Prologue', 'epilogue': 'Epilogue', **{f'ch{i:02d}': str(i) for i in range(1, 20)}}
ORDER = {LABEL[p]: k for k, p in enumerate(PIECES)}

ADD = [
    'Vembu, Sridhar', 'Tenkasi', 'T.M.A. Pai Foundation v. State of Karnataka',
    'Nadhamuni, Srikanth', 'Malhotra, Arjun', 'Chandrasekaran, N.', 'Kota', 'Bandi, Reddy',
    'Gunda, Reedhar', 'Jairam, Aparna', 'Comptroller and Auditor General', 'IMPRESS',
    'UNITES (Union for IT and ITES Employees)', 'Plano', 'iSPIRT',
]

# Terms whose index heading differs from how the text names them: extra search patterns.
ALIASES = {
    'Apprentices': ['apprentice', 'apprenticeship'], 'B-1 business visa': ['B-1'],
    'Capitation fee laws (Karnataka, Maharashtra, Tamil Nadu, Andhra Pradesh)': ['capitation'],
    'Computer policy of 1984': ['1984 policy', 'policy of 1984', 'computer policy'],
    'DOEACC scheme': ['DOEACC'], 'Employability': ['employability', 'employable'],
    'Harvard University': ['Harvard'], 'Income-tax Act, section 80HHC': ['80HHC'],
    'Indian Institute of Information Technology, Design and Manufacturing, Jabalpur': ['Jabalpur'],
    'Puttaswamy judgment (privacy), 2017': ['Puttaswamy'], 'Russian invasion of Ukraine, 2022': ['Ukraine'],
    'Supreme Court of India': ['Supreme Court'], 'TDC-12 and TDC-316 (ECIL computers)': ['TDC-12', 'TDC-316', 'TDC'],
    'Unni Krishnan judgment, 1993': ['Unni Krishnan'], 'URAL computer': ['Ural', 'URAL'],
    'Women in computing and engineering': ['women'],
}


def body(p):
    with open(os.path.join(ROOT, 'book', 'drafts', p + '.md'), encoding='utf-8') as f:
        return f.read().split('\n## Notes')[0]


TEXT = {p: body(p) for p in PIECES}


def found(pat, text, ci=False):
    return re.search(r'(?<![A-Za-z])' + re.escape(pat) + r'(?![A-Za-z])', text, re.I if ci else 0) is not None


def locations(term, old):
    core = re.sub(r'\s*\(pseudonym[^)]*\)', '', term).strip()
    m = re.match(r'^([^,()]+),\s*([^,()]+)$', core)
    if m and not re.search(r'\d', m.group(2)) and m.group(2)[:1].isupper():
        surname, given = m.group(1).strip(), m.group(2).strip()
        tokens = [t.strip('.') for t in re.split(r'[\s.]+', given) if t.strip('.')]
        out = []
        for p in PIECES:
            t = TEXT[p]
            if found(surname, t) and (LABEL[p] in old or any(found(tok, t) for tok in tokens if len(tok) > 1)
                                      or any(re.search(r'\b' + tok + r'\.', t) for tok in tokens if len(tok) == 1)):
                out.append(LABEL[p])
        return out
    pats = []
    pm = re.match(r'^(.*?)\s*\(([^)]*)\)$', core)
    if pm:
        pats = [pm.group(1).strip(), pm.group(2).strip()]
    else:
        pats = [core]
    pats = [re.sub(r',\s*(1[89]\d\d|20\d\d)$', '', x) for x in pats if x]
    pats = pats + ALIASES.get(term, [])
    forms = []
    for x in pats:
        forms.append(x)
        forms.append(x[:-1] if x.endswith('s') else x + 's')
        if x.endswith('ies'):
            forms.append(x[:-3] + 'y')
    out = []
    for p in PIECES:
        if any(found(x, TEXT[p], ci=not (x.isupper() and len(x) <= 6)) for x in forms if x):
            out.append(LABEL[p])
    return out


def main():
    with open(F, encoding='utf-8') as f:
        src = f.read()
    head = src.split('\n## A\n')[0].rstrip() + '\n'
    entries = {}
    for line in src.splitlines():
        m = re.match(r'^- (.+?): (.+)$', line)
        if m:
            entries[m.group(1)] = set(x.strip() for x in m.group(2).split(','))
    for a in ADD:
        entries.setdefault(a, set())
    kept, dropped, changed = {}, [], 0
    for term, old in entries.items():
        new = locations(term, old)
        if not new:
            dropped.append(term)
            continue
        if set(new) != old:
            changed += 1
        kept[term] = new
    head = re.sub(r'This list gives \d+ terms', 'This list gives %d terms' % len(kept), head)
    out = [head]
    letters = {}
    for term in sorted(kept, key=lambda s: re.sub(r'[^a-z0-9 ]', '', s.lower())):
        k = re.sub(r'[^A-Za-z]', '', term)[:1].upper() or '#'
        letters.setdefault(k, []).append(term)
    for k in sorted(letters):
        out.append('## %s\n' % k)
        out += ['- %s: %s' % (t, ', '.join(sorted(kept[t], key=ORDER.get))) for t in letters[k]]
        out.append('')
    with open(F, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out).rstrip() + '\n')
    print('terms kept %d, changed %d, dropped %d: %s' % (len(kept), changed, len(dropped), '; '.join(dropped)))


if __name__ == '__main__':
    main()
