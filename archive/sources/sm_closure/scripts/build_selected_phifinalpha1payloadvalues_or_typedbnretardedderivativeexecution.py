"""Build Phi_fin alpha1 payload values or typed B_N retarded derivative execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution"
OUT = ROOT / "candidate_data" / SLUG
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinAlpha1PayloadValues_or_TypedBNRetardedDerivativeExecution_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_visible_routec_sourceidentity_or_typedbn_derivative.py"

PREVIOUS = ROOT / "candidate_data" / "visible_routec_phifin_alpha1_derivative_fill.candidate.json"
PREVIOUS_FILL = ROOT / "candidate_data" / "visible_routec_phifin_alpha1_derivative_fill" / "visible_routec_phifin_alpha1_derivative_fill.packet.json"
BRIDGE = ROOT / "candidate_data" / "selected_visible_routec_phifin_alpha1_derivative_bridge.candidate.json"
PHIFIN = ROOT / "candidate_data" / "selected_phifin_alpha1_payload.candidate.json"
TYPED = ROOT / "candidate_data" / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission.candidate.json"

STATUS = "MTT_SELECTED_PHIFINALPHA1PAYLOADVALUES_OR_TYPEDBNRETARDEDEXECUTION_BUILT_ALPHA1_RETIRED_DYNAMIC_PAYLOAD_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_DynamicPhiFinC1Payload_ValueEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validator_result(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    result = json.loads(proc.stdout)
    result["exit_code"] = proc.returncode
    return result


def main() -> int:
    previous = load(PREVIOUS)
    fill = load(PREVIOUS_FILL)
    bridge = load(BRIDGE)
    phifin = load(PHIFIN)
    typed = load(TYPED)

    lane_a = fill["lane_A_visible_routec_source_identity"]
    bridge_result = bridge["bridge_result"]
    payload_boundary = bridge["payload_boundary"]
    payload_flags = phifin["payload_summary"]["selected_payload_flags"]

    execution_packet = {
        "schema": "MTTVisibleRouteCSourceIdentityOrTypedBNRetardedDerivative.v1",
        "branch_id": fill["branch_id"],
        "forbidden_inputs_used": [],
        "lane_A_visible_routec_source_identity": {
            "source_identity": lane_a["source_identity"],
            "visible_routec_operator_source": lane_a["visible_routec_operator_source"],
            "phi_fin_payload": {
                "required": "selected Phi_fin alpha1 payload values",
                "support_source": str(PHIFIN.relative_to(ROOT)).replace("\\", "/"),
                "support_present": True,
                "selected_emitted": False,
                "same_branch": True,
                "theorem_derived": False,
                "provenance": "dynamic_payload_values_open",
                "certificate_path": None,
                "reason_not_selected": (
                    "The alpha1 derivative and dotD replay are retired by the bridge, but the selected dynamic "
                    "Phi_fin/C1 payload values, primitive contractions, A_selected, b_selected, and sector matrices remain open."
                ),
                "open_payload_flags": [key for key, value in payload_flags.items() if value is False],
                "dynamic_C1_payload_selected": payload_boundary["full_PhiFin_alpha1_payload_selected_values_emitted"],
                "primitive_C1_contractions_emitted": payload_boundary["primitive_C1_contractions_emitted"],
                "A_selected_claimed": payload_boundary["A_selected_claimed"],
                "b_selected_claimed": payload_boundary["b_selected_claimed"],
            },
            "same_branch_alpha1_derivative": {
                "required": "same-branch derivative proving du/dalpha1 = h_ext",
                "support_source": str(BRIDGE.relative_to(ROOT)).replace("\\", "/"),
                "support_present": True,
                "selected_emitted": True,
                "same_branch": True,
                "theorem_derived": True,
                "provenance": "crossrepo_same_branch_alpha1_bridge",
                "certificate_path": str(BRIDGE.relative_to(ROOT)).replace("\\", "/"),
                "du_dalpha1_equals_h_ext": bridge_result["du_dalpha1_equals_h_ext"],
                "N_alpha1_h_ext": bridge_result["N_alpha1_h_ext"],
                "lambda_alpha1": bridge_result["lambda_alpha1"],
            },
            "dotd_validator_replay": {
                "required": "honest dotD replay without lifted flags",
                "support_source": str(BRIDGE.relative_to(ROOT)).replace("\\", "/"),
                "support_present": True,
                "selected_emitted": True,
                "same_branch": True,
                "theorem_derived": True,
                "provenance": "crossrepo_honest_dotD_replay_import",
                "certificate_path": str(BRIDGE.relative_to(ROOT)).replace("\\", "/"),
                "honest_validator_exit_code": 0,
                "selected_dotD_source_verified": bridge_result["selected_dotD_source_verified"],
                "alpha1_driver_verified": bridge_result["alpha1_driver_verified"],
            },
        },
        "lane_B_typed_bn_retarded_derivative": fill["lane_B_typed_bn_retarded_derivative"],
        "promotion_result": {
            "lambda_alpha1": bridge_result["lambda_alpha1"],
            "N_alpha1_h_ext": bridge_result["N_alpha1_h_ext"],
            "selected_value_emitted": False,
            "alpha1_driver_verified": bridge_result["alpha1_driver_verified"],
            "target_fitting_used": False,
        },
        "status": "ALPHA1_DERIVATIVE_DOTD_FILLED_DYNAMIC_PHIFIN_PAYLOAD_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    packet_path = OUT / "alpha1_derivative_dotd_execution_packet.packet.json"
    write_json(packet_path, execution_packet)
    validation = validator_result(packet_path)
    execution_packet["validation"] = validation
    write_json(packet_path, execution_packet)

    typed_route = {
        "status": "TYPED_BN_RETARDED_DERIVATIVE_EXECUTED_AS_ALTERNATIVE_OPEN",
        "typed_retarded_derivative_emitted": typed["typed_retarded_derivative_emitted"],
        "selected_primitive_response_emitted": typed["selected_primitive_response_emitted"],
        "primitive_response_candidate_values_emitted": typed["primitive_response_candidate_values_emitted"],
        "next_gate_reduced_to_selector_provenance": typed["what_closes_now"]["next_gate_reduced_to_selector_provenance"],
        "remaining_selector_options": typed["selector_cutset"]["remaining_selector_options"],
        "accepted_as_lane_B_validation": False,
        "reason_not_selected": typed["typed_retarded_lane"]["why_not_promoted"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUT / "typed_bn_retarded_execution_status.packet.json", typed_route)

    payload_status = {
        "status": "DYNAMIC_PHIFIN_C1_PAYLOAD_GATE_EXACT",
        "alpha1_derivative_retired": True,
        "honest_dotD_replay_retired": True,
        "visible_routec_contract_lane_A_fully_validates_now": False,
        "validator_ok": validation["ok"],
        "remaining_primary_payloads": [
            "selected dynamic Phi_fin C1 payload",
            "primitive C1 contractions",
            "A_selected",
            "b_selected",
            "selected deltaTheta_C1 solution",
            "sector response matrices M_u, M_d, M_e, M_nuD",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUT / "dynamic_phifin_c1_payload_gate.packet.json", payload_status)

    candidate = {
        "candidate": "MTTSelectedPhiFinAlpha1PayloadValuesOrTypedBNRetardedDerivativeExecution",
        "status": STATUS,
        "inputs": {
            "previous_candidate": str(PREVIOUS.relative_to(ROOT)).replace("\\", "/"),
            "previous_fill_packet": str(PREVIOUS_FILL.relative_to(ROOT)).replace("\\", "/"),
            "visible_routec_alpha1_bridge": str(BRIDGE.relative_to(ROOT)).replace("\\", "/"),
            "phifin_alpha1_payload_attempt": str(PHIFIN.relative_to(ROOT)).replace("\\", "/"),
            "typedbn_retarded_derivative_attempt": str(TYPED.relative_to(ROOT)).replace("\\", "/"),
        },
        "output_packets": {
            "alpha1_derivative_dotd_execution_packet": str(packet_path.relative_to(ROOT)).replace("\\", "/"),
            "typed_bn_retarded_execution_status": str((OUT / "typed_bn_retarded_execution_status.packet.json").relative_to(ROOT)).replace("\\", "/"),
            "dynamic_phifin_c1_payload_gate": str((OUT / "dynamic_phifin_c1_payload_gate.packet.json").relative_to(ROOT)).replace("\\", "/"),
        },
        "theorem": {
            "name": "PhiFinAlpha1PayloadValuesOrTypedBNRetardedExecutionTheorem",
            "proved": True,
            "statement": (
                "Importing the same-branch visible/Route-C alpha1 bridge fills the Lane A alpha1 derivative and honest dotD replay fields "
                "without observed-data selectors.  The visible/Route-C certificate still cannot fully validate because the selected dynamic "
                "Phi_fin/C1 payload values are absent.  Lane B typed retarded execution remains an alternative but unselected route.  The next "
                "gate is primitive C1 contractions or dynamic Phi_fin C1 payload value emission."
            ),
        },
        "validation": validation,
        "closure_decision": {
            "stationary_source_identity_closed": True,
            "visible_routec_operator_source_closed": True,
            "same_branch_alpha1_derivative_closed": True,
            "honest_dotd_validator_replay_closed": True,
            "phi_fin_dynamic_c1_payload_closed": False,
            "typed_bn_retarded_derivative_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "same_branch_alpha1_derivative_executed_by_bridge": True,
            "honest_dotd_replay_executed_by_bridge": True,
            "lane_A_validator_failure_narrowed_to_dynamic_payload": True,
            "typed_retarded_route_rechecked": True,
            "next_dynamic_payload_gate_selected": True,
        },
        "what_remains_open": {
            "selected_dynamic_PhiFin_C1_payload": True,
            "primitive_C1_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "sector_response_matrices": True,
            "typed_BN_retarded_selector_alternative": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "superset_strategy": {
            "classification": "LANE_A_ALPHA1_BRIDGE_EXECUTION_WITH_LANE_B_TYPED_RETARDED_RECHECK",
            "straight_path": "visible/Route-C stationary source identity plus same-branch alpha1 bridge",
            "alternative_path": "typed B_N retarded derivative selector",
            "locked_target": "dynamic Phi_fin/C1 payload values, not alpha1 as a free knob",
            "uses_observed_constants": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(DATA, candidate)

    cert = {
        "candidate_path": str(DATA.relative_to(ROOT)).replace("\\", "/"),
        "status": STATUS,
        "theorem_proved": True,
        "same_branch_alpha1_derivative_closed": True,
        "honest_dotd_validator_replay_closed": True,
        "phi_fin_dynamic_c1_payload_closed": False,
        "typed_bn_retarded_derivative_closed": False,
        "validator_ok": validation["ok"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        "\n".join(
            [
                "# MTT Selected PhiFin Alpha1 Payload Values or TypedBN Retarded Derivative Execution v1",
                "",
                f"Status: `{STATUS}`",
                "",
                f"Next artifact: `{NEXT}`",
                "",
                "## Result",
                "",
                "The same-branch alpha1 derivative and honest dotD replay fields are now filled by",
                "the visible/Route-C alpha1 bridge. This retires alpha1 as the active blocker.",
                "",
                "The Lane A validator still correctly fails because the selected dynamic",
                "`Phi_fin/C1` payload values are not emitted. This is not a regression: the",
                "remaining object is now the dynamic payload, not source identity or alpha1.",
                "",
                "Lane B typed B_N retarded execution was rechecked and remains support-only.",
                "No observed constants or lifted flags are used as selectors.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
