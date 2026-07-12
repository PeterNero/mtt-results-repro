from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "revised_tex_vnext" / "Superset_Determinations_in_Modal_Triplet_Theory_v3" / "main.tex"


def replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, lambda _: replacement, text, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return updated


def main() -> None:
    text = PAPER.read_text(encoding="utf-8")
    text = replace_once(text, r"\\title\{Superset Determinations in.*?Modal Triplet Theory \(MTT\)\}",
        r"\title{Superset Determinations in Modal Triplet Theory:\\Parameter Identifiability after True-SM Closure}", "title")
    text = text.replace(r"\date{January 2026}", r"\date{July 2026}", 1)
    body = r"""\begin{abstract}
We reformulate the MTT superset program as an audited parameter-identifiability
framework. The former one-loop gauge crossings, fitted $\zeta$ ratios,
minimum-norm threshold vector, common scale $K$, and claimed
$\alpha_s(M_Z)$ cross-prediction are withdrawn. Their inputs and scale choices
were not independent. The current authority instead closes embedded
renormalized-Standard-Model equivalence at a one-shared-physical-primitive,
measured-profile standard, using selected SMDR~v1.3 transport and a complete
eight-row covariance. We classify every output as structural theorem,
calibration, replay/profile coordinate, diagnostic, or held-out prediction.
This preserves the superset strategy as a rigorous tool for comparing
encodings while preventing fitted values from being promoted into source
theorems.
\end{abstract}

\section{Purpose of the superset program}

MTT can organize several effective encodings through shared carrier, projector,
bundle, overlap, and response data. The superset strategy is useful when it
asks which observables are jointly representable and which parameters are
identifiable from a declared input set. It is not, by itself, a method for
deriving measured constants.

We use five disjoint status classes:
\begin{enumerate}
\item \textbf{Structural theorem:} follows from selected mathematical data
without observed value selection.
\item \textbf{Calibration:} parameters are chosen to reproduce declared data.
\item \textbf{Profile/replay:} measured coordinates are transported through a
specified scheme or embedded action.
\item \textbf{Diagnostic:} a comparison tests consistency but was involved in
selection or fitting.
\item \textbf{Held-out prediction:} the compared observable was absent from
source selection, calibration, branch choice, and uncertainty construction.
\end{enumerate}

\section{Retirement of the legacy Tier-3 execution}

The former scales $\Lambda_{12}$ and $\Lambda_{23}$ were obtained from a
one-loop crossing exercise. The reported values near $4.2$--$5~\mathrm{TeV}$
were then used to extract $\zeta$ ratios, fit a common scale, choose a
minimum-norm threshold, and reconstruct $\alpha_s$. This chain is retired.

Specifically:
\begin{itemize}
\item a gauge crossing is not an MTT coherence or cutoff scale;
\item the old $0.560$ and $0.229$ ratios are not current profile values;
\item $K$ was calibrated with gravitational/electroweak information and was
not an independent prediction;
\item the minimum-norm threshold was a regularized fit selected by an external
norm, not a source theorem; and
\item $\alpha_s$ was not held out from the latent extraction and threshold
choices, so it was not a cross-prediction.
\end{itemize}

\section{Current common-scheme profile}

The selected numerical transport uses SMDR~v1.3 at
\[
Q=M_t=172.5590883453979~\mathrm{GeV}.
\]
Its gauge entries are
\[
g_Y=0.3585945042\pm0.0000307251,
\quad g_2=0.6475986708\pm0.0000287665,
\quad g_3=1.163427409\pm0.004036156.
\]
Fifteen locked source coordinates are transported into eight full-SM
$\overline{\mathrm{MS}}$ rows. The differentiated map emits a positive-definite
$8\times8$ covariance with all 36 symmetric entries and all 15 BCT--WZH
cross-block entries. These rows are profile transport, not MTT-derived
constants.

\section{Adopted closure and parameter count}

The final global audit closes 12/12 obligations for embedded renormalized-SM
equivalence at the adopted standard. The accounting is:
\begin{itemize}
\item one shared physical primitive $P_{\mathrm{EW}}$, counted once;
\item zero Higgs-specific adjustable parameters at the embedding layer;
\item measured threshold, mass-scheme, and magnitude/profile coordinates
retained explicitly as profile data; and
\item imported standard SM perturbative quantization and observable transport.
\end{itemize}
This is a more economical cross-sector representation than independently
retuning each sector, but it is not zero-input physics. Profile coordinates
must not be hidden when comparing parameter counts with the Standard Model.

The magnitude-bearing profile contains ten scalar labels: nine charged Yukawa
magnitudes and $\lambda_H$. At the strict internal source tier, accepted values
remain 0/10. Seven physical threshold and three mass-scheme rows are likewise
accepted at the admitted profile tier while strict internal emitted values
remain zero.

\section{Selected structural outputs}

The current superset contains genuine source-side structure independent of the
profile values, including:
\begin{itemize}
\item the locked 27-by-27 qutrit--Weyl/minimal matrix architecture;
\item the selected rank-two literal Cech--HYM witness, closed 2/2;
\item the internal $K_{\mathrm{threshold}}$ response ledger, closed 10/10;
\item the selected retarded $q79/F/m1$ orientation representative; and
\item the CKM $\Pi$ rows, closed at the prediction-with-uncertainty-profile
standard.
\end{itemize}
These achievements constrain how the measured profile can be embedded. They do
not automatically emit every profile magnitude.

\section{Strict-upgrade ledger}

Beyond the adopted baseline, nine stronger obligations are tracked:
\begin{center}
\begin{tabular}{cll}
\toprule
ID & Upgrade & Status \\
\midrule
U1 & zero-primitive empirical source & open \\
U2 & literal global Cech--HYM/QaSU3 & closed 2/2 \\
U3 & official joint input likelihood & partial \\
U4 & CKM prediction beyond source rows & closed at profile criterion \\
U5 & absolute neutrino mass and ontology & partial \\
U6 & strong-CP selection & partial \\
U7 & MTT-derived quantization & partial \\
U8 & constructive nonperturbative 4D QFT & partial \\
U9 & unique observed-branch selection & partial \\
\bottomrule
\end{tabular}
\end{center}
Closing U2 or U4 does not imply that the other seven upgrades close.

\section{Identifiability theorem}

\begin{theorem}[Profile-standard identifiability]
Given the selected branch, common-scheme profile, one shared electroweak
primitive, embedded SM action, and selected finite operator data, the accepted
observable rows are jointly reproducible with their declared covariance.
Removing the measured magnitude/threshold profile destroys numerical
identifiability of those rows because the current internal source inventory
emits no replacement scalar values.
\end{theorem}

\begin{proof}
The selected transport and embedding provide the forward map and covariance at
the profile standard. The strict source-row audits attempt all required scalar
slots and accept zero internal magnitude and physical threshold/mass values.
Therefore the profile rows are sufficient for the adopted forward execution
and presently necessary for its numerical values.
\end{proof}

\section{Rules for future superset calculations}

Every future execution must publish raw inputs, units, scheme and scale,
selection rules, fitted parameters, covariance, branch choices, code, and unit
tests. A claimed held-out prediction must include a data-separation certificate
showing that the observable was absent from all source and calibration paths.
No matching point, internal spectral gap, or gauge crossing may be promoted to
a physical cutoff without a separate source theorem.

\section{Conclusion}

The superset program survives, but in a sharper form. Its current success is
the coherent, reproducible embedding of the renormalized SM and the reduction
of many sector-specific constructions to shared finite operator data. The old
crossing-scale calibration and its downstream numerical claims are retired.

The next frontier is not another backfit. It is source promotion: emit the ten
magnitude rows and physical threshold/mass values from selected MTT data, or
retain them transparently as measured profile coordinates. That distinction is
the correct measure of progress toward strict no-knob closure.

"""
    text = replace_once(text, r"\\begin\{abstract\}.*?(?=\\begin\{thebibliography\})", body, "body")
    PAPER.write_text(text, encoding="utf-8", newline="\n")
    print(f"Updated {PAPER}")


if __name__ == "__main__":
    main()
