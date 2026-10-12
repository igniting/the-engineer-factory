# Dataset plan

Phase 1c task 3 (2026-10-11). Plans each CSV to be built in Phase 3 under `research/data/`. Rules (from the brief and house decisions D3, D4):

- One CSV per series family. Every file opens with `#` comment lines: title, definition, unit, coverage, source IDs, method notes, breaks.
- **Never splice silently.** Each source gets its own column (e.g. `exports_usd_m_nasscom`, `exports_usd_m_rbi`). A reconciled column (`*_reconciled`) is added only with a written method in the header and an overlap year where both sources exist.
- Indian fiscal years stored as `FY1999-00` with a separate `year_end` column (2000). Calendar-year series use `year`.
- Nominal and real values kept side by side. Real rupee values use CPI-IW (S0156) linked across bases with the published linking factors (4.63 for 1982 to 2001 base, general index; 2.88 for 2016 to 2001 base), base year stated. Real dollar values use US CPI-U (S0157). Dollar conversions use RBI annual average rates (S0155), fiscal-year average for fiscal-year series.
- Every row carries a `source_id` and a `confidence` (high = official/filed; medium = industry association or consultant; low = press estimate or single secondary source).
- Each CSV gets a short companion note in `research/data/notes/` listing gaps and decisions.

Status codes: **ready** = registered sources cover most years; **partial** = coverage gaps; **needs sources** = key sources not yet registered (register in Phase 3, or record as a gap).

---

## A. Reference series (needed by everything else)

| File | Definition and unit | Years | Sources | Breaks and method | Status |
|---|---|---|---|---|---|
| `inr_usd.csv` | Rupees per US dollar, annual average; calendar and fiscal year | 1950-2026 | S0155 (RBI Handbook); S0001 gives 1951 (Rs 4.5) and 1960s-80s spot values to cross-check | Official rate to 1992; FEDAI indicative 1993-April 2012; RBI reference rate from May 2012 (S0155). Note 1966 and 1991 devaluations. Mark 2025-26 values LIVE-CHECKED. | **built 2026-10-12** (calendar year 1950-2025; RBI/Fed G.5A/PWT columns, S0155, S0320, S0319) |
| `inr_usd_fy.csv` | Rupees per US dollar, financial-year average and end-year | FY1986-87 to FY2025-26 | S0155 (RBI Table 133) | Pre-1986-87 not obtained; derive from monthly G.5A if needed. | **built 2026-10-12** |
| `cpi_iw.csv` | CPI for Industrial Workers, all-India general index, each base as published, plus a linked series rebased to a stated year | 1960-2026 | S0156; RBI Handbook | Bases 1960, 1982, 2001, 2016. Use published linking factors only; record each factor in the header. | **built 2026-10-12** (FY1993-94 to FY2025-26, linked to 2016=100; 1960-base series not obtained) |
| `cpi_india_cy.csv` | India CPI (OECD MEI, tracks CPI-IW), calendar-year average, 2015=100 | 1957-2024 | S0321 | Used for calendar-year rupee series and pre-1993-94 deflation. | **built 2026-10-12** |
| `us_cpi_u.csv` | US CPI-U, annual average, 1982-84=100 | 1950-2026 | S0157 | None. | **built 2026-10-12** (1950-2025; 2025 on 11 months) |

## B. Industry size

| File | Definition and unit | Years | Sources | Breaks and method | Status |
|---|---|---|---|---|---|
| `software_exports.csv` | Software and services export revenue, US$ million, nominal and real (2025 dollars) | 1978-2026 | 1978-1998: S0001 (citing Bhatnagar; 1990-91 to 1997-98 table), S0005/S0006, S0070 (Heeks), S0085; 1998-2026: S0107 and S0140 (Nasscom), S0106 (RBI survey from 2002-03) | Three definitional families, kept apart: (1) early 'software exports' (S0001, Heeks); (2) Nasscom 'IT-BPM' / 'technology industry' exports, which later include BPM, ER&D, products, and are revised (e.g. FY25 raised from $282.6bn to $297bn, S0140); (3) RBI balance-of-payments 'software services' (S0106). No reconciled column unless an overlap method is documented. Flag years where Y2K revenue is separately estimated (S0109). | **built 2026-10-12** (Heeks 1980-1997/98; Bhatnagar 1990-91 to 1997-98; Nasscom 4 points; RBI survey 2009-11; RBI BoP 2000-01 to 2025-26 from six Handbook editions; gap FY1998-99 and FY1999-2000) |
| `industry_workforce.csv` | Direct employment, persons | 1985-2026 | S0001 (2.4m in 2010), S0107 (c. 2m FY2008), S0140 (5.95m FY26), S0211 (PLFS-based shares), S0154; Phase 2 adds S0140 (FY25E 5.8m; FY24 restated 5.67m), S0306 (FY26 59.5 lakh, +1.35 lakh), S0316 (NITI 7.5-8m all-sector tech workforce 2023: separate column, not comparable) | Nasscom 'direct employees' definition changes (IT services only vs IT-BPM vs 'technology industry'); PLFS is a household survey with a different occupational/industry classification. Separate columns; never splice Nasscom and PLFS. | **built 2026-10-12, points only** (8 periods FY1989-90 to FY2025-26; PLFS levels not obtained) |
| `domestic_vs_export.csv` | Domestic vs export revenue, US$ billion | 1990-2026 | S0001 (2010: exports $50bn, domestic $17bn), S0107, S0140 | Same Nasscom definition breaks. | partial |
| `delivery_mix.csv` | Share of export revenue delivered onsite vs offshore, % | 1990-2026 | S0086 (FY2000: 57.25% onsite), S0106 (RBI: FY2007-08 25.4% onsite, later rounds), S0085 (1990s) | Nasscom vs RBI definitions; RBI 'offsite' includes BPO. Key for Ch. 6 and 11. | partial |

## C. Firms

| File | Definition and unit | Years | Sources | Breaks and method | Status |
|---|---|---|---|---|---|
| `top_firms.csv` | Headcount, revenue (US$ m), revenue per employee (US$ thousand, nominal and real) for TCS, Infosys, Wipro, HCLTech, and one of Tech Mahindra/Cognizant; plus Cognizant India headcount | 1993-2026 (Infosys from F-1/20-F; TCS from 2004 IPO; Cognizant from 1998) | S0089, S0161 (Infosys), S0160 (TCS), S0143 (Wipro), S0192 (Cognizant), S0138, S0139 (FY26-27 live), Dataquest Top 20 (S0077) for pre-listing years; Phase 2 adds Infosys 20-F FY2002-FY2026 (S0264-S0266, S0270-S0272, S0287-S0291, S0296, S0297), Wipro 20-F (S0292, S0298), Cognizant 10-K (S0274-S0277, S0293, S0299), TCS press compilations (S0139, S0310) | Fiscal year ends differ (March vs December); IFRS vs Indian GAAP; mergers (Satyam into Tech Mahindra; CMC into TCS); headcount includes or excludes subsidiaries and BPO. Record the basis per row. | partial (HCLTech and Tech Mahindra sources to register) |
| `firm_women_attrition.csv` | Women's share of employees (%), attrition (LTM, %) by firm | 2005-2026 | S0160, S0161, S0107 (industry FY09), S0211; Phase 2 adds Cognizant attrition 2021-25 (S0293, S0299), TCS attrition 13.3% Q2 FY27 (S0310) | Attrition definitions change (voluntary vs total; IT services vs consolidated). | partial |

## D. Education

| File | Definition and unit | Years | Sources | Breaks and method | Status |
|---|---|---|---|---|---|
| `engineering_intake.csv` | AICTE approved intake, enrolment, vacancy; B.E./B.Tech; by state and branch, with CS/IT share | 1947-2026 (thin before 1990) | S0151 (AICTE dashboard: 2012-13 onwards), S0152 (AISHE from 2010-11), S0001 (1998: c. 135,000 engineering students; 2010: 1.3m), S0003 (1978: 1,500 IIT seats, 100,000 candidates), S0074 (1990 Lok Sabha answer) | AICTE 'approved intake' excludes supernumerary seats and covers only AICTE-approved institutions (IITs and some universities outside it); AISHE counts enrolment across all years of study. Pre-2010 figures from scattered official answers; mark each. | partial (needs pre-2010 AICTE annual reports) |
| `engineering_graduates.csv` | Engineering/CS/IT graduates (outturn), degree vs diploma | 2000-2026 | S0213 (2004 Duke counts), S0152 (AISHE outturn), S0151 | Degree vs diploma; engineering vs CS/IT; counts vs intake. Directly tests M08. | partial |
| `women_engineering_enrolment.csv` | Women's share of B.Tech enrolment, % | 2010-2026 | S0152 (2020-21: 28.7%), parliamentary answers (to register) | AISHE method changes. | partial |
| `cs_degrees_early.csv` | Computer science programmes and graduates, IITs and others | 1965-1995 | S0001 (MCA from 1980; IIT Kanpur B.Tech CS 1978), S0003, S0016 (Banerjee 1996, to locate) | Sparse; may become a table in the text rather than a series. | needs sources |

## E. Labour market

| File | Definition and unit | Years | Sources | Breaks and method | Status |
|---|---|---|---|---|---|
| `graduate_unemployment.csv` | Unemployment rate, usual status, graduates aged 15+, and youth 15-29, % | 1983-2026 | S0154 (PLFS 2017-18 to 2024-25); earlier NSSO employment-unemployment rounds (to register) | PLFS (2017-) vs NSSO quinquennial rounds; usual status definitions. Do not splice. | partial |
| `employability_tests.csv` | Share passing vendor employability thresholds by role, % | 2011-2019 | S0153 (Aspiring Minds/SHL) | Vendor test, not labour-market outcome; editions conflated in press. Present only with that label (M07). | partial |
| `fresher_pay.csv` | Starting annual salary for engineering graduates at large IT services firms, Rs lakh, nominal and real | 1981-2026 | Infosys F-1 (S0089) may give 1990s pay; Nasscom; company disclosures; press reports of 'stagnant fresher pay' | Offer vs CTC vs in-hand; mass recruiter vs premium tracks. | **needs sources** (no fresher-pay source registered yet) |
| `fresher_hiring.csv` | Campus/fresher hires per year by firm | 1998-2026 | S0089 (Infosys FY1998: 1,300 accepted of 70,870 applicants), S0115 (Infosys 16,000+ trained 2008-09), S0138 (TCS FY27 target 25,000, Q2 onboarded 10,000), S0133 (NITES on delays); Phase 2 adds Infosys applications/interviews/offers FY2004-FY2026 (S0264-S0266, S0270-S0272, S0287-S0291, S0296, S0297), TCS FY27 offers 25,000 and Q1/Q2 joiners (S0309, S0310, S0138), Infosys Mysuru terminations (S0311-S0314; events, not a series) | Hires vs offers vs onboarded; firms stopped disclosing at times. | partial |

## F. Migration and diaspora

| File | Definition and unit | Years | Sources | Breaks and method | Status |
|---|---|---|---|---|---|
| `h1b_country.csv` | H-1B approvals by country of birth, count and % | 1999-2026 | S0104 (INS 1999-2000: India 48.5%), S0105 (CRS; FY2023 India 72%), USCIS annual 'Characteristics' reports (to register individually) | Initial vs continuing petitions; approvals vs visas issued (State Department data). | partial |
| `h1b_employer.csv` | Approvals by employer, top 20, by year | 2009-2026 | S0159 (USCIS employer hub), S0104 ('Top 100 users' 2000); Phase 2 adds Proclamation 11069's claim that the largest IT outsourcers' registrations fell 24,946 to 2,055 (S0300; administration's figure, firms unnamed) | Employer name changes and subsidiaries; tests M11. | partial |
| `h1b_policy.csv` | Cap, fees, rule changes (event table rather than series) | 1990-2026 | S0105, S0136, S0137 (2025-26 fee and litigation, LIVE-CHECKED) | Event list. | partial |
| `indian_students_us.csv` | Indian students in the US and OPT participants | 1949-2026 | S0158 (Open Doors; 2024-25: 363,019; OPT 143,740), S0003 (1949 data) | OPT count whether India-only to confirm. | partial |
| `iit_emigration.csv` | Share of IIT graduates abroad, by cohort | 1970s-2010 | S0046 (IIT Bombay), S0047, S0172 (JEE 2010 top 1,000: 36% abroad) | Different cohorts and definitions; table, not series. | partial |

## G. Beyond services

| File | Definition and unit | Years | Sources | Breaks and method | Status |
|---|---|---|---|---|---|
| `gcc.csv` | Number of GCCs/MNC R&D centres and employees in India | 2004-2026 | S0207 (Zinnov: 594 centres, 146,760 staff, 2008; 93 new in 2004), S0141 (Nasscom-Zinnov FY24: 1,700+ GCCs, 1.9m staff, $64.6bn), S0204 (Karnataka 875); Phase 2 adds Nasscom-Zinnov 2030 projection (S0317) and FY26 2,117 GCCs, 2.36m, $98.4bn (S0318) | 'MNC R&D centre' vs 'GCC' (includes back-office captives); consultant counts revised. Separate columns per source. | partial |
| `foreign_firm_india_headcount.csv` | India headcount of foreign IT firms | 1995-2026 | S0192 (Cognizant), S0193 (Accenture 2007), S0194 (IBM 2006), S0001 (IBM 2010: c. 85,000), S0170 (EPAM); Phase 2 adds Cognizant 2025: 256,900 of 351,600 in India (S0299) | Most firms do not disclose; sparse table. | partial |
| `startup_funding.csv` | Venture/startup funding, US$ bn, deals | 2010-2026 | S0147 (Tracxn/Inc42 via press), S0190 (SaaS estimates) | Vendors differ ('tech startups' vs all). One column per vendor. | partial |
| `upi.csv` | UPI monthly transactions, volume and value | 2016-2026 | S0129 (NPCI) | None (official). | ready |
| `mobile_data_price.csv` | Effective mobile data price, Rs per GB | 2014-2026 | S0130 (Jio launch claims); TRAI reports (to register) | Company claims vs regulator data. | needs sources |

## H. Early computing (small tables, not time series)

| File | Content | Sources | Status |
|---|---|---|---|
| `computers_installed.csv` | Computers in India: 15 digital computers end-1964 (S0007); 12 R&D + 2 educational installations 1961-64 (S0001); c. 80 IBM 1401s by 1970 (S0001); ECIL 98 sold 1971-78 (S0001); <1,000 in 1978, 80,000 in 1990 (S0001) | S0001, S0007, S0041 | partial |

---

## Gaps to fill in Phase 3 (sources not yet registered)

1. Fresher pay series (no source yet). Candidate sources: company annual reports and investor calls, Nasscom, contemporaneous press with named firms and years.
2. Pre-2010 AICTE annual reports (intake by branch and state).
3. NSSO employment-unemployment rounds for pre-2017 graduate unemployment.
4. TRAI data-price reports.
5. HCLTech and Tech Mahindra filings; Dataquest Top 20 archives for pre-listing years.
6. CPI-IW linking factor for the 1960 to 1982 base.
7. USCIS annual 'Characteristics of H-1B' reports for each year (register individually).

## Cross-checks planned

- Export series: S0001's 1990-98 table vs Heeks (S0070) vs Nasscom's later back-series.
- Workforce: Nasscom vs PLFS for overlapping years (2017-18 onward).
- Infosys headcount: F-1 (S0089) vs 20-F series (S0161) for FY1998-99.
- Engineer counts: Duke 2004 (S0213) vs AICTE/AISHE for the same year.
