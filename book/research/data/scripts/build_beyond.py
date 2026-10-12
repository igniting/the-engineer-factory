"""Build gcc.csv, foreign_firm_india_headcount.csv, startup_funding.csv, upi.csv, computers_installed.csv.
Usage: python3 -I build_beyond.py OUT_DIR. Values transcribed; see notes/beyond_services.md."""
import csv, os, sys

OUT = sys.argv[1]


def write(name, header, cols, rows):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        for h in header:
            f.write("# " + h + "\n")
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)


write("gcc.csv", [
    "title: Global capability centres (GCCs) and MNC R&D centres in India",
    "definition: counts, employees and revenue as defined by each source; 'MNC R&D centre' (2008) is narrower than 'GCC' (2024-26, includes back-office captives)",
    "unit: centres; persons; US$ billion",
    "coverage: 2004 (new centres), 2007-08, FY2024, FY2026; 2030 projection kept separate",
    "source_ids: S0207 (Zinnov via EE Times 2008), S0141, S0317 (Nasscom-Zinnov 2024 via Reuters), S0318 (Zinnov-Nasscom FY26 via Business Today), S0140",
    "method: transcribed; projection rows flagged",
    "breaks: definitions and restatements (Nasscom restated GCC revenue in Sept 2024, S0140); all figures are from an industry body and a consultancy that sells to GCCs",
], ["period", "measure", "value", "unit", "source_id", "confidence", "note"], [
    ["2004", "new MNC R&D centres opened", 93, "centres", "S0207", "low", "read via summariser"],
    ["2007", "new MNC R&D centres opened", 24, "centres", "S0207", "low", ""],
    ["2008", "MNC R&D centres", 594, "centres", "S0207", "low", "Bangalore 312, Pune 96"],
    ["2008", "MNC R&D centre employees", 146760, "persons", "S0207", "low", ""],
    ["FY2024", "GCCs (companies)", "about 1,700", "centres", "S0317; S0141", "medium", "2,975 units (S0141); '1750+' in Nasscom release (S0140)"],
    ["FY2024", "GCC employees", 1900000, "persons", "S0317", "medium", ""],
    ["FY2024", "GCC revenue", 64.6, "US$ bn", "S0317; S0141", "medium", ""],
    ["FY2026", "GCCs", 2117, "centres", "S0318", "medium", ""],
    ["FY2026", "GCC employees", 2360000, "persons", "S0318", "medium", ""],
    ["FY2026", "GCC revenue", 98.4, "US$ bn", "S0318", "medium", ""],
    ["2030 (projection, 2024)", "GCCs", "2,100-2,200", "centres", "S0317", "medium", "PROJECTION"],
    ["2030 (projection, 2024)", "GCC employees", "2.5-2.8 million", "persons", "S0317", "medium", "PROJECTION"],
    ["2030 (projection, 2024)", "GCC revenue", "99-105", "US$ bn", "S0317", "medium", "PROJECTION"],
    ["2029 (target)", "new GCCs targeted by Karnataka policy", 500, "centres", "S0204", "low", "TARGET; via summaries"],
])

write("foreign_firm_india_headcount.csv", [
    "title: India headcount of foreign (non-Indian-headquartered) IT firms",
    "definition: employees in India as reported by the firm or press",
    "unit: persons",
    "coverage: sparse points 2005-2025",
    "source_ids: S0193, S0194, S0170, S0293, S0192, S0299",
    "method: transcribed",
    "breaks: most firms do not disclose India headcount; IBM and Accenture points are press reports of company statements",
], ["year", "firm", "india_employees", "total_employees", "source_id", "confidence", "note"], [
    ["early 2005", "IBM", 23000, "", "S0194", "medium", "'two years earlier' than Feb 2007"],
    ["early 2006", "IBM", 39000, "", "S0194", "medium", ""],
    ["Feb 2007", "IBM", 53000, "c. 300,000", "S0194", "medium", ">70,000 expected in 2007 (company)"],
    ["Aug 2007 (planned)", "Accenture", 35000, 160000, "S0193", "medium", "plan; more than US (just over 30,000)"],
    ["2021", "EPAM", 4349, "52,617 delivery", "S0170", "high", "10-K FY2021"],
    ["2024", "EPAM", 10072, "c. 55,100 delivery", "S0170", "high", "'India became our largest delivery location'"],
    ["2022", "Cognizant", 258500, 355300, "S0293", "high", "US-headquartered"],
    ["2023", "Cognizant", 254000, 347700, "S0293", "high", ""],
    ["2024", "Cognizant", 241500, 336800, "S0192", "high", ""],
    ["2025", "Cognizant", 256900, 351600, "S0299", "high", ""],
])

write("startup_funding.csv", [
    "title: Venture funding raised by Indian startups, by data vendor",
    "definition: total funding raised in the calendar year as reported by each vendor; vendors define 'startup' and 'tech' differently",
    "unit: US$ billion",
    "coverage: 2021-2024",
    "source_ids: S0147 (Tracxn via The Week, read via summariser; Inc42)",
    "method: transcribed; never splice vendors (dispute xx)",
    "breaks: Tracxn 2021 value is implied from its stated 31% decline in 2022",
], ["year", "vendor", "funding_usd_bn", "source_id", "confidence", "note"], [
    ["2021", "Tracxn (implied)", "c. 37", "S0147", "low", "implied by 2022 figure and -31%"],
    ["2021", "Inc42", "c. 42", "S0147", "low", ""],
    ["2021", "other vendor (as reported)", 43.5, "S0147", "low", "vendor not identified in register"],
    ["2022", "Tracxn", 25.7, "S0147", "medium", ""],
    ["2023", "Tracxn", 10.8, "S0147", "medium", "-58%"],
    ["2024", "Tracxn", 11.1, "S0147", "medium", "+2.11%; six unicorns"],
])

# UPI: volume lakh, value Rs crore, from RBI Handbook 'Payment System(s) Indicators' (latest edition per year)
UPI = [("FY2016-17", 180, 6961, "20468 (2021 ed., Table 63)"), ("FY2017-18", 9152, 109832, "20468"),
       ("FY2018-19", 53915, 876971, "20468"), ("FY2019-20", 125186, 2131730, "20468"),
       ("FY2020-21", 223307, 4103658, "23235 (2025 ed., Table 61)"), ("FY2021-22", 459561, 8415900, "23883 (2026 ed., Table 58)"),
       ("FY2022-23", 837144, 13914932, "23883"), ("FY2023-24", 1311295, 19995086, "23883")]
rows = [[p, v, round(v / 10000, 2), val, round(val / 100000, 2), "S0155 (RBI Handbook HTML id " + ed + ")", "high", ""] for p, v, val, ed in UPI]
rows.append(["Aug 2025 (month)", "", 20.01, "", "", "S0129 (NPCI via press)", "medium", "first month above 20 billion transactions; monthly, not annual"])
write("upi.csv", [
    "title: Unified Payments Interface (UPI) transactions, India",
    "definition: annual (April-March) volume and value of UPI transactions, RBI payment system indicators",
    "unit: volume in lakh and in billion transactions; value in Rs crore and in Rs lakh crore",
    "coverage: FY2016-17 to FY2023-24 annual; one monthly point (Aug 2025)",
    "source_ids: S0155 (RBI Handbook of Statistics on Indian Economy: 2021 ed. Table 63 id=20468; 2025 ed. Table 61 id=23235; 2026 ed. Table 58 id=23883; HTML views, accessed 2026-10-12); S0129",
    "method: latest edition per year; editions agree where they overlap (FY2017-18 9,152 lakh in 2018 and 2021 editions; FY2016-17 value revised from Rs 6,900 crore to Rs 6,961 crore)",
    "breaks: UPI introduced in FY2016-17 (RBI note). FY2024-25 not in the editions read. NPCI site unreachable from this container.",
], ["period", "volume_lakh", "volume_billion", "value_rs_crore", "value_rs_lakh_crore", "source_id", "confidence", "note"], rows)

write("computers_installed.csv", [
    "title: Computers installed in India, early counts",
    "definition: machines counted by each source; scope differs (all digital computers, IBM installations, ECIL sales, PCs in use)",
    "unit: machines",
    "coverage: 1964-2010 points",
    "source_ids: S0007, S0001, S0020, S0003, S0237",
    "method: transcribed; table, not a series",
    "breaks: different definitions; dispute (s) on IBM installations (over 150 vs 800 maintained)",
], ["date", "measure", "value", "source_id", "confidence", "note"], [
    ["end 1964", "digital computers in India", 15, "S0007", "medium", "read via summariser"],
    ["1961-64", "computers installed (12 R&D, 2 educational)", 14, "S0001 p. 18 [check]", "medium", ""],
    ["1965", "computers in India", 30, "S0020 p. 4", "high", "Committee on Automation"],
    ["1968", "computers in India", 88, "S0020 p. 4", "high", ""],
    ["1967-71", "computers introduced (5 referred for labour screening)", 94, "S0020 p. 4", "high", ""],
    ["1970", "IBM 1401 installations", "about 80", "S0001 p. 19", "high", ""],
    ["Aug 1971", "computers in India (govt 10, PSU 39, private 55, R&D 36)", 140, "S0020 p. 25", "high", ""],
    ["1971-78", "ECIL computers sold (4 to private sector)", 98, "S0001 pp. 25-26", "high", "plus 75 ruggedised TDC-316s for defence"],
    ["1974", "IBM share of installations", "65% of 217", "S0003 p. 800", "high", ""],
    ["1977-78", "IBM installations", "over 150", "S0001 p. 29", "high", "dispute (s): Dataquest says CMC maintained 800 (S0237)"],
    ["1978", "computers in India", "less than 1,000", "S0001 p. 29", "high", ""],
    ["1990", "computers in India", 80000, "S0001 p. 29", "high", "growth after the 1984 policy (Ch. 8); scope not defined"],
    ["2010", "personal computers in use", "over 60 million", "S0001 p. 7", "medium", ""],
])
print("ok")
