from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = (
    ROOT
    / "revised_tex_vnext"
    / "Baseline_Scales_and_Phenomenological_Consistency_in_Modal_Triplet_Theory_v2"
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
    require(TEX.exists(), "Baseline Scales v2 main.tex missing")
    require((PROJECT / "series.sty").exists(), "series.sty missing")
    text = TEX.read_text(encoding="utf-8")
    check_environments(text)

    required = [
        "scale and provenance ledger",
        "internal gap is an internal\nmass or truncation scale",
        "four-dimensional EFT cutoff",
        "makes no prediction and no assertion of present empirical viability",
        "A_{\\rm int}^{\\rm phys}=M_{\\rm int}^2\\widehat A_{\\rm int}",
        "They are not physical decay widths",
        "does not\nby itself:",
        "define a four-dimensional momentum cutoff",
        "\\|e^{\\tau L_{QQ}}\\|\\le M_Qe^{-\\omega_Q\\tau}",
        "It is independent of $\\lambda_\\ast^{\\rm int}$",
        "not definitionally equal to\n$m_\\ast^{\\rm int}$",
        "Conditional internal-mass bridge",
        "m_k^2=m_0^2+\\lambda_k",
        "External high-energy damping",
        "is not\navailable without an external damping construction",
        "does not imply this formula",
        "large internal gap alone is not a fifth-force certificate",
        "it is not itself a GW\nobservable",
        "Formal consistency set",
        "Consistency-witness criterion",
        "does not exhibit one viable model",
        "no fine tuning is required",
        "not evaluated by this ledger",
        "They may not cite it as proof that MTT satisfies experimental constraints",
        "not a universal cutoff or empirical shield",
    ]
    for item in required:
        require(item in text, f"required scale repair missing: {item}")

    forbidden = [
        "The spectral gap $\\lambda_\\ast$ plays the role of an effective cutoff scale",
        "higher-energy excitations are exponentially damped or integrated out",
        "fifth-force constraints are automatically satisfied",
        "all known\nparticle-physics constraints are satisfied",
        "radiative stability follows from controlled truncation",
        "classical tests of general relativity are satisfied automatically",
        "MTT predictions are\nconsistent with",
        "requires\nno additional scale input",
        "All observational constraints currently known can be satisfied",
        "requires no additional phenomenological assumptions to\nremain viable",
        "demonstrated that they can be chosen\nconsistently",
        "No circular dependence or fine-tuning among these scales is required",
    ]
    for item in forbidden:
        require(item not in text, f"withdrawn scale claim remains: {item}")

    require(all(ord(char) < 128 for char in text),
            "non-ASCII or mojibake remains in Baseline Scales v2")
    require("\t" not in text, "tab escape remains in Baseline Scales v2")
    print("Baseline Scales v2 theorem audit passed")


if __name__ == "__main__":
    main()
