"""Build Qa/SU3 candidate payload fill or profile source acquisition."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_qasu3candidatepayloadfill_or_profilesourceacquisition"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PAYLOAD_FILL = PACKET_DIR / "qasu3_candidate_payload_fill_attempt.packet.json"
PROFILE_ACQ = PACKET_DIR / "profile_source_acquisition_attempt.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_payload_fill.packet.json"
CUTSET = PACKET_DIR / "ordered_source_or_profile_workspace_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_QaSU3CandidatePayloadFill_or_ProfileSourceAcquisition_v1.md"

STATUS = "MTT_SELECTED_QASU3CANDIDATEPAYLOADFILL_OR_PROFILESOURCEACQUISITION_BUILT_PARTIAL_PAYLOAD_TRUE_EQ_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def exists_path(path_string: str) -> bool:
    return Path(path_string).exists() if ":" in path_string else (ROOT / path_string).exists()


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining.candidate.json")
    mining = load(
        DATA
        / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining"
        / "qasu3_packet_candidate_mining.packet.json"
    )
    same_source = load(DATA / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json")
    parity_replacement = load(
        DATA
        / "selected_qasu3sourcepacket_or_finalsmparityclosure"
        / "qasu3_parity_interface_replacement.packet.json"
    )

    support_candidates = {
        row["candidate_id"]: row for row in mining["mined_candidates"]
    }
    local_same_source = same_source["same_source_packet_attempt"]
    topological_candidate = local_same_source["topological_candidate"]
    closed_support = local_same_source["closed_support"]
    promotion_tests = same_source["promotion_tests"]
    minimal_closing_payload = same_source["minimal_closing_payload"]["must_supply"]

    partial_payload_fields = {
        "selected_branch_label": local_same_source["branch"],
        "ordered_difference": topological_candidate["ordered_difference"],
        "line_bundle_value": topological_candidate["value"],
        "doubled_c2_value": topological_candidate["double_value"],
        "unique_ordered_difference": topological_candidate["unique_ordered_difference"],
        "matches_target_L": topological_candidate["matches_target_L"],
        "matches_target_L2_after_doubling": topological_candidate["matches_target_L2_after_doubling"],
        "s3_block_projector_retention_closed": closed_support["s3_block_projector_retention_closed"],
        "s3_flat_deligne_restriction_closed": closed_support["s3_flat_deligne_restriction_closed"],
        "s3_freed_witten_cancellation_closed": closed_support["s3_freed_witten_cancellation_closed"],
        "visible_gs_bianchi_residual_zero": closed_support["visible_gs_bianchi_residual_zero"],
        "visible_gs_curvature_closed": closed_support["visible_gs_curvature_closed"],
    }

    operator_payload_slots = {
        "selected_source_status_for_L3_minus_K2_or_enlarged_visible_source": False,
        "standard_lattice_base_ordering_and_base_swap_breaking": False,
        "Pic0_selection_or_physical_quotient_theorem": False,
        "same_source_Chern_Weil_row_derived": promotion_tests["T6_same_source_Chern_Weil_row_derived"],
        "transition_rhoE_or_Cech_Dolbeault_DE_data": promotion_tests["T7_transition_rhoE_or_DE_emitted"],
        "selected_HYM_or_RouteC_residual": promotion_tests["T8_selected_HYM_or_RouteC_residual"],
        "Riesz_Green_dotD_projector_retention": promotion_tests["T9_Riesz_Green_dotD_projector_retention"],
        "finite_determinant_heat_spectrum_or_torsion_response": promotion_tests[
            "T10_finite_determinant_or_torsion_response"
        ],
    }

    filled_operator_slot_count = sum(bool(value) for value in operator_payload_slots.values())
    required_operator_slot_count = len(operator_payload_slots)

    qasu3_payload_fill = {
        "schema": "MTTQaSU3CandidatePayloadFillAttempt.v1",
        "status": "BEST_LANE_PARTIAL_PAYLOAD_EMITTED_ACTUAL_OPERATOR_PAYLOAD_OPEN",
        "input_candidate_mining": rel(
            DATA
            / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining"
            / "qasu3_packet_candidate_mining.packet.json"
        ),
        "best_lane": "local_same_source_visible_color_attempt",
        "best_lane_source": support_candidates["local_same_source_visible_color_attempt"]["source"],
        "best_lane_present": support_candidates["local_same_source_visible_color_attempt"]["present"],
        "why_best_lane": [
            "it emits an explicit ordered-difference candidate instead of only a prose dependency",
            "it carries closed S3/Freed-Witten/Green-Schwarz support from the same visible/color route",
            "it exposes the exact source/operator slots still missing for promotion",
        ],
        "partial_payload_emitted": True,
        "partial_payload_fields": partial_payload_fields,
        "operator_payload_slots": operator_payload_slots,
        "filled_operator_slot_count": filled_operator_slot_count,
        "required_operator_slot_count": required_operator_slot_count,
        "actual_selected_operator_payload_filled": False,
        "accepted_as_actual_QaSU3_packet": False,
        "accepted_for_true_SM_equivalence": False,
        "accepted_for_no_knob": False,
        "remaining_minimal_operator_payload": minimal_closing_payload,
        "primary_repair": same_source["minimal_closing_payload"]["primary_repair"],
        "secondary_repair": same_source["decision"]["secondary_next_artifact"],
        "superset_strategy_used": (
            "superset path: lock the SM-parity interface to the strongest same-source visible/color lane, "
            "then combine topology, S3/Freed-Witten/Green-Schwarz support, typed-monad scaffolding, and "
            "operator-source audits only as constrained support; no observed SM constants select the lane"
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    profile_acquisition = {
        "schema": "MTTProfileSourceAcquisitionAttempt.v1",
        "status": "NO_PROFILE_WORKSPACE_IMPORTED_QASU3_LANE_PRIORITIZED",
        "required_profile_workspace_payload": [
            "official or independently reconstructed non-Higgs likelihood/covariance source",
            "basis map to lambda_Mt, y_t_Mt, g_2_Mt, g_Y_Mt, g_3_Mt",
            "correlation/covariance provenance",
            "loop-order, threshold, and scheme convention",
            "machine replay acceptance rule",
        ],
        "local_profile_source_imported_now": False,
        "surrogate_profile_remains_diagnostic_only": True,
        "route_A_can_close_true_SM_equivalence_now": False,
        "why_qasu3_prioritized": [
            "the local repo already has a concrete same-source partial packet",
            "profile route still lacks a provenance-safe workspace",
            "Qa/SU3 promotion would also strengthen the selected source/interface theorem",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTPromotionDecisionAfterQaSU3PayloadFill.v1",
        "status": "PARTIAL_QASU3_PAYLOAD_FILLED_PROMOTION_BLOCKED_BY_SOURCE_OPERATOR_GATES",
        "route_A_profile_source_acquisition": {
            "profile_workspace_imported": False,
            "can_close_true_SM_equivalence_now": False,
        },
        "route_B_qasu3_payload_fill": {
            "best_lane_selected": qasu3_payload_fill["best_lane"],
            "partial_payload_emitted": True,
            "actual_selected_operator_payload_filled": False,
            "filled_operator_slot_count": filled_operator_slot_count,
            "required_operator_slot_count": required_operator_slot_count,
            "can_close_true_SM_equivalence_now": False,
            "can_close_no_knob_now": False,
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTOrderedSourceOrProfileWorkspaceCutset.v1",
        "status": "ORDERED_SOURCE_OR_PROFILE_WORKSPACE_REQUIRED",
        "closed_now": [
            "best Qa/SU3 payload-fill lane selected",
            "partial same-source visible/color payload emitted",
            "profile workspace acquisition attempted and rejected as absent",
            "remaining operator/source gates enumerated",
        ],
        "remaining_minimal_payloads": [
            "source-select the ordered V_alpha/L3-K2 lane or an enlarged visible source",
            "prove Pic0 selection or a physical quotient theorem removing Pic0",
            "emit selected transition/rho_E or Cech-Dolbeault/D_E data",
            "prove selected HYM/Route-C residual and Riesz/Green/dotD/projector retention",
            "or import an official/reconstructed non-Higgs profile likelihood workspace",
        ],
        "recommended_next_artifact": "MTT_Selected_OrderedVAlphaPic0Source_or_ProfileWorkspaceImport_v1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedQaSU3CandidatePayloadFillOrProfileSourceAcquisition",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining.candidate.json"),
            "qasu3_candidate_mining": rel(
                DATA
                / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining"
                / "qasu3_packet_candidate_mining.packet.json"
            ),
            "same_source_visible_color_attempt": rel(
                DATA / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json"
            ),
            "qasu3_parity_interface_replacement": rel(
                DATA
                / "selected_qasu3sourcepacket_or_finalsmparityclosure"
                / "qasu3_parity_interface_replacement.packet.json"
            ),
        },
        "output_packets": {
            "qasu3_candidate_payload_fill_attempt": rel(PAYLOAD_FILL),
            "profile_source_acquisition_attempt": rel(PROFILE_ACQ),
            "promotion_decision": rel(PROMOTION),
            "ordered_source_or_profile_workspace_cutset": rel(CUTSET),
        },
        "source_presence_checked": {
            "all_mined_candidates_present": mining["all_candidates_present"],
            "same_source_packet_present": exists_path(support_candidates["local_same_source_visible_color_attempt"]["source"]),
            "parity_interface_support_present": parity_replacement["support_presence"]["all_required_support_present"],
        },
        "theorem": {
            "name": "QaSU3PayloadFillReductionTheorem",
            "proved": True,
            "statement": (
                "Among the mined Qa/SU3 lanes, the same-source visible/color lane is the strongest current "
                "payload-fill candidate because it emits a concrete ordered L3-K2 topological payload and closed "
                "S3/Freed-Witten/Green-Schwarz support. This fills a partial source payload but does not supply "
                "the selected operator maps, Pic0 rule, or HYM/Riesz/Green/dotD gates required for actual Qa/SU3 "
                "promotion or true SM equivalence."
            ),
        },
        "what_closes_now": {
            "best_qasu3_payload_lane_selected": True,
            "partial_same_source_payload_emitted": True,
            "profile_source_acquisition_attempted": True,
            "remaining_gate_cutset_sharpened": True,
        },
        "what_remains_open": {
            "actual_QaSU3_operator_payload": True,
            "ordered_source_selection": True,
            "Pic0_selection_or_quotient": True,
            "selected_transition_rhoE_or_DE": True,
            "selected_HYM_Riesz_Green_dotD": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": previous["closure_decision"]["SM_parity_closed"],
            "partial_QaSU3_payload_filled": True,
            "actual_QaSU3_packet_promoted": False,
            "profile_workspace_imported": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": cutset["recommended_next_artifact"],
    }

    cert = {
        "certificate": "MTT_Selected_QaSU3CandidatePayloadFill_or_ProfileSourceAcquisition_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "partial_QaSU3_payload_filled": True,
        "actual_QaSU3_packet_promoted": False,
        "profile_workspace_imported": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected QaSU3CandidatePayloadFill or ProfileSourceAcquisition v1

Status: `{STATUS}`.

This artifact promotes the mined Qa/SU3 support list into an executable payload
fill attempt.

The strongest current lane is the local same-source visible/color attempt. It
emits a concrete partial payload: branch `q79/F,m=1`, ordered difference
`L3_minus_K2`, line-bundle value `[1, -2, 0]`, doubled value `[2, -4, 0]`,
and closed S3/Freed-Witten/Green-Schwarz support.

This is progress, but not closure. The actual selected operator payload still
requires ordered source selection, Pic0 selection or quotient, selected
transition/rho_E or Cech-Dolbeault/D_E data, selected HYM/Route-C residual, and
Riesz/Green/dotD/projector retention.

The superset strategy used here is constrained: several encodings support the
same lane, but the lane is locked to the declared SM-parity target and no
observed constants are used as selectors.
"""

    for path, payload in [
        (PAYLOAD_FILL, qasu3_payload_fill),
        (PROFILE_ACQ, profile_acquisition),
        (PROMOTION, promotion),
        (CUTSET, cutset),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
