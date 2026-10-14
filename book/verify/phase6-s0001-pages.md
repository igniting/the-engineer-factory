# S0001 (Rajaraman, History of Computing in India 1955-2010) page audit

Mapping rule: printed page = form-feed chunk index (0-based) - 5 = PDF page (1-based) - 6. Verified on every chunk with a footer (printed pp. 1-88; chunks 6-93), and against `pdftotext -layout` for PDF pp. 13, 27, 50, 81 (footers 7, 21, 44, 75). Blank/unnumbered: chunks 0-5 (front matter), 11 (p. 6), 15 (p. 10), 25 (p. 20), 63 (p. 58), 94-96.

| file | note number | cited page(s) | correct printed page(s) | status | evidence phrase |
|---|---|---|---|---|---|
| prologue.md | 62 | p. 7 | 7 | ok | 'In 1955 only a few dozen scientists and engineers in India knew about computers.' |
| prologue.md | 63 | p. 15 | 15 | ok | 'Mahalanobis founded the Indian Statistical Institute (ISI) in Kolkata in 1931 and Bhabha the Tata Institute...' |
| prologue.md | 64 | pp. 15-16 | 15-16 | ok | p15: 'The computer was ready in June 1955 and arrived in Kolkata in July 1955 without'; p16: 'Mukherjee and Roy installed and tested the machine at the ISI using their notes and it started working in A...' |
| prologue.md | 65 | p. 16 | 16 | ok | 'Around a dozen people learnt to program the computer which was used for some statistical calculations.' |
| ch01.md | 6 | p. 15 | 15 | ok | 'Mahalanobis founded the Indian Statistical Institute (ISI) in Kolkata in 1931 and Bhabha the Tata Institute...' |
| ch01.md | 12 | p. 15 | 15 | ok | '3.1 EARLY COMPUTER INSTALLATIONS Nehru's confidants, P.C.Mahalanobis and Homi J.Bhabha, influenced policy m...' |
| ch01.md | 13 | p. 13 | 13 | ok | 'The second five year plan (1956-61) was drafted by Mahalanobis, a well known statistician.' |
| ch01.md | 27 | p. 15 | 15 | ok | 'Mahalanobis formed a small computer group at the ISI and ordered a computer from the British Tabulating Mac...' |
| ch01.md | 28 | p. 15, citing Mukherjee's memoir (S0015, not seen) | 15 | ok | p15: 'sent Mohi Mukherjee and Amresh Roy to England in December 1954 [1]' (ref [1] = Mukherjee, 'The first Computer in India') |
| ch01.md | 30 | p. 15 | 15 | ok | 'A computer HEC-2M (Hollerith Electronic Computer Model 2M) was being designed by A.D.Booth at Birbek Colleg...' |
| ch01.md | 32 | pp. 15-16 | 15-16 | ok | p15: 'The computer was ready in June 1955 and arrived in Kolkata in July 1955 without'; p16: 'Mukherjee and Roy installed and tested the machine at the ISI using their notes and it started working in A...' |
| ch01.md | 34 | p. 16 | 16 | ok | 'HEC-2M had a drum memory with 1024, 24 bit words and had to be programmed in machine language.' |
| ch01.md | 35 | p. 16 | 16 | ok | 'Around a dozen people learnt to program the computer which was used for some statistical calculations.' |
| ch01.md | 37 | p. 16 | 16 | ok | 'In the meanwhile at the ISI, Kolkata, HEC-2M was found to be a very difficult machine to use.' |
| ch01.md | 38 | p. 7 | 7 | ok | 'In 1955 only a few dozen scientists and engineers in India knew about computers.' |
| ch01.md | 39 | p. 16 | 16 | ok | 'It was difficult to get funds, particularly foreign exchange funds.' |
| ch01.md | 40 | p. 16 | 16 | ok | 'He negotiated with the USSR and a URAL-1 computer was ordered in 1958 with assistance from the United Natio...' |
| ch01.md | 41 | p. 16 | 16 | ok | 'URAL-1 was also a first generation machine using vacuum tubes and had a drum memory, punched tape I/O and a...' |
| ch01.md | 42 | p. 16 (Russian engineers) | 16 | ok | 'It was installed by the Russian engineers.' |
| ch01.md | 43 | p. 16 | 16 | ok | 'All the manuals were in Russian and the ISI engineers learnt Russian to enable them to maintain the machine.' |
| ch01.md | 46 | p. 16 | 16 | ok | 'ISI was the de-facto National Computer Centre used by other universities...' |
| ch01.md | 47 | p. 16 | 16 | ok | 'ISI was the de-facto National Computer Centre used by other universities, atomic energy establishment and d...' |
| ch01.md | 53 | p. 15 | 15 | ok | 'Mahalanobis founded the Indian Statistical Institute (ISI) in Kolkata in 1931 and Bhabha the Tata Institute...' |
| ch01.md | 65 | p. 16 | 16 | ok | 'could perform 12000 operations per second' |
| ch01.md | 67 | p. 17 and ref. 25 | 17 (ref. 25 listed on p. 64) | ok | p17: 'a bold decision ... in 1963 [25]'; ref [25] P.V.S.Rao, 'member of the committee which evaluated CDC3600-160A' (ref list p64) |
| ch01.md | 69 | p. 16 | 16 | ok | 'It was installed at the new building of TIFR in 1962 and named TIFRAC (TIFR Automatic Calculator) by Jawaha...' |
| ch01.md | 70 | p. 16 | 16 | ok | 'It was installed at the new building of TIFR in 1962 and named TIFRAC (TIFR Automatic Calculator) by Jawaha...' |
| ch01.md | 79 | p. 17 gives 1961 to 1963 | 17 | ok | 'After the completion of the TIFRAC project R.Narasimhan went to the University of Illinois during 1961 to 1...' |
| ch01.md | 81 | p. 17 | 17 | ok | 'It was a bold decision as CDC 3600 was not yet a commonly used computer in 1963 [25].' |
| ch01.md | 82 | p. 17 | 17 | ok | 'The system was bought for USD 1.5 million with funds provided by the United States Agency for International...' |
| ch01.md | 83 | p. 17 ('mid 1964') | 17 | ok | 'It was installed at the TIFR in mid 1964' |
| ch01.md | 84 | p. 17 | 17 | ok | 'Over 150 institutions from all over India used it effectively for numerous large scale number crunching pro...' |
| ch01.md | 88 | pp. 16-17 | 16-17 | ok | p16: 'When TIFRAC was inaugurated in 1960, ISI decided to build a second generation digital computer'; p17: 'It was not a successful project as the computer was unreliable' |
| ch01.md | 91 | p. 18 | 18 | ok | 'Between 1961 and 1964 twelve computers were installed in Research and Development organizations and two in ...' |
| ch01.md | 93 | p. 15 | 15 | ok | 'It has a preamble which among other clauses states that "Science and technology can make up for deficiencie...' |
| ch01.md | 94 | p. 18 | 18 | ok | '3.2 COMPUTER MANUFACTURE Other than the Scientific Policy Resolution which broadly laid down the policy to ...' |
| ch01.md | 95 | p. 3 (Bhabha Committee, 1963); p. 21 (after the 1962 border war with China); see Ch. 3 | 3, 21 | ok | p3: 'The Bhabha Committee appointed by the Government of India in 1963'; p21: 'After the border skirmish with China in 1962' |
| ch01.md | 99 | pp. 15-16 | 15-16 | ok | p15: 'A computer HEC-2M (Hollerith Electronic Computer Model 2M) was being designed by A.D.Booth at Birbek Colleg...'; p16: 'Around a dozen people learnt to program the computer which was used for some statistical calculations.' |
| ch01.md | 100 | p. 16 | 16 | ok | 'All the manuals were in Russian and the ISI engineers learnt Russian to enable them to maintain the machine.' |
| ch01.md | 103 | p. 7 | 7 | ok | 'In 1955 only a few dozen scientists and engineers in India knew about computers.' |
| ch01.md | 105 | p. 17 | 17 | ok | 'Another computer installed early in India was an IBM 1620 in August 1963 at the Indian Institute of Technol...' |
| ch01.md | 106 | p. 17 (USAID funds through the Kanpur Indo-American Programme); see Ch. 2 | 17 | ok | 'USAID which channelled the funding through the Kanpur indo-American Program (KIAP)' |
| ch02.md | 6 | p. 17 | 17 | ok | 'It was the first computer with a FORTRAN compiler to be installed in an educational institution in India.' |
| ch02.md | 7 | p. 17 | 17 | ok | 'an IBM 1620 in August 1963 at the Indian Institute of Technology, Kanpur' |
| ch02.md | 67 | p. 18 | 18 | ok | 'The IBM 1620 was used 24 x 7' |
| ch02.md | 68 | p. 18 | 18 | ok | 'The IBM 1620 was used 24 x 7 and all students had free access to it.' |
| ch02.md | 72 | p. 18 | 18 | ok | 'IITK also pioneered by introducing in 1964 a compulsory course in programming and numerical methods to all ...' |
| ch02.md | 75 | p. 70 | 70 | ok | 1966 entry: 'M.Tech program in computers in the Electrical Engineering Department started at IIT/Kanpur' |
| ch02.md | 80 | pp. 17-18 | 17-18 | ok | p17: 'As soon as the IBM 1620 started working a ten day intensive course on programming for the faculty of IITK w...'; p18: 'restricting the course to IITK faculty, he invited scientists, engineers, and the faculty members of other ...' |
| ch02.md | 82 | p. 18 | 18 | ok | 'Each course had around 60 participants'; 'conducted thrice a year' |
| ch02.md | 84 | p. 18 | 18 | ok | 'The course was so popular that it was continued till 1975 by the IITK faculty after the American Professors...' |
| ch02.md | 94 | p. 18 | 18 | ok | 'IITK bought an IBM7044 in 1966 (with funds provided by the Government of India)' |
| ch02.md | 122 | p. 34 | 34 | ok | 'again pioneered in starting an undergraduate programme in Computer Science in 1978' |
| ch02.md | 123 | p. 34 | 34 | ok | 'The IIT/Kanpur senate had grudgingly allowed 20 students to be admitted to the Computer Science (CSc) progr...' |
| ch02.md | 124 | p. 34 | 34 | ok | 'Entry to IITs is highly competitive and over 100,000 students took the entrance examination from all over I...' |
| ch02.md | 127 | p. 34 | 34 | ok | 'However, the CSc programme was so popular among the students that the rank of the last student admitted to ...' |
| ch02.md | 128 | p. 34 | 34 | ok | 'This came as a surprise to other IITs and all...' |
| ch02.md | 141 | pp. 17-18, 34 | 17-18, 34 | ok | p17: 'The IBM 1620 was imported with financial assistance of the United States Agency for International Developme...'; p18: 'IITK also pioneered by introducing in 1964 a compulsory course in programming and numerical methods to all ...'; p34: 'Entry to IITs is highly competitive and over 100,000 students took the entrance examination from all over I...' |
| ch02.md | 144 | p. 3 | 3 | ok | 'This department was established in 1970 and was the first breakpoint'; ECIL financed to design computers |
| ch03.md | 8 | pp. 15, 18 | 15, 18 | ok | p15: 'The parliament of India passed the Scientific Policy Resolution in 1958, the full text of which may be foun...'; p18: 'The Directorate General of Technical Development and the Department of Defence Supplies controlled the area...' |
| ch03.md | 9 | p. 18 | 18 | ok | 'Computers were not considered a priority area that deserved foreign exchange outflow.' |
| ch03.md | 12 | pp. 18-19 | 18-19 | ok | p18: 'IBM of the USA and the British Tabulating Machines (which was later named International Computers Ltd., ICL...'; p19: 'The used 1401 computers were dismantled in a factory in Mumbai, the worn out parts were replaced, and the m...' |
| ch03.md | 15 | p. 19 | 19 | ok | 'IBM was also running data centres in major cities to cater to smaller companies which could not afford to r...' |
| ch03.md | 16 | p. 19 | 19 | ok | 'In comparison to IBM its rival International Computers Ltd., a British company which was marketing ICL 1901...' |
| ch03.md | 17 | p. 19 | 19 | ok | 'In 1971 the IBM 1401 was phased out in the USA.) The annual rental charged for a high end 1401 (i.e., one w...' |
| ch03.md | 18 | p. 70 | 70 | ok | 1966 entry: 'Rupee devalued from Rs.4.5 per USD to Rs.7.5 per USD' |
| ch03.md | 19 | p. 70 | 70 | ok | 'Windfall profit to IBM as rentals were quoted in dollars. • ISIJU project complete. • M.Tech program in com...' |
| ch03.md | 20 | p. 19 | 19 | ok | 'In its defence IBM asserted that the rental included free maintenance and the services of a systems enginee...' |
| ch03.md | 21 | p. 19 | 19 | ok | 'A whole generation of maintenance engineers and programmers were trained and nurtured by IBM.' |
| ch03.md | 24 | p. 21 | 21 | ok | 'After the border skirmish with China in 1962 it was realized that electronics and communications were impor...' |
| ch03.md | 25 | p. 21 | 21 | ok | 'Unfortunately Bhabha was killed in an air crash before formally submitting the report.' |
| ch03.md | 27 | p. 21 | 21 | ok | 'It also suggested the constitution of an Electronics Commission (EC) with wide financial and executive powe...' |
| ch03.md | 29 | p. 21 | 21 | ok | 'The committee recommended setting up one very large computer to be imported for a national facility and 3 t...' |
| ch03.md | 30 | p. 24 | 24 | ok | 'It opined that "attaining self-sufficiency in systems engineering and fabrication is of fundamental importa...' |
| ch03.md | 31 | p. 21 | 21 | ok | 'The Bhabha Committee report was discussed by a large group of participants from educational institutions, c...' |
| ch03.md | 32 | pp. 21-22 | 21-22 | ok | p21: 'We do not have a large enough internal market of sufficient volume to justify the chronological development...'; p22: 'However, my comment was not taken seriously.' |
| ch03.md | 33 | p. 22 | 22 | ok | 'Vikram Sarabhai (who succeeded Homi Bhabha) and chaired the conference opined at the concluding session tha...' |
| ch03.md | 34 | p. 22 | 22 | ok | 'I do not think that this could be at the cost of a major national effort, which we must put out without fur...' |
| ch03.md | 35 | pp. 24, 70 | 24, 70 | ok | p24: 'Menon was the Director of TIFR when he took over the DoE.'; p70: '1970 • Department of Electronics (DoE) established by the Government of India with M.G.K.Menon as its Secre...' |
| ch03.md | 37 | p. 23 | 23 | ok | 'The department drafted an elaborate set of rules [38] for import of computers based on essentiality, whethe...' |
| ch03.md | 38 | p. 22 | 22 | ok | 'Thus obtaining foreign exchange for import of equipment required elaborate justification.' |
| ch03.md | 39 | p. 23 | 23 | ok | 'Quadrupling of oil prices in 1973 by the Organization of Petroleum Exporting Countries (OPEC) accentuated t...' |
| ch03.md | 40 | p. 23 | 23 | ok | 'This delay and restriction particularly hurt companies which wanted to import computers for software export.' |
| ch03.md | 41 | p. 23 | 23 | ok | 'The first nuclear test by India in 1974 further aggravated Indo-US relations leading to an embargo on the i...' |
| ch03.md | 42 | p. 24 | 24 | ok | 'Still the DoE kept on delaying the announcement of a minicomputer policy as it was concerned about the requ...' |
| ch03.md | 43 | pp. 24, 71 | 24, 71 | ok | p24: 'A panel on minicomputers chaired by P.V.S.Rao appointed by the DoE [40] opined that mini computers can be m...'; p71: 'Demand for the period 1974-79 projected around 1400 minicomputers. • Santacruz Electronic Export Promotion ...' |
| ch03.md | 44 | p. 27 | 27 | ok | 'The DoE became very unpopular as a number of legitimate requests for the import of computers by educational...' |
| ch03.md | 45 | pp. 25, 70 | 25, 70 | ok | p25: 'S.Srikantan who was chosen to head this division, had designed the mini- computer Trombay Digital Computer ...'; p70: '1969 • TDC 12 computer commissioned at the Bhabha Atomic Research Centre,Mumbai.' |
| ch03.md | 46 | p. 25 | 25 | ok | 'An Operating System, an assembler, BASIC, and FORTRAN compilers were developed.' |
| ch03.md | 47 | p. 25 | 25 | ok | 'This was followed by a TDC 316, a 16 bit computer built in 1975 which also had ECOBOL, a version of COBOL c...' |
| ch03.md | 48 | p. 25 | 25 | ok | 'The numbers of computers sold by ECIL during 1971 to 1978 were 21 TDC 12s, 32 TDC 312s, 35 TDC 316s and 10 ...' |
| ch03.md | 49 | p. 25 | 25 | ok | 'Specification of ECIL Machines Word Memory Cycle Machine length size time Technology Software Typical (bits...' |
| ch03.md | 50 | pp. 25-26 | 25-26 | ok | p25: 'It however worked more like a cottage industry as the volume of production was'; p26: 'Most of the ECIL machines were bought by the Atomic Energy Establishments, government departments and Unive...' |
| ch03.md | 52 | p. 26 | 26 | ok | 'The cost of each system was Rs.30 million and 25 systems were deployed by the Indian Air Force' |
| ch03.md | 53 | p. 25 | 25 | ok | '75 ruggedized TDC 316 computers were deployed in a defence project' |
| ch03.md | 54 | p. 26 | 26 | ok | 'In the published literature this important contribution of ECIL is not mentioned.' |
| ch03.md | 55 | p. 26 | 26 | ok | 'The deployment of TDC 312s in data logging of rolling mills and in controlling the cutting of billets in st...' |
| ch03.md | 56 | p. 26 | 26 | ok | 'The DoE gave grants/loans of Rs. 37.44 million to ECIL' |
| ch03.md | 57 | p. 26 | 26 | ok | 'Many of them later joined the private manufacturers and software companies to lead groups there.' |
| ch03.md | 88 | p. 22 | 22 | ok | 'The Ministry of Labour, Employment and Rehabilitation had set up a committee in 1969 under the chairmanship...' |
| ch03.md | 103 | pp. 22-23 | 22-23 | ok | p22: 'The report of this committee constrained the introduction of computers in banks, insurance companies and ma...'; p23: 'White collar workers who were quite vociferous saw these computers primarily as labour saving devices and n...' |
| ch03.md | 104 | p. 23 | 23 | ok | 'The committee felt that in India with large scale unemployment, the use of computers and other sophisticate...' |
| ch03.md | 105 | p. 23 | 23 | ok | 'The Department of Electronics was constrained by these observations and had to move cautiously.' |
| ch03.md | 106 | p. 19 | 19 | ok | 'A whole generation of maintenance engineers and programmers were trained and nurtured by IBM.' |
| ch03.md | 107 | p. 26 | 26 | ok | 'However, the contribution of the ECIL was in the training of over a thousand engineers in designing systems...' |
| ch03.md | 108 | pp. 18, 71 | 18, 71 | ok | p18: 'conducted thrice a year ... continued till 1975'; p71 (1972): 'Separate Computer Science Programme starts at IIT/Kanpur. Masters and Phd degrees offered' |
| ch03.md | 109 | p. 27 | 27 | ok | 'set up in 1972 with a grant of Rs.2.85 million from the DoE and USD 2 million from the UNDP' |
| ch03.md | 113 | p. 27 | 27 | ok | 'The DoE invested Rs.31.72 million and the UNDP provided funding of USD 4.4 million' |
| ch03.md | 114 | pp. 28, 71 | 28, 71 | ok | p28: 'For example, the RCC at Jadavpur University started in 1977 and had a Burroughs 6738 main frame and allowed...'; p71: 'RCC to give low cost computer time to students and software exporters. • ECIL imports IRIS 55 (from France)...' |
| ch03.md | 115 | p. 28 | 28 | ok | 'Foreseeing the departure of IBM from India, the DoE established CMC in 1976 to maintain imported computers ...' |
| ch03.md | 116 | p. 27 | 27 | ok | 'A core group of scientists who were employed by the NCST later became leaders in the profession.' |
| ch03.md | 117 | p. 28 | 28 | ok | 'Recognizing the potential of software export DoE allowed import of computers exclusively meant for software...' |
| ch03.md | 118 | p. 28 | 28 | ok | 'TCS was also an early pioneer which actively scouted for programming work from outside India in Iran, Switz...' |
| ch03.md | 119 | p. 28 | 28 | ok | 'Tata and Burroughs formed a company to manufacture computers in Mumbai in 1975.' |
| ch03.md | 120 | p. 59 | 59 | ok | 'As a poor country with a low demand for computers it was strategically incorrect to try to design computers...' |
| ch03.md | 121 | p. 59 | 59 | ok | 'The fear of unemployment which was in the backdrop while taking decisions regarding the use of computers in...' |
| ch03.md | 126 | pp. 27-28 | 27-28 | ok | p27: NCSDCT, NIC set up by DoE; p28: CMC, RCCs, import for software export (1974) |
| ch03.md | 127 | pp. 19, 26-28 | 19, 26-28 | ok | p19: 'IBM was also running data centres in major cities to cater to smaller companies which could not afford to r...'; p26: 'An important contribution of the ECIL was in providing ruggedized computers for the Air Defence Ground Envi...'; p27: 'The DoE established the National Centre for Software Development and Computing Techniques (NCSDCT) at TIFR,...'; p28: 'Recognizing the importance of designing an air defence system for India the DoE funded the ADGES project at...' |
| ch03.md | 130 | p. 82 | 82 | ok | '1975 Internal emergency declared by Indira Gandhi when her election was ruled invalid by the Allahabad High...' |
| ch03.md | 132 | p. 24 | 24 | ok | 'A minicomputer policy was ultimately announced in 1978 which was more or less along the recommendations of ...' |
| ch03.md | 133 | p. 24 | 24 | ok | 'Also 1978 was the year IBM left India and the policy announcement was timely as a number of private entrepr...' |
| ch04.md | 4 | p. 23 | 23 | ok | 'long delay of one to three years in obtaining clearance to import computers' |
| ch04.md | 17 | p. 19 | 19 | ok | 'In 1971 the IBM 1401 was phased out in the USA.) The annual rental charged for a high end 1401 (i.e., one w...' |
| ch04.md | 18 | pp. 18-19 | 18-19 | ok | p18: 'IBM of the USA and the British Tabulating Machines (which was later named International Computers Ltd., ICL...'; p19: 'In other words IBM maintained that it was selling a computing service rather than just renting a computer.' |
| ch04.md | 31 | p. 19 | 19 | ok | 'The first computer at the Tata Consultancy Services was an IBM 1401' |
| ch04.md | 37 | p. 22 | 22 | ok | 'India had a perpetual balance of trade deficit.' |
| ch04.md | 38 | p. 23 | 23 | ok | 'The department drafted an elaborate set of rules [38] for import of computers based on essentiality, whethe...' |
| ch04.md | 39 | p. 23 | 23 | ok | 'Quadrupling of oil prices in 1973 by the Organization of Petroleum Exporting Countries (OPEC) accentuated t...' |
| ch04.md | 40 | p. 23 | 23 | ok | 'The first nuclear test by India in 1974 further aggravated Indo-US relations leading to an embargo on the i...' |
| ch04.md | 42 | p. 27 | 27 | ok | 'The DoE became very unpopular as a number of legitimate requests for the import of computers by educational...' |
| ch04.md | 50 | p. 28 | 28 | ok | 'Recognizing the potential of software export DoE allowed import of computers exclusively meant for software...' |
| ch04.md | 52 | pp. 21-22 | 21-22 | ok | p21: 'Foreign exchange can also be earned by software export."'; p22: 'However, my comment was not taken seriously.' |
| ch04.md | 61 | p. 28 | 28 | ok | 'TCS converted software running on computers of other manufacturers to run on the Burroughs computer.' |
| ch04.md | 64 | p. 28 | 28 | ok | 'S.Ramadorai, who succeeded F.C.Kohli as the CEO of TCS in 1996, has written the history of TCS [115]' |
| ch04.md | 65 | p. 28 | 28 | ok | 'Tata and Burroughs formed a company to manufacture computers in Mumbai in 1975.' |
| ch04.md | 68 | p. 28 | 28 | ok | 'TCS was also an early pioneer which actively scouted for programming work from outside India in Iran, Switz...' |
| ch04.md | 72 | p. 29 | 29 | ok | 'The major events during this period were the exit of IBM, the entry of private manufacturers of computers w...' |
| ch04.md | 74 | p. 29 | 29 | ok | 'There was insignificant software export in 1978' |
| ch04.md | 91 | p. 18 | 18 | ok | 'Over 1500 scientists working in a number of Universities and research laboratories were trained.' |
| ch04.md | 92 | p. 19 | 19 | ok | 'A whole generation of maintenance engineers and programmers were trained and nurtured by IBM.' |
| ch04.md | 93 | p. 26 | 26 | ok | 'However, the contribution of the ECIL was in the training of over a thousand engineers in designing systems...' |
| ch04.md | 94 | p. 27 | 27 | ok | 'This centre was set up in 1972 with a grant of Rs.2.85 million from the DoE and USD 2 million from the Unit...' |
| ch04.md | 100 | pp. 23, 28 | 23, 28 | ok | p23: import rules based on essentiality/foreign exchange; p28: 'allowed import of computers exclusively meant for software export' |
| ch04.md | 103 | p. 19 | 19 | ok | 'IBM was also running data centres in major cities' |
| ch04.md | 106 | pp. 24, 29 | 24, 29 | ok | p24: 'Also 1978 was the year IBM left India and the policy announcement was timely as a number of private entrepr...'; p29: 'In 1973 India had enacted the Foreign Exchange Regulation Act (FERA) to conserve foreign exchange.' |
| ch04.md | 107 | p. 29 | 29 | ok | 'The number of computers in India which was less than 1000 in 1978' |
| ch05.md | 6 | pp. 18-19 | 18-19 | ok | p18: 'IBM was more aggressive and proposed to the Government of India that it would manufacture mechanical key pu...'; p19: 'IBM's business model was to import used (or As Is) IBM 1401 computers at a so called inter-company billing ...' |
| ch05.md | 7 | pp. 18-19 | 18-19 | ok | p18: 'IBM chose the 1401 data processing machine as suitable'; p19: 'The used 1401 computers were dismantled in a factory in Mumbai, the worn out parts were replaced, and the m...' |
| ch05.md | 8 | p. 19 | 19 | ok | 'In 1971 the IBM 1401 was phased out in the USA.) The annual rental charged for a high end 1401 (i.e., one w...' |
| ch05.md | 9 | p. 19 | 19 | ok | 'IBM was also running data centres in major cities to cater to smaller companies which could not afford to r...' |
| ch05.md | 12 | p. 19 | 19 | ok | 'In other words IBM maintained that it was selling a computing service rather than just renting a computer.' |
| ch05.md | 15 | p. 19 | 19 | ok | 'A whole generation of maintenance engineers and programmers were trained and nurtured by IBM.' |
| ch05.md | 17 | p. 29 | 29 | ok | 'Under this act foreign companies except those considered essential were to dilute equity to 40% and take an...' |
| ch05.md | 22 | p. 29 | 29 | ok | 'In the meanwhile IBM gave a proposal to the government to set up a 100% export oriented manufacturing unit ...' |
| ch05.md | 24 | p. 29 | 29 | ok | 'Indian Railways, the Planning Commission, many textiles and petrochemical companies, and numerous education...' |
| ch05.md | 26 | p. 30 | 30 | ok | 'ICL, the British Company, diluted its equity as per FERA and formed the International Computer India Manufa...' |
| ch05.md | 27 | p. 30 | 30 | ok | 'A coalition government led by Morarji Desai took over.' |
| ch05.md | 36 | p. 29 | 29 | ok | 'After prolonged negotiations the government was unwilling to relax FERA for IBM.' |
| ch05.md | 43 | p. 29 | 29 | ok | 'The computers which were rented were sold to the customers at their book value which was almost zero.' |
| ch05.md | 44 | pp. 29-30 | 29-30 | ok | p29: 'The card manufacture and data centre operations were taken over by a group of ex-IBM employees who formed a...'; p30: 'Data Machines (IDM).' |
| ch05.md | 45 | p. 30 | 30 | ok | 'Maintenance of IBM computers was taken over by the Computer Maintenance Corporation (CMC) which had been se...' |
| ch05.md | 46 | p. 28 | 28 | ok | 'CMC was setup at a cost of Rs.53 million' |
| ch05.md | 48 | p. 30 | 30 | ok | 'All spare parts of IBM 1401s and other computers were sold to CMC at nominal price.' |
| ch05.md | 50 | p. 29 | 29 | ok | 'IBM's confidence arose from the fact that there were over 150 IBM installations in India.' |
| ch05.md | 51 | p. 30 | 30 | ok | 'There was thus no disruption of operations of computers [4].' |
| ch05.md | 56 | p. 40 | 40 | ok | 'The ones who started manufacturing were ... ORG Systems, Baroda' |
| ch05.md | 57 | p. 29 | 29 | ok | 'There was insignificant software export in 1978 whereas it increased to USD128 million in 1990.' |
| ch05.md | 58 | p. 30 | 30 | ok | 'The committee observed that there have been long delays in importing computers due to the cumbersome proced...' |
| ch05.md | 59 | p. 30 | 30 | ok | 'Menon was moved away from the DoE to the Department of Science and Technology in 1978 and Biswajit Nag beca...' |
| ch05.md | 60 | p. 31 | 31 | ok | 'It added that small scale entrepreneurs should be preferred for manufacturing special purpose computers for...' |
| ch05.md | 62 | p. 31 | 31 | ok | 'Only the public sector company ECIL would be allowed to manufacture 32 bit computers.' |
| ch05.md | 63 | p. 31 | 31 | ok | 'The policy also stated that it would continue to be restrictive in allowing use of computers in areas where...' |
| ch05.md | 64 | pp. 39-40 | 39-40 | ok | p39: 'Even though this policy did'; p40: 'not completely free the industry from the "licence-permit raj" it allowed the entry of private companies to...' |
| ch05.md | 65 | p. 40 | 40 | ok | 'The ones who started manufacturing were DCM Data Products, Delhi, ORG Systems, Baroda, Hindustan Computers ...' |
| ch05.md | 93 | p. 40 | 40 | ok | 'These companies designed and fabricated printed circuit boards, mounted and soldered all the components and...' |
| ch05.md | 94 | p. 40 | 40 | ok | 'As software could not be imported they had to develop operating systems, device drivers, compilers and appl...' |
| ch05.md | 95 | p. 40 | 40 | ok | 'AT&T was not allowed to market UNIX by the US regulators with the result that it was almost "open source" w...' |
| ch05.md | 96 | pp. 36, 40 | 36, 40 | ok | p36: 'A committee set up by the Reserve Bank of India (RBI) with R.Rangarajan as its chairman recommended that al...'; p40: 'UNIX became the operating system of choice as Rangarajan Committee on bank computerization [66] had standar...' |
| ch05.md | 97 | p. 40 | 40 | ok | 'This market was large and could not be ignored.' |
| ch05.md | 98 | p. 40 | 40 | ok | 'Thus during 1978-1984 a large number of systems programmers in India became experts in UNIX development and...' |
| ch05.md | 99 | pp. 40, 66 (ref. 73) | 40, 66 (ref. 73) | ok | p40: 'AT&T was not allowed to market UNIX by the US regulators with the result that it was almost "open source" w...'; p66: 'See also Reference [5], p.263. [71] V.Rajaraman was a member of the review team and the report was submitte...' |
| ch05.md | 101 | p. 26 | 26 | ok | 'However, the contribution of the ECIL was in the training of over a thousand engineers in designing systems...' |
| ch05.md | 102 | p. 40 | 40 | ok | 'ECIL found it difficult to compete with these companies and lost many of their designers to the private sec...' |
| ch05.md | 103 | p. 40 | 40 | ok | 'These companies designed mother boards and device drivers, modified the UNIX OS and wrote compilers from sc...' |
| ch05.md | 104 | p. 31 | 31 | ok | 'Locally made DCM computers were used as terminals at various venues and connected to a Hewlett Packard server.' |
| ch05.md | 105 | p. 31 | 31 | ok | 'He had heard from the private entrepreneurs during his interactions with them when he was organizing the As...' |
| ch05.md | 106 | p. 34 | 34 | ok | 'The IIT/Kanpur senate had grudgingly allowed 20 students to be admitted to the Computer Science (CSc) progr...' |
| ch05.md | 107 | p. 34 | 34 | ok | 'The IIT/Kanpur senate had grudgingly allowed 20 students to be admitted to the Computer Science (CSc) progr...' |
| ch05.md | 108 | p. 34 | 34 | ok | 'The panel recommended expanding the undergraduate programmes in Computer Science at IITs and other engineer...' |
| ch05.md | 109 | p. 34 | 34 | ok | 'In the Indian education system, after graduation from high school, a large number of students enroll in a t...' |
| ch05.md | 110 | pp. 34-35 | 34-35 | ok | p35: 'MCAs were expected to design software systems for management and business applications' |
| ch05.md | 111 | p. 35 | 35 | ok | 'Initially the Government of India decided to fully fund ten institutions to start this programme.' |
| ch05.md | 112 | p. 35 | 35 | ok | 'This programme which was uniquely Indian provided an opportunity to a large number of B.Sc/B.Com students t...' |
| ch05.md | 113 | p. 42 | 42 | ok | 'NIIT was established in 1981' |
| ch05.md | 115 | p. 33 | 33 | ok | 'In 1982 there was a waiting time of over 2 years to get a land line telephone connection.' |
| ch05.md | 116 | p. 35 | 35 | ok | 'In 1981 the Electronic Commission appointed a committee with me as its chairman to promote software export ...' |
| ch05.md | 118 | p. 36 | 36 | ok | 'The increase in computer use by banks was a red flag to the trade unions and they observed 1984 as "anti- c...' |
| ch05.md | 120 | pp. 30-31 | 30-31 | ok | p30: 'In 1984 Indira Gandhi was assassinated and her son Rajiv Gandhi took over as the Prime Minister.'; p31: 'In 1984, Indira Gandhi was assassinated and Rajiv Gandhi became the Prime Minister.' |
| ch05.md | 122 | p. 31 | 31 | ok | 'A liberalized policy on minicomputers was announced in 1984 with the following main highlights [55]: • Any ...' |
| ch05.md | 123 | p. 32 | 32 | ok | '• Assembled boards with microprocessors and boards with interface electronics could be imported.' |
| ch05.md | 124 | p. 32 | 32 | ok | 'Thus local manufacturing of boards slowly disappeared. • Import of application software was allowed and dut...' |
| ch05.md | 125 | p. 40 | 40 | ok | 'growth of computers went up by 100% and the cost went down by 50%'; 'screw driver' |
| ch05.md | 126 | p. 41 | 41 | ok | 'His reply was that his job was to locate companies in Taiwan, Singapore and Hongkong which could provide re...' |
| ch05.md | 127 | p. 41 | 41 | ok | 'His reply was that his job was to locate companies in Taiwan, Singapore and Hongkong which could provide re...' |
| ch05.md | 128 | p. 42 | 42 | ok | 'The only major failing was not investing enough resources to develop a local integrated circuit manufacturi...' |
| ch05.md | 129 | p. 28 | 28 | ok | 'Even though Menon understood the importance of manufacturing semiconductor devices and set up a committee i...' |
| ch05.md | 130 | p. 32 | 32 | ok | 'Earlier it used to be over 100%. • Sending engineers abroad to develop and maintain software for clients at...' |
| ch05.md | 131 | pp. 29, 41 | 29, 41 | ok | p29: 'USD128 million in 1990'; p41: 'USD 131 million in 1990' |
| ch05.md | 132 | p. 29 | 29 | ok | 'The major events during this period were the exit of IBM, the entry of private manufacturers of computers w...' |
| ch06.md | 9 | p. 29 | 29 | ok | 'The major events during this period were the exit of IBM, the entry of private manufacturers of computers w...' |
| ch06.md | 25 | p. 32 | 32 | ok | 'Software was exempted from excise duty. • Customs duty on imported computers for software export was reduced.' |
| ch06.md | 26 | p. 29 | 29 | ok | 'The number of computers in India which was less than 1000 in 1978 increased to 80,000 in 1990.' |
| ch06.md | 65 | p. 35 | 35 | ok | 'In 1981 the Electronic Commission appointed a committee with me as its chairman to promote software export ...' |
| ch06.md | 66 | p. 32 | 32 | ok | 'Earlier it used to be over 100%. • Sending engineers abroad to develop and maintain software for clients at...' |
| ch06.md | 67 | p. 32 | 32 | ok | 'However, the importer was expected to export software and earn 250% of the cost of the imported computer wi...' |
| ch06.md | 74 | p. 36 | 36 | ok | 'The DoE negotiated with the Department of Telecommunication (DoT) in 1985 to allow Texas Instruments (TI) t...' |
| ch06.md | 93 | pp. 29, 41 | 29, 41 | ok | p29: 'USD128 million in 1990'; p41: 'USD 131 million in 1990' |
| ch06.md | 96 | p. 42 | 42 | ok | 'NASSCOM started with 38 members in 1988 and by 1999 it had 464 members.' |
| ch06.md | 114 | p. 34 | 34 | ok | 'It was felt by the panel that India needed a large number of persons to develop business/management informa...' |
| ch06.md | 115 | p. 35 | 35 | ok | 'The availability of well trained MCAs was one of the contributing factors for the rapid growth of software ...' |
| ch06.md | 116 | p. 42 | 42 | ok | 'NIIT was established in 1981 and started a franchising model to spread their courses to smaller towns in In...' |
| ch07.md | 6 | p. 34 | 34 | ok | 'In 1980 the Electronics Commission foresaw the problem of scarcity of human resources for the emerging comp...' |
| ch07.md | 7 | p. 34 | 34 | ok | 'A Panel on Computer Manpower Development under my chairmanship (I was also a member of the Electronics Commission during 1979-1982)' |
| ch07.md | 8 | p. 34 | 34 | ok | 'Another novel proposal of the panel was to start a new programme called Master of Computer Applications (MCA).' |
| ch07.md | 9 | p. 34 | 34 | ok | 'In the Indian education system, after graduation from high school, a large number of students enroll in a t...' |
| ch07.md | 10 | p. 34 | 34 | ok | 'It was felt by the panel that India needed a large number of persons to develop business/management informa...' |
| ch07.md | 11 | p. 34 | 34 | ok | 'The curriculum was planned to encompass three disciplines: computer science with emphasis in software engin...' |
| ch07.md | 12 | p. 35 | 35 | ok | 'Initially the Government of India decided to fully fund ten institutions to start this programme.' |
| ch07.md | 13 | pp. 35, 66 | 35, 66 | ok | p35: 'Details of the MCA programme may be found in [60, 61]'; p66: ref [60] CSI Communication, Vol.5, No.4, October 1981 |
| ch07.md | 14 | p. 35 | 35 | ok | 'The availability of well trained MCAs was one of the contributing factors for the rapid growth of software ...' |
| ch07.md | 15 | p. 56 | 56 | ok | 'The number of MCAs graduating in 1998 was around 7000 whereas it jumped to 120,000 by 2010 [108].' |
| ch07.md | 16 | p. 34 | 34 | ok | 'Entry to IITs is highly competitive and over 100,000 students took the entrance examination from all over I...' |
| ch07.md | 17 | p. 34 | 34 | ok | 'a Department of Computer Science and Engineering was started in all the IITs' |
| ch07.md | 25 | p. 36 | 36 | ok | 'The DoE set up a committee in 1985 with S.Sampath as its chairman which suggested training teachers in Comp...' |
| ch07.md | 28 | p. 42 | 42 | ok | 'NIIT was established in 1981' |
| ch07.md | 34 | p. 42 | 42 | ok | 'NIIT was established in 1981 and started a franchising model to spread their courses to smaller towns in In...' |
| ch07.md | 39 | p. 42 | 42 | ok | 'At the same time private initiatives giving non-formal training in software development and computer use al...' |
| ch07.md | 46 | p. 34 | 34 | ok | 'Entry to IITs is highly competitive and over 100,000 students took the entrance examination from all over I...' |
| ch07.md | 101 | p. 36 | 36 | ok | 'The DoE negotiated with the Department of Telecommunication (DoT) in 1985 to allow Texas Instruments (TI) t...' |
| ch07.md | 102 | p. 36 | 36 | ok | 'This was the first step in breaking the monopoly of the DoT in communications and had far reaching conseque...' |
| ch08.md | 4 | p. 33 | 33 | ok | 'In 1984 a research group was formed under the leadership of Satyanarayan (Sam) Pitroda assisted by M.V.' |
| ch08.md | 7 | pp. 33, 36 | 33, 36 | ok | p33: 'The public switched networks as well as overseas communication links were the monopoly of the government an...'; p36: 'The DoE negotiated with the Department of Telecommunication (DoT) in 1985 to allow Texas Instruments (TI) t...' |
| ch08.md | 8 | p. 31 | 31 | ok | 'Asian Games were to be held in Delhi in 1982 and Rajiv Gandhi, the son of the Prime Minister Indira Gandhi,...' |
| ch08.md | 9 | p. 31 | 31 | ok | 'In 1984, Indira Gandhi was assassinated and Rajiv Gandhi became the Prime Minister.' |
| ch08.md | 10 | pp. 29, 37 | 29, 37 | ok | p29: 'Even though the political environment was choppy during this period, Rajiv Gandhi who belonged to the post-...'; p37: 'The Science Advisory Committee to the Prime Minister chaired by C.N.R.Rao set up a committee in 1986 with m...' |
| ch08.md | 12 | pp. 31-32, 40 | 31-32, 40 | ok | p31: 'A liberalized policy on minicomputers was announced in 1984 with the following main highlights [55]: • Any ...'; p32: 'In other words fully populated boards could be imported which were more reliable and cheaper than boards fa...'; p40: 'The growth was due to the liberal import of fully assembled sub-systems (i.e., populated boards).' |
| ch08.md | 13 | p. 32 | 32 | ok | 'The policies to protect public sector companies, ECIL and CMC, were continued by: • Reserving manufacture o...' |
| ch08.md | 14 | p. 32 | 32 | ok | 'Earlier it used to be over 100%. • Sending engineers abroad to develop and maintain software for clients at...' |
| ch08.md | 18 | p. 32 | 32 | ok | 'However, the importer was expected to export software and earn 250% of the cost of the imported computer wi...' |
| ch08.md | 19 | pp. 32-33 | 32-33 | ok | p32: 'However, the importer was expected to export software and earn 250% of the cost of the imported computer wi...'; p33: 'This network was allowed to be used by software exporters at a concessional tariff.' |
| ch08.md | 23 | pp. 34-36 | 34-36 | ok | p34: '5.3 GOVERNMENT INITIATIVES We saw that during 1970-78 the Department of Electronics had taken a number of i...'; p35: 'The centre at the IISc/Bangalore, of which I was the coordinator, specialized in developing CAD tools in el...'; p36: 'The DoE negotiated with the Department of Telecommunication (DoT) in 1985 to allow Texas Instruments (TI) t...' |
| ch08.md | 24 | pp. 33, 42 | 33, 42 | ok | p33: 'The public switched networks as well as overseas communication links were the monopoly of the government an...'; p42: 'N.Vittal an IAS officer who took over the DoE in 1990 was dynamic and more business savvy as opposed to the...' |
| ch08.md | 25 | p. 36 | 36 | ok | 'This was the first step in breaking the monopoly of the DoT in communications and had far reaching conseque...' |
| ch08.md | 29 | p. 36 | 36 | ok | 'The DoE negotiated with the Department of Telecommunication (DoT) in 1985 to allow Texas Instruments (TI) t...' |
| ch08.md | 33 | p. 36 | 36 | ok | 'TI's centre in Bangalore developed software tools' |
| ch08.md | 35 | p. 42 | 42 | ok | 'Indian engineers could design large scale integrated circuits, including combined analog and digital system...' |
| ch08.md | 40 | p. 33 | 33 | ok | 'In 1982 there was a waiting time of over 2 years to get a land line telephone connection.' |
| ch08.md | 41 | p. 33 | 33 | ok | 'Another company named the Videsh Sanchar Nigam Ltd. (VSNL) was established in 1986 to improve overseas comm...' |
| ch08.md | 42 | p. 33 | 33 | ok | 'CDOT recruited a highly motivated group of engineers and developed a rugged switch and a digital exchange i...' |
| ch08.md | 43 | p. 33 | 33 | ok | 'Every nook and corner of India was connected within 5 years.' |
| ch08.md | 50 | p. 36 | 36 | ok | 'The increase in computer use by banks was a red flag to the trade unions and they observed 1984 as "anti- c...' |
| ch08.md | 53 | pp. 31, 39 | 31, 39 | ok | p31: 'The policy also stated that it would continue to be restrictive in allowing use of computers in areas where...'; p39: '5.4 CONSEQUENCES OF GOVERNMENT POLICY The minicomputer policy of 1978 opened up the computer industry and s...' |
| ch08.md | 54 | p. 38 | 38 | ok | 'In 1984 it handled over 5 million passengers travelling in over 600 long distance trains with around 50,000...' |
| ch08.md | 55 | p. 38 | 38 | ok | 'It had 50 counters and customers could go to any counter to get a reservation done for any train [68].' |
| ch08.md | 56 | p. 38 (for 1984 and 1986) | 38 | ok | 'began in 1984 and was completed in 1986' |
| ch08.md | 57 | p. 38 | 38 | ok | 'Instead of waiting for hours to get a reservation and having to run from counter to counter the customers c...' |
| ch08.md | 58 | p. 38 | 38 | ok | 'The counter clerks were also happy as they could reconcile the collected cash against issued tickets with t...' |
| ch08.md | 59 | p. 38 | 38 | ok | 'There was also no reduction of staff; in fact there was an increase as more counters were operated with mor...' |
| ch08.md | 60 | p. 38 | 38 | ok | 'The system interestingly was developed on a VAX cluster connected to terminals at the counters.' |
| ch08.md | 61 | p. 38 | 38 | ok | 'It was the first time in the world that such a system was developed for on-line transaction processing on a...' |
| ch08.md | 62 | p. 38 | 38 | ok | 'There was an attitudinal change among both the general public and the white collar workers about computeriz...' |
| ch08.md | 63 | p. 39 | 39 | ok | 'The use of manually filled ballot papers has been discontinued.) The effectiveness of computers in three hi...' |
| ch08.md | 64 | p. 38 | 38 | ok | 'The counter clerks were also happy as they could reconcile the collected cash against issued tickets with t...' |
| ch08.md | 65 | p. 36 | 36 | ok | 'The Ministry of Human Resources Development of the Government of India gave a grant of Rs.500 million (Rs.1...' |
| ch08.md | 66 | p. 36 | 36 | ok | 'A team led by an official of the US Department of State visited the institute and a number of conditions fo...' |
| ch08.md | 67 | p. 37 | 37 | ok | 'The US government did not give an export licence to Cray before the date specified in the contract signed b...' |
| ch08.md | 68 | p. 37 | 37 | ok | 'The committee decided to cancel the order given to Cray and buy instead a Cyber992 mainframe with a vectori...' |
| ch08.md | 69 | p. 37 | 37 | ok | 'The denial of Cray was a blessing in disguise as the money saved was used to buy state-of-the-art powerful ...' |
| ch08.md | 72 | p. 37 | 37 | ok | 'The committee suggested a mission mode project to build parallel computers with a speed of a giga-flop or a...' |
| ch08.md | 73 | p. 37 | 37 | ok | 'Consequently, the DoE established a Centre for Development of Advanced Computing (CDAC) at Pune in 1988 wit...' |
| ch08.md | 74 | pp. 37-38 | 37-38 | ok | p37: 'Besides the effort by CDAC there was a flurry of activities in designing parallel computers between 1985 an...'; p38: 'Notable among these were FLOSOLVER, a machine to solve fluid dynamics problems by the National Aeronautical...' |
| ch08.md | 76 | p. 38 | 38 | ok | 'All the projects described above generated a large pool of engineers adept in designing and programming par...' |
| ch08.md | 77 | p. 37 | 37 | ok | 'Besides its efforts in parallel computing, another notable contribution of CDAC was the development of an i...' |
| ch08.md | 78 | p. 35 | 35 | ok | 'Many scientists went abroad to get trained in the design and use of CAD tools and later on developed tools ...' |
| ch08.md | 79 | p. 36 | 36 | ok | 'This programme led to the design of parallel computers, expert systems in medicine, soft computing includin...' |
| ch08.md | 80 | p. 35 | 35 | ok | 'In 1984 the DoE along with the UNDP funded a programme called Computer Aided Management in the three Indian...' |
| ch08.md | 81 | p. 36 | 36 | ok | 'The DoE set up a committee in 1985 with S.Sampath as its chairman which suggested training teachers in Comp...' |
| ch08.md | 82 | pp. 38-39 | 38-39 | ok | p38: 'In 1986 the DoE obtained a funding of USD 6 million spread over 4 years from the UNDP with Government of In...'; p39: 'Rs.41 million for a project titled Education and Research in Computer Networks (ERNET).' |
| ch08.md | 83 | p. 39 | 39 | ok | 'ERNET also brought the Internet to India under the leadership of S.Ramani of NCST, Mumbai.' |
| ch08.md | 84 | p. 42 | 42 | ok | 'By 1990 a good foundation had been laid in advanced technology areas such as CAD/CAM, parallel computer dev...' |
| ch08.md | 88 | p. 42 | 42 | ok | 'This period also saw the establishment of two industry groups: the Manufacturer's Association for Informati...' |
| ch08.md | 89 | p. 42 | 42 | ok | 'NASSCOM was fortunate in employing Dewang Mehta as its President in 1991.' |
| ch08.md | 90 | p. 42 | 42 | ok | 'NASSCOM was fortunate in employing Dewang Mehta as its President in 1991.' |
| ch08.md | 91 | p. 42 | 42 | ok | 'A difference of opinion between two technocrats in the DoE in 1989 led to the department being taken over b...' |
| ch08.md | 92 | p. 42 | 42 | ok | 'He was instrumental in setting up STPs and obtaining a host of fiscal concessions to the software industry ...' |
| ch08.md | 94 | p. 39 | 39 | ok | 'Software Technology Parks provided infrastructure such as buildings, work stations and continuous uninterru...' |
| ch08.md | 96 | p. 39 | 39 | ok | 'As the investment required to set up a company in STP was low, this initiative allowed many small entrepren...' |
| ch08.md | 97 | p. 39 | 39 | ok | 'The first STP was established in Bangalore in 1990.' |
| ch08.md | 101 | p. 41 | 41 | ok | 'Breaking the monopoly of VSNL (the overseas communication company in the public sector) by the DoE, providi...' |
| ch08.md | 103 | pp. 29, 41 | 29, 41 | ok | p29: 'USD128 million in 1990'; p41: 'USD 131 million in 1990' |
| ch08.md | 106 | pp. 29, 31, 33 | 29, 31, 33 | ok | p29: 'Even though the political environment was choppy during this period, Rajiv Gandhi who belonged to the post-...'; p31: 'Asian Games were to be held in Delhi in 1982 and Rajiv Gandhi, the son of the Prime Minister Indira Gandhi,...'; p33: 'Under the leadership of Rajiv Gandhi two policy decisions were taken.' |
| ch08.md | 111 | pp. 33, 36, 39, 42 | 33, 36, 39, 42 | ok | p33: 'Another company named the Videsh Sanchar Nigam Ltd. (VSNL) was established in 1986 to improve overseas comm...'; p36: 'The DoE negotiated with the Department of Telecommunication (DoT) in 1985 to allow Texas Instruments (TI) t...'; p39: 'Software Technology Parks provided infrastructure such as buildings, work stations and continuous uninterru...'; p42: 'A difference of opinion between two technocrats in the DoE in 1989 led to the department being taken over b...' |
| ch08.md | 112 | p. 30 | 30 | ok | 'In the general election of 1989 the Congress party lost ... This coalition was unstable and fell in 1990' |
| ch08.md | 113 | p. 43 | 43 | ok | 'During the election campaign Rajiv Gandhi was assassinated' |
| ch08.md | 114 | p. 43 | 43 | ok | 'India started with a near default economic situation in 1991 which forced the government to open the econom...' |
| ch09.md | 1 | p. 43 | 43 | ok | 'Manmohan Singh, a professional economist, was inducted as the finance minister by P.V.Narasimha Rao.' |
| ch09.md | 7 | pp. 44, 48 | 44, 48 | ok | p44: '6.3 CONSEQUENCES OF GOVERNMENT POLICY CHANGES With the changes in the government policies there was a sudde...'; p48: 'Software Services Export Revenue Value in Year million US Growth Dollars Percent 1990-1991 128 28 1991-1992...' |
| ch09.md | 9 | p. 43 | 43 | ok | 'India was about to default on foreign loans; however it was bailed out by the International Monetary Fund (...' |
| ch09.md | 11 | p. 43 | 43 | ok | 'The Rupee was devalued (from Rs.17.5 to Rs.26 per USD)' |
| ch09.md | 24 | p. 48 | 48 | ok | 'Software Services Export Revenue Value in Year million US Growth Dollars Percent 1990-1991 128 28 1991-1992...' |
| ch09.md | 25 | p. 44 | 44 | ok | 'According to N.R.Narayana Murthy [80], a very successful entrepreneur (who had founded INFOSYS a software c...' |
| ch09.md | 30 | p. 44 | 44 | ok | 'This allowed companies to: (i) open offices abroad, (ii) convert rupees to foreign currency to meet marketi...' |
| ch09.md | 31 | p. 44 | 44 | ok | 'The devaluation of the rupee enabled Indian software companies to be competitive in selling their services ...' |
| ch09.md | 46 | p. 43 | 43 | ok | 'The industry also provided employment to 160,000 software engineers [79].' |
| ch09.md | 48 | p. 45 | 45 | ok | 'The salary of software engineers in India was about 20% that of an equivalent western engineer.' |
| ch09.md | 69 | pp. 44-45 | 44-45 | ok | p44: 'According to N.R.Narayana Murthy [80], a very successful entrepreneur (who had founded INFOSYS a software c...'; p45: 'The Indian software companies set up secure areas in their premises devoted entirely to a particular client...' |
| ch09.md | 70 | p. 45 | 45 | ok | 'Any bugs reported by the customers when their shift ended could be fixed during the prime shift in India en...' |
| ch09.md | 76 | p. 45 | 45 | ok | 'An ISO 9001 [83] certificate was awarded only after auditors inspected the processes used by a software com...' |
| ch09.md | 77 | p. 45 | 45 | ok | 'The Motorola (India) software team was the first team in the world to attain this maturity level in 1993.' |
| ch09.md | 79 | p. 46 | 46 | ok | 'The process orientation allowed companies which were recruiting large numbers of employees each year to qui...' |
| ch09.md | 80 | p. 48 | 48 | ok | 'Software Services Export Revenue Value in Year million US Growth Dollars Percent 1990-1991 128 28 1991-1992...' |
| ch09.md | 82 | p. 48 | 48 | ok | Table (Bhatnagar [82]): growth 28%-63% a year, 1990-91 to 1997-98 |
| ch09.md | 83 | p. 43 | 43 | ok | 'This along with fortuitous circumstances of the need to fix the Y2K bug, the Euro conversion requirement, a...' |
| ch09.md | 84 | p. 46 | 46 | ok | 'This was a godsend opportunity to many fledgling software services companies in India.' |
| ch09.md | 86 | p. 47 | 47 | ok | 'Besides the Y2K problem, the European Union announced in 1995 that the Euro will be used as the common curr...' |
| ch09.md | 87 | pp. 46-47 | 46-47 | ok | p46: 'The "brain drain" of the 60s and the 70s became "opportunity gain" in the 90s when India liberalized its ec...'; p47: 'to many fledgling Indian software companies to get small contracts at the beginning which grew as the compa...' |
| ch09.md | 88 | p. 47 | 47 | ok | 'IBM which wanted to re-enter India partnered with the Tata group and started TATA-IBM in 1992 with 50% stake.' |
| ch09.md | 89 | pp. 47-48 | 47-48 | ok | p47: 'For example, American Express established a centre in Mumbai in 1994 to carry out back-office functions suc...'; p48: 'In 1994 Oracle set up a software development centre in Bangalore and in 1997 GE Capital International Servi...' |
| ch09.md | 94 | p. 47 | 47 | ok | 'The export earning of software services companies were significant and the voice of NASSCOM was strong and ...' |
| ch09.md | 95 | p. 48 | 48 | ok | Table (Bhatnagar [82]): 1990-91 128 ... 1997-98 1759, growth column |
| ch10.md | 30 | p. 36 | 36 | ok | 'The DoE negotiated with the Department of Telecommunication (DoT) in 1985 to allow Texas Instruments (TI) t...' |
| ch10.md | 37 | p. 48 | 48 | ok | 'In 1997 they announced a DSP chip code named Ankur (a Sanskrit word meaning Seedling) [64] which was entire...' |
| ch10.md | 39 | p. 48 | 48 | ok | 'In 1994 Oracle set up a software development centre in Bangalore' |
| ch10.md | 89 | p. 55 | 55 | ok | 'Vinay Deshpande and Shashank Garg of Encore Software Ltd. along with me, when I was a Director of the compa...' |
| ch11.md | 19 | p. 45 | 45 | ok | 'An ISO 9001 [83] certificate was awarded only after auditors inspected the processes used by a software com...' |
| ch11.md | 20 | pp. 45-46 | 45-46 | ok | p45: 'In addition to ISO 9001 certification many companies obtained the certificate issued by the Software Engine...'; p46: 'certification is essential for bidding for software projects in Europe whereas the CMM maturity level is va...' |
| ch11.md | 22 | p. 45 | 45 | ok | 'The Motorola (India) software team was the first team in the world to attain this maturity level in 1993.' |
| ch11.md | 25 | p. 52 | 52 | ok | 'In 1999, 6 out of 12 CMM level 5 certified companies in the world were in India.' |
| ch11.md | 28 | p. 46 | 46 | ok | 'The process orientation allowed companies which were recruiting large numbers of employees each year to qui...' |
| ch11.md | 40 | p. 46 | 46 | ok | 'There were not enough software engineers in the USA and Europe to fix the bug and it had to be outsourced.' |
| ch11.md | 43 | p. 46 | 46 | ok | '23% of the revenue of INFOSYS ... in 1997 was for fixing the Y2K bug [4, p.349]' |
| ch11.md | 50 | p. 47 | 47 | ok | 'Besides the Y2K problem, the European Union announced in 1995 that the Euro will be used as the common curr...' |
| ch11.md | 55 | p. 48 | 48 | ok | 'Software Services Export Revenue Value in Year million US Growth Dollars Percent 1990-1991 128 28 1991-1992...' |
| ch11.md | 56 | p. 46 | 46 | ok | 'Many of them earned the goodwill of clients by not only fixing the Y2K bug but also improving the software ...' |
| ch11.md | 57 | p. 46 | 46 | ok | 'In fact the Y2K problem which was considered a big threat in the mid 90s did not become one partly due to a...' |
| ch11.md | 80 | p. 50 | 50 | ok | 'The government realized that they were irrelevant to the IT industry. • Enabling state controlled banks to ...' |
| ch11.md | 101 | p. 45 | 45 | ok | 'coding and testing that took 70 to 80% of the time was done in India' |
| ch11.md | 104 | p. 51 | 51 | ok | 'Private corporate bodies were allowed to set up Universities in 2002 with relevant acts [93].' |
| ch12.md | 6 | p. 56 | 56 | ok | 'During the period 1998 to 2010 there was a rapid growth of private engineering colleges and colleges offeri...' |
| ch12.md | 7 | p. 51 | 51 | ok | 'Private corporate bodies were allowed to set up Universities in 2002 with relevant acts [93].' |
| ch12.md | 8 | p. 56 | 56 | ok | 'The number of MCAs graduating in 1998 was around 7000 whereas it jumped to 120,000 by 2010 [108].' |
| ch12.md | 9 | p. 12 | 12 | ok | 'Whereas the graduates of the IITs and the NITs (around 10,000) are excellent, industry employers opine that...' |
| ch12.md | 10 | p. 51 | 51 | ok | 'The University Grants Commission which controls Universities also set up a National Assessment and Accredit...' |
| ch12.md | 15 | p. 56 | 56 | ok | 'The IT companies' common complaint was that there were not enough employable graduates' |
| ch12.md | 16 | p. 56 | 56 | ok | 'All major IT companies had in- house training programmes ranging from 12 weeks to 6 months.' |
| ch12.md | 23 | p. 56 | 56 | ok | 'With many of these companies having a work force of the order of 120,000 the replacement numbers themselves...' |
| ch12.md | 99 | p. 56 | 56 | ok | 'In 1998 the number of engineering students was around 135,000 and in 2010 it grew to 1,300,000, a growth of...' |
| ch12.md | 100 | p. 12 | 12 | ok | 'Currently India graduates around 1.3 million engineers per year with 32% in Computer Engineering and IT fro...' |
| ch14.md | 37 | p. 53 | 53 | ok | 'American Express was the first organization to start BPO work in India in 1994 followed by GE Capital Inter...' |
| ch14.md | 40 | p. 53 | 53 | ok | 'The only requirement was trainable human resources with good knowledge of English (which was available in r...' |
| ch14.md | 65 | p. 80 | 80 | ok | 2010 entry: 'Direct employment 2.4 million in IT' |
| ch14.md | 66 | p. 52 | 52 | ok | 'CMM level 5 certification has been obtained by 166 IT companies in India' |
| ch14.md | 67 | p. 49 | 49 | ok | 'These companies had over 400 delivery centres outside India with presence in 52 countries.' |
| ch14.md | 110 | p. 79 | 79 | ok | '2005 • Oracle acquires IFlex an Indian Banking software product company. • Special Economic Zone (SEZ) Act ...' |
| ch14.md | 111 | pp. 49, 53 | 49, 53 | ok | p49: 'Two hundred and fifty seven software/service companies were set up in SEZ by 2007'; p53: BPO centres in SEZs 'as the profit earned ... was tax exempt' |
| ch14.md | 121 | pp. 53-54 | 53-54 | ok | p53: 'Texas Instruments which had started work in India in 1985 developing software tools discovered that the qua...'; p54: 'Other microelectronics design and R and D centres were also set up in India during this period by companies...' |

## Summary

| file | notes | ok | fix | not-found |
|---|---|---|---|---|
| ch01.md | 38 | 38 | 0 | 0 |
| ch02.md | 17 | 17 | 0 | 0 |
| ch03.md | 62 | 62 | 0 | 0 |
| ch04.md | 25 | 25 | 0 | 0 |
| ch05.md | 63 | 63 | 0 | 0 |
| ch06.md | 12 | 12 | 0 | 0 |
| ch07.md | 19 | 19 | 0 | 0 |
| ch08.md | 65 | 65 | 0 | 0 |
| ch09.md | 25 | 25 | 0 | 0 |
| ch10.md | 4 | 4 | 0 | 0 |
| ch11.md | 14 | 14 | 0 | 0 |
| ch12.md | 10 | 10 | 0 | 0 |
| ch14.md | 8 | 8 | 0 | 0 |
| prologue.md | 4 | 4 | 0 | 0 |
| **total** | 366 | 366 | 0 | 0 |

No S0001 endnotes in ch13, ch15, ch16, ch18, ch19, epilogue. ch17 mentions S0001 only in a drafting note (no page).
