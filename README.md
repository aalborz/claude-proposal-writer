# claude-proposal-writer

A [Claude Code Skill](https://docs.claude.com/en/docs/claude-code/skills) for writing **client-winning business proposals in English**, especially for AI, software, web, and consulting services. The output is a structured 12-section proposal (LTR) that starts from the client's problem and value instead of selling the tools.

## What it does

Built on a proven proposal-writing methodology, embedding these principles:

- **Three golden rules:** write about the client, not yourself; sell the outcome, not the tool; stay short and clear.
- **12-section framework:** executive summary, understanding of the situation, solution, scope (included/excluded), timeline, value/ROI, investment, and next step.
- **Automatic self-review** against an 8-item checklist of common mistakes.
- **Clean PDF output** with a professional color palette (navy/gold/teal).

## Install

Clone this repo into your Claude Code skills folder:

```bash
# project level
git clone https://github.com/aalborz/claude-proposal-writer .claude/skills/proposal-writer

# or user level (all projects)
git clone https://github.com/aalborz/claude-proposal-writer ~/.claude/skills/proposal-writer
```

Then in Claude Code, just say: "write a proposal for [client]" — the skill activates automatically.

## Structure

| Path | Description |
|---|---|
| `SKILL.md` | Core instructions: rules, workflow, and the 12-section table |
| `references/methodology.md` | Detailed guide for each section + common mistakes + checklist |
| `references/example-proposal.md` | A complete reference example (website + AI assistant) |
| `scripts/md_to_pdf.py` | Converts a Markdown proposal to PDF |
| `examples/` | Two generated examples (online store, medical clinic) |

## Building a PDF

```bash
pip install markdown          # requirement
python scripts/md_to_pdf.py examples/proposal-clinic.md
```

The script converts Markdown into styled HTML and prints it with headless Chrome or Edge. Only Chrome or Edge is required.

Brand colors are defined as variables at the top of `scripts/md_to_pdf.py`; to use a different brand, just swap the hex values.

## Credit

Methodology adapted from the [Careerpreneur Academy](https://careerpreneuracademy.com/proposal-writing.html) proposal-writing guide — AI Consultant course.

## License

[MIT](LICENSE)
