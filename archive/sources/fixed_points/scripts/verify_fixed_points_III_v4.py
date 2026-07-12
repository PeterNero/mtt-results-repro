from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "revised_tex_vnext" / "Fixed_Points_III__Disturbance___Damping_Balance_and_Stability_v4"
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
    require(TEX.exists(), "FP III v4 main.tex missing")
    require((PROJECT / "series.sty").exists(), "series.sty missing")
    require((PROJECT / "refs.bib").exists(), "refs.bib missing")
    text = TEX.read_text(encoding="utf-8")
    check_environments(text)

    required = [
        "joint spectral decomposition",
        "multi-index $\\alpha$ includes all three spectral labels",
        "One-sided modal remainder bound",
        "deterministic amplitude $f_\\alpha$ and stochastic power $q_\\alpha$",
        "Deterministic input-to-state bound",
        "Stochastic second-moment bound",
        "Exact scalar OU classification",
        "Worst-case deterministic sign criterion",
        "\\Sigma_q:=",
        "\\Sigma_f:=",
        "No statement in this section controls a disturbance acting directly in",
        "Enhanced invariance principle",
        "\\int_0^\\infty\\bigl(R_x(s)+R_x(s)^\\ast\\bigr)\\,ds",
        "nonzero area anomaly",
        "A stochastic\ninvariant measure is not called a deterministic fixed point",
    ]
    for item in required:
        require(item in text, f"required FP III repair missing: {item}")

    require("2\\int_{0}^{\\infty}\\bigl(R_x(s)+R_x(s)^\\ast\\bigr)" not in text,
            "old doubled Green-Kubo tensor remains")
    require("\\delta_{n,k}" not in text, "old shared disturbance parameter remains")
    require("Neglecting $R$ (or under a smallness control)" not in text,
            "nonlinear-to-Gaussian bridge remains")
    require("Bundlewise $\\Leftrightarrow$ modewise" not in text,
            "old nonlinear equivalence claim remains")

    print("Fixed Points III v4 theorem audit passed")


if __name__ == "__main__":
    main()
