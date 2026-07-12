"""Build the Pi_CKM closure-cost trace-law candidate and acceptance cutset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_pickmclosurecosttracefunctional_or_angleweightrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRACE_LAW = PACKET_DIR / "pickm_source_trace_law_candidate.packet.json"
PREDICTION = PACKET_DIR / "ckm_angle_prediction_from_trace_law_candidate.packet.json"
ACCEPTANCE = PACKET_DIR / "pickm_trace_law_acceptance_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PiCKMClosureCostTraceFunctional_or_AngleWeightRows_v1.md"

PREVIOUS = DATA / "selected_kckmtraceassemblyrule_or_oneprincipleckmclosure.candidate.json"
SCAN = DATA / "selected_eckmweightrowcertificates_or_ckmangleclosuredecision" / "available_eckm_trace_invariant_scan.packet.json"
LEADING = DATA / "selected_deltav_to_ckm_anglemagnitudemap_or_honestflavorobservableexecution" / "leading_sqrt_flavor_angle_map.packet.json"
CONTRACT = DATA / "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution" / "sector_pair_projection_contract.packet.json"

STATUS = "MTT_SELECTED_PICKM_TRACE_LAW_CANDIDATE_BUILT_SOURCE_DERIVATION_OPEN"
NEXT = "MTT_Selected_PiCKMSourceDerivationClauses_or_CKMPredictionUpgrade_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    previous = load(PREVIOUS)
    scan = load(SCAN)
    leading = load(LEADING)
    contract = load(CONTRACT)

    if previous["next_required_artifact"] != "MTT_Selected_PiCKMClosureCostTraceFunctional_or_AngleWeightRows_v1":
        raise ValueError("previous artifact does not point at Pi_CKM closure-cost trace functional")

    source_constants = scan["source_constants"]
    best = scan["best_by_weight_row"]
    weights = {row: best[row]["value"] for row in ["W12", "W23", "W13"]}
    target_weights = {row: best[row]["target_weight"] for row in ["W12", "W23", "W13"]}

    rows = {
        "Pi_CKM^12": {
            "weight": "W12",
            "formula": "Tr_N(Pi_CKM^12 K_sel) := (||R_Z||_F^2 + 5 sin(delta_79))/6",
            "source_formula": best["W12"]["formula"],
            "value": weights["W12"],
            "interpretation": "nearest-adjacent q79 sine/light-phase closure-cost row",
            "derivation_clause_closed": False,
        },
        "Pi_CKM^23": {
            "weight": "W23",
            "formula": "Tr_N(Pi_CKM^23 K_sel) := (sqrt(3) + 3 q |cos(delta_79)|/2)/8",
            "source_formula": best["W23"]["formula"],
            "value": weights["W23"],
            "interpretation": "middle-heavy q79 cosine/heavy-link closure-cost row",
            "derivation_clause_closed": False,
        },
        "Pi_CKM^13": {
            "weight": "W13",
            "formula": "Tr_N(Pi_CKM^13 K_sel) := (5 q + 3(448/64))/18",
            "source_formula": best["W13"]["formula"],
            "value": weights["W13"],
            "interpretation": "long-bridge q79 plus dyadic/sevenfold modulus closure-cost row",
            "derivation_clause_closed": False,
        },
    }

    trace_law = {
        "schema": "MTTPiCKMSourceTraceLawCandidate.v1",
        "status": "PICKM_SOURCE_TRACE_LAW_CANDIDATE_BUILT_NOT_PROMOTED",
        "source_constants": source_constants,
        "rows": rows,
        "candidate_emits_three_numeric_weights": True,
        "accepted_as_selected_row_certificates": False,
        "accepted_weight_rows": 0,
        "why_not_promoted": [
            "the row formulas were identified by a diagnostic postcheck scan",
            "the closure-cost projector derivation clauses are not yet proved",
            "the frozen replay weights are not matched exactly",
        ],
        "diagnostic_postcheck_scan_used_for_discovery": True,
        "observed_data_used_as_selector_for_source_closure": False,
        "target_fitting_used_to_accept_rows": False,
    }

    leading_angles = leading["predicted_angles"]
    measured_targets = {
        row: leading["residuals_against_measured_replay"][angle]["measured_replay_target"]
        for row, angle in [("W12", "s12"), ("W23", "s23"), ("W13", "s13")]
    }
    angle_map = {"W12": "s12", "W23": "s23", "W13": "s13"}
    predicted_angles: dict[str, Any] = {}
    for row, angle in angle_map.items():
        leading_value = leading_angles[angle]
        predicted = leading_value * (1.0 + weights[row] / 448.0)
        target = measured_targets[row]
        predicted_angles[angle] = {
            "leading_angle": leading_value,
            "candidate_weight": weights[row],
            "candidate_correction_factor": 1.0 + weights[row] / 448.0,
            "candidate_prediction": predicted,
            "frozen_replay_target": target,
            "absolute_residual": predicted - target,
            "relative_residual": abs(predicted - target) / abs(target),
        }

    max_relative_residual = max(item["relative_residual"] for item in predicted_angles.values())
    prediction = {
        "schema": "MTTCKMAnglePredictionFromPiTraceLawCandidate.v1",
        "status": "CKM_ANGLE_PREDICTION_FROM_TRACE_LAW_CANDIDATE_EXECUTED",
        "normalization": contract["normalization"],
        "predicted_angles": predicted_angles,
        "max_relative_residual_against_frozen_replay": max_relative_residual,
        "orders_of_improvement_over_leading_map": {
            angle: leading["residuals_against_measured_replay"][angle]["relative_residual"]
            / predicted_angles[angle]["relative_residual"]
            for angle in ["s12", "s23", "s13"]
        },
        "observed_data_used_for_postcheck": True,
        "accepted_as_exact_ckm_closure": False,
    }

    acceptance = {
        "schema": "MTTPiCKMTraceLawAcceptanceCutset.v1",
        "status": "PICKM_TRACE_LAW_SOURCE_DERIVATION_CLAUSES_OPEN",
        "candidate_is_numerically_strong": True,
        "candidate_source_only_when_evaluated": True,
        "candidate_selected_by_diagnostic_postcheck_scan": True,
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_ckm_angle_rows": 0,
        "remaining_derivation_clauses": {
            "Pi_CKM_12_projector_derivation": "derive the 1/6 normalization and five sine branches from selected closure-cost fibers",
            "Pi_CKM_23_projector_derivation": "derive the 1/8 normalization and q-cos heavy-link term from selected closure-cost fibers",
            "Pi_CKM_13_projector_derivation": "derive the 1/18 normalization and 448/64 modulus term from selected long-bridge fibers",
        },
        "one_principle_upgrade_needed": (
            "derive the three rows as consequences of one selected closure-cost trace principle rather than three "
            "postcheck-selected formulas"
        ),
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector_for_source_closure": False,
        "target_fitting_used_to_accept_rows": False,
    }

    theorem = {
        "name": "PiCKMTraceLawCandidateTheorem",
        "proved": True,
        "statement": (
            "The current source stack admits a compact three-row Pi_CKM trace-law candidate evaluated only from "
            "selected q79, R_Z/R_X, and finite-modulus constants.  This candidate dramatically improves the CKM "
            "angle replay residuals, but it is not a selected row theorem because the projector derivation clauses "
            "remain open and the formulas were found by diagnostic postcheck scan."
        ),
    }

    data = {
        "candidate": "MTTSelectedPiCKMClosureCostTraceFunctionalOrAngleWeightRows",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "available_invariant_scan": rel(SCAN),
            "leading_ckm_angle_map": rel(LEADING),
            "sector_pair_projection_contract": rel(CONTRACT),
        },
        "output_packets": {
            "pickm_source_trace_law_candidate": rel(TRACE_LAW),
            "ckm_angle_prediction_from_trace_law_candidate": rel(PREDICTION),
            "pickm_trace_law_acceptance_cutset": rel(ACCEPTANCE),
        },
        "closure_decision": {
            "Pi_CKM_trace_law_candidate_built": True,
            "candidate_emits_three_numeric_weights": True,
            "selected_Pi_CKM_row_certificates": 0,
            "accepted_weight_rows": 0,
            "accepted_exact_ckm_correction_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "key_numbers": {
            "candidate_weights": weights,
            "frozen_replay_weight_obligations": target_weights,
            "max_relative_residual_against_frozen_replay": max_relative_residual,
            "accepted_eckm_weight_rows": 0,
            "remaining_derivation_clauses": 3,
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "diagnostic_postcheck_scan_used_for_discovery": True,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used_to_accept_rows": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PiCKMClosureCostTraceFunctional_or_AngleWeightRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "Pi_CKM_trace_law_candidate_built": True,
        "candidate_emits_three_numeric_weights": True,
        "selected_Pi_CKM_row_certificates": 0,
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "diagnostic_postcheck_scan_used_for_discovery": True,
        "target_fitting_used_to_accept_rows": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PiCKMClosureCostTraceFunctional or AngleWeightRows v1

Status: `{STATUS}`.

## Theorem

`PiCKMTraceLawCandidateTheorem` is proved.

The current source stack now has an explicit three-row `Pi_CKM` trace-law
candidate:

```text
W12 = (||R_Z||_F^2 + 5 sin(delta_79))/6
W23 = (sqrt(3) + 3 q |cos(delta_79)|/2)/8
W13 = (5 q + 3(448/64))/18
```

Evaluating these rows gives:

```text
W12 = {weights['W12']:.15f}
W23 = {weights['W23']:.15f}
W13 = {weights['W13']:.15f}
max relative CKM-angle residual = {max_relative_residual:.6e}
accepted W rows = 0/3
```

This is a strong candidate, but not a selected theorem yet.  The formulas were
identified by diagnostic postcheck scan, and the three closure-cost projector
derivation clauses remain open.

Next artifact: `{NEXT}`.
"""

    write_json(TRACE_LAW, trace_law)
    write_json(PREDICTION, prediction)
    write_json(ACCEPTANCE, acceptance)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
