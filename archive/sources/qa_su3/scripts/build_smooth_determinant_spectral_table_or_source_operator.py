"""Build the smooth determinant spectral-table/source-operator gate."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

FINITE = DATA / "minimal_hsel_gret_finite_galerkin_candidate.candidate.json"
ORBIT = DATA / "central_twist_orbit_democracy_source_or_determinant_operator.candidate.json"

OUTPUT_DATA = DATA / "smooth_determinant_spectral_table_or_source_operator.candidate.json"
OUTPUT_CERT = CERTS / "smooth_determinant_spectral_table_or_source_operator_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Smooth_Determinant_Spectral_Table_or_Source_Operator_v1.md"


def det3(matrix: list[list[int]]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def build() -> tuple[dict[str, object], dict[str, object], str]:
    finite = json.loads(FINITE.read_text(encoding="utf-8"))
    orbit = json.loads(ORBIT.read_text(encoding="utf-8"))
    h = finite["hessian"]["matrix"]
    determinant = det3(h)

    finite_hessian_spectrum = {
        "operator": "finite projected Hessian H_sel on basis (K1,K2,c)",
        "eigenvalues_exact": ["8", "18 - sqrt(73)", "18 + sqrt(73)"],
        "trace_exact": 44,
        "determinant_exact": determinant,
        "zeta_regularized_finite_rank_logdet": "log(2008)",
        "zeta_regularized_finite_rank_logdet_numeric": math.log(determinant),
        "positive": True,
        "closed_for_finite_projected_hessian": True,
    }

    complement_test = {
        "name": "SmoothComplementIdentifiabilityTest",
        "same_finite_projection": "Both completions restrict to the same H_sel on the selected charge-coordinate Galerkin block.",
        "completion_A": {
            "spectrum": ["8", "18 - sqrt(73)", "18 + sqrt(73)"],
            "determinant": "2008",
            "logdet": "log(2008)",
        },
        "completion_B": {
            "spectrum": ["8", "18 - sqrt(73)", "18 + sqrt(73)", "Lambda"],
            "conditions": ["Lambda>0", "the extra mode lies in the smooth complement killed by the finite projection"],
            "determinant": "2008*Lambda",
            "logdet": "log(2008) + log(Lambda)",
        },
        "conclusion": "The finite Galerkin packet determines the projected Hessian determinant, but not the smooth complement determinant.",
        "smooth_determinant_identified": False,
    }

    source_scan = {
        "fixed_point_corpus": {
            "evidence": "uniform spectral gaps, compact Nil lower bounds, and functional calculus language",
            "usable_for_full_table": False,
            "why_not": "gap/lower-bound data do not specify all positive eigenvalues, multiplicities, or index weights",
        },
        "theta_nil_laplacian_corpus": {
            "evidence": "scalar Nil Laplacian formulas and first-eigenvalue lower bounds",
            "usable_for_full_table": False,
            "why_not": "scalar first-gap formulas are not the selected Qa/SU3 color-threshold operator spectrum",
        },
        "finite_galerkin_packet": {
            "evidence": "exact finite H_sel, G_ret, Pi_tw, tau, trace(Pi_tw), trace(tau^2)",
            "usable_for_full_table": False,
            "why_not": "it gives a finite projected operator, not a same-source smooth determinant spectrum",
        },
    }

    rejection_theorem = {
        "name": "FiniteProjectedHessianDoesNotDetermineSmoothThresholdDeterminant",
        "proof": [
            "The finite H_sel block is a projection of the selected charge sector onto three charge coordinates.",
            "Its finite-rank zeta determinant is exactly log(2008).",
            "A smooth threshold operator may have additional positive modes in the projection complement.",
            "Adding any positive complement eigenvalue Lambda leaves the finite H_sel block unchanged but changes the smooth determinant by log(Lambda).",
            "Therefore the smooth determinant is not identifiable from H_sel, G_ret, Pi_tw, tau, and finite trace invariants alone.",
        ],
        "verdict": "SMOOTH_DETERMINANT_REQUIRES_SELECTED_COMPLEMENT_SPECTRUM_OR_SOURCE_OPERATOR",
    }

    candidate = {
        "candidate": "SelectedQaSU3SmoothDeterminantSpectralTableOrSourceOperator",
        "status": "QA_SU3_FINITE_HESSIAN_DETERMINANT_CLOSED_SMOOTH_SPECTRUM_UNDERDETERMINED",
        "input_finite_candidate": str(FINITE.relative_to(ROOT)),
        "input_orbit_gate": str(ORBIT.relative_to(ROOT)),
        "finite_hessian_determinant": finite_hessian_spectrum,
        "smooth_complement_identifiability": complement_test,
        "source_scan": source_scan,
        "rejection_theorem": rejection_theorem,
        "decision": {
            "finite_projected_hessian_zeta_determinant": "CLOSED_LOG_2008",
            "smooth_threshold_spectral_table": "OPEN",
            "smooth_source_operator": "OPEN",
            "full_Qa_SU3_threshold_closure_now": False,
            "next_required_artifact": "Selected_Qa_SU3_Complement_Spectrum_or_Smooth_Operator_Source_v1",
        },
        "what_this_closes": [
            "exact finite projected Hessian spectrum",
            "exact finite projected Hessian determinant det(H_sel)=2008",
            "finite-rank zeta determinant log(2008)",
            "proof that complement spectrum is the remaining determinant datum",
        ],
        "what_remains_open": [
            "same-source smooth Qa/SU3 threshold operator",
            "positive complement spectrum and multiplicities",
            "index weights and zero-mode/BRST quotient policy for the smooth determinant",
            "heat/zeta/torsion finite part of that smooth operator",
        ],
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedQaSU3SmoothDeterminantSpectralTableOrSourceOperator",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "finite_hessian_spectrum_exact": True,
            "finite_hessian_determinant_log2008": True,
            "smooth_complement_identifiability_test": True,
        },
        "what_remains_open": {
            "smooth_threshold_spectral_table": True,
            "same_source_smooth_operator": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["decision"]["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    finite = candidate["finite_hessian_determinant"]
    test = candidate["smooth_complement_identifiability"]
    return f"""# Selected Qa/SU3 Smooth Determinant Spectral Table or Source Operator v1

## What Closes

The finite projected Hessian determinant is now exact.

```text
H_sel spectrum = {finite["eigenvalues_exact"]}
det(H_sel) = {finite["determinant_exact"]}
finite-rank zeta logdet = {finite["zeta_regularized_finite_rank_logdet"]}
```

This is the strongest determinant statement available from the current selected
finite Galerkin packet.

## Why This Still Is Not The Smooth Threshold Determinant

The smooth determinant has a complement-spectrum problem.  Two smooth
completions can share the same finite projection:

```text
Completion A logdet = {test["completion_A"]["logdet"]}
Completion B logdet = {test["completion_B"]["logdet"]}
```

The extra `Lambda` mode is invisible to the finite charge-coordinate block but
changes the determinant.  Therefore the selected finite Hessian does not
identify the full smooth Qa/SU3 threshold determinant.

## Corpus Scan Result

The fixed-point and Theta/Nil papers supply spectral-gap language, scalar
Nil-Laplacian formulas, and lower bounds.  They do not supply the selected
Qa/SU3 color-threshold spectrum, multiplicities, index weights, or smooth
operator finite part.

## Verdict

```text
finite projected determinant: closed
smooth threshold determinant: open
full Qa/SU3 closure: no
```

Next artifact:

```text
{candidate["decision"]["next_required_artifact"]}
```
"""


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
