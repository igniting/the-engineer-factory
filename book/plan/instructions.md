# Master instructions (as given by the author, 2026-10-11)

Saved verbatim in substance so every future session can re-read the brief. If this file and STATE.md disagree about *what to do next*, STATE.md wins; if they disagree about *rules*, this file wins.

## 1. Job
Research, write, fact-check and assemble a complete narrative nonfiction book end to end, with no human interviews and no human drafting. The author only starts sessions and says "continue". Work in small steps across many sessions; keep all progress in files. At the start of every session read `book/STATE.md` and do the next task. Never start over unless told "restart".

## 2. The book
- Working title: "The Engineer Factory: How India Built Software Engineering, and What AI Does to It" (better titles may be proposed in Phase 1).
- Subject: how India built software engineering as a field of study and a profession, from the first computers at ISI and TIFR in the 1950s to AI coding agents in 2025-26, and what may come next. India is the main story; other countries only as short comparative sidebars where they shaped India's path or a contrast explains it.
- Every chapter covers both halves: **education** (who was taught what, where, by whom, at what quality) and **profession** (what the work was, who did it, how it paid, how it changed lives and cities).
- Central questions:
  1. Why did India become a software services exporter rather than a hardware, product or domestic-software nation?
  2. How did the education system and the industry shape each other?
  3. Who became a software engineer in each era (caste, class, gender, region, language, family background), and what did the job do to their lives, families and cities?
  4. What role did the state play: obstacle, customer, enabler, builder of digital public infrastructure?
  5. What did migration to the US and the diaspora do to the industry at home, and the reverse?
  6. What did the business model (billing by the hour, the pyramid, utilisation, the bench) do to the craft, careers and pay?
  7. Is AI ending the model India built, and what could replace it?
- Working thesis (test it; look as hard for evidence against as for): India's software profession was shaped less by technology than by three constraints: scarce foreign exchange, a surplus of English-educated engineers, and a US labour market hungry for them. The result priced engineering by the hour and grew by adding people. AI attacks exactly that model.
- Audience: technically literate general readers, engineers, students, policymakers in India and abroad.
- Length: 110,000-130,000 words; ~18 chapters of 6,000-7,500 words, plus prologue, epilogue, notes, bibliography, timeline, data appendix.
- Author note [optional, to be confirmed by author]: published under "[YOUR NAME]"; "[I studied computer science at IIT Kanpur and lead an AI engineering organisation in Bangalore.]" Use only in the preface and AI disclosure note. **Placeholder not yet filled in by author.**

## 3. Files and state
See `book/STATE.md` for the file map.

## 4. Workflow
One task per step, then update STATE.md. When context is nearly full, finish the current task, update STATE.md, stop with: "Ready. Say continue."

- Phase 0 - Setup: folder, STATE.md, style.md, empty source register.
- Phase 1 - Map the ground: (a) bibliography >=150 sources, primary first, annotated; (b) chronology >=300 dated events 1930s-2026; (c) people index, myths list, dataset plan; (d) revise outline if evidence suggests; record why.
- Phase 2 - Research dossiers, one per chapter, each with: 1 summary (300 words); 2 timeline table (date, event, significance, source ID); 3 evidence notes 3,000-6,000 words, every claim tagged; 4 people; 5 numbers table (measure, value, unit, year, definition, source ID, confidence); 6 disputes; 7 documented scenes (6-12; who, where, when, what; source IDs); 8 documented voices (quotes <50 words, exact source and page/timestamp); 9 comparative sidebar material; 10 gaps.
- Phase 3 - Data: build CSV series. Reconcile series with different definitions; never splice silently.
- Phase 4 - Drafting from dossier only. Missing fact -> back to Phase 2 for that chapter first. Every factual sentence traceable; numbered endnotes keyed to source IDs.
- Phase 5 - Independent verification per chapter as a separate task (use a sub-agent that has not seen the drafting if possible). Re-open source for every number, date, name, quotation, causal claim. Log in `verify/chNN-factcheck.md`: claim, source ID, verdict (confirmed/corrected/removed/softened), note. Quotations exact or removed/paraphrased. Key claims need two independent sources or are marked as resting on one. Chapter cannot advance with unresolved items.
- Phase 6 - Revision: whole-book read; fix repetition, contradictions, pacing, transitions, arc; each part answers the central questions; re-verify changes.
- Phase 7 - Assembly: title page, AI disclosure note, preface, contents, prologue, chapters, epilogue, timeline appendix, data appendix, endnotes, bibliography, index term list. One Markdown manuscript; .docx and .epub if tools allow.

## 5. Starting outline
See `book/plan/outline.md` (v0 = the author's starting outline).

## 6. Sources and data
Replace interviews with documented first-hand material: memoirs and company histories; oral histories (Computer History Museum, IEEE History Center, university projects); published interviews, speeches, podcast/video transcripts, investor-call transcripts; parliamentary debates; government reports (DoE, MeitY, Planning Commission, Electronics Commission), STPI and SEZ data, RBI software-export surveys; company annual reports and SEC filings (Infosys, Wipro 20-F from 1999-2000); contemporaneous press (Dataquest from 1982, Express Computer, Business India, India Today, EPW, ET, The Hindu, TOI, US press); court judgments (Unni Krishnan 1993, TMA Pai 2002); US records (USCIS H-1B, DOL LCA, Congressional hearings); academic work (IEEE Annals, ethnographies, economics of offshoring and diaspora).

Starting books to locate and verify (check titles, years, contents): Dinesh C. Sharma, The Long Revolution; The Outsourcer; Ross Bassett, The Technological Indian; Arora & Gambardella (eds), From Underdogs to Tigers; AnnaLee Saxenian, The New Argonauts; Upadhya & Vasavi (eds), In an Outpost of the Global Economy; Carol Upadhya, Reengineering India; A. Aneesh, Virtual Migration; Xiang Biao, Global "Body Shopping"; Devesh Kapur, Diaspora, Development, and Democracy; Kiran Karnik, The Coalition of Competitors; S. Ramadorai, The TCS Story... and Beyond; Steve Hamm, Bangalore Tiger; Nandan Nilekani, Imagining India; Nilekani & Viral Shah, Rebooting India.

Datasets (1970s-2026 where possible): software/services exports (nominal, real); industry workforce (changing definitions); headcount and revenue per employee for top five firms; fresher hiring and pay (nominal, real); engineering seats, enrolment, vacancies by branch and state, CS share; graduate employability and unemployment; H-1B approvals, F-1 students and OPT for Indians; GCC count and staff; startup funding; women's share; attrition.

## 7. Myths to test
See `book/research/myths.md`.

## 8. Style guide
See `book/plan/style.md`.

## 9. Honesty rules (non-negotiable)
- The book is AI-generated. Never imply interviews were conducted. Attribute every first-hand account to its published source.
- Never invent people, quotations, dialogue, thoughts, scenes, numbers or sources. No composites. Unknown -> leave out or say unknown.
- Quotations exact, short (<50 words), cited with page/timestamp; never reproduce long passages from copyrighted works. Paraphrase and cite.
- Distinguish what a company or body says about itself from independent evidence; label press releases, recruiters, vendors, advocacy groups.
- Mark anything not verified. Mark anything after the knowledge cutoff as checked through live sources, or remove it.
- Write the AI disclosure note for front matter: researched and written by AI under [YOUR NAME]'s direction, using published sources in the bibliography; no interviews; errors may remain; how to report corrections.

## 10. Quality gates
- Dossier done: every claim has a source ID; Gaps section honest.
- Draft done: meets word target, uses only dossier material, every factual sentence has a note.
- Chapter final: fact-check log has no open items; full read-through finds no contradiction with other chapters.
- Book done: all chapters final, appendices and bibliography complete, STATE.md says "Complete".

## 11. Reporting
After each task, update STATE.md and report in three lines: what was done, what is next, any problem. On "continue", read STATE.md and resume.
