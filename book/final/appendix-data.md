# Data appendix

This appendix describes the 27 data files built for this book. Each section says what a file measures, how it is defined, what years it covers, where the figures come from and what limits them, and gives a short table of selected values. The full files, with a source ID and usually a confidence grade on every row, are in the book's repository under `book/research/data/`, together with notes on gaps (`notes/`) and the scripts that rebuild them (`scripts/`). Source IDs refer to the source register, `book/research/sources.md`. A few conventions apply throughout. Indian fiscal years run from April to March and are written FY2023-24 (the year to 31 March 2024); where a file gives a single year for a fiscal year, it is the calendar year in which the fiscal year ends. Lakh (100,000) and crore (10 million) are converted to international units. Rupee amounts are converted to US dollars at annual average rates from `inr_usd.csv` (calendar years) and `inr_usd_fy.csv` (fiscal years). Real values are deflated as each file states: rupee series by an Indian consumer price index (`cpi_india_cy.csv` or `cpi_iw.csv`), dollar series by the US CPI-U (`us_cpi_u.csv`), with the base year given in the column name. Series with different definitions are kept in separate columns and never joined. Figures from Nasscom, the industry's lobby group, from Zinnov, a consultancy that sells to the global capability centres it counts, from Aspiring Minds, which sells the test it reports on, and from the National Foundation for American Policy (NFAP), a pro-immigration group, are marked as such, as are projections.

## Reference series

### Rupees per US dollar, calendar year (`inr_usd.csv`)

**What it measures.** The annual average exchange rate of the Indian rupee against the US dollar, used for every calendar-year conversion in the book.

**Definition and unit.** Rupees per US dollar. Three independent series sit in separate columns: the Reserve Bank of India (RBI) Handbook (1987-2025), the Federal Reserve's G.5A noon buying rates (1973-2025) and the Penn World Table (1950-2023). A preferred column takes RBI where available, then the Federal Reserve, then the Penn World Table.

**Coverage.** 1950-2025 (76 years).

**Sources.** S0155, S0320, S0319.

**Caveats.** The series agree within 0.3 per cent in the overlap years checked. The rupee was pegged for much of the period, and the regime dates in the file's header (fixed parity from 1949, devaluation of June 1966, sterling link, basket peg, unified market rate from 1993) are from background knowledge and not yet sourced. Annual averages hide the within-year jumps of 1966 and July 1991.

| Year | Rupees per dollar (preferred) | Series used |
|---|---|---|
| 1950 | 4.76 | Penn World Table |
| 1960 | 4.76 | Penn World Table |
| 1966 | 6.36 | Penn World Table (devaluation in June) |
| 1970 | 7.50 | Penn World Table |
| 1975 | 8.41 | Federal Reserve |
| 1980 | 7.89 | Federal Reserve |
| 1985 | 12.33 | Federal Reserve |
| 1991 | 22.69 | RBI (devaluations of 1 and 3 July) |
| 2000 | 44.94 | RBI |
| 2010 | 45.73 | RBI |
| 2020 | 74.10 | RBI |
| 2025 | 87.17 | RBI |

Full file: `book/research/data/inr_usd.csv`.

### Rupees per US dollar, fiscal year (`inr_usd_fy.csv`)

**What it measures.** The exchange rate averaged over the Indian fiscal year, and the rate at its end, used for converting fiscal-year flows such as export earnings and company revenue.

**Definition and unit.** Rupees per US dollar, annual average and end-year (31 March) rate, as published in RBI Handbook Table 133.

**Coverage.** FY1986-87 to FY2025-26.

**Sources.** S0155.

**Caveats.** The basis changes from official rates (to FY1991-92) to indicative market rates and then RBI and FBIL reference rates. Averages are used for flows, end-year rates for stocks. No RBI series was obtained for fiscal years before FY1986-87.

| Fiscal year | Average | End-year (31 March) |
|---|---|---|
| FY1986-87 | 12.78 | 12.89 |
| FY1991-92 | 24.47 | 31.23 |
| FY1995-96 | 33.45 | 34.35 |
| FY2000-01 | 45.68 | 46.64 |
| FY2005-06 | 44.27 | 44.61 |
| FY2008-09 | 45.99 | 50.95 |
| FY2013-14 | 60.50 | 60.10 |
| FY2015-16 | 65.47 | 66.33 |
| FY2020-21 | 74.23 | 73.50 |
| FY2022-23 | 80.36 | 82.22 |
| FY2024-25 | 84.58 | 85.58 |
| FY2025-26 | 88.31 | 94.65 |

Full file: `book/research/data/inr_usd_fy.csv`.

### Consumer prices in India, calendar year (`cpi_india_cy.csv`)

**What it measures.** A long consumer price index for India, used to deflate calendar-year rupee figures and any figure before FY1993-94.

**Definition and unit.** OECD Main Economic Indicators series for India, index 2015 = 100. A multiplier column converts a nominal rupee value of a given year into 2024 rupees.

**Coverage.** 1957-2024.

**Sources.** S0321 (OECD via FRED).

**Caveats.** The OECD documentation was not read. The series moves with the Consumer Price Index for Industrial Workers (CPI-IW) rather than the newer CPI Combined, and is treated here as CPI-IW-based. Base changes in the underlying national index (1960, 1982, 2001, 2016) are linked by the OECD by a method not documented in the file.

| Year | Index (2015 = 100) | Multiply by, for 2024 rupees |
|---|---|---|
| 1960 | 1.70 | 91.71 |
| 1970 | 3.09 | 50.41 |
| 1975 | 5.40 | 28.89 |
| 1980 | 6.55 | 23.81 |
| 1985 | 10.23 | 15.25 |
| 1991 | 17.59 | 8.87 |
| 1995 | 25.40 | 6.14 |
| 2000 | 36.57 | 4.27 |
| 2005 | 44.44 | 3.51 |
| 2010 | 67.29 | 2.32 |
| 2015 | 100.00 | 1.56 |
| 2024 | 155.99 | 1.00 |

Full file: `book/research/data/cpi_india_cy.csv`.

### Consumer Price Index for Industrial Workers, fiscal year (`cpi_iw.csv`)

**What it measures.** The Labour Bureau's CPI-IW, the index the book's house rules prefer for deflating fiscal-year rupee series.

**Definition and unit.** All-India general index, fiscal-year average, as reproduced in RBI Handbook Table 34. The file gives the value on the base in force each year and a series linked to 2016 = 100 with the published linking factors (4.63 and 2.88), plus a multiplier into FY2025-26 rupees.

**Coverage.** FY1993-94 to FY2025-26.

**Sources.** S0156 via S0155.

**Caveats.** Bases change in FY2005-06 and FY2020-21. Values on the older bases are published as whole numbers, so the linked series carries rounding error of up to about 0.2 per cent. Earlier years are not in this table; `cpi_india_cy.csv` covers them by calendar year.

| Fiscal year | Base | Published value | Linked (2016 = 100) | Multiply by, for FY2025-26 rupees |
|---|---|---|---|---|
| FY1993-94 | 1982 | 258 | 19.35 | 7.60 |
| FY1995-96 | 1982 | 313 | 23.47 | 6.26 |
| FY2000-01 | 1982 | 444 | 33.30 | 4.41 |
| FY2005-06 | 2001 | 117 | 40.62 | 3.62 |
| FY2008-09 | 2001 | 145 | 50.35 | 2.92 |
| FY2010-11 | 2001 | 180 | 62.50 | 2.35 |
| FY2013-14 | 2001 | 236 | 81.94 | 1.79 |
| FY2015-16 | 2001 | 265 | 92.01 | 1.60 |
| FY2020-21 | 2016 | 118 | 118.00 | 1.25 |
| FY2022-23 | 2016 | 131 | 131.00 | 1.12 |
| FY2024-25 | 2016 | 143 | 143.00 | 1.03 |
| FY2025-26 | 2016 | 147 | 147.00 | 1.00 |

Full file: `book/research/data/cpi_iw.csv`.

### US consumer prices (`us_cpi_u.csv`)

**What it measures.** The US Consumer Price Index for All Urban Consumers, used to express dollar figures in 2025 dollars.

**Definition and unit.** BLS series CUUR0000SA0, US city average, all items, annual average, index 1982-84 = 100. A multiplier converts a nominal dollar value of a given year into 2025 dollars. Fiscal-year dollar figures elsewhere are deflated with a weighted average of the two calendar years they span, as each file states.

**Coverage.** 1950-2025. 2026 is omitted as a partial year.

**Sources.** S0157.

**Caveats.** The 2025 average rests on 11 months, because October 2025 is missing from the BLS data.

| Year | CPI-U (1982-84 = 100) | Multiply by, for 2025 dollars |
|---|---|---|
| 1950 | 24.1 | 13.36 |
| 1960 | 29.6 | 10.88 |
| 1970 | 38.8 | 8.30 |
| 1975 | 53.8 | 5.98 |
| 1980 | 82.4 | 3.91 |
| 1985 | 107.6 | 2.99 |
| 1991 | 136.2 | 2.36 |
| 2000 | 172.2 | 1.87 |
| 2005 | 195.3 | 1.65 |
| 2010 | 218.1 | 1.48 |
| 2020 | 258.8 | 1.24 |
| 2025 | 321.9 | 1.00 |

Full file: `book/research/data/us_cpi_u.csv`.

## Computers and early computing education

### Computers installed in India (`computers_installed.csv`)

**What it measures.** How many computers India had, from the first counts in the 1960s to 2010.

**Definition and unit.** Machines, as counted by each source. The scope differs from row to row: all digital computers, IBM installations, ECIL sales, personal computers in use.

**Coverage.** Points from 1964 to 2010. A table of separate counts, not a series.

**Sources.** S0007, S0001, S0020, S0003, S0237.

**Caveats.** Definitions change between rows. The sources disagree on IBM's installed base in 1977-78 (over 150 machines in Rajaraman's account; 800 installations maintained by CMC in Dataquest's), probably because they count different things. The 1990 figure does not define its scope.

| Date | Measure | Value |
|---|---|---|
| End 1964 | Digital computers in India | 15 |
| 1965 | Computers in India (Committee on Automation) | 30 |
| 1968 | Computers in India | 88 |
| 1967-71 | Computers introduced (5 referred for labour screening) | 94 |
| 1970 | IBM 1401 installations | about 80 |
| Aug 1971 | Computers in India (government 10, public sector 39, private 55, research and education 36) | 140 |
| 1971-78 | ECIL computers sold (4 to private buyers) | 98 |
| 1974 | IBM share of installations | 65% of 217 |
| 1977-78 | IBM installations (disputed) | over 150 |
| 1978 | Computers in India | fewer than 1,000 |
| 1990 | Computers in India | 80,000 |
| 2010 | Personal computers in use | over 60 million |

Full file: `book/research/data/computers_installed.csv`.

### Early computer-science degrees (`cs_degrees_early.csv`)

**What it measures.** When computer science began as a degree subject in India, and the few counts of graduates available before 2010.

**Definition and unit.** A table of dated events with counts where the source gives them; persons or programmes.

**Coverage.** 1965-2010.

**Sources.** S0001 (Rajaraman 2012), S0003 (Bassett 2009), S0043.

**Caveats.** Sources disagree on the start of Kanpur's master's teaching (1965 or 1966) and on the rank of the last student admitted to its first B.Tech class (44 or 40). Rajaraman's 1998 figure of 135,000 'engineering students' is probably an intake, not a count of all students.

| Date | Event or count | Value |
|---|---|---|
| 1965 | IIT Kanpur M.Tech with a computer-science option, first CS teaching as a discipline (1966 in Rajaraman's chronology) | |
| 1978 | IIT Kanpur's first B.Tech in computer science, the first at any IIT | 20 seats |
| 1978-80 | Other IITs start CS degrees | |
| 1980 | Rajaraman panel proposes the Master of Computer Applications (MCA) | |
| 1980s | Institutions fully funded to start the MCA | 10 |
| 1998 | MCA graduates | about 7,000 |
| 1998 | Engineering students (probably intake) | about 135,000 |
| 2010 | MCA graduates | about 120,000 |

Full file: `book/research/data/cs_degrees_early.csv`.

## Engineering education and graduates

### Engineering colleges, intake, enrolment and vacancy (`engineering_intake.csv`)

**What it measures.** The capacity of India's engineering education: how many colleges, how many approved places, how many students took them up and how many places stayed empty.

**Definition and unit.** Institutions; persons; per cent. 'Approved intake' is the maximum admissions the All India Council for Technical Education (AICTE) approves, excluding supernumerary seats, at AICTE institutions only (the IITs are outside AICTE). First-year enrolment at all levels is the figure given to the Lok Sabha. Vacancy is the share of approved places left empty.

**Coverage.** College counts 1950-51 to 2005-06; intake and enrolment 2012-13 to 2021-22; IIT seats 1978.

**Sources.** S0248 (statistics ministry), S0323 (Lok Sabha reply), S0267 (Avanti Fellows analysis of AICTE and AISHE data), S0324, S0001.

**Caveats.** College counts are institutions, not students. There is a gap in all series between 2006 and 2012. AICTE's 2022-23 data are an incomplete load and are not used, and its data on graduates placed in jobs are unusable. A 2023 press table of 'BTech' intake does not match either official series and is kept apart at low confidence.

| Year | Colleges | Approved intake, all levels | Approved intake, undergraduate | First-year enrolment, all levels | Undergraduate seats empty |
|---|---|---|---|---|---|
| 1950-51 | 31 | | | | |
| 1960-61 | 76 | | | | |
| 1970-71 | 107 | | | | |
| 1980-81 | 149 | | | | |
| 1990-91 | 289 | | | | |
| 1997-98 | 486 | | | | |
| 2000-01 | 678 | | | | |
| 2005-06 | 1,562 | | | | |
| 2012-13 | | 2,695,333 | 1,549,000 | 1,751,538 | 37.6% |
| 2014-15 | | | 1,705,000 (peak) | 1,739,357 | |
| 2016-17 | | | | 1,559,229 | 49.5% |
| 2021-22 | | 2,366,728 | 1,253,000 | | 34.1% |

Full file: `book/research/data/engineering_intake.csv`.

### Engineering graduates (`engineering_graduates.csv`)

**What it measures.** How many engineers India produces each year, a much-quoted and poorly measured figure.

**Definition and unit.** Persons per year, with the measure stated on each row; four-year degrees and three-year diplomas are kept apart.

**Coverage.** 2004 and about 2013 only. The official AISHE out-turn tables were not obtained.

**Sources.** S0213 (Duke University study, 2005), S0153 (Aspiring Minds, 2014), S0001.

**Caveats.** There is no consistent series. The 2004 figures are a Nasscom projection reported by the Duke team. The 600,000 figure is Aspiring Minds' and is unsourced. Rajaraman's 1.3 million is kept only to document a dispute: he calls it both students and annual graduates, and it is most likely intake or seats.

| Period | Measure | Value |
|---|---|---|
| 2004 | Bachelor's degrees in engineering, CS and IT (Nasscom projection) | 112,000 |
| 2004 | Three-year diplomas in the same fields (Nasscom projection) | 103,000 |
| 2004 | Total, degrees and diplomas | 215,000 |
| c. 2013 | Engineers graduating annually (Aspiring Minds, unsourced) | 600,000 |
| c. 2010 | Rajaraman's 1.3 million (probably intake; not graduates) | 1,300,000 |

Full file: `book/research/data/engineering_graduates.csv`.

### Women in engineering education (`women_engineering_enrolment.csv`)

**What it measures.** Women's share of engineering students and graduates.

**Definition and unit.** Per cent, with the base stated on every row: AICTE first-year undergraduate enrolment, AISHE enrolment across all years of study, or AISHE degrees awarded. One workforce figure is kept for contrast.

**Coverage.** 2012-13, 2020-21 and 2021-22 points; no consistent annual series.

**Sources.** S0325 (Society of Women Engineers, citing AICTE and AISHE), S0152, S0117.

**Caveats.** The bases differ in scope and are never combined. A widely reported rise from 8 per cent (2016) to 19.72 per cent (2021) appears to concern the IITs and NITs, not all colleges; its scope could not be verified and it is excluded.

| Year | Base | Women |
|---|---|---|
| 2012-13 | AICTE first-year undergraduate engineering enrolment | 33.7% (303,229) |
| 2020-21 | AICTE first-year undergraduate engineering enrolment | 30.2% (200,865) |
| 2020-21 | AISHE B.Tech enrolment, all years | 28.7% |
| 2021-22 | AISHE undergraduate computer engineering enrolment | 34.2% |
| 2021-22 | AISHE undergraduate computer engineering degrees awarded | 38.5% (83,696) |
| 2001-02 | Software professionals in industry (Nasscom; contrast only) | 21% |

Full file: `book/research/data/women_engineering_enrolment.csv`.

### 'Employability' estimates (`employability_tests.csv`)

**What it measures.** The share of tested engineering students who met a test vendor's or consultant's benchmark for particular jobs.

**Definition and unit.** Per cent of the tested sample meeting the vendor's own benchmark for a role. This is not a labour-market outcome: it does not measure whether graduates found work.

**Coverage.** Aspiring Minds reports of 2014 and 2016; one McKinsey figure of about 2005 as reported by the Duke study.

**Sources.** S0153 (Aspiring Minds National Employability Report), S0213.

**Caveats.** Aspiring Minds sells the AMCAT test it uses, and the benchmarks are its own. Samples and benchmarks differ between editions, and press reports often mix them. The McKinsey study itself was not read. Every use names the vendor and the role.

| Report | Role or measure | Meeting benchmark |
|---|---|---|
| 2014 (2013 graduates) | Software engineer, IT services ('trainable within 3 to 6 months') | 18.43% |
| 2014 | Software engineer, IT products | 3.21% |
| 2014 | Non-functional role such as BPO | 39.84% |
| 2016 | Software engineer, IT services | 17.91% |
| 2016 | Software engineer, IT products | 3.67% |
| 2016 | Business process outsourcing | 40.57% |
| 2016 | Start-up software engineering | 3.84% |
| 2016 | 'Software-industry ready' (programming) | 4.51% |
| c. 2005 | Indian engineers able to 'compete in the global outsourcing arena' (McKinsey, via Duke) | 25% |

Samples: over 120,000 students at 520+ colleges (2014); over 150,000 at 650+ colleges (2016). Full file: `book/research/data/employability_tests.csv`.

### Graduate unemployment (`graduate_unemployment.csv`)

**What it measures.** Unemployment among Indian graduates, with a few comparison points.

**Definition and unit.** Unemployment rate, per cent of the labour force. Indian rows use the Periodic Labour Force Survey (PLFS), usual status (principal and subsidiary), persons aged 15 and over with graduate education, unless stated. PLFS years run July to June.

**Coverage.** India 2019-20 to 2023-24; one all-persons and one under-25 point; US 2025 points.

**Sources.** S0326 (Press Information Bureau), S0327, S0328, S0329 (statistics ministry), S0136.

**Caveats.** PLFS rates for 2017-18 and 2018-19 were not obtained (a register note giving 17.2 per cent for 2017-18 was wrong; that is the 2019-20 figure). The 2023-24 graduate rate of 11.2 per cent comes from a press report and conflicts with 13.0 per cent in another note; it is low confidence. PLFS is never joined to the older NSSO surveys. The under-25 figure uses a different method and was not read in the original. The US figures are as cited in a US presidential proclamation.

| Year | Country | Population | Rate |
|---|---|---|---|
| 2019-20 | India | Graduates aged 15+ (PLFS) | 17.2% |
| 2020-21 | India | Graduates aged 15+ (PLFS) | 15.5% |
| 2021-22 | India | Graduates aged 15+ (PLFS) | 14.9% |
| 2022-23 | India | Graduates aged 15+ (PLFS) | 13.4% |
| 2023-24 | India | Graduates aged 15+ (PLFS; press report, disputed) | 11.2% |
| 2023-24 | India | All persons aged 15+ (PLFS) | 3.2% |
| 2023 | India | Graduates under 25 (State of Working India 2026) | 39.3% |
| 2025 | United States | Recent graduates aged 22-27, computer science (NY Fed) | 6.1% |
| 2025 | United States | Recent graduates aged 22-27, computer engineering (NY Fed) | 7.5% |

Full file: `book/research/data/graduate_unemployment.csv`.

### Emigration of IIT graduates (`iit_emigration.csv`)

**What it measures.** The share of IIT graduates and top entrance-exam scorers who went abroad.

**Definition and unit.** Share of a cohort living or working abroad, in per cent or as stated.

**Coverage.** 1970s IIT Bombay cohorts; the JEE 2010 cohort.

**Sources.** S0003 (Bassett), S0046 (Sukhatme survey), S0172 (Choudhury, Ganguli and Gaulé, NBER Working Paper 31308, 2023).

**Caveats.** Institutions, cohorts and methods differ, so the rows cannot be read as a trend. The second row is a secondary report of the Sukhatme survey.

| Cohort | Measure | Value |
|---|---|---|
| 1973-1977 graduates | IIT Bombay electrical engineering graduates living abroad | slightly over 40% |
| Since 1970 | IIT Bombay graduates settled abroad (as reported in Nature, 1993) | about 3 in 10 |
| JEE 2010, top 1,000 | Migrated abroad by about 2020 | 36% |
| JEE 2010, top 100 | Migrated abroad | 62% |
| JEE 2010 cohort | Extra migration for graduate school at the original 'Top 5' IITs | +5 percentage points |

Full file: `book/research/data/iit_emigration.csv`.

### Indian students in the United States (`indian_students_us.csv`)

**What it measures.** How many students from India were enrolled in American higher education, including those on post-study work.

**Definition and unit.** Persons, academic year, from the Institute of International Education's Open Doors India fact sheet. A level split is given for the latest two years.

**Coverage.** 2017/18 to 2024/25. Earlier Open Doors years were not obtained.

**Sources.** S0158 (IIE is a non-profit with State Department support).

**Caveats.** Totals include Optional Practical Training (OPT), the post-study work route, which rose from 97,556 to 143,740 in the last year; graduate students fell 9.5 per cent in 2024/25 while the total rose.

| Academic year | Total | Undergraduate | Graduate | OPT |
|---|---|---|---|---|
| 2017/18 | 196,271 | | | |
| 2018/19 | 202,014 | | | |
| 2019/20 | 193,124 | | | |
| 2020/21 | 167,582 | | | |
| 2021/22 | 199,182 | | | |
| 2022/23 | 268,923 | | | |
| 2023/24 | 331,602 | 36,053 | 196,567 | 97,556 |
| 2024/25 | 363,019 | 40,135 | 177,892 | 143,740 |

Full file: `book/research/data/indian_students_us.csv`.

## The industry

### Software and services exports (`software_exports.csv`)

**What it measures.** India's export earnings from software and related services, in three families of series that measure different things.

**Definition and unit.** US$ million, nominal, with real columns in 2025 dollars (deflated by `us_cpi_u.csv`). Family one is early gross foreign-exchange earnings from software: Heeks (citing his own research and Dataquest) and Bhatnagar (via Rajaraman). Family two is Nasscom's industry exports, whose scope widens over time from 'software exports' to 'IT-BPO exports' to 'technology industry' exports including business process management and engineering services. Family three is the RBI: a survey of software and IT services exporters (2009-11) and the balance-of-payments 'software services' receipts (from FY2000-01).

**Coverage.** 1980 to FY2025-26, with gaps (no series for FY1998-99 to FY1999-2000 except one Nasscom point). Heeks rows for 1980-1987 are calendar years; all others are fiscal years.

**Sources.** S0085, S0001, S0109, S0107, S0140, S0306, S0106, S0155 (six editions of the RBI Handbook).

**Caveats.** The families are not reconciled and must not be joined. Heeks's figures are gross; net foreign-exchange earnings were estimated at about 40 per cent of gross. Nasscom's figures are a lobby group's and change definition; its FY2025-26 figure is an estimate. The RBI balance-of-payments series is compiled with Nasscom data as a controlling total, so it is not wholly independent. The FY2025-26 RBI value is preliminary. Revisions between RBI editions were small.

| Period | Heeks | Bhatnagar | Nasscom (lobby) | RBI survey | RBI balance of payments | RBI BoP, 2025 dollars |
|---|---|---|---|---|---|---|
| 1980 | 4.0 | | | | | |
| 1984 | 25.3 | | | | | |
| FY1990-91 | 131.2 | 128 | | | | |
| FY1995-96 | 668.0 | 734 | | | | |
| FY1997-98 | 1,650.0 | 1,759 | | | | |
| FY1998-99 | | | 2,650 (software exports) | | | |
| FY2000-01 | | | | | 6,341 | 11,771 |
| FY2005-06 | | | | | 23,600 | 38,592 |
| FY2010-11 | | | | 47,600 | 53,100 | 77,784 |
| FY2015-16 | | | | | 74,153 | 100,406 |
| FY2020-21 | | | | | 99,997 | 122,945 |
| FY2025-26 | | | 246,000 (estimate) | | 203,675 (preliminary) | |

Full file: `book/research/data/software_exports.csv`.

### Industry employment (`industry_workforce.csv`)

**What it measures.** How many people the Indian software and IT industry employs.

**Definition and unit.** Persons, point estimates in separate columns by source. The industry's scope widens over time, from 'software professionals' to 'IT-BPO' to the 'technology industry' including business process management, engineering services, products and global capability centres.

**Coverage.** FY1989-90 to FY2025-26, sparse points only; no annual series was obtained.

**Sources.** S0259 (Infosys prospectus, quoting Nasscom), S0254, S0001, S0107, S0140, S0306, S0316 (NITI Aayog).

**Caveats.** Almost every figure is Nasscom's, a lobby group's estimate on the definition current at the time; FY2023-24 was restated upwards after a 2024 reassessment of global capability centres. NITI Aayog's range is an all-sector 'tech workforce' including technology jobs outside the industry and must not be compared with Nasscom's. PLFS-based counts were not obtained.

| Period | Measure | Persons |
|---|---|---|
| FY1989-90 | Software professionals (Nasscom) | 56,000 |
| 1996 | Software professionals (Nasscom) | 160,000 |
| FY1997-98 | Software professionals (Nasscom) | 200,000 |
| FY2007-08 | IT-BPO direct employees (Nasscom, 'nearly 2 million') | 2,000,000 |
| 2010 | Direct employment in IT (Rajaraman, from Nasscom) | 2,400,000 |
| FY2023-24 | Technology industry direct employees (Nasscom, restated) | 5,670,000 |
| 2023 | All-sector tech workforce (NITI Aayog; not comparable) | 7.5-8 million |
| FY2024-25 | Technology industry (Nasscom estimate; revised to 5,815,000) | 5,800,000 |
| FY2025-26 | Technology industry (Nasscom estimate; net additions 135,000) | 5,950,000 |

Full file: `book/research/data/industry_workforce.csv`.

### The largest firms (`top_firms.csv`)

**What it measures.** Revenue, headcount and revenue per employee at selected Indian-heritage IT firms.

**Definition and unit.** One row per firm-year. Revenue in US$ million, nominal and in 2025 dollars; Wipro also in rupees, converted at the RBI fiscal-year average rate (the book's conversion, not Wipro's). Employees at year end. Revenue per employee in US$ thousand, using the average of opening and closing headcount. Infosys, Wipro and TCS years end on 31 March (the year shown is the calendar year in which the fiscal year ends); Cognizant uses calendar years.

**Coverage.** Infosys FY1999-FY2026 with gaps; Wipro FY2016-FY2026; Cognizant 2001-2025 with headcount gaps; TCS headcount points.

**Sources.** Infosys 20-F and F-1 filings (S0322, S0264-S0266, S0270-S0272, S0287-S0291, S0296, S0297); Wipro 20-F (S0292, S0298); Cognizant 10-K (S0192, S0275-S0277, S0293, S0299); SEC XBRL company facts; TCS (S0160, S0139, S0310); S0155; S0157.

**Caveats.** Infosys reported under US GAAP to FY2008 and IFRS from FY2009. Wipro states headcount as 'more than' a round number and revises it between filings. Cognizant's 2001-02 counts cover technical professionals only. TCS and HCLTech revenue were not compiled (the TCS site was blocked to the research tools); the FY2026 TCS headcount is derived.

| Firm | Year | Revenue, US$m | Revenue, 2025 US$m | Employees | Revenue per employee, US$k |
|---|---|---|---|---|---|
| Infosys | FY1999 | 121 | 238 | 3,800 | |
| Infosys | FY2005 | 1,592 | 2,691 | 36,800 | 52.5 |
| Infosys | FY2009 | 4,663 | 6,979 | 104,900 | 47.6 |
| Infosys | FY2012 | 6,994 | 9,959 | 150,000 | |
| Infosys | FY2020 | 12,780 | 16,044 | 242,371 | 54.3 |
| Infosys | FY2023 | 18,212 | 19,831 | 343,234 | 55.4 |
| Infosys | FY2024 | 18,562 | 19,469 | 317,240 | 56.2 |
| Infosys | FY2026 | 20,158 | | 328,594 | 61.8 |
| Wipro | FY2026 | 10,489 | | more than 240,000 | 44.6 |
| Cognizant | 2012 | 7,347 | 10,302 | 156,700 | 49.9 |
| Cognizant | 2025 | 21,108 | 21,108 | 351,600 (256,900 in India) | 61.3 |
| TCS | FY2025 | | | 607,979 | |

Full file: `book/research/data/top_firms.csv`.

### Recruitment and fresher hiring (`fresher_hiring.csv`)

**What it measures.** How many people applied to, were interviewed by and were offered jobs at the largest firms, and how many new graduates were hired.

**Definition and unit.** Persons. Infosys rows are the company's annual recruitment statistics as filed with the SEC. From FY2003-04 'offers' counts all offers of employment, experienced (lateral) and fresher alike. Offers per 1,000 applications is calculated for this book. Other rows are fresher-specific press figures, each labelled.

**Coverage.** Infosys FY1997-98 to FY2025-26 with gaps (FY1998-99 to FY1999-2000, FY2002-03, FY2005-06 to FY2006-07, FY2010-11, FY2012-13 to FY2018-19); TCS, HCLTech and Infosys press points for FY2022-23 to FY2026-27.

**Sources.** Infosys filings (S0259, S0322, S0260, S0270, S0264, S0265, S0271, S0272, S0266, S0287-S0291, S0296, S0297); press (S0309, S0310, S0138, S0139, S0133).

**Caveats.** Offers, hires and joiners are different measures and must not be compared across columns. 'Tested' is not reported from FY2011-12. Infosys used 'received' and 'screened' for applications in different filings. The press figures are low to medium confidence; the Infosys figures of 50,000 and 11,900 fresh graduates for FY2022-23 and FY2023-24 come from a trade site citing other reports. The TCS figure for the July-September 2026 quarter postdates the book's research cut-off.

| Fiscal year (Infosys) | Applications | Interviewed | Offers | Offers per 1,000 applications |
|---|---|---|---|---|
| FY1997-98 | 70,870 | 5,800 | 1,790 | 25.3 |
| FY2000-01 | 385,200 | 20,800 | 7,650 | 19.9 |
| FY2001-02 | 193,640 | 6,730 | 1,710 | 8.8 |
| FY2004-05 | 1,348,800 | 36,600 | 14,500 | 10.8 |
| FY2007-08 | 885,000 | 97,600 | 46,300 | 52.3 |
| FY2008-09 | 488,700 | 46,600 | 16,900 | 34.6 |
| FY2011-12 | 622,970 | 60,860 | 41,460 | 66.6 |
| FY2019-20 | 2,141,373 | 150,130 | 83,319 | 38.9 |
| FY2020-21 | 1,427,618 | 135,216 | 48,029 | 33.6 |
| FY2021-22 | 5,866,636 | 523,385 | 222,500 | 37.9 |
| FY2023-24 | 2,436,929 | 194,367 | 26,975 | 11.1 |
| FY2025-26 | 5,884,480 | 450,901 | 87,286 | 14.8 |

Press points on freshers: TCS 'reportedly' hired over 44,000 in FY2025-26 and had made 25,000 fresher offers for FY2026-27 by April 2026, with about 14,000 joining in April-June 2026 and 10,000 in July-September; HCLTech hired over 11,000 graduates in FY2025-26; Infosys planned to add 20,000 freshers in FY2026-27. Full file: `book/research/data/fresher_hiring.csv`.

### Starting pay (`fresher_pay.csv`)

**What it measures.** The annual pay of new graduates joining Indian IT services firms.

**Definition and unit.** Rupees lakh a year, nominal, as reported; medians, single-firm packages and quoted ranges are different measures and labelled. A real column gives the value, or the midpoint of a range, in 2024 rupees, deflated by `cpi_india_cy.csv`.

**Coverage.** Points from 2007 to 2026; no consistent series. Years after 2024 are not deflated.

**Sources.** S0330, S0331, S0332, S0333, S0334, S0153.

**Caveats.** Offer, cost-to-company and take-home pay differ. Premium tracks (such as TCS 'Digital' or HCLTech 'Elite') are excluded. The 2007 TCS figure rests on one anecdotal source. The Moneycontrol study's method was not read. The Aspiring Minds figures are a vendor's estimates.

| Year | Measure | Rs lakh a year | 2024 Rs lakh |
|---|---|---|---|
| 2007 | TCS trainee package (single anecdotal source) | 3.16 | 9.86 |
| 2012 | Median fresher pay, large IT firms (Moneycontrol study) | 2.45 | 4.77 |
| 2014 | STEM graduate starting salaries (TeamLease Digital estimate) | 2.0-2.5 | 3.72 |
| 2015 | Median salary (Aspiring Minds, vendor estimate) | 2.82 | 4.40 |
| 2016 | Median salary (Aspiring Minds, vendor estimate) | 3.13 | 4.65 |
| 2022 | Median fresher pay, large IT firms (Moneycontrol study) | 3.55 | 3.89 |
| 2022 | Infosys fresher pay (annual report, as reported) | 3.6 | 3.94 |
| 2022 | Freshers at large firms (T.V. Mohandas Pai) | 3.5-4.0 | 4.11 |
| 2025 | STEM graduate starting salaries (TeamLease Digital estimate) | 3.0-3.5 | |
| 2025 | Wipro entry-level salaries (company) | 3.0-4.0 | |
| 2026 | TCS trainee package | 3.36 | |

Full file: `book/research/data/fresher_pay.csv`.

### Attrition and women's share, by firm (`firm_women_attrition.csv`)

**What it measures.** The share of staff leaving each year, and the share of women in the workforce, at firms that report them.

**Definition and unit.** Per cent. Each row states the firm's own definition: total or voluntary attrition, with or without subsidiaries, IT services only, trailing twelve months.

**Coverage.** Infosys attrition FY2005-06 to FY2011-12 and FY2019-20 to FY2023-24, women FY2023-24; Cognizant 2020-2025; TCS FY2024-25 and the quarter to September 2026.

**Sources.** Infosys 20-F (S0265, S0271, S0272, S0266, S0291) and 6-K results filings (S0381); Cognizant 10-K (S0293, S0192, S0299); TCS (S0160, S0310).

**Caveats.** Definitions differ between firms and change over time; rows with different definitions must not be compared. Cognizant switched its headline measure in its 10-K for 2023 from total to voluntary attrition in technology services, so 2022 appears on both bases. The Infosys women's figure is 'nearly 40%'.

| Firm | Period | Attrition | Definition | Women |
|---|---|---|---|---|
| Infosys | FY2005-06 | 11.2% | Comparable, excluding BPO and subsidiaries | |
| Infosys | FY2007-08 | 13.4% | Comparable, excluding BPO and subsidiaries | |
| Infosys | FY2010-11 | 17.0% | Twelve months to 31 March | |
| Infosys | FY2011-12 | 14.7% | Twelve months to 31 March | |
| Infosys | FY2019-20 | 15.1% | Voluntary, standalone, fourth quarter | |
| Infosys | FY2020-21 | 15.2% | Voluntary, IT services, fourth quarter annualised | |
| Infosys | FY2021-22 | 27.7% | Voluntary, last twelve months | |
| Infosys | FY2022-23 | 20.9% | Voluntary, last twelve months, IT services | |
| Infosys | FY2023-24 | 12.6% | Voluntary, last twelve months, IT services | 39.3% |
| Cognizant | 2020 | 20.6% | Total | 36% |
| Cognizant | 2021 | 30.8% | Total | 38% |
| Cognizant | 2022 | 31.7% | Total | 38% |
| Cognizant | 2022 | 25.6% | Voluntary, technology services | |
| Cognizant | 2023 | 13.8% | Voluntary, technology services | 38% |
| Cognizant | 2025 | 13.9% | Voluntary, technology services | 39% |
| TCS | FY2024-25 | 13.3% | Last twelve months, IT services | 35.2% |

Full file: `book/research/data/firm_women_attrition.csv`.

### Foreign firms' Indian headcount (`foreign_firm_india_headcount.csv`)

**What it measures.** How many people foreign-headquartered IT firms employ in India.

**Definition and unit.** Employees in India, as reported by the firm or by the press from company statements; persons.

**Coverage.** Sparse points, 2005-2025.

**Sources.** S0193, S0194, S0170, S0293, S0192, S0299.

**Caveats.** Most firms do not disclose Indian headcount. The IBM and Accenture points are press reports of company statements, and the Accenture figure was a plan.

| Date | Firm | Employees in India | Total employees |
|---|---|---|---|
| Early 2005 | IBM | 23,000 | |
| Early 2006 | IBM | 39,000 | |
| Feb 2007 | IBM | 53,000 | about 300,000 |
| Aug 2007 (planned) | Accenture | 35,000 | 160,000 |
| 2021 | EPAM | 4,349 | 52,617 (delivery) |
| 2024 | EPAM | 10,072 | about 55,100 (delivery) |
| 2022 | Cognizant | 258,500 | 355,300 |
| 2023 | Cognizant | 254,000 | 347,700 |
| 2024 | Cognizant | 241,500 | 336,800 |
| 2025 | Cognizant | 256,900 | 351,600 |

Full file: `book/research/data/foreign_firm_india_headcount.csv`.

### Global capability centres (`gcc.csv`)

**What it measures.** The number, staff and revenue of multinational companies' own centres in India: research and development centres in the 2000s, 'global capability centres' (GCCs) in the 2020s.

**Definition and unit.** Centres; persons; US$ billion, as each source defines them. The 2008 'MNC R&D centre' is narrower than the later GCC, which includes back-office captives. GCC 'revenue' measures work done for the parent, not sales.

**Coverage.** 2004 and 2007 (new centres), 2008, FY2023-24 and FY2025-26, with projections and a state target kept separate.

**Sources.** S0207 (Zinnov via EE Times), S0141, S0317 (Nasscom-Zinnov via Reuters), S0318 (Zinnov-Nasscom via Business Today), S0140, S0204.

**Caveats.** Every figure comes from Nasscom, the industry's lobby group, or Zinnov, a consultancy that sells to GCCs; both have an interest in a growing count. Nasscom restated GCC revenue in September 2024. The 2004-08 figures were read through a summary. Projections and the Karnataka target are not outcomes.

| Period | Measure | Centres | Employees | Revenue, US$bn |
|---|---|---|---|---|
| 2004 | New MNC R&D centres opened (Zinnov) | 93 | | |
| 2007 | New MNC R&D centres opened (Zinnov) | 24 | | |
| 2008 | MNC R&D centres (Zinnov) | 594 | 146,760 | |
| FY2023-24 | GCCs (Nasscom-Zinnov) | about 1,700 companies (2,975 units) | 1,900,000 | 64.6 |
| FY2025-26 | GCCs (Zinnov-Nasscom) | 2,117 | 2,360,000 | 98.4 |
| 2030 | PROJECTION made in 2024 (Nasscom-Zinnov) | 2,100-2,200 | 2.5-2.8 million | 99-105 |
| 2029 | TARGET: new GCCs sought by Karnataka's policy | 500 | | |

Full file: `book/research/data/gcc.csv`.

### Start-up funding (`startup_funding.csv`)

**What it measures.** Venture funding raised by Indian start-ups each year.

**Definition and unit.** US$ billion, calendar year, as reported by each data vendor.

**Coverage.** 2021-2024.

**Sources.** S0147 (Tracxn via The Week; Inc42).

**Caveats.** Vendors define 'start-up' and 'tech' differently, and their series must not be joined. Tracxn's 2021 figure is implied from its reported 31 per cent fall in 2022. Some rows were read through a summary.

| Year | Vendor | US$ billion |
|---|---|---|
| 2021 | Tracxn (implied) | about 37 |
| 2021 | Inc42 | about 42 |
| 2021 | Other vendor, as reported | 43.5 |
| 2022 | Tracxn | 25.7 |
| 2023 | Tracxn | 10.8 |
| 2024 | Tracxn | 11.1 |

Full file: `book/research/data/startup_funding.csv`.

### Unified Payments Interface (`upi.csv`)

**What it measures.** The volume and value of payments made through UPI, the state-backed mobile payments network.

**Definition and unit.** Annual (April-March) volume in billion transactions and value in Rs lakh crore (Rs trillion), from the RBI's payment system indicators.

**Coverage.** FY2016-17 to FY2023-24, plus one monthly point for August 2025.

**Sources.** S0155 (RBI Handbook, 2021, 2025 and 2026 editions), S0129.

**Caveats.** UPI began in FY2016-17, so that year is partial. FY2024-25 was not in the editions read; the NPCI site could not be reached. The August 2025 figure is monthly and from the press.

| Period | Transactions, billion | Value, Rs lakh crore |
|---|---|---|
| FY2016-17 | 0.02 | 0.07 |
| FY2017-18 | 0.92 | 1.10 |
| FY2018-19 | 5.39 | 8.77 |
| FY2019-20 | 12.52 | 21.32 |
| FY2020-21 | 22.33 | 41.04 |
| FY2021-22 | 45.96 | 84.16 |
| FY2022-23 | 83.71 | 139.15 |
| FY2023-24 | 131.13 | 199.95 |
| August 2025 (one month) | 20.01 | |

Full file: `book/research/data/upi.csv`.

## The H-1B visa

### Cap and policy events (`h1b_policy.csv`)

**What it measures.** The annual cap on new H-1B visas, how many new petitions were issued against it, and the main policy changes.

**Definition and unit.** Petitions, US fiscal years (October-September). Numeric rows are NFAP's table of new petitions issued against the cap; other rows are dated events.

**Coverage.** 1990-2026.

**Sources.** S0105 (Congressional Research Service), S0338 (NFAP), S0335, S0136, S0137, S0300.

**Caveats.** NFAP is a pro-immigration group; its table is compiled from government data. The start year of the extra 20,000 places for holders of US master's degrees is not in the sources read (Chapter 13 gives 2004). Rulings of June and September 2026 on the $100,000 fee are summarised differently by different law firms, and the court orders were not read; the 2026 events postdate the research cut-off.

| US fiscal year | Cap | New petitions issued against the cap |
|---|---|---|
| 1992 | 65,000 | 48,600 |
| 1995 | 65,000 | 54,200 |
| 1997 | 65,000 | 65,000 (cap first reached, September 1997) |
| 1999 | 115,000 | 115,000 |
| 2000 | 115,000 | 115,000 |
| 2001 | 195,000 | 163,600 |
| 2002 | 195,000 | 79,100 |
| 2003 | 195,000 | 78,000 |
| 2004-2026 | 65,000 | 65,000 (cap reached every year) |

Events in the file: the Immigration Act of 1990 creates the visa; the FY2005 cap is reached on the first day of filing; the FY2008 cap is reached in two days in April 2007 (about 119,193 petitions); denial rates for initial employment fall from 24 per cent (FY2018) to 13 per cent (FY2020); the first lottery by electronic registration is held for FY2021; Proclamation 10973 of 19 September 2025 requires a $100,000 payment for new petitions; a DHS rule of 29 December 2025 weights selection towards higher wage levels; a Massachusetts court rules the fee unlawful on 8 June 2026; Proclamation 11069 of 18 September 2026 extends the fee to September 2027; and a California court vacates the implementing policies on 30 September 2026. Full file: `book/research/data/h1b_policy.csv`.

### H-1B approvals by country of birth (`h1b_country.csv`)

**What it measures.** The share of approved H-1B petitions that went to workers born in India.

**Definition and unit.** Approved petitions and per cent, by beneficiary's country of birth; initial (new employment), continuing (extensions) or all, as labelled.

**Coverage.** October 1999-February 2000; FY2005 (new arrivals); FY2023; FY2024. USCIS reports for FY2000-22 exist but could not be reached.

**Sources.** S0104, S0105, S0336 (USCIS FY2023 report), S0335 (USCIS FY2024 report, via a verified mirror).

**Caveats.** Petitions are not people: one worker can appear more than once. The FY2005 row counts new arrivals, a different measure. The USCIS FY2024 report gives two slightly different totals for India.

| Period | Measure | India | Share |
|---|---|---|---|
| Oct 1999-Feb 2000 | Approved petitions (INS) | 124,697 | 48.5% |
| FY2005 | New arrivals | | 49.0% |
| FY2023 | All approved petitions | 279,386 | 72.3% |
| FY2023 | Approved, initial employment | 68,825 | 57.9% |
| FY2023 | Approved, continuing employment | 210,561 | 78.8% |
| FY2024 | All approved petitions | 283,397 | 71.0% |
| FY2024 | Approved, initial employment | 80,449 | 57.0% |
| FY2024 | Approved, continuing employment | 203,306 | 78.7% |
| FY2023 | All approved petitions, China (for comparison) | 45,344 | 11.7% |
| FY2024 | All approved petitions, China (for comparison) | 46,680 | 11.7% |

Full file: `book/research/data/h1b_country.csv`.

### H-1B approvals by employer (`h1b_employer.csv`)

**What it measures.** Approved H-1B petitions for initial employment at selected employers.

**Definition and unit.** Petitions approved for new and concurrent employment, by employer, as compiled by NFAP from the USCIS H-1B Employer Data Hub, with related entities grouped by NFAP.

**Coverage.** FY2022-FY2025 for selected employers, and one administration claim on registrations.

**Sources.** S0337, S0338 (NFAP, a pro-immigration group); S0300; underlying data S0159 (USCIS hub, not reachable).

**Caveats.** NFAP revises earlier years between briefs (Cognizant FY2024 appears as 2,837 and 2,873). 'Indian-based' is NFAP's grouping and includes Cognizant, which is headquartered in the United States. The administration's claim that the largest outsourcing firms cut registrations from 24,946 to 2,055 concerns registrations, not approvals, names no firms and is a party's figure.

| Employer | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Amazon | 4,052 | 3,871 | 4,644 |
| Meta Platforms | 735 | 920 | 1,555 |
| Microsoft | 987 | 1,264 | 1,394 |
| Google | 1,267 | 1,058 | 1,050 |
| TCS | 1,174 | 1,452 | 846 |
| Cognizant | 2,597 | 2,873 (2,837 in an earlier brief) | 743 |
| IBM | 979 | 1,348 | 501 |
| LTIMindtree | 914 | 798 | 401 |
| HCL America | 715 | 1,248 | 379 |
| Infosys | | 2,504 | 263 |
| Wipro | | | 267 |
| Top seven Indian-based companies (NFAP grouping) | | | 4,573 (70% below FY2015) |

Full file: `book/research/data/h1b_employer.csv`.
