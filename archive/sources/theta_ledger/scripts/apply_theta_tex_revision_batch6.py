from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = (
    ROOT
    / "revised_tex_vnext"
    / "Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v3"
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
        r"\\title\{Execution of Modal Triplet Theory I:.*?Threshold Sectors\}",
        r"""\title{Execution of Modal Triplet Theory I:
Gauge, HYM, Threshold, and Axion Status after True-SM Closure}""",
        "title",
    )
    text = text.replace(r"\date{January 2026}", r"\date{July 2026}", 1)
    body = r"""\begin{abstract}
We replace the obsolete few-TeV Calabi--Yau benchmark with the current audited
execution status of the MTT gauge, Hermitian Yang--Mills (HYM), threshold, and
axion sectors. The selected gauge profile is transported by SMDR~v1.3 to
$Q=M_t$ and enters an eight-row positive-definite precision object. Embedded
renormalized-Standard-Model equivalence closes at the adopted
one-shared-physical-primitive/profile standard. On the selected
$q79/F/m1$ rank-two bundle, the literal Cech--HYM witness closes, including the
finite cocycle and continuum tail certificates. The internal
$K_{\mathrm{threshold}}$ response ledger also closes, but physical
threshold/mass rows remain admitted profile data rather than strict MTT-emitted
values. The old fitted Kahler moduli, exceptional-cycle thresholds, and axion
normalizations are withdrawn. Strong CP remains open because the complete
$E_6$ color anomaly cancels and no selected flux/threshold axion-current map
has yet supplied a nonzero effective anomaly.
\end{abstract}

\section{Status standard and authority}

This paper reports two distinct closure standards:
\begin{enumerate}
\item \textbf{Adopted profile standard.} MTT embeds the renormalized Standard
Model on the selected branch, with one shared physical primitive and measured
common-scheme profile rows. The final audit closes 12/12 obligations.
\item \textbf{Strict source standard.} Every numerical value must be emitted
from selected MTT source geometry without empirical profile rows. This stronger
zero-primitive/no-knob standard remains open.
\end{enumerate}
The distinction is essential: closure at the first standard must not be
described as closure at the second.

The old Tier-3/Tier-4 calculation used a gauge crossing near $5~\mathrm{TeV}$
to fit Kahler ratios, thresholds, and axion data. That crossing is withdrawn.
None of its downstream numerical geometry is retained as current authority.

\section{Selected gauge and precision execution}

The selected common-scheme point is
\[
Q=M_t=172.5590883453979~\mathrm{GeV}.
\]
The gauge rows are
\begin{align}
g_Y&=0.3585945042\pm0.0000307251,\\
g_2&=0.6475986708\pm0.0000287665,\\
g_3&=1.163427409\pm0.004036156,
\end{align}
with $g_1=\sqrt{5/3}\,g_Y$ when GUT normalization is required. These are
measured-profile coordinates transported by the selected multi-loop Standard
Model pipeline; they are not first-principles MTT predictions.

The full selected precision map transports 15 common source coordinates into
eight $\overline{\mathrm{MS}}$ output rows. Its covariance is positive definite,
contains all 36 symmetric entries, and contains all 15 BCT--WZH cross-block
entries. The declared reproducible baseline is the diagonal measured-input
profile because no public official joint likelihood for all 15 coordinates was
identified.

\section{HYM and bundle execution}

The selected literal bundle result is stronger than the legacy string-lift
ansatz. On the selected $q79/F/m1$ rank-two bundle:
\begin{itemize}
\item the finite Cech witness contains 81 table entries and all 729 cocycle
triples;
\item the projected HYM solution has residual $8.21\times10^{-13}$,
coercivity margin $26.02$, and error indicator $3.15\times10^{-14}$; and
\item the weighted-theta Fourier-tail/Wiener certificate has
$Z=0.38508$ and $Y+Zr=0.00932703<r=0.01$.
\end{itemize}
Together these close the selected rank-two literal Cech--HYM witness families
2/2, including continuum existence and local uniqueness in the certified
ball. They do not prove uniqueness over all HYM branches or rank-three
sector/operator transfer.

\section{Threshold execution}

Two threshold layers must be kept separate.

\subsection{Internal response layer}

The selected internal $K_{\mathrm{threshold}}$ ledger closes 10/10. The direct
$K_{\mathrm{threshold}}.\Omega_H.\lambda$ row is locked, and the charged
$K$-to-$\Omega$ construction is available through the selected source rule
\[
\Omega_i^{\mathrm{src}}
=D_{\mathrm{fin}}[\mathrm{class}(i)]\,
K_{\mathrm{threshold}}.\Omega_i\,e^{-2\pi n_i}.
\]
This is a closure statement about the finite internal response machinery.

\subsection{Physical matching layer}

Seven physical threshold rows and three mass-scheme rows are closed only at the
admitted-external/profile tier. Their strict MTT-emitted value count remains
zero. The selected multi-loop transport and covariance therefore make the
profile execution reproducible, but they do not convert measured matching rows
into source-derived constants.

The legacy one-loop bulk logarithm, exceptional-cycle vector, and minimum-norm
threshold fit are withdrawn as numerical results. They may be retained only as
historical ansatz templates for a future source-selected compactification.

\section{Axion and strong-CP status}

The current corpus supports a conditional Peccei--Quinn mechanism and selected
axion decay-constant ratios. It does not select the absolute axion
normalization or solve strong CP.

For the complete $E_6$ $Q_\psi$ current, the exact color-anomaly audit gives
\[
\mathcal A_{\mathrm{matter}}=+12,
\qquad
\mathcal A_{\mathrm{complete\mbox{-}27\ exotics}}=-12,
\qquad
\mathcal A_{\mathrm{total}}=0.
\]
The matter-only/singlet diagnostic $N_{\mathrm{DW}}=3$ is not the anomaly of the
complete spectrum. A strong-CP theorem therefore requires a selected
flux/threshold decoupling and axion-current anomaly-matching map, followed by
quality and electric-dipole-moment control. That map remains open.

\section{Retired Calabi--Yau benchmark}

The former values $\zeta_2/\zeta_1\simeq0.560$,
$\zeta_3/\zeta_1\simeq0.229$, their derived Kahler ratios, the fitted internal
volume, exceptional-cycle coefficients, and corresponding axion decay
constants all depended on the withdrawn gauge profile. They are not updated by
substituting new ratios into the old formulas because topology, stability,
warping, normalization, and degeneracy were not independently selected.

A future geometric execution must publish:
\begin{enumerate}
\item the compactification topology, intersection form, bundle, flux and
stability chamber;
\item all priors, constraints, discrete branches, flat directions and
degeneracies;
\item the absolute-unit bridge and threshold scheme; and
\item a held-out comparison not used to select the geometry.
\end{enumerate}

\section{Conclusion}

Execution I now has a clean split. Gauge/precision profile execution, the
selected rank-two literal Cech--HYM witness, and the internal
$K_{\mathrm{threshold}}$ machinery are closed at their declared standards.
Physical threshold/mass values remain admitted profile rows, and the old
Calabi--Yau numerical lift is retired. Axion ratios and a conditional PQ lane
survive, while absolute normalization and strong-CP selection remain open.

The result supports embedded renormalized-SM equivalence at the adopted profile
standard. It does not establish a zero-knob compactification, derive the
measured gauge rows, or solve strong CP.

"""
    text = replace_once(
        text,
        r"\\begin\{abstract\}.*?(?=\\begin\{thebibliography\})",
        body,
        "body",
    )
    PAPER.write_text(text, encoding="utf-8", newline="\n")
    print(f"Updated {PAPER}")


if __name__ == "__main__":
    main()
