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
