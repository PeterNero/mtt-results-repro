from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = (
    ROOT
    / "revised_tex_vnext"
    / "Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale_v2"
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
        r"\\title\{Theta Closure in Modal Triplet Theory IV:.*?Closure Scale\}",
        r"""\title{Theta Closure in Modal Triplet Theory IV:
Conditional Gravity Scaling and Cosmological Cutoff Audit}""",
        "title",
    )
    text = text.replace(r"\date{January 2026}", r"\date{July 2026}", 1)
    text = replace_once(
        text,
        r"\\begin\{abstract\}.*?\\end\{abstract\}",
        r"""\begin{abstract}
We re-evaluate the propagation of the gauge-profile geometry into gravity and
cosmology. Within the effective product ansatz of Papers~I--III, the updated
dimensionless internal-volume coefficient is
$\widehat V_{\mathrm{int}}=20.07064R_1^3$. Restoring the common internal length
$\ell_{\mathrm{int}}$ gives
$G_N^{-1}=20.07064\ell_{\mathrm{int}}^6R_1^3/G_{10}$; hence the gauge profile
does not determine Newton's constant without an absolute-scale and fundamental
gravity normalization. The former identification
$\Lambda_\Theta\sim5~\mathrm{TeV}$ is withdrawn with the obsolete gauge
crossing, so its numerical primordial-tensor bound is also withdrawn. We retain
the correctly normalized conditional relation
$r\leq 2\epsilon^2(\Lambda_\Theta/M_{\mathrm{Pl}})^2/(\pi^2A_s)$ when
$H\leq\epsilon\Lambda_\Theta$. The paper therefore supplies conditional
scaling laws and an assumption audit, not cross-sector numerical closure.
\end{abstract}""",
        "abstract",
    )

    text = replace_once(
        text,
        r"\\section\{Introduction\}.*?(?=% ===========================\n\\section\{Propagation of \$\\Theta\$ to Newton's constant\})",
        r"""\section{Introduction}

Papers~I--III now establish a selected common-scheme gauge profile, a
calibrated leading geometric realization, and a conditional twistor
representation check. They do not select an absolute internal length, a
fundamental ten-dimensional gravitational coupling, or a cosmological
coherence cutoff. This distinction controls what can be transported into the
gravity and cosmology sectors.

This paper asks two scoped questions. First, what dimensionless internal-volume
coefficient follows if the effective round-$S^2$/nilmanifold product ansatz is
used? Second, what tensor inequality follows if a separately selected
coherence cutoff bounds the Hubble scale? The answers are conditional scaling
relations. They must not be promoted into predictions of $G_N$ or $r$ until
the missing absolute-scale and cutoff source theorems are supplied.


% ===========================
""",
        "introduction",
    )

    text = text.replace(
        "In this section we show how the same $\\Theta$ fixed by the gauge sector in\nPapers~I--III propagates into the gravitational sector, yielding a concrete\nrelation for Newton's constant.\nNo new parameters are introduced beyond those already fixed by $\\Theta$.",
        "We compute the gravity scaling implied by the selected effective product\nansatz. The calculation introduces no retuning of the dimensionless profile,\nbut it retains the independent absolute length $\\ell_{\\mathrm{int}}$ and\nfundamental coupling $G_{10}$.",
        1,
    )
    text = text.replace(
        "Equation \\eqref{eq:GN_reduction} is structural and does not depend on the details\nof the Standard Model sector.",
        "Equation \\eqref{eq:GN_reduction} is the standard dimensional-reduction\nform assumed here. Its applicability to MTT requires the product metric,\nEinstein-frame convention, and absence or control of warp/dilaton corrections.",
        1,
    )
    text = text.replace(
        "The internal volume therefore factorizes as",
        "After factoring out a common physical length $\\ell_{\\mathrm{int}}$,\nwrite the remaining radii and metric parameters as dimensionless quantities.\nUnder the unwarped product ansatz the physical internal volume factorizes as",
        1,
    )
    text = text.replace(
        "(2\\pi R_1)\\;\n\\mathrm{Area}(\\Sigma_2)\\;\n\\mathrm{Vol}(\\Sigma_3).",
        "\\ell_{\\mathrm{int}}^6(2\\pi R_1)\\;\n\\widehat{\\mathrm{Area}}(\\Sigma_2)\\;\n\\widehat{\\mathrm{Vol}}(\\Sigma_3).",
        1,
    )

    text = replace_once(
        text,
        r"\\subsection\{Insertion of \$\\Theta\$--fixed geometric data\}.*?(?=% ===========================\n\\section\{Propagation of \$\\Theta\$ to a cosmological tensor bound\})",
        r"""\subsection{Insertion of the selected gauge-profile geometry}

Paper~II's calibrated leading ansatz gives the dimensionless relations
\begin{align}
\widehat{\mathrm{Area}}(\Sigma_2)
&=4\pi(f_2R_{\mathrm{lens}})^2
=4\pi(0.2555137R_1),\\
\widehat{\mathrm{Vol}}(\Sigma_3)&=c=0.9948493R_1,
\qquad (a=b=1).
\end{align}
These are profile-realization data, not an independent gravity-sector
selection. Substitution gives
\begin{align}
\widehat V_{\mathrm{int}}
&=(2\pi R_1)\,[4\pi(0.2555137R_1)]\,(0.9948493R_1)\\
&=20.0706400R_1^3,
\end{align}
and therefore
\begin{equation}
\boxed{\mathrm{Vol}(X_{\mathrm{int}})
=20.0706400\,\ell_{\mathrm{int}}^6R_1^3.}
\label{eq:volume_result}
\end{equation}

\subsection{Conditional expression for $G_N$}

Under the dimensional-reduction assumptions,
\begin{equation}
\boxed{\frac{1}{G_N}
=\frac{20.0706400\,\ell_{\mathrm{int}}^6R_1^3}{G_{10}}.}
\label{eq:GN_theta}
\end{equation}
The gauge profile fixes only the displayed dimensionless shape coefficient
within the chosen ansatz. It does not fix $\ell_{\mathrm{int}}^6/G_{10}$, nor
does this paper derive the reduction formula from the selected MTT action.
Thus no numerical prediction of Newton's constant follows.


% ===========================
""",
        "gravity evaluation",
    )

    text = replace_once(
        text,
        r"\\section\{Propagation of \$\\Theta\$ to a cosmological tensor bound\}.*?(?=% ===========================\n\\section\{Observational status and falsifiability\})",
        r"""\section{Conditional cosmological cutoff relation}
% ===========================

The old gauge crossing did not select a physical coherence cutoff. In
particular, the former assignment $\Lambda_\Theta\sim5~\mathrm{TeV}$ and the
scan $[3,10]~\mathrm{TeV}$ are withdrawn. The current gauge matching point
$Q=M_t$ is a renormalization convention and must not be identified with
$\Lambda_\Theta$.

Let a future source theorem select a physical cutoff $\Lambda_\Theta$, and
suppose the relevant cosmological solution satisfies the quantitative
admissibility condition
\begin{equation}
H\leq\epsilon\Lambda_\Theta,
\qquad 0<\epsilon<1.
\label{eq:admissibility_H}
\end{equation}
For vacuum tensor fluctuations in standard slow-roll normalization,
\begin{equation}
P_t=\frac{2H^2}{\pi^2M_{\mathrm{Pl}}^2},
\qquad r=\frac{P_t}{A_s}.
\end{equation}
Consequently,
\begin{equation}
\boxed{r\leq
\frac{2\epsilon^2}{\pi^2A_s}
\left(\frac{\Lambda_\Theta}{M_{\mathrm{Pl}}}\right)^2.}
\label{eq:r_bound_general}
\end{equation}
This corrects the legacy formula, which omitted the factor
$2/(\pi^2A_s)$. Equation~\eqref{eq:r_bound_general} remains conditional on the
tensor-production model as well as on independently selected values of
$\Lambda_\Theta$ and $\epsilon$. It supplies no current numerical bound.


% ===========================
""",
        "cosmology relation",
    )

    text = replace_once(
        text,
        r"\\section\{Observational status and falsifiability\}.*?(?=% ===========================\n\\section\{Conclusion\})",
        r"""\section{Status and falsifiability}
% ===========================

The conditional relation~\eqref{eq:r_bound_general} can become falsifiable
only after MTT independently selects a cutoff, an admissibility margin, and a
cosmological production law. A measured tensor amplitude could then test that
joint hypothesis. Without those selections, neither detection nor
non-detection of primordial tensors presently falsifies the gauge-profile
closure program. The withdrawn $10^{-30}$--$10^{-29}$ interval must not be
quoted as an MTT prediction.


% ===========================
""",
        "status section",
    )

    text = replace_once(
        text,
        r"\\section\{Conclusion\}.*?(?=% ===========================\n\\section\*\{References\})",
        r"""\section{Conclusion}
% ===========================

Within the selected effective product ansatz, the updated gauge profile fixes
the dimensionless internal-volume coefficient to
$20.0706400R_1^3$. Restoring dimensions shows explicitly why this is not yet a
prediction of Newton's constant: the independent combination
$\ell_{\mathrm{int}}^6/G_{10}$ remains.

The cosmological result is likewise a conditional scaling law. The obsolete
few-TeV gauge crossing cannot serve as a physical coherence cutoff, and the
legacy numerical tensor bound is withdrawn. A future closure theorem must
select $\Lambda_\Theta$, the quantitative margin $\epsilon$, and the applicable
cosmological state before Equation~\eqref{eq:r_bound_general} becomes a
numerical prediction. Paper~IV therefore documents cross-sector dependencies
and correct formulas; it does not establish gravity or cosmology closure.


% ===========================
""",
        "conclusion",
    )

    PAPER.write_text(text, encoding="utf-8", newline="\n")
    print(f"Updated {PAPER}")


if __name__ == "__main__":
    main()
