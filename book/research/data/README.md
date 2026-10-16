# Datasets (Phase 3)

Each CSV opens with `#` header lines: title, definition, unit, coverage, source IDs, method and breaks. Every row carries a `source_id` (and usually a `confidence`). Series with different definitions are kept in separate columns and never spliced silently. Notes on gaps and decisions are in `notes/`. Plans and status are in `../dataset_plan.md`.

**Rebuild:** `sh scripts/build_all.sh RAW_DIR`, where RAW_DIR holds the downloads listed in `scripts/build_reference.py`. Other scripts use transcribed values. A full rebuild on 2026-10-12 reproduced every file byte for byte.

**Source check (2026-10-12):** every source ID cited in every CSV exists in `../sources.md`.

| File | Title | Coverage | Rows | Status |
|---|---|---|---|---|
| `computers_installed.csv` | Computers installed in India, early counts | 1964-2010 points | 13 | built 2026-10-12 (table 1964-2010) |
| `cpi_india_cy.csv` | Consumer price index for India, calendar-year average (OECD Main Economic Indicators) | 1957-2024 | 68 | built 2026-10-12 |
| `cpi_iw.csv` | Consumer Price Index for Industrial Workers (CPI-IW), all-India general index, financial-year average (April-March) | FY1993-94 to FY2025-26 (earlier fiscal years not in this table; use cpi_india_cy.csv for 1957-1992 calendar years) | 33 | built 2026-10-12 (FY1993-94 to FY2025-26, linked to 2016=100; 1960-base series not obtained) |
| `cs_degrees_early.csv` | Early computer-science degrees in India: dated events and counts | 1965-2010 | 8 | built 2026-10-12 (event table 1965-2010; disagreements noted) |
| `employability_tests.csv` | Vendor and consultant 'employability' estimates for Indian engineering graduates | Aspiring Minds/SHL 2014 and 2016 reports; McKinsey c. 2005 as reported by Duke | 9 | built 2026-10-12 (Aspiring Minds 2014, 2016; McKinsey via Duke) |
| `engineering_graduates.csv` | Engineering graduates (out-turn) in India, point estimates | 2004 and c. 2013 only (AISHE out-turn tables not obtained) | 5 | built 2026-10-12, points only (2004 Duke; c. 2013 Aspiring Minds; AISHE out-turn not obtained) |
| `engineering_intake.csv` | Engineering education capacity in India: institutions, approved intake, enrolment and vacancy | institutions 1950-51 to 2005-06; intake and enrolment 2012-13 to 2021-22; IIT seats 1978 | 24 | built 2026-10-12, partial (colleges 1950-2006; intake by level 2012-13, 2014-15, 2021-22; all-level enrolment 2012-21; vacancy; AICTE dashboard and eparlib blocked) |
| `firm_women_attrition.csv` | Attrition rate and women's share of workforce, by firm | Infosys attrition FY2005-06 to FY2011-12 and FY2019-20 to FY2023-24, women FY2023-24; Cognizant 2020-2025; TCS FY2019-20 to FY2024-25 and Q2 FY2026-27 | 27 | built 2026-10-12, partial (Infosys attrition FY2006-12; Cognizant 2020-25 attrition and women; TCS FY25, Q2 FY27) |
| `foreign_firm_india_headcount.csv` | India headcount of foreign (non-Indian-headquartered) IT firms | sparse points 2005-2025 | 10 | built 2026-10-12, points (IBM, Accenture, EPAM, Cognizant) |
| `fresher_hiring.csv` | Recruitment funnel and fresher hiring, by firm and fiscal year | Infosys FY1998-FY2026 (gaps FY1999-2000, FY2003, FY2006-07, FY2011, FY2013-19); TCS, HCLTech and Infosys press points FY2023-FY2027 | 24 | built 2026-10-12, partial (Infosys funnel 16 fiscal years FY1998-FY2026; TCS/HCLTech/Infosys press points; offers include laterals from FY2004) |
| `fresher_pay.csv` | Starting (fresher) annual pay in Indian IT services, point estimates | 2007-2026 points; no consistent series | 11 | built 2026-10-12, points only (2007-2026; press, vendor and company statements) |
| `gcc.csv` | Global capability centres (GCCs) and MNC R&D centres in India | 2004 (new centres), 2007-08, FY2024, FY2026; 2030 projection kept separate | 14 | built 2026-10-12 (2004-08 Zinnov; FY24, FY26; projections flagged) |
| `graduate_unemployment.csv` | Graduate unemployment rates, India (PLFS) with US comparison points | India graduates 2019-20 to 2023-24 (PLFS years July-June); one all-persons and one under-25 point; US 2025 points | 9 | built 2026-10-12, partial (PLFS graduates 2019-20 to 2023-24; 2017-19 not obtained; US points) |
| `h1b_country.csv` | H-1B petitions approved by beneficiary's country of birth | Oct 1999-Feb 2000; FY2005 (arrivals); FY2023; FY2024. FY2000-22 USCIS reports exist but uscis.gov blocks this container. | 10 | built 2026-10-12, points (1999-2000, FY2005, FY2023, FY2024) |
| `h1b_employer.csv` | H-1B petitions approved for initial employment, selected employers | FY2022-FY2025 (selected employers); one administration claim on registrations | 45 | built 2026-10-12, partial (NFAP FY2022-25) |
| `h1b_policy.csv` | H-1B cap, petitions issued against the cap, and policy events | 1990-2026 | 28 | built 2026-10-12 (cap 1992-2026 and events) |
| `iit_emigration.csv` | Emigration of IIT graduates and top JEE scorers | 1970s cohorts; JEE 2010 cohort | 5 | built 2026-10-12 (table) |
| `indian_students_us.csv` | Students from India in US higher education (Open Doors) | 2017/18 to 2024/25 (earlier years in Open Doors not obtained) | 8 | built 2026-10-12, partial (2017/18-2024/25) |
| `industry_workforce.csv` | Employment in India's software/IT industry, persons, point estimates by source | FY1989-90 to FY2025-26, sparse points only (no annual series obtained) | 8 | built 2026-10-12, points only (8 periods FY1989-90 to FY2025-26; PLFS levels not obtained) |
| `inr_usd.csv` | Indian rupees per US dollar, calendar-year annual average | 1950-2025 | 76 | built 2026-10-12 (calendar year 1950-2025; RBI/Fed G.5A/PWT columns, S0155, S0320, S0319) |
| `inr_usd_fy.csv` | Indian rupees per US dollar, financial year (April-March) annual average and end-year rate | FY1986-87 to FY2025-26; year_end is the calendar year in which the financial year ends | 40 | built 2026-10-12 |
| `software_exports.csv` | Indian software and services export revenue, US$ million, three definitional families kept apart | 1980-FY2025-26, with gaps (see notes/software_exports.md). Heeks rows 1980-1987 are calendar years; all others fiscal years April-March. | 45 | built 2026-10-12 (Heeks 1980-1997/98; Bhatnagar 1990-91 to 1997-98; Nasscom 4 points; RBI survey 2009-11; RBI BoP 2000-01 to 2025-26 from six Handbook editions; gap FY1998-99 and FY1999-2000) |
| `startup_funding.csv` | Venture funding raised by Indian startups, by data vendor | 2021-2024 | 6 | built 2026-10-12, partial (Tracxn 2021-24; vendors apart) |
| `top_firms.csv` | Revenue, headcount and revenue per employee, selected Indian-heritage IT firms | Infosys FY1999-FY2026 (gaps FY2002-03, FY2007, FY2011, FY2013-15); Wipro FY2016-FY2026; Cognizant 2001-2025 (headcount gaps 2003-06, 2008-10, 2013-19); TCS headcount points | 56 | built 2026-10-12, partial (Infosys FY1999-FY2026 with gaps; Wipro FY2016-26; Cognizant 2001-2025 with headcount gaps; TCS headcount points; TCS/HCLTech revenue not obtained) |
| `upi.csv` | Unified Payments Interface (UPI) transactions, India | FY2016-17 to FY2023-24 annual; one monthly point (Aug 2025) | 9 | built 2026-10-12 (RBI Handbook FY2016-17 to FY2023-24) |
| `us_cpi_u.csv` | US Consumer Price Index for All Urban Consumers (CPI-U), US city average, all items, annual average | 1950-2025. 2026 omitted (partial year; January-August 2026 monthly values 325.252-334.980 available in the raw file) | 76 | built 2026-10-12 (1950-2025; 2025 on 11 months) |
| `women_engineering_enrolment.csv` | Women's share of engineering enrolment and degrees in India | 2012-13, 2020-21, 2021-22 points; no consistent annual series obtained | 6 | built 2026-10-12, points only (AICTE 2012-13, 2020-21; AISHE 2020-21, 2021-22; bases kept apart) |

**Not built:** `mobile_data_price.csv`. TRAI's data-price reports are not registered and Indian government sites reset connections from this container. The only source in hand is Jio's own launch release (S0130), a company claim.

**Units and conventions.**
- Indian fiscal years are labelled `FY1999-00` style, or by the year in which they end (stated in each header).
- Real dollar values are in 2025 dollars (US CPI-U).
- Real rupee values use CPI-IW (fiscal years) or the OECD India CPI (calendar years, and before 1993-94).
- 1 lakh = 100,000; 1 crore = 10 million.

**Source and confidence rules.**
- Confidence is high for official or filed data, medium for an industry body, consultant or reputable press, and low for single or anecdotal sources.
- Industry-body and vendor figures (Nasscom, Zinnov, Aspiring Minds, NFAP) are labelled as such in each file.
