from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "revised_tex_vnext" / "Modal_Triplet_Theory__Foundation_v7"
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
    require(TEX.exists(), "Foundation v7 main.tex missing")
    require((PROJECT / "series.sty").exists(), "series.sty missing")
    text = TEX.read_text(encoding="utf-8")
    check_environments(text)

    required = [
        "dimension neutral",
        "M_{10}\\longrightarrow Y_4",
        "globally hyperbolic Lorentzian base",
        "not appended\nas a seventh independent product coordinate",
        "stabilization flow $R_\\tau$",
        "physical propagator $U(t_2,t_1)$",
        "renormalization or coarse-graining scale $\\mu$",
        "spectral measures strongly commute",
        "L_{QQ}=-\\kappa A_{\\rm int}|_{Q\\mathcal H}+B_Q",
        "nonnormal generator",
        "Independent logical gates",
        "Projected time-step existence",
        "Strict-Lyapunov equilibrium promotion",
        "The theorem does not apply without the invariant complete domain",
        "Schur--Feshbach reduction with domains",
        "Riesz-projector stability",
        "Basin-local fixed-point robustness",
        "Autonomous descent criterion",
        "Exact\nmicroscopic recovery would require",
        "hybrid dynamical system",
        "Complete admissibility-margin ledger",
        "They cannot acquire Lorentzian signature",
        "\\text{gauge blocks}",
        "Scoped MTT foundation",
    ]
    for item in required:
        require(item in text, f"required Foundation repair missing: {item}")

    forbidden = [
        "Under base-only warping of the internal geometry",
        "Base-only warping ensures",
        "Projected equilibrium",
        "Selection is not an additional dynamical term",
        "globally well-posed semiflow",
        "All results below persist up to",
        "fully rigorous foundational framework",
        "SA.3 $\\Rightarrow$ exponential decay",
        "B_1|_y \\simeq",
    ]
    for item in forbidden:
        require(item not in text, f"superseded Foundation claim remains: {item}")

    require(all(ord(char) < 128 for char in text),
            "non-ASCII or mojibake remains in Foundation v7")
    require("\t" not in text, "tab escape remains in Foundation v7")
    print("MTT Foundation v7 theorem audit passed")


if __name__ == "__main__":
    main()
