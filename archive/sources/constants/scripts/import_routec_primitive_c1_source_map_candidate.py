"""Import Route-C primitive C1 tensor / Hessian source-map candidate."""

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

PREVIOUS = CERTS / "routec_sector_projectors_dotd_on_smooth_bn_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution_certificate.json"
UPSTREAM_DIR = SM / "candidate_data" / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
UPSTREAM_SOURCE_MAP = UPSTREAM_DIR / "primitive_tensor_hessian_source_map_candidate.packet.json"
UPSTREAM_SELECTION_KERNEL = UPSTREAM_DIR / "source_map_selection_obligation_kernel.packet.json"
UPSTREAM_GALERKIN_PACKET = UPSTREAM_DIR / "honest_galerkin_execution_value_slots.packet.json"

OUTPUT_PACKET = DATA / "routec_primitive_c1_source_map_candidate_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_primitive_c1_source_map_candidate_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_PrimitiveC1_SourceMapCandidate_Import_v1.md"

STATUS = "ROUTEC_PRIMITIVE_C1_SOURCE_MAP_CANDIDATE_IMPORTED_SELECTION_OPEN"
PREVIOUS_STATUS = "ROUTEC_SECTOR_PROJECTORS_DOTD_ON_SMOOTH_BN_IMPORTED_C1_SOURCE_OPEN"
UPSTREAM_STATUS = (
    "MTT_SELECTED_PRIMITIVEC1TENSOR_HESSIANSOURCEMAP_OR_HONESTGALERKINC1EXECUTION_"
    "BUILT_SOURCE_MAP_CANDIDATE_VALUES_OPEN"
)
NEXT = "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    source_map = load(UPSTREAM_SOURCE_MAP)
    kernel = load(UPSTREAM_SELECTION_KERNEL)
    galerkin = load(UPSTREAM_GALERKIN_PACKET)

    support = source_map["closed_support"]
    residuals = source_map["candidate_residual_operators"]
    replay = source_map["residual_completion_replay"]
    if_selected = source_map["if_source_map_selected_then"]
    emitted = kernel["currently_emitted"]
    current = kernel["minimal_truth_table"]["current_case"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_RouteC_C1_Primitive_Response_or_Selected_Source_Proof_v1",
        "F1_upstream_packet_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["theorem_proved"] is True
        and upstream_cert["candidate_path"].endswith(
            "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json"
        ),
        "F3_support_attached_on_72_real_target": source_map["status"]
        == "SOURCE_MAP_CANDIDATE_CONSTRUCTED_SELECTION_OPEN"
        and support["strict_72_real_acceptance_target"]["total_real_coordinates"] == 72
        and support["selected_source_selector_attached"] is True
        and support["same_branch_source_required"] is True
        and support["canonical_Q_residual_available"] is True
        and support["Q_residual_rank"] == 6
        and support["projector_idempotence_verified"] is True,
        "F4_alpha_dotd_prefix_and_trace_norm_attached": support["alpha1_dotD_driver_verified"] is True
        and support["static_trace_transfer_normalization_selected"] is True,
        "F5_residual_shapes_exact_but_unselected": residuals["phase_R_Z"]["selected_by_MTT_now"]
        is False
        and residuals["shift_R_X"]["selected_by_MTT_now"] is False
        and residuals["phase_R_Z"]["shape"]["residual_norm_sq"] == 4.0
        and residuals["shift_R_X"]["shape"]["residual_norm_sq"] == 2.0,
        "F6_conditional_completion_algebra_exact": replay[
            "phase_projection_plus_residual_equals_target"
        ]
        is True
        and replay["shift_projection_plus_residual_equals_target"] is True
        and replay["routed_72_real_completion"]["conditional_b_norm_sq"] == 24.0
        and if_selected["rank"] == 2
        and if_selected["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
        and if_selected["A_transpose_b"] == [12.0, 12.0]
        and if_selected["deltaTheta_C1"] == [1.0, 1.0],
        "F7_selection_kernel_keeps_values_open": kernel["status"]
        == "SELECTION_OBLIGATION_KERNEL_BUILT_VALUES_OPEN"
        and all(
            emitted[key] is False
            for key in [
                "selected_A_selected",
                "selected_b_selected",
                "selected_basis_transport_vertex_or_Hessian_values",
                "selected_deltaTheta_C1",
                "selected_differentiated_residual_projector_source_rule",
            ]
        )
        and current["phase_R_Z_selected"] is False
        and current["shift_R_X_selected"] is False
        and current["b_source_emitted"] is False
        and current["A_selected_promotes"] is False,
        "F8_galerkin_slots_restate_open_value_run": galerkin["status"]
        == "HONEST_GALERKIN_EXECUTION_SLOTS_RESTATED_VALUES_OPEN"
        and galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72
        and galerkin["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING"
        and galerkin["selected_source_verified"] is False
        and galerkin["can_replace_source_map_now"] is False,
        "F9_no_value_promotion_or_target_fit": upstream["source_map_selected_claimed"] is False
        and upstream["A_selected_claimed"] is False
        and upstream["b_selected_claimed"] is False
        and upstream["deltaTheta_C1_claimed"] is False
        and upstream["sector_response_matrices_claimed"] is False
        and upstream["honest_Galerkin_C1_claimed"] is False
        and upstream["observed_data_used"] is False
        and upstream["target_fitting_used"] is False,
    }

    summary = {
        "strict_real_coordinates": 72,
        "Q_residual_rank": support["Q_residual_rank"],
        "phase_residual_norm_sq": residuals["phase_R_Z"]["shape"]["residual_norm_sq"],
        "shift_residual_norm_sq": residuals["shift_R_X"]["shape"]["residual_norm_sq"],
        "conditional_b_norm_sq": replay["routed_72_real_completion"]["conditional_b_norm_sq"],
        "if_selected_rank": if_selected["rank"],
        "if_selected_A_transpose_A": if_selected["A_transpose_A"],
        "if_selected_A_transpose_b": if_selected["A_transpose_b"],
        "if_selected_deltaTheta_C1": if_selected["deltaTheta_C1"],
        "source_map_selected_by_MTT_now": source_map["selected_by_MTT_now"],
        "selected_A_selected_emitted": emitted["selected_A_selected"],
        "selected_b_selected_emitted": emitted["selected_b_selected"],
        "honest_galerkin_selected_source_verified": galerkin["selected_source_verified"],
    }

    return {
        "packet": "RouteC_PrimitiveC1_SourceMapCandidate_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_source_map": str(UPSTREAM_SOURCE_MAP),
            "upstream_selection_kernel": str(UPSTREAM_SELECTION_KERNEL),
            "upstream_galerkin_packet": str(UPSTREAM_GALERKIN_PACKET),
        },
        "theorem": {
            "name": "RouteCPrimitiveC1SourceMapCandidateImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The primitive C1 frontier is sharpened to a concrete "
                "same-branch source-map candidate: phase Z/clock maps to R_Z, "
                "shift X maps to R_X, and both share canonical Q_residual rank "
                "6 support in the 72-real coordinate target.  The if-selected "
                "algebra gives A^T A=12 I, A^T b=(12,12), and "
                "deltaTheta_C1=(1,1), but R_Z, R_X, b_selected, A_selected, "
                "sector response matrices, and honest Galerkin C1 values are "
                "not promoted."
            ),
        },
        "checks": checks,
        "primitive_c1_source_map_summary": summary,
        "upstream_primitive_c1_source_map_candidate": upstream,
        "upstream_packets": {
            "source_map": source_map,
            "selection_kernel": kernel,
            "honest_galerkin_slots": galerkin,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_source_map_selected": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_deltaTheta_C1": False,
            "claims_sector_response_matrices": False,
            "claims_honest_Galerkin_C1": False,
            "claims_SM_parity_dynamic_packet_closure": False,
            "claims_full_no_knob_flavor_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCPrimitiveC1SourceMapCandidateImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "primitive_c1_source_map_summary": packet["primitive_c1_source_map_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["primitive_c1_source_map_summary"]
    return f"""# RouteC Primitive C1 Source Map Candidate Import v1

Status: `{cert["status"]}`.

The primitive C1 frontier is now explicit.  The imported candidate maps the
phase leg to `R_Z`, the shift leg to `R_X`, and uses canonical `Q_residual`
support of rank `{s["Q_residual_rank"]}` in the `{s["strict_real_coordinates"]}`-real
coordinate target.

The conditional algebra is exact:

```text
||R_Z||^2 = {s["phase_residual_norm_sq"]}
||R_X||^2 = {s["shift_residual_norm_sq"]}
A^T A = {s["if_selected_A_transpose_A"]}
A^T b = {s["if_selected_A_transpose_b"]}
deltaTheta_C1 = {s["if_selected_deltaTheta_C1"]}
```

This is still a candidate, not selected-source closure.  `R_Z`, `R_X`,
`b_selected`, `A_selected`, sector response matrices, and honest Galerkin C1
values remain unpromoted.

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
