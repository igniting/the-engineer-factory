# Notes: graduate_unemployment.csv, employability_tests.csv, fresher_pay.csv

**Built:** 2026-10-12 by `scripts/build_labour.py`.

## Graduate unemployment
- **Sources by year.** PLFS usual-status rate for graduates aged 15+:
  - 17.2% (2019-20), 15.5% (2020-21) and 14.9% (2021-22), from the government's own release (PIB, Lok Sabha reply, 20 March 2023, S0326);
  - 13.4% (2022-23), via PTI (S0327);
  - 11.2% (2023-24), from *ETV Bharat* only (S0328).
- **Dispute (ooo).** This register's earlier S0154 note gave 13.0% for 2023-24, against 11.2% in S0328. The original documents (DGE and Rajya Sabha) are unreachable from this container.
- **Register correction.** The S0154 note's '17.2% (2017-18)' was wrong: 17.2% is the 2019-20 figure.
- **Missing years.** 2017-18 and 2018-19 were not obtained.
- **Contrast figures.** All persons aged 15+: 3.2% in 2023-24 (MoSPI, S0329). The Azim Premji University report's 39.3% for graduates under 25 (2023, via S0328) uses a different population and is kept as a separate row.
- **US points.** CS graduates 6.1% and computer engineering graduates 7.5% (ages 22-27, 2025), as cited in the US proclamation (S0136).
- **Blocked sources.** dge.gov.in, rsdebate, data.gov.in and AISHE reset connections from this container. mospi.gov.in works, but the PLFS annual-report PDFs were not located there. The PARI mirror page is JavaScript-only.

## Employability tests (M07)
- **2014 report** (2013 graduates, more than 120,000 students): IT services 18.43%, products 3.21%, BPO 39.84%.
- **2016 report** (more than 150,000 students, 650+ colleges): IT services 17.91%, products 3.67%, BPO 40.57%, startups 3.84%.
- **Caveat for every use.** These are a test vendor's benchmarks for its own product (AMCAT), not labour-market outcomes. Name the vendor and the role each time.

## Fresher pay
These are points, not a series, and the measures differ (median across firms, single-firm package, quoted ranges).
- **Median for large IT firms** (Moneycontrol study via HR Katha, S0331): Rs 2.45 lakh (2012) and Rs 3.55 lakh (2022). In 2024 rupees (OECD CPI) that is Rs 4.77 lakh and Rs 3.89 lakh, **a real fall of about 18%** over the decade.
- **The 2007 TCS package** (Rs 3.16 lakh, about Rs 9.9 lakh in 2024 rupees) rests on a Reddit post relayed by *Business Today* (S0330). Do not use it as evidence.
- **Corroboration.** Quoted ranges point the same way: Wipro's CHRO in April 2025 (Rs 3-4 lakh, 'flat for over a decade', S0334); T.V. Mohandas Pai in 2022 (Rs 3.5-4 lakh, 'the same' as 10-12 years earlier, S0333); TeamLease Digital (Rs 2-2.5 lakh in 2014, Rs 3-3.5 lakh in 2025, S0332).
- **Missing.** No firm discloses fresher pay in its SEC filings as read. Premium tracks (TCS Digital and Prime, HCLTech 'Elite', Infosys specialist roles up to Rs 21 lakh) are excluded.

## Use in drafting
- **Prologue, Ch. 18 and 19.** Fresher pay was roughly flat in nominal terms from 2012 to 2025, so it fell in real terms. Meanwhile applications to Infosys reached 5.9 million (fresher_hiring.csv) and graduate unemployment fell from 17.2% to 13.4% (2019-23). Present all three without implying a causal link.
