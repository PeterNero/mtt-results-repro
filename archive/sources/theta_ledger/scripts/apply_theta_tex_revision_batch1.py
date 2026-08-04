from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = (
    ROOT
    / "revised_tex_vnext"
    / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry_v2"
    / "main.tex"
)


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    if text.count(start) != 1:
        raise SystemExit(f"expected one start marker, found {text.count(start)}: {start}")
    if text.count(end) != 1:
        raise SystemExit(f"expected one end marker, found {text.count(end)}: {end}")
    before, remainder = text.split(start, 1)
    _, after = remainder.split(end, 1)
    return before + replacement.rstrip() + "\n\n" + end + after


def require_replace(text: str, old: str, new: str) -> str:
    if old not in text:
        raise SystemExit(f"missing expected contextual text: {old[:100]!r}")
    return text.replace(old, new)


def main() -> None:
    text = PAPER.read_text(encoding="utf-8")
    text = require_replace(
        text,
        "Theta Closure in Modal Triplet Theory I:\nGauge Couplings from Internal Geometry",
        "Theta Closure in Modal Triplet Theory I:\nGauge-Profile Targets from Multi-Loop Common-Scheme Transport",
    )

    transport = r"""
% ===========================
\section{Selected multi-loop common-scheme transport}
% ===========================

The former one-loop evolution to $5~\mathrm{TeV}$ is not used in this
revision.  In particular, the Standard Model equations do not place the
$g_1=g_2$ crossing there.  We instead use the selected SMDR~v1.3 transport,
which maps fifteen measured source coordinates to the full non-decoupled
Standard Model in the tadpole-free pure $\overline{\mathrm{MS}}$ scheme at
\[
 Q=M_t=172.5590883453979~\mathrm{GeV}.
\]
This is a scheme and comparison scale, not an MTT coherence scale.

The accepted gauge rows are
\begin{align}
 g_Y(Q)&=0.3585945042\pm0.0000307251,\\
 g_2(Q)&=0.6475986708\pm0.0000287665,\\
 g_3(Q)&=1.163427409\pm0.004036156.
\end{align}
With the paper's GUT normalization,
\[
 g_1(Q)=\sqrt{\frac53}\,g_Y(Q)
       =0.4629435143\pm0.0000396660.
\]
These rows are outputs of a common multi-loop matching/running map.  Their
covariance is propagated from the declared diagonal measured-input profile;
an official joint likelihood spanning all fifteen source coordinates is not
claimed.

% ===========================
\section{Numerical $\Theta$--profile targets from gauge data}
% ===========================

Under the coupling--overlap relation already proved conditionally above,
\[
 \frac{I_b}{I_a}=\left(\frac{g_a}{g_b}\right)^2.
\]
Consequently the selected common-scheme profile gives
\begin{equation}
\boxed{
 \frac{I_2}{I_1}=0.5110273\pm0.0001231,
 \qquad
 \frac{I_3}{I_1}=0.158335\pm0.001098.
}
\label{eq:targets}
\end{equation}
The propagated covariance of the two ratios is
$-6.1892\times10^{-9}$, corresponding to correlation $-0.04578$.

These are experimentally anchored profile targets.  A geometry adjusted to
reproduce them is a calibrated realization.  A held-out prediction would
require fixing that geometry without these gauge rows and then computing an
observable not used in source, branch, scale, or model selection.
"""
    text = replace_between(
        text,
        r"\section{One-loop renormalization group running to $\mu_\Theta$}",
        r"\section{Transition to the geometric $\Theta$-problem}",
        transport,
    )

    replacements = {
        "= 0.560,": "= 0.5110273,",
        "= 0.229.": "= 0.158335.",
        r"\frac{0.560\cdot 2\pi}{\kappa_\ell}\,R_1": r"\frac{0.5110273\cdot 2\pi}{\kappa_\ell}\,R_1",
        r"\frac{3.518}{\kappa_\ell}\,R_1": r"\frac{3.210879}{\kappa_\ell}\,R_1",
        r"\sqrt{(3.518/\kappa_\ell)\,R_1}": r"\sqrt{(3.210879/\kappa_\ell)\,R_1}",
        r"0.229\cdot 2\pi\,R_1": r"0.158335\cdot 2\pi\,R_1",
        r"1.439\,R_1": r"0.994849\,R_1",
        r"\frac{8\kappa_\ell}{3.518}\approx 2.274\,\kappa_\ell": r"\frac{8\kappa_\ell}{3.210879}\approx 2.492\,\kappa_\ell",
        r"Fix $\mu_\Theta=5~\mathrm{TeV}$ and choose": r"At the selected common-scheme profile point $Q=M_t$, choose",
        r"$\frac{I_2}{I_1}\approx 0.560$ and $\frac{I_3}{I_1}\approx 0.229$": r"$\frac{I_2}{I_1}=0.5110273$ and $\frac{I_3}{I_1}=0.158335$",
        r"$(f_2R_{\mathrm{lens}})^2=3.518R_1\le 7.036<8$": r"$(f_2R_{\mathrm{lens}})^2=3.210879R_1\le 6.421758<8$",
        "at\n$\\mu_\\Theta=5~\\mathrm{TeV}$,": r"at the selected common-scheme point $Q=M_t$:",
        r"\frac{I_2}{I_1} \approx 0.560": r"\frac{I_2}{I_1} = 0.5110273",
        r"\frac{I_3}{I_1} \approx 0.229": r"\frac{I_3}{I_1} = 0.158335",
        r"\frac{I_2^{(0)}}{I_1} \approx 0.560": r"\frac{I_2^{(0)}}{I_1} = 0.5110273",
        r"\frac{I_3^{(0)}}{I_1} \approx 0.229": r"\frac{I_3^{(0)}}{I_1} = 0.158335",
    }
    for old, new in replacements.items():
        text = require_replace(text, old, new)

    scale_separation = r"""
% ===========================
\section{Scale separation and withdrawn legacy calibration}
% ===========================

The scale $Q=M_t$ used above is a renormalization/matching coordinate.  It does
not determine the physical internal gap, compactification radius, proper-time
filter, Planck scale, Hubble scale, or primordial tensor amplitude.  The former
identifications
\[
 Q\sim E_{\mathrm{gap,min}}\sim\tau_0^{-1/2}
\]
were additional calibrations tied to the invalid $4.2$--$5~\mathrm{TeV}$
crossing and are withdrawn.

The dimensionless spectral inequalities in the preceding sections remain
conditional geometric statements.  Converting them to SI or external energy
units requires an independently selected action normalization and a theorem
relating the internal operator spectrum to physical propagator poles or
response scales.  No cosmological or quantum-gravity bound is inferred in this
paper.
"""
    text = replace_between(
        text,
        r"\section{Absolute scale calibration and quantum--gravity consistency}",
        r"\section{Falsifiability}",
        scale_separation,
    )

    ending = r"""
% ===========================
\section{Falsifiability and status}
% ===========================

At the profile tier, the direct test is whether a specified internal geometry,
with its measure and harmonic normalization fixed independently of the gauge
targets, emits the two ratios in \eqref{eq:targets} within the propagated
covariance.  If the geometry is fitted to those ratios, the result is instead
a realization and round-trip consistency check.

The old cosmological and Gaussian quantum-gravity discriminators are removed
because their physical scale identification is not derived here.  The current
broader MTT repository closes embedded renormalized-Standard-Model equivalence
at the adopted one-shared-physical-primitive/profile standard.  That successor
does not turn the present overlap targets into zero-knob predictions and does
not derive standard perturbative quantization from MTT.

\section{Conclusion}

The coupling--overlap formula survives as a conditional dimensional-reduction
identity.  Its numerical implementation is now placed in one selected
multi-loop common scheme at $Q=M_t$, yielding
\[
 I_2/I_1=0.5110273(12),\qquad I_3/I_1=0.15834(11).
\]
The full covariance provenance is retained, and the absence of a public joint
fifteen-coordinate likelihood is stated explicitly.

The former $5~\mathrm{TeV}$ crossing, the geometry calibrated to its ratios,
and the identification of that scale with an internal gap, proper-time cutoff,
or cosmological scale are not results of this revision.  Papers II--V must be
re-executed or reclassified accordingly.  This paper therefore supplies a
reproducible profile target and a precise geometric test, not a unique
first-principles prediction of gauge couplings or internal geometry.
"""
    text = replace_between(text, r"\section{Falsifiability}", r"\section*{References}", ending)
    PAPER.write_text(text, encoding="utf-8")
    print(f"updated {PAPER}")


if __name__ == "__main__":
    main()
