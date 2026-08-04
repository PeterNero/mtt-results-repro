from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = (
    ROOT
    / "revised_tex_vnext"
    / "Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle_v2"
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
        r"\\title\{Theta Closure in Modal Triplet Theory V:.*?Weak Mixing Angle\}",
        r"""\title{Theta Closure in Modal Triplet Theory V:
Weak-Angle Round Trip and the Non-Circularity Criterion}""",
        "title",
    )
    text = text.replace(r"\date{January 2026}", r"\date{July 2026}", 1)
    body = r"""\begin{abstract}
We reassess whether the weak mixing angle provides a redundant test of the
selected MTT gauge profile. Let
$r_{21}=I_2/I_1=g_1^2/g_2^2$, with $g_1=\sqrt{5/3}\,g_Y$. Then
$\sin^2\theta_W=3r_{21}/(5+3r_{21})$ at the same scale and in the same scheme.
For the selected SMDR profile at $Q=M_t$, this gives
$\sin^2\theta_W=0.2346644\pm0.0000433$. Because $r_{21}$ was itself obtained
from the measured $(g_Y,g_2)$ profile, this equality is an exact algebraic
round trip, not a held-out prediction. Supplying an absolute $g_2$ from
$(G_F,m_W)$ does not remove that circularity. A genuine redundancy test
requires an MTT source theorem selecting $r_{21}$ without electroweak gauge
data, followed by independent common-scheme transport. The obsolete one-loop
$5~\mathrm{TeV}$ calculation and its precision-prediction claim are withdrawn.
\end{abstract}

\section{Selected inputs and scope}

Paper~I adopts the full-Standard-Model $\overline{\mathrm{MS}}$ profile
transported by SMDR~v1.3 to
\[
Q=M_t=172.5590883453979~\mathrm{GeV}.
\]
Its relevant entries are
\[
g_Y=0.3585945042\pm0.0000307251,
\qquad
g_2=0.6475986708\pm0.0000287665,
\]
or $g_1=\sqrt{5/3}\,g_Y$ in GUT normalization. The associated overlap ratio is
\[
r_{21}:=\frac{I_2}{I_1}=0.5110273\pm0.0001231.
\]
Paper~II realizes this ratio by calibrating its effective geometry. Paper~III
checks conditional compatibility of the quadratic norm. Neither paper
currently supplies a value-source theorem selecting $r_{21}$ independently of
the gauge profile.

\section{Same-scale weak-angle identity}

The overlap convention is
\[
\frac{1}{g_a^2}=\frac{I_a}{g_{10}^2}.
\]
Therefore
\begin{equation}
r_{21}=\frac{I_2}{I_1}=\frac{g_1^2}{g_2^2}.
\label{eq:r21}
\end{equation}
Using $g_Y^2=(3/5)g_1^2$ and the $\overline{\mathrm{MS}}$ definition
\[
s_W^2(Q):=\frac{g_Y^2(Q)}{g_Y^2(Q)+g_2^2(Q)},
\]
gives the exact identity
\begin{equation}
\boxed{s_W^2(Q)=\frac{3r_{21}(Q)}{5+3r_{21}(Q)}.}
\label{eq:weak_identity}
\end{equation}

\begin{theorem}[Gauge-profile round-trip theorem]
If $r_{21}(Q)$ is constructed from the same measured common-scheme pair
$(g_Y(Q),g_2(Q))$ through Equation~\eqref{eq:r21}, then evaluating
Equation~\eqref{eq:weak_identity} returns the weak angle encoded in that pair.
The equality is algebraic and cannot constitute an independent prediction.
\end{theorem}

\begin{proof}
Substitution of $r_{21}=(5/3)g_Y^2/g_2^2$ into
Equation~\eqref{eq:weak_identity} gives
$g_Y^2/(g_Y^2+g_2^2)$ identically.
\end{proof}

For the selected ratio,
\begin{equation}
s_W^2(M_t)=0.2346644\pm0.0000433,
\end{equation}
where the uncertainty is propagated from the selected $r_{21}$ row. Direct
substitution of the selected $g_Y$ and $g_2$ gives the same central value. This
is a useful convention and arithmetic check, but it has no held-out status.

\section{Why the $(G_F,m_W)$ construction remains circular}

An electroweak input such as $(G_F,m_W)$ can set an absolute $SU(2)$
normalization, subject to radiative matching. It cannot make the weak-angle
test independent when the ratio $r_{21}$ still comes from the measured
hypercharge-to-$SU(2)$ profile. Indeed, once $g_2$ and $r_{21}$ are supplied,
Equation~\eqref{eq:r21} defines $g_1$ and hence the weak angle. The information
being tested is already present in $r_{21}$.

The earlier tree-level value near $0.2312$ used the obsolete $5~\mathrm{TeV}$
profile and a one-loop return to $M_Z$. It is withdrawn as a prediction. Its
threshold scan also showed that the apparent precision was not stable under
the stated electroweak matching variation.

\section{Criterion for a genuine redundant determination}

A non-circular weak-angle test requires all of the following:
\begin{enumerate}
\item MTT geometry selects $r_{21}$ without using $g_Y$, $g_1$, $g_2$, or
$\sin^2\theta_W$ as value inputs;
\item an absolute gauge normalization and matching scale are selected without
using the held-out weak angle;
\item the boundary data are transported with a declared multi-loop scheme and
threshold prescription; and
\item the resulting $s_W^2$ is compared with a measurement not used anywhere
in selection, calibration, or branch choice.
\end{enumerate}
Only then is Equation~\eqref{eq:weak_identity} a prediction map rather than a
round-trip map. Current Papers~I--III satisfy the algebraic and realization
parts but not the first value-source condition.

\section{Conclusion}

The weak mixing angle is exactly consistent with the selected gauge profile,
as it must be. The precise same-scale result is
$s_W^2(M_t)=0.2346644\pm0.0000433$. This validates the hypercharge
normalization and overlap-ratio bookkeeping.

It does not add an independent Standard Model observable to MTT closure. The
former non-circularity claim fails because the overlap ratio already contains
the measured weak-angle information. The next theorem target is sharply
defined: select $r_{21}$ from MTT source geometry before consulting the
electroweak gauge profile, then execute a held-out common-scheme comparison.


% ===========================
"""
    text = replace_once(
        text,
        r"\\begin\{abstract\}.*?(?=\\section\*\{References\})",
        body,
        "paper body",
    )
    PAPER.write_text(text, encoding="utf-8", newline="\n")
    print(f"Updated {PAPER}")


if __name__ == "__main__":
    main()
