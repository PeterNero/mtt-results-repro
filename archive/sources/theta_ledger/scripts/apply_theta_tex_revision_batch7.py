from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = (
    ROOT
    / "revised_tex_vnext"
    / "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v3"
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
        r"\\title\{Execution of Modal Triplet Theory II:.*?CY Corner\}",
        r"""\title{Execution of Modal Triplet Theory II:
Flavor, CKM, Neutral, and Higgs Status after True-SM Closure}""",
        "title",
    )
    text = text.replace(r"\date{January 2026}", r"\date{July 2026}", 1)
    body = r"""\begin{abstract}
We replace the legacy fitted Calabi--Yau flavor benchmark with the current
audited execution status. The 27-by-27 qutrit--Weyl/minimal matrix ledger,
charged Yukawa profile rows, selected $\Pi_{\mathrm{CKM}}$ rows, electroweak
primitive, and direct Higgs/threshold row support embedded renormalized-Standard-
Model equivalence at the adopted one-shared-physical-primitive/profile
standard. The final audit closes 12/12 obligations at that standard. This is
not a zero-knob derivation of measured masses. The nine charged Yukawa
magnitudes and $\lambda_H$ remain profile labels rather than internally emitted
strict source values. CKM closes at the prediction-with-uncertainty standard,
with maximum displacement $2.3565\times10^{-4}$ standard deviations. In the
neutral sector, MTT now emits a complete internal dimensionless response, but
its spectrum $[1,4,7]$ cannot be converted into the physical neutrino spectrum
by one common scale or nil subtraction. The old fitted PMNS, seesaw, and
few-TeV Higgs benchmarks are therefore withdrawn as predictions.
\end{abstract}

\section{Closure standard}

The accepted result is embedded renormalized-SM equivalence on the selected
branch at the one-shared-physical-primitive/profile standard. It imports the
standard SM quantization and uses a declared measured-input profile. It does
not derive all empirical values from MTT, prove unique observed-branch
selection, or establish a zero-primitive/no-knob theory.

The older Execution~II matrices were constructed with adjustable local texture
entries, phases, scale choices, and benchmark masses. The first correction pass
made their real-matrix diagonalizations arithmetically reproducible and removed
an unsupported CP claim. The present revision goes further: those matrices are
classified as historical profile fits and are no longer the authority for
flavor closure.

\section{Charged flavor and the 27-by-27 operator}

The current charged-sector authority contains:
\begin{itemize}
\item the locked 27-by-27 qutrit--Weyl/minimal matrix ledger;
\item the counted AH-equivalent HYM/projective lane, closed 8/8;
\item the selected charged Yukawa basis and magnitude-profile rows; and
\item the selected common-scheme threshold and mass transport with covariance.
\end{itemize}
These objects establish that the selected branch can reproduce the charged
renormalized-SM data coherently through one operator architecture.

At the strict source-value tier, however, the magnitude-bearing functional has
ten replay labels---nine charged Yukawa magnitudes and $\lambda_H$---and zero
accepted internal no-knob labels. Thus the matrix and basis maps are genuine
structural achievements, while the measured charged masses remain profile data
at the adopted closure standard.

\section{CKM and weak CP violation}

Three selected $\Pi_{\mathrm{CKM}}$ source rows are retained. They use neither
observed CKM values nor target residual fitting as selectors. Against the
frozen declared CKM uncertainty profile, their maximum displacement is
\begin{equation}
2.3564680386\times10^{-4}\ \text{standard deviations}.
\end{equation}
The strict-upgrade row U4 therefore closes at the
prediction-with-uncertainty-profile standard. Exact equality to a moving global
fit central estimator is neither obtained nor required, and no empirical
residual correction is introduced.

This CKM result supersedes the legacy printed real Yukawa matrices. Those real
matrices could reproduce mixing magnitudes but could not establish a nonzero
Jarlskog invariant. Weak-sector CP now belongs to the selected complex branch
and $\Pi_{\mathrm{CKM}}$ execution. It must not be confused with strong-CP
closure, which remains open.

\section{Neutral and PMNS sector}

The selected same-source neutral construction has advanced beyond the old
benchmark seesaw. Its complete internal dimensionless response is
\begin{equation}
a_{\mathrm{int}}=0.34195899479289005,
\qquad dY_\nu=I_3+X_3,
\end{equation}
with
\begin{equation}
H_{1,\nu}=
\begin{pmatrix}
-2a&0&-2a\\
0&-2a&-2a\\
-2a&-2a&0
\end{pmatrix}.
\end{equation}
All nine $H_{1,\nu}$ rows and all seven provenance fields are selected: six
entries equal $-2a$ and three are exact zeros. The associated selected
two-representative orbit has diagonal coefficient 1, cyclic-shift coefficients
$3/2\pm i\sqrt3/2$, and Hermitian spectrum $[1,4,7]$.

This is not yet a dimensionful neutrino Yukawa or mass matrix. A common scale
cannot alter eigenvalue ratios. Nil subtraction gives $[0,3,6]$ and therefore
the invariant ratio
\[
r_{\mathrm{direct}}=\frac{3}{6}=\frac12,
\]
whereas the stored normal-ordering oscillation postcheck is
$r_{\mathrm{post}}=0.02980501393$. The scale-only completion is therefore
falsified. The minimal surviving routes require either a selected non-affine
spectral-action slope plus one universal physical scale, or a selected
dimensionful seesaw/Dirac--Majorana block.

Consequently the old fitted neutrino masses, PMNS matrix, and Majorana scale are
withdrawn as predictions. They may be used only as historical benchmark data;
they do not close absolute neutrino mass, ordering selection, or ontology.

\section{Higgs status}

At the adopted profile standard, $P_{\mathrm{EW}}$ is counted once as the one
shared physical primitive, with zero Higgs-specific free parameters. The direct
$K_{\mathrm{threshold}}.\Omega_H.\lambda$ row and its row-purpose/formula bridge
are locked, and the common SMDR transport carries the Higgs row in the selected
precision object.

This closes the Higgs coordinate for embedded renormalized-SM equivalence. It
does not make $\lambda_H$ an internally emitted no-knob value: the
magnitude/profile functional still carries it as a replay label. The former
$\tan\beta=10$, $5~\mathrm{TeV}$ supersymmetric matching benchmark and its
one-loop Higgs pole-mass corridor are withdrawn. A strict UV-Higgs derivation
would require a selected magnitude-bearing source functional and dedicated
scheme/threshold transport independent of the measured Higgs coordinate.

\section{Sector status table}

\begin{center}
\begin{tabular}{p{0.24\linewidth}p{0.29\linewidth}p{0.37\linewidth}}
\toprule
Sector & Closed result & Remaining stronger obligation \\
\midrule
Charged flavor & 27-by-27 structure, basis maps, profile magnitudes & internal
source emission of nine magnitudes \\
CKM & selected prediction profile; U4 closed & no stronger central-estimator
identity required \\
Neutral/PMNS & internal dimensionless 9/9 response & non-affine action or
dimensionful seesaw, scale and ontology \\
Higgs & direct $K$ row and profile-standard coordinate & internal no-knob
$\lambda_H$ value source \\
\bottomrule
\end{tabular}
\end{center}

\section{Conclusion}

Execution II now records the actual frontier. Charged flavor, CKM, and Higgs
participate in the closed 12/12 embedded renormalized-SM equivalence theorem at
the adopted one-shared-primitive/profile standard. The CKM strict upgrade is
also closed at the correct uncertainty-profile criterion.

The result is not a derivation of all fermion masses from zero empirical
inputs. Ten magnitude labels remain profile data at the strict source tier,
and physical neutrino completion is demonstrably impossible by a common scale
alone. This separation preserves the genuine matrix/operator achievements
without promoting fitted or replayed values into source theorems.

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
