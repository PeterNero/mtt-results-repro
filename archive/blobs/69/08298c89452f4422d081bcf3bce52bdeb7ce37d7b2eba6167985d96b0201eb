from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "revised_tex_vnext" / "Fixed_Points_I__Fixed_Points_over_Multi_Bundle_Manifolds_v6"
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
    require(TEX.exists(), "v6 main.tex missing")
    require((PROJECT / "series.sty").exists(), "series.sty missing")
    require((PROJECT / "refs.bib").exists(), "refs.bib missing")
    text = TEX.read_text(encoding="utf-8")
    check_environments(text)

    required = [
        "conditional functional-analytic framework",
        "Control geometry versus physical spacetime",
        "Scope of the fiber-product model",
        "Stabilization parameter",
        "maps bounded subsets of\n$L^2$ into bounded subsets of $H^{1+\\delta}",
        "Rellich embedding $H^{1+\\delta}\\hookrightarrow\\!\\hookrightarrow H^1$",
        "$L^2$-closed, bounded, convex",
        "because $\\PiCoh$ is an\n$L^2$-orthogonal projection",
        "V_\\varepsilon:=\\{w\\in H^1(\\Bint):W^{1/2}w\\in L^2\\}",
        "\\frac{1+L/w_0}{1-L/w_0}",
        "Uniqueness by itself does not imply an exponential rate",
        "sequentially demicontinuous",
        "\\varepsilon_j\\Delta_Y\\Psi_{\\varepsilon_j}$ tends to zero",
    ]
    for item in required:
        require(item in text, f"required v6 repair missing: {item}")

    forbidden = [
        "A rigorous functional-analytic framework",
        "\\Phi_t: L^2\\to H^1$ is compact",
        "\\frac{1+L/\\sqrt{w_0}}",
        "Exponential rate under uniqueness",
    ]
    for item in forbidden:
        require(item not in text, f"obsolete v5 claim remains: {item}")

    print("Fixed Points I v6 theorem audit passed")


if __name__ == "__main__":
    main()
