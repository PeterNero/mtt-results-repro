from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = (
    ROOT
    / "revised_tex_vnext"
    / "The_Projection__Admissibility_Principle__Descent__Recovery__and_Structural_Constraints_v2"
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
    require(TEX.exists(), "Projection-Admissibility v2 main.tex missing")
    require((PROJECT / "series.sty").exists(), "series.sty missing")
    text = TEX.read_text(encoding="utf-8")
    check_environments(text)

    required = [
        "That statement is false",
        "r\\circ s=\\operatorname{id}_{\\mathbb R}",
        "Representative section",
        "Exact upper decoder",
        "D_t:T_t(A)\\to A",
        "Autonomous reduced evolution",
        "Effective merger",
        "Projection--descent and recovery",
        "Noninjectivity does not obstruct representative selection",
        "Surjectivity is the set-theoretic gate for a right section",
        "Finite-diameter contraction obstruction",
        "This theorem concerns a reduced self-map",
        "additive-error inequality is not a Banach contraction",
        "Section-conditioning diagnostic",
        "Admissibility without automatic selection",
        "Measure-dependent reduced kernel",
        "Different upper measures",
        "does not by itself establish an arrow of",
        "Fixed-point locality descent",
        "This theorem does not imply state factorization",
        "representative section. It is not an\nexact decoder",
        "Horizon area or entropy is not obtained from",
        "Scoped principle",
        "No probability rule, entropy production, arrow of time, universality class",
        "\\quad c\\varepsilon\\ge0",
    ]
    for item in required:
        require(item in text, f"required replacement missing: {item}")

    forbidden = [
        "Necessity of Noninjectivity",
        "Generic Finiteness of Admissibility",
        "Projection--Admissibility Obstruction",
        "Probability from Degeneracy",
        "Arrow of Time from Admissibility Loss",
        "Information Loss from Admissibility Exhaustion",
        "probability as a consequence of noninjective projection",
        "probability emerges at the effective level",
        "fully constructive realization",
        "derives rigorously",
        "no global right inverse of the effective evolution exists",
        "Entropy associated with horizons is naturally interpreted",
        ",quad c\\varepsilon",
    ]
    for item in forbidden:
        require(item not in text, f"withdrawn claim remains: {item}")

    require(all(ord(char) < 128 for char in text),
            "non-ASCII or mojibake remains in Projection-Admissibility v2")
    require("\t" not in text, "tab escape remains in Projection-Admissibility v2")
    print("Projection-Admissibility v2 theorem audit passed")


if __name__ == "__main__":
    main()
