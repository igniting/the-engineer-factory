"""Build top_firms.csv. Usage: python3 -I build_firms.py OUT_DIR
Values transcribed from company filings (pages/items in notes/top_firms.md) and from
SEC XBRL company facts (data.sec.gov/api/xbrl/companyfacts, accessed 2026-10-12).
Reads us_cpi_u.csv and inr_usd_fy.csv from OUT_DIR."""
import csv, os, sys

OUT = sys.argv[1]

# Infosys: fiscal year ends 31 March. Revenue US$ million; employees at 31 March.
# rev source: 20-F five-year comparison sentences (Item 5) or XBRL (RevenueFromContractsWithCustomers).
INFY_REV = {1999: (121.0, "S0270 (20-F FY2004)"), 2001: (414, "S0264 (20-F FY2005)"), 2004: (1063, "S0265 (20-F FY2008)"),
            2005: (1592, "S0264"), 2008: (4176, "S0265"), 2009: (4663, "S0271 (20-F FY2009)"),
            2010: (4804, "S0272 (20-F FY2010)"), 2012: (6994, "S0266 (20-F FY2012)"),
            2016: (9501, "XBRL; S0287"), 2017: (10208, "XBRL; S0288"), 2018: (10939, "XBRL; S0289"),
            2019: (11799, "XBRL; S0290"), 2020: (12780, "XBRL; S0287"), 2021: (13561, "XBRL; S0288"),
            2022: (16311, "XBRL; S0289"), 2023: (18212, "XBRL; S0290"), 2024: (18562, "XBRL; S0291"),
            2025: (19277, "XBRL; S0296"), 2026: (20158, "S0297 (20-F FY2026)")}
INFY_EMP = {1999: (3800, "S0270"), 2000: (5390, "S0322 (20-F FY2001)"), 2001: (9830, "S0322"),
            2004: (23800, "S0270"), 2005: (36800, "S0264"), 2006: (52700, "S0272"),
            2008: (91200, "S0265"), 2009: (104900, "S0271"), 2010: (113800, "S0272"), 2012: (150000, "S0266"),
            2016: (194044, "S0287"), 2017: (200364, "S0288"), 2018: (204107, "S0289"), 2019: (228123, "S0290"),
            2020: (242371, "S0287"), 2021: (259619, "S0288"), 2022: (314015, "S0289"), 2023: (343234, "S0290"),
            2024: (317240, "S0291"), 2025: (323578, "S0296"), 2026: (328594, "S0297")}
# Wipro: fiscal year ends 31 March. Revenue INR million (consolidated, IFRS). Employees 'more than' N at 31 March.
WIT_REV_INR = {2016: (512440, "XBRL"), 2017: (550402, "XBRL"), 2018: (544871, "XBRL"), 2019: (585845, "XBRL"),
               2020: (610232, "XBRL"), 2021: (619430, "XBRL"), 2022: (790934, "XBRL"), 2023: (904876, "XBRL"),
               2024: (897603, "XBRL; S0298"), 2025: (890884, "XBRL; S0298"), 2026: (926240, "S0298 (20-F FY2026)")}
WIT_EMP = {2019: (170000, "S0292 (20-F FY2021)"), 2020: (175000, "S0292"), 2021: (200000, "S0292"),
           2022: (240000, "S0292 (20-F FY2024)"), 2023: (250000, "S0298 (20-F FY2025)"),
           2024: (232000, "S0298 (20-F FY2025; 234,000 in 20-F FY2024)"), 2025: (230000, "S0298"),
           2026: (240000, "S0298 (20-F FY2026)")}
# Cognizant: calendar year. Revenue US$ million (XBRL Revenues/SalesRevenueNet). Employees at 31 December.
CTSH_REV = {2007: 2135.6, 2008: 2816.3, 2009: 3278.7, 2010: 4592.4, 2011: 6121.2, 2012: 7346.5, 2013: 8843.2,
            2014: 10263, 2015: 12416, 2016: 13487, 2017: 14810, 2018: 16125, 2019: 16783, 2020: 16652,
            2021: 18507, 2022: 19428, 2023: 19353, 2024: 19736, 2025: 21108}
CTSH_EMP = {2001: (3470, "S0275 (10-K FY2002; technical professionals)", ""),
            2002: (6100, "S0275 ('over 6,100' technical professionals)", ""),
            2007: (55400, "S0276 (10-K FY2007)", ""), 2011: (137700, "S0277 (derived: 156,700 less 'approximately 19,000')", ""),
            2012: (156700, "S0277 (10-K FY2012)", ""), 2020: (289500, "S0293 (10-K FY2021)", ""),
            2021: (330600, "S0293", ""), 2022: (355300, "S0293", 258500), 2023: (347700, "S0293", 254000),
            2024: (336800, "S0192 (10-K FY2024)", 241500), 2025: (351600, "S0299 (10-K FY2025)", 256900)}
# TCS: fiscal year ends 31 March (except Q2 FY27 point). Headcount only; revenue not obtained from primary sources.
TCS_EMP = {2025: (607979, "S0160 (Q4 FY2024-25 fact sheet)"), 2026: (584519, "derived: S0160 less 23,460 (S0139)")}

cpi = {int(r[0]): float(r[1]) for r in csv.reader(l for l in open(os.path.join(OUT, "us_cpi_u.csv")) if not l.startswith("#")) if r[0].isdigit()}
fx = {int(r[1]): float(r[2]) for r in csv.reader(l for l in open(os.path.join(OUT, "inr_usd_fy.csv")) if not l.startswith("#")) if r[1].isdigit()}


def defl(fy_end, fiscal):
    if not fiscal:
        return cpi.get(fy_end)
    a, b = cpi.get(fy_end - 1), cpi.get(fy_end)
    return 0.75 * a + 0.25 * b if a and b else None


rows = []


def add(firm, fiscal, year, rev_usd, rev_inr, emp, emp_note, emp_india, src, conf, note):
    prev = None
    for r in rows:
        if r[0] == firm and r[2] == year - 1 and r[6] != "":
            prev = r[6]
    d = defl(year, fiscal)
    real = f"{rev_usd * cpi[2025] / d:.1f}" if (rev_usd != "" and d) else ""
    rpe = ""
    if rev_usd != "" and emp != "":
        avg = (emp + prev) / 2 if prev not in (None, "") else None
        if avg:
            rpe = f"{rev_usd * 1e6 / avg / 1000:.1f}"
    rows.append([firm, "FY Apr-Mar" if fiscal else "CY", year, "" if rev_usd == "" else f"{rev_usd:.1f}", real,
                 "" if rev_inr == "" else rev_inr, emp, emp_note, emp_india, rpe, src, conf, note])


for y in sorted(set(INFY_REV) | set(INFY_EMP)):
    r, e = INFY_REV.get(y), INFY_EMP.get(y)
    src = "; ".join(x for x in [r[1] if r else "", e[1] if e else ""] if x)
    add("Infosys", True, y, r[0] if r else "", "", e[0] if e else "", "approximately" if e and y <= 2012 else ("exact" if e else ""), "",
        src, "high", "US$ revenue as reported (IFRS from FY2009; earlier US GAAP)")
for y in sorted(set(WIT_REV_INR) | set(WIT_EMP)):
    r, e = WIT_REV_INR.get(y), WIT_EMP.get(y)
    usd = r[0] / fx[y] if (r and y in fx) else ""
    src = "; ".join(x for x in [(r[1] + "; S0155 FX") if r else "", e[1] if e else ""] if x)
    add("Wipro", True, y, usd, r[0] if r else "", e[0] if e else "", "more than" if e else "", "", src, "high" if r else "medium",
        "US$ = INR revenue / RBI FY average rate (book's conversion, not Wipro's convenience translation)")
for y in sorted(set(CTSH_REV) | set(CTSH_EMP)):
    e = CTSH_EMP.get(y)
    src = "; ".join(x for x in ["XBRL (10-K)" if y in CTSH_REV else "", e[1] if e else ""] if x)
    add("Cognizant", False, y, CTSH_REV.get(y, ""), "", e[0] if e else "", "approximately" if e else "", e[2] if e else "",
        src, "high", "US company; most staff in India")
for y, (v, s) in sorted(TCS_EMP.items()):
    add("TCS", True, y, "", "", v, "derived" if "derived" in s else "as reported", "", s, "medium", "revenue not compiled (TCS site blocked)")
rows.append(["TCS", "quarter end 30 Sep 2026", 2027, "", "", "", 598056, "as reported", "", "", "S0310; S0138", "medium", "Q2 FY27 point (POST-CUTOFF)"])

with open(os.path.join(OUT, "top_firms.csv"), "w", newline="") as f:
    for h in [
        "title: Revenue, headcount and revenue per employee, selected Indian-heritage IT firms",
        "definition: one row per firm-year; Infosys, Wipro and TCS fiscal years end 31 March (year = calendar year in which it ends); Cognizant calendar years",
        "unit: revenue US$ million (nominal and 2025 dollars); Wipro also INR million; employees persons at year end; revenue per employee US$ thousand",
        "coverage: Infosys FY1999-FY2026 (gaps FY2002-03, FY2007, FY2011, FY2013-15); Wipro FY2016-FY2026; Cognizant 2001-2025 (headcount gaps 2003-06, 2008-10, 2013-19); TCS headcount points",
        "source_ids: Infosys 20-F/F-1 S0322, S0264-S0266, S0270-S0272, S0287-S0291, S0296, S0297; Wipro 20-F S0292, S0298; Cognizant 10-K S0192, S0275-S0277, S0293, S0299;",
        "  SEC XBRL company facts (data.sec.gov, CIK 1067491, 1123799, 1058290, accessed 2026-10-12); TCS S0160, S0139, S0310; FX S0155; CPI S0157",
        "method: revenue_per_employee = revenue / mean of opening and closing headcount (blank if either missing). Real values: fiscal years deflated by 0.75*CPI(y-1)+0.25*CPI(y); calendar years by CPI(y).",
        "breaks: Infosys revenue US GAAP to FY2008, IFRS from FY2009. Wipro headcount stated as 'more than' N and revised between filings (FY2024: 234,000 then 232,000). Cognizant 2001-02 counts are technical professionals only.",
    ]:
        f.write("# " + h + "\n")
    w = csv.writer(f)
    w.writerow(["firm", "year_type", "year", "revenue_usd_m", "revenue_real_2025usd_m", "revenue_inr_m", "employees",
                "employees_qualifier", "employees_india", "revenue_per_employee_usd_k", "source_id", "confidence", "note"])
    w.writerows(rows)
print("ok", len(rows))
