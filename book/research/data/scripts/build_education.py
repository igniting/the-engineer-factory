"""Build engineering_intake.csv and engineering_graduates.csv. Usage: python3 -I build_education.py OUT_DIR
Values transcribed from cited sources; see notes/education.md."""
import csv, os, sys

OUT = sys.argv[1]
LAKH = 100000

# Engineering/technology colleges (MoSPI compilation, S0248): academic year -> count
COLLEGES = {"1950-51": 31, "1960-61": 76, "1970-71": 107, "1980-81": 149, "1985-86": 242, "1989-90": 285,
            "1990-91": 289, "1994-95": 337, "1995-96": 355, "1997-98": 486, "2000-01": 678, "2001-02": 1077,
            "2005-06": 1562}
# AICTE approved intake, all engineering levels (degree + diploma + PG), Lok Sabha reply Dec 2021 via Careers360 (S0323)
INTAKE_ALL = {"2012-13": 2695333, "2021-22": 2366728}
# AICTE approved intake by level, Avanti Fellows from AICTE panel (S0267), lakh
INTAKE_LEVEL = {"2012-13": (15.49, 10.08, 1.38), "2014-15": (17.05, 12.62, 2.16), "2021-22": (12.53, 9.77, 1.37)}
# Enrolment (first-year admissions against AICTE intake), all engineering levels, Lok Sabha reply via Careers360 (S0323)
ENROL_ALL = {"2012-13": 1751538, "2013-14": 1784127, "2014-15": 1739357, "2015-16": 1677754, "2016-17": 1559229,
             "2017-18": 1486462, "2018-19": 1416319, "2019-20": 1410683, "2020-21": 1275880}
# Vacancy share of approved seats (Avanti, S0267), percent: (UG engineering, diploma)
VACANCY = {"2012-13": (37.6, 32.2), "2016-17": (49.5, 43.3), "2019-20": (44.3, 41.8), "2020-21": (44.1, 49.1),
           "2021-22": (34.1, 49.4)}
# Careers360 2023 table 'BTech: seats, enrolment' from AICTE data (S0324): definition unclear, kept apart
C360_2023 = {"2019-20": (2368590, 1384326), "2020-21": (2442918, 1295347), "2021-22": (2539502, 1411001)}
# AISHE BE/BTech enrolment, all years of study (via S0324): calendar labels as published
AISHE_BTECH = {"2016-17": 4085321, "2020-21": 3663685}
# IIT seats (S0001 p. 34)
IIT = {"1978-79": (1500, "over 100,000 candidates")}

years = sorted(set(COLLEGES) | set(INTAKE_ALL) | set(INTAKE_LEVEL) | set(ENROL_ALL) | set(VACANCY) | set(C360_2023) | set(AISHE_BTECH) | set(IIT))
with open(os.path.join(OUT, "engineering_intake.csv"), "w", newline="") as f:
    for h in [
        "title: Engineering education capacity in India: institutions, approved intake, enrolment and vacancy",
        "definition: separate columns per source and definition. 'approved intake' = AICTE maximum admissions excl. supernumerary seats (AICTE institutions only; IITs outside AICTE).",
        "  enrolment_all_levels_first_year = students admitted against AICTE intake, all engineering levels (degree, diploma, PG), as given to Lok Sabha;",
        "  aishe_be_btech_enrolment_all_years = students enrolled in all years of BE/BTech study (AISHE), a stock, not an intake.",
        "unit: institutions; persons; percent",
        "coverage: institutions 1950-51 to 2005-06; intake and enrolment 2012-13 to 2021-22; IIT seats 1978",
        "source_ids: S0248 (MoSPI table 1.17); S0323 (Lok Sabha reply Dec 2021 via Careers360); S0267 (Avanti Fellows analysis of AICTE panel and AISHE); S0324 (Careers360 Apr 2023, AICTE and AISHE data); S0001 p. 34",
        "method: lakh converted at 100,000. Reconciliation: Avanti's UG+diploma+PG intake equals the Lok Sabha all-level intake in both overlap years (2012-13: 26.95 lakh; 2021-22: 23.67 lakh).",
        "breaks: AICTE 2022-23 data is an incomplete load (per S0267) and is not used; AICTE 'placed' data is unusable (per S0267). The Careers360 2023 'BTech' intake (23.7-25.4 lakh) does not match the UG-only or all-level series; definition unclear; low confidence.",
    ]:
        f.write("# " + h + "\n")
    w = csv.writer(f)
    w.writerow(["academic_year", "eng_tech_colleges", "aicte_intake_all_levels", "aicte_intake_ug_degree", "aicte_intake_diploma",
                "aicte_intake_pg", "enrolment_all_levels_first_year", "vacancy_ug_pct", "vacancy_diploma_pct",
                "c360_btech_intake_2023table", "c360_btech_enrolment_2023table", "aishe_be_btech_enrolment_all_years",
                "iit_seats", "source_id", "confidence", "note"])
    for y in years:
        lv = INTAKE_LEVEL.get(y)
        src = []
        if y in COLLEGES: src.append("S0248")
        if y in INTAKE_ALL or y in ENROL_ALL: src.append("S0323")
        if lv or y in VACANCY: src.append("S0267")
        if y in C360_2023 or y in AISHE_BTECH: src.append("S0324")
        if y in IIT: src.append("S0001 p. 34")
        conf = "high" if (y in COLLEGES or y in INTAKE_ALL or y in ENROL_ALL) else ("medium" if (lv or y in VACANCY) else "low")
        note = ""
        if y in IIT: note = "1,500 IIT seats for " + IIT[y][1]
        if y == "2014-15": note = "peak approved intake at UG, diploma and PG levels (S0267)"
        w.writerow([y, COLLEGES.get(y, ""), INTAKE_ALL.get(y, ""),
                    int(lv[0] * LAKH) if lv else "", int(lv[1] * LAKH) if lv else "", int(lv[2] * LAKH) if lv else "",
                    ENROL_ALL.get(y, ""), VACANCY.get(y, ("", ""))[0], VACANCY.get(y, ("", ""))[1],
                    C360_2023.get(y, ("", ""))[0], C360_2023.get(y, ("", ""))[1], AISHE_BTECH.get(y, ""),
                    IIT[y][0] if y in IIT else "", "; ".join(src), conf, note])

GRAD = [
    ("2004", "engineering_cs_it_bachelors", 112000, "S0213 pp. 5, 8", "medium", "NASSCOM projection reported by Duke study; four-year degrees"),
    ("2004", "engineering_cs_it_diplomas", 103000, "S0213 pp. 5, 8", "medium", "three-year diplomas"),
    ("2004", "engineering_cs_it_total", 215000, "S0213 p. 5", "medium", "bachelor's plus diploma"),
    ("c. 2013", "engineering_graduates_claimed", 600000, "S0153 p. 7", "low", "Aspiring Minds: 'the six hundred thousand engineers that graduate annually'; no source given"),
    ("c. 2010", "rajaraman_1_3_million", 1300000, "S0001 pp. 12, 56", "low", "Rajaraman calls this both 'students' (p. 56) and graduates 'per year' (p. 12); probably intake (dispute ii); do not use as graduates"),
]
with open(os.path.join(OUT, "engineering_graduates.csv"), "w", newline="") as f:
    for h in [
        "title: Engineering graduates (out-turn) in India, point estimates",
        "definition: measure column states what is counted; degree vs diploma kept apart",
        "unit: persons per year",
        "coverage: 2004 and c. 2013 only (AISHE out-turn tables not obtained)",
        "source_ids: S0213 (Duke 2005), S0153 (Aspiring Minds 2014), S0001",
        "method: transcribed as published",
        "breaks: no consistent series. The Rajaraman 1.3 million row is kept only to document dispute (ii) and myth M08.",
    ]:
        f.write("# " + h + "\n")
    w = csv.writer(f)
    w.writerow(["period", "measure", "value", "source_id", "confidence", "note"])
    w.writerows(GRAD)
print("ok", len(years))
