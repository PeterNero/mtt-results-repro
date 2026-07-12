"""Import primitive-C1 contraction envelope / dynamic-overlap tensor boundary."""

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

PREVIOUS = CERTS / "primitivec1_or_weylpair_sectorrouting_sourceemission_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission.candidate.json"
SM_CERT = SM / "certificates" / "selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission_certificate.json"

OUTPUT_PACKET = DATA / "primitivec1_contractions_or_dynamicoverlaptensor_sourceemission_import.candidate.json"
OUTPUT_CERT = CERTS / "primitivec1_contractions_or_dynamicoverlaptensor_sourceemission_import_certificate.json"
OUTPUT_NOTE = CORPUS / "PrimitiveC1_Contractions_or_DynamicOverlapTensor_SourceEmission_Import_v1.md"

STATUS = "PRIMITIVEC1_CONTRACTION_ENVELOPE_IMPORTED_DYNAMIC_VALUES_OPEN"
PREVIOUS_STATUS = "PRIMITIVEC1_OR_WEYLPAIR_ROUTING_IMPORTED_STATIC_ROUTE_CLOSED_DYNAMIC_CONTRACTIONS_OPEN"
SM_STATUS = (
    "MTT_SELECTED_PRIMITIVEC1_CONTRACTIONS_OR_DYNAMICOVERLAPTENSOR_SOURCEEMISSION_"
    "ENVELOPE_BUILT_DYNAMIC_VALUES_OPEN"
)
NEXT = "Selected_U1Y_RouteC_DynamicOverlapTensor_HessianNormalization_or_GalerkinC1Contractions_ValueEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    closed = sm_packet["closed_inputs"]
    envelope = sm_packet["contraction_envelope"]
    summary = envelope["candidate_summary"]
    manifests = sm_packet["honest_vs_formal_primitive_manifest"]
    promotion = sm_packet["promotion_test"]
    live = sm_packet["live_blockers"]

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_theorem_proved": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and sm_packet["theorem"]["proved"] is True,
        "G2_closed_inputs_imported": all(
            closed[key] is True
            for key in [
                "alpha1_driver_verified",
                "selected_dotD_source_verified",
                "honest_dotD_alpha1_replay",
                "static_weyl_sector_routing",
                "static_singlet_neutrino_shift_rule",
                "static_trace_transfer_normalization",
                "primitive_class_C1_observable_layer",
                "current_layer_not_flavor_closure",
            ]
        ),
        "G3_contraction_envelope_constructed": envelope["constructed"] is True
        and envelope["active_shift"] == [1, 1]
        and envelope["fixed_fiber_class"] == [0, 1, 2]
        and envelope["phase_route"] == ["u", "e"]
        and envelope["shift_route"] == ["d", "nuD"]
        and summary["fixed_fiber_candidates"] == [0, 1, 2]
        and summary["all_fixed_fiber_rank_three"] is True
        and summary["all_fixed_fiber_rank_values"] == [3],
        "G4_envelope_not_promoted_as_dynamic_tensor": envelope["selected_as_dynamic_tensor"]
        is False
        and sm_packet["dynamic_overlap_tensor_claimed"] is False
        and sm_packet["primitive_C1_contractions_claimed"] is False,
        "G5_honest_and_formal_manifests_still_open": manifests["honest_status"]
        == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING"
        and manifests["honest_selected_source_verified"] is False
        and manifests["formal_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING"
        and manifests["formal_selected_source_verified"] is False
        and manifests["formal_lift_promoted"] is False,
        "G6_promotion_test_blocks_A_b_rank": promotion["all_required_fields_emitted"] is False
        and promotion["A_selected_promotion_allowed"] is False
        and promotion["b_selected_promotion_allowed"] is False
        and promotion["rank_or_consistency_test_allowed"] is False
        and all(value is False for value in promotion["required_fields"].values()),
        "G7_live_dynamic_blockers_remain": live["selected_dynamic_overlap_tensor_or_transfer_functor"]
        is True
        and live["selected_primitive_C1_contractions"] is True
        and live["selected_b_selected_or_Hessian_normalization"] is True
        and live["selected_A_selected_response_operator"] is True
        and live["selected_sector_response_matrices"] is True
        and live["selected_deltaTheta_C1_solution"] is True,
        "G8_no_target_or_closure_overclaim": sm_packet["closure_claimed"] is False
        and sm_packet["A_selected_claimed"] is False
        and sm_packet["b_selected_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False,
    }

    return {
        "packet": "PrimitiveC1_Contractions_or_DynamicOverlapTensor_SourceEmission_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_contraction_envelope_packet": str(SM_PACKET),
            "sm_contraction_envelope_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "PrimitiveC1ContractionEnvelopeImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "Given selected alpha1/dotD replay, static Weyl routing, the "
                "1_M shift rule, finite trace normalization, and the selected "
                "primitive C1 observable class, the finite primitive candidates "
                "form a routed contraction envelope over active shift (1,1) and "
                "fiber class {0,1,2}. This is not a selected dynamic overlap "
                "tensor and not selected primitive C1 contractions: the honest "
                "and formal Galerkin manifests still record missing contraction "
                "values, so A_selected, b_selected, and rank tests remain blocked."
            ),
        },
        "checks": checks,
        "closed_inputs": closed,
        "contraction_envelope": envelope,
        "honest_vs_formal_primitive_manifest": manifests,
        "promotion_test": promotion,
        "retired_blockers": sm_packet["retired_blockers"],
        "live_blockers": live,
        "what_closes_now": sm_packet["what_closes_now"],
        "what_remains_open": sm_packet["what_remains_open"],
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "The static route plus primitive candidates now gives a finite "
                "envelope. The next gate must produce selected non-scalar dynamic "
                "overlap/Hessian data or honest Galerkin primitive contractions."
            ),
        },
        "guardrails": {
            "contraction_envelope_constructed": True,
            "selected_dynamic_overlap_tensor_claimed": False,
            "selected_primitive_C1_contractions_claimed": False,
            "A_selected_claimed": False,
            "b_selected_claimed": False,
            "rank_tests_allowed_now": False,
            "observed_data_used": False,
            "target_fitting_used": False,
            "full_SM_closure_claimed": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "PrimitiveC1ContractionsOrDynamicOverlapTensorSourceEmissionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "frontier_update": packet["frontier_update"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    env = packet["contraction_envelope"]
    return f"""# PrimitiveC1 Contractions or DynamicOverlapTensor SourceEmission Import v1

Status: `{cert["status"]}`.

## Result

The selected static route plus finite primitive candidates now produces a routed
contraction envelope:

```text
active shift = {env["active_shift"]}
fixed fiber class = {env["fixed_fiber_class"]}
phase route = {env["phase_route"]}
shift route = {env["shift_route"]}
all fixed-fiber candidates rank three = {env["candidate_summary"]["all_fixed_fiber_rank_three"]}
max absolute entry = {env["candidate_summary"]["all_fixed_fiber_max_abs_values"][0]}
```

## Boundary

The envelope is not a selected dynamic tensor and not selected primitive C1
contractions. The honest and formal Galerkin manifests still record missing
primitive contractions, so `A_selected`, `b_selected`, `deltaTheta_C1`, sector
response matrices, and flavor closure remain open.

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
