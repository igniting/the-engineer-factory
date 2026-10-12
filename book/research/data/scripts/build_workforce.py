"""Build industry_workforce.csv. Usage: python3 -I build_workforce.py OUT_DIR
All values transcribed from the cited pages; see notes/industry_workforce.md."""
import csv, os, sys

OUT = sys.argv[1]
# (period, period_type, year_end, column, value, definition, source, page, confidence, note)
POINTS = [
    ("FY1989-90", "FY", 1990, "nasscom", 56000, "software professionals employed by the Indian software industry", "S0259", "p. 41", "medium",
     "NASSCOM figure quoted in Infosys's 1999 prospectus ('fiscal 1990')"),
    ("1996", "CY", 1996, "nasscom", 160000, "software professionals", "S0254; S0001", "S0254 p. 5; S0001 p. 43", "medium",
     "Rajaraman gives 160,000 'software engineers' in a passage on 1991-97; period approximate"),
    ("FY1997-98", "FY", 1998, "nasscom", 200000, "software professionals employed by the Indian software industry", "S0259", "p. 41", "medium",
     "NASSCOM figure quoted in Infosys's 1999 prospectus ('fiscal 1998')"),
    ("FY2007-08", "FY", 2008, "nasscom", 2000000, "IT-BPO direct employees ('nearly 2 million', 'the 2 million professionals')", "S0107", "slide 2", "medium",
     "FY2008 estimate; lobby presentation"),
    ("2010", "CY", 2010, "rajaraman", 2400000, "direct employment in IT ('2.4 million in IT and 8.2 million in support services')", "S0001", "pp. 5, 7, 80", "medium",
     "Rajaraman's chronology; underlying source is NASSCOM; indirect 8.2m not entered"),
    ("FY2023-24", "FY", 2024, "nasscom", 5670000, "technology industry direct employees, restated after 2024 GCC reassessment", "S0140", "p. 1 (Note to Editors)", "medium",
     "Restated FY2024 figure in the 2025 Strategic Review release"),
    ("FY2023-24", "FY", 2024, "niti_low", 7500000, "total tech workforce incl. tech jobs in other sectors (2023)", "S0316", "PDF p. 6; printed p. 12", "medium",
     "Not comparable with Nasscom: all sectors, calendar 2023; NITI gives 7.5-8 million"),
    ("FY2023-24", "FY", 2024, "niti_high", 8000000, "total tech workforce incl. tech jobs in other sectors (2023)", "S0316", "PDF p. 6; printed p. 12", "medium",
     "Upper end of NITI's range"),
    ("FY2024-25", "FY", 2025, "nasscom", 5800000, "technology industry direct employees, FY2025E", "S0140", "p. 1", "medium",
     "Estimate made in Feb 2025 ('126,000 net hiring with a total headcount of 5.8 Mn'); revised to 58.15 lakh in Feb 2026 (S0306)"),
    ("FY2024-25", "FY", 2025, "nasscom_revised", 5815000, "technology industry direct employees, FY25 as revised", "S0306", "PTI report", "medium",
     "Revised base given with the FY26 figure"),
    ("FY2025-26", "FY", 2026, "nasscom", 5950000, "technology industry direct employees, FY26 estimate (59.5 lakh)", "S0306", "PTI report", "medium",
     "Net additions 1.35 lakh (2.3%) against revenue growth of 6.1%"),
]
NET = {"FY2024-25": ("126,000 (Feb 2025 est.); 1.33 lakh (as revised, S0306)", "S0140; S0306"),
       "FY2025-26": ("1.35 lakh", "S0306")}

cols = ["nasscom", "nasscom_revised", "rajaraman", "niti_low", "niti_high"]
rows = {}
for p, pt, ye, col, val, defn, src, page, conf, note in POINTS:
    r = rows.setdefault(p, {"period": p, "period_type": pt, "year_end": ye, "defs": [], "src": [], "notes": [], "conf": conf})
    r[col] = val
    r["defs"].append(f"{col}: {defn}")
    r["src"].append(f"{src} ({page})")
    r["notes"].append(note)

with open(os.path.join(OUT, "industry_workforce.csv"), "w", newline="") as f:
    for h in [
        "title: Employment in India's software/IT industry, persons, point estimates by source",
        "definition: separate columns per source and definition; the industry's scope widens over time (software professionals -> IT-BPO -> 'technology industry' incl. BPM, ER&D, products, GCCs)",
        "unit: persons",
        "coverage: FY1989-90 to FY2025-26, sparse points only (no annual series obtained)",
        "source_ids: S0259 (Infosys 424B4 prospectus 1999, quoting NASSCOM), S0254, S0001, S0107, S0140, S0306, S0316",
        "method: values transcribed as published. No reconciled column. NITI's all-sector range kept in niti_low/niti_high and never compared with Nasscom.",
        "breaks: every Nasscom point uses the definition current at the time; FY2024 restated upward after the 2024 GCC reassessment (S0140). PLFS-based levels (S0154, S0211) not obtained.",
    ]:
        f.write("# " + h + "\n")
    w = csv.writer(f)
    w.writerow(["period", "period_type", "year_end", "nasscom_direct_employees", "nasscom_revised",
                "rajaraman_direct_employment", "niti_all_sector_low", "niti_all_sector_high",
                "nasscom_net_additions", "definitions", "source_id", "confidence", "note"])
    for p in sorted(rows, key=lambda k: (rows[k]["year_end"], k)):
        r = rows[p]
        w.writerow([p, r["period_type"], r["year_end"]] + [r.get(c, "") for c in cols] +
                   [NET.get(p, ("", ""))[0], " | ".join(r["defs"]), "; ".join(r["src"] + ([NET[p][1]] if p in NET else [])),
                    r["conf"], " | ".join(n for n in r["notes"] if n)])
print("ok", len(rows))
