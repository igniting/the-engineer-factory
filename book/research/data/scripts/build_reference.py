"""Build reference series: us_cpi_u.csv, inr_usd.csv, inr_usd_fy.csv.

Usage: python3 -I build_reference.py RAW_DIR OUT_DIR

RAW_DIR must hold the files downloaded on the access date:
  cu.txt                 BLS cu.data.1.AllItems (S0157)
  pv23957.html           RBI Handbook Table 132, HTML view (S0155)
  pv23958.html           RBI Handbook Table 133, HTML view (S0155)
  XRNCUSINA618NRUG.csv   FRED, Penn World Table 11.0 'xr' for India (S0319)
  fred_a.csv             FRED AEXINUS, Federal Reserve G.5A annual (S0320)
Raw files are not committed (size and licence); URLs are in each CSV header.
"""
import csv, html, os, re, sys

RAW, OUT = sys.argv[1], sys.argv[2]
ACCESSED = "2026-10-12"


def page_text(name, table):
    s = open(os.path.join(RAW, name), encoding="utf-8", errors="ignore").read()
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s)))
    i = t.find(table)
    return t[i:t.find("Notes :", i)]


def fred(name):
    d = {}
    for r in csv.reader(open(os.path.join(RAW, name))):
        if r[0][:4].isdigit() and r[1] not in ("", "."):
            d[int(r[0][:4])] = float(r[1])
    return d


def write(path, header_lines, cols, rows):
    with open(path, "w", newline="") as f:
        for h in header_lines:
            f.write("# " + h + "\n")
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)


# ---------- US CPI-U ----------
monthly, annual = {}, {}
for line in open(os.path.join(RAW, "cu.txt")):
    p = line.split()
    if not p or p[0] != "CUUR0000SA0":
        continue
    y, per = int(p[1]), p[2]
    if per == "M13":
        annual[y] = float(p[3])
    elif per.startswith("M") and p[3] != "-":
        monthly.setdefault(y, []).append(per)
base = annual[2025]
rows = []
for y in sorted(annual):
    if y < 1950:
        continue
    n = len(monthly.get(y, []))
    note = "October 2025 missing (BLS footnote X, data unavailable; reportedly the 2025 federal funding lapse, verify); BLS annual average uses 11 months" if y == 2025 else ""
    rows.append([y, f"{annual[y]:.3f}", n, f"{base / annual[y]:.4f}", "S0157", "high", note])
write(os.path.join(OUT, "us_cpi_u.csv"), [
    "title: US Consumer Price Index for All Urban Consumers (CPI-U), US city average, all items, annual average",
    "definition: BLS series CUUR0000SA0, not seasonally adjusted; annual average (period M13) as published by BLS",
    "unit: index, 1982-84=100; to_2025_usd = CPI(2025)/CPI(year), multiply a nominal dollar value of that year to express it in 2025 dollars",
    "coverage: 1950-2025. 2026 omitted (partial year; January-August 2026 monthly values 325.252-334.980 available in the raw file)",
    "source_ids: S0157 (BLS flat file https://download.bls.gov/pub/time.series/cu/cu.data.1.AllItems, accessed " + ACCESSED + ")",
    "method: values copied as published; months_in_average counts monthly observations present in the raw file",
    "breaks: none in the index. 2025 average based on 11 months (October 2025 missing in BLS data, footnote X)",
], ["year", "cpi_u_annual_avg", "months_in_average", "to_2025_usd", "source_id", "confidence", "note"], rows)

# ---------- INR per USD, calendar year ----------
rbi_cy = {}
for m in re.finditer(r"\b(19[89]\d|20[0-2]\d) ([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)",
                     page_text("pv23957.html", "Table 132")):
    rbi_cy[int(m.group(1))] = float(m.group(3))
pwt, g5a = fred("XRNCUSINA618NRUG.csv"), fred("fred_a.csv")
rows = []
for y in range(1950, 2026):
    r, p, g = rbi_cy.get(y), pwt.get(y), g5a.get(y)
    if r is not None:
        pref, psrc, conf = r, "S0155", "high"
    elif g is not None:
        pref, psrc, conf = g, "S0320", "high"
    else:
        pref, psrc, conf = p, "S0319", "medium"
    note = ""
    if y == 1966:
        note = "Devaluation 6 June 1966 from Rs 4.76 to Rs 7.50 per dollar; PWT value is a within-year average"
    elif y == 1991:
        note = "Devaluations of 1 and 3 July 1991"
    elif y in (1971, 1972, 1973):
        note = "Bretton Woods collapse; regime change (see header; unsourced)"
    elif y == 2025:
        note = "PWT not yet available for 2025"
    rows.append([y, "" if r is None else f"{r:.4f}", "" if g is None else f"{g:.4f}",
                 "" if p is None else f"{p:.4f}", f"{pref:.4f}", psrc, conf, note])
write(os.path.join(OUT, "inr_usd.csv"), [
    "title: Indian rupees per US dollar, calendar-year annual average",
    "definition: three independent series kept in separate columns, plus a preferred column built by a stated rule",
    "unit: rupees per US dollar",
    "coverage: 1950-2025",
    "source_ids: S0155 RBI Handbook of Statistics on Indian Economy, Table 132 (HTML view https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=23957), 1987-2025;",
    "  S0320 Federal Reserve G.5A annual averages of noon buying rates in New York (FRED AEXINUS), 1973-2025;",
    "  S0319 Penn World Table 11.0, variable xr, market plus estimated (FRED XRNCUSINA618NRUG), 1950-2023. All accessed " + ACCESSED + ".",
    "method: inr_per_usd_preferred = RBI where available (1987-2025); else Federal Reserve G.5A (1973-1986); else PWT (1950-1972).",
    "  Overlap checks: 1987 RBI 12.9552, G.5A 12.9469, PWT 12.9615; 1991 RBI 22.6890, G.5A 22.7116, PWT 22.7424; 2010 RBI 45.7262, G.5A 45.6507, PWT 45.7258. Differences under 0.3% in these years.",
    "breaks: RBI uses official rates to 1992, FEDAI indicative rates 1993 to April 2012, RBI reference rates from May 2012 (FBIL from July 2018).",
    "  Regime notes from background knowledge, NOT yet sourced (verify in Phase 5): fixed parity Rs 4.7619 from September 1949; Rs 7.50 from June 1966; sterling link from December 1971; basket peg from September 1975; unified market rate from March 1993.",
    "  Cross-check: S0001 cites Rs 4.5 per dollar for 1951, which does not match the official parity of about Rs 4.76; treat S0001's figure as approximate.",
], ["year", "inr_per_usd_rbi", "inr_per_usd_fed_g5a", "inr_per_usd_pwt", "inr_per_usd_preferred", "preferred_source_id", "confidence", "note"], rows)

# ---------- INR per USD, financial year (April-March) ----------
rows = []
for m in re.finditer(r"\b(\d{4})-(\d{2}) ([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)",
                     page_text("pv23958.html", "Table 133")):
    y0 = int(m.group(1))
    rows.append([f"FY{y0}-{m.group(2)}", y0 + 1, m.group(5), m.group(6), "S0155", "high",
                 "official rates" if y0 <= 1991 else ("FEDAI indicative" if y0 < 2012 else "FEDAI to April 2012, then RBI reference" if y0 == 2012 else "RBI/FBIL reference")])
write(os.path.join(OUT, "inr_usd_fy.csv"), [
    "title: Indian rupees per US dollar, financial year (April-March) annual average and end-year rate",
    "definition: RBI Handbook Table 133, US dollar columns",
    "unit: rupees per US dollar",
    "coverage: FY1986-87 to FY2025-26; year_end is the calendar year in which the financial year ends",
    "source_ids: S0155 (https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=23958, accessed " + ACCESSED + ")",
    "method: values copied as published. Use the average for fiscal-year flow series (rule D3); use end-year for stocks at 31 March.",
    "breaks: official rates to 1991-92; FEDAI indicative from 1992-93; RBI reference rates from May 2012; FBIL from July 2018. Earlier fiscal years: no RBI series obtained; derive from monthly data in Phase 3 if needed, documented.",
], ["fiscal_year", "year_end", "inr_per_usd_avg", "inr_per_usd_end_year", "source_id", "confidence", "basis"], rows)
print("ok", len(rows))

# ---------- CPI-IW, financial year (RBI Table 34) ----------
# Additional raw files: pv23859.html (RBI Handbook Table 34), INDCPIALLAINMEI.csv (FRED, OECD MEI)
t = page_text("pv23859.html", "Table 34")
base, rows = "1982", []
for m in re.finditer(r"\(Base : (\d{4}) = 100 for CPI - IW\)|\b(\d{4})-(\d{2}) ([\d.]+) ([\d.]+)", t):
    if m.group(1):
        base = m.group(1)
        continue
    y0, val = int(m.group(2)), float(m.group(4))
    factor = {"1982": 4.63 * 2.88, "2001": 2.88, "2016": 1.0}[base]
    rows.append([f"FY{y0}-{m.group(3)}", y0 + 1, base, f"{val:g}", f"{val / factor:.2f}", "S0156; S0155", "high",
                 "2025-26 published to one decimal" if y0 == 2025 else ""])
cur = float(rows[-1][4])
for r in rows:
    r.insert(5, f"{cur / float(r[4]):.4f}")
write(os.path.join(OUT, "cpi_iw.csv"), [
    "title: Consumer Price Index for Industrial Workers (CPI-IW), all-India general index, financial-year average (April-March)",
    "definition: Labour Bureau CPI-IW as reproduced in RBI Handbook Table 34; value_as_published on the base in force that year; linked_2016_100 rebased with the published linking factors",
    "unit: index; linked_2016_100 has 2016=100; to_fy2025_26_inr multiplies a nominal rupee value of that year to express it in FY2025-26 rupees",
    "coverage: FY1993-94 to FY2025-26 (earlier fiscal years not in this table; use cpi_india_cy.csv for 1957-1992 calendar years)",
    "source_ids: S0156 (Labour Bureau) via S0155 (RBI Handbook Table 34, https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=23859, accessed " + ACCESSED + ")",
    "method: linking factors as published in the table's notes: 4.63 (1982 to 2001 base, general index) and 2.88 (2001 to 2016 base). Base 1982 values divided by 4.63*2.88; base 2001 values divided by 2.88.",
    "breaks: base changes at FY2005-06 (2001=100) and FY2020-21 (2016=100). Values on 1982 and 2001 bases are published as whole numbers, so linked values carry rounding error of up to about 0.2%.",
], ["fiscal_year", "year_end", "base", "value_as_published", "linked_2016_100", "to_fy2025_26_inr", "source_id", "confidence", "note"], rows)

# ---------- India CPI, calendar year (OECD MEI) ----------
o = fred("INDCPIALLAINMEI.csv")
last = max(o)
rows = [[y, f"{o[y]:.4f}", f"{o[last] / o[y]:.4f}", "S0321", "medium", ""] for y in sorted(o)]
write(os.path.join(OUT, "cpi_india_cy.csv"), [
    "title: Consumer price index for India, calendar-year average (OECD Main Economic Indicators)",
    "definition: OECD MEI series for India, total, index 2015=100 (FRED INDCPIALLAINMEI). Tracks CPI-IW: five-year changes match RBI CPI-IW within about 1% for 1994-2024, and 2019 inflation (7.7%) matches CPI-IW rather than CPI Combined (3.7%). Treat as CPI-IW-based; OECD documentation not read.",
    "unit: index 2015=100; to_" + str(last) + "_inr multiplies a nominal rupee value of that year to express it in " + str(last) + " rupees",
    "coverage: 1957-" + str(last),
    "source_ids: S0321 (OECD MEI via FRED, https://fred.stlouisfed.org/series/INDCPIALLAINMEI, accessed " + ACCESSED + ")",
    "method: values as published by FRED. Use for calendar-year rupee series and for years before FY1993-94.",
    "breaks: underlying national base changes (1960, 1982, 2001, 2016) are linked by OECD; method not documented here. Confidence medium for that reason.",
], ["year", "cpi_index_2015_100", "to_" + str(last) + "_inr", "source_id", "confidence", "note"], rows)
print("cpi ok")
