# Phase 9 acquisition: gaps2

Access date for everything below: 2026-10-15. Downloads are in `/tmp/claude-0/-home-user-the-engineer-factory/77811d28-2ce1-5ce7-bf67-63b31b0b4c18/scratchpad/acq2_gaps2/dl/`.

**How the text was read.** Items marked **[D]** were downloaded with curl and the quotation was checked in the downloaded text (PDF or HTML converted to text). Items marked **[F]** were read with the WebFetch tool. That tool passes the page through an extraction model, so the wording is very probably the page's own, but it should be checked against the live page before it is printed. Search-engine summaries are never used as evidence here. Where one appears, it is labelled as a lead only.

---

## Q1. TCS attrition, FY2019-20 to FY2023-24 (ch18, para 41, n. 39) — status: found (press only; TCS's own documents blocked)

Ch18 now says the TCS rates 'appear in its quarterly fact sheets, which could not be obtained'. tcs.com returns 403 to curl and to WebFetch. BSE's announcement API returns 'Access Denied'. web.archive.org is blocked by the egress policy. TCS does not file with the SEC. Each year's figure below therefore comes from press reports that quote the results. TCS's own label for the measure, as relayed by the press, is LTM (last twelve months) attrition in IT services.

| At 31 March | TCS IT-services attrition | Source read | Exact wording |
|---|---|---|---|
| 2020 (FY2019-20) | 12.1% | HR Katha, 17 Apr 2020 [F]; *Communications Today*, 17 Apr 2020, credited to Business Standard [F] | HRK: "In FY20, the total employee strength at TCS was 4,48,464, and the attrition rate was 12.1 per cent." CT: "Attrition fell to 12.1 percent in Q4." |
| 2021 (FY2020-21) | 7.2% | HR Katha, 13 Apr 2021 [F] | "an all-time low attrition rate of 7.2 per cent for FY21"; headcount "about 488,649" |
| 2022 (FY2021-22) | 17.4% | *The News Minute*, 11 Apr 2022, TNM Staff with PTI inputs [F] | "The company's attrition rate rose further to 17.4% on a trailing 12-month basis as compared to 15.3% in the previous quarter." Headcount "592,195". |
| 2023 (FY2022-23) | 20.1% | HR Katha, 21 Apr 2023 [F] | "While TCS posted an attrition rate of 20.1 per cent (last-twelve-month or LTM basis)," |
| 2024 (FY2023-24) | 12.5% | HR Katha, 12 Apr 2024 [F] | "The attrition rate dipped to 12.5 per cent, a slight decline from 13.1 per cent in the previous quarter." |

- **Definition.** Two of the sources state the basis: 'trailing 12-month basis' (TNM 2022) and 'last-twelve-month or LTM basis' (HRK 2023). The FY2020 and FY2021 reports do not state it.
  - Lead only (search summaries, not read): the TCS press releases and fact sheets use the label 'LTM IT Services Attrition'.
  - Lead only: the Q4 FY24 call transcript reportedly says 'Our LTM attrition in IT services ... was at 12.5% at the end of Q4, down 80 bps sequentially and in our comfort range of 11% to 13%'. Verify it in the transcript at https://www.tcs.com/content/dam/tcs/investor-relations/financial-statements/2023-24/q4/Management%20Commentary/ (403 from here).
- **Comparison with Infosys.** TCS used one basis (LTM) throughout. That makes its series cleaner than Infosys's, whose basis changed in FY2022 (see ch18).
- **Second outlet.** Business Today's Q4 FY24 article (13 Apr 2024, 'TCS reports a decline in headcount for the first time in 19 years', reprinted by *Communications Today*) was read only in the CT reprint. That reprint mentions 'a decline in attrition' but gives no figure. Business Today, Business Standard and Deccan Herald all returned 403. The FY21, FY23 and FY24 figures therefore rest on HR Katha alone, and HR Katha is a trade site.
- **Recommendation.** If the author can open tcs.com from an ordinary browser, the fact sheet (path pattern in records.md) would be the primary source. If not, use the table above with the note 'as reported by'.

## Q2. Moneycontrol's 2022 fresher-pay study (S0331) — status: partly (original located, not readable)

- **The original was located.** *Analytics India Magazine* links to it: Lokesh Choudhary, 'Behind the Growing (and Huge) IT CEO-Fresher Pay Gap', 16 Aug 2022 [F].
  - The link is https://www.moneycontrol.com/news/business/it-ceo-pay-shot-up-835-in-a-decade-while-freshers-salary-grew-45-8602591.html.
  - The title is inferred from the URL slug: 'IT CEO pay shot up 835% in a decade while freshers' salary grew 45%'.
  - The article ID (8602591) fits late May 2022, just before HR Katha's report of 1 June 2022. The author and exact date are not confirmed.
- **Why it was not read.** Moneycontrol blocks this tool chain: the search tool reports that the domain is 'not accessible to our user agent', and WebFetch reports that it is 'unable to fetch'. The block was respected and not worked around.
- **Figures as relayed (no change from S0331).**
  - HR Katha [F]: "They were earning about Rs 2.45 lakh in 2012, and are now earning Rs 3.55 lakh in 2022." CEOs "used to earn a median annual remuneration of Rs 3.37 a decade ago" [sic, no unit] and "now earn Rs 31.5 crore in 2022!"; growth "835 per cent".
  - AIM [F], an independent relay: "While the median salary of freshers has increased to Rs 3.55 lakh from Rs 2.45 lakh over the last decade"; "the median salary of tech CEOs saw an 835% jump".
- **Methodology not known.** Which companies, and whether 'pay' means cost-to-company, are still unread.
- **A different study, not to be mixed with this one.** *Business Today*, 27 Dec 2022, ran its own analysis: CEO pay up about 1,500% and fresher pay about 50% (median CEO about 1,449%, median fresher about 40%). Only search summaries of it were seen.

## Q3. Zoho — status: partly

**Zoho's own 'About us' page** (https://www.zoho.com/aboutus.html) [D]. This is the company's self-description. The page is live and includes 2026 entries.
- 1996: "AdventNet Inc. is born in New Jersey, USA. It all begins with Network Management."
- 1998, 2000: moves to San Jose, then to Pleasanton, California.
- 2003: "We launch our sister brand: ManageEngine!"
- 2009: "AdventNet is renamed to Zoho Corporation Pvt Ltd."
- 2011: "We open an office in Tenkasi, India."
- 2013: "Zoho University starts in Tenkasi, India."
- Funding: "Since we have never taken money from investors, we have always been able to focus on what is best for the customer."
- The employee count in "more than [ ] employees" is filled in by script, so no number is in the static HTML.
- 2026 entry: "Sridhar Vembu transitions to Chief Scientist ... while Shailesh Kumar Davey takes over as CEO of Zoho Corp. Co-founder Tony Thomas now leads Zoho US". This is post-mid-2025 material, live-checked.
- **Conflict with the register.** Register S0175 says Tenkasi dates from 2019. Zoho's own timeline says 2011 (office) and 2013 (Zoho University). *The Week* (below) also says 2011. The 2019 date is probably Vembu's own move to the village. The register entry should be corrected.

**Founders.** Mixergy interview, Andrew Warner, 9 Mar 2010 (transcript) [F]:
- "We have never taken any outside money."
- "the three of us came together and that's how that happened"
- Vembu names Tony Thomas and his own brother as co-founders.
- The transcript gives the company's age inconsistently ('14 years old' and 'fifteen years ago').

**Employee counts (press).**
- Naandika Tripathi, 'Cover story: Sridhar Vembu's vision from the village', *Forbes India*, 3 Jun 2020 [F]. The magazine reports 9,300 employees worldwide, 8,800 of them in India, and 500 in its two rural offices (Tenkasi and Renigunta). The figures are Forbes India's own reporting.
- Lakshmi Subramanian, 'Sridhar Vembu's vision: How Zoho transformed Tenkasi into rural tech hub', *The Week*, 12 Oct 2025 (issue of 19 Oct 2025) [F; post-mid-2025, live-checked]. "Starting with a modest thatched-roof shed in Mathalamparai in 2011 with just six employees"; "Now employing 1,200 people"; rural offices "employing more than 3,000 people". The same article also says '15 such centres', which is inconsistent with the 'some 100' offices it mentions.
- No current company-wide headcount from a reliable source was found.

**Vembu quotes.** No published interview read here has him contrasting products with services in so many words. These come closest:
1. *Forbes India*, 3 Jun 2020 [F]: "... one thing that I noted was in India we have perfect talent but we produce almost zero software products." (WebFetch returned this part; a search snippet gives the opening as "When we decided to launch this company," which needs checking) Also: "I always felt that in order to advance economically, you needed to take up these complex tasks."
2. *Forbes India*, 3 Jun 2020 [F], on the move to villages: "I always thought that people migrating from villages to cities is not a good idea".
3. e27, 'If US doesn't want Indians it is okay: Zoho CEO Sridhar Vembu', c. Apr 2017 (no byline or date on the page) [F]: "Since Zoho is an Indian company, the visa changes are not going to impact us." and "So I think India should be happy to keep the talent here."
4. *The Week*, 2025 [F]: "You need not necessarily be in a metro to run or work for a software company,"

- Vembu's April 2025 criticism of Indian IT ('input-based billing'; 'The IT industry sucked in talent that may have gone into manufacturing or infrastructure') was made in posts on X, as reported by *Business Today*, 18 Apr 2025. It is not an interview and was not read here.
- The Kiruba Shankar podcast on 'services vs products companies in India', listed on Zoho's blog, was not found.

## Q4. Aadhaar's builders — status: partly (good on team and architecture; book excerpt not found)

**A. UIDAI, *Aadhaar Technology & Architecture: Principles, Design, Best Practices, & Key Lessons*, March 2014, 170 pp.** [D; primary, official]. UIDAI's own document, via an archive.org mirror: https://ia800108.us.archive.org/17/items/Aadhaar-Technology-Architecture/AadhaarTechnologyArchitecture_March2014.pdf
- Chairman's message (printed p. 5), signed Nandan Nilekani: "Aadhaar technology system was able to succeed due to its core principles – openness, vendor-neutrality, security, and data analytics."
- Director General's message, Vijay Madan (printed p. 6/7, PDF p. 7): "Appropriately, the Technology Centre was the first unit of UIDAI to start functioning in 2009 in Bangalore. UIDAI technology team was able to develop the required applications and successfully generate the first Aadhaar number within a year of its formation."
  - Same page: "Aadhaar generation was commenced in August 2010 and the first Aadhaar letter was formally handed over to a resident at Nandurbar in Maharashtra on 29 September 2010."
- Editor's desk, Ashok Dalwai, DDG, Technology Centre, Bengaluru (PDF p. 10). It credits "a band of dedicated domain experts who worked with the UIDAI's Tech Centre" and names "Srikanth Nadhamuni, Raj Mashruwala, Pramod Varma, Sanjay Jain, Vivek Raghavan, and Jagdish Babu".
- Executive summary (PDF p. 19): "Entire technology architecture behind Aadhaar is based on principles of openness, linear scalability, strong security, and most importantly vendor neutrality."
  - A later section says: "Aadhaar system is entirely built using open source components".

**B. Mitu Jayashankar and N.S. Ramnath, 'UIDAI: Inside the World's Largest Data Management Project', *Forbes India*, 29 Nov 2010** (https://www.forbesindia.com/article/big-bet/uidai-inside-the-worlds-largest-data-management-project/19632/1) [F]. This is the best contemporary account of the people.
- Of the private-sector recruits: "23 took massive pay cuts to join the Project Management Unit (PMU) for the UIDAI"; "Another 140 have been drawn from the government."
- Pramod Varma: "an old Infosys hand who was on the project as its chief software architect". He "would tap his friends at various companies to lend him a conference room".
- Nadhamuni: "When Nilekani left Infosys to head the UID project, he invited Nadhamuni to head the technology centre."
- On Nilekani as manager: "He put down a simple guideline: No silos."
- Two officials quoted by name: K. Ganga, "We only talk through files and files don't have names and faces.", and Ashok Pal Singh, "And yet everyone is here because they want to be."

**C. Regunath Balasubramanian, principal architect,** in Vandana Sharma, 'Aadhaar: A Testimony to Success of FOSS in India!', *Open Source For You*, 4 Dec 2011 [F]: "The primary technical requirements of the project were of scale and vendor neutrality at all levels." and "FOSS helped us achieve vendor-neutrality in many of our application components".

**D. Srikanth Nadhamuni,** in Akhila Ranganna, 'Tech Guru, Srikanth Nadhamuni on his Constant Search For the Next Big Idea', *Man's World India*, 25 Jan 2016 [F]: "the garage startup atmosphere of a few sharp guys working closely is exactly what was needed" and "it was a massive technology challenge, doing a 1000 trillion biometric matches per day". The 'rented apartment with two tables and two whiteboards' detail is the writer's narration, not Nadhamuni's words.

**E. Ram Sewak Sharma, *The Making of Aadhaar: World's Largest Identity Platform* (Rupa, 2020).** No publisher or magazine excerpt was found. Two reviews were read; they can be used only as 'the reviewer says':
- Soni Mishra, 'Selling the dream', *The Week*, 7 Nov 2020 (issue of 15 Nov) [F]. It quotes the book on friction between private-sector staff and officers: "These fissures disturbed me. Nandan had also expressed his disappointment.... [The] good thing was, we never took sides," Sharma writes. The 'salespersons' line is also the book's, as quoted by the reviewer.
- Sandeep Sinha, review in *The Tribune*, 11 Oct 2020 [F]. Reviewer's words: "Nandan Nilekani, who headed the UIDAI project, thought that if someone was suitable for the job, it was enough." and "Those drawn from the private sector did their work primarily on the basis of emails,"
- The Week gives 199 pp.; a retailer listing gives 244 pp. (ISBN 9789390356126). Rupa's page has a 2025 date. The edition is unresolved.

**F. Not read.**
- YourStory's excerpt of Shankkar Aiyar, *Aadhaar: A Biometric History* (Penguin, 2017), 'History of Aadhaar: How Nandan's core team came together' (https://yourstory.com/2017/07/history-of-aadhaar/): 403.
- YourStory's 'Techie Tuesdays' profile of Pramod Varma (Jan 2017): 403. Lead only: it says he joined as a full-time volunteer in July 2009.
- Already registered: the Nilekani CHM oral history S0360, p. 14.

## Q5. First-person account by an engineer at a multinational captive centre — status: not found

- **No first-person account in a reputable outlet was found.** Searches covered TI Bangalore, Microsoft IDC, the GE centre, Intel, SAP Labs and Google. What turned up was executive statements and company releases.
- **Usable by-product: TI's own claim on the satellite link** (bears on the ch08/ch15 dates). 'TI Celebrates 20 Years as a Technology Innovator in India', TI press release, Bangalore, 8 Aug 2005 (https://ti.com/ww/in/news_detail/2008_2005/news_detail_sc05161.html) [F]. It says TI began operations in India in 1985 and that "In 1985, TI India was the first to install and use a satellite dish for exporting software" (wording as extracted; recheck). This is a company claim and conflicts with 1986 dates for when the link began operating.
- **Lead: Quartz,** 'How a US chipmaker unwittingly became an incubator for Indian entrepreneurs' (qz.com/india/437318). It returned 403. Per search summary only, it says TI's 'salaries typically bested other options'.
- **Lead: Ittiam.** Srini Rajam and seven other TI India executives left TI India in 2001 to found Ittiam. Interviews from 2001 (*Financial Times*, *Hindu BusinessLine*, BBC) are listed on ittiam.com but were not read.
- **Lead: a book.** Chitra Narayanan, *The Sona Story* (on C. Valliappa, whose Sona Towers housed TI). It is a business biography, not an engineer's account.

## Q6. Lok Sabha, 24 November 1966 (ch03, para 63, n. 67; S0227) — status: found (printed record read)

- **The record.** The Parliament Digital Library item is mirrored on archive.org (Public.Resource.Org collection 'legislaturesofindia'): *Lok Sabha Debates (24-Nov-1966)*, Third Series, Session XVI, identifier `eparlib.nic.in.54794`, source given as https://eparlib.sansad.in/handle/123456789/54794. https://archive.org/details/eparlib.nic.in.54794 [D: OCR text `lsd_03_16_24-11-1966_djvu.txt`].
- **The item.** 'Calling attention to matter of urgent public importance: Proposed strike by LIC employees on 25th November, 1966', cols. 5284-5308 (Agrahayana 3, 1888 Saka). It was raised by Indrajit Gupta. The Finance Minister, Sachindra Chaudhuri, made the statement.
- **The figures are confirmed** in the Minister's statement, cols. 5287-88: "The process of switching over to computers is expected to take some three years. During this period, as a result of this switch-over, 383 jobs would disappear but the very process of computerisation would create 225 new jobs. The net reduction in the number of jobs is therefore only 158, i.e, about 50 per year."
  - S.M. Banerjee read the same passage into the record at col. 5285, raising it as a point of order.
- **Other facts in the statement.**
  - The strike: the All-India Insurance Employees' Association called "a day's token strike on Friday, November 25, 1966, as a protest against the introduction of Automation through installation and commissioning of Electronic Computers by the L.I.C." (col. 5286, OCR-corrected).
  - The machines: "A Computer at Bombay was installed in November, 1965 and the other at Calcutta ... is expected to be installed some time next year. The decision to instal the Computers was taken as early as 1964." (col. 5287)
  - Scale: the 158 is "insignificant as compared to the 1500 or so new jobs created in the L.I.C. every year" (col. 5288).
  - The unions' claim, as reported by Vasudevan Nair, col. 5297: "computerisation will make 30,000 out of 40,000 employees redundant".
- **IBM** is not named on this day.
- **Bonus: 23 March 1967 (S0019),** archive.org `eparlib.nic.in.1233` [D], cols. 675-80, oral question *40 from George Fernandes.
  - K.C. Pant: the Bombay system "was about Rs 42 lakhs (excluding importation charges and sales tax)". Its manufacturer was "M/s International Business Machines Corporation of USA". The Calcutta machine was from "International Computers and Tabulators Ltd of UK". Payment was made "under a 'blocked rupee' arrangement".
  - S.M. Banerjee: "growing discontent among 40,000 life insurance employees".
  - Morarji Desai: "There is going to be no retrenchment on this account." The OCR reads '70 retrenchment ० this account'; check the page image. Desai also said: "It will be an unwise policy if we do not do this."
- **The ch03 sentence can drop 'not yet checked'.** The dispute over the earlier 'pp. 69-81' citation is resolved: those were page numbers in a partial PDF, and the printed record uses columns.

## Q7. Aspray's figure for software exports around 1980 (ch04, para 75, n. 72; S0230) — status: found (figure confirmed; no page numbers exist)

- **The source.** William Aspray, 'The Role of Policy in the Rise of the Indian Software and IT-Enabled Services Industry', *The Rutherford Journal* 3 (2010), 'A Special Issue on the History of Computing' [D: article and volume index].
  - The article is at https://rutherfordjournal.org/article030101.html. The volume index (https://rutherfordjournal.org/current2.html) confirms 'Volume 3, 2010'. The '[inferred; to confirm]' note in S0230 can be removed.
- **The passage.** It is in the section 'Trade, industrial regulation, and foreign investment policy', in the paragraph after the Burroughs/body-shopping paragraph: "As of 1980, the Indian software industry was predominantly a body-shopping industry. ... At this time, there were 21 Indian firms providing this business, doing a total of only $4 million of export business annually. TCS and Tata Infotech, another member of the Tata conglomerate, held 63% of the market."
- **Pages.** The journal is online and has no page numbers. Cite it by section and paragraph.
- **What lies behind the figure.** The sentence has no note of its own. The section's note 2 says the policy "is described in considerably more detail, for the period up until 1996, in Heeks 1996" (Richard Heeks, *India's Software Industry*, Sage, 1996). Note 1 says the paper "draws heavily on the ACM report by Aspray, Mayadas, and Vardi (2006)". Heeks is the likely source of the figure, but this was not verified.
- **The ACM report could not be fetched.** acm.org returns 403 and web.archive.org is blocked.
- **Ch04 is accurate as drafted:** 'twenty-one firms exporting about $4 million a year, mostly by sending people to client sites'. Optionally add TCS and Tata Infotech's 63% share.

## Q8. First computerised railway reservation at New Delhi (ch08, para 55, n. 54) — status: found (official audit record)

- **The audit report.** Comptroller and Auditor General of India, *Report No. 11 of 2007 (Railways): Performance Audit (IT Audit)*, period ended March 2006, laid 14 May 2007, ch. 1 'Computerised Passenger Reservation System of the Indian Railways', para 1.3, printed p. 4 [D].
  - The old cag.gov.in URL now returns 404. The report index page (https://cag.gov.in/en/old-audit-reports/view/13664) links to the current copy: https://d7i5wg8xwe4hf.cloudfront.net/uploads/old_reports/union/union_performance/2006_2007/Railways/Report_no_11/chap_1.pdf
  - Para 1.3: "The pilot project of PRS was launched on 15 November 1985, over Northern Railway with the installation of the Integrated Multiple Train Passenger Reservation System (IMPRESS), an online transaction processing system developed by the Indian Railways in association with Computer Maintenance Corporation (CMC) Ltd., at New Delhi."
  - Same para: "This application was subsequently implemented in 1987, at Mumbai, Chennai, Kolkata and Secunderabad." CONCERT, developed by CRIS, was "first implemented at the Secunderabad PRS site in September 1994".
  - Overview (same report, overview.pdf, p. 1): "The Computerised Passenger Reservation System, launched in November 1985 as a pilot project on Northern Railway, ..."
- **Trade press.** DQI Bureau, 'Happy Journey!', *Dataquest*, 6 Nov 2009 [F]: "A pilot project consisting of a few popular trains was first implemented at New Delhi in November 1985." and "Upon its success, the entire New Delhi reservation system was computerized in May 1987."
- **Government press.** PIB backgrounder, 'From Queues to Clicks: Four Decades of Passenger Reservation in Indian Railways', 6 Aug 2026 [D; post-mid-2025, live-checked] (https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/aug/doc202686945401.pdf). It gives 1986 for "PRS introduced, marking the beginning of computerised railway reservations in India" and says "Introduced in 1986, PRS has evolved ...". It gives no day or month.
- **How the dates fit together.** The pilot (IMPRESS, a few trains) ran at New Delhi from 15 Nov 1985 (CAG). The government's own count, and Rajaraman's 'by 1986', date the start of the system proper to 1986. New Delhi was fully computerised in May 1987 (Dataquest). No CRIS primary page giving 15 Nov 1986 was found; CRIS's site returned 404.
- **Suggested wording.** "A pilot covering a few trains began at New Delhi on 15 November 1985, according to the Comptroller and Auditor General."

## Q9. iSPIRT after 2013 (ch17, paras 55-63) — status: partly

- **India Stack** (https://indiastack.org/, maintained by iSPIRT) [D]. This is iSPIRT's self-description.
  - FAQ: "Individuals interested in contributing to or working on India Stack may volunteer with iSPIRT, a non-profit think tank which champions digital public goods and maintains this website."
  - Timeline on the home page: "2012 UIDAI launches eKYC ..."; "2015 CCA launches eSign as an open API"; "2016 NPCI launches Unified Payments Interface"; "2021 The Account Aggregator framework goes live with 8 banks".
  - India Stack credits these launches to government bodies (UIDAI, NPCI, CCA, MeitY), not to iSPIRT.
- **Press account of the decade.** Suprita Anupam, '10 Years Of iSPIRT: Inside The Making Of A Product Nation', *Inc42*, 27 Feb 2023 (S0189, now read) [F].
  - It describes iSPIRT as "building the India Stack since 2013". Its list of iSPIRT projects includes OCEN, Account Aggregator (AA) support with Sahamati, health-stack work and drone rules.
  - Its criticism: AA and OCEN "have struggled to emote the kind of response UPI did"; volunteer retention; allegations of conflicts of interest.
  - It gives no direct quote from Sharad Sharma.
- **Controversy.** Rohan Venkataramakrishnan, 'Co-founder of UIDAI-associated outfit admits to anonymously trolling Aadhaar critics on Twitter', *Scroll.in*, 23 May 2017 [F].
  - It says iSPIRT was "constituted in 2013 as an offshoot of industry body NASSCOM's annual product conclave". This conflicts with ch17's framing, where iSPIRT is a break from Nasscom; reconcile.
  - Sharad Sharma, governing-council member, "anonymity seemed easier than propriety"; "I condoned tweets with uncivil comments."
- **Policy advocacy (angel tax).** Shilpa S Ranipeta, 'Startups write to PM Modi seeking immediate action on angel tax issue', *The News Minute*, 16 Jan 2019 [F]. iSPIRT's letter asked that "Investments received by a startup, as recognized by DIPP from resident investors up to Rs 10 crore per year" be exempt. It cited a 48% fall in angel investors since 2015. The letter was signed by nearly 70 entrepreneurs.
- **Product-nation policy.** Aditi Agrawal, 'Summary: National Policy on Software Products (NPSP)', *MediaNama*, 3 Jun 2019 [F]: "On 28 February 2019, the cabinet approved the National Policy on Software Products". Its target is a "10x increase in global software product market share by 2025", with a Software Product Development Fund of "a corpus of ₹1,000 crore".
  - The PIB release (pib.gov.in) returned 403.
  - No source read credits iSPIRT with drafting the NPSP, so do not assert it.
- **Not read (leads).**
  - The Ken, 'How did a private organisation like iSpirt end up with the master key to Aadhaar?' (paywall).
  - Quartz, 'Nilekani's iSPIRT shadow on India's RBI digital payments panel' (Jan 2019; 403).
  - ispirt.in and pn.ispirt.in (Cloudflare block).

---

## Proposed register entries

| ID | Citation | URL | Type | Notes | Status | Chapters |
|---|---|---|---|---|---|---|
| SNEW1 | HRK News Bureau. 'TCS defers increments, will not reduce jobs.' *HR Katha*, 17 Apr 2020; 'TCS hired 40,185 in FY21, outlook seems bright', 13 Apr 2021; 'TCS, Infosys, HCL have hired less in Q4 than last year', 21 Apr 2023; 'TCS attrition cools as top performers rewarded', 12 Apr 2024. | https://www.hrkatha.com/?p=20909 ; https://www.hrkatha.com/news/tcs-hired-40185-in-fy21-outlook-seems-bright/ ; https://www.hrkatha.com/?p=38142 ; https://www.hrkatha.com/news/tcs-attrition-cools-as-top-performers-rewarded/ | S (trade press relaying company results) | TCS attrition: 12.1% (FY20), 7.2% (FY21), 20.1% LTM (FY23), 12.5% (FY24). Fact sheets (S0160) not reachable. | seen 2026-10-15 | 18, data |
| SNEW2 | TNM Staff with PTI. 'TCS net profit jumps 7.4% to Rs 9926 crore in Q4, attrition rises to 17.4%.' *The News Minute*, 11 Apr 2022; and *Communications Today*, 'TCS net profit flat at Rs 8049 crore in Q4; freezes salary hike', 17 Apr 2020 (credited to Business Standard). | https://www.thenewsminute.com/atom/tcs-net-profit-jumps-74-rs-9926-crore-q4-attrition-rises-174-162817 ; https://www.communicationstoday.co.in/?p=51269 | S (press) | 17.4% 'on a trailing 12-month basis' (Q4 FY22); 12.1% (Q4 FY20), second outlet. | seen 2026-10-15 | 18 |
| SNEW3 | Choudhary, Lokesh. 'Behind the Growing (and Huge) IT CEO-Fresher Pay Gap.' *Analytics India Magazine*, 16 Aug 2022; links the Moneycontrol original, 'IT CEO pay shot up 835% in a decade while freshers' salary grew 45%' (moneycontrol.com, c. late May 2022, art. 8602591; not readable by this tool chain). | https://analyticsindiamag.com/behind-the-growing-and-huge-it-ceo-fresher-pay-gap/ ; https://www.moneycontrol.com/news/business/it-ceo-pay-shot-up-835-in-a-decade-while-freshers-salary-grew-45-8602591.html | S (press relaying press) | Second relay of the S0331 figures (Rs 2.45 lakh to 3.55 lakh; CEO median +835%). Original located, not read. | seen 2026-10-15 (AIM); located (Moneycontrol) | 18 |
| SNEW4 | Zoho Corporation. 'About us' (timeline). | https://www.zoho.com/aboutus.html | P (company self-description) | AdventNet born New Jersey 1996; renamed Zoho Corporation Pvt Ltd 2009; Tenkasi office 2011; Zoho University in Tenkasi 2013; 'never taken money from investors'; 2026 entry on Vembu becoming Chief Scientist and Davey CEO (live-checked). Corrects S0175's Tenkasi 2019. | seen 2026-10-15 | 17 |
| SNEW5 | Tripathi, Naandika. 'Cover story: Sridhar Vembu's vision from the village.' *Forbes India*, 3 Jun 2020. | https://www.forbesindia.com/article/big-bet/cover-story-sridhar-vembus-vision-from-the-village/59833/1 | S (press, with founder quotes) | 9,300 employees (8,800 India); 500 in Tenkasi and Renigunta; Vembu: 'in India we have perfect talent but we produce almost zero software products.' | seen 2026-10-15 | 17 |
| SNEW6 | Subramanian, Lakshmi. 'Sridhar Vembu's vision: How Zoho transformed Tenkasi into rural tech hub.' *The Week*, 12 Oct 2025. | https://www.theweek.in/magazine/theweek/business/2025/10/11/sridhar-vembus-vision-how-zoho-transformed-tenkasi-into-rural-tech-hub.html | S (press) | Mathalamparai shed 2011, six staff; now 1,200; more than 3,000 in rural offices. Post-mid-2025, live-checked. | seen 2026-10-15 | 17 |
| SNEW7 | Warner, Andrew. Interview with Sridhar Vembu. *Mixergy*, 9 Mar 2010 (transcript). | https://mixergy.com/interviews/sridhar-vembu/ | P (founder interview) | 'We have never taken any outside money'; three co-founders (Vembu, his brother, Tony Thomas). Transcript is rough. | seen 2026-10-15 | 17 |
| SNEW8 | Unique Identification Authority of India. *Aadhaar Technology & Architecture: Principles, Design, Best Practices, & Key Lessons*. New Delhi: UIDAI, March 2014. 170 pp. | https://ia800108.us.archive.org/17/items/Aadhaar-Technology-Architecture/AadhaarTechnologyArchitecture_March2014.pdf | P (official) | Tech Centre 'first unit of UIDAI', Bangalore 2009; first Aadhaar 'within a year'; generation from Aug 2010; Nandurbar, 29 Sep 2010; names Nadhamuni, Mashruwala, Varma, Jain, Raghavan, Babu; openness, vendor neutrality, open source. | seen 2026-10-15 (pp. 5-19) | 16 |
| SNEW9 | Jayashankar, Mitu and N.S. Ramnath. 'UIDAI: Inside the World's Largest Data Management Project.' *Forbes India*, 29 Nov 2010. | https://www.forbesindia.com/article/big-bet/uidai-inside-the-worlds-largest-data-management-project/19632/1 | S (press, contemporary) | 23 private-sector recruits took 'massive pay cuts'; 140 from government; Varma 'chief software architect'; Nadhamuni heads tech centre; MindTree built the enrolment client. | seen 2026-10-15 | 16 |
| SNEW10 | Sharma, Vandana. 'Aadhaar: A Testimony to Success of FOSS in India!' *Open Source For You*, 4 Dec 2011. | https://www.opensourceforu.com/2011/12/aadhaar-testimony-to-foss-success-in-india/ | S (trade press, architect interview) | Regunath Balasubramanian: 'scale and vendor neutrality at all levels'. | seen 2026-10-15 | 16 |
| SNEW11 | Ranganna, Akhila. 'Tech Guru, Srikanth Nadhamuni on his Constant Search For the Next Big Idea.' *Man's World India*, 25 Jan 2016. | https://www.mansworldindia.com/tech/tech-guru-srikanth-nadhamuni-constant-search-next-big-idea/ | S (profile with quotes) | 'garage startup atmosphere'; '1000 trillion biometric matches per day'. | seen 2026-10-15 | 16 |
| SNEW12 | Mishra, Soni. 'Selling the dream' (review of R.S. Sharma, *The Making of Aadhaar*, Rupa 2020). *The Week*, 7 Nov 2020; and Sinha, Sandeep, review, *The Tribune*, 11 Oct 2020. | https://www.theweek.in/theweek/leisure/2020/11/06/selling-the-dream.html ; https://www.tribuneindia.com/news/book-reviews/how-an-identity-platform-became-a-tool-of-governance-154084 | R (reviews) | Book quoted by The Week on private-sector/IAS 'fissures'; Tribune reviewer on hiring and email culture. Reviewers' words only. | seen 2026-10-15 | 16 |
| SNEW13 | Lok Sabha Debates, Third Series, Session XVI, 24 November 1966, cols. 5284-5308: calling attention, proposed strike by LIC employees (Finance Minister Sachindra Chaudhuri). Parliament Digital Library, mirrored on archive.org (eparlib.nic.in.54794). | https://archive.org/details/eparlib.nic.in.54794 | P (official record) | Supersedes S0227's eparlib URL and page range. 383 jobs lost, 225 created, net 158 over three years; Bombay computer installed Nov 1965; decision 1964; strike 25 Nov 1966. | seen 2026-10-15 (OCR text) | 3 |
| SNEW14 | Lok Sabha Debates, Fourth Series, Session I, 23 March 1967, cols. 675-80: oral question *40 (George Fernandes), 'Computers in LIC'. archive.org mirror (eparlib.nic.in.1233). | https://archive.org/details/eparlib.nic.in.1233 | P (official record) | Supplements S0019 (now readable). IBM system at Bombay about Rs 42 lakh; ICT for Calcutta; blocked-rupee payment; Desai: no retrenchment. | seen 2026-10-15 (OCR text) | 3 |
| SNEW15 | Comptroller and Auditor General of India. *Report No. 11 of 2007 (Railways): Performance Audit (IT Audit)*, ch. 1 'Computerised Passenger Reservation System of the Indian Railways', para 1.3, p. 4; and overview. Laid 14 May 2007. | https://d7i5wg8xwe4hf.cloudfront.net/uploads/old_reports/union/union_performance/2006_2007/Railways/Report_no_11/chap_1.pdf | P (audit report) | PRS pilot 'launched on 15 November 1985' (IMPRESS, Northern Railway, with CMC, New Delhi); 1987 at Mumbai, Chennai, Kolkata, Secunderabad; CONCERT Sept 1994. | seen 2026-10-15 | 8 |
| SNEW16 | DQI Bureau. 'Happy Journey!' *Dataquest*, 6 Nov 2009; and PIB backgrounder 'From Queues to Clicks: Four Decades of Passenger Reservation in Indian Railways', 6 Aug 2026. | https://www.dqindia.com/happy-journey/ ; https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/aug/doc202686945401.pdf | S (trade press); P (government release) | Pilot at New Delhi Nov 1985, full New Delhi May 1987 (DQ); PRS 'Introduced in 1986' (PIB, live-checked, post-mid-2025). | seen 2026-10-15 | 8 |
| SNEW17 | Texas Instruments. 'TI Celebrates 20 Years as a Technology Innovator in India.' Press release, Bangalore, 8 Aug 2005. | https://ti.com/ww/in/news_detail/2008_2005/news_detail_sc05161.html | P (company claim) | Operations from 1985; 'first to install and use a satellite dish for exporting software' in 1985 (company claim; recheck wording). | seen 2026-10-15 | 8, 15 |
| SNEW18 | India Stack (website maintained by iSPIRT), home page and FAQ. | https://indiastack.org/ | P (self-description) | iSPIRT 'a non-profit think tank which champions digital public goods and maintains this website'; timeline 2009-2021 credits UIDAI, NPCI, CCA, MeitY. | seen 2026-10-15 | 17 |
| SNEW19 | Venkataramakrishnan, Rohan. 'Co-founder of UIDAI-associated outfit admits to anonymously trolling Aadhaar critics on Twitter.' *Scroll.in*, 23 May 2017. | https://scroll.in/article/838468/co-founder-of-uidai-associated-outfit-admits-to-anonymously-trolling-aadhaar-critics-on-twitter | S (press) | iSPIRT 'constituted in 2013 as an offshoot of ... NASSCOM's annual product conclave'; Sharad Sharma's admission. | seen 2026-10-15 | 17 |
| SNEW20 | Ranipeta, Shilpa S. 'Startups write to PM Modi seeking immediate action on angel tax issue.' *The News Minute*, 16 Jan 2019; and Agrawal, Aditi, 'Summary: National Policy on Software Products (NPSP)', *MediaNama*, 3 Jun 2019. | https://www.thenewsminute.com/atom/startups-write-pm-modi-seeking-immediate-action-angel-tax-issue-95134 ; https://www.medianama.com/2019/06/223-summary-national-policy-on-software-products-npsp/ | S (press) | iSPIRT angel-tax letter (Rs 10 crore exemption; angels down 48% since 2015); NPSP approved 28 Feb 2019, '10x' target, Rs 1,000 crore fund. NPSP not linked to iSPIRT in any source read. | seen 2026-10-15 | 17 |

Register amendments suggested (not made):
- **S0230.** Volume and year are confirmed: *Rutherford Journal* 3, 2010. Cite by section, since the journal has no pages.
- **S0227.** Replace with SNEW13, or update its URL and columns. Drop 'per search summary'.
- **S0019.** Now readable via SNEW14.
- **S0175.** The Tenkasi date of 2019 is contradicted by Zoho (2011).
- **S0189.** Now seen.

## Searched, not found

- **TCS primary documents.**
  - tcs.com fact sheets, press releases and call transcripts: 403 to curl (browser user agent) and to WebFetch.
  - BSE announcements API: Akamai 'Access Denied'.
  - nsearchives: 404.
  - web.archive.org: blocked by egress.
  - Press that returned 403: Business Today, Business Standard, Deccan Herald. Second outlets for FY21, FY23 and FY24 were therefore not read.
- **Moneycontrol original:** blocked to this tool chain at the user-agent level; not worked around. Author, date and method unknown.
- **Zoho.**
  - No current company-wide headcount; the figure on zoho.com is rendered by script.
  - YourStory's 25-years piece (S0175): 403.
  - No published interview with an explicit Vembu products-versus-services quote. The Zoho blog's 'Sridhar gets interviewed by The Hindu' (2007) links nowhere. The Kiruba Shankar podcast was not found.
- **Aadhaar.**
  - No excerpt of R.S. Sharma's book from the publisher or a magazine.
  - YourStory's Aiyar excerpt and its Pramod Varma profile: 403.
  - New India Abroad's report of the 30 May 2024 Nilekani/Varma CHM event has no quotes.
  - UIDAI's 'Work with UIDAI' page: 404. The 2011 volunteer and sabbatical guidelines were not found.
- **Captive-centre engineer, first person:** nothing in a reputable outlet. Searched TI Bangalore, Microsoft IDC, Intel, SAP Labs, the GE centre, Google and Srini Rajam/Ittiam. Quartz on TI: 403.
- **Lok Sabha:**
  - eparlib.sansad.in still resets the connection and returns 503. The archive.org mirror worked.
  - No scholarly source quoting the 24 Nov 1966 debate was sought further, since the record itself was read.
- **Aspray's underlying source:** the ACM 2006 report (acm.org 403; Wayback blocked) and Heeks 1996 (not online) were not checked.
- **Railways:** no CRIS primary page found (cris.org.in/crisweb 404). The 'PRS at New Delhi on 15 Nov 1986' date was not found in any source read. The Business Standard 'story behind PNR' (2017) was not read.
- **iSPIRT:**
  - ispirt.in and pn.ispirt.in: Cloudflare block.
  - The Ken: paywall.
  - Quartz (RBI panel): 403.
  - PIB release on the NPSP: 403.
  - YourStory 'iSPIRT releases blue papers' (Mar 2013): not read.
