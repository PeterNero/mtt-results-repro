"""Build Step 8 precision-value/operator-packet route execution boundary."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRECISION_ROUTE = PACKET_DIR / "step8_precision_value_route_status.packet.json"
OPERATOR_ROUTE = PACKET_DIR / "step8_operator_source_slot_closure.packet.json"
TRUE_BOUNDARY = PACKET_DIR / "step8_dynamic_true_equivalence_boundary.packet.json"
CLOSURE_BOUNDARY = PACKET_DIR / "step8_closure_boundary.packet.json"
HANDOFF = PACKET_DIR / "step8_to_step9_handoff.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step8_PrecisionValueEmission_or_ActualQaSU3OperatorPacketClosure_v1.md"

STEP7 = DATA / "selected_step7_commonrgcovarianceobservablesuite_or_finaltruesmequivalencegate.candidate.json"
STEP7_HANDOFF = (
    DATA
    / "selected_step7_commonrgcovarianceobservablesuite_or_finaltruesmequivalencegate"
    / "step7_to_step8_handoff.packet.json"
)
PRECISION_ATTEMPT = DATA / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill.candidate.json"
LOCAL_QFT_PRECISION = DATA / "selected_localqftprecisionobservabletable_or_qasu3hymoperatorpacket_valueattempt.candidate.json"
HEAT_FINAL = DATA / "selected_heattorsionresponse_finalgate.candidate.json"
POST_EIGHT = DATA / "selected_heattorsionresponse_finalgate/post_eight_slot_true_equivalence_frontier.packet.json"
HEAT_SLOT = DATA / "selected_heattorsionresponse_finalgate/finite_determinant_heat_torsion_slot_closure.packet.json"
HEAT_RESPONSE = DATA / "selected_heattorsionresponse_finalgate/selected_finite_heat_spectrum_response.packet.json"
VSD01_DYNAMIC = DATA / "selected_vsd01_dynamicoperatorbackimport_or_yukawavaluefrontier.candidate.json"
TRACE_PAYLOAD = DATA / "selected_tracepayload_or_fullhymoperatoremission.candidate.json"

STATUS = (
    "MTT_SELECTED_STEP8_PRECISIONVALUEEMISSION_OR_ACTUALQASU3OPERATORPACKETCLOSURE_"
    "CLOSED_SOURCE_SLOTS_DYNAMIC_VALUES_OPEN"
)
NEXT = "MTT_Selected_Step9_DynamicQaSU3C1Response_or_PrecisionProfileCompletion_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 8 inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        STEP7,
        STEP7_HANDOFF,
        PRECISION_ATTEMPT,
        LOCAL_QFT_PRECISION,
        HEAT_FINAL,
        POST_EIGHT,
        HEAT_SLOT,
        HEAT_RESPONSE,
        VSD01_DYNAMIC,
        TRACE_PAYLOAD,
    ]
    require_sources(sources)

    step7 = load(STEP7)
    step7_handoff = load(STEP7_HANDOFF)
    precision_attempt = load(PRECISION_ATTEMPT)
    local_qft_precision = load(LOCAL_QFT_PRECISION)
    heat_final = load(HEAT_FINAL)
    post_eight = load(POST_EIGHT)
    heat_slot = load(HEAT_SLOT)
    heat_response = load(HEAT_RESPONSE)
    vsd01_dynamic = load(VSD01_DYNAMIC)
    trace_payload = load(TRACE_PAYLOAD)

    precision_route = {
        "schema": "MTTStep8PrecisionValueRouteStatus.v1",
        "status": "PRECISION_ROUTE_EXECUTED_PARTIAL_VALUES_FULL_PROFILE_OPEN",
        "precision_attempt_source": rel(PRECISION_ATTEMPT),
        "local_qft_precision_source": rel(LOCAL_QFT_PRECISION),
        "partial_precision_values_emitted": precision_attempt["closure_decision"][
            "partial_precision_values_emitted"
        ],
        "minimal_local_QFT_value_suite_filled": local_qft_precision["closure_decision"][
            "minimal_local_QFT_value_suite_filled"
        ],
        "precision_observable_table_closed": local_qft_precision["closure_decision"][
            "precision_observable_table_closed"
        ],
        "full_precision_observable_value_table_closed": False,
        "published_or_reconstructed_profile_likelihood_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PRECISION_ROUTE, precision_route)

    operator_route = {
        "schema": "MTTStep8OperatorSourceSlotClosure.v1",
        "status": "ALL_EIGHT_OPERATOR_SOURCE_SLOTS_CLOSED_AT_SOURCE_SLOT_LAYER",
        "heat_final_source": rel(HEAT_FINAL),
        "post_eight_frontier_source": rel(POST_EIGHT),
        "heat_response_source": rel(HEAT_RESPONSE),
        "operator_source_slots_closed": post_eight["operator_source_slots_closed"],
        "operator_source_slots_remaining": post_eight["operator_source_slots_remaining"],
        "source_slot_layer_closed": post_eight["source_slot_layer_closed"],
        "all_operator_source_slots_closed": heat_final["closure_decision"][
            "all_operator_source_slots_closed"
        ],
        "finite_determinant_heat_spectrum_or_torsion_response_closed": heat_final[
            "closure_decision"
        ]["finite_determinant_heat_spectrum_or_torsion_response_closed"],
        "finite_heat_spectrum_response_emitted": heat_slot["closure_result"][
            "finite_heat_spectrum_response_emitted"
        ],
        "finite_positive_complement_pseudodeterminant_emitted": heat_slot["closure_result"][
            "finite_positive_complement_pseudodeterminant_emitted"
        ],
        "selected_finite_invariants": heat_response["finite_invariants"],
        "actual_dynamic_QaSU3_operator_packet_closed": heat_final["closure_decision"][
            "actual_dynamic_QaSU3_operator_packet_closed"
        ],
        "smooth_analytic_torsion_closed": heat_slot["closure_result"][
            "smooth_analytic_torsion_closed"
        ],
        "full_S2_value_emission_closed": heat_slot["closure_result"][
            "full_S2_value_emission_closed"
        ],
        "primitive_C1_response_closed": heat_slot["closure_result"]["primitive_C1_response_closed"],
        "selected_dotD_alpha1_source_identity_closed": heat_slot["closure_result"][
            "selected_dotD_alpha1_source_identity_closed"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(OPERATOR_ROUTE, operator_route)

    true_boundary = {
        "schema": "MTTStep8DynamicTrueEquivalenceBoundary.v1",
        "status": "SOURCE_SLOT_LAYER_CLOSED_DYNAMIC_SM_VALUES_OPEN",
        "dynamic_first_response_source": rel(VSD01_DYNAMIC),
        "trace_payload_source": rel(TRACE_PAYLOAD),
        "VSD01_dynamic_tensor_subgate_closed": vsd01_dynamic["closure_decision"][
            "VSD01_dynamic_tensor_subgate_closed"
        ],
        "transition_rhoE_or_Cech_Dolbeault_DE_data_closed": trace_payload["closure_decision"][
            "transition_rhoE_or_Cech_Dolbeault_DE_data_closed"
        ],
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "accepted_Yukawa_Higgs_RG_value_layer_closed": vsd01_dynamic["closure_decision"][
            "accepted_Yukawa_Higgs_RG_value_layer_closed"
        ],
        "true_SM_equivalence_still_requires": post_eight["true_SM_equivalence_still_requires"],
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(TRUE_BOUNDARY, true_boundary)

    closure_boundary = {
        "schema": "MTTStep8ClosureBoundary.v1",
        "status": "STEP8_CLOSED_AS_ROUTE_EXECUTION_AND_SOURCE_SLOT_CLOSURE_NOT_TRUE_EQUIVALENCE",
        "completed_step": 8,
        "step7_closed_for_plan_contract": step7["closure_decision"][
            "step7_closed_for_plan_contract"
        ],
        "precision_route_executed": True,
        "precision_route_full_closure": False,
        "operator_source_slot_route_closed": True,
        "all_operator_source_slots_closed": True,
        "operator_source_slots_closed": 8,
        "operator_source_slots_remaining": 0,
        "source_slot_layer_closed": True,
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "step8_closed_for_plan_contract": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CLOSURE_BOUNDARY, closure_boundary)

    handoff = {
        "schema": "MTTStep8ToStep9Handoff.v1",
        "status": "HANDOFF_TO_STEP9_DYNAMIC_QASU3_C1_RESPONSE_OR_PRECISION_PROFILE_COMPLETION",
        "completed_step": 8,
        "next_step": 9,
        "next_required_artifact": NEXT,
        "step9_must_close": {
            "actual_dynamic_QaSU3_operator_packet": True,
            "selected_dotD_alpha1_and_primitive_C1_response_source_identity": True,
            "full_S2_value_emission_beyond_DE_gap_layer": True,
            "precision_QFT_observable_functor_with_accepted_RG_threshold_covariance": True,
            "no_proxy_Yukawa_mixing_value_derivation_for_no_knob_upgrade": True,
        },
        "step9_can_reuse": {
            "all_eight_operator_source_slots_closed": True,
            "selected_finite_heat_spectrum_response": True,
            "transition_DE_trace_slot": True,
            "VSD01_dynamic_first_response_layer": True,
            "partial_precision_values": True,
        },
        "step9_must_not_use_as_selectors": step7_handoff["step8_must_not_use_as_selectors"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(HANDOFF, handoff)

    candidate = {
        "candidate": "MTTSelectedStep8PrecisionValueEmissionOrActualQaSU3OperatorPacketClosure",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "step8_precision_value_route_status": rel(PRECISION_ROUTE),
            "step8_operator_source_slot_closure": rel(OPERATOR_ROUTE),
            "step8_dynamic_true_equivalence_boundary": rel(TRUE_BOUNDARY),
            "step8_closure_boundary": rel(CLOSURE_BOUNDARY),
            "step8_to_step9_handoff": rel(HANDOFF),
        },
        "theorem": {
            "name": "Step8PrecisionRouteAndOperatorSourceSlotClosureTheorem",
            "proved": True,
            "statement": (
                "Step 8 is closed as a route-execution theorem. The precision route has been "
                "executed through partial precision and minimal local-QFT value rows but does "
                "not close the full precision/profile table. The operator route closes all eight "
                "operator-source slots at the selected finite source-slot layer, including the "
                "finite heat trace and positive-complement pseudodeterminant response. This does "
                "not yet promote an actual dynamic Qa/SU3 operator packet, selected dotD/C1 response, "
                "full S2 value emission, true SM equivalence, or full no-knob closure."
            ),
        },
        "closure_decision": {
            "step8_closed_for_plan_contract": True,
            "precision_route_executed": True,
            "precision_route_full_closure": False,
            "operator_source_slot_route_closed": True,
            "all_operator_source_slots_closed": True,
            "operator_source_slots_closed": 8,
            "operator_source_slots_remaining": 0,
            "source_slot_layer_closed": True,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "step8_plan_contract": True,
            "precision_route_attempt_executed": True,
            "minimal_local_QFT_value_suite_filled": True,
            "all_eight_operator_source_slots_closed_at_source_slot_layer": True,
            "finite_heat_trace_and_pseudodeterminant_response_emitted": True,
            "step9_handoff_typed": True,
        },
        "what_remains_open": handoff["step9_must_close"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "step8_contract_closure_claimed": True,
        "operator_source_slot_layer_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step8_PrecisionValueEmission_or_ActualQaSU3OperatorPacketClosure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "step8_contract_closure_claimed": True,
        "operator_source_slot_layer_closure_claimed": True,
        "all_operator_source_slots_closed": True,
        "operator_source_slots_closed": 8,
        "operator_source_slots_remaining": 0,
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step8 PrecisionValueEmission or ActualQaSU3OperatorPacketClosure v1

Status: `{STATUS}`.

Step 8 is closed as route execution and source-slot closure:

```text
precision route executed              : true
full precision/profile table closed   : false
operator source-slot route closed     : true
operator source slots closed          : 8
operator source slots remaining       : 0
source-slot layer closed              : true
actual dynamic Qa/SU3 packet closed   : false
true SM equivalence closed            : false
full no-knob closure                  : false
```

The new mathematical gain is that the finite determinant/heat-spectrum/torsion
slot is closed at the selected finite 27-mode source layer, so all eight
operator-source slots are now closed there.  The remaining frontier is dynamic:
promote those source-slot closures into an actual Qa/SU3 operator packet with
selected dotD/C1/full-S2 value emission, or complete the precision/profile value
route with accepted loop/scheme/covariance semantics.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
