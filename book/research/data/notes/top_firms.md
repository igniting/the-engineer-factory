# Notes: top_firms.csv

**Built:** 2026-10-12 by `scripts/build_firms.py`.

## Sources and where each value comes from

**Infosys revenue.** Two kinds of source:
- The '[revenues] grew from $X million in fiscal Y to $Z million in fiscal W' sentences in Item 5 of each 20-F:
  - FY1999 $121.0m (20-F FY2004, S0270);
  - FY2001 $414m (S0264);
  - FY2004 $1,063m (S0265);
  - FY2005 $1,592m (S0264);
  - FY2008 $4,176m (S0265);
  - FY2009 $4,663m (S0271);
  - FY2010 $4,804m (S0272);
  - FY2012 $6,994m (S0266);
  - FY2026 $20,158m (S0297).
- SEC XBRL company facts (RevenueFromContractsWithCustomers) for FY2016-FY2025. These match the 20-F sentences where both exist.

**Infosys employees.** At 31 March, from the 'total employees grew from ... to ...' sentences and the Employees sections.

**Wipro revenue.** INR million, consolidated:
- XBRL for FY2016-FY2025 (filed values from later 20-Fs);
- FY2026 from the 20-F FY2026 income statement (₹926,240 million).

US dollars are the book's own conversion at the RBI financial-year average rate (`inr_usd_fy.csv`), not Wipro's convenience translation. For example, Wipro's FY2026 convenience figure is $9,871m, against $10,489m at the FY average rate.

**Wipro employees.** 'More than N' at 31 March, from the three-year sentence in each 20-F. The latest filing is preferred.

**Cognizant.**
- Revenue: XBRL (Revenues/SalesRevenueNet), 2007-2025.
- Employees: 10-K text. 2001-02 counts are 'technical professionals' only. 2011 is derived from the 2012 10-K ('an increase of approximately 19,000').
- India headcount: 2022-2025.

**TCS.** Headcount points only:
- FY2024-25: 607,979 (S0160, fact sheet).
- FY2025-26: 584,519, derived as 607,979 less the 23,460 net fall reported by *Business Standard* (S0139). A derived figure; replace it with TCS's own FY26 number when obtained.
- 30 September 2026: 598,056 (S0310).

## Discrepancies
1. **Infosys at 31 March 2004.** About 23,800 (20-F FY2004) vs about 25,700 (20-F FY2008's five-year comparison). The later figure probably includes subsidiaries such as Infosys BPO, or reflects restatement; not resolved. The CSV uses 23,800.
2. **Wipro at 31 March 2024.** 'More than 234,000' (20-F FY2024) vs 'more than 232,000' (20-F FY2025). The CSV uses 232,000.
3. **Accounting basis.** Infosys revenue is US GAAP to FY2008 and IFRS from FY2009, so small breaks are possible at the switch.

## Gaps
- **Infosys:** revenue FY2000, FY2002-03, FY2006-07, FY2011, FY2013-15; employees FY2002-03, FY2007, FY2011, FY2013-15. Fill from 20-F filings on EDGAR (FY2003, FY2007, FY2011, FY2015 cover these through their five-year comparisons).
- **Wipro:** revenue and employees before FY2016-19.
- **Cognizant:** employees 2003-06, 2008-10, 2013-19 (10-Ks on EDGAR).
- **TCS and HCLTech:** revenue and employee series. Their sites and annual-report PDFs are blocked; try BSE filings.

## Use in drafting
- Revenue per employee (mean headcount) for Infosys was about $44-57k in nominal terms in every year computed from FY2001 to FY2024 (FY2001 $54k; FY2010 $44k; FY2017-24 $52-57k), so it fell in real terms. It then rose to $60-62k in FY2025-26 as headcount stalled.
- Cognizant shows the same rise (about $55k in 2023 to $61k in 2025). Wipro's stays at about $45k.
- These are the companies' own figures, and the pattern is consistent with Chapter 19's 'non-linearity'. Give the method whenever the figure is quoted.
