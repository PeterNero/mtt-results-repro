from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "revised_tex_vnext" / "Fixed_Points_II__Fixed_Points_in_a_10D_Modal_Model_v3"
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
    require(TEX.exists(), "FP II v3 main.tex missing")
    require((PROJECT / "series.sty").exists(), "series.sty missing")
    require((PROJECT / "references.bib").exists(), "references.bib missing")
    text = TEX.read_text(encoding="utf-8")
    check_environments(text)

    required = [
        "Projected Fixed Points and Equilibria in a 10D Modal Model",
        "not counted as a seventh",
        "Strong commutation of vertical operators",
        "possibly overlapping or nested",
        "It is not the Lorentzian d'Alembertian",
        "stabilization parameters",
        "Projector commutation for the base-regularized model",
        "\\label{eq:Q-duhamel}",
        "No factor $e^{-\\lambda_{\\Aop}t}$ is asserted for $\\Pcoh w$",
        "Strict Lyapunov identity",
        "could be\na nonstationary periodic point",
        "Base zero mode",
        "q_{\\mathrm{coh}}(\\tau)",
        "$L^2$-closed",
        "No full-map decay from the fiber gap",
        "\\Xsix=T^2_1\\times T^2_2\\times T^2_3",
        "\\sum_{n=1}^3\\|A_n^{1/2}\\Psi\\|_{\\Ltwo}^{2}",
    ]
    for item in required:
        require(item in text, f"required FP II repair missing: {item}")

    forbidden = [
        "\\Xsix = S^1_{\\mathrm{cen}}\\times T^2_1\\times T^2_2\\times T^2_3",
        "M_1(\\tau)\\le C_0(1+\\tau^{-1/2})e^{-\\lambda_{\\Aop}\\tau}",
        "q(\\tau):=C_{\\Pi}M_1(\\tau)",
        "Projected fixed points are equilibria",
        "Assume $\\varepsilon>0$ and $-\\Delta_Y$ has a spectral gap",
        "three parallel internal bundles",
    ]
    for item in forbidden:
        require(item not in text, f"obsolete FP II claim remains: {item}")

    print("Fixed Points II v3 theorem audit passed")


if __name__ == "__main__":
    main()
