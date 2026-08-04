from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "revised_tex_vnext" / "Fixed_Points_IV__Curvature__Centroid_Motion__and_Structural_Transitions_on_Bundle_Manifolds_v4"
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
    require(TEX.exists(), "FP IV v4 main.tex missing")
    require((PROJECT / "series.sty").exists(), "series.sty missing")
    require((PROJECT / "refs.bib").exists(), "refs.bib missing")
    text = TEX.read_text(encoding="utf-8")
    check_environments(text)

    required = [
        "L=\\nabla^\\ast\\nabla+\\mathcal R",
        "Bounded-curvature cluster persistence",
        "curved Riesz projector",
        "Q\\mathcal RP",
        "Noncoherent leakage bound",
        "Karcher centroid",
        "First-order modulation law",
        "does not follow from the FP first-order gradient flow",
        "Signed interaction criterion",
        "It does not\nyield positive constants $c_1,c_2$",
        "Energy-barrier exclusion with work",
        "Exit does not determine selection",
    ]
    for item in required:
        require(item in text, f"required FP IV repair missing: {item}")

    forbidden = [
        "D = \\Delta + \\mathcal R",
        "Large overlap therefore favors merging",
        "M_{\\mathrm{eff}}\\,\\ddot X",
    ]
    for item in forbidden:
        require(item not in text, f"superseded FP IV claim remains: {item}")

    print("Fixed Points IV v4 theorem audit passed")


if __name__ == "__main__":
    main()
