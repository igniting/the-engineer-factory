# Notes: reference series (us_cpi_u, inr_usd, inr_usd_fy)

**Built:** 2026-10-12 by `scripts/build_reference.py` from files downloaded the same day (raw files kept outside the repo; URLs in each CSV header).

## Decisions
- **Exchange rate, calendar year.** Three series are kept side by side (RBI, Federal Reserve G.5A, Penn World Table 11.0). The preferred column uses RBI from 1987, G.5A for 1973-86 and PWT for 1950-72. Overlap years agree within 0.3% (1987, 1991, 2010), so the preferred column has no visible break. The rule is stated in the header (house rule: no silent splicing).
- **Exchange rate, financial year.** RBI only, FY1986-87 to FY2025-26. Use for fiscal-year flow series such as Nasscom revenue (house rule D3). For fiscal years before 1986-87 no official FY series was obtained. If needed, compute April-March averages from monthly G.5A data (FRED EXINUS, from 1973) and document it as a derived series.
- **US CPI-U.** BLS annual averages 1950-2025. `to_2025_usd` converts a nominal dollar value to 2025 dollars. 2025's average rests on 11 months, because BLS has no October 2025 value.

## Gaps and checks
1. **The rupee's pre-1993 regime** (parity, sterling link, basket) is described in the CSV header from background knowledge. Source it in Phase 5, e.g. RBI *History* volumes or Joshi and Little.
2. **S0001's '1951: Rs 4.5'** does not match the official parity of about Rs 4.76. Recorded as approximate.
3. **The 2026 values** (CPI January-August; FY2025-26 exchange rate) are live data and should be refreshed at final assembly.
4. **RBI Handbook XLSX and PDF files on rbidocs** are blocked by a CAPTCHA. The HTML table views on rbi.org.in work and were used.

## CPI (added 2026-10-12)
- **`cpi_iw.csv`.** RBI Handbook Table 34, fiscal years FY1993-94 to FY2025-26. It is linked to 2016=100 with the factors the table itself publishes (4.63; 2.88). `to_fy2025_26_inr` gives FY2025-26 rupees. Values on the old bases are whole numbers, so linked values carry about 0.2% rounding error.
- **`cpi_india_cy.csv`.** OECD MEI India CPI, calendar years 1957-2024 (2015=100), used for calendar-year rupee series and for anything before FY1993-94.
  - **How it was tested.** Over 1994-2024 its five-year changes match RBI's CPI-IW within about 1%. Its 2019 inflation (7.7%) matches CPI-IW, not CPI Combined (3.7%, World Bank FPCPITOTLZGIND). The OECD's own source note was not read, so confidence is medium.
- **Gap.** The planned 1960=100 CPI-IW series, and its linking factor to 1982=100, were not obtained. The OECD series makes it unnecessary for deflation, but the book should not quote CPI-IW index numbers before 1993-94.
- **Rule for drafting.** Fiscal-year rupee values: deflate with `cpi_iw.csv`. Calendar-year rupee values, or any year before FY1993-94: deflate with `cpi_india_cy.csv`. State which one in each table note.
