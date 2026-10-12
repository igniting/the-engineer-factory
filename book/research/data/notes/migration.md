# Notes: migration files

**Built:** 2026-10-12 by `scripts/build_migration.py`.

## h1b_country.csv
- **Recent years.** India-born beneficiaries were 72.3% of approved H-1B petitions in FY2023 and 71.0% in FY2024 (USCIS annual reports to Congress, S0336, S0335). China was 11.7% in both years.
- **The split that matters.** India's share is 57-58% of petitions for initial employment but 79% of continuing ones. So the stock of Indian H-1B workers is larger than the flow of new ones.
- **Earlier points.** About 1999-2000: 48.5% of approvals (INS, via a law-firm reproduction, S0104). FY2005: 49.0% of new arrivals (CRS, S0105, a different measure).
- **Source checks.** The FY2024 report was read from a mirror (poder360.com.br). Its FY2020-23 approvals table matches the FY2023 report on govinfo exactly, so the copy is taken as authentic. The FY2024 report also contradicts itself slightly: India is 283,397 in Figure 5 and 283,755 in Table 4a.
- **Gap.** uscis.gov returns 'Access Denied' to this container, so the FY2000-22 reports were not obtained.

## h1b_employer.csv (tests M11)
- **What it covers.** NFAP's compilations from the USCIS Employer Data Hub, FY2022-25 (S0337, S0338). NFAP is a pro-immigration policy group; its tables reproduce USCIS counts but group affiliates by its own judgement.
- **FY2025.** Amazon 4,644, Meta 1,555, Microsoft 1,394 and Google 1,050 lead. TCS has 846 and Cognizant 743; Infosys 263 and Wipro 267 are outside the top 25.
- **FY2024.** Cognizant 2,837 (2,873 in the later brief), Infosys 2,504, TCS 1,452.
- **NFAP's summary.** The top seven Indian-based firms had 4,573 approvals in FY2025, '70% from FY 2015' lower.
- **The administration's claim** of a 92% fall in registrations by the largest outsourcers (S0300) is kept as a separate, low-confidence row.

## h1b_policy.csv
- The cap and the number of petitions issued against it, 1992-2026 (NFAP Appendix Table 1).
- Dated events from CRS (S0105), USCIS (S0335), the proclamations (S0136, S0300) and the court summaries (S0137).

## indian_students_us.csv
- **Totals (Open Doors, India fact sheet 2025, S0158).** 196,271 (2017/18), a trough of 167,582 (2020/21), then 363,019 (2024/25).
- **2024/25 split.** Graduate students 177,892 (down 9.5%); OPT 143,740 (up 47.3%).
- **Gap.** Earlier years back to the 1950s exist in Open Doors but were not obtained.

## iit_emigration.csv
- **IIT Bombay, 1970s.** Slightly over 40% of IIT Bombay EE graduates of 1973-77 were abroad (Sukhatme via Bassett, S0003, p. 803).
- **JEE 2010.** 36% of the top 1,000 JEE 2010 scorers, and 62% of the top 100, had migrated (Choudhury, Ganguli and Gaulé, NBER w31308, S0172).
- **Caution.** These are not a trend: different institutions, cohorts and methods.

## Use in drafting (Ch. 13, 19)
FY2023-25 shows a switch: US technology firms replaced Indian IT firms at the top of new H-1B approvals, before the $100,000 fee took effect (September 2025). The decline therefore predates the fee, and the book should not credit the fee with the fall in FY2025 approvals. FY2025 ended on 30 September 2025, nine days after the fee began.
