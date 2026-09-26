---
name: proposal-writer
description: Write client-winning business proposals in English, especially for AI, software, web, and consulting services. Use whenever the user wants to create, draft, write, or improve a "proposal", "quote", "statement of work", "SOW", or a client-facing offer. Produces a structured 12-section proposal that leads with the client's problem and value, not the tools.
---

# Proposal Writer — Writing a Winning Proposal

The goal of this skill: build a proposal that gets the client to "yes." A proposal is the bridge between the sales conversation and the signed contract — not your technical resume.

## Three Golden Rules (never break these)

1. **Write about the client, not about yourself.** Focus on their problem and their outcome, not your technical capabilities.
2. **Sell the outcome, not the tool.** The client isn't buying a "chatbot"; they're buying "3 free hours a day" and "more leads." Drop technical jargon (RAG, embeddings, API) unless the client is technical themselves.
3. **Keep it short and clear.** For small businesses, 2-4 pages is enough. A long proposal doesn't get read.

## Workflow

### Step 1 — Gather information (ask before writing)
If the user hasn't given you these, ask before writing. Without them the proposal comes out generic and ineffective:
- Client name / company and the main point of contact
- The client's core problem or need (in their own words and numbers — "3 hours a day," "losing 20% of leads")
- What you're building / delivering (scope of work)
- Budget / price and payment terms
- Rough timeline
- The user's own brand/company name and contact info

If some details are unclear, make a reasonable assumption and mark it with `[...]` so the user can fill it in later — don't stall the work over it.

### Step 2 — Write the 12 sections
Read `references/methodology.md` and follow it for detailed guidance and tone for each section. Structure:

| # | Section | Required? |
|---|---|---|
| 1 | Header and basic details (title, parties, date, expiration date) | |
| 2 | Executive summary — 3-4 sentences: problem → solution → main outcome | ★ |
| 3 | Our understanding of your situation — reflect the client's problems back in their own words | ★ |
| 4 | Proposed solution — simple, without heavy technical jargon | ★ |
| 5 | Scope of work (included ✅ / not included ⛔) | ★ |
| 6 | Phases and timeline — phase/task/duration table | ★ |
| 7 | Expected results and value — in terms of money and time + simple ROI | ★ |
| 8 | Investment and payment terms — price comes *after* value is proven | ★ |
| 9 | What we need from you — access, content, point of contact | |
| 10 | About us — brief, results-focused credibility | |
| 11 | Terms and offer validity — expiration, number of revisions, ownership | |
| 12 | Next step and acceptance — make saying "yes" easy | ★ |

★ sections are required for every proposal. For small projects, non-required sections can be shortened or merged.

### Step 3 — Final review
Before delivery, check the "Common Mistakes" section in `references/methodology.md`. Make sure:
- The executive summary is self-contained (if someone reads only that, they get the message).
- The price comes after the value, not before it.
- The scope of work has a clear boundary (included/not included).
- The next step is a specific, simple action, not a vague ending.
- The word "investment" is used instead of "cost."

## Format and language

- Output defaults to **English, left-to-right (LTR)**, unless the user asks otherwise.
- Write the output as a Markdown file (e.g. `proposal-[client].md`).
- For formal delivery to the client, convert the file to **PDF**:
  `python .claude/skills/proposal-writer/scripts/md_to_pdf.py proposal-[client].md`
  This script converts the Markdown into styled HTML and prints it with headless Chrome/Edge (requires: `pip install markdown` and Chrome or Edge installed). For Word output, use the `docx` skill.
- Tone: professional but plain and human. No overblown promises, no hollow corporate-speak.
- An expiration date on the header creates gentle time pressure — always include one.

## Reference example

`references/example-proposal.md` is a complete, realistic example proposal (website + AI assistant project). Use it as a model for structure, tone, and level of detail — but don't copy the content blindly; replace it with your current client's actual situation.
