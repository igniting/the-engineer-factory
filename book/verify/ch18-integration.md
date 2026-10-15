# Ch. 18 Phase 8 integration log (2026-10-15)

Words 4,618 -> 4,763 (+145). Notes 85 -> 87. Gate: `ch18.md: words=4763 markers_ok=True n=87 notes_match=True dashes=0 banned=[] missing_ids=[] body_bullets=0 has_drafting_notes=True`.

| Passage (new sentence) | Source, page | How verified |
|---|---|---|
| "In the quarter to March 2020 its executives reported voluntary attrition of 15.1 per cent, or 18.2 per cent counting dismissals." | S0381, 6-K Ex. 99.5, call of 20 Apr 2020 (acc. 0001067491-20-000029) | Re-fetched from EDGAR with the house User-Agent. "Attrition on a standalone basis was slightly higher at 18.2%; however, voluntary attrition reduced further to 15.1% from 15.6% last quarter. Higher involuntary attrition during Q4 ..." |
| "A year later voluntary attrition, 'calculated on annualized basis', was 15.2 per cent, and had risen, they said, 'as demand for talent increased'." | S0381, Ex. 99.5, call of 14 Apr 2021 (-21-000030) | "Voluntary attrition for IT services calculated on annualized basis increased to 15.2% as demand for talent increased." |
| "On that basis it was 27.7 per cent in the year to March 2022, 20.9 per cent in the year to March 2023 and 12.6 per cent in the year to March 2024." | S0381, Ex. 99.5 calls of 13 Apr 2022 and 13 Apr 2023; Ex. 99.4 Fact Sheet Q4 FY2024 | "Voluntary LTM attrition increased to 27.7%."; "LTM voluntary attrition declined to 20.9%."; fact-sheet row "Voluntary Attrition % (LTM - IT Services) 12.6% 12.9% 20.9%". |
| "From FY2021-22 the company reported voluntary attrition over the previous twelve months instead ... The first two figures are not strictly comparable with the last three" | S0381 | Basis change visible in the wording above (quarter / annualised vs LTM). |

Transcripts are unpaginated; notes give exhibit, date and accession. Statements are labelled as the company's to investors.

## Disputes changed
- None lettered. The drafting-notes gap "TCS and Infosys attrition series" is half closed (Infosys); TCS FY2020-24 still not obtained (n. 37 now cites S0160 only, S0161 removed from it).

## Data file
- `book/research/data/firm_women_attrition.csv` exists. Proposed version (five Infosys rows FY2019-20 to FY2023-24, plus header coverage, source_ids and breaks updated; CRLF endings preserved) at `int_ch18/firm_women_attrition.csv`. The repository file and the README row count (17 -> 22) and coverage text need the same change. Note: the women's share 39.3% at 31 March 2024 (fact sheet) is entered in the FY2023-24 S0381 row; it does not change the chapter's 'nearly 40%' (S0291).

## Leads declined
- 20-F "net of attrition" hiring figures: no rate; not needed.
- TCS rates from search-engine summaries (records.md): not read; not used.
