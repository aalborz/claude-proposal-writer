#!/usr/bin/env python3
"""
Convert a Markdown proposal to a professionally styled PDF.
Path: Markdown -> styled HTML (LTR) -> PDF via headless Chrome/Edge.

Usage:
    python md_to_pdf.py input.md [output.pdf]
"""
import sys
import os
import subprocess
import tempfile

import markdown  # pip install markdown

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

# ---- brand colors (swap these hex values for your own brand) ----
NAVY = "#0e1a2b"       # primary navy (headings, text)
NAVY2 = "#16263d"
GOLD = "#c8943b"       # brand gold (accent)
GOLD_DARK = "#9a6f1f"
GOLD_SOFT = "#e3c489"
TEAL = "#2c7a7b"       # teal (secondary accent)
PAPER = "#fbf9f4"      # paper-like background
PAPER_SOFT = "#f4f0e7"
BORDER = "#e7e1d4"
MUTED = "#5b6675"


def build_css():
    return f"""
@page {{ size: A4; margin: 18mm 16mm; }}
* {{ box-sizing: border-box; }}
body {{
    font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    direction: ltr; text-align: left;
    color: {NAVY}; line-height: 1.6; font-size: 12pt;
    background: #fff;
    -webkit-print-color-adjust: exact; print-color-adjust: exact;
}}
h1 {{
    font-size: 21pt; font-weight: 700; color: {NAVY}; margin: 0 0 4pt;
    border-bottom: 3px solid {GOLD}; padding-bottom: 10pt; line-height: 1.3;
}}
h2 {{
    font-size: 15pt; font-weight: 700; color: {NAVY}; margin: 22pt 0 8pt;
    padding-left: 10pt; border-left: 4px solid {GOLD};
    page-break-after: avoid;
}}
h3 {{ font-size: 13pt; font-weight: 500; color: {TEAL}; margin: 14pt 0 6pt; }}
p {{ margin: 6pt 0; }}
strong {{ color: {NAVY2}; font-weight: 700; }}
a {{ color: {GOLD_DARK}; text-decoration: none; }}
ul, ol {{ margin: 6pt 0; padding-left: 22pt; }}
li {{ margin: 3pt 0; }}
li::marker {{ color: {GOLD}; }}
hr {{ border: none; border-top: 1px solid {BORDER}; margin: 16pt 0; }}
blockquote {{
    margin: 12pt 0; padding: 10pt 14pt;
    background: {PAPER_SOFT}; border-left: 4px solid {GOLD};
    color: {NAVY2}; border-radius: 4px;
}}
table {{
    border-collapse: collapse; width: 100%; margin: 10pt 0; font-size: 11pt;
    page-break-inside: avoid;
}}
th, td {{ border: 1px solid {BORDER}; padding: 7pt 10pt; text-align: left; }}
thead th {{ background: {NAVY}; color: {PAPER}; font-weight: 700; }}
tbody tr:nth-child(even) {{ background: {PAPER}; }}
table, blockquote {{ page-break-inside: avoid; }}
"""


def convert(md_path, pdf_path=None):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()

    if pdf_path is None:
        pdf_path = os.path.splitext(md_path)[0] + ".pdf"
    # Chrome resolves --print-to-pdf relative to its own cwd, so force absolute.
    pdf_path = os.path.abspath(pdf_path)

    html_body = markdown.markdown(text, extensions=["tables", "sane_lists"])
    html = f"""<!DOCTYPE html>
<html lang="en" dir="ltr"><head><meta charset="utf-8">
<style>{build_css()}</style></head><body>{html_body}</body></html>"""

    tmp_html = tempfile.NamedTemporaryFile(
        suffix=".html", delete=False, mode="w", encoding="utf-8"
    )
    tmp_html.write(html)
    tmp_html.close()

    chrome = next((c for c in CHROME_CANDIDATES if os.path.exists(c)), None)
    if not chrome:
        raise SystemExit("Chrome/Edge not found. Install Chrome or Edge.")

    file_url = "file:///" + tmp_html.name.replace("\\", "/")
    subprocess.run([
        chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}", file_url,
    ], check=True)
    os.unlink(tmp_html.name)
    print(f"PDF created: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python md_to_pdf.py input.md [output.pdf]")
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
