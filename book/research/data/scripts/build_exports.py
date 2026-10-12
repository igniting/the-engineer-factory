"""Build software_exports.csv.

Usage: python3 -I build_exports.py OUT_DIR
Values are transcribed from the cited pages and from RBI Handbook HTML views
(edition ids listed in the CSV header; accessed 2026-10-12). Reads us_cpi_u.csv from OUT_DIR for the real column.
"""
import csv, os, sys

OUT = sys.argv[1]

# Heeks working paper, Table 1 (S0085, printed p. 2), citing Heeks 1996 (S0070) and Dataquest 1998.
# 1980-1987 calendar years; from 1988/89 fiscal years (April-March).
HEEKS = {"1980": 4.0, "1981": 6.8, "1982": 13.5, "1983": 18.2, "1984": 25.3, "1985": 27.7,
         "1986": 38.9, "1987": 54.1, "FY1988-89": 69.7, "FY1989-90": 105.4, "FY1990-91": 131.2,
         "FY1991-92": 173.9, "FY1992-93": 219.8, "FY1993-94": 314.0, "FY1994-95": 480.9,
         "FY1995-96": 668.0, "FY1996-97": 997.0, "FY1997-98": 1650.0}
# Rajaraman (S0001), Table 2 'Software Services Export Revenue' (printed p. 48), source Bhatnagar.
BHATNAGAR = {"FY1990-91": 128, "FY1991-92": 164, "FY1992-93": 225, "FY1993-94": 330,
             "FY1994-95": 450, "FY1995-96": 734, "FY1996-97": 1100, "FY1997-98": 1759}
# Nasscom export figures as reported; definitions differ by year (see header).
NASSCOM = {"FY1998-99": (2650, "software exports, NASSCOM via Computergram June 1999", "S0109"),
           "FY2006-07": (31400, "IT-BPO exports, NASSCOM 2008 presentation", "S0107"),
           "FY2024-25": (224400, "technology industry exports, FY2025E, Strategic Review 2025", "S0140"),
           "FY2025-26": (246000, "technology industry exports, FY26 estimate, Strategic Review 2026 via PTI", "S0306")}
# RBI survey of computer software and IT services exports (S0106, read via summariser: medium-low).
RBI_SURVEY = {"FY2009-10": 38700, "FY2010-11": 47600}
# RBI balance of payments, 'Software services' credit (receipts), US$ million, latest edition per year.
RBI_BOP = {"FY2000-01": (6341, "10663"), "FY2001-02": (7556, "10663"), "FY2002-03": (9600, "10663"),
           "FY2003-04": (12800, "10663"), "FY2004-05": (17700, "10663"), "FY2005-06": (23600, "10663"),
           "FY2006-07": (31300, "10663"), "FY2007-08": (40300, "10663"),
           "FY2008-09": (46300, "15930"), "FY2009-10": (49705, "15930"), "FY2010-11": (53100, "15930"),
           "FY2011-12": (62212, "17914"), "FY2012-13": (65867, "18598"), "FY2013-14": (69483, "18598"),
           "FY2014-15": (73108, "18598"), "FY2015-16": (74153, "18598"), "FY2016-17": (74350, "18598"),
           "FY2017-18": (77326, "18598"), "FY2018-19": (83466, "22604"), "FY2019-20": (93102, "23949"),
           "FY2020-21": (99997, "23949"), "FY2021-22": (122093, "23949"), "FY2022-23": (146775, "23949"),
           "FY2023-24": (160333, "23949"), "FY2024-25": (180626, "23949"), "FY2025-26": (203675, "23949")}

cpi = {}
for r in csv.reader(l for l in open(os.path.join(OUT, "us_cpi_u.csv")) if not l.startswith("#")):
    if r[0].isdigit():
        cpi[int(r[0])] = float(r[1])


def year_end(p):
    return int(p) if p.isdigit() else int(p[2:6]) + 1


def deflator(p):
    """CPI weight for the period: calendar year as is; fiscal year = 0.75*CPI(y0) + 0.25*CPI(y0+1)."""
    if p.isdigit():
        return cpi.get(int(p))
    y0 = int(p[2:6])
    if y0 in cpi and y0 + 1 in cpi:
        return 0.75 * cpi[y0] + 0.25 * cpi[y0 + 1]
    return None


def real(v, p):
    d = deflator(p)
    return "" if (v in ("", None) or d is None) else f"{v * cpi[2025] / d:.1f}"


periods = sorted(set(HEEKS) | set(BHATNAGAR) | set(NASSCOM) | set(RBI_SURVEY) | set(RBI_BOP),
                 key=lambda p: (year_end(p), p))
rows = []
for p in periods:
    h, b = HEEKS.get(p, ""), BHATNAGAR.get(p, "")
    n = NASSCOM.get(p)
    rb = RBI_BOP.get(p)
    srcs = []
    if h != "": srcs.append("S0085 p.2")
    if b != "": srcs.append("S0001 p.48")
    if n: srcs.append(n[2])
    if p in RBI_SURVEY: srcs.append("S0106")
    if rb: srcs.append("S0155 (HB id " + rb[1] + ")")
    conf = "high" if rb else ("medium" if (h != "" or b != "" or n) else "low")
    note = ""
    if p == "FY2025-26":
        note = "RBI value preliminary; Nasscom value an estimate"
    if p == "FY1990-91":
        note = "Dispute (t) resolved: $128m and $131.2m are two series for the same fiscal year"
    rows.append([p, "CY" if p.isdigit() else "FY", year_end(p),
                 h, real(h, p), b, real(b, p),
                 n[0] if n else "", n[1] if n else "",
                 RBI_SURVEY.get(p, ""), rb[0] if rb else "", real(rb[0], p) if rb else "",
                 "; ".join(srcs), conf, note])

with open(os.path.join(OUT, "software_exports.csv"), "w", newline="") as f:
    for h in [
        "title: Indian software and services export revenue, US$ million, three definitional families kept apart",
        "definition: (1) early 'software exports' (gross foreign-exchange earnings): Heeks (S0085, citing Heeks 1996 and Dataquest) and Bhatnagar via Rajaraman (S0001);",
        "  (2) Nasscom industry exports, whose scope widens over time: 'software exports' (1998-99), 'IT-BPO exports' (2006-07), 'technology industry' exports incl. BPM, ER&D, products (2024-26);",
        "  (3) RBI: survey of computer software and IT services exports (S0106, 2009-11) and balance-of-payments 'Software services' credit (S0155, 2000-01 onwards).",
        "unit: US$ million, nominal; *_real_2025usd columns in 2025 US dollars using us_cpi_u.csv",
        "coverage: 1980-FY2025-26, with gaps (see notes/software_exports.md). Heeks rows 1980-1987 are calendar years; all others fiscal years April-March.",
        "source_ids: S0085 (printed p. 2, Table 1); S0001 (printed p. 48, Table 2); S0109; S0107; S0140; S0306; S0106; S0155 (RBI Handbook 'India's Overall Balance of Payments - US Dollar(s)': 2008 ed. Table 142 id=10663; 2014 ed. Table 140 id=15930; 2017 ed. Table 139 id=17914; 2018 ed. Table 133 id=18598; 2024 ed. id=22604; 2026 ed. Table 124 id=23949; HTML views at https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=..., accessed 2026-10-12)",
        "method: values transcribed as published. Real values: calendar years deflated by CPI-U of that year; fiscal years by 0.75*CPI(y0)+0.25*CPI(y0+1). No reconciled column: the families measure different things.",
        "breaks: Heeks figures are gross; net foreign-exchange earnings were estimated at around 40% of gross (S0085, p. 2). Nasscom and RBI definitions differ; RBI BoP includes all resident software exporters, Nasscom includes BPM and ER&D.",
        "  RBI BoP: each year taken from the latest edition read (edition id in source_id). Revisions between editions were small (2013-14: 69,439 in 2014 ed. vs 69,483 in 2018 ed.; 2016-17: 73,651 P vs 74,350 PR). 2025-26 preliminary. RBI BoP does not separate software before 2000-01 in the editions read.",
    ]:
        f.write("# " + h + "\n")
    w = csv.writer(f)
    w.writerow(["period", "period_type", "year_end",
                "sw_exports_usd_m_heeks", "sw_exports_heeks_real_2025usd",
                "sw_exports_usd_m_bhatnagar", "sw_exports_bhatnagar_real_2025usd",
                "nasscom_exports_usd_m", "nasscom_definition",
                "rbi_survey_sw_it_exports_usd_m", "rbi_bop_software_receipts_usd_m", "rbi_bop_real_2025usd",
                "source_id", "confidence", "note"])
    w.writerows(rows)
print("ok", len(rows))
