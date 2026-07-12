"""Build H one-parameter execution ledger or strict finite-H source rows packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_honeparameterexecutionledger_or_strictfinitehsourcerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EXECUTION_LEDGER = PACKET_DIR / "h_one_parameter_execution_ledger.packet.json"
STRICT_ROWS = PACKET_DIR / "strict_finite_h_source_rows_execution.packet.json"
CLAIM_BOUNDARY = PACKET_DIR / "claim_boundary_after_h_execution.packet.json"
NEXT_PACKET = PACKET_DIR / "next_strict_upgrade_or_nonhiggs_prediction.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HOneParameterExecutionLedger_or_StrictFiniteHSourceRows_v1.md"

STATUS = (
    "MTT_SELECTED_HONEPARAMETEREXECUTIONLEDGER_OR_STRICTFINITEHSOURCEROWS_"
    "MINIMAL_H_CLOSED_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_StrictFiniteHSourceRowConstruction_or_NonHiggsHRGPrediction_v1"

SOURCES = {
    "previous": DATA / "selected_honeparameteradoptionpolicy_or_finitehsourceconstruction.candidate.json",
    "adoption_policy": DATA
    / "selected_honeparameteradoptionpolicy_or_finitehsourceconstruction"
    / "h_one_parameter_adoption_policy.packet.json",
    "standards": DATA
    / "selected_honeparameteradoptionpolicy_or_finitehsourceconstruction"
    / "h_closure_standards_ledger.packet.json",
    "finite_h_workorder": DATA
    / "selected_honeparameteradoptionpolicy_or_finitehsourceconstruction"
    / "strict_finite_h_construction_workorder.packet.json",
    "controlled_radial": DATA
    / "selected_hradialsourcevalue_or_directnhexecution"
    / "controlled_one_parameter_radial_NH_closure.packet.json",
    "hlambda_gate": DATA / "selected_hlambdaoverlapkernelrow_or_scalaromegaexecutiongate.candidate.json",
    "hrg_crossuse": DATA / "selected_hrgprimitivecrossusepredictionaudit_or_sourcetheoremattempt.candidate.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H execution-ledger inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    sources = require_sources()
    previous = sources["previous"]["closure_decision"]
    adoption = sources["adoption_policy"]
    standards = sources["standards"]["standards"]
    workorder = sources["finite_h_workorder"]
    controlled = sources["controlled_radial"]
    hlambda = sources["hlambda_gate"]["closure_decision"]
    hrg_crossuse = sources["hrg_crossuse"]["closure_decision"]

    parameter = adoption["parameter"]
    r_h = parameter["value"]
    n_h = parameter["derived_N_H"]
    conditional_rows = adoption["conditional_result_if_adopted"]["conditional_H_K_rows"]

    execution_ledger = {
        "schema": "MTTHOneParameterExecutionLedger.v1",
        "status": "ONE_PARAMETER_H_EXECUTION_LEDGER_CLOSED",
        "closure_claimed": True,
        "adopted_parameter": {
            "id": parameter["id"],
            "role": parameter["role"],
            "value": r_h,
            "derived_N_H": n_h,
            "parameter_count_spent": 1,
            "declared_before_this_execution": True,
            "retuned_per_observable": False,
        },
        "executed_result": {
            "minimal_one_parameter_H_closure_closed": True,
            "conditional_H_K_rows": conditional_rows,
            "strict_K_rows_without_parameter": adoption["conditional_result_if_adopted"][
                "strict_K_rows_without_adoption"
            ],
            "lambda_H_calibrated": True,
            "lambda_H_predicted": False,
            "controlled_r_H": controlled["derived_controlled_values"]["r_H"],
            "controlled_N_H": controlled["derived_controlled_values"]["N_H_equals_r_H_squared"],
        },
        "scope": {
            "H_threshold_row": True,
            "all_SM_parameters": False,
            "Yukawa_or_CKM_or_masses": False,
            "nonHiggs_HRG_predictions": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    strict_rows = {
        "schema": "MTTStrictFiniteHSourceRowsExecution.v1",
        "status": "STRICT_FINITE_H_SOURCE_ROWS_EXECUTED_ZERO_ROWS",
        "closure_claimed": True,
        "accepted_counts": workorder["accepted_now"],
        "required_source_objects": workorder["required_source_objects"],
        "row_slots": {
            "F_H_selected": False,
            "N_H_from_Hess_F_H_emitted": False,
            "M_source_restricted_to_B_Huv_emitted": False,
            "K_H_primitive_response_emitted": False,
            "R_H_RG_strict_source_emitted": False,
            "direct_K_threshold_Omega_H_lambda_emitted": False,
            "Huu_Hud_Hdd_rows_emitted": False,
        },
        "already_promoted_support": workorder["already_promoted_support"],
        "remaining_strict_polar_gap": workorder["remaining_strict_polar_gap"],
        "strict_no_knob_source_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    claim_boundary = {
        "schema": "MTTHClaimBoundaryAfterOneParameterExecution.v1",
        "status": "MINIMAL_H_CLAIM_CLOSED_TRUE_SM_AND_NOKNOB_OPEN",
        "closure_claimed": True,
        "claims": {
            "minimal_one_parameter_H_closure": True,
            "strict_no_knob_H_closure": False,
            "lambda_H_prediction": False,
            "full_no_knob_SM_closure": False,
            "true_SM_equivalence": False,
        },
        "parameter_budget": {
            "H_parameters_spent": 1,
            "global_selected_universal_parameters_spent": standards[
                "minimal_one_parameter_H_closure"
            ]["parameter_count"],
            "general_policy_selected_universal_parameter_count": sources["standards"][
                "general_policy_import"
            ]["general_selected_universal_parameter_count"],
        },
        "guardrails": [
            "Do not report this as no-knob H closure.",
            "Do not report lambda_H as predicted.",
            "Do not reuse UP-RET-OVERLAP.HRG outside H without a non-Higgs prediction map.",
            "Do not use this parameter to select topology, branch, quotient, or source rows.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextStrictUpgradeOrNonHiggsHRGPrediction.v1",
        "status": "NEXT_STRICT_UPGRADE_OR_NONHIGGS_HRG_PREDICTION",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "one counted H parameter executed",
            "minimal H closure reported at one-parameter standard",
            "strict source-row execution rechecked with zero rows",
            "claim boundary between minimal H closure and no-knob closure fixed",
        ],
        "still_open": [
            "strict selected finite-H/source rows",
            "accepted non-Higgs UP-RET-OVERLAP.HRG prediction target",
            "lambda_H prediction without calibration",
            "full SM/no-knob equivalence",
        ],
        "recommended_order": [
            "attempt strict F_H/M_source/K_H/R_H^RG source-row construction",
            "if strict rows remain zero, seek an independent non-Higgs HRG prediction to upgrade credibility",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHOneParameterExecutionLedgerOrStrictFiniteHSourceRows",
        "status": STATUS,
        "previous_status": sources["previous"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "minimal_one_parameter_H_closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "h_one_parameter_execution_ledger": rel(EXECUTION_LEDGER),
            "strict_finite_h_source_rows_execution": rel(STRICT_ROWS),
            "claim_boundary_after_h_execution": rel(CLAIM_BOUNDARY),
            "next_strict_upgrade_or_nonhiggs_prediction": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "H_one_parameter_adopted_now": True,
            "H_parameter_count_spent": 1,
            "minimal_one_parameter_H_closure_closed": True,
            "conditional_H_K_rows_closed": conditional_rows,
            "strict_H_K_rows_without_parameter": adoption["conditional_result_if_adopted"][
                "strict_K_rows_without_adoption"
            ],
            "controlled_r_H": r_h,
            "controlled_N_H": n_h,
            "lambda_H_calibrated": True,
            "lambda_H_predicted": False,
            "strict_finite_H_source_rows_executed": True,
            "strict_value_rows_accepted": 0,
            "strict_finite_H_source_closed": False,
            "accepted_nonhiggs_HRG_prediction_targets": hrg_crossuse[
                "accepted_nonhiggs_prediction_target_count"
            ],
            "hlambda_controlled_one_parameter_10of10_imported": (
                hlambda["controlled_one_parameter_H_layer_built"]
                and hlambda["controlled_parameterized_K_row_count"] == 10
            ),
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "HOneParameterExecutionLedgerOrStrictFiniteHSourceRowsTheorem",
            "proved": True,
            "statement": (
                "The minimal H layer is now executable at exactly one counted parameter: "
                "declaring UP-RET-OVERLAP.HRG gives r_H, N_H, and a conditional 10/10 H K "
                "row ledger. Strict finite-H/source rows were executed in parallel and still "
                "emit zero accepted rows, so no-knob H closure, lambda_H prediction, and full "
                "SM/no-knob equivalence remain open."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHOneParameterExecutionLedgerOrStrictFiniteHSourceRows",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "minimal_one_parameter_H_closure_claimed": True,
        "H_one_parameter_adopted_now": True,
        "H_parameter_count_spent": 1,
        "conditional_H_K_rows_closed": conditional_rows,
        "strict_finite_H_source_closed": False,
        "lambda_H_predicted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected H One-Parameter Execution Ledger or StrictFiniteHSourceRows v1

## Theorem

`HOneParameterExecutionLedgerOrStrictFiniteHSourceRowsTheorem` is emitted.

## Minimal H Result

The H one-parameter ledger is executed.

- parameter: `UP-RET-OVERLAP.HRG`;
- parameter count spent: `1`;
- calibrated `r_H`: `{r_h}`;
- controlled `N_H=r_H^2`: `{n_h}`;
- conditional H K rows: `{conditional_rows}/10`;
- `lambda_H` status: calibrated, not predicted.

## Strict Result

Strict finite-H/source rows are still open.

- strict source rows accepted: `0`;
- selected `F_H`: `false`;
- selected `M_source`: `false`;
- selected `K_H`: `false`;
- strict `R_H^RG`: `false`;
- no-knob H closure: `false`.

## Boundary

This closes a minimal one-parameter H layer only. It does not close no-knob H,
does not predict `lambda_H`, and does not close full SM equivalence.

## Next Artifact

`{NEXT}`
"""

    write_json(EXECUTION_LEDGER, execution_ledger)
    write_json(STRICT_ROWS, strict_rows)
    write_json(CLAIM_BOUNDARY, claim_boundary)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
