from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "revised_tex_vnext" / "Modal_Triplet_Theory__A_Typed_Relationship_Atlas_v3"
TEX = PROJECT / "main.tex"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_environments(text: str) -> None:
    stack: list[str] = []
    for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", text):
        action, environment = match.groups()
        if action == "begin":
            stack.append(environment)
        else:
            require(bool(stack), f"orphan end{{{environment}}}")
            require(stack.pop() == environment, f"misnested environment {environment}")
    require(not stack, f"unclosed environment {stack[-1] if stack else 'unknown'}")


def main() -> None:
    require(TEX.exists(), "Relationship Atlas v3 main.tex missing")
    text = TEX.read_text(encoding="utf-8")
    check_environments(text)

    required = [
        "typed\natlas of relationships",
        "not a proved superset of all",
        "Why the superset claim is reclassified",
        "Typed relationship vocabulary",
        "Embedding",
        "Controlled reduction",
        "Reconstruction",
        "Conditional bridge",
        "Interpretive correspondence",
        "Calibration and postdiction",
        "Containment certificate",
        "canonicality statement",
        "Motif reuse is not containment",
        "Relationships also do not compose automatically",
        "Realization underdetermination",
        "does not select a unique MTT\nrealization",
        "Reconstruction is not inevitability",
        "Current cross-framework atlas",
        "GR is therefore not derived",
        "Born rule and full quantum equivalence remain",
        "Exact SM closure\nis not used as evidence",
        "does not select the compactification",
        "No unique-vacuum or landscape-elimination theorem",
        "former all-loop constructive-QG conjunction is withdrawn",
        "No Barbero--Immirzi prediction",
        "does not identify stabilization time with RG scale",
        "MTT\nadmissibility alone does not derive local finiteness",
        "Shared-symbol insufficiency",
        "Synthetic or mock fits validate software and identifiability, not\nphysical closure",
        "Predictive closure ladder",
        "Typed MTT relationship atlas",
        "No universal containment theorem follows",
        "underdetermined until a source-independent canonicality theorem",
    ]
    for item in required:
        require(item in text, f"required atlas repair missing: {item}")

    forbidden = [
        "\\begin{theorem}[Superset Containment Theorem]",
        "\\begin{theorem}[Emergence of the Born rule]",
        "\\begin{theorem}[Family number from modal reuse]",
        "\\begin{theorem}[Flux fixed point equals unique minimizer]",
        "\\begin{theorem}[UV finiteness and BV/QME]",
        "\\begin{theorem}[LQG containment]",
        "\\begin{theorem}[Bottleneck reuse across regimes]",
        "fully constructive completion",
        "unique stable coherent fixed point",
        "all major frameworks of theoretical physics considered here arise",
        "We have shown that MTT",
        "contains as projections",
        "no sector introduces independent parameters",
        "there are fewer free parameters than in the SM+GR baseline",
        "MTT is highly predictive",
        "MTT inherits existing experimental validation",
        "perturbatively unitary, causal, UV-finite QG",
        "single dynamically selected background",
        "exactly three mutually commuting modal bundles",
    ]
    for item in forbidden:
        require(item not in text, f"withdrawn superset claim remains: {item}")

    require(text.count(r"\end{document}") == 1,
            "Relationship Atlas v3 must have exactly one end{document}")
    require(all(ord(char) < 128 for char in text),
            "non-ASCII or mojibake remains in Relationship Atlas v3")
    require("\t" not in text, "tab escape remains in Relationship Atlas v3")
    print("Relationship Atlas v3 theorem audit passed")


if __name__ == "__main__":
    main()
