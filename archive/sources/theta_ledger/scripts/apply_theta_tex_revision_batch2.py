from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = (
    ROOT
    / "revised_tex_vnext"
    / "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps_v2"
    / "main.tex"
)


def require_replace(text: str, old: str, new: str, count: int | None = None) -> str:
    found = text.count(old)
    if found == 0 or (count is not None and found != count):
        raise SystemExit(f"expected contextual text count {count}, found {found}: {old[:100]!r}")
    return text.replace(old, new)


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise SystemExit(f"non-unique section markers: {start!r}, {end!r}")
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    return before + replacement.rstrip() + "\n\n" + end + after


def replace_between_first(text: str, start: str, end: str, replacement: str) -> str:
    start_at = text.find(start)
    end_at = text.find(end, start_at + len(start))
    if start_at < 0 or end_at < 0:
        raise SystemExit(f"missing ordered section markers: {start!r}, {end!r}")
    return text[:start_at] + replacement.rstrip() + "\n\n" + text[end_at:]


def main() -> None:
    text = PAPER.read_text(encoding="utf-8")
    text = require_replace(
        text,
        "Direct Geometric Realization of Nonabelian Overlaps",
        "Direct Geometric Realization of Selected Gauge-Profile Overlaps",
        count=1,
    )
    text = require_replace(text, r"\date{January 2026}", r"\date{July 2026}", count=1)

    old_abstract = r"""We compute the leading--order nonabelian overlap integrals $I_2^{(0)}$ and
$I_3^{(0)}$ appearing in the $\Theta$--closure program of Modal Triplet Theory
(MTT) using explicit internal geometry (Route~A).
Working on the baseline internal space
$S^1_{\mathrm{cen}}\times L(3,1)\times\Gamma\backslash\mathrm{Nil}_3$, we evaluate
the $SU(2)$ overlap on a constant--curvature lens layer and the $SU(3)$ overlap
on a compact Heisenberg nilmanifold with left--invariant metric.
We show that these overlaps can be matched exactly to the numerical
$\Theta$--targets extracted from Standard Model gauge couplings at the matching
scale $\mu_\Theta=5~\mathrm{TeV}$, while satisfying all spectral gap and
admissibility constraints of the MTT Foundation with large margin.
This provides the first explicit realization of $\Theta$--closure at leading
order using concrete internal geometry, independent of twistor or string--theoretic
constructions."""
    new_abstract = r"""We re-execute the Route~A geometric overlap ansatz against the selected
multi-loop gauge-profile targets of Paper~I.  In its stated dimensionless
normalization, the round-$S^2$ effective lens base and isotropic compact
Heisenberg nilmanifold can be retargeted analytically to
\[
 (f_2R_{\mathrm{lens}})^2=0.2555137R_1,
 \qquad c=0.9948493R_1.
\]
The associated spectral lower bounds remain above the assumed dimensionless
admissibility floor.  This proves existence of a calibrated representative in
the declared ansatz.  It does not prove that the full lens space reduces to
this $S^2$ model, that the geometry is selected uniquely by MTT, or that the
gauge couplings are held-out predictions.  The old $5~\mathrm{TeV}$ target pair
is withdrawn."""
    text = require_replace(text, old_abstract, new_abstract, count=1)

    relation = r"""
\section{Relation to the revised $\Theta$--closure core paper}

Paper~I now transports measured source coordinates with SMDR~v1.3 to the
full-Standard-Model $\overline{\mathrm{MS}}$ profile at $Q=M_t$.  In the same
GUT-normalized overlap convention it supplies
\[
 \frac{I_2}{I_1}=0.5110273\pm0.0001231,
 \qquad
 \frac{I_3}{I_1}=0.158335\pm0.001098.
\]
The scale $Q=M_t$ is a matching convention, not an internal gap or coherence
scale.  This paper asks only whether the explicit Route~A ansatz contains a
representative with those overlap ratios and the stated dimensionless gap
margin.  Because the gauge rows select the target, success is a calibrated
realization and round-trip test.

"""
    text = replace_between(
        text,
        r"\section{Relation to the $\Theta$--closure core paper}",
        r"\section{Overlap definitions}",
        relation,
    )

    convention = r"""
\section{Lens sector: computation of $I_2^{(0)}$}

\paragraph{Dimensional and geometric convention.}
All radii and overlaps below are dimensionless after one common internal length
unit has been factored out.  The ``lens layer'' used in the calculation is an
effective two-dimensional constant-curvature base modeled by a round $S^2$; it
is not the full three-dimensional lens space $L(3,1)$.  A full lens-space
realization requires a separate reduction theorem.
"""
    text = require_replace(text, r"\section{Lens sector: computation of $I_2^{(0)}$}", convention, count=1)
    text = require_replace(
        text,
        "The coefficient ``2'' uniquely identifies the round two--sphere\n"
        "as the baseline model. We therefore take",
        "The coefficient ``2'' motivates the round two--sphere as the baseline\n"
        "effective model within this ansatz; it is not a global uniqueness theorem. We take",
        count=1,
    )

    replacements = {
        "0.560": "0.5110273",
        "0.280": "0.2555137",
        "0.229": "0.158335",
        "1.439": "0.9948493",
        "2.878": "1.989699",
    }
    for old, new in replacements.items():
        text = require_replace(text, old, new)

    first_conclusion = r"""
\section{Route-A result and scope}

Within the declared dimensionless ansatz, the selected profile targets admit
an explicit lens-base/nil representative and the assumed spectral inequalities
remain satisfied.  This closes the algebraic retargeting and ansatz-level
existence check.  It does not close source selection of the geometry, a literal
$L(3,1)$ reduction, global HYM connection data, or a held-out gauge-coupling
prediction.

"""
    text = replace_between_first(text, r"\section{Conclusion}", r"\appendix", first_conclusion)

    second_start = text.rfind(r"\section{Conclusion}")
    bibliography = text.find(r"\begin{thebibliography}{99}", second_start)
    if second_start < 0 or bibliography < 0:
        raise SystemExit("could not locate final conclusion/bibliography")
    final_conclusion = r"""\section{Conclusion}

The Route~A formulas have been evaluated in the same normalization and scheme
as revised Paper~I.  The new central representative is
\[
 (f_2R_{\mathrm{lens}})^2=0.2555137R_1,
 \qquad c=0.9948493R_1,
\]
with uncertainties inherited from the two profile ratios.  The nil spectral
estimate and lens lower bound continue to exceed the assumed dimensionless
floor for the stated parameter range.

The earlier numbers $0.280R_1$ and $1.439R_1$ belonged to the withdrawn
$5~\mathrm{TeV}$ profile and are not retained.  The present construction is a
calibrated existence result: the target gauge rows were used to determine the
geometry.  Selection of this geometry before empirical comparison, literal
lens-space reduction, and a global HYM representative remain separate proof
obligations.

"""
    text = text[:second_start] + final_conclusion + text[bibliography:]
    PAPER.write_text(text, encoding="utf-8")
    print(f"updated {PAPER}")


if __name__ == "__main__":
    main()
