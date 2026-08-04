from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "revised_tex_vnext" / "Fixed_Points_VI__Formal_Synthesis_and_Physical_Interpretations_v4"
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
    require(TEX.exists(), "FP VI v4 main.tex missing")
    require((PROJECT / "series.sty").exists(), "series.sty missing")
    text = TEX.read_text(encoding="utf-8")
    check_environments(text)

    required = [
        "Inherited theorem.",
        "Conditional completion.",
        "Physical interpretation.",
        "A product of three\nbundle projectors is permitted only when those projectors strongly commute",
        "Circle--lens--nil labels",
        "trace, trace-zero, and reused-full carrier lanes",
        "not identified with the\nq79/Fu--Yau compactification",
        "Corrected fixed-point chain",
        "projected time-step\nfixed point is not automatically a steady solution",
        "Conditional contraction uniqueness",
        "different units and cannot be represented\nby one shared disturbance threshold",
        "Q\\mathcal RP",
        "first-order\nmodulation equation",
        "does not establish merger",
        "A\\Sigma+\\Sigma A^\\top+Q=0",
        "Semigroup covariance and resolvent bounds",
        "For a nonnormal matrix, the spectral abscissa alone does not imply",
        "Classical positivity of $\\Sigma$ does not\nimply this inequality",
        "exact exit diagnostic for the declared constraints",
        "Status of a Lorentzian master action",
        "do not by themselves prove three gauge factors",
        "Instantaneous bilocal obstruction",
        "does not establish microcausality",
        "Local-mediator completion",
        "Not derived by this series.",
        "Scoped FP synthesis",
    ]
    for item in required:
        require(item in text, f"required FP VI repair missing: {item}")

    forbidden = [
        "\\Pcoh(y):=\\Pi_1(y)\\Pi_2(y)\\Pi_3(y)",
        "A\\Sigma+\\Sigma A^\\top = Q",
        "\\|A^{-1}\\|\\le \\frac1{\\gap(A)}",
        "a merge into a single structure is permitted",
        "positive bias grows overlap",
        "measurement-like irreversibility",
        "\\gamma_a(X) \\ge \\delta_a(X)",
        "\\Phi_{\\mathrm{crit}} := \\sup",
        "\\begin{proposition}[Microcausality]",
        "s>2",
        "No equations, fixed-point theorems, stability results, or physical conclusions have been altered",
        "constructed from the nil, lens, and shared-circle data",
    ]
    for item in forbidden:
        require(item not in text, f"superseded FP VI claim remains: {item}")

    require("â" not in text, "mojibake remains in FP VI v4")
    print("Fixed Points VI v4 theorem audit passed")


if __name__ == "__main__":
    main()
