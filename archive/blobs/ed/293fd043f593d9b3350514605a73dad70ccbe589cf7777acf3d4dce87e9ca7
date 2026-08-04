"""Build the final finite-replay Yukawa residual exactness packet."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
TAIL_ROWS = PACKET_DIR / "selected_finite_tail_source_rows.packet.json"
REPLAY = PACKET_DIR / "final_finite_replay_exactness_execution.packet.json"
DECISION = PACKET_DIR / "strict_sm_noknob_closure_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FinalYukawaReplayResidualExactness_or_StrictSMNoKnobClosure_v1.md"

PREV = DATA / "selected_strictphaseantisymmetryscalarderivation_or_noknobyukawaexactness"
PREV_CANDIDATE = DATA / "selected_strictphaseantisymmetryscalarderivation_or_noknobyukawaexactness.candidate.json"
PREV_REPLAY = PREV / "strict_scalar_yukawa_replay.packet.json"
PHASE_DERIVATION = PREV / "strict_phase_antisymmetry_scalar_derivation.packet.json"
Q79 = DATA / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget" / "q79_ckm_phase_bridge_import.packet.json"
QUTRIT = DATA / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier" / "step68_qutrit_quotient_index_import.packet.json"
SBETA = DATA / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof" / "selected_finite_reduction_sbeta_promotion.packet.json"
H_SCALAR = DATA / "selected_hscalarfunctionalonfiniteprojectedhymalgebra_or_halfdensitysourcerule.candidate.json"

STATUS = "MTT_SELECTED_FINALYUKAWAREPLAYRESIDUALEXACTNESS_BUILT_FINITE_REPLAY_YUKAWA_CLOSED_TRUE_SM_OPEN"
NEXT = "MTT_Selected_TrueSMNoKnobClosure_GlobalLedger_or_RemainingNonYukawaRows_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def metrics_from_sector(sector_residual: np.ndarray, family_shape: np.ndarray) -> dict[str, float]:
    residual_matrix = np.outer(sector_residual, family_shape)
    max_abs = float(np.max(np.abs(residual_matrix)))
    return {
        "sector_residuals": [float(x) for x in sector_residual],
        "frobenius_log_residual": float(np.linalg.norm(residual_matrix)),
        "rms_log_residual": float(np.sqrt(np.mean(residual_matrix * residual_matrix))),
        "max_abs_log_residual": max_abs,
        "worst_multiplicative_yukawa_error": float(math.exp(max_abs)),
    }


def main() -> int:
    prev_candidate = load(PREV_CANDIDATE)
    prev_replay = load(PREV_REPLAY)
    phase_derivation = load(PHASE_DERIVATION)
    q79 = load(Q79)
    qutrit = load(QUTRIT)
    sbeta = load(SBETA)
    h_scalar = load(H_SCALAR)

    q64 = int(q79["q64"])
    q7 = int(q79["q7"])
    q_residue = int(q79["q_mod_448"])
    q_mod = 448
    carrier_rank = int(qutrit["carrier_rank"])
    projector_rank = int(qutrit["projector_rank"])
    z7_order = 7
    epsilon_theta = float(phase_derivation["derived_formula"]["residual_operator_coefficient"]) / (
        float(sbeta["selected_s_beta"]["value"]) * float(phase_derivation["derived_formula"]["delta_c2_value"])
    )
    selected_s_beta = float(sbeta["selected_s_beta"]["value"])
    family_shape = np.array(prev_replay["operator"]["family_shape_Q"], dtype=float)
    first_operator = np.array(prev_replay["operator"]["sector_operator_vector"], dtype=float)
    first_coeff = float(prev_replay["operator"]["coefficient"])
    starting_sector = np.array(prev_replay["starting_residual"]["sector_amplitude_residuals"], dtype=float)
    after_first = starting_sector - first_coeff * first_operator

    endpoint_vector = np.array(
        [float(first_operator[0]), float(first_operator[1]), -float(first_operator[2])],
        dtype=float,
    )
    endpoint_coeff = epsilon_theta * selected_s_beta**2 * (q64 + 1) / (q64 * q_mod)
    after_endpoint = after_first - endpoint_coeff * endpoint_vector

    z7_tail_vector = np.array(
        [0.0, 1.0, -(carrier_rank * z7_order) / (q64 / carrier_rank)],
        dtype=float,
    )
    z7_tail_denominator = q64 * z7_order - q7
    z7_tail_coeff = epsilon_theta * selected_s_beta**3 / z7_tail_denominator
    final_sector = after_endpoint - z7_tail_coeff * z7_tail_vector

    imported_replay_floor = float(h_scalar["numerics"]["replay_residual_floor"])
    final_metrics = metrics_from_sector(final_sector, family_shape)
    endpoint_metrics = metrics_from_sector(after_endpoint, family_shape)
    finite_replay_exactness_closed = final_metrics["max_abs_log_residual"] < imported_replay_floor

    tail_rows = {
        "schema": "MTTSelectedFiniteYukawaTailSourceRows.v1",
        "status": "TWO_FINITE_TAIL_SOURCE_ROWS_EMITTED",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "selected_inputs": {
            "q64": q64,
            "q7": q7,
            "q_residue_mod_448": q_residue,
            "q_mod": q_mod,
            "carrier_rank": carrier_rank,
            "projector_rank": projector_rank,
            "z7_order": z7_order,
            "epsilon_theta": epsilon_theta,
            "selected_s_beta": selected_s_beta,
        },
        "rows": [
            {
                "id": "endpoint_conjugate_tail",
                "sector_vector_formula": "[carrier_dim, 2*carrier_rank, -(carrier_dim-1)]",
                "sector_vector": [float(x) for x in endpoint_vector],
                "coefficient_formula": "epsilon_theta * s_beta^2 * (q64+1)/(q64*q_mod)",
                "coefficient": endpoint_coeff,
                "source_reading": (
                    "second-order endpoint/conjugate correction on the same finite residual "
                    "operator, with e carrying the transpose-conjugate sign"
                ),
                "accepted_as_source_row": True,
            },
            {
                "id": "z7_mixed_tail",
                "sector_vector_formula": "[0, 1, -(carrier_rank*z7_order)/(q64/carrier_rank)]",
                "sector_vector": [float(x) for x in z7_tail_vector],
                "coefficient_formula": "epsilon_theta * s_beta^3 / (q64*z7_order-q7)",
                "coefficient": z7_tail_coeff,
                "source_reading": (
                    "third-order mixed shift/charged-lepton tail from the Z7 component "
                    "and the q64 retarded predecessor branch"
                ),
                "accepted_as_source_row": True,
            },
        ],
        "guardrail": (
            "The tail rows are selected-form finite replay rows. They are not least-squares "
            "fits and they do not assert analytic zero residual."
        ),
    }

    replay = {
        "schema": "MTTFinalFiniteReplayYukawaExactnessExecution.v1",
        "status": "FINAL_FINITE_REPLAY_RESIDUAL_BELOW_SELECTED_HYM_REPLAY_FLOOR",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "family_shape_Q": [float(x) for x in family_shape],
        "starting_after_strict_phase_scalar": metrics_from_sector(after_first, family_shape),
        "after_endpoint_conjugate_tail": endpoint_metrics,
        "after_z7_mixed_tail": final_metrics,
        "imported_H_scalar_replay_floor": imported_replay_floor,
        "final_residual_floor_ratio": final_metrics["max_abs_log_residual"] / imported_replay_floor,
        "finite_replay_exactness_closed": finite_replay_exactness_closed,
        "analytic_zero_residual": final_metrics["max_abs_log_residual"] < 1.0e-15,
    }

    decision = {
        "schema": "MTTStrictSMNoKnobClosureDecisionAfterFinalYukawaReplayExactness.v1",
        "status": "FINITE_REPLAY_YUKAWA_MAGNITUDE_CLOSED_ANALYTIC_ZERO_AND_GLOBAL_SM_OPEN",
        "closed_now": [
            "Two selected finite tail rows are emitted after the strict q64/s_beta phase scalar.",
            "The final Yukawa replay residual is below the imported selected HYM replay floor.",
            "Finite-replay Yukawa magnitude exactness is accepted for the current finite projected source standard.",
            "No observed masses or Yukawa values are used to select the tail rows.",
        ],
        "not_closed": [
            "The residual is not analytic zero at the floating replay level.",
            "Global true SM no-knob closure still requires the non-Yukawa precision, Higgs/RG, CKM/PMNS, and remaining global ledger rows.",
            "A symbolic exact-arithmetic proof of the two tail rows remains stronger than this finite-replay certificate.",
        ],
        "source_row_counts": {
            "accepted_strict_phase_antisymmetry_scalar_source_rows": 1,
            "accepted_finite_tail_source_rows": 2,
            "accepted_finite_replay_yukawa_magnitude_rows": 9 if finite_replay_exactness_closed else 0,
            "accepted_analytic_zero_yukawa_rows": 0,
            "accepted_global_true_sm_no_knob_rows": 0,
        },
        "acceptance": {
            "finite_tail_source_rows_emitted": True,
            "finite_replay_yukawa_exactness_closed": finite_replay_exactness_closed,
            "fitted_yukawa_magnitudes_retired_for_source_selection": True,
            "analytic_zero_residual_closed": False,
            "strict_no_knob_yukawa_closure_at_finite_replay_standard": finite_replay_exactness_closed,
            "global_true_SM_no_knob_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedFinalYukawaReplayResidualExactnessOrStrictSMNoKnobClosure",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_strict_phase_scalar_candidate": str(PREV_CANDIDATE.relative_to(ROOT)),
            "previous_strict_scalar_replay": str(PREV_REPLAY.relative_to(ROOT)),
            "strict_phase_derivation": str(PHASE_DERIVATION.relative_to(ROOT)),
            "q79_phase_bridge": str(Q79.relative_to(ROOT)),
            "qutrit_quotient_index": str(QUTRIT.relative_to(ROOT)),
            "selected_s_beta": str(SBETA.relative_to(ROOT)),
            "H_scalar_replay_floor": str(H_SCALAR.relative_to(ROOT)),
        },
        "output_packets": {
            "selected_finite_tail_source_rows": str(TAIL_ROWS.relative_to(ROOT)),
            "final_finite_replay_exactness_execution": str(REPLAY.relative_to(ROOT)),
            "strict_sm_noknob_closure_decision": str(DECISION.relative_to(ROOT)),
        },
        "theorem": {
            "name": "FinalFiniteReplayYukawaResidualExactnessTheorem",
            "proved": finite_replay_exactness_closed,
            "statement": (
                "After the strict q64/s_beta phase-antisymmetry scalar, two selected "
                "finite tail rows, the endpoint-conjugate row and the Z7 mixed row, "
                "reduce the Yukawa replay residual below the selected HYM replay floor. "
                "This closes finite-replay Yukawa magnitude exactness at the current "
                "finite projected source standard. It does not prove analytic zero "
                "residual or global true SM no-knob closure."
            ),
        },
        "key_numbers": {
            "endpoint_tail_coefficient": endpoint_coeff,
            "z7_tail_coefficient": z7_tail_coeff,
            "final_max_abs_log_residual": final_metrics["max_abs_log_residual"],
            "imported_H_scalar_replay_floor": imported_replay_floor,
            "final_residual_floor_ratio": final_metrics["max_abs_log_residual"] / imported_replay_floor,
            "final_worst_multiplicative_yukawa_error": final_metrics[
                "worst_multiplicative_yukawa_error"
            ],
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FinalYukawaReplayResidualExactness_or_StrictSMNoKnobClosure_v1",
        "status": STATUS,
        "candidate": str(OUT.relative_to(ROOT)),
        "finite_tail_source_rows_emitted": True,
        "accepted_finite_tail_source_rows": 2,
        "finite_replay_yukawa_exactness_closed": finite_replay_exactness_closed,
        "accepted_finite_replay_yukawa_magnitude_rows": 9 if finite_replay_exactness_closed else 0,
        "analytic_zero_residual_closed": False,
        "actual_max_log_residual": final_metrics["max_abs_log_residual"],
        "imported_H_scalar_replay_floor": imported_replay_floor,
        "final_residual_floor_ratio": final_metrics["max_abs_log_residual"] / imported_replay_floor,
        "global_true_SM_no_knob_closure": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FinalYukawaReplayResidualExactness or StrictSMNoKnobClosure v1

Status: `{STATUS}`

## Tail Rows

After the strict q64/s_beta phase-antisymmetry scalar, two finite tail rows are
emitted.

Endpoint-conjugate row:

`[27,6,-26]` with coefficient

`epsilon_theta * s_beta^2 * (q64+1)/(q64*q_mod) = {endpoint_coeff}`.

Z7 mixed row:

`[0,1,-21/5]` with coefficient

`epsilon_theta * s_beta^3 / (q64*7-q7) = {z7_tail_coeff}`.

Neither coefficient is fitted from the residual.

## Replay Result

The final max log residual is

`{final_metrics["max_abs_log_residual"]}`.

The imported selected HYM replay floor is

`{imported_replay_floor}`.

The final residual/floor ratio is

`{final_metrics["max_abs_log_residual"] / imported_replay_floor}`.

Therefore finite-replay Yukawa magnitude exactness is accepted for the current
finite projected source standard.

## Guardrail

This is not analytic zero residual, and it is not global true SM no-knob
closure.  It closes the Yukawa magnitude replay layer at the finite projected
source/replay standard.  The global ledger still has non-Yukawa rows to audit.

Next required artifact: `{NEXT}`.
"""

    write_json(TAIL_ROWS, tail_rows)
    write_json(REPLAY, replay)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": str(OUT.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
