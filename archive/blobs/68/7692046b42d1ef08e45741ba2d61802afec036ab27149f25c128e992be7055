"""Import dynamic overlap-kernel or C1-primitive source-emission reduction."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "smslotfunctor_downstream_operator_payload_ledger_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_dynamic_overlapkernel_or_c1primitive_source_emission.candidate.json"
SM_CERT = SM / "certificates" / "selected_dynamic_overlapkernel_or_c1primitive_source_emission_certificate.json"

OUTPUT_PACKET = DATA / "dynamic_overlap_or_c1primitive_source_emission_import.candidate.json"
OUTPUT_CERT = CERTS / "dynamic_overlap_or_c1primitive_source_emission_import_certificate.json"
OUTPUT_NOTE = CORPUS / "DynamicOverlap_or_C1Primitive_SourceEmission_Import_v1.md"

STATUS = "DYNAMIC_OVERLAP_OR_C1PRIMITIVE_REDUCTION_IMPORTED_TYPED_DERIVATIVE_VALUES_OPEN"
PREVIOUS_STATUS = "SMSLOTFUNCTOR_DOWNSTREAM_LEDGER_IMPORTED_STATIC_PROMOTED_DYNAMIC_OPEN"
SM_STATUS = (
    "MTT_SELECTED_DYNAMIC_OVERLAPKERNEL_OR_C1PRIMITIVE_SOURCE_EMISSION_"
    "REDUCED_TYPED_DERIVATIVE_PRIMITIVE_VALUES_OPEN"
)
NEXT = "Selected_U1Y_RouteC_TypedBN_RetardedDerivative_or_PrimitiveResponse_ValueEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    lanes = sm_packet["lanes"]
    cutset = sm_packet["dynamic_cutset"]
    static_import = sm_packet["static_import"]
    remains = sm_packet["what_remains_open"]

    lane_a = lanes["A_same_source_alpha1_strength"]
    lane_b = lanes["B_typed_retarded_derivative"]
    lane_c = lanes["C_selected_C1_primitive_or_vertex"]

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_dynamic_reduction_proved": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and sm_cert["dynamic_kernel_emitted"] is False
        and sm_cert["selected_C1_primitive_emitted"] is False,
        "G2_static_import_consumed": static_import["sector_pair_partition_closed_static"] is True
        and static_import["oneM_Dirac_rule_closed_static"] is True
        and static_import["finite_trace_transfer_closed_static"] is True
        and static_import["dynamic_C1_operator_values_closed"] is False,
        "G3_lane_A_alpha1_ready_but_open": lane_a["closed"] is False
        and lane_a["source_identity_selected"] is True
        and lane_a["lambda_alpha1_candidate"] == 1.0
        and lane_a["h_ext_residual_l2"] < 1e-10,
        "G4_lane_B_typed_derivative_ready_but_open": lane_b["closed"] is False
        and lane_b["dotD_source_algebra_closed"] is True
        and lane_b["validator_math_passes_if_driver_is_theorem_derived"] is True
        and lane_b["typed_BN_tangent_or_retarded_kernel_emitted"] is False
        and lane_b["honest_dotD_replay_from_kernel"] is False,
        "G5_lane_C_primitive_candidates_ready_but_open": lane_c["closed"] is False
        and lane_c["canonical_mode_conserving_C1_zero"] is True
        and lane_c["noninvariant_active_shift_forced"] is True
        and lane_c["noninvariant_candidates_nonzero"] is True
        and lane_c["conditional_weylpair_A_exact"] is True
        and lane_c["promote_to_A_selected"] is False,
        "G6_minimal_remaining_objects_named": all(cutset["already_closed_or_reduced"].values())
        and len(cutset["remaining_minimal_objects"]) == 4,
        "G7_no_target_or_closure_overclaim": sm_packet["closure_claimed"] is False
        and sm_packet["dynamic_kernel_emitted"] is False
        and sm_packet["selected_C1_primitive_emitted"] is False
        and sm_packet["A_selected_claimed"] is False
        and sm_packet["b_selected_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False,
    }

    return {
        "packet": "DynamicOverlap_or_C1Primitive_SourceEmission_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_dynamic_reduction_packet": str(SM_PACKET),
            "sm_dynamic_reduction_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "DynamicOverlapOrC1PrimitiveReductionImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "After static SM-slot routing and finite trace transfer are closed, "
                "the remaining C1 obstruction is dynamic. The legal lanes are now "
                "separated: alpha1 source-strength/retarded derivative, typed "
                "B_N End0-to-sector values, or selected primitive/vertex response "
                "values with b_selected. Conditional Weyl-pair algebra is ready "
                "but still not A_selected."
            ),
        },
        "checks": checks,
        "dynamic_cutset": cutset,
        "lanes": lanes,
        "what_closes_now": sm_packet["what_closes_now"],
        "what_remains_open": remains,
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "The static sector ambiguity is gone; the next artifact must emit "
                "typed retarded derivative data or primitive response values."
            ),
        },
        "guardrails": {
            "dynamic_kernel_emitted": False,
            "selected_C1_primitive_emitted": False,
            "A_selected_claimed": False,
            "b_selected_claimed": False,
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "DynamicOverlapOrC1PrimitiveSourceEmissionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "frontier_update": packet["frontier_update"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Dynamic Overlap or C1 Primitive SourceEmission Import v1

Status: `{cert["status"]}`.

## Result

The C1 frontier is now dynamic rather than static-sector.  Static routing and
finite trace transfer are closed inputs; the remaining legal lanes are:

1. typed dynamic `B_N` retarded derivative or alpha1 source-strength theorem;
2. selected End0-to-sector realization/functor values;
3. selected dynamic overlap/Hessian normalization and `b_selected`;
4. selected primitive/vertex/basis-transport response values.

Conditional Weyl-pair algebra remains exact but unpromoted to `A_selected`.

Next artifact: `{packet["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
