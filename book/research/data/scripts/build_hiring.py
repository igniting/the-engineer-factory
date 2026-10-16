"""Build fresher_hiring.csv and firm_women_attrition.csv. Usage: python3 -I build_hiring.py OUT_DIR
Values transcribed from company filings and press reports; see notes/hiring_attrition.md."""
import csv, os, sys

OUT = sys.argv[1]

# Infosys recruitment funnel (Item 6.D 'Employees'; prospectus for FY1998). Offers are ALL offers of employment
# (campus and lateral) unless stated. (fy_end, applications, tested, interviewed, offers, accepted, source, qualifier)
INFY = [
    (1998, 70870, 21350, 5800, 1790, 1300, "S0259 (424B4 prospectus, 1999)", "approximately"),
    (2001, 385200, 49100, 20800, 7650, 6100, "S0322 (20-F FY2001)", "approximately"),
    (2002, 193640, "", 6730, 1710, 1550, "S0260 (20-F FY2002)", "approximately"),
    (2004, 908500, "", 18200, 13600, "", "S0270 (20-F FY2004)", "approximately"),
    (2005, 1348800, 122000, 36600, 14500, "", "S0264 (20-F FY2005)", "approximately; tested 'over'"),
    (2008, 885000, 227500, 97600, 46300, "", "S0265 (20-F FY2008)", "approximately/over"),
    (2009, 488700, 77600, 46600, 16900, "", "S0271 (20-F FY2009)", "approximately"),
    (2010, 400800, 77000, 61000, 26200, "", "S0272 (20-F FY2010)", "approximately"),
    (2012, 622970, "", 60860, 41460, "", "S0266 (20-F FY2012)", "approximately"),
    (2020, 2141373, "", 150130, 83319, "", "S0287 (20-F FY2020)", "exact"),
    (2021, 1427618, "", 135216, 48029, "", "S0288 (20-F FY2021)", "exact"),
    (2022, 5866636, "", 523385, 222500, "", "S0289 (20-F FY2022)", "exact"),
    (2023, 5342299, "", 389183, 114374, "", "S0290 (20-F FY2023)", "exact"),
    (2024, 2436929, "", 194367, 26975, "", "S0291 (20-F FY2024)", "exact"),
    (2025, 4457748, "", 430080, 83207, "", "S0296 (20-F FY2025)", "exact"),
    (2026, 5884480, "", 450901, 87286, "", "S0297 (20-F FY2026)", "exact"),
]
# Other firms: fresher-specific figures from press (period, firm, measure, value, source, confidence, note)
OTHER = [
    ("FY2025-26", "TCS", "freshers_hired", 44000, "S0309", "low", "'reportedly' over 44,000 freshers hired in FY26 (Business Today)"),
    ("FY2026-27", "TCS", "fresher_offers", 25000, "S0309; S0139", "medium", "offers made by April 2026; 'Clarity on demand will lead to more hiring' (CEO to PTI); BS frames it against a usual c. 40,000"),
    ("Q1 FY2026-27", "TCS", "freshers_joined", 14000, "S0310", "medium", "approximately 14,000 joined by end of Q1"),
    ("Q2 FY2026-27", "TCS", "freshers_joined", 10000, "S0138", "medium", "onboarded in the quarter to 30 Sep 2026 (POST-CUTOFF)"),
    ("FY2026-27", "Infosys", "fresher_plan", 20000, "S0139", "medium", "company said it will add 20,000 freshers (plan, not hires)"),
    ("FY2025-26", "HCLTech", "freshers_hired", 11000, "S0139", "medium", "'over 11,000 graduates last fiscal'"),
    ("FY2023-24", "Infosys", "freshers_hired", 11900, "S0133 (HR Katha)", "low", "'hired only 11,900 new graduates this year' vs 50,000 the previous year (as reported, citing other reports)"),
    ("FY2022-23", "Infosys", "freshers_hired", 50000, "S0133 (HR Katha)", "low", "as reported"),
]

with open(os.path.join(OUT, "fresher_hiring.csv"), "w", newline="") as f:
    for h in [
        "title: Recruitment funnel and fresher hiring, by firm and fiscal year",
        "definition: Infosys rows are the company's annual recruitment statistics (applications received, tested, interviewed, offers of employment extended, offers accepted).",
        "  From FY2004 the offers figure is all 'offers of employment' (campus and lateral), not freshers only. Other rows are fresher-specific press figures; measure column says which.",
        "unit: persons",
        "coverage: Infosys FY1998-FY2026 (gaps FY1999-2000, FY2003, FY2006-07, FY2011, FY2013-19); TCS, HCLTech and Infosys press points FY2023-FY2027",
        "source_ids: S0259, S0322, S0260, S0270, S0264, S0265, S0271, S0272, S0266, S0287-S0291, S0296, S0297 (Infosys, Item 6.D or prospectus 'Human resources'); S0309, S0310, S0138, S0139, S0133",
        "method: transcribed as published. offer_rate_per_1000_applications computed = offers / applications * 1000.",
        "breaks: 'tested' not reported from FY2012 onward; FY2005 20-F gives two phrasings (interviewed 'over 36,600' and 'approximately 36,600'). Offers vs hires vs joiners are different measures: never compare across columns.",
    ]:
        f.write("# " + h + "\n")
    w = csv.writer(f)
    w.writerow(["firm", "period", "year_end", "measure", "applications", "tested", "interviewed", "offers", "accepted",
                "value", "offer_rate_per_1000_applications", "qualifier", "source_id", "confidence", "note"])
    for y, a, t, i, o, acc, s, q in INFY:
        w.writerow(["Infosys", f"FY{y-1}-{str(y)[2:]}", y, "funnel", a, t, i, o, acc, "", f"{o / a * 1000:.1f}", q, s, "high",
                    "offers include laterals" if y >= 2004 else ""])
    for p, firm, m, v, s, c, n in OTHER:
        ye = int(p[-7:-3]) + 1 if p.startswith(("FY", "Q")) else ""
        w.writerow([firm, p, ye, m, "", "", "", "", "", v, "", "", s, c, n])

# Attrition and women's share (period, firm, attrition_pct, attrition_definition, women_pct, women_definition, source, confidence)
AW = [
    ("FY2005-06", "Infosys", 11.2, "comparable attrition, excl. Infosys BPO and subsidiaries", "", "", "S0265 (20-F FY2008)", "high"),
    ("FY2006-07", "Infosys", 13.7, "comparable attrition, excl. Infosys BPO and subsidiaries", "", "", "S0265", "high"),
    ("FY2007-08", "Infosys", 13.4, "comparable attrition, excl. Infosys BPO and subsidiaries", "", "", "S0265", "high"),
    ("FY2008-09", "Infosys", 11.1, "attrition excl. Infosys BPO and subsidiaries", "", "", "S0271 (20-F FY2009)", "high"),
    ("FY2009-10", "Infosys", 13.4, "attrition (as stated)", "", "", "S0272 (20-F FY2010)", "high"),
    ("FY2010-11", "Infosys", 17.0, "attrition, twelve months to 31 March", "", "", "S0266 (20-F FY2012)", "high"),
    ("FY2011-12", "Infosys", 14.7, "attrition, twelve months to 31 March", "", "", "S0266", "high"),
    ("FY2023-24", "Infosys", "", "", 40, "'nearly 40%' of workforce (quoted statement in 20-F)", "S0291 (20-F FY2024)", "medium"),
    ("FY2019-20", "Infosys", 15.1, "voluntary attrition, standalone, Q4 (quarter to 31 Mar 2020); total 18.2", "", "", "S0381 (6-K Ex. 99.5 call 20 Apr 2020)", "medium"),
    ("FY2020-21", "Infosys", 15.2, "voluntary attrition, IT services, Q4 annualised", "", "", "S0381 (6-K Ex. 99.5 call 14 Apr 2021)", "medium"),
    ("FY2021-22", "Infosys", 27.7, "voluntary attrition, LTM to 31 Mar", "", "", "S0381 (6-K Ex. 99.5 call 13 Apr 2022)", "high"),
    ("FY2022-23", "Infosys", 20.9, "voluntary attrition, LTM to 31 Mar (IT services per Q4 FY2024 fact sheet)", "", "", "S0381 (6-K Ex. 99.5 call 13 Apr 2023; Ex. 99.4 18 Apr 2024)", "high"),
    ("FY2023-24", "Infosys", 12.6, "voluntary attrition, LTM, IT services", 39.3, "women share of employees at 31 Mar 2024 (fact sheet)", "S0381 (6-K Ex. 99.4 Fact Sheet Q4 FY2024)", "high"),
    (2020, "Cognizant", 20.6, "total attrition (voluntary and involuntary)", 36, "women share of workforce at 31 Dec", "S0293 (10-K FY2021)", "high"),
    (2021, "Cognizant", 30.8, "total attrition (voluntary and involuntary)", 38, "women share at 31 Dec (c. 123,000 women)", "S0293", "high"),
    (2022, "Cognizant", 31.7, "total attrition (voluntary and involuntary)", 38, "women share at 31 Dec (c. 134,000 women)", "S0293", "high"),
    (2022, "Cognizant", 25.6, "Voluntary Attrition - Tech Services", "", "", "S0293 (10-K FY2023)", "high"),
    (2023, "Cognizant", 13.8, "Voluntary Attrition - Tech Services", 38, "women share 'approximately 38%'", "S0293", "high"),
    (2024, "Cognizant", 15.9, "Voluntary Attrition - Tech Services", 38, "women share 'approximately 38%'", "S0192 (10-K FY2024)", "high"),
    (2025, "Cognizant", 13.9, "Voluntary Attrition - Tech Services", 39, "women share 'approximately 39%'", "S0299 (10-K FY2025)", "high"),
    ("FY2019-20", "TCS", 12.1, "attrition at 31 Mar 2020 as reported (basis not stated in the reports; press reports of Q4 results)", "", "", "S0384 (HR Katha 17 Apr 2020); S0385 (Communications Today 17 Apr 2020)", "medium"),
    ("FY2020-21", "TCS", 7.2, "attrition for FY2020-21 as reported (basis not stated; one outlet)", "", "", "S0384 (HR Katha 13 Apr 2021)", "low"),
    ("FY2021-22", "TCS", 17.4, "attrition, trailing 12 months to 31 Mar 2022, as reported", "", "", "S0385 (The News Minute with PTI 11 Apr 2022)", "medium"),
    ("FY2022-23", "TCS", 20.1, "attrition, LTM to 31 Mar 2023, as reported (one outlet)", "", "", "S0384 (HR Katha 21 Apr 2023)", "low"),
    ("FY2023-24", "TCS", 12.5, "attrition at 31 Mar 2024 (Q4), as reported (basis not stated; one outlet)", "", "", "S0384 (HR Katha 12 Apr 2024)", "low"),
    ("FY2024-25", "TCS", 13.3, "LTM attrition, IT services", 35.2, "women share of workforce", "S0160 (Q4 FY2024-25 fact sheet)", "medium"),
    ("Q2 FY2026-27", "TCS", 13.3, "12-month trailing attrition (to 30 Sep 2026)", "", "", "S0310", "medium"),
]
with open(os.path.join(OUT, "firm_women_attrition.csv"), "w", newline="") as f:
    for h in [
        "title: Attrition rate and women's share of workforce, by firm",
        "definition: each row states the firm's own attrition definition (total vs voluntary; with or without subsidiaries; IT services only) and women's-share basis",
        'unit: percent',
        'coverage: Infosys attrition FY2005-06 to FY2011-12 and FY2019-20 to FY2023-24, women FY2023-24; Cognizant 2020-2025; TCS FY2019-20 to FY2024-25 and Q2 FY2026-27',
        'source_ids: S0265, S0271, S0272, S0266, S0291 (Infosys 20-F); S0381 (Infosys 6-K call transcripts and Q4 FY2024 fact sheet); S0293, S0192, S0299 (Cognizant 10-K); S0160, S0310 (TCS); S0384, S0385 (TCS FY2019-20 to FY2023-24, press reports of quarterly results)',
        'method: transcribed as published; two Cognizant 2022 rows because the 10-K changed its headline metric from total to voluntary (tech services) attrition',
        'breaks: definitions differ between firms and over time (Infosys moves from quarterly or annualised voluntary attrition in FY2019-20 and FY2020-21 to LTM voluntary attrition from FY2021-22; TCS FY2019-20 to FY2023-24 are press-reported, with the LTM basis stated only for FY2021-22 and FY2022-23, and are not voluntary-only measures); do not compare across rows with different attrition_definition',
    ]:
        f.write("# " + h + "\n")
    w = csv.writer(f)
    w.writerow(["firm", "period", "attrition_pct", "attrition_definition", "women_pct", "women_definition", "source_id", "confidence"])
    for p, firm, a, ad, wp, wd, s, c in AW:
        w.writerow([firm, p, a, ad, wp, wd, s, c])
print("ok")
