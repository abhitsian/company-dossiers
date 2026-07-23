# Uber Freight — Product Dossier
> Uber's digital freight brokerage, managed-transportation, and logistics-software arm: it matches shippers with a 95k-carrier network, and now also sells the TMS software (the tool that runs a shipper's transportation) and an AI layer (Insights AI) built on top of that freight flow. Arc: from a spot-load matching app to a full logistics operating system that tries to earn more than a low-margin brokerage can.
> **UBER (parent)** · Uber mkt cap ~$151.5B · FWD P/E 24.56 · Freight is a sub-segment (no standalone ticker) · Updated **2026-07-04** · Sources: **9** (see §15)
> **v1 — earnings-grounded + web research**
> One living file. Arc: **Facts → Insights → Differentiators → Plays.** Skim the bold headlines for the gist; drill for detail.
> *How to use: feed sources over time. Each new source is MERGED (dedupe, sharpen, `[S#]`-tag, correct), not appended. Every fact is source-grounded; estimates are labeled `[est]`.*

---

## 1. Wow Vault ★
*The selective, non-obvious layer. Bar: would a sharp interviewer NOT already know it?*

**★ Freight is Uber's worst-margin business, and management keeps it because it fills demand troughs, not because the brokerage makes money.**
- **Mechanism:** Rideshare demand drops ~45% from Saturday to Monday; an AV sitting idle in that trough earns nothing. Delivery and Freight give the same vehicle a baseline of work during the trough, so utilization stays high and daily revenue-per-vehicle is steadier than any pure-mobility rival can offer. [S2]
- **Why non-obvious:** Most people read Freight as a struggling, roughly-breakeven-to-negative brokerage (lost ~$43M adj. EBITDA through Q3 2025 [S5]). Its real value is smoothing demand for the future AV fleet, not making money on its own.
- **Deploy:** "Should Uber keep Freight?" — recall hook: *"Freight isn't a brokerage bet, it's the Sunday-night shift for a robot truck."*
- **Source:** [S2][S5]

**★ Uber Freight built its own logistics LLM and is trying to switch from selling capacity (take-rate) to selling intelligence (software).**
- **Mechanism:** Insights AI is a logistics-specific LLM built into the TMS; 30+ AI agents handle scheduling, read arrival/departure times out of emails, and fix LTL data. Accuracy went from 60–70% to ~98% before they scaled it. ~$1.6B of freight has already run through the AI setup across 5 design-partner brands (incl. Colgate-Palmolive). [S3][S4][S8]
- **Why non-obvious:** The pitch turns a commodity brokerage into a data business — "query your network instead of waiting two weeks for a PowerPoint." Software margins are far higher than moving-a-truck margins.
- **Deploy:** metrics / strategy — recall hook: *"They're monetizing the exhaust of the freight, not just the freight."*
- **Source:** [S3][S4]

**★ "Returned to growth for the first time in nearly 2 years" is the whole Freight headline, and it's a demand-recovery story, not a share-win story.**
- **Mechanism:** Freight shrank for ~2 years through the freight-market downturn (falling rates, too much capacity after the 2021 boom). Q1 2026 is the first up-quarter. [S1]
- **Why non-obvious:** Interviewers will assume product wins caused it. Most of it is the freight cycle turning, not Uber Freight out-executing C.H. Robinson.
- **Deploy:** "Is Freight working?" — recall hook: *"The tide came back in; don't confuse it with the boat getting faster."*
- **Source:** [S1]

**★ Uber Freight is really three businesses stapled together, with three different margin profiles.**
- **Mechanism:** (1) Brokerage/spot — a thin take-rate for matching full-truckload (FTL) loads; (2) Managed Transportation + TMS — from the $2.25B Transplace acquisition (2021), a stickier, SaaS-like software/back-office (BPO) business on ~$20B of Freight-under-Management; (3) AI/Insights — an early software upsell. [S3][S7]
- **Why non-obvious:** "Uber Freight = Uber for trucks" misses that the Transplace deal made it mainly a *managed-transportation + software* company, not a spot marketplace.
- **Deploy:** "Explain the business" — recall hook: *"Spot is the front door; the money question is the software floor above it."*
- **Source:** [S7][S3]

**★ Convoy, the venture-funded twin that bet on a pure marketplace, died; Uber Freight survived because it's attached to a $150B parent.**
- **Mechanism:** Convoy shut down in 2023; DAT bought its platform in July 2025. Uber Freight lived through the same brutal down-cycle because Uber's balance sheet and cash flow from other products carried it. [S6]
- **Why non-obvious:** The clean-marketplace bet on freight failed. Surviving needed either assets (J.B. Hunt), scale relationships (C.H. Robinson), or a rich parent (Uber).
- **Deploy:** competitive strategy — recall hook: *"Freight tech didn't reward the purest marketplace — it rewarded the deepest pockets."*
- **Source:** [S6]

**★ The AI-agent play is the same "10% of code is agent-written" bet, applied to logistics ops.**
- **Mechanism:** The parent says agents now commit ~10% of its code, offsetting headcount growth [S1]. Uber Freight uses the same logic for freight ops — agents do the scheduling and data-cleanup grunt work so human ops handle the exceptions. [S4][S8]
- **Why non-obvious:** It links the Freight AI story to the parent's cost thesis: AI turns a labor-heavy brokerage-ops business into a leaner one.
- **Deploy:** "How does AI change unit economics here?" — recall hook: *"The moat isn't the LLM, it's firing the 3am dispatcher email."*
- **Source:** [S1][S4]

**★ The AI trains on proprietary freight flow that rivals can't cheaply copy.**
- **Mechanism:** ~$20B FUM plus years of load/rate/lane data is the training material for the domain LLM. A generic GPT wrapper doesn't have Colgate's lane-level exception history. [S3][S4]
- **Why non-obvious:** It's the one place Freight has a real data moat — the brokerage's low margin is the *cost of acquiring* the data the AI sells.
- **Deploy:** AI moat question — recall hook: *"The thin-margin freight is the data-acquisition cost for the fat-margin AI."*
- **Source:** [S3][S4]

---

## 2. Reframes & mental models to borrow
- **"Ask your network vs. wait two weeks for the PowerPoint."** Insights AI turns analytics from a lagging report into a system you can query. → any "AI in enterprise workflow" prompt. [S3]
- **"Fill the trough."** A low-margin business is worth the load it puts on a shared asset while the high-margin business is idle. → portfolio / synergy / "why keep the loss-making segment" prompts. [S2]
- **"System of record → command center."** The TMS is moving from tracking the network to running it (proactive recommendations, not dashboards). → product-vision prompts for any workflow tool. [S4]
- **"Barbell, applied to shippers."** The parent runs low-end (frequency) and high-end (profit) at once [S1][S2]; Freight's version is SMB self-serve spot at one end, enterprise managed-transportation at the other. → segmentation / pricing prompts.
- **"Data-first, technology-first challenge."** The founder's view that supply chain is really an information problem, not a trucks problem. → "reframe this industry" prompts. [S3]
- **"Agents on the basics, humans on the exceptions."** 30+ agents do the repetitive ops; people handle exceptions, cost control, and network optimization. → "how should AI split work with humans" prompts. [S4]

---

## 3. Numbers that signal depth

**Headline scale & product**
| Metric | Value | Source |
|---|---|---|
| Freight under management (FUM) | ~$20B annually | [S3] |
| Shippers served | ~10,000 (incl. many Fortune 500) | [S3] |
| FTL carrier network | ~95,000 carriers | [S9] |
| LTL carriers | 150+ | [S9] |
| Freight moved through AI infra (to date) | ~$1.6B across 5 design-partner brands | [S4] |
| AI agents live | 30+ | [S4] |
| Insights AI accuracy | ~98% (up from initial 60–70%) | [S3] |
| Instant-quote validity window | 15 minutes | [S9] |
| Dispute-resolution time cut (TMS Financials bulk tools) | up to 20% | [S4] |

**Market arcs**
- Q1 2026: Freight "returned to growth for the first time in nearly 2 years." [S1]
- 2021 peak: ~$2.1B revenue — then the largest trucking digital marketplace by revenue. [S5]
- 2025: reported >$1.2B Freight GMV; pushing higher-margin services to lift take-rate and CLTV. [S5]

**Audited financials (segment)**
- Freight adj. EBITDA: about **−$43M** through Q3 2025 — the weakest segment in Uber's portfolio. [S5]
- Parent context (FY25): Uber revenue $14.37B Q4 (+20% Y/Y), FY adj. EBITDA $8.7B (+35%), FCF ~$9.8B (+42%). [S2] Q1 2026 revenue $13.20B (+14.5%). [S1]
- Transplace acquisition (Nov 2021): **$2.25B** (up to $750M stock + rest cash); financed partly by $550M from ADG / D1 Capital / GCM Grosvenor. [S7]

**Unit economics (cross-ref /follow-the-dollar) — all `[est]`**
- Brokerage net-revenue (take) margins across the industry run in the mid-teens % of gross revenue; net EBITDA margins are low-single-digit even for healthy brokers `[est]`. Uber Freight being negative at the adj-EBITDA line [S5] means its cost to serve (ops labor + tech spend) is more than its net take — the AI-automation thesis attacks that gap directly. [S4]
- Managed-transportation/TMS revenue is more software/BPO-like, so its margins are structurally higher than spot brokerage `[est]`; shifting the mix toward it is the margin lever.

---

## 4. Business anatomy — Acquire / Engage / Retain / Monetize

- **Acquire**
  - *Shippers:* SMB through self-serve web/app (post a load, get an instant 15-min quote [S9]); enterprise through managed-transportation sales (the inherited Transplace relationships + Fortune 500 book [S3][S7]); AI is now a top-of-funnel wedge via the Design Partner Program (5 brands, incl. Colgate-Palmolive) [S4].
  - *Carriers:* app-based self-onboard; ~95k FTL carriers browse upfront-priced loads and book instantly [S9]. CAC lever = the **Carrier Card** same-day payout (vs. the industry's 30–90 days) for carriers spending ~$3,500/mo [S9].
  - Cross-sell off the parent brand's trust; no real mobility→freight consumer overlap (different buyer).

- **Engage**
  - *Core loop (shipper):* post/tender load → get instant price → track in real time → reconcile payment in the TMS.
  - *Core loop (carrier):* browse upfront-priced loads → book → haul → get paid same day. **Powerloop** (drop-trailer/dedicated tours) keeps carriers moving with pre-loaded trailers and fixed weekly or %-based rates [S1-blog/S9].
  - *Aha (shipper):* the instant transparent quote (no haggling); then Insights AI answering a network question in seconds instead of a 2-week analyst cycle [S3].
  - *Aha (carrier):* getting paid today.
  - Surfaces: shipper web dashboard + app; carrier app; the **TMS portal** (now the command center, with AR/AP financials) [S4]; **Uber Freight Exchange** (Spot + procurement scenario analysis) [S4].

- **Retain**
  - Managed transportation + TMS = high switching cost (workflows built in, integrations, historical data). This is the sticky layer; spot brokerage is inherently promiscuous (carriers and shippers use several load boards at once).
  - Insights AI deepens the lock-in: the more freight runs through it, the better its network-specific recommendations.
  - Boring plumbing that retains: order-to-cash inside the TMS (2025 TMS Financials) removes a reason to use a separate system [S4].
  - Churn driver: in a down-cycle, spot shippers chase the cheapest capacity; retention is weak where the only value is price.

- **Monetize**
  - *Brokerage take-rate:* the margin between shipper price and carrier pay (spot + contract FTL/LTL).
  - *Managed transportation:* fees on ~$20B FUM (software + BPO). [S3][S7]
  - *TMS software:* SaaS-style licensing of the platform.
  - *Insights AI / data:* an early upsell — the intended margin-mix shift. [S3][S4]
  - *Carrier financial products:* Carrier Card spend/interchange economics `[est]`. [S9]
  - Price fences: self-serve spot (low) vs. enterprise managed (high) — the shipper-side barbell.

---

## 5. Moats & Weaknesses

**Moats**
| Moat | Evidence | Deepening / eroding |
|---|---|---|
| Proprietary freight-flow data → domain LLM | ~$20B FUM, years of lane/rate/exception data feeding Insights AI [S3][S4] | **Deepening** — compounds with volume; the hardest thing for a rival to copy |
| Parent balance sheet + multi-product cash flows | Survived the down-cycle that killed Convoy [S6]; Uber ~$9.8B FCF [S2] | **Stable** — patient capital most freight-tech pure-plays lack |
| Managed-transportation switching costs | Transplace enterprise book, TMS integrations [S7] | **Deepening** as the TMS adds financials/command-center depth [S4] |
| Trough-utilization role in future AV network | Freight fills the Sat→Mon demand trough [S2] | **Deepening** — but only pays off if/when Uber's AV fleet scales |
| Scale of carrier network | ~95k FTL carriers, same-day-pay hook [S9] | **Eroding-ish** — carriers multi-home; network size ≠ loyalty |

**Weaknesses**
| Weakness | Why it bites | Where a rival attacks |
|---|---|---|
| Structurally unprofitable segment | ~−$43M adj. EBITDA thru Q3'25 [S5] | C.H. Robinson raised its 2026 OI target to $965M–$1.04B [S5] — scale + relationships out-earn it |
| Commoditized core (spot brokerage) | Matching FTL loads is a race to the thinnest take | DAT/Convoy neutral marketplace [S6]; traditional load boards; anyone with capacity |
| Cyclicality | The whole segment shrank ~2 yrs on the freight down-cycle [S1] | Asset-backed players (J.B. Hunt 360) ride cycles with fleet security |
| No consumer cross-sell | The freight buyer isn't the rideshare/Eats consumer | Can't reuse the 202M-MAPC funnel that powers Mobility/Delivery [S2] |
| AI is early / unproven at margin | Only ~$1.6B run through it, 5 pilot brands [S4] | Flexport shipped competing AI tools Feb 2025 [S3]; incumbents copy fast |
| Not core to the parent narrative | Barely mentioned on earnings calls [S1][S2] | Under-invested vs. Mobility/Delivery/AV; disposal/spin risk |

---

## 6. AI impact — deflationary or moat?

| AI vector | Deflationary / commoditizing | Moat-deepening / compounding |
|---|---|---|
| Generic LLMs for shipper Q&A | Any broker can bolt a GPT wrapper onto a dashboard | — |
| **Domain LLM trained on proprietary freight flow** | — | Insights AI on ~$20B FUM data rivals can't match [S3][S4] |
| **AI agents automating ops** (scheduling, email parsing, LTL data-fix) | Table-stakes soon; competitors will automate too | Near-term margin relief on a negative-EBITDA segment; compounds with the parent's agent tooling [S1][S4] |
| Automated pricing/matching | Commoditizes the spot-brokerage take-rate further | — |
| AI-driven procurement (Exchange scenario analysis) | Modeling tools get cheap and universal | Sticky if fused into the managed-transportation workflow [S4] |

**Net read:** A **tailwind for the software/managed layer, a headwind for the spot-brokerage layer.** AI speeds up the commoditization of pure load-matching (bad for take-rate) while giving Uber Freight its one defensible asset — a domain LLM on proprietary flow — a reason to exist above the brokerage. The single real AI risk: if the domain-LLM edge turns out to be shallow (generic models + a customer's own data close 90% of the gap cheaply), Freight is left holding only the loss-making brokerage. [S3][S4][S5]

---

## 7. Needs-based segments → problems → solutions
*Shreyas method: segment on the JOB, not company size/vertical. The domain's real needs axes: (a) how much certainty of capacity/price the shipper needs, (b) how much of the transportation function they want to own vs. outsource, and (c) for carriers, cash-flow timing vs. load-certainty. 5-Point Test applied per segment.*

**Segmentation basis:** the *transportation job-to-be-done* — cover a load now vs. run a network vs. keep a truck earning vs. get paid now. These cut across SMB/enterprise and are product-specific, targetable, and winnable.

**A. "Cover this load right now" (spot shipper)** — Job: functional — get one load moved this week at a fair, known price without phone-tag. Social: look competent to the plant manager. Friction: opaque broker quotes, haggling, no instant certainty. Nudge: extrinsic — the 15-min locked instant quote [S9]. Aha: *"I posted a load and had a firm price before I finished my coffee."* Today → gap: strong on instant quote, weak on why they'd come back when a cheaper board exists → **Play #1 (retention wedge), #6 (SMB Carrier-Card-style loyalty).**

**B. "Run my whole network for me" (enterprise managed-transportation shipper)** — Job: functional — outsource the transportation function end-to-end and lower landed cost; personal — the VP of Supply Chain wants fewer fires and a defensible number for the CFO. Friction: fragmented systems, 2-week analyst cycles, no proactive optimization. Nudge: intrinsic — control and confidence over the network. Aha: *"I asked which origin is underperforming and got the answer, not a ticket."* [S3] Today → gap: the crown jewel (Transplace book + TMS), but AI-proactivity is still early → **Play #2 (Insights AI as the retention/expansion engine).**

**C. "Procure my annual contract freight smarter" (procurement-led shipper)** — Job: functional — award a bid across carriers optimizing cost vs. service, fast. Emotional: fear of locking in a bad rate for a year. Friction: weeks of manual modeling in spreadsheets. Nudge: extrinsic — instant side-by-side scenario comparison in Uber Freight Exchange [S4]. Aha: *"I compared five award strategies in clicks, not weeks."* Today → gap: real feature, low awareness → **Play #4 (procurement as a land-and-expand wedge into managed transportation).**

**D. "Keep my truck earning, and pay me now" (carrier / owner-operator)** — Job: functional — cut empty miles and get cash today; personal — a small-fleet owner living on thin working capital. Friction: 30–90 day broker payment terms, deadhead between loads. Nudge: extrinsic — same-day Carrier Card payout [S9] + Powerloop drop-trailer tours that keep them moving [S9]. Aha: *"I dropped one trailer, grabbed the next, and got paid tonight."* Today → gap: strong hooks, but carriers multi-home and loyalty is thin → **Play #6 (deepen carrier financial products into a real reason to stay).**

**E. "Automate the ops desk" (logistics ops team inside a shipper)** — Job: functional — stop drowning in scheduling emails and LTL data errors; social — the team wants to do strategy, not data entry. Friction: repetitive manual work eats the day. Nudge: intrinsic — freedom to do higher-impact exception/cost work. Aha: *"The agent booked the dock appointment and fixed the LTL record while I slept."* [S4][S8] Today → gap: 30+ agents live but early → **Play #3 (agent marketplace / automation depth as the differentiator).**

---

## 8. Strategy *(Shreyas Strategy Template)*
- **One-sentence strategy:** Use Uber's balance sheet to survive the freight down-cycle as a brokerage, while turning proprietary freight flow into a higher-margin managed-transportation + AI-software business — and hold the segment as trough-utilization insurance for the parent's future AV fleet.
- **Prioritize:** enterprise managed-transportation retention/expansion + the Insights AI/agent layer (the margin story). **Don't over-serve:** the commoditized SMB spot-only shipper who comes back only for the lowest price.
- **Pillars (moat → segment):** (1) Proprietary-flow domain LLM → segments B/C/E; (2) Managed-transportation switching costs → segment B; (3) Carrier financial products → segment D; (4) Parent capital + AV trough-fill → whole-segment survival.
- **North star:** the share of a customer's Freight-under-Management run through Uber Freight *software/AI* (not just capacity brokered) — because that's the durable, high-margin, high-retention number. `[est., proposed]`
- **Non-priorities (trade-offs):** winning the pure race-to-the-bottom spot market on price; consumer cross-sell (no overlap); international breadth ahead of North-American depth.
- **Roadmap / metrics:**
  - **Now** — automate ops with agents to shrink the EBITDA loss. Leading: % of ops actions agent-handled; Lagging: segment adj. EBITDA (from −$43M toward breakeven) [S5].
  - **Next** — move managed-transportation accounts onto Insights AI. Leading: # design-partner→paying conversions; Lagging: software/AI revenue as % of Freight revenue.
  - **Later** — position the network as AV trough-fill. Leading: AV freight miles piloted; Lagging: AV revenue-per-vehicle-per-day smoothing [S2].

---

## 9. Contrarian bets & open tensions
- **Bet: A domain-specific logistics LLM is a durable moat.** *Bear:* frontier general models + a customer's own data will close the gap cheaply, and "domain LLM" becomes a wrapper. *Counter:* the training material is proprietary multi-shipper flow that no single customer or generic model has [S3][S4]. **Best skeptic angle** lives here.
- **Bet: Keep a structurally loss-making segment for optionality.** *Bear:* ~−$43M EBITDA [S5] is real cash going into a business barely mentioned on earnings calls [S1][S2]; spin it. *Counter:* the trough-utilization AV thesis makes it strategic insurance, and AI can flip the margins [S2][S4].
- **Bet: Managed transportation (Transplace) is the future, not spot.** *Bear:* $2.25B was a rich price [S7] for a slow-growth BPO, and integration is hard. *Counter:* it's the only sticky, higher-margin layer Freight has.
- **Valuation tension:** Freight is a rounding error in Uber's ~$151.5B cap and dilutes the "profitable-compounder" story; some investors would value Uber *higher* if Freight were spun or shut — but that forfeits the AV trough-fill option. [S1][S2]

---

## 10. Big Picture — Looks Wrong, Is Right

**A. Wise refusals**
- **Not spinning/shutting the loss-making Freight segment** → why the restraint is correct: it's cheap optionality on AV trough-utilization and a proprietary-data flywheel; killing it to flatter near-term EBITDA gives up both. [S2][S5]
- **Not chasing the pure spot-marketplace crown that Convoy died for** → correct: the clean-marketplace bet failed the cycle; leaning into managed transportation + software is the survivable position. [S6][S7]
- **Not forcing consumer cross-sell** (no "order a truck in the Uber app") → correct: the freight buyer is a supply-chain professional, not a rideshare consumer; the 202M-MAPC funnel doesn't transfer. [S2]

**B. Counterintuitive moves**
- **Running a negative-margin brokerage to feed a domain LLM** → the bigger play: the thin/negative brokerage margin is the *cost of acquiring* the freight-flow data that trains the high-margin AI. [S3][S4]
- **Building 30+ narrow ops agents instead of one flashy shipper chatbot** → the bigger play: the ROI is in automating the invisible 3am ops-desk labor (the real cost center), not in a demo-friendly chat UI. [S4][S8]
- **Barely marketing Freight on earnings calls while investing in its AI** → the bigger play: keep the parent narrative on Mobility/Delivery/AV, and let Freight quietly de-risk its margins before making it a story. [S1][S2]

---

## 11. Mistakes & Mis-executions → Opportunities
- **Overpaid/overextended into the 2021 freight peak** (built for a boom that reversed; the segment then shrank ~2 years) → *why:* rode cyclical 2021 rates as if they were structural, and scaled cost into a top. → *fix:* make the ops base variable-cost via agents so the next down-cycle doesn't produce another multi-year bleed. [S1][S5] `[judgment]`
- **Still negative adj. EBITDA years after the Transplace deal** → *why:* folding a BPO/managed-transportation business into a brokerage is slow — two cost structures, one still commoditized. → *fix:* speed up the mix-shift to TMS/AI revenue where the margins are; publish a segment path-to-breakeven. [S5][S7]
- **AI monetization is late and thin** (Insights AI quietly running since 2023, only ~$1.6B flow, 5 pilot brands, while Flexport shipped competing tools Feb 2025) → *why:* accuracy had to climb from 60–70% to ~98% before scaling — a real gate, but it gave up first-mover cover. → *fix:* convert design partners to paid fast; sell the agents as an add-on SKU. [S3][S4]
- **Weak spot-shopper retention** → *why:* the only value a price-shopping SMB gets is the instant quote, and nothing compounds. → *fix:* a carrier-card-style loyalty/financial hook for shippers, or bundle a lightweight TMS free to create switching cost. [S9] `[judgment]`
- **Under-told story to the market** → *why:* Freight is deprioritized in the parent narrative, with almost no segment disclosure on calls. → *fix:* if the AI-margin flip is real, give it a disclosed metric so the option value gets credit. [S1][S2] `[judgment]`

---

## 12. What's missing → Plays to run *(10× / 100× — hypotheses, not today)*

**Gaps:** (a) no compounding reason for spot shippers to come back; (b) the proprietary-flow data asset is under-monetized (only ~$1.6B run through AI vs. ~$20B FUM); (c) the carrier relationship is transactional despite the same-day-pay hook; (d) the agents save internal cost but aren't a sold product yet.

- **Play #1 — Free lightweight TMS for SMB spot shippers (switching-cost wedge).** Closes gap (a). *Right-to-win:* Uber already runs the platform at scale, so a stripped TMS costs little at the margin. **10×** on retention. Proof: give it to 500 spot shippers, measure repeat-book rate vs. control. `[est]`
- **Play #2 — Insights AI as the expansion engine on the managed book.** Closes gap (b). *Right-to-win:* the domain LLM only works on proprietary flow Uber Freight already holds [S3][S4]. **10×** on revenue/account via software attach. Proof: convert the 5 design partners to paid, publish net-revenue-retention lift.
- **Play #3 — Sell the agents (agent SKU / "AI ops desk as a service").** Closes gap (d). *Right-to-win:* 30+ battle-tested agents on real freight ops [S4][S8]; the parent's agent tooling depth [S1]. **10×** by turning a cost center into a revenue line. Proof: price one agent (dock-scheduling) as an add-on to 20 accounts.
- **Play #4 — Procurement-led land-and-expand.** Closes gap (b). *Right-to-win:* Uber Freight Exchange scenario analysis already exists [S4]; procurement is an annual, high-stakes wedge into managed transportation. **10×** on enterprise logo acquisition. Proof: win 10 annual bids via Exchange, track attach to managed services.
- **Play #5 — AV trough-fill pilots (100× optionality).** Closes the parent-synergy gap. *Right-to-win:* only Uber has both the AV network ambition and the freight baseload [S2]. **100×** if AVs scale — Freight becomes the utilization smoother that makes AV fleet economics work. Proof: one lane, one AV partner, measured revenue-per-vehicle-per-day smoothing.
- **Play #6 — Deepen carrier financial products (fuel, factoring, insurance) into loyalty.** Closes gap (c). *Right-to-win:* Carrier Card + same-day pay already sit in the carrier's cash-flow path [S9]. **10×** on carrier retention + a new fee line. Proof: add factoring to Carrier Card, measure load-booking share among enrolled carriers.

**Small compounding wins (a dozen 5%s = a double):** the 20% dispute-resolution cut in TMS Financials [S4]; Powerloop keeping carriers loaded (fewer empty miles) [S9]; 15-min quote conversion tuning [S9]; LTL data-error auto-correction cutting chargebacks [S8]; bundling AR/AP so shippers drop a second system [S4].

---

## 13. Interview arsenal
- **[Strategy]** "Should Uber keep or sell Uber Freight?" → keep: trough-utilization AV insurance + a proprietary-data flywheel; the −$43M is the cost of the option and AI can flip it. Sell-case: it dilutes the profitable-compounder story. → §1, §9, §10A.
- **[Product sense]** "Design the next product for a small carrier." → the JTBD is *cash now + no empty miles*; extend Carrier Card into factoring/loyalty (Play #6). → §7D, §12.
- **[Metrics]** "What's the north star for Uber Freight?" → the share of a customer's FUM run through Uber Freight *software/AI*, not capacity brokered — because it's the durable, high-margin, retentive number. → §8.
- **[Product design]** "Improve retention for spot shippers." → nothing compounds today; give them a free lightweight TMS to build switching cost (Play #1). → §7A, §11, §12.
- **[Strategy / AI]** "Is the logistics LLM a real moat?" → yes, but only insofar as it trains on multi-shipper proprietary flow no generic model or single customer has; name the bear case (frontier models + own data close the gap). → §1, §6, §9.
- **[Estimation]** "Size Uber Freight's AI-software revenue opportunity." → anchor on ~$20B FUM, assume X% attach at a software take-rate, contrast with the ~$1.6B run through AI today. → §3, §12.
- **[Execution]** "Freight is losing money — what do you do in the first 90 days?" → make the ops base variable-cost with agents (attack the cost line), convert AI design partners to paid, publish a path-to-breakeven. → §8, §11.
- **[Product sense]** "Why did Convoy die and Uber Freight survive?" → the pure-marketplace bet failed the cycle; survival needed assets, relationships, or a rich parent. → §1, §5.

---

## 14. Dig next
- Standalone Uber Freight segment revenue/EBITDA trend by quarter (Uber 10-Q segment notes) — earnings calls give almost no Freight detail. [S1][S2]
- Insights AI paid conversion numbers and pricing model (design-partner → paying) — only pilot-flow is disclosed today. [S4]
- Take-rate / net-revenue-margin for the brokerage vs. managed-transportation split — to quantify the mix-shift thesis in §3 unit economics.
- Carrier Card economics (interchange, spend, factoring attach) — §4/§12 rest on `[est]`.
- Current employee headcount + any post-2023 layoffs — cost-structure context.
- Whether Uber has publicly tied Freight to AV trough-fill beyond the earnings-call framing. [S2]
- Competitive: C.H. Robinson's own AI (Navisphere) progress; J.B. Hunt 360; DAT/Convoy marketplace traction post-July-2025. [S5][S6]

---

## 15. Source log
| S# | Title | Type | Date | Path / URL |
|---|---|---|---|---|
| S1 | Uber Q1 2026 earnings call | Transcript | 2026-05-06 | provided in task |
| S2 | Uber Q4/FY2025 earnings call | Transcript | 2026-02-04 | provided in task |
| S3 | "Uber Freight bets big on AI tools to grow its business" | Article | 2025-05-21 | https://techcrunch.com/2025/05/21/uber-freight-bets-big-on-ai-tools-to-grow-its-business/ |
| S4 | "Deliver 2025" platform features + "New era of intelligent supply chains" (Insights AI, 30+ agents, $1.6B, TMS Financials, Exchange) | Vendor blog/newsroom | 2025 | https://www.uberfreight.com/en-US/blog/deliver-2025-unveiling-new-platform-features ; https://www.uberfreight.com/en-US/newsroom/uber-freight-launches-industry-first-ai-logistics-network-at-scale-ushering |
| S5 | Uber Freight competition + segment EBITDA (−$43M), C.H. Robinson 2026 OI target, 2021 $2.1B rev, 2025 >$1.2B GMV | Article (Supply Chain Dive / FreightWaves / Sacra) | 2025 | https://www.supplychaindive.com/news/uber-freight-competition-freight-brokerage-morgan-stanley/562498/ ; https://www.freightwaves.com/news/technology-uber-freight-convoy-rise-as-traditiona-load-boards-lose-market-share |
| S6 | Convoy shutdown + DAT acquisition of Convoy platform (July 2025, ~30k carriers) | Article | 2025-07 | https://sacra.com/c/convoy/ |
| S7 | "Uber Freight Completes Acquisition of Transplace" ($2.25B, $550M financing, $16B FUM) | Press release / news | 2021-11-15 | https://www.cnbc.com/2021/07/22/uber-to-buy-transportation-logistics-company-transplace-in-2point25-billion-deal.html ; https://investor.uber.com/news-events/news/press-release-details/2021/Uber-Freight-Completes-Acquisition-of-Transplace/default.aspx |
| S8 | "Uber Freight rolls out integrated AI to simplify shipper operations" (agentic AI: scheduling, email time-capture, LTL data-fix) | Article | 2025-09-16 | https://www.digitalcommerce360.com/2025/09/16/uber-freight-agentic-ai/ |
| S9 | "How Does Uber Freight Work" (95k FTL / 150+ LTL carriers, 15-min quotes, Carrier Card same-day pay, Powerloop) | Guide | 2026 | https://parcelpath.com/how-does-uber-freight-work/ |
