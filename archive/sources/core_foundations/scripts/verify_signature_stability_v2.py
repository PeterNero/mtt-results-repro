from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = (
    ROOT
    / "revised_tex_vnext"
    / "Lorentzian_Base_Compatibility_and_Signature_Stability_in_the_MTT_Fixed_Point_Realization_v2"
)
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
    require(TEX.exists(), "Signature Stability v2 main.tex missing")
    require((PROJECT / "series.sty").exists(), "series.sty missing")
    text = TEX.read_text(encoding="utf-8")
    check_environments(text)

    required = [
        "Positive Gram obstruction",
        "cannot be a Lorentzian metric",
        "additional signature\ndata and must be selected and justified independently",
        "globally hyperbolic Lorentzian base",
        "stabilization parameter $\\tau$ is not automatically physical time $t$",
        "Principal symbols and physical signature",
        "Quadratic hyperbolicity criterion",
        "if and only if\nits inertia is $(1,d-1)$ or $(d-1,1)$",
        "Euclidean metric symbol",
        "Multi-time metric symbols",
        "conditional principal-symbol statement, not a universal no-go",
        "No selection of three spatial dimensions",
        "Hyperbolicity alone therefore does not select",
        "Uniform inertia stability",
        "Continuous signature change crosses degeneracy",
        "Principal-symbol descent",
        "inherits the already selected\nLorentzian characteristic cone",
        "This theorem proves descent, not emergence or selection",
        "Compatibility ledger",
        "Lorentzian compatibility and stability",
        "does not derive Lorentzian signature or $3+1$ dimensions",
    ]
    for item in required:
        require(item in text, f"required signature repair missing: {item}")

    forbidden = [
        "Definition of effective signature",
        "When $K_{\\mu\\nu}$ is nondegenerate, the effective signature",
        "Exclusion of Euclidean and $(2+2)$ signatures",
        "Why $(3+1)$ survives",
        "$(3+1)$ is conditionally inevitable",
        "Three spatial dimensions provide the minimal number",
        "Lorentzian signatures with more than three spatial dimensions are excluded",
        "positive-definite kinetic form therefore fails to encode",
        "No new assumptions are introduced",
        "selected as the minimal stable configuration",
        "results from the structural constraints of the theory",
    ]
    for item in forbidden:
        require(item not in text, f"withdrawn signature claim remains: {item}")

    require(all(ord(char) < 128 for char in text),
            "non-ASCII or mojibake remains in Signature Stability v2")
    require("\t" not in text, "tab escape remains in Signature Stability v2")
    print("Signature Stability v2 theorem audit passed")


if __name__ == "__main__":
    main()
