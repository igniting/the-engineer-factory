"""Build h1b_country.csv, h1b_employer.csv, h1b_policy.csv, indian_students_us.csv, iit_emigration.csv.
Usage: python3 -I build_migration.py OUT_DIR. Values transcribed; see notes/migration.md."""
import csv, os, sys

OUT = sys.argv[1]


def write(name, header, cols, rows):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        for h in header:
            f.write("# " + h + "\n")
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)


# ---------- h1b_country.csv ----------
HC = [
    ("Oct 1999-Feb 2000", "approved petitions (INS)", "India", 124697, 257077, 48.5, "S0104 (via visalaw.com table)", "medium", "INS original not read"),
    ("FY2005", "new arrivals", "India", "", "", 49.0, "S0105 (RL30498)", "medium", "different measure"),
    ("FY2023", "all approved petitions", "India", 279386, 386318, 72.3, "S0336 (USCIS FY2023 report, Table 4a, p. 27)", "high", ""),
    ("FY2023", "all approved petitions", "China", 45344, 386318, 11.7, "S0336 (Table 4a, p. 27)", "high", ""),
    ("FY2023", "approved, initial employment", "India", 68825, 118948, 57.9, "S0336 (Table 4b, p. 33)", "high", ""),
    ("FY2023", "approved, continuing employment", "India", 210561, 267370, 78.8, "S0336 (Table 4c, p. 39)", "high", ""),
    ("FY2024", "all approved petitions", "India", 283397, 399395, 71.0, "S0335 (USCIS FY2024 report, Figure 5, p. 6)", "high", "Table 4a gives 283,755 (71%) of 399,378 with known sex: internal inconsistency"),
    ("FY2024", "all approved petitions", "China", 46680, 399395, 11.7, "S0335 (Figure 5, p. 6)", "high", ""),
    ("FY2024", "approved, initial employment", "India", 80449, 141192, 57.0, "S0335 (Table 4b, p. 31)", "high", "total is beneficiaries with known sex"),
    ("FY2024", "approved, continuing employment", "India", 203306, 258186, 78.7, "S0335 (Table 4c, p. 36)", "high", ""),
]
write("h1b_country.csv", [
    "title: H-1B petitions approved by beneficiary's country of birth",
    "definition: count and share of approved H-1B petitions (initial, continuing or all) by country of birth; one petition can relate to the same person more than once",
    "unit: petitions; percent",
    "coverage: Oct 1999-Feb 2000; FY2005 (arrivals); FY2023; FY2024. FY2000-22 USCIS reports exist but uscis.gov blocks this container.",
    "source_ids: S0104, S0105, S0335 (FY2024 report; copy via poder360.com.br mirror, verified: its FY2020-23 rows in Table 1b match S0336 exactly), S0336 (FY2023 report via govinfo CMR-HS8-00193273)",
    "method: transcribed; shares as published",
    "breaks: 'initial' vs 'continuing' split published from FY2020; approvals are petitions not people; FY2005 figure is new arrivals.",
], ["period", "measure", "country", "count", "total", "share_pct", "source_id", "confidence", "note"], HC)

# ---------- h1b_employer.csv ----------
# NFAP tables of approved petitions for initial employment (from USCIS Employer Data Hub).
EMP25 = {"Amazon": (4644, 3871, 4052), "Meta Platforms": (1555, 920, 735), "Microsoft": (1394, 1264, 987),
         "Google": (1050, 1058, 1267), "TCS": (846, 1452, 1174), "Apple": (823, 864, 707),
         "Cognizant": (743, 2873, 2597), "IBM": (501, 1348, 979), "Deloitte": (432, 891, 591),
         "Capgemini": (401, 1041, 1110), "LTIMindtree": (401, 798, 914), "HCL America": (379, 1248, 715)}
APPX25 = {"Tech Mahindra": 295, "Wipro": 267, "Infosys": 263, "Accenture": 254}
rows = []
for e, (a25, a24, a23) in EMP25.items():
    for fy, v in (("FY2025", a25), ("FY2024", a24), ("FY2023", a23)):
        rows.append([fy, e, v, "S0338 (NFAP Nov 2025, Table 1, p. 6)", "medium", ""])
for e, v in APPX25.items():
    rows.append(["FY2025", e, v, "S0338 (Appendix Table 2)", "medium", "not in top 25"])
rows += [["FY2024", "Infosys", 2504, "S0337 (NFAP Dec 2024, p. 2)", "medium", ""],
         ["FY2024", "Cognizant", 2837, "S0337 (p. 2)", "medium", "NFAP Nov 2025 gives 2,873 for FY2024: revision or typo"],
         ["FY2022", "Amazon", 6396, "S0337; S0338", "medium", ""],
         ["FY2025", "top seven Indian-based companies (NFAP grouping)", 4573, "S0338 (p. 6)", "medium", "'a drop of 70% from FY 2015 and 37% fewer than in FY 2024' (NFAP)"],
         ["FY2025 vs FY2027 cap seasons", "largest IT staffing and outsourcing firms, combined registrations (unnamed)", "24,946 to 2,055", "S0300", "low", "US administration's claim; registrations, not approvals"]]
write("h1b_employer.csv", [
    "title: H-1B petitions approved for initial employment, selected employers",
    "definition: approved petitions for initial (new and concurrent) employment by employer, as compiled by NFAP from the USCIS H-1B Employer Data Hub; NFAP groups related entities",
    "unit: petitions",
    "coverage: FY2022-FY2025 (selected employers); one administration claim on registrations",
    "source_ids: S0337, S0338 (National Foundation for American Policy, a pro-immigration policy group), S0300; underlying data S0159 (USCIS hub, blocked from this container)",
    "method: transcribed from NFAP tables",
    "breaks: NFAP revises earlier years between briefs (Cognizant FY2024 2,837 vs 2,873). 'Indian-based' is NFAP's classification (Cognizant is US-headquartered).",
], ["fiscal_year", "employer", "approvals_initial_employment", "source_id", "confidence", "note"], rows)

# ---------- h1b_policy.csv (event table + cap) ----------
CAP = {1992: (65000, 48600), 1993: (65000, 61600), 1994: (65000, 60300), 1995: (65000, 54200), 1996: (65000, 55100),
       1997: (65000, 65000), 1998: (65000, 65000), 1999: (115000, 115000), 2000: (115000, 115000), 2001: (195000, 163600),
       2002: (195000, 79100), 2003: (195000, 78000)}
rows = [[str(y), "cap and petitions issued against cap", c, i, "S0338 (Appendix Table 1)", "medium", "fiscal year"] for y, (c, i) in sorted(CAP.items())]
rows.append(["2004-2026", "cap and petitions issued against cap", 65000, 65000, "S0338 (Appendix Table 1)", "medium", "cap reached every year"])
EV = [
    ("1990", "Immigration Act of 1990 (P.L. 101-649) creates the H-1B classification with an annual cap of 65,000", "S0105"),
    ("1997-09", "Cap first reached", "S0105 (RL30498)"),
    ("FY1999-2000", "Cap raised temporarily to 115,000", "S0105; S0338"),
    ("FY2001-03", "Cap raised to 195,000", "S0105; S0338"),
    ("FY2004", "Cap returns to 65,000", "S0338"),
    ("FY2005", "Cap reached on the first day of filing", "S0105 (RL30498)"),
    ("by FY2025", "20,000 additional petitions for holders of US master's or higher degrees (start date not in sources read)", "S0338"),
    ("2007-04", "FY2008 cap reached in two days (c. 119,193 petitions)", "S0105 (RL30498)"),
    ("FY2018-20", "Denial rates for initial employment 24% (FY2018), 21% (FY2019), 13% (FY2020)", "S0338 (Table 2)"),
    ("FY2021", "First lottery based on electronic registration", "S0335 (p. 21)"),
    ("2025-09-19", "Proclamation 10973: $100,000 payment for new petitions, effective 21 Sep 2025", "S0136"),
    ("2025-12-29", "DHS final rule: weighted selection favouring higher wage levels", "S0300"),
    ("2026-06-08", "D. Mass. rules the fee unlawful (what was vacated disputed, aaa)", "S0137"),
    ("2026-09-18", "Proclamation 11069 extends the fee to 21 Sep 2027", "S0300"),
    ("2026-09-30", "N.D. Cal. vacates agency policies implementing the fee (Global Nurse Force v. Trump)", "S0137"),
]
for d, e, s in EV:
    rows.append([d, e, "", "", s, "high" if s.startswith(("S0105", "S0136", "S0300")) else "medium", "POST-CUTOFF" if d.startswith("2026") else ""])
write("h1b_policy.csv", [
    "title: H-1B cap, petitions issued against the cap, and policy events",
    "definition: rows with cap/issued numbers are NFAP's table of new petitions issued against the cap by fiscal year; other rows are dated policy events",
    "unit: petitions (where numeric)",
    "coverage: 1990-2026",
    "source_ids: S0105 (CRS IF12912, RL30498), S0338 (NFAP), S0335, S0136, S0137, S0300",
    "method: transcribed",
    "breaks: event table, not a series",
], ["date", "event_or_measure", "cap", "issued", "source_id", "confidence", "note"], rows)

# ---------- indian_students_us.csv ----------
OD = {"2017/18": 196271, "2018/19": 202014, "2019/20": 193124, "2020/21": 167582, "2021/22": 199182,
      "2022/23": 268923, "2023/24": 331602, "2024/25": 363019}
rows = [[y, v, "", "", "", "", "S0158 (Open Doors India fact sheet 2025)", "high", ""] for y, v in OD.items()]
rows[-2][2:6] = [36053, 196567, 1426, 97556]
rows[-1][2:6] = [40135, 177892, 1252, 143740]
write("indian_students_us.csv", [
    "title: Students from India in US higher education (Open Doors)",
    "definition: international students from India enrolled in or on OPT at US institutions, academic year; level split for the latest two years",
    "unit: persons",
    "coverage: 2017/18 to 2024/25 (earlier years in Open Doors not obtained)",
    "source_ids: S0158 (Institute of International Education, Open Doors, India fact sheet 2025; IIE is a non-profit with State Department support)",
    "method: transcribed from the fact sheet",
    "breaks: totals include OPT (Optional Practical Training: post-study work), which rose from 97,556 to 143,740; graduate students fell 9.5% in 2024/25",
], ["academic_year", "total", "undergraduate", "graduate", "non_degree", "opt", "source_id", "confidence", "note"], rows)

# ---------- iit_emigration.csv ----------
IIT = [
    ("1973-1977 graduates", "IIT Bombay electrical engineering graduates living abroad", "slightly over 40%", "S0003 p. 803; S0046", "medium", "Sukhatme survey as reported by Bassett"),
    ("since 1970", "IIT Bombay graduates settled abroad", "about 3 in 10", "S0046 (as reported in Nature, 1993)", "low", "secondary report of the survey"),
    ("JEE 2010 top 1,000", "migrated abroad (by c. 2020)", "36%", "S0172 (NBER w31308, abstract)", "high", ""),
    ("JEE 2010 top 100", "migrated abroad", "62%", "S0172 (abstract)", "high", ""),
    ("JEE 2010 cohort", "extra migration for graduate school at original 'Top 5' IITs vs equally talented peers", "+5 percentage points", "S0172 (abstract)", "high", ""),
]
write("iit_emigration.csv", [
    "title: Emigration of IIT graduates and top JEE scorers",
    "definition: share of a cohort living or working abroad; cohorts and methods differ by study",
    "unit: percent or ratio as stated",
    "coverage: 1970s cohorts; JEE 2010 cohort",
    "source_ids: S0003, S0046, S0172 (Choudhury, Ganguli and Gaule, NBER Working Paper 31308, June 2023)",
    "method: transcribed; a table, not a series",
    "breaks: different institutions, cohorts and definitions; do not compare as a trend",
], ["cohort", "measure", "value", "source_id", "confidence", "note"], IIT)
print("ok")
