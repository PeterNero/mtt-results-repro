"""Import the q79 VAlpha/S3 mod-3 cocycle compatibility gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79_REPO / "certificates"

PREVIOUS_GATE = CERTS / "selected_qa_su3_same_source_valpha_s3_attempt_import_certificate.json"
Q79_COMPAT = Q79_CERTS / "valpha_s3_mod3_cocycle_compatibility_certificate.json"

OUTPUT_CERT = CERTS / "selected_qa_su3_valpha_s3_mod3_compatibility_import_certificate.json"
OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_valpha_s3_integral_lift_or_physical_quotient.template.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def integral_lift_template() -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3VAlphaS3IntegralLiftOrPhysicalQuotient.v1",
        "status": "OPEN_SELECTED_QA_SU3_VALPHA_S3_INTEGRAL_LIFT_OR_PHYSICAL_QUOTIENT_REQUIRED",
        "purpose": (
            "Upgrade the imported finite F_3^2 VAlpha/S3 cocycle compatibility "
            "into a non-fixture selected integral source certificate, or prove "
            "that the physical quotient selected by MTT only needs the finite "
            "quotient and carries the remaining smooth operator data."
        ),
        "must_supply": {
            "typed_cech_or_appell_humbert_transition_data": None,
            "integral_lift_from_F3_squared_to_L3_minus_K2": None,
            "same_source_or_physical_quotient_map": None,
            "base_factor_order_selection": None,
            "pic0_selection_or_quotient": None,
            "visible_gs_row_derivation_from_lifted_source": None,
            "selected_D_E_dotD_Riesz_Green_packets": None,
            "primitive_C1_or_Yukawa_overlap_contractions": None,
        },
        "acceptance_tests": [
            "The V_alpha source is selected without fixture flags.",
            "The S3 finite support and V_alpha source are bound by one typed source object.",
            "The ordered L3-K2 lane and base-factor order are selected or quotiented.",
            "Pic0 freedom is either selected, quotiented, or proved physically invisible.",
            "The same object emits D_E, dotD, Riesz/Green, and GS source data.",
            "No observed masses, mixings, or benchmark flavor entries are used as inputs.",
        ],
        "forbidden_shortcuts": [
            "Do not treat GL(2,F3) equivalence as integral equality.",
            "Do not use the finite F_3^2 quotient to distinguish equal mod-3 V_alpha blocks.",
            "Do not infer Pic0 resolution from finite cocycle compatibility alone.",
            "Do not promote fixture-only operator packets to selected source data.",
        ],
    }


def main() -> None:
    previous = load(PREVIOUS_GATE)
    compat = load(Q79_COMPAT)
    template = integral_lift_template()

    compatibility = compat["compatibility"]
    pullback = compat["s3_finite_pullback"]
    valpha = compat["valpha_mod3_blocks"]
    closes = compat["what_this_closes"]
    does_not_close = compat["what_this_does_not_close"]

    output = {
        "certificate": "SelectedQaSU3VAlphaS3Mod3CompatibilityImport",
        "status": "QA_SU3_VALPHA_S3_MOD3_COMPATIBILITY_IMPORTED_INTEGRAL_LIFT_OPEN",
        "inputs": {
            "previous_same_source_gate": str(PREVIOUS_GATE.relative_to(ROOT)),
            "q79_mod3_compatibility": str(Q79_COMPAT),
        },
        "closed_now": {
            "q79_mod3_compatibility_imported": True,
            "finite_active_qutrit_quotient_compatible_with_valpha_blocks": closes[
                "finite_active_qutrit_quotient_compatible_with_valpha_blocks"
            ],
            "selected_s3_commutator_is_nondegenerate_mod3": closes[
                "selected_s3_commutator_is_nondegenerate_mod3"
            ],
            "selected_s3_pullback_table_is_bilinear": closes[
                "selected_s3_pullback_table_is_bilinear"
            ],
            "s3_commutator_gl2_equivalent_to_valpha_g1g2": compatibility[
                "s3_commutator_gl2_equivalent_to_valpha_g1g2"
            ],
            "s3_commutator_gl2_equivalent_to_valpha_g3g4": compatibility[
                "s3_commutator_gl2_equivalent_to_valpha_g3g4"
            ],
            "same_source_gate_reduced_to_integral_lift_or_physical_quotient": True,
        },
        "finite_compatibility": {
            "active_quotient": pullback["active_quotient"],
            "entry_count": pullback["entry_count"],
            "bilinear_matrix_B_left_right_mod3": pullback[
                "bilinear_matrix_B_left_right_mod3"
            ],
            "commutator_matrix_B_minus_BT_mod3": pullback[
                "commutator_matrix_B_minus_BT_mod3"
            ],
            "commutator_determinant_mod3": pullback[
                "commutator_determinant_mod3"
            ],
            "gl2_transform_count_g1g2": compatibility["gl2_transform_count_g1g2"],
            "gl2_transform_count_g3g4": compatibility["gl2_transform_count_g3g4"],
            "direct_matrix_equality_g1g2": compatibility[
                "direct_matrix_equality_g1g2"
            ],
            "direct_matrix_equality_g3g4": compatibility[
                "direct_matrix_equality_g3g4"
            ],
        },
        "valpha_mod3_limit": {
            "selected_L": valpha["selected_L"],
            "selected_L2": valpha["selected_L2"],
            "block_g1g2_mod3": valpha["block_g1g2_mod3"],
            "block_g3g4_mod3": valpha["block_g3g4_mod3"],
            "blocks_equal_mod3": valpha["blocks_equal_mod3"],
            "cannot_distinguish_integral_base_order_from_mod3_data": valpha[
                "blocks_equal_mod3"
            ],
        },
        "not_closed": {
            "same_source_valpha_s3_binding": does_not_close[
                "same_source_valpha_s3_binding"
            ]
            is False,
            "integral_ordered_L3_K2_source_selection": does_not_close[
                "integral_ordered_L3_K2_source_selection"
            ]
            is False,
            "base_factor_order_selection": does_not_close[
                "base_factor_order_selection"
            ]
            is False,
            "Pic0_selection_or_quotient": does_not_close[
                "Pic0_selection_or_quotient"
            ]
            is False,
            "selected_D_E_dotD_Riesz_Green": does_not_close[
                "selected_D_E_dotD_Riesz_Green"
            ]
            is False,
            "primitive_C1_contractions": does_not_close[
                "primitive_C1_contractions"
            ]
            is False,
            "full_SM_closure": does_not_close["full_SM_closure"] is False,
        },
        "next_object": {
            "name": "Selected_Qa_SU3_VAlpha_S3_Integral_Lift_or_Physical_Quotient_v1",
            "template": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
            "minimal_parent_gate": previous["first_true_gate"]["minimal_object"],
        },
        "guardrails": {
            "claims_integral_source_selection": False,
            "claims_same_source_binding": False,
            "claims_pic0_resolved": False,
            "claims_selected_operator_execution": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
        },
        "honest_answer": compat["verdict"]["honest_answer"],
        "why_not_enough": compat["verdict"]["why_not_enough"],
        "next_action": compat["verdict"]["next_action"],
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(
            json.dumps(template, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(cert_text)


if __name__ == "__main__":
    main()
