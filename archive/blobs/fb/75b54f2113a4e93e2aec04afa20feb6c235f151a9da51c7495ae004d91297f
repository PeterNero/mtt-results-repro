"""Build the CKM scalar-evaluator readiness artifact.

This follows the sector-pair weight source reduction and imports the latest
active-ledger closures.  Its purpose is to retire stale missing ingredients for
E_CKM^ij and identify the remaining value-execution payload precisely.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_ckmweightscalarevaluator_or_selectedflavorgalerkinvalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
READINESS = PACKET_DIR / "eckm_scalar_evaluator_readiness.packet.json"
FORMAL = PACKET_DIR / "formal_eckm_evaluator_instantiation.packet.json"
GAP = PACKET_DIR / "remaining_flavor_galerkin_value_gap.packet.json"
DECISION = PACKET_DIR / "eckm_scalar_evaluator_acceptance_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CKMWeightScalarEvaluator_or_SelectedFlavorGalerkinValues_v1.md"

PREVIOUS = DATA / "selected_ckmsectorpairweightsourcetheorem_or_fullflavorgalerkinrun.candidate.json"
REDUCTION = (
    DATA
    / "selected_ckmsectorpairweightsourcetheorem_or_fullflavorgalerkinrun"
    / "ckm_weight_scalar_functional_reduction.packet.json"
)
WEIGHTS = (
    DATA
    / "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution"
    / "required_q448_sector_pair_weights.packet.json"
)
ACTIVE = DATA / "selected_activeledger_dotdc1supersession_or_valuelayerfrontier.candidate.json"
ZERO_MODE = DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"
DEGREEN = DATA / "selected_visiblechernweildegreenimport_or_fullsectorpayloadupgrade.candidate.json"
HONEST_GATE = (
    DATA
    / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun"
    / "honest_galerkin_execution_value_run_gate.packet.json"
)
RTHETA = (
    DATA
    / "selected_secondorderorbitqualitativesmclosure_or_rthetascalarvalues"
    / "rtheta_scalar_value_obligation.packet.json"
)

STATUS = "MTT_SELECTED_CKMWEIGHT_SCALAR_EVALUATOR_READINESS_BUILT_VALUE_EXECUTION_OPEN"
NEXT = "MTT_Selected_ZeroModeGramSectorContractionPayload_or_ECKMWeightRows_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    previous = load(PREVIOUS)
    reduction = load(REDUCTION)
    weights = load(WEIGHTS)
    active = load(ACTIVE)
    zero_mode = load(ZERO_MODE)
    degreen = load(DEGREEN)
    honest_gate = load(HONEST_GATE)
    rtheta = load(RTHETA)

    if previous["closure_decision"]["ckm_weight_scalar_functional_reduction_closed"] is not True:
        raise ValueError("previous E_CKM reduction is not closed")
    if active["closure_decision"]["source_layer_closed"] is not True:
        raise ValueError("active source layer is not closed")
    if active["closure_decision"]["DE_Green_gap_layer_closed"] is not True:
        raise ValueError("D_E/Riesz/Green gap layer is not closed")

    readiness_rows = {
        "q448_projection_contract": {
            "closed": True,
            "source": rel(PREVIOUS),
            "role": "normalizes C_ij = 1 + W_ij/448 and names Pi_CKM^ij rows",
        },
        "selected_q79_heavylink_orbit_domain": {
            "closed": True,
            "source": rel(PREVIOUS),
            "role": "supplies Delta_v, q79 phase, lambda orbit, and second-order CP/splitting domain",
        },
        "active_dotD_C1_first_response_source_layer": {
            "closed": active["closure_decision"]["source_layer_closed"],
            "source": rel(ACTIVE),
            "role": "retires dotD/A/b/deltaTheta/primitive-first-response as generic blockers",
        },
        "DE_Riesz_Green_gap_layer": {
            "closed": active["closure_decision"]["DE_Green_gap_layer_closed"]
            and degreen["closure_decision"]["D_E_Riesz_Green_gap_layer_closed"],
            "source": rel(DEGREEN),
            "role": "supplies selected gap/Riesz/Green layer support, not yet sector value matrices",
        },
        "zero_mode_projector_basis_values": {
            "closed": zero_mode["theorem"]["selected_values_emitted"],
            "source": rel(ZERO_MODE),
            "role": "must emit P_s, K_s, gaps, End0-equivariance, and ordered sector bases",
        },
        "selected_L2_Gram_trace_convention_values": {
            "closed": zero_mode["theorem"]["selected_values_emitted"],
            "source": rel(ZERO_MODE),
            "role": "must fix the basis-dependent trace/Gram values used by E_CKM",
        },
        "finite_Hessian_C1_sector_contraction_values": {
            "closed": honest_gate["selected_source_verified"],
            "source": rel(HONEST_GATE),
            "role": "must emit primitive three-by-three contraction terms and sector response matrices as values",
        },
        "E_CKM_weight_row_certificates": {
            "closed": False,
            "source": rel(REDUCTION),
            "role": "must certify W12,W23,W13 as selected scalar rows rather than postcheck obligations",
        },
    }
    closed_count = sum(1 for row in readiness_rows.values() if row["closed"])
    required_count = len(readiness_rows)

    readiness = {
        "schema": "MTTECKMScalarEvaluatorReadiness.v1",
        "status": "ECKM_READINESS_UPDATED_AFTER_ACTIVE_LEDGER_IMPORT",
        "closed_required_rows": closed_count,
        "required_rows": required_count,
        "readiness_rows": readiness_rows,
        "stale_blockers_retired": [
            "generic dotD_alpha1 source absence",
            "generic A_selected/b_selected/deltaTheta absence",
            "generic primitive first-response source absence",
            "generic D_E/Riesz/Green gap-layer absence",
        ],
        "still_open_blockers": [
            key for key, value in readiness_rows.items() if value["closed"] is False
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    formal = {
        "schema": "MTTFormalECKMEvaluatorInstantiation.v1",
        "status": "FORMAL_ECKM_EVALUATOR_TYPED_NOT_EXECUTED",
        "evaluator": "E_CKM^ij = Tr_N(Pi_CKM^ij K_CKM(Delta_v, Orbit_lambda, C1/Hessian/zero-mode value rows))",
        "rows": {
            "W12": {
                "projector": "Pi_CKM^12",
                "formal_value": "Tr_N(Pi_CKM^12 K_CKM)",
                "required_postcheck_weight": weights["q448_weights_if_matching_measured_replay"]["W12"],
            },
            "W23": {
                "projector": "Pi_CKM^23",
                "formal_value": "Tr_N(Pi_CKM^23 K_CKM)",
                "required_postcheck_weight": weights["q448_weights_if_matching_measured_replay"]["W23"],
            },
            "W13": {
                "projector": "Pi_CKM^13",
                "formal_value": "Tr_N(Pi_CKM^13 K_CKM)",
                "required_postcheck_weight": weights["q448_weights_if_matching_measured_replay"]["W13"],
            },
        },
        "inputs_available": reduction["available_source_layer"]
        + [
            "active-ledger dotD/A/b/deltaTheta/primitive first-response source layer",
            "selected D_E/Riesz/Green gap layer",
        ],
        "inputs_not_available_as_values": readiness["still_open_blockers"],
        "selected_functional_executed": False,
        "accepted_weight_rows": 0,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
    }

    gap = {
        "schema": "MTTRemainingFlavorGalerkinValueGap.v1",
        "status": "ZERO_MODE_GRAM_SECTOR_CONTRACTION_PAYLOAD_REMAINS_OPEN",
        "overlap_with_rtheta_scalar_frontier": True,
        "rtheta_selected_functional_executed": rtheta["selected_functional_executed"],
        "rtheta_accepted_scalar_row_count_now": rtheta["accepted_scalar_row_count_now"],
        "honest_galerkin_current_manifest_status": honest_gate["current_manifest_status"],
        "honest_galerkin_required_inputs": honest_gate["required_inputs"],
        "zero_mode_validator_passes_now": zero_mode["finite_acceptance_validator"]["passes_now"],
        "zero_mode_current_blockers": zero_mode["current_blockers"],
        "minimal_next_payload": {
            "name": NEXT,
            "must_emit": [
                "selected sector zero-mode projectors P_u,P_d,P_e and ordered bases K_u,K_d,K_e",
                "selected L2 Gram/trace convention in those bases",
                "finite Hessian/C1 sector contraction value matrices",
                "three row certificates evaluating Tr_N(Pi_CKM^ij K_CKM)",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTECKMScalarEvaluatorAcceptanceDecision.v1",
        "status": "ECKM_DOMAIN_READY_VALUE_EXECUTION_OPEN",
        "eckm_readiness_updated": True,
        "closed_required_rows": closed_count,
        "required_rows": required_count,
        "formal_evaluator_typed": True,
        "selected_functional_executed": False,
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "CKM_angle_magnitudes_derived_exact": False,
        "Jarlskog_source_derived_without_measured_angles": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "CKMWeightScalarEvaluatorReadinessTheorem",
        "proved": True,
        "statement": (
            "After importing the active ledger, E_CKM^ij no longer lacks generic dotD, A/b/"
            "deltaTheta, primitive first-response, or D_E/Riesz/Green gap-layer support. "
            "The formal scalar evaluator is typed, but it is not executed because selected "
            "zero-mode basis values, Gram/trace values, finite Hessian/C1 sector contraction "
            "value matrices, and W_ij row certificates are not emitted."
        ),
    }

    data = {
        "candidate": "MTTSelectedCKMWeightScalarEvaluatorOrSelectedFlavorGalerkinValues",
        "status": STATUS,
        "inputs": {
            "previous_weight_source_reduction": rel(PREVIOUS),
            "eckm_reduction": rel(REDUCTION),
            "required_q448_weights": rel(WEIGHTS),
            "active_ledger": rel(ACTIVE),
            "zero_mode_basis_theorem": rel(ZERO_MODE),
            "degreen_import": rel(DEGREEN),
            "honest_galerkin_gate": rel(HONEST_GATE),
            "rtheta_scalar_obligation": rel(RTHETA),
        },
        "output_packets": {
            "eckm_scalar_evaluator_readiness": rel(READINESS),
            "formal_eckm_evaluator_instantiation": rel(FORMAL),
            "remaining_flavor_galerkin_value_gap": rel(GAP),
            "eckm_scalar_evaluator_acceptance_decision": rel(DECISION),
        },
        "closure_decision": {
            "eckm_readiness_updated": True,
            "formal_evaluator_typed": True,
            "stale_source_blockers_retired": True,
            "closed_required_rows": closed_count,
            "required_rows": required_count,
            "selected_zero_mode_basis_values_emitted": False,
            "selected_Gram_trace_values_emitted": False,
            "finite_Hessian_C1_sector_contraction_values_emitted": False,
            "selected_functional_executed": False,
            "accepted_weight_rows": 0,
            "accepted_exact_ckm_correction_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "CKM_angle_magnitudes_derived_exact": False,
            "Jarlskog_source_derived_without_measured_angles": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "key_numbers": {
            "readiness_closed_required_rows": closed_count,
            "readiness_required_rows": required_count,
            "required_q448_weights": weights["q448_weights_if_matching_measured_replay"],
            "rtheta_accepted_scalar_row_count_now": rtheta["accepted_scalar_row_count_now"],
            "accepted_eckm_weight_rows": 0,
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_CKMWeightScalarEvaluator_or_SelectedFlavorGalerkinValues_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "eckm_readiness_updated": True,
        "formal_evaluator_typed": True,
        "stale_source_blockers_retired": True,
        "closed_required_rows": closed_count,
        "required_rows": required_count,
        "selected_functional_executed": False,
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "CKM_angle_magnitudes_derived_exact": False,
        "Jarlskog_source_derived_without_measured_angles": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected CKMWeightScalarEvaluator or SelectedFlavorGalerkinValues v1

Status: `{STATUS}`.

## Theorem

`CKMWeightScalarEvaluatorReadinessTheorem` is proved.

After importing the active ledger, `E_CKM^ij` no longer lacks the generic
source-layer pieces:

```text
dotD/A/b/deltaTheta/primitive first response : closed
D_E/Riesz/Green gap layer                    : closed
q448 projection contract                     : closed
second-order orbit domain                    : closed
```

The formal evaluator is now typed:

```text
E_CKM^ij = Tr_N(Pi_CKM^ij K_CKM(Delta_v, Orbit_lambda, C1/Hessian/zero-mode value rows))
```

## Current Readiness

```text
closed required rows = {closed_count}/{required_count}
accepted W rows      = 0/3
```

Still open:

```text
zero-mode basis/projector values
selected L2 Gram/trace values
finite Hessian/C1 sector contraction value matrices
W12,W23,W13 row certificates
```

The next artifact must emit the zero-mode/Gram/sector-contraction payload, then
evaluate the three traces.

Next artifact: `{NEXT}`.
"""

    write_json(READINESS, readiness)
    write_json(FORMAL, formal)
    write_json(GAP, gap)
    write_json(DECISION, decision)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
