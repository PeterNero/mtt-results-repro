"""Build the cross-repo common D_E/dotD/Riesz/Green payload map."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")

LOCAL_CUTSET = CERTS / "selected_qa_su3_m1_operator_cutset_certificate.json"
SM_PARITY_GS = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "certificates"
    / "selected_visible_green_schwarz_operator_source_certificate.json"
)
SM_PARITY_PIPELINE = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "certificates"
    / "selected_routec_hym_operator_pipeline_certificate.json"
)
QA_PACKET_FINITE = (
    TEXPAPERS
    / "mtt-qa-su3-packet-proof"
    / "certificates"
    / "finite_cochain_packet_or_de_response_gate_certificate.json"
)
QA_PACKET_A01 = (
    TEXPAPERS
    / "mtt-qa-su3-packet-proof"
    / "certificates"
    / "a01_de_operator_exit_gate_certificate.json"
)
Q79_ORIENTATION = (
    TEXPAPERS
    / "mtt-q79-proof-repro"
    / "certificates"
    / "iwasawa_orientation_de_dotd_bridge_certificate.json"
)
Q79_VALIDATORS_REPORT = (
    TEXPAPERS / "mtt-q79-proof-repro" / "reports" / "selected_missing_data_report.json"
)
PROTO_ROOT = TEXPAPERS / "mtt-protospinor-gr-response-proof"

OUTPUT_CERT = CERTS / "common_de_dotd_riesz_green_payload_map_certificate.json"
OUTPUT_TEMPLATE = CERTS / "common_selected_operator_payload.template.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def protospinor_exact_vocab_hits() -> list[str]:
    hits = []
    for path in PROTO_ROOT.rglob("*"):
        if path.suffix.lower() not in {".md", ".py", ".json"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(token in text for token in ("D_E", "dotD", "Riesz", "Chern-Weil")):
            hits.append(str(path))
    return hits


def template() -> dict[str, Any]:
    return {
        "schema": "CommonSelectedOperatorPayload.v1",
        "status": "OPEN_COMMON_SELECTED_OPERATOR_PAYLOAD_REQUIRED",
        "purpose": (
            "One reusable payload for the recurring D_E/dotD/Riesz/Green blocker "
            "across the q79, Qa/SU3, SM-parity, and no-knob repos."
        ),
        "payload_order": [
            "selected_source_certificate",
            "selected_visible_bundle_sheaf_or_routec_source",
            "chern_weil_or_equivalent_operator_row_derivation",
            "coherent_spectral_zero_mode_projectors",
            "sector_D_E_action_matrices",
            "Riesz_projectors_and_gap_bounds",
            "reduced_Green_operators",
            "same_branch_dotD_alpha1_response",
            "primitive_C1_or_target_overlap_contractions",
        ],
        "reuse_rule": (
            "A repo may import this payload only if it cites the same selected "
            "source and branch for all operator layers; validator shapes alone "
            "are reusable, but selected-source flags are not."
        ),
        "forbidden_shortcuts": [
            "Do not import lifted smoke flags as selected source proof.",
            "Do not treat symbolic Green-Schwarz curvature closure as D_E/dotD closure.",
            "Do not use observed flavor, CP, or mass data to select q79 over q369.",
        ],
    }


def main() -> None:
    local = load(LOCAL_CUTSET)
    sm_gs = load(SM_PARITY_GS)
    sm_pipeline = load(SM_PARITY_PIPELINE)
    qa_finite = load(QA_PACKET_FINITE)
    qa_a01 = load(QA_PACKET_A01)
    q79_orientation = load(Q79_ORIENTATION)
    q79_missing = load(Q79_VALIDATORS_REPORT)
    proto_hits = protospinor_exact_vocab_hits()
    tmpl = template()

    output = {
        "certificate": "CommonDEDotDRieszGreenPayloadMap",
        "status": "COMMON_DE_DOTD_RIESZ_GREEN_PAYLOAD_MAPPED_CW_SOURCE_FIRST",
        "inputs": {
            "local_operator_cutset": str(LOCAL_CUTSET.relative_to(ROOT)),
            "sm_parity_visible_gs_operator_source": str(SM_PARITY_GS),
            "sm_parity_routec_hym_pipeline": str(SM_PARITY_PIPELINE),
            "qa_su3_finite_cochain_or_de_response_gate": str(QA_PACKET_FINITE),
            "qa_su3_a01_de_operator_exit_gate": str(QA_PACKET_A01),
            "q79_orientation_de_dotd_bridge": str(Q79_ORIENTATION),
            "q79_selected_missing_data_report": str(Q79_VALIDATORS_REPORT),
            "protospinor_gr_response_repo": str(PROTO_ROOT),
        },
        "common_payload": tmpl["payload_order"],
        "repo_alignment": {
            "mtt_nonsm_constants_no_knob": {
                "status": local["status"],
                "first_gate": local["next_object"]["name"],
                "open_payload": local["cut_set"],
            },
            "mtt_sm_parity_closure": {
                "gs_gate_status": sm_gs["status"],
                "pipeline_status": sm_pipeline["status"],
                "closed_support": {
                    "selected_S3_source_imported_as_closed": sm_gs["what_closes"][
                        "selected_S3_source_imported_as_closed"
                    ],
                    "visible_GS_curvature_imported_as_closed": sm_gs["what_closes"][
                        "visible_GS_curvature_imported_as_closed"
                    ],
                    "validator_sequence_locked": sm_pipeline["what_closes"][
                        "D_E_Riesz_Green_dotD_validator_sequence_locked"
                    ],
                },
                "open_payload": {
                    "selected_visible_bundle_or_sheaf_operator_source": sm_gs[
                        "what_remains_open"
                    ]["selected_visible_bundle_or_sheaf_operator_source"],
                    "selected_D_E_dotD_Riesz_Green": sm_gs["what_remains_open"][
                        "selected_D_E_dotD_Riesz_Green"
                    ],
                    "selected_source_origin_proof": sm_pipeline["what_remains_open"][
                        "selected_source_origin_proof"
                    ],
                },
            },
            "mtt_qa_su3_packet_proof": {
                "finite_gate_status": qa_finite["status"],
                "a01_gate_status": qa_a01["status"],
                "closed_support": {
                    "finite_cochain_acceptance_contract": qa_finite["what_closes"][
                        "finite_cochain_acceptance_contract"
                    ],
                    "operator_response_acceptance_contract": qa_finite[
                        "what_closes"
                    ]["operator_response_acceptance_contract"],
                    "operator_exit_acceptance_interface_built": qa_a01[
                        "what_closes"
                    ]["operator_exit_acceptance_interface_built"],
                },
                "open_payload": {
                    "selected_source_certificate": qa_finite["what_remains_open"][
                        "selected_source_certificate"
                    ],
                    "selected_DE_dotD_response": qa_finite["what_remains_open"][
                        "selected_DE_dotD_response"
                    ],
                    "selected_DE_or_rhoE_operator_matrix": qa_a01[
                        "what_remains_open"
                    ]["selected_DE_or_rhoE_operator_matrix"],
                    "spectral_heat_riesz_or_torsion_exit": qa_a01[
                        "what_remains_open"
                    ]["spectral_heat_riesz_or_torsion_exit"],
                },
            },
            "mtt_q79_proof_repro": {
                "orientation_status": q79_orientation["status"],
                "closed_support": {
                    "orientation_dependencies_compared": q79_orientation[
                        "what_this_closes"
                    ]["orientation_dependencies_compared"],
                    "m_label_to_q_label_conditional_map_formulated": q79_orientation[
                        "what_this_closes"
                    ]["m_label_to_q_label_conditional_map_formulated"],
                    "sector_orientation_packets_formulated": q79_orientation[
                        "what_this_closes"
                    ]["sector_orientation_packets_formulated"],
                },
                "open_payload": {
                    "selected_D_E_constructed": q79_missing[
                        "selected_D_E_constructed"
                    ],
                    "selected_D_E_routes": q79_missing["selected_D_E_routes"],
                    "selected_orientation_carrying_D_E": q79_orientation[
                        "still_open"
                    ]["selected_orientation_carrying_D_E"],
                    "selected_dotD_same_branch_derivative": q79_orientation[
                        "still_open"
                    ]["selected_dotD_same_branch_derivative"],
                },
            },
            "mtt_protospinor_gr_response_proof": {
                "exact_DE_dotD_vocab_hits": proto_hits,
                "has_related_operator_vocab_hits": len(proto_hits) > 0,
                "shares_sm_typed_payload": False,
                "interpretation": (
                    "Adjacent operator-gap repo, but not evidence for the same "
                    "SM D_E/dotD/Riesz/Green payload unless exact typed bridge "
                    "artifacts are later added."
                ),
            },
        },
        "path_decision": {
            "construct_Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1_is_correct": True,
            "why": [
                "It is the first object in this repo that can derive the visible Tr_F row from a selected source.",
                "It can feed the same-source D_E/Riesz/Green/dotD validators used by q79 and SM parity.",
                "It avoids reopening closed S3/Freed-Witten/Green-Schwarz curvature work.",
                "It gives the Qa/SU3 packet repo the missing selected operator payload rather than another interface.",
            ],
            "not_the_next_move": [
                "Do not build another symbolic Bianchi or curvature-row closure.",
                "Do not select q79 over q369 from observed CP.",
                "Do not import smoke validator data as selected matrices.",
            ],
        },
        "memory_checkpoint": {
            "current_branch_frontier": local["next_object"]["name"],
            "next_artifact_to_build": "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1",
            "repository": str(ROOT),
            "latest_committed_baseline": "274d6eb Import Qa SU3 m1 operator cutset",
        },
        "guardrails": {
            "claims_common_payload_constructed": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_or_nonSM_closure": False,
            "uses_observed_flavor_data": False,
        },
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(
            json.dumps(tmpl, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(cert_text)


if __name__ == "__main__":
    main()
