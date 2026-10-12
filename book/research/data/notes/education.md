# Notes: engineering_intake.csv and engineering_graduates.csv

**Built:** 2026-10-12 by `scripts/build_education.py`.

## What the series show
- **Colleges.** Engineering and technology colleges went from 31 (1950-51) to 149 (1980-81), 289 (1990-91), 486 (1997-98) and 1,562 (2005-06). Source: the MoSPI compilation (S0248). This counts institutions, not seats.
- **Approved intake (AICTE).**
  - All engineering levels: 26.95 lakh in 2012-13 and 23.67 lakh in 2021-22 (Lok Sabha reply, December 2021, via Careers360, S0323).
  - By level (Avanti Fellows, S0267): undergraduate degree 15.49 lakh (2012-13), a peak of 17.05 lakh (2014-15), then 12.53 lakh (2021-22). Diploma and postgraduate intake peaked in the same year.
  - **Reconciliation.** Avanti's three levels sum exactly to the Lok Sabha totals in both overlap years.
- **Enrolment against intake, all levels.** Fell from 17.84 lakh (2013-14) to 12.76 lakh (2020-21), per the Lok Sabha reply (S0323). Careers360 headlines this as 'BTech enrolment'. It cannot be undergraduate only: it is larger than the undergraduate seats implied by Avanti's vacancy rates. Using those rates, 2012-13 undergraduate enrolment works out at about 9.7 lakh, diploma about 6.8 lakh and postgraduate about 1 lakh, which together give about 17.5 lakh, matching the Lok Sabha figure. So the series covers all levels, and the CSV labels it that way.
- **Vacancy.** The share of approved undergraduate seats left empty peaked at 49.5% (2016-17) and fell to 34.1% (2021-22), mostly because seats were cut. Diploma vacancy rose to 49.4% (S0267).
- **AISHE BE/BTech enrolment, all years of study.** 40.85 lakh to 36.64 lakh, 'between 2016 and 2021' (S0324, citing AISHE). This is a stock of students, not intake. The exact academic years are not stated in the article: the CSV puts them at 2016-17 and 2020-21 (low confidence).
- **Careers360's April 2023 'BTech' table** (intake 23.7-25.4 lakh, 2019-22; S0324) fits neither the undergraduate nor the all-level series. Its definition is unclear, so it is kept apart at low confidence.

## Graduates
Only point estimates:
- 2004: 112,000 bachelor's and 103,000 diplomas in engineering, CS and IT (Duke, via NASSCOM projections; S0213).
- c. 2013: Aspiring Minds' unsourced '600,000' graduates (S0153).

Rajaraman's '1.3 million' is kept only to document dispute (ii). AISHE out-turn tables were not obtained.

## Gaps and blocked sources
- **AICTE dashboard** (facilities.aicte-india.org) refused connection, and returned 503 via WebFetch. **Parliamentary archives** (eparlib) are blocked. **The Avanti repository** on GitHub is outside this session's scope.
- **Missing years:** intake for 2013-14 and 2015-16 to 2020-21 by level; anything after 2021-22 (AICTE 2022-23 is an incomplete load per S0267); colleges after 2005-06; AISHE out-turn.
- **CS/IT share of intake:** not obtained.

## Use in drafting (Ch. 12, Ch. 19)
- The '1.5 million engineers a year' myth (M08) matches approved undergraduate intake at its 2014-15 peak (17 lakh), not graduates. A third to a half of seats were empty.
- Capacity has fallen by about a quarter since the peak (S0267). That predates AI tools: the AICTE moratorium on new colleges ran from 2020 (S0323).
