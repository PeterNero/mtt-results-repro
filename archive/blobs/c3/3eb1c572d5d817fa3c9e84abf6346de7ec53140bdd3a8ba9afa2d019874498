from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "revised_tex_vnext" / "Fixed_Points_V__Curvature_Coupling__Multi_Structure_Dynamics_and_Drivers_v6"
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
    require(TEX.exists(), "FP V v6 main.tex missing")
    require((PROJECT / "series.sty").exists(), "series.sty missing")
    text = TEX.read_text(encoding="utf-8")
    check_environments(text)

    required = [
        "L_x=\\nabla_x^\\ast\\nabla_x+\\mathcal R_x",
        "joint spectral label, including multiplicity",
        "Exact scalar OU variance",
        "Stationary covariance",
        "Cross-covariance bound",
        "smallest positive eigenvalues",
        "Damping bound for canonical correlation",
        "Admissible domains and deficit score",
        "not a\nphysical energy, selection potential, or infinite enforcement cost",
        "A merely Lipschitz nonlinear function of a Gaussian process is not generally",
        "Finite-grid exit bound",
        "Continuous-time Gaussian exit bound",
        "Fixed-time simultaneous-exit bound",
        "No propagation theorem from covariance alone",
        "neither supplies a\nforce causing the exit nor selects the state or basin after exit",
    ]
    for item in required:
        require(item in text, f"required FP V repair missing: {item}")

    forbidden = [
        "\\deltaNW",
        "\\delta_n^{(\\omega)}",
        "globally hyperbolic Lorentzian manifold",
        "Divergence of $\\Phisel$ corresponds to infinite energetic cost",
        "Probabilistic censorship of nonadmissible behaviour",
        "loss of admissibility on a finite slab is\na non--generic event",
        "\\sqrt{\\|\\Sigma_A\\|\\|\\Sigma_B\\|}",
    ]
    for item in forbidden:
        require(item not in text, f"superseded FP V claim remains: {item}")

    print("Fixed Points V v6 theorem audit passed")


if __name__ == "__main__":
    main()
