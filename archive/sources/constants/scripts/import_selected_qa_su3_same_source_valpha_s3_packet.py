"""Import the q79 same-source V_alpha/S3 operator packet frontier."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79_REPO / "certificates"

LOCAL_ARCH = CERTS / "selected_qa_su3_visible_source_architecture_certificate.json"
Q79_IMPORT = Q79_CERTS / "selected_qa_su3_visible_source_architecture_import_certificate.json"
Q79_FUSION_GATE = Q79_CERTS / "same_source_monad_gs_operator_fusion_gate_certificate.json"
Q79_FUSION_ATTEMPT = Q79_CERTS / "same_source_monad_gs_operator_fusion_attempt_certificate.json"
Q79_TEMPLATE = Q79_CERTS / "selected_qa_su3_same_source_valpha_s3_operator_packet.template.json"

OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_same_source_valpha_s3_operator_packet.template.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_same_source_valpha_s3_packet_import_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    local_arch = load(LOCAL_ARCH)
    q79_import = load(Q79_IMPORT)
    fusion_gate = load(Q79_FUSION_GATE)
    fusion_attempt = load(Q79_FUSION_ATTEMPT)
    template = load(Q79_TEMPLATE)

    validator = fusion_attempt["validator_result"]["parsed_report"]
    subvalidators = validator["subvalidators"]
    open_items = fusion_attempt["first_open_items"]

    output = {
        "certificate": "SelectedQaSU3SameSourceVAlphaS3PacketImport",
        "status": "QA_SU3_SAME_SOURCE_VALPHA_S3_PACKET_IMPORTED_OPEN_ITEMS_CERTIFIED",
        "inputs": {
            "local_visible_source_architecture": str(LOCAL_ARCH.relative_to(ROOT)),
            "q79_architecture_import": str(Q79_IMPORT),
            "q79_fusion_gate": str(Q79_FUSION_GATE),
            "q79_fusion_attempt": str(Q79_FUSION_ATTEMPT),
            "q79_same_source_template": str(Q79_TEMPLATE),
        },
        "template_written": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "closed_now": {
            "q79_same_source_fusion_gate_executable": q79_import["closed_now"][
                "q79_fusion_validator_already_executable"
            ],
            "local_architecture_ranked": local_arch["closed_now"]["ranked_architectures_built"],
            "same_source_template_imported": template["schema"]
            == "SelectedQaSU3SameSourceVAlphaS3OperatorPacket.v1",
            "current_best_patchwork_attempt_refused": fusion_attempt["what_this_closes"][
                "current_best_patchwork_attempt_executed"
            ],
            "open_items_machine_reported": fusion_attempt["what_this_closes"][
                "open_fields_are_machine_reported"
            ],
            "invalid_patchwork_proof_blocked": fusion_gate["what_this_closes"][
                "invalid_patchwork_proof_blocked"
            ],
        },
        "validator_result": {
            "exit_code": validator["exit_code"],
            "schema": validator["schema"],
            "status": validator["status"],
            "open_item_count": fusion_attempt["open_item_count"],
            "first_open_items": open_items,
            "ordered_source_exit_code": subvalidators["ordered_source"]["exit_code"],
            "selected_source_promotion_exit_code": subvalidators[
                "selected_source_promotion"
            ]["exit_code"],
            "would_close_selected_monad_difference_source": validator[
                "would_close_selected_monad_difference_source"
            ],
        },
        "not_closed": {
            "same_source_valpha_s3_binding": q79_import["not_closed"][
                "same_source_valpha_s3_binding"
            ],
            "same_source_fusion_packet": q79_import["not_closed"][
                "same_source_fusion_packet"
            ],
            "selected_L3_minus_K2_source": q79_import["not_closed"][
                "selected_L3_minus_K2_source"
            ],
            "Pic0_selection_or_quotient": q79_import["not_closed"][
                "Pic0_selection_or_quotient"
            ],
            "typed_transition_or_rhoE_data": q79_import["not_closed"][
                "typed_transition_or_rhoE_data"
            ],
            "selected_D_E_dotD_Riesz_Green": q79_import["not_closed"][
                "selected_D_E_dotD_Riesz_Green"
            ],
            "primitive_C1_or_Yukawa_contractions": q79_import["not_closed"][
                "primitive_C1_or_Yukawa_contractions"
            ],
            "full_SM_closure": True,
        },
        "mapping_to_q79_fusion_packet": q79_import["mapping_to_q79_fusion_packet"],
        "hard_next_step": q79_import["verdict"]["hard_next_step"],
        "next_action": fusion_gate["verdict"]["next_action"],
        "guardrails": {
            "claims_same_source_binding_proved": False,
            "claims_selected_D_E_constructed": False,
            "claims_pic0_resolved": False,
            "claims_selected_visible_bundle_constructed": False,
            "claims_full_SM_closure": False,
            "uses_lifted_flags_as_proof": False,
            "uses_observed_masses_or_mixings": False,
        },
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    template_text = json.dumps(template, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(template_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
