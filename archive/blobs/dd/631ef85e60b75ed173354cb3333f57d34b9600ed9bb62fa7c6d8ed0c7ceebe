#!/usr/bin/env python3
"""Verify that the MTT book v10 matches the current reconciled corpus."""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
BOOK_ROOT = TEXPAPERS / "10 The Book on Modal Triplet Theory"
V9 = BOOK_ROOT / "_work" / "The_Book_on_Modal_Triplet_Theory_v9" / "main.tex"
V10 = (
    BOOK_ROOT
    / "revised_tex_vnext"
    / "The_Book_on_Modal_Triplet_Theory_v10"
    / "main.tex"
)
AUDIT = BOOK_ROOT / "BOOK_V10_CURRENT_CORPUS_RECONCILIATION_AUDIT_2026-07-15.md"

LABELS = (
    "Supersedes.",
    "Reason.",
    "Resolution.",
    "Retained result.",
    "Remaining boundary.",
)

REQUIRED_TOKENS = (
    r"\documentclass[11pt,openany]{book}",
    r"\date{July 2026\\Version 10}",
    "more than a metaphor and less than a",
    r"1+3\times3=(1+3)+(1+2+3)=4+6=10",
    r"\otimes_{\mathbb R}\mathbb C",
    r"\operatorname{Dic}_3",
    "Strict global Spin closure still requires",
    "q79 Fu--Yau branch is the strongest selected physical compactification",
    r"$27\times27$",
    r"$96\times96$",
    "12/12 obligations closed",
    "one-shared-physical-primitive/profile standard",
    "not a strict no-knob theorem",
    "Standard SM BRST/Faddeev--Popov quantization is imported",
    "Basin volume depends on a measure",
    r"\frac{I_2}{I_1}=0.5110273\pm0.0001231",
    r"\frac{I_3}{I_1}=0.158335\pm0.001098",
    "The old $4.2$--$5$ TeV crossing is withdrawn",
    "A Typed Atlas, Not a Universal Superset",
    "Current Claim Ledger",
)

FORBIDDEN_TOKENS = (
    "How spacetime, particles, forces, and quantum theory emerge from one field",
    "One field. One arena. Three filters. One inequality. One coherent world.",
    "three families only",
    r"\chapter{Ontic Gaussian damping}",
    r"\section{Ontic Gaussian damping}",
    "Osterwalder--Schrader positivity and BRST/BV consistency checks are satisfied",
    r"\chapter{The Great Coherence}",
    "recovered as coherent sectors of a single framework",
    "Born weights are basin volumes",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_environment_balance(text: str) -> None:
    stack: list[str] = []
    for match in re.finditer(r"\\(begin|end)\{([^{}]+)\}", text):
        action, name = match.groups()
        if action == "begin":
            stack.append(name)
            continue
        require(bool(stack), f"unmatched end environment: {name}")
        expected = stack.pop()
        require(expected == name, f"environment mismatch: began {expected}, ended {name}")
    require(not stack, f"unclosed environments: {stack}")


def check_revision_note(text: str) -> None:
    heading = r"\chapter*{Revision Note for This Edition}"
    toc = r"\addcontentsline{toc}{chapter}{Revision Note for This Edition}"
    require(text.count(heading) == 1, "expected one book revision-note chapter")
    require(text.count(toc) == 1, "revision note is not in the table of contents")

    note_start = text.index(heading)
    note_end = text.index(r"\end{description}", note_start)
    main_start = text.index(r"\mainmatter")
    require(note_start < note_end < main_start, "revision note is not in front matter")
    note = text[note_start:note_end]
    for label in LABELS:
        require(note.count(rf"\item[{label}]") == 1, f"missing revision field: {label}")
    require("version~9" in note, "superseded book version is not identified")
    require("q79" in note and "Born" in note and "few-TeV" in note, "revision note is not book-specific")


def main() -> int:
    require(V9.exists(), f"preserved v9 source missing: {V9}")
    require(V10.exists(), f"v10 source missing: {V10}")
    require(AUDIT.exists(), f"book reconciliation audit missing: {AUDIT}")

    text = V10.read_text(encoding="utf-8")
    require(text.isascii(), "v10 TeX contains non-ASCII source characters")
    require("amsthm" not in text, "unneeded amsthm dependency was reintroduced")
    require(not re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b", text), "placeholder remains")
    require(text.count(r"\begin{document}") == 1, "document start is not unique")
    require(text.count(r"\end{document}") == 1, "document end is not unique")
    require(text.rstrip().endswith(r"\end{document}"), "content follows end of document")
    require(text.count("{") == text.count("}"), "brace counts differ")
    check_environment_balance(text)
    check_revision_note(text)

    require(len(re.findall(r"\\part\{", text)) >= 7, "expected at least seven book parts")
    require(len(re.findall(r"\\chapter(?:\*)?\{", text)) >= 25, "book chapter coverage is unexpectedly small")
    require(text.count(r"\frontmatter") == 1, "front matter marker missing or duplicated")
    require(text.count(r"\mainmatter") == 1, "main matter marker missing or duplicated")
    require(text.count(r"\appendix") == 1, "appendix marker missing or duplicated")
    require(text.count(r"\backmatter") == 1, "back matter marker missing or duplicated")
    require(text.count(r"\endfirsthead") >= 2, "multi-page ledgers lack first-page headers")
    require(text.count(r"\endhead") >= 2, "multi-page ledgers lack continuation headers")

    for token in REQUIRED_TOKENS:
        require(token in text, f"required current-corpus token missing: {token}")
    for token in FORBIDDEN_TOKENS:
        require(token not in text, f"retired version-9 claim reappears: {token}")

    flat = re.sub(r"\s+", " ", text)
    require(
        "literal product $S^1\\times\\mathrm{Lens}\\times\\mathrm{Nil}$ and literal manifold nesting are retired"
        in flat,
        "Lens--Nil retirement is not explicit",
    )
    require(
        "completed UV-finite quantum- gravity language are withdrawn" in flat,
        "quantum-gravity withdrawal context is missing",
    )
    require(
        "It does not claim that MTT has derived the Born rule" in flat,
        "Born-rule boundary is not explicit in the abstract",
    )
    require(
        "Either route is additional source data, not a consequence of the rank count" in flat,
        "real/complex intertwiner guardrail is missing",
    )

    audit = AUDIT.read_text(encoding="utf-8")
    require("Version 9 is preserved unchanged" in audit, "audit lacks source-preservation statement")
    require("12/12" in audit and "96x96" in audit, "audit lacks current numerical baseline")
    require("Boundaries Preserved" in audit, "audit lacks remaining-boundary ledger")

    print("PASS: preserved v9 and complete v10 book sources found")
    print("PASS: v10 structure, environments, revision delta, and chapter coverage verified")
    print("PASS: current geometry, q79, SM-profile, Theta, and open-boundary claims verified")
    print("PASS: strongest retired v9 overclaim phrases are absent")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
