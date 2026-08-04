from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = (
    ROOT
    / "revised_tex_vnext"
    / "Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization_v2"
    / "main.tex"
)


def replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, lambda _: replacement, text, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return updated


def main() -> None:
    text = PAPER.read_text(encoding="utf-8")

    text = replace_once(
        text,
        r"\\title\{Theta Closure in Modal Triplet Theory III:.*?Normalization\}",
        r"""\title{Theta Closure in Modal Triplet Theory III:
Conditional Twistor--Action Matching and Normalization Audit}""",
        "title",
    )
    text = text.replace(r"\date{January 2026}", r"\date{July 2026}", 1)

    text = replace_once(
        text,
        r"\\begin\{abstract\}.*?\\end\{abstract\}",
        r"""\begin{abstract}
We audit a conditional Route~B representation of the leading--order nonabelian
overlap integrals $I_2^{(0)}$ and $I_3^{(0)}$ in Modal Triplet Theory (MTT)
using the self--dual Yang--Mills (SDYM) twistor corner. Fiber reduction gives
the same quadratic $L^2$ functional used by Route~A. The numerical
normalization is not independent, however: the $SU(2)$ result additionally
uses the bridge convention $dA_{\mathrm{dir}}=2\omega_{\mathrm{FS}}$ and the
effective round-$S^2$ lens model, while the $SU(3)$ result uses the selected
nilmanifold, color harmonic, and factorization assumption of Paper~II. Under
these declared shared inputs Route~B reproduces
$I_2^{(0)}=4\pi(f_2R_{\mathrm{lens}})^2$ and
$I_3^{(0)}=\int\|\chi_{\mathrm{col}}\|^2d\mu=c$. The result is therefore a
conditional representation-level cross-check, not an independent selection
of the overlap values or a completed nonabelian $\Theta$--closure theorem.
\end{abstract}""",
        "abstract",
    )

    text = replace_once(
        text,
        r"\\section\{Relation to Papers I and II\}.*?(?=\\section\{Introduction\})",
        r"""\section{Relation to Papers I and II}

This paper is the third component of the conservative $\Theta$--closure program:
\begin{itemize}
\item \textbf{Paper I} defines the selected common-scheme gauge profile and
the corresponding overlap-ratio targets.
\item \textbf{Paper II} realizes those targets in a calibrated effective
round-$S^2$/nilmanifold ansatz (Route~A).
\item \textbf{Paper III} tests whether the same quadratic overlap functional
is reproduced by the twistor--encoded gauge action (Route~B), and audits which
normalization inputs remain shared with Route~A.
\end{itemize}

Agreement between Routes~A and~B is a conditional internal consistency check.
It is not statistically or logically independent evidence when the routes
share the internal metric, harmonic, normalization bridge, or target profile.

""",
        "relation section",
    )

    text = replace_once(
        text,
        r"\\section\{Introduction\}.*?(?=\\section\{Twistor corner and SDYM action\})",
        r"""\section{Introduction}

Modal Triplet Theory (MTT) proposes that observable four--dimensional physics
arises from a coherent projection of a higher--dimensional modal configuration
space. In this framework, inverse squared gauge couplings are represented by
overlap integrals of internal harmonic representatives. Whether the values of
those integrals are selected by MTT geometry or calibrated to an observed
profile is a separate theorem question.

Paper~I transports the measured Standard Model gauge profile in a common
scheme to $Q=M_t=172.5590883453979~\mathrm{GeV}$. Paper~II maps the resulting
ratios into a leading effective geometry on
$S^1_{\mathrm{cen}}\times L(3,1)\times\Gamma\backslash\mathrm{Nil}_3$; its
round-$S^2$ lens base and nilmanifold parameters constitute a calibrated
ansatz-level realization, not a unique geometry selection.

The purpose of this paper is to determine precisely what the twistor--action
construction (Route~B) adds. Unlike Route~A, it represents the quadratic gauge
norm through fiber reduction of an SDYM action. It does not, by itself, select
the map from the Fubini--Study form to the effective lens area, the internal
color fiber, or the color harmonic. Those bridges are stated as assumptions
rather than hidden inside a claim of independent normalization.

We show that:
\begin{itemize}
\item twistor fiber reduction produces a quadratic $L^2$ norm of the massless
representative;
\item the declared direction-sphere bridge recovers the $4\pi$ coefficient
used by the effective $SU(2)$ lens-base model;
\item the selected color factorization reproduces the nilmanifold $SU(3)$
overlap functional; and
\item numerical equality with Route~A is conditional on these shared inputs,
while a quantitative bound on omitted coherence corrections remains open.
\end{itemize}

The result is a representation-level compatibility theorem, not an
independent value source or a completed nonabelian $\Theta$--closure theorem.

""",
        "introduction",
    )

    text = text.replace(
        "This normalization fixes the fiber measure uniquely and removes any overall\nconstant ambiguity in the twistor action.",
        "This convention fixes the fiber measure once chosen. It does not by itself\nfix the relative normalization between $g_{\\mathrm{tw}}$, $g_{10}$, and the\ninternal MTT overlap.",
        1,
    )
    text = text.replace(
        r"\begin{theorem}[Route~B SU(2) overlap normalization]",
        r"\begin{theorem}[Conditional Route~B $SU(2)$ normalization]",
        1,
    )
    text = text.replace(
        "For the $SU(2)$ gauge sector, the twistor--action formulation fixes the\nleading--order overlap uniquely as",
        "Assume the SDYM fiber reduction, the coupling identification, and the\ndirection-sphere bridge $dA_{\\mathrm{dir}}=2\\omega_{\\mathrm{FS}}$. For the\n$SU(2)$ gauge sector the resulting leading--order overlap is",
        1,
    )
    text = text.replace(
        "independently of the internal spectral bounds used in Route~A.",
        "without using the internal Laplacian bound. The metric scale and the\ndirection-sphere bridge are nevertheless shared with the Route~A ansatz.",
        1,
    )
    text = text.replace(
        "This completes Route~B for the $SU(2)$ sector: the overlap normalization is\nderived entirely from twistor fiber geometry and the SDYM action, with no\nreference to the internal Laplacian or its eigenvalues.",
        "This gives an independent representation of the quadratic norm, but not an\nindependent numerical value source. The Fubini--Study normalization, coupling\nidentification, and effective lens metric remain declared bridge inputs.",
        1,
    )
    text = text.replace(
        "This factorization is canonical within the admissible slab and introduces no\nadditional physical assumptions.",
        "This factorization is an explicit Route~B assumption. The present paper does\nnot derive it, select the compact nilmanifold, or prove uniqueness of the color\nharmonic from the twistor action alone.",
        1,
    )
    text = text.replace(
        r"\begin{theorem}[Route~B $SU(3)$ overlap normalization]",
        r"\begin{theorem}[Conditional Route~B $SU(3)$ overlap identity]",
        1,
    )
    text = text.replace(
        "the twistor--action\nformulation fixes the leading--order overlap uniquely as",
        "the twistor--action\nreduction yields the conditional leading--order identity",
        1,
    )
    text = text.replace(
        "Together with the $SU(2)$ analysis, this completes Route~B for the massless\nnonabelian gauge sector at leading order. Corrections beyond this regime are\ncontrolled by the coherence gap and are of order $O(\\lambda_Q^{-1})$.",
        "Together with the $SU(2)$ analysis, this supplies a conditional Route~B\ncompatibility check for the massless nonabelian sector. The assumed asymptotic\norder $O(\\lambda_Q^{-1})$ is not yet accompanied here by a coefficient or\nuniform remainder bound and must not be read as a numerical error certificate.",
        1,
    )

    text = replace_once(
        text,
        r"\\section\{Consistency with \$\\Theta\$--targets\}.*?(?=\\section\{Scope and limitations\})",
        r"""\section{Consistency with the selected gauge profile}

Paper~I gives the selected common-scheme targets at
$Q=M_t=172.5590883453979~\mathrm{GeV}$:
\[
\frac{I_2}{I_1}=0.5110273(12),
\qquad
\frac{I_3}{I_1}=0.15834(11),
\qquad
I_1=2\pi R_1.
\]
The parenthesized uncertainties affect the final displayed digits. With the
leading identities used in Papers~II and~III, these imply
\[
(f_2R_{\mathrm{lens}})^2=0.2555137\,R_1,
\qquad
c=0.9948493\,R_1.
\]
The former $5~\mathrm{TeV}$ profile and the values $0.560$, $0.229$,
$0.280R_1$, and $1.439R_1$ are withdrawn.

\begin{theorem}[Conditional Route~A/Route~B agreement]
Assume the common coupling-overlap convention, the selected Paper~I profile,
the Paper~II effective internal ansatz, the SDYM fiber reduction, the
direction-sphere normalization bridge, and color--twistor factorization. Then
both routes evaluate the same leading quadratic functional and give
\[
I_2^{(0)}=4\pi(f_2R_{\mathrm{lens}})^2,
\qquad
I_3^{(0)}=c.
\]
Consequently both reproduce the displayed profile ratios.
\end{theorem}

\begin{proof}
Under the listed assumptions, both constructions evaluate the $L^2$ norm of
the same selected massless representative. Equality follows from the shared
normalization bridges. It is an exact round-trip identity within the selected
ansatz, not an independent derivation of the input profile or internal metric.
\end{proof}

\section{Dependency audit}

The Route~B comparison shares the following inputs with Papers~I and~II:
\begin{enumerate}
\item the measured common-scheme gauge profile and $I_1=2\pi R_1$ convention;
\item the relation $g_a^{-2}=g_{10}^{-2}I_a$ and its common normalization;
\item the effective round-$S^2$ lens-base metric and scale
$f_2R_{\mathrm{lens}}$;
\item the compact nilmanifold, its metric parameter $c$, and the chosen color
harmonic; and
\item the identification of the twistor fiber norm with the selected internal
overlap, including $dA_{\mathrm{dir}}=2\omega_{\mathrm{FS}}$.
\end{enumerate}
Route~B independently supplies only the twistor/SDYM representation of the
quadratic norm conditional on these bridges. A genuinely independent value
derivation would have to select the bridges and internal representatives from
twistor-corner MTT data without importing the Route~A realization.

""",
        "target and dependency sections",
    )

    text = replace_once(
        text,
        r"\\section\{Scope and limitations\}.*?(?=% ===========================\n\\appendix)",
        r"""\section{Scope and limitations}

This paper establishes conditional leading-order compatibility between two
representations of the nonabelian overlap functional. It does not establish:
\begin{itemize}
\item a source theorem selecting the gauge profile or internal geometry;
\item an independent $SU(2)$ or $SU(3)$ numerical normalization;
\item a coefficient-level bound for corrections denoted
$O(\lambda_Q^{-1})$;
\item Yukawa/flavor structure, ultraviolet completion, or string embedding.
\end{itemize}

\section{Conclusion}

The SDYM twistor reduction and the direct internal calculation can be placed
on the same quadratic $L^2$ footing. Once the shared normalization and geometry
bridges are declared, the two descriptions agree exactly at leading order and
reproduce the selected Paper~I overlap profile. This is a useful consistency
result because it checks that the twistor encoding does not alter the gauge
kinetic functional.

It is not a second independent determination of the numerical overlaps.
The $SU(2)$ coefficient uses the direction-sphere bridge and effective lens
metric; the $SU(3)$ identity uses the selected nilmanifold and color harmonic.
The strongest justified conclusion is therefore conditional
representation-level compatibility. Independent geometric selection and a
quantitative coherence-remainder estimate remain separate theorem targets.

""",
        "scope and conclusion",
    )

    text = text.replace(
        "Thus Route~B yields the same functional object as Route~A, but with the crucial advantage\nthat the overall constant is fixed by the twistor fiber normalization \\eqref{eq:FSnorm}.",
        "Thus Route~B yields the same functional form as Route~A after imposing the\nbridge between the twistor fiber norm and the internal overlap. The\nFubini--Study convention fixes a fiber measure, but does not alone determine\nthe relative coupling normalization or select the internal metric scale.",
        1,
    )
    text = text.replace(
        r"\begin{proposition}[Twistor-action normalization yields $\kappa_\ell=4\pi$]",
        r"\begin{proposition}[Conditional recovery of $\kappa_\ell=4\pi$]",
        1,
    )
    text = text.replace(
        "Let the SU(2) massless gauge mode be represented in the twistor corner by a constant\nfiber harmonic $\\psi^{(0)}$ normalized to $\\|\\psi^{(0)}\\|_{L^2(\\mathbb{CP}^1)}=1$ with respect\nto the Fubini--Study measure \\eqref{eq:FSnorm}. Then the induced MTT overlap for the\nSU(2) lens sector is",
        "Let the $SU(2)$ massless gauge mode be constant on the twistor fiber. In\naddition to \\eqref{eq:FSnorm}, assume the direction-sphere bridge\n$dA_{\\mathrm{dir}}=2\\omega_{\\mathrm{FS}}$ and scale that metric by\n$(f_2R_{\\mathrm{lens}})^2$. Then the induced MTT overlap is",
        1,
    )
    text = text.replace(
        "The twistor line $L_x\\cong\\mathbb{CP}^1$ parametrizes null directions and is naturally\nidentified with the unit two-sphere of directions.\nScaling the spatial metric by $(f_2R_{\\mathrm{lens}})^2$ scales the corresponding\ndirection-sphere area by $(f_2R_{\\mathrm{lens}})^2$.\nWith the canonical normalization \\eqref{eq:FSnorm}, the area of the unit sphere is $4\\pi$,\nhence the overlap is $4\\pi(f_2R_{\\mathrm{lens}})^2$.",
        "By the bridge assumption,\n$\\int_{L_x}dA_{\\mathrm{dir}}=2\\int_{L_x}\\omega_{\\mathrm{FS}}=4\\pi$.\nMetric scaling multiplies this area by $(f_2R_{\\mathrm{lens}})^2$,\nwhich gives the stated overlap. The factor of two is part of the explicit\nbridge and is not derived from \\eqref{eq:FSnorm} alone.",
        1,
    )
    text = text.replace(
        "This establishes the SU(2) overlap normalization entirely within Route~B.",
        "This recovers the Route~A coefficient conditionally; it does not select the\ndirection-sphere bridge or lens scale entirely within Route~B.",
        1,
    )
    text = text.replace(
        "the same fiber normalization argument \\eqref{eq:fiber_identity} applies and fixes the\noverall coefficient. In particular, if the SU(3) massless harmonic is chosen as a unit",
        "the same fiber reduction \\eqref{eq:fiber_identity} applies after the relative\ncoupling normalization is declared. In particular, if the $SU(3)$ massless harmonic is chosen as a unit",
        1,
    )
    text = text.replace(
        "This is a clean follow-up\nderivation and does not require modifying Papers~I or~II.",
        "Until those steps are supplied, the $SU(3)$ result is a conditional\ncross-check and not an independent normalization theorem.",
        1,
    )

    PAPER.write_text(text, encoding="utf-8", newline="\n")
    print(f"Updated {PAPER}")


if __name__ == "__main__":
    main()
