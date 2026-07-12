"""Build the U1/Y local-determinant-from-27-mode D_E gap-layer gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "electroweak_fill": DATA / "selected_electroweak_u1y_operatorrow_or_anchor_valuepacket_fill.candidate.json",
    "u1_operator_fill": DATA / "selected_electroweak_u1y_operator_row_source_packet.fill_attempt.json",
    "routec_trace_gap": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer_certificate.json"
OUTPUT_SPECTRUM = DATA / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.spectrum_attempt.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_U1Y_LocalDeterminant_From_27Mode_DE_GapLayer_v1.md"

STATUS = "ELECTROWEAK_U1Y_LOCALDETERMINANT_FROM_27MODE_DE_GAPLAYER_ATTEMPTED_FUNCTIONAL_MAP_OPEN"
NEXT = "Selected_Electroweak_U1Y_DeterminantFunctional_Weighting_or_NoGo_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def model_spectrum() -> dict[str, Any]:
    """Return the finite 27-mode model spectrum implied by the closed D_E layer."""
    gamma = 4.0 * math.pi**2 / 9.0
    complement_logdet = 12.0 * math.log(gamma) + 12.0 * math.log(2.0 * gamma)
    h_zero_shift_eta = 1.0
    h_with_zero_shift_logdet = complement_logdet + 2.0 * math.log(h_zero_shift_eta)
    return {
        "schema": "Conditional27ModeDEFiniteSpectrumAttempt.v1",
        "basis_id": "F3xF3_gerbe_twisted_fourier_N1_rank3",
        "basis_dimension": 27,
        "base_laplacian_unit": "(2*pi/3)^2",
        "base_laplacian_unit_numeric": gamma,
        "F3xF3_frequency_spectrum": [
            {"eigenvalue": "0", "multiplicity": 1},
            {"eigenvalue": "(2*pi/3)^2", "multiplicity": 4},
            {"eigenvalue": "2*(2*pi/3)^2", "multiplicity": 4},
        ],
        "rank3_model_positive_complement": [
            {"eigenvalue": "(2*pi/3)^2", "multiplicity": 12},
            {"eigenvalue": "2*(2*pi/3)^2", "multiplicity": 12},
        ],
        "rank3_model_kernel_multiplicity": 3,
        "H_sector_zero_cluster_shift_candidate": {
            "selected_eta_N": h_zero_shift_eta,
            "shifted_zero_modes": 2,
            "unshifted_zero_modes": 1,
            "include_in_determinant_policy_selected": False,
            "reason": "The trace-equals-27mode theorem identifies the H-sector zero-cluster rank-two shift, but the electroweak U1/Y determinant functional has not selected whether this H-sector shift enters the U1/Y threshold finite part.",
        },
        "conditional_zeta_logdet_positive_complement": {
            "formula": "12*log((2*pi/3)^2) + 12*log(2*(2*pi/3)^2)",
            "numeric": complement_logdet,
        },
        "conditional_logdet_if_H_eta1_zero_shift_included": {
            "formula": "positive_complement_logdet + 2*log(1)",
            "numeric": h_with_zero_shift_logdet,
        },
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    fill = load(INPUTS["electroweak_fill"])
    u1_fill = load(INPUTS["u1_operator_fill"])
    trace_gap = load(INPUTS["routec_trace_gap"])
    spectrum = model_spectrum()

    gap = trace_gap["finite_trace_route"]["gap_layer"]
    determinant_map_tests = {
        "use_27mode_gap_bound_as_logdet": {
            "status": "REJECTED_BOUND_NOT_SPECTRUM",
            "reason": "selected_gap_lower_bound is a Riesz/gap stability bound, not an eigenvalue list or zeta finite part.",
            "value_tested": gap["selected_gap_lower_bound"],
        },
        "use_rank3_model_complement_spectrum_as_U1Y": {
            "status": "CONDITIONAL_SUPPORT_NOT_SELECTED_U1Y_FUNCTIONAL",
            "reason": "The rank-3 F3xF3 complement spectrum is emitted by the D_E gap-layer theorem, but no source selects it as the U1/Y local determinant on V/<s> with hypercharge/index weights.",
            "conditional_logdet": spectrum["conditional_zeta_logdet_positive_complement"]["numeric"],
        },
        "include_H_zero_cluster_shift": {
            "status": "POLICY_OPEN",
            "reason": "The H-sector rank-two zero-cluster shift is source-identified, but the U1/Y determinant finite-part policy has not selected inclusion, exclusion, or cancellation.",
            "conditional_logdet_if_eta1_included": spectrum["conditional_logdet_if_H_eta1_zero_shift_included"]["numeric"],
        },
        "use_Pperp_trace_index_as_weighted_spectrum": {
            "status": "REJECTED_PROJECTOR_NOT_SPECTRUM",
            "reason": "P_perp closes the quotient trace index 2/3 only; it cannot supply positive eigenvalues or a zeta/heat/torsion finite part.",
        },
    }

    required_functional = {
        "schema": "SelectedElectroweakU1YDeterminantFunctionalRequired.v1",
        "must_select": [
            "sector restriction from the 27-mode B_N/End0 packet to U1/Y on V/<s>",
            "kernel and H-sector zero-cluster inclusion/exclusion policy",
            "hypercharge/index/Dynkin weights before electroweak comparison",
            "same-scheme SU2 determinant row or exact cancellation theorem",
            "regularization convention for finite zeta/heat/torsion part",
            "lambda_12 formula using only selected rows",
        ],
        "must_not_use": [
            "observed lambda_12 or sin^2(theta_W)",
            "gap lower bound as determinant spectrum",
            "P_perp identity spectrum",
            "Qa/SU3 log(2008) injection",
            "unit convention or physical anchor data",
        ],
    }

    decision = {
        "attempt_executed": True,
        "conditional_27mode_spectrum_written": True,
        "positive_model_complement_spectrum_available": True,
        "selected_U1Y_determinant_functional_closed": False,
        "selected_positive_U1Y_eigenvalues_closed": False,
        "selected_zeta_heat_torsion_finite_part_closed": False,
        "same_scheme_SU2_determinant_or_cancellation_closed": False,
        "lambda_12_closed": False,
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedElectroweakU1YLocalDeterminantFrom27ModeDEGapLayer",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "electroweak_fill": fill["status"],
            "u1_operator_fill": u1_fill["status"],
            "routec_trace_gap": trace_gap["status"],
        },
        "conditional_spectrum_path": rel(OUTPUT_SPECTRUM),
        "closed_27mode_prefix": {
            "basis_id": gap["basis_id"],
            "basis_dimension": gap["basis_dimension"],
            "selected_trace_equality_for_27mode_DE": trace_gap["decision"]["selected_trace_equality_for_27mode_DE"],
            "DE_gap_Riesz_Green_layer_closed": trace_gap["decision"]["DE_gap_Riesz_Green_layer_closed"],
            "selected_gap_lower_bound": gap["selected_gap_lower_bound"],
            "selected_green_norm_bound": gap["selected_green_norm_bound"],
        },
        "determinant_map_tests": determinant_map_tests,
        "required_functional": required_functional,
        "decision": decision,
        "theorem": {
            "name": "ElectroweakU1YLocalDeterminantFrom27ModeDEGapLayerGate",
            "proved": True,
            "statement": (
                "The selected 27-mode D_E gap layer emits a conditional finite "
                "model spectrum, but it does not by itself select the electroweak "
                "U1/Y local determinant functional. A U1/Y determinant closure "
                "requires a same-source restriction/weighting/finite-part theorem "
                "mapping the 27-mode B_N operator to V/<s>, plus a same-scheme "
                "SU2 row or cancellation theorem. Therefore lambda_12 remains open."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_lambda12_target_witness": False,
            "promotes_gap_bound_as_spectrum": False,
            "promotes_Pperp_as_spectrum": False,
            "injects_Qa_log2008": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakU1YLocalDeterminantFrom27ModeDEGapLayer",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "spectrum_attempt_path": rel(OUTPUT_SPECTRUM),
        "note_path": rel(OUTPUT_NOTE),
        "closed": {
            "conditional_27mode_model_spectrum": True,
            "gap_bound_rejected_as_logdet": True,
            "Pperp_rejected_as_spectrum": True,
            "required_U1Y_determinant_functional_isolated": True,
        },
        "open": {
            "selected_U1Y_determinant_functional": True,
            "selected_positive_U1Y_eigenvalues": True,
            "selected_finite_part": True,
            "same_scheme_SU2_determinant_or_cancellation": True,
            "lambda_12": True,
        },
        "conditional_logdet_positive_complement": spectrum["conditional_zeta_logdet_positive_complement"]["numeric"],
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, spectrum, render_note(candidate, cert, spectrum)


def render_note(candidate: dict[str, Any], cert: dict[str, Any], spectrum: dict[str, Any]) -> str:
    return f"""# Selected Electroweak U1Y LocalDeterminant From 27Mode DE GapLayer v1

## Result

```text
status = {candidate["status"]}
conditional_27mode_spectrum_written = true
selected_U1Y_determinant_functional_closed = false
lambda_12_closed = false
measured_electroweak_closure = false
```

## What We Tried Before

Yes: earlier gates tried nearby routes. They closed the 27-mode `D_E`
gap/Riesz/Green layer, tested scalar proxy spectra, and ran diagnostic
`lambda_12` scans. They did not select the determinant functional mapping the
27-mode `D_E` packet to the U1/Y finite part on `V/<s>`.

## Conditional Spectrum

```json
{json.dumps(spectrum, indent=2, sort_keys=True)}
```

## Determinant Map Tests

```json
{json.dumps(candidate["determinant_map_tests"], indent=2, sort_keys=True)}
```

## Required Functional

```json
{json.dumps(candidate["required_functional"], indent=2, sort_keys=True)}
```

## Next

```text
{candidate["decision"]["next_required_artifact"]}
```

The new missing object is not another 27-mode `D_E` proof. It is the selected
U1/Y determinant functional: the source theorem that says which weighted,
kernel-quotiented, regularized part of the 27-mode packet is the U1/Y local
threshold row, and how the same scheme handles SU2 or cancels it.

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, spectrum, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_SPECTRUM, spectrum)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_SPECTRUM, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
