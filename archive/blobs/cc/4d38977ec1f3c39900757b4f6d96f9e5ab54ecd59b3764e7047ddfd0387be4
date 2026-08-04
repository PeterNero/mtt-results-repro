from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "revised_tex_vnext" / "Coherent_Kinematics_in_Modal_Triplet_Theory_v2"
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
    require(TEX.exists(), "Coherent Kinematics v2 main.tex missing")
    require((PROJECT / "series.sty").exists(), "series.sty missing")
    text = TEX.read_text(encoding="utf-8")
    check_environments(text)

    required = [
        "encoding-level construction",
        "Chart ordering alone is not a causal order",
        "Three levels of kinematic statement",
        "Compatible chart family",
        "constant on the $r_\\alpha$ fibers",
        "No exclusion principle follows from support\ncoincidence alone",
        "Chart-relative position",
        "Chart-persistent encoding trajectory",
        "Encoding worldline equivalence",
        "Gluing of encoding trajectories",
        "not necessarily to a unique upper path",
        "Regularity requires more than contraction",
        "Regular encoding trajectory",
        "By itself it proves neither continuity",
        "Bridge to physical spacetime motion",
        "Physical causal class",
        "Conditional finite propagation",
        "not proved by\nadmissibility, contractivity, or a partial order of charts",
        "Chart order is not causal order",
        "does not prove physical\ncoalescence",
        "cannot by\nitself encode a split",
        "event horizon in a regular globally hyperbolic spacetime does not generally",
        "No global-right-inverse obstruction follows from noninjectivity alone",
        "physical locality and null/timelike classes come from the selected",
        "Encoding kinematics with a physical bridge",
        "The first conclusion is encoding kinematics",
    ]
    for item in required:
        require(item in text, f"required kinematics repair missing: {item}")

    forbidden = [
        "X \\;\\sim\\; Y_4 \\times B_1 \\times B_2 \\times B_3",
        "Continuity from contractivity",
        "Null coherent structures",
        "Timelike coherent structures",
        "No superluminal motion",
        "Universality of characteristic classification",
        "Termination at merge",
        "Bifurcation at split",
        "kinematic histories defined by chart persistence possess an intrinsic arrow",
        "absence of a global section selecting",
        "horizons mark the boundary beyond which worldlines cannot be extended",
        "exclusion principles arise",
        "Photonic coherent structures provide the canonical example",
        "This universality explains why disparate effective theories share",
    ]
    for item in forbidden:
        require(item not in text, f"withdrawn kinematics claim remains: {item}")

    require(text.count(r"\end{document}") == 1,
            "Coherent Kinematics v2 must have exactly one end{document}")
    require(all(ord(char) < 128 for char in text),
            "non-ASCII or mojibake remains in Coherent Kinematics v2")
    require("\t" not in text, "tab escape remains in Coherent Kinematics v2")
    print("Coherent Kinematics v2 theorem audit passed")


if __name__ == "__main__":
    main()
