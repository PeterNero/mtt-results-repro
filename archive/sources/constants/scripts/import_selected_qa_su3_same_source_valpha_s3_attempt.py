"""Import the sharper q79 same-source VAlpha/S3 operator packet attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79_REPO / "certificates"

PREVIOUS_IMPORT = CERTS / "selected_qa_su3_same_source_valpha_s3_packet_import_certificate.json"
Q79_ATTEMPT = Q79_CERTS / "selected_qa_su3_same_source_valpha_s3_operator_packet_attempt_certificate.json"
Q79_TEMPLATE = Q79_CERTS / "selected_qa_su3_same_source_valpha_s3_operator_packet.template.json"

OUTPUT_CERT = CERTS / "selected_qa_su3_same_source_valpha_s3_attempt_import_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS_IMPORT)
    attempt = load(Q79_ATTEMPT)
    template = load(Q79_TEMPLATE)

    report = attempt["validator_result"]["parsed_report"]
    subvalidators = report["subvalidators"]
    open_items = attempt["first_open_items"]

    layers = {
        "L0_identity_and_selected_source": [
            "selected_by_mtt must be true",
            "same_source_valpha_s3_operator must be true",
            "packet is marked fixture_only",
            "source_certificate missing",
        ],
        "L1_valpha_ordered_source": [
            "rank2_valpha_model_selected must be true",
            "terminal_monad_difference_L3_minus_K2_selector_closed must be true",
            "nonzero_ext_class_selected must be true",
            "non_split_stability_proved must be true",
            "ordered_source_validator_passes must be true",
            "Pic0 resolution is not selected or quotiented",
            "ordered-source validator did not pass (exit 2)",
        ],
        "L2_s3_gs_same_source": [
            "same_source_link_valpha_to_s3_proved must be true",
            "chern_weil_row_derived_from_same_source must be true",
            "visible_gs_source_validator_passes must be true",
            "coherent_spectral_zero_mode_projectors_closed must be true",
            "visible GS source validator did not pass (exit 1)",
        ],
        "L3_operator_execution": [
            "typed_transition_or_rhoE_data_emitted must be true",
            "hym_strominger_or_routec_residual_pass must be true",
            "sector_D_E_packets_pass must be true",
            "riesz_green_packets_pass must be true",
            "dotD_packets_pass must be true",
            "selected_source_promotion_validator_passes must be true",
            "primitive_C1_or_Yukawa_overlap_contractions must be true",
            "selected-source promotion validator did not pass (exit 1)",
        ],
    }

    output = {
        "certificate": "SelectedQaSU3SameSourceVAlphaS3AttemptImport",
        "status": "QA_SU3_SAME_SOURCE_VALPHA_S3_ATTEMPT_IMPORTED_S3_CONSUMED_SOURCE_OPEN",
        "inputs": {
            "previous_same_source_import": str(PREVIOUS_IMPORT.relative_to(ROOT)),
            "q79_attempt": str(Q79_ATTEMPT),
            "q79_template": str(Q79_TEMPLATE),
        },
        "closed_now": {
            "sharper_valpha_s3_validator_imported": True,
            "closed_s3_support_consumed": attempt["what_this_closes"][
                "closed_s3_support_consumed"
            ],
            "current_best_attempt_executed": attempt["what_this_closes"][
                "current_best_attempt_executed"
            ],
            "open_fields_machine_reported": attempt["what_this_closes"][
                "open_fields_are_machine_reported"
            ],
            "template_schema_matches": template["schema"]
            == "SelectedQaSU3SameSourceVAlphaS3OperatorPacket.v1",
            "previous_generic_fusion_import_passed_forward": previous["closed_now"][
                "q79_same_source_fusion_gate_executable"
            ],
        },
        "validator_result": {
            "exit_code": report["exit_code"],
            "schema": report["schema"],
            "status": report["status"],
            "open_item_count": attempt["open_item_count"],
            "first_open_items": open_items,
            "subvalidator_exit_codes": attempt["subvalidator_exit_codes"],
            "would_close_same_source_valpha_s3_operator_packet": report[
                "would_close_same_source_valpha_s3_operator_packet"
            ],
        },
        "dependency_layers": layers,
        "first_true_gate": {
            "layer": "L0_identity_and_selected_source",
            "reason": (
                "All downstream ordered-source, GS-source, and operator validators "
                "depend on one non-fixture selected source certificate binding "
                "V_alpha/L3-K2, S3/GS support, and D_E/dotD."
            ),
            "minimal_object": "Selected_Source_Certificate_for_VAlpha_S3_DE.v1",
        },
        "not_closed": {
            "same_source_valpha_s3_binding": attempt["what_this_does_not_close"][
                "same_source_valpha_s3_binding"
            ]
            is False,
            "selected_visible_valpha_source": attempt["what_this_does_not_close"][
                "selected_visible_valpha_source"
            ]
            is False,
            "Pic0_selection_or_quotient": attempt["what_this_does_not_close"][
                "Pic0_selection_or_quotient"
            ]
            is False,
            "selected_D_E_dotD_Riesz_Green": attempt["what_this_does_not_close"][
                "selected_D_E_dotD_Riesz_Green"
            ]
            is False,
            "primitive_C1_contractions": attempt["what_this_does_not_close"][
                "primitive_C1_contractions"
            ]
            is False,
            "full_SM_closure": True,
        },
        "hard_next_step": attempt["verdict"]["hard_next_step"],
        "honest_answer": attempt["verdict"]["honest_answer"],
        "guardrails": {
            "claims_same_source_binding": False,
            "claims_selected_visible_valpha_source": False,
            "claims_chern_weil_derivation_from_same_source": False,
            "claims_selected_operator_execution": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
        },
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
