"""Build graduate_unemployment.csv, employability_tests.csv, fresher_pay.csv.
Usage: python3 -I build_labour.py OUT_DIR  (reads cpi_india_cy.csv for real pay)
Values transcribed from cited sources; see notes/labour.md."""
import csv, os, sys

OUT = sys.argv[1]


def write(name, header, cols, rows):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        for h in header:
            f.write("# " + h + "\n")
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)


# ---------- graduate_unemployment.csv ----------
GU = [
    ("2019-20", "India", "graduates, age 15+, usual status (PLFS)", 17.2, "S0326 (PIB, Lok Sabha reply, 20 Mar 2023)", "high", ""),
    ("2020-21", "India", "graduates, age 15+, usual status (PLFS)", 15.5, "S0326", "high", ""),
    ("2021-22", "India", "graduates, age 15+, usual status (PLFS)", 14.9, "S0326", "high", ""),
    ("2022-23", "India", "graduates, age 15+, usual status (PLFS)", 13.4, "S0327 (PTI via Careers360, 17 Dec 2023)", "medium", "lowest Chandigarh 5.6%, highest Andaman & Nicobar 33%"),
    ("2023-24", "India", "graduates, age 15+, usual status (PLFS)", 11.2, "S0328 (ETV Bharat, 6 Aug 2026)", "low", "conflicts with 13.0% in the S0154 register note (dispute ooo); verify against PLFS 2023-24 report"),
    ("2023-24", "India", "all persons, age 15+, usual status (ps+ss) (PLFS)", 3.2, "S0329 (MoSPI press note, PLFS annual report 2023-24, p. 2)", "high", "for contrast"),
    ("2023", "India", "graduates under 25 (Azim Premji University, State of Working India 2026)", 39.3, "S0328 (reporting SWI 2026)", "low", "different age group and method; report itself not read; 35% in 1983 per the same report"),
    ("2025", "United States", "recent graduates aged 22-27, computer science major (NY Fed)", 6.1, "S0136 (Proclamation 10973, p. 46027)", "medium", "as cited by the US government"),
    ("2025", "United States", "recent graduates aged 22-27, computer engineering major (NY Fed)", 7.5, "S0136", "medium", "as cited by the US government"),
]
write("graduate_unemployment.csv", [
    "title: Graduate unemployment rates, India (PLFS) with US comparison points",
    "definition: unemployment rate = unemployed as % of labour force; PLFS usual status (principal + subsidiary) for persons aged 15+ with graduate education unless stated",
    "unit: percent",
    "coverage: India graduates 2019-20 to 2023-24 (PLFS years July-June); one all-persons and one under-25 point; US 2025 points",
    "source_ids: S0326 (PIB 20 Mar 2023), S0327, S0328, S0329 (MoSPI), S0136",
    "method: transcribed as published. PLFS 2017-18 and 2018-19 graduate rates not obtained (S0154 register note giving 17.2% for 2017-18 is wrong: 17.2% is 2019-20).",
    "breaks: PLFS from 2017-18 only; earlier NSSO rounds not obtained. Never splice with NSSO or with SWI age-group figures.",
], ["year", "country", "population", "unemployment_rate_pct", "source_id", "confidence", "note"], GU)

# ---------- employability_tests.csv ----------
ET = [
    ("2013 graduates (2014 report)", "Software engineer, IT services ('trainable within 3 to 6 months')", 18.43, ">120,000 students, 520+ colleges", "S0153 (2014 ed., pp. 7, 12)"),
    ("2013 graduates (2014 report)", "Software engineer, IT products", 3.21, ">120,000 students, 520+ colleges", "S0153 (2014 ed., p. 7)"),
    ("2013 graduates (2014 report)", "Non-functional role such as BPO", 39.84, ">120,000 students, 520+ colleges", "S0153 (2016 ed., p. 5, restating 2014)"),
    ("2016 report", "Software engineer, IT services", 17.91, ">150,000 students, 650+ colleges", "S0153 (2016 ed., pp. 5, 11)"),
    ("2016 report", "Software engineer, IT products", 3.67, ">150,000 students, 650+ colleges", "S0153 (2016 ed., p. 5)"),
    ("2016 report", "Business process outsourcing", 40.57, ">150,000 students, 650+ colleges", "S0153 (2016 ed., p. 5)"),
    ("2016 report", "Startup software engineering", 3.84, ">150,000 students, 650+ colleges", "S0153 (2016 ed., p. 5)"),
    ("2016 report", "'software-industry ready' (programming skills)", 4.51, ">150,000 students, 650+ colleges", "S0153 (2016 ed., p. 11)"),
    ("c. 2005", "Indian engineers able to 'compete in the global outsourcing arena' (McKinsey, via Duke)", 25, "not stated", "S0213 (p. 9)"),
]
write("employability_tests.csv", [
    "title: Vendor and consultant 'employability' estimates for Indian engineering graduates",
    "definition: share of tested students meeting the vendor's own benchmark for a role; NOT a labour-market outcome (myth M07)",
    "unit: percent of tested sample",
    "coverage: Aspiring Minds/SHL 2014 and 2016 reports; McKinsey c. 2005 as reported by Duke",
    "source_ids: S0153 (Aspiring Minds National Employability Report: Engineers, 2014 and 2016 eds.; 2016 ed. printed page = PDF page - 2), S0213",
    "method: transcribed as published. Aspiring Minds sells the AMCAT test it uses; benchmarks are its own.",
    "breaks: samples and benchmarks differ by edition; press often conflates editions. Every use must name the vendor and the role definition.",
], ["test_cohort", "role_or_measure", "pct_meeting_benchmark", "sample", "source_id"], ET)

# ---------- fresher_pay.csv ----------
cpi = {int(r[0]): float(r[1]) for r in csv.reader(l for l in open(os.path.join(OUT, "cpi_india_cy.csv")) if not l.startswith("#")) if r[0].isdigit()}
base = max(cpi)
FP = [
    (2007, "TCS Assistant Systems Engineer trainee, annual package", 3.16, "", "S0330 (Business Today, 9 Feb 2026, citing a Reddit post)", "low", "single anecdotal source"),
    (2012, "median fresher pay, large IT firms (Moneycontrol study)", 2.45, "", "S0331 (HR Katha, 1 Jun 2022, reporting Moneycontrol)", "medium", "study method not read"),
    (2014, "STEM graduate starting salaries (TeamLease Digital CEO's estimate)", 2.0, 2.5, "S0332 (ThePrint, 11 Sep 2025)", "low", "range as quoted"),
    (2015, "median salary for the same skill (Aspiring Minds)", 2.82, "", "S0153 (2016 ed., p. 5)", "low", "vendor estimate; 'last year' in 2016 report; aspiration 3.10"),
    (2016, "median salary for the same skill (Aspiring Minds)", 3.13, "", "S0153 (2016 ed., p. 5)", "low", "vendor estimate; median aspiration 3.40"),
    (2022, "median fresher pay, large IT firms (Moneycontrol study)", 3.55, "", "S0331", "medium", "+45% on 2012 per the study"),
    (2022, "Infosys fresher pay (per Infosys annual report, as reported)", 3.6, "", "S0331", "medium", "annual report not read"),
    (2022, "freshers at large IT firms (T.V. Mohandas Pai, former Infosys CFO)", 3.5, 4.0, "S0333 (Business Today, 27 Dec 2022)", "low", "'the same ... that the companies were paying 10-12 years ago'"),
    (2025, "STEM graduate starting salaries (TeamLease Digital CEO's estimate, 'today')", 3.0, 3.5, "S0332", "low", ""),
    (2025, "Wipro entry-level salaries FY2025-26 (CHRO, post-results press conference)", 3.0, 4.0, "S0334 (People Matters, 16 Apr 2025, citing News18)", "medium", "'unchanged ... flat for over a decade'"),
    (2026, "TCS Assistant Systems Engineer, annual package", 3.36, "", "S0330 (citing Careers360)", "low-medium", ""),
]
rows = []
for y, m, lo, hi, s, c, n in FP:
    mid = (lo + (hi or lo)) / 2
    real = f"{mid * cpi[base] / cpi[y]:.2f}" if y in cpi else ""
    rows.append([y, m, lo, hi, real, s, c, n])
write("fresher_pay.csv", [
    "title: Starting (fresher) annual pay in Indian IT services, point estimates",
    "definition: annual cost-to-company or package as reported; medians, single-firm packages and quoted ranges are different measures (measure column)",
    "unit: Rs lakh per year, nominal; real_" + str(base) + "_inr_lakh = midpoint deflated by India CPI (cpi_india_cy.csv, OECD MEI) to " + str(base) + " rupees",
    "coverage: 2007-2026 points; no consistent series",
    "source_ids: S0330, S0331, S0332, S0333, S0334, S0153",
    "method: transcribed; ranges kept as low/high; real value uses the midpoint of a range; years after " + str(base) + " not deflated",
    "breaks: offer vs CTC vs in-hand; mass-recruiter vs premium tracks (e.g. TCS 'Digital', HCLTech 'Elite') excluded",
], ["year", "measure", "pay_rs_lakh_low", "pay_rs_lakh_high", "real_" + str(base) + "_inr_lakh", "source_id", "confidence", "note"], rows)
print("ok")
