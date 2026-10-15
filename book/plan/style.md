# Style guide

Source: author's master instructions, section 8, plus decisions logged below. Applies to every draft. The checker in Phase 5 also checks style.

## Core rules (from the brief)
1. **Shape.** Narrative nonfiction. Each chapter opens with a documented scene, moves between people, institutions and numbers, and ends on a turn that leads into the next chapter.
2. **Both halves.** Every chapter covers education (who was taught what, where, by whom, at what quality) and profession (the work, who did it, how it paid, what it did to lives and cities).
3. **Plain English.** Short and medium sentences, varied rhythm. Concrete detail over adjectives. Explain a technical term the first time it appears, in one clause.
4. **Numbers.** Always give unit, year and definition. Prefer one well-chosen number to five. When comparing rupee amounts, convert to US dollars at that year's rate and say which rate (see House decisions, D3).
5. **Fairness.** Present founders, officials, workers and critics on the evidence. Give the strongest version of competing interpretations.
6. **Banned words and habits.** No "delve", "tapestry", "testament", "landscape", "navigate", "in today's fast-paced world". No lists inside narrative chapters. No stacked rhetorical questions. No moralising summaries at the end of sections. No em-dash asides (use commas, parentheses sparingly, or a new sentence).
7. **Sidebars.** 400-900 words, clearly marked, titled by the question they answer (e.g. "Why did Ireland get the factories and India the programmers?").

## Honesty in prose (from section 9)
- Never imply interviews. Use attribution phrases tied to a published source: "in his memoir", "as she told an interviewer for the Computer History Museum in 2004", "in a 2003 investor call".
- No invented scenes, thoughts, dialogue or composite characters. Interior states only when the person recorded them ("he later wrote that he was terrified").
- Quotations under 50 words, exact, endnoted with page or timestamp.
- Self-description is labelled: "Infosys said in its annual report", "according to Nasscom, the industry's lobby group".
- Post-cutoff or live-checked material is flagged in the endnote ("checked against [source] on [date]").

## House decisions (added by the agent; record new ones with date and reason)
- **D1 (2026-10-11) Spelling.** British/Indian English spelling (programme, labour, liberalisation, centre), matching the brief and the Indian audience. Exception: proper names and US titles keep their own spelling (e.g. "Kanpur Indo-American Program" if that is the documented form; check).
- **D2 (2026-10-11) Indian numbers.** Use international units in running text (million, billion). Give lakh/crore only inside a quotation or where the original figure is in crore, then convert: "Rs 500 crore (Rs 5 billion, about $X million at the 1995 rate)".
- **D3 (2026-10-11) Exchange rates.** Use annual-average INR/USD rates from a single series (target: RBI Handbook of Statistics on the Indian Economy, annual average; source ID to be assigned) stored in `research/data/inr_usd.csv`. Fiscal-year figures (April-March) use the fiscal-year average. State "at the year's average rate" in the endnote, not in the text.
- **D4 (2026-10-11) Real values.** Deflate rupee series with CPI-IW (long series) unless the dossier argues otherwise; deflate dollar series with US CPI-U. State base year in every table.
- **D5 (2026-10-11) Fiscal years.** Write Indian fiscal years as "FY1999-2000" or "the year to March 2000" on first use in a chapter; never bare "FY00".
- **D6 (2026-10-11) Names.** First mention: full name and role; thereafter surname. Companies: full name on first mention per chapter ("Tata Consultancy Services (TCS)"), then the common short form. Cities: use the name in use at the time, with the current name on first mention ("Bangalore (Bengaluru since 2014)"); default to "Bangalore" in pre-2014 narrative.
- **D7 (2026-10-11) Endnotes.** Numbered per chapter. Format: `[n] S0123, p. 45.` in drafts; expanded to full short-citation form at assembly. One note may cite several sources. Every factual sentence carries a note, or shares one with adjacent sentences drawn from the same source (the note says so).
- **D8 (2026-10-11) Caste, class, gender.** Describe groups using the terms of the cited study, with the study's definitions; never generalise from a single anecdote. Name individuals' caste or community only where the person or a published biography states it and it matters to the argument.
- **D9 (2026-10-11) Dashes.** En dashes for ranges (1985–1991) are allowed in final assembly; in working files use a hyphen. No em dashes anywhere in prose.
- **D10 (2026-10-11) Confidence language.** Use "documented", "reported", "claimed", "estimated" deliberately: documented = primary record; reported = contemporaneous press; claimed = party with an interest; estimated = modelled number.

- **D11 (2026-10-14) AI disclosure.** The book's AI-assisted drafting and the conflict of interest (Anthropic products such as Claude Code and Claude Cowork appear in sources and text) are disclosed in a front-matter note at assembly, and in one plain sentence at the first mention of Claude Code in Chapter 19 (revised 2026-10-15 after the publisher's critique; the epilogue no longer repeats it). Chapters describe the products neutrally, as the sources do.

- **D12 (2026-10-14) Renaming years.** First-mention parentheticals give the renaming year only where sourced: Mumbai 1995 (S0341), Chennai 1996 (S0342), Kolkata 2001 (S0343), Bengaluru and Mysuru 2014 (S0344), Odisha 2011 (S0345). Gurgaon/Gurugram and Poona/Pune use '(now X)' without a year. Period names are used in period narrative (e.g. Bombay and Madras for 1998 data).

## Banned-word check (run before marking a draft done)
`grep -niE "delve|tapestry|testament|landscape|navigat|fast-paced|—" book/drafts/chNN.md` must return nothing (except "landscape" inside a quotation or proper name, which the checker notes).

- **D13 (2026-10-15) Research log stays in the notes.** After the publisher's critique: the body states what is known and flags real uncertainty in a clause; gaps in the record ('no copy has been located'), source-version adjudication and dating disputes go in the notes. No 'not yet', no 'for this book' in the body. Main secondary sources are named once per chapter; quotations, contested claims, self-descriptions and allegations stay attributed in the body.
