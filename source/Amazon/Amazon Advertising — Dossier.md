# Amazon Advertising — Product Dossier
> Amazon's retail-media and full-funnel ad business: it turns the world's largest purchase-intent dataset (shopper carts, searches, streaming) into ads, sold to sellers, brands, and agencies. Arc: it started as a keyword-search ad network bolted onto the store and became a full-funnel media platform (search → CTV → conversational AI) that is Amazon's highest-margin growth engine.
> **AMZN** (segment, not separate ticker) · Ads run-rate ~$68B/yr · ~75–80% of US retail media · Updated **2026-07-04** · Sources: **11** (see log)
> One living file. Arc: **Facts → Insights → Differentiators → Plays.** Skim the bold headlines for the gist; drill for detail.
> *v1 — earnings-grounded + web research. Ground every fact in a source; estimates labeled (est.).*

## 1. Business anatomy — Acquire / Engage / Retain / Monetize

- **Acquire (advertisers).** Self-serve funnel: any 3P seller (61% of units [S2]) or 1P brand can launch Sponsored Products in minutes from Seller/Vendor Central — no minimum. Up-funnel: Sponsored Brands/Display, then Sponsored TV and DSP (agency and enterprise, once high-minimum, now open to SMBs via resellers [S7]). The store itself is the top of the acquisition funnel — every seller who lists is a latent advertiser. Creative Agent removes the production-cost barrier that kept SMBs out of video and CTV. [S1]
- **Engage.** Core loop for a seller: launch campaign → win auction → gain sales velocity → earn organic rank ("halo") → grow → spend more to defend and expand. The aha is the TACoS realization — ads aren't a cost, they're the organic-growth flywheel. [S9] Amazon's own hooks: a unified Campaign Manager (merged Ads Console and DSP, late 2025) [S4], Ads Agent managing hundreds of campaigns, performance dashboards, and new-to-brand metrics.
- **Retain.** Switching cost is high: a seller's organic rank, review velocity, and Best-Seller badges all follow from sustained ad spend on Amazon — stop and you lose position to rivals who keep bidding. The catalog, the buyer graph, and fulfillment are all Amazon-locked. Net revenue retention is structurally high because ad spend is defensive as much as offensive (you bid on your own brand terms so rivals don't). No public NRR, but the halo mechanic makes churn self-punishing. [S9]
- **Monetize.** Several lines on one purchase graph: (1) **Sponsored Products** — CPC auction, largest offering, bottom-funnel [S2]; (2) **Sponsored Brands / Display** — CPC, brand plus retargeting, on and off Amazon; (3) **Sponsored TV / Prime Video / DSP** — CPM, CTV plus programmatic across Amazon-owned (Fire TV, Twitch, IMDb, Music) and third-party (Netflix, Disney+, Hulu) inventory [S7][S8]; (4) emerging **Sponsored Prompts** in the shopping agent (free beta as of 2026, monetization pending) [S8]. Take-rate is the auction clearing price; ARPU (revenue per advertiser) grows as sellers move up-funnel from search to CTV.

---

## 2. Numbers that signal depth

**Headline scale**
| Metric | Value | Source |
|---|---|---|
| Amazon Ads revenue, Q1 2026 | $17.2B, +22% Y/Y | [S1] |
| Amazon Ads revenue, Q4 2025 | $21.3B, +22% Y/Y | [S2] |
| Full-year 2025 ad revenue | $68B+ | [S6] |
| Incremental ad revenue added in 2025 | $12B+ | [S2][S6] |
| US retail-media revenue 2025 (ex-Prime Video/Twitch) | $60.6B | [S5] |
| US ad-rev forecast 2026 | ~$56.7B (17.9% growth) | [S4] |

**Market arcs**
| Metric | Value | Source |
|---|---|---|
| Amazon share of US retail media 2025 | 75%+ (some measures ~79.7%) | [S3][S5] |
| Walmart Connect (2nd) 2026 forecast | $5.99B | [S4] |
| Amazon + Walmart share of *incremental* retail media 2026 | 89% | [S5] |
| Amazon ad growth vs. Meta (14.2%) / Google (5.6%) | ~18% | [S4] |

**Surfaces & AI**
| Metric | Value | Source |
|---|---|---|
| Prime Video ad-supported viewers (global) | 315M+ (from 200M early-2024), 16 countries | [S2][S4] |
| Marketer ↑ in Prime Video spend, past year | +59% | [S4] |
| Rufus users (before Alexa-for-Shopping rebrand) | 300M used in 2025; ~250M MAU | [S2][S8] |
| Brand Prompt continuation rate | ~20% keep talking about the brand | [S1] |
| Sponsored-prompt buyers who are new-to-brand | ~70% | [S4] |
| Creative Agent country coverage | 7 countries | [S1] |
| Ads Agent early beta: time saved / ACoS improvement | 30–40% / 12–18% (vendor-reported) | [S8] |

**Unit economics (seller-side, industry benchmarks — not Amazon-reported)**
- Sponsored Products CPC ≈ $1/click (varies by category). [S7 context]
- Healthy account: ACoS ~28–30%, TACoS ~10–15%; 30–60% of brand revenue comes directly from ads, the rest organic. [S9]
- DSP was historically CPM-based with high minimums; in 2025 resellers opened DSP to SMBs with <$10K budgets. [S7]
- Ad-segment operating margin: **not disclosed**; est. 40%+ contribution given near-zero marginal inventory cost (est., inferred from the all-time-high 13.1% total op-margin [S1]).

---

## 3. Wow Vault ★
*Non-obvious layer — what makes an interviewer lean in. Ranked strongest first.*

**★ Amazon Advertising is a high-margin cash machine hiding inside a low-margin retailer**
- **Mechanism:** An ad slot on a search-results page a shopper already loaded costs almost nothing to fill. The traffic, the logistics, and the catalog are already paid for by the retail business. So each extra ad dollar drops almost straight to operating income. Amazon never breaks out ad-segment margin, but it is the reason NA op-margin hit 7.9% and worldwide op-margin hit an all-time-high 13.1% in Q1 2026. [S1]
- **Why non-obvious:** People model Amazon as a thin-margin retailer plus AWS. Ads is the third leg — ~$68B run-rate [S6] growing 22% [S1] at software-like margins — and it is what lets Amazon fund free shipping, price cuts ("America's lowest priced retailer, 14% lower on avg" [S2]), and Prime Video losses. The store is the loss-leader; ads and AWS are the profit.
- **Deploy:** Any "how does Amazon make money / where's the margin" question — recall hook: *"the shelf was already there; the ad is pure margin."*
- **Source:** [S1][S6]

**★ The ad product is the ranking algorithm's release valve — sellers pay to jump a queue Amazon controls**
- **Mechanism:** Organic rank on Amazon is earned through sales velocity. Sponsored Products lets a seller *buy* the velocity that then earns organic rank — the "halo." That's why healthy accounts run ACoS ~28–30% but TACoS 10–15%: ads rent the visibility that seeds the organic engine. [S9] Amazon charges for the one thing every seller wants and can't get another way: position on a page Amazon owns end to end.
- **Why non-obvious:** Sponsored Products looks like Google keyword ads, but it works differently. Amazon is both the auctioneer and the referee of the free results next to the ad, so it can tune how much organic reach a category gets — and therefore how much ad demand it creates.
- **Deploy:** "Is this a durable business / what's the pricing power" — recall hook: *"they sell the queue and also run the queue."*
- **Source:** [S9]

**★ First-party purchase data is a targeting asset Google and Meta cannot copy**
- **Mechanism:** Amazon knows what you *bought*, not just what you clicked or liked. Amazon DSP (its demand-side ad-buying platform) targets on real purchase history and reaches beyond Amazon.com — IMDb, Twitch, Fire TV, Amazon Music, plus third-party sites and now Netflix, Disney+, and Hulu CTV. [S7][S8] With cookies going away, this closed loop (ad exposure → actual purchase, measured on the same platform) is the cleanest attribution in advertising.
- **Why non-obvious:** Meta and Google optimize on guessed intent; Amazon optimizes on transactions and closes the loop itself. That is why marketers raised Prime Video spend 59% in a year [S4] — the same purchase graph, now in the living room.
- **Deploy:** Competitive / moat questions vs. Google and Meta — recall hook: *"purchase data beats click data, and only Amazon owns the receipt."*
- **Source:** [S7][S4]

**★ ~75–80% of US retail media runs through Amazon — a near-monopoly most people don't clock**
- **Mechanism:** Amazon took 75%+ of US retail-media ad spend in 2025; ~79.7% share by one measure. Walmart Connect is second at ~8% ($5.99B forecast 2026 vs. Amazon's $56.71B US). Amazon and Walmart together take 89% of *new* retail-media dollars in 2026. [S3][S5]
- **Why non-obvious:** "Retail media" sounds fragmented and competitive. It isn't — it's a duopoly tilting toward a monopoly, and Amazon's share is close to Google's in search, but younger and growing faster (17–22% vs. Google's ~6% ad growth [S4]).
- **Deploy:** Market-structure / TAM questions — recall hook: *"retail media isn't a race, it's Amazon and a rounding error."*
- **Source:** [S3][S5]

**★ Agentic shopping is both the biggest threat and the next ad surface**
- **Mechanism:** If shoppers hand buying to AI agents, the sponsored-search funnel shrinks — fewer humans look at the results page. Amazon's answer: make the agent (Rufus → now Alexa for Shopping) the surface. Multi-turn conversations create "multiple opportunities to surface relevant products… some of which will be sponsored." Nearly 20% of shoppers who hit a Brand Prompt keep talking about that brand; ~70% of sponsored-prompt buyers are new to the brand. [S1][S4]
- **Why non-obvious:** Everyone frames AI agents as a threat to Amazon's ad funnel. Amazon is turning the threat into inventory — a conversation has more places to sell than a single results page.
- **Deploy:** "How does AI change this business" / disruption questions — recall hook: *"the chat isn't the end of the ad — it's more ad slots per session."*
- **Source:** [S1][S4]

**★ The retailer-agent thesis: Amazon bets shoppers start at Rufus, not at ChatGPT**
- **Mechanism:** Jassy's contrarian claim — third-party general-purpose agents are "a small fraction" of even search-engine referrals and "not often able to get the pricing right or the product information right… no personalization data." Consumers want selection, low price, fast delivery, and trust; "horizontal agents are pretty good at aggregating selection, but retailers are much better at doing all 4." [S1][S2]
- **Why non-obvious:** The common fear is that OpenAI or Perplexity becomes the front door and Amazon becomes a dumb fulfillment backend — commoditized, with no ad surface. Amazon's bet is the reverse: the retailer's own agent wins because it has the live price, live inventory, and your purchase history.
- **Deploy:** "Is Amazon disintermediated by AI" — recall hook: *"horizontal agents aggregate; only the retailer can price, stock, and personalize."*
- **Source:** [S1][S2]

**★ Creative Agent cuts ad creation from weeks to hours — and that grows the advertiser base, not just efficiency**
- **Mechanism:** Creative Agent (agentic ad creation, now in 7 countries, builds streaming-TV ads from a concept) turns "a weeks-long process into just hours." [S1][S2] The point isn't speed for big brands — it's that SMB sellers who could never afford a video agency can now run CTV ads. "SMB creative so much faster… no longer have to spend as much money." [S1]
- **Why non-obvious:** AI-generated creative reads as a feature. It's really TAM expansion — it pulls the long tail of 2M+ sellers up-funnel into DSP and CTV inventory that production cost used to lock them out of.
- **Deploy:** "What's the growth lever" / AI-as-moat — recall hook: *"the moat isn't the creative, it's the millions of new advertisers it brings in."*
- **Source:** [S1][S2]

**★ Prime Video ads gave Amazon the top-of-funnel its marketplace ads never had**
- **Mechanism:** Prime Video's ad tier reaches 315M+ monthly viewers worldwide (up from 200M in early 2024). [S2][S4] Marketplace ads are bottom-funnel — they capture existing intent. Prime Video plus Thursday Night Football (15M+ avg viewers) [S2] give brand advertisers demand generation, targeted with the same purchase graph.
- **Why non-obvious:** Amazon quietly became a top-tier CTV/streaming ad seller by putting all Prime members into ads by default (opt-out costs extra), which built the largest premium ad-supported streaming audience overnight.
- **Deploy:** "How does Amazon go beyond search ads" — recall hook: *"they flipped a switch and 200M+ Prime members became a TV ad audience overnight."*
- **Source:** [S2][S4]

---

## 4. Reframes & mental models to borrow
- **"The shelf is already paid for."** An ad slot on a page the retail business already loaded costs ~zero at the margin → use on any margin/monetization prompt.
- **"Sell the queue, run the queue."** Amazon charges for position on a ranking it also controls → pricing-power and durability prompts.
- **"Rent visibility to seed organic (ACoS vs. TACoS)."** Ads buy sales velocity that earns free rank; the gap between the two metrics is the halo → metrics/analytics prompts. [S9]
- **"Purchase data beats click data."** Real transactions plus closed-loop attribution vs. guessed intent → competitive-moat prompts vs. Google/Meta.
- **"Horizontal agents aggregate; retailers do all four."** Selection, price, delivery, trust — the retailer-agent thesis → AI-disruption prompts. [S1]
- **"Barbell / full-funnel."** Bottom-funnel search (harvest intent) plus top-funnel CTV (create intent) in one purchase-graph buy → strategy/roadmap prompts.
- **"More turns, more slots."** A conversation sells better than a results page because it has more sponsored moments → agentic-commerce prompts. [S1]

---

## 5. Moats & Weaknesses

**Moats**
| Moat | Evidence | Deepening / eroding |
|---|---|---|
| First-party purchase data + closed-loop attribution | Real buy history powers DSP; ad → purchase measured on same platform | **Deepening** — extends to CTV via Prime Video/Netflix deals [S4][S8] |
| Owns the demand surface (auctioneer + referee of organic rank) | Sponsored Products = largest offering; halo/TACoS mechanic [S2][S9] | **Deepening** — agent surfaces add more slots [S1] |
| Retail-media scale duopoly | 75%+ US retail media; 89% of incremental w/ Walmart [S3][S5] | **Deepening** — outgrowing Google/Meta [S4] |
| Full-funnel in one buy (search → CTV) | 315M Prime Video viewers on same graph [S2] | **Deepening** — Netflix/Comcast/Samsung expansion [S1] |
| AI creative removes SMB cost barrier | Creative Agent weeks→hours, 7 countries [S1] | **Deepening** — grows advertiser base |

**Weaknesses**
| Weakness | Why it bites | Where a rival attacks |
|---|---|---|
| Concentrated on bottom-funnel search intent | Most revenue captures existing demand, not demand-gen; caps TAM vs. brand budgets | Google/Meta/TikTok own upper-funnel discovery + brand affinity |
| On-Amazon only for most inventory | Off-Amazon reach (DSP) is smaller and less proven than the open web | The Trade Desk / Google own the independent open web at scale |
| Agentic shopping shrinks the results page | Fewer human page-views = fewer sponsored-search impressions if agents mediate | OpenAI/Perplexity as the shopping front door, bypassing Amazon's ad surface |
| "Pay-to-play" fatigue among sellers | Rising CPCs eat seller margins; ads feel like a tax on the marketplace | Shopify/DTC pitch "own your customer, no ad tax" |
| Ad clutter erodes shopper trust | Too many sponsored slots hurt relevance and long-term conversion | Any rival competing on a cleaner, higher-trust results experience |

---

## 6. AI impact — deflationary or moat?

| AI vector | Deflationary | Moat-deepening |
|---|---|---|
| Generative ad creative (Creative Agent) | Creative gets cheap and commoditized industry-wide | ✔ But pulls millions of SMB sellers into CTV/DSP they couldn't afford — TAM expansion on Amazon's inventory [S1] |
| Campaign automation (Ads Agent, Bedrock-powered) | Agencies' optimization labor commoditized | ✔ Runs on Amazon's own real-time auction + purchase data; 30–40% time savings keeps spend on-platform [S8] |
| Conversational/agentic shopping (Alexa for Shopping) | Threatens the sponsored-search page-view model | ✔ Turns each conversation into several sponsored turns; ~20% brand-continuation, ~70% new-to-brand [S1][S4] |
| Horizontal AI agents (ChatGPT/Perplexity shopping) | Could push Amazon out of the front door | Retailer-agent thesis: only Amazon has live price + stock + your receipts [S1] |
| First-party data + LLM targeting | — | ✔ The purchase graph makes Amazon's models better-grounded than click-based rivals [S7] |

**Net read:** Net **tailwind**. AI cheapens the parts Amazon doesn't monetize (creative production, campaign labor) while deepening the parts it owns (purchase-grounded targeting, the demand surface, closed-loop attribution). AI grows the advertiser base and adds ad slots per session. **The one real risk to watch:** if consumers adopt a *third-party* agent (ChatGPT/Perplexity) as the shopping front door faster than Amazon can make its own agent the default, the sponsored-search page-view — Amazon's largest ad line — erodes before the conversational-ad line is monetized to replace it. The Sponsored Prompts beta being *free* as of 2026 [S8] shows the replacement revenue isn't proven yet.

---

## 7. Needs-based segments → problems → solutions
*Shreyas method — segment on the JOB the advertiser is hiring Amazon Ads to do, not company size or vertical. Each passes the 5-Point Test (consistent needs · product-specific · targetable · prioritizable · winnable).*

**Segmentation basis:** the advertiser's *funnel position and relationship to Amazon's sales channel* — because on Amazon, the ad's job depends on where the buyer is in the purchase decision and whether the advertiser sells on Amazon at all. Demographics (SMB vs. enterprise) cut across all of these and predict nothing about the job.

**A. "Defend my shelf" — the incumbent seller protecting won position.** Job (functional): keep competitors off my product and brand terms and hold organic rank. (Emotional): fear of losing the Best-Seller badge overnight. Friction: rising CPCs feel like extortion; hard to prove defensive spend "works." Nudge (extrinsic): show share-of-voice erosion when they pause. Aha: *"my TACoS held and organic rank held — the spend was insurance that paid rank."* Today: Sponsored Products/Brands on own and competitor terms. Gap: no clear "defensive vs. offensive" spend split in reporting. → **Play #1**.

**B. "Buy me velocity to earn rank" — the launcher of a new product.** Job (functional): create the sales velocity that Amazon's algorithm turns into free organic rank. (Social): get to page 1 before the review flywheel exists. Friction: cold start — no reviews, no history, ACoS spikes to 60%+. Nudge (intrinsic): the halo — every paid sale seeds future organic sales. Aha: *"ACoS was ugly for 8 weeks, then organic took over and TACoS fell."* [S9] Today: aggressive Sponsored Products bidding. Gap: no explicit "launch mode" that front-loads spend against a rank target. → **Play #2**.

**C. "Create demand I don't have yet" — the brand marketer doing demand-gen.** Job (functional): reach people *before* they search, build brand affinity. (Emotional): be seen as a real brand, not a marketplace commodity. Friction: Amazon is bottom-funnel by reputation; CTV production is expensive and slow. Nudge: Creative Agent (weeks→hours) plus Prime Video's 315M viewers on the same purchase graph. Aha: *"I ran a CTV spot and watched new-to-brand purchases move — attribution I never got on regular TV."* [S1][S2] Today: DSP + Prime Video + Sponsored TV. Gap: creative barrier for SMBs (now falling). → **Play #3, #6**.

**D. "Reach my buyer everywhere, measured once" — the omnichannel performance advertiser.** Job (functional): one buy across Amazon, open web, and CTV with unified purchase-based attribution. (Personal): stop reconciling 5 dashboards. Friction: DSP was enterprise-only, high minimums, complex. Nudge (extrinsic): unified Campaign Manager plus closed-loop measurement rivals can't match. Aha: *"one audience, one report, real-purchase attribution across Netflix and Amazon."* [S4][S7] Today: DSP + unified console. Gap: off-Amazon reach still trails the open-web independents. → **Play #4**.

**E. "Convert the conversation" — the advertiser chasing the agentic shopper.** Job (functional): be the product the AI shopping agent recommends. (Emotional): fear of being invisible when a human never sees the results page. Friction: no playbook, Sponsored Prompts still free beta, no bid controls. Nudge (intrinsic): ~70% of sponsored-prompt buyers are new to the brand — pure incremental reach. Aha: *"the agent surfaced us mid-conversation and the shopper kept asking about our brand."* [S1][S4] Today: Sponsored Products Prompts (free beta). Gap: unmonetized, unmeasured, no optimization surface. → **Play #5**.

---

## 8. Strategy *(Shreyas Strategy Template)*
- **One-sentence strategy:** Turn the world's largest purchase-intent dataset into a full-funnel ad platform by monetizing every surface a shopper touches — search results, TV, and now AI conversations — with attribution rivals can't replicate.
- **Prioritize / Don't over-serve:** Prioritize **incremental, purchase-grounded surfaces** (Sponsored Products, Prime Video/CTV, agentic prompts) and the **long tail of SMB advertisers** (via self-serve + AI creative). Don't over-serve **off-Amazon open-web display** as a standalone business — it's a feature of the buy, not the point.
- **Pillars (moat → segment):** (1) Purchase data + closed-loop attribution → serves D & C. (2) Ownership of the demand surface + halo mechanic → serves A & B. (3) Full-funnel in one buy (search→CTV→chat) → serves C, D, E. (4) AI removing creation/optimization cost → serves the SMB long tail across all segments.
- **North star:** Advertiser-attributed incremental sales per shopper session (revenue Amazon can prove the ad *caused*, across every surface) — because that's the number that justifies moving budget off Google/Meta and survives the move to agents.
- **Non-priorities (trade-offs):** Amazon accepts more ad clutter on the results page (short-term trust cost) to grow monetization; accepts being bottom-funnel-heavy rather than chasing pure brand-awareness budgets; won't hand its purchase data to third-party horizontal agents on terms that commoditize it ("a value exchange that makes sense for both parties" [S2]).
- **Roadmap / metrics:** Now — grow Sponsored Products + Prime Video (leading: advertiser count / new-to-brand %; lagging: ad revenue, +22% [S1]). Next — monetize the shopping agent + scale Creative Agent globally (leading: sponsored-prompt continuation ~20% [S1], SMB CTV advertisers; lagging: prompt-ad revenue once beta ends). Later — own omnichannel measurement as the industry standard (leading: DSP off-Amazon reach; lagging: DSP share of total ad revenue).

---

## 9. Contrarian bets & open tensions
- **Bet: the shopping agent adds ad slots rather than removing them.** *Bear case:* agents shop *for* the user, no results page is ever seen, sponsored-search (the biggest line) collapses, and the free Prompts beta never monetizes at replacement scale. *Counter:* a multi-turn conversation has more sellable moments than one page; ~70% of prompt buyers are new to the brand — real incremental reach, not cannibalized. [S1][S4] *Best skeptic angle:* it's still **free beta** in 2026 — Amazon hasn't proven anyone will *pay* for a conversational slot.
- **Bet: shoppers start at the retailer's agent, not ChatGPT.** *Bear case:* consumers already treat ChatGPT/Perplexity as the answer layer; Amazon becomes fulfillment plumbing behind someone else's front door. *Counter:* horizontal agents "can't get pricing or product info right… no personalization data"; retailers do selection, price, delivery, and trust. [S1] *Skeptic angle:* Amazon said the same about Google search referrals for years and still pays for them — front-door control isn't guaranteed.
- **Bet: more ad load is worth the trust cost.** *Bear case:* stuffing in sponsored slots (and now sponsored *prompts*) hurts relevance, shoppers trust results less, long-term conversion falls — the classic ad-load-vs-experience death spiral. *Counter:* purchase-grounded targeting keeps sponsored results relevant enough that clutter hasn't dented units (+15% [S1]). *Valuation tension:* ad revenue is the margin story propping up the whole company's 13.1% op-margin [S1] — the market is pricing in continued 20%+ ad growth, so any slowdown from agent-driven funnel compression hits the stock harder than its size alone.

---

## 10. Big Picture — Looks Wrong, Is Right

**A. Wise refusals**
- **Not handing purchase data to third-party horizontal agents on their terms** → looks like refusing free distribution; is right because the data plus closed-loop attribution is the moat — giving it away turns Amazon into a fulfillment backend. Jassy insists on "a value exchange that makes sense for both parties." [S2]
- **Not breaking out ad-segment margin** → looks like opacity investors dislike; is right because disclosing 40%+ (est.) margins would invite antitrust scrutiny of a near-monopoly and hand competitors and sellers a pricing-fairness argument. [S1]
- **Keeping Sponsored Prompts free (not monetizing the agent yet)** → looks like leaving money on the table; is right because charging before shopper behavior settles would suppress the adoption that builds the new inventory. Seed the surface first, charge once it carries weight. [S8]

**B. Counterintuitive moves**
- **Cluttering its own store with ads while claiming to be the most customer-obsessed retailer** → serves the flywheel: ad margin funds the price cuts (14% cheaper on avg [S2]) and free shipping that drive the traffic the ads monetize. The clutter pays for the low prices. [S2]
- **Putting all Prime members into ad-supported Prime Video by default (opt-out costs extra)** → looks anti-customer; it built a 315M-viewer premium CTV audience overnight [S2], the top-of-funnel Amazon's search ads lacked — targeted with the same purchase graph.
- **Opening DSP to sub-$10K SMBs via resellers** → looks like diluting a premium enterprise product; is right because AI creative (Creative Agent) makes the long tail servable at near-zero marginal cost, and millions of small advertisers is a bigger, stickier pool than a few hundred agencies. [S7][S1]

---

## 11. Mistakes & Mis-executions → Opportunities
- **Ad clutter is nearing relevance-degrading levels on the results page** → *why:* every quarter's revenue target pulls toward more slots; the auctioneer-and-referee conflict has no internal check → *opportunity:* a shopper-trust guardrail metric (organic-result satisfaction) tied to ad-load, sold as "quality density" — protects the long-term conversion the halo depends on. [S9]
- **Reporting still centers ACoS, not TACoS — under-teaching sellers the real value** → *why:* ACoS is the legacy click-attribution metric; Amazon under-invests in surfacing the organic halo it delivers → *opportunity:* make TACoS plus a defensive/offensive spend split first-class in the console; sellers who track TACoS are 2.3x more likely to grow profitably [S9] — teaching it cuts ad-tax fatigue and churn. → ties to Segment A/B.
- **Off-Amazon (open-web) reach lags the independents despite better data** → *why:* Amazon built out its owned-and-operated surfaces first; open-web supply and transparency trail The Trade Desk → *opportunity:* use the memory and supply advantages plus the Netflix/Comcast deals [S1] to make DSP the default purchase-attributed open-web buy. → ties to Segment D / Play #4.
- **Late and cautious on the conversational-ad surface (still free beta in 2026)** → *why:* fear of degrading the new agent experience plus no monetization model yet; defensible but risks a horizontal agent setting shopper habits first → *opportunity:* ship bid controls plus measurement for Sponsored Prompts before the front-door habit sets. [S1][S8] → ties to Segment E / Play #5.
- **Brand-name churn (Rufus → Alexa for Shopping mid-2026)** → *why:* renaming a 300M-user product [S2] mid-flight risks advertiser and shopper confusion during the exact window habits form → *opportunity:* stability plus a single advertiser-facing surface across the agent, so the ad product isn't re-learned each rename. [S10]

---

## 12. What's missing → Plays to run *(10× / 100× — hypotheses, not today)*

**Gaps:** (a) sellers can't tell defensive from offensive ad spend; (b) no "launch mode" that front-loads spend against a rank target; (c) SMBs still under-penetrated in CTV despite falling creative cost; (d) off-Amazon reach trails the open web; (e) the agent surface is unmonetized and unmeasured.

- **Play #1 — Defensive Shield reporting + auto-bidding.** Split ad spend into "defend won position" vs. "acquire new," auto-bid to hold share-of-voice on owned terms. *Closes gap (a).* *Why Amazon:* it owns the share-of-voice and rank data no one else sees. *10x* on Segment A retention (turns fear-driven spend into a measurable product). *Proof:* pilot a "share-of-voice held" metric with 100 brand-registered sellers.
- **Play #2 — Launch Mode.** A guided campaign that front-loads spend against a page-1-rank target, accepts high ACoS for N weeks, then tapers as organic takes over. *Closes gap (b).* *Why Amazon:* only it knows the velocity→rank function. *10x* on new-product success rate; deepens the halo lock-in. *Proof:* A/B launch-mode vs. manual on new ASINs, measure week-12 organic rank.
- **Play #3 — SMB CTV in a box.** Creative Agent → one-click Prime Video/Sponsored TV campaign for any seller, budgeted from their existing Sponsored Products spend. *Closes gap (c).* *Why Amazon:* Creative Agent (weeks→hours [S1]) + 315M-viewer inventory + purchase attribution. *100x* on CTV advertiser count (few hundred agencies → millions of sellers). *Proof:* offer to top 10K sellers, measure CTV adoption + new-to-brand lift.
- **Play #4 — Purchase-attributed open web as the default.** Make DSP the buy where every open-web/CTV impression is measured against actual Amazon purchases, positioned as the answer to cookie-loss. *Closes gap (d).* *Why Amazon:* closed-loop attribution + Netflix/Comcast/Samsung supply [S1]. *10x* on off-Amazon share. *Proof:* publish attributed-ROAS case studies vs. open-web incumbents.
- **Play #5 — Conversational Ads platform (bid + measure).** Turn Sponsored Prompts from free beta into a real auction with bid controls, brand-safety, and a conversation-attribution metric. *Closes gap (e).* *Why Amazon:* it owns the agent AND the receipt. *100x* if agentic shopping scales — a whole new inventory class. *Proof:* charge a small cohort, measure willingness-to-pay vs. new-to-brand lift (~70% [S4]).
- **Play #6 — Creative Agent as an ad network flywheel.** Let Creative Agent auto-generate and auto-place cross-format campaigns (search + display + CTV + prompt) from one product page. *Why Amazon:* full-funnel inventory + generative creative in one house. *10x* ARPU by moving sellers up-funnel automatically.

**Small compounding wins:** TACoS-first dashboards; new-to-brand as a default KPI; brand-term defense alerts; auto-negative-keyword suggestions; Prime Day launch-mode presets; unified single login across ad surfaces; localized Creative Agent in more of the 7→N countries [S1].

---

## 13. Interview arsenal
- **[Strategy]** "Where does Amazon actually make money?" → §1 ★1 + §4 Monetize: ads (+AWS) are the margin; the store is the loss-leader. Recall: *"the shelf is already paid for."*
- **[Product sense]** "Design a feature for a struggling Amazon seller." → §7 Segment B + §12 Play #2 Launch Mode; anchor on the velocity→rank halo, measure via TACoS not ACoS. [S9]
- **[Strategy / competitive]** "How does Amazon Ads beat Google & Meta?" → §1 ★3 + §5 moats: real purchase data + closed-loop attribution + owning the demand surface.
- **[Product sense / AI]** "Do AI shopping agents kill Amazon's ad business?" → §1 ★5–6 + §9: conversation adds slots; retailer-agent thesis; but flag the free-beta risk. [S1][S8]
- **[Metrics]** "What's the north star for Amazon Ads?" → §8: advertiser-attributed incremental sales per session; contrast ACoS vs. TACoS as the analyst's tell. [S9]
- **[Market sizing / estimation]** "Size US retail media / Amazon's share." → §3: ~$60B US retail media 2025, Amazon 75%+, Walmart ~8%. [S3][S5]
- **[Product design]** "How would you monetize the shopping agent without ruining trust?" → §12 Play #5 + §10-A: seed free, add bid controls + conversation-attribution, guardrail on relevance.
- **[Execution]** "Amazon just cut seller fees / Prime Day moved — how does that hit ads?" → §4 flywheel: ad margin funds price cuts that drive the traffic ads monetize. [S1][S2]

---

## 14. Dig next
- Exact ad-segment operating margin — currently estimated; find any analyst teardown or SEC-filing breakout.
- Sponsored Products vs. DSP vs. Prime Video revenue split — Amazon lumps all as "advertising services."
- Alexa-for-Shopping rebrand impact on advertiser tooling and Sponsored Prompts roadmap post-May 2026. [S10]
- DSP off-Amazon reach vs. The Trade Desk (open-web share numbers).
- International ad growth by geo (EU/Brazil/India) — earnings only give worldwide.
- Whether/when Sponsored Prompts exits free beta and its pricing model. [S8]

---

## 15. Source log
| S# | Title | Type | Date | Path / URL |
|---|---|---|---|---|
| S1 | Amazon Q1 2026 Earnings Call | Earnings transcript | 2026-04-29 | _sources/Amazon-latest-earnings.txt |
| S2 | Amazon Q4 2025 Earnings Call | Earnings transcript | 2026-02-05 | _sources/Amazon-latest-earnings.txt |
| S3 | eMarketer — Amazon retail media dominance FAQ | Analyst | 2025-2026 | emarketer.com/content/faq-on-amazon-advertising--retail-media-dominance--prime-video-scale--agentic-ad-tools |
| S4 | eMarketer — Amazon advertising key facts (Prime Video, agentic) | Analyst | 2025-11 | emarketer.com (same FAQ, figures) |
| S5 | Advanced Television — Amazon 2025 retail media >$60bn | News | 2025-05-21 | advanced-television.com/2025/05/21/forecast-amazon-2025-retail-media-ad-revenue-to-exceed-60bn/ |
| S6 | Marketing Dive — Amazon annual ad revenue passes $68B | News | 2026-02 | marketingdive.com/news/amazon-annual-ad-revenue-passes-68b-boosted-by-full-funnel-strategy/811569/ |
| S7 | Amazon Ads — DSP product page + 2025 guides | Vendor/product | 2025 | advertising.amazon.com/solutions/products/amazon-dsp |
| S8 | Novadata / Scaledon — Ads Agent & Rufus Ads 2026 | Vendor analysis | 2026 | novadata.io/resources/news/amazon-ads-agent-ai-campaign-management |
| S9 | Quartile / Helium 10 — ACoS vs TACoS | Vendor education | 2025 | quartile.com/blog/tacos-amazon-advertising-vs-acos |
| S10 | Adweek — Alexa for Shopping rebrand | News | 2026-05 | adweek.com/commerce/amazons-souped-up-ai-rebrand-with-alexa-reveals-its-advertising-growth-plans/ |
| S11 | Amazon Ads unBoxed 2025 — Creative Agent | Vendor/product | 2025 | advertising.amazon.com/resources/whats-new/unboxed-2025-creative-agent |
