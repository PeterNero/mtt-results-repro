"""Import the q79 S3 source-origin ladder for the m=1 de_response gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_CERTS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\certificates")

DERESPONSE_IMPORT = CERTS / "selected_qa_su3_m1_deresponse_target_import_certificate.json"
FINITE_CP = Q79_CERTS / "visible_twisted_s3_finite_cp_cancellation_certificate.json"
SMOOTH_LIFT_ATTEMPT = Q79_CERTS / "visible_twisted_s3_smooth_source_lift_attempt_certificate.json"
CLASS_RESTRICTION_ATTEMPT = (
    Q79_CERTS / "visible_twisted_s3_class_restriction_packet_attempt_certificate.json"
)
CLASS_RESTRICTION_CLOSURE = (
    Q79_CERTS / "visible_twisted_s3_class_restriction_closure_certificate.json"
)
DELIGNE_GAUGE = Q79_CERTS / "iwasawa_deligne_cover_gauge_reduction_certificate.json"

OUTPUT_CERT = CERTS / "selected_qa_su3_m1_s3_source_origin_ladder_certificate.json"
OUTPUT_TEMPLATE = (
    CERTS / "selected_qa_su3_m1_spectral_projector_de_dotd_source.template.json"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def spectral_source_template() -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3M1SpectralProjectorDEDotDSource.v1",
        "status": "OPEN_SELECTED_QA_SU3_M1_SPECTRAL_PROJECTOR_DE_DOTD_SOURCE_REQUIRED",
        "purpose": (
            "Use the selected smooth S3 twisted source as input, then prove the "
            "coherent spectral zero-mode projector theorem and construct the "
            "selected D_E/dotD/Riesz/Green operator-source packet on the same branch."
        ),
        "accepted_prerequisites": {
            "selected_S3_flat_Deligne_class": "from visible_twisted_s3_class_restriction_closure_certificate.json",
            "smooth_S3_twisted_Freed_Witten_cancellation": "from visible_twisted_s3_class_restriction_closure_certificate.json",
            "block_factorized_family_Higgs_projector_retention_for_this_source": "from visible_twisted_s3_class_restriction_closure_certificate.json",
        },
        "must_supply": {
            "coherent_spectral_zero_mode_projector_retention": None,
            "selected_visible_Green_Schwarz_operator_source": None,
            "selected_D_E_files": None,
            "selected_Riesz_Green_files": None,
            "selected_dotD_alpha1_files": None,
            "primitive_C1_contraction_inputs": None,
            "promotion_report_showing_same_source_for_all_rows": None,
        },
        "acceptance_tests": [
            "The spectral projector is proved, not inferred from block-sector family/Higgs retention.",
            "The selected D_E, reduced Green, Riesz/gap, and dotD packets all cite the same selected S3 source.",
            "The dotD validator has selected_dotD_source_verified and alpha1_driver_verified true for source reasons.",
            "No benchmark flavor matrices, observed masses, CKM/PMNS entries, or observed CP sign are inputs.",
        ],
        "forbidden_shortcuts": [
            "Do not equate block-factorized projectors with coherent spectral zero-mode projectors.",
            "Do not treat a finite CP cancellation as a selected differential operator source.",
            "Do not make q=79 depend on measured flavor data.",
        ],
    }


def main() -> None:
    deresponse = load(DERESPONSE_IMPORT)
    finite_cp = load(FINITE_CP)
    smooth_lift_attempt = load(SMOOTH_LIFT_ATTEMPT)
    class_attempt = load(CLASS_RESTRICTION_ATTEMPT)
    class_closure = load(CLASS_RESTRICTION_CLOSURE)
    deligne_gauge = load(DELIGNE_GAUGE)
    template = spectral_source_template()

    closes = class_closure["what_this_closes"]
    calculations = class_closure["calculation_results"]
    still_open = class_closure["still_open"]
    guardrails = class_closure["guardrails"]
    finite_closes = finite_cp["what_this_closes"]

    output = {
        "certificate": "SelectedQaSU3M1S3SourceOriginLadder",
        "status": "QA_SU3_M1_S3_SOURCE_ORIGIN_LADDER_IMPORTED_SPECTRAL_DE_DOTD_OPEN",
        "inputs": {
            "previous_deresponse_import": str(DERESPONSE_IMPORT.relative_to(ROOT)),
            "q79_deligne_cover_gauge_reduction": str(DELIGNE_GAUGE),
            "q79_visible_twisted_s3_finite_cp_cancellation": str(FINITE_CP),
            "q79_visible_twisted_s3_smooth_source_lift_attempt": str(
                SMOOTH_LIFT_ATTEMPT
            ),
            "q79_visible_twisted_s3_class_restriction_attempt": str(
                CLASS_RESTRICTION_ATTEMPT
            ),
            "q79_visible_twisted_s3_class_restriction_closure": str(
                CLASS_RESTRICTION_CLOSURE
            ),
        },
        "closed_now": {
            "cover_gauge_reduction_is_auxiliary_not_a_knob": (
                deligne_gauge["what_this_closes"][
                    "cover_refinement_invariance_for_Deligne_Cech_representatives"
                ]
                is True
            ),
            "finite_S3_CP_source_class_matches_q79_m1_twist": finite_closes[
                "S3_finite_CP_source_class_matches_q79_m1_twist"
            ],
            "finite_rank_two_S3_DD_obstruction_cancellable_by_twisted_CP": finite_closes[
                "finite_rank_two_S3_DD_obstruction_is_cancellable_by_twisted_CP"
            ],
            "selected_S3_flat_Deligne_class": closes["selected_S3_flat_Deligne_class"],
            "selected_S3_pullback_restriction_table": closes[
                "selected_S3_pullback_restriction_table"
            ],
            "smooth_S3_twisted_Freed_Witten_cancellation": closes[
                "smooth_S3_twisted_Freed_Witten_cancellation"
            ],
            "block_factorized_family_Higgs_projector_retention_for_this_source": closes[
                "block_factorized_family_Higgs_projector_retention_for_this_source"
            ],
            "class_restriction_validator_passed": class_closure["validator_result"][
                "selected_packet_exit_code"
            ]
            == 0,
        },
        "earlier_attempts_that_correctly_refused_promotion": {
            "smooth_source_lift_attempt_status": smooth_lift_attempt["status"],
            "smooth_source_lift_attempt_refused_until_selected_cover_and_projectors": smooth_lift_attempt[
                "calculation_results"
            ][
                "attempt_refused_until_selected_cover_and_projectors"
            ],
            "class_restriction_attempt_status": class_attempt["status"],
            "class_restriction_attempt_refused_until_smooth_class_and_projectors": class_attempt[
                "calculation_results"
            ][
                "attempt_refused_until_smooth_class_and_projectors"
            ],
            "later_closure_supplies_the_missing_smooth_class_restriction_and_block_projectors": True,
        },
        "not_closed": {
            "coherent_spectral_zero_mode_projector_retention": still_open[
                "coherent_spectral_zero_mode_projector_retention"
            ],
            "selected_D_E_dotD_Riesz_Green": still_open[
                "selected_D_E_dotD_Riesz_Green"
            ],
            "selected_visible_Green_Schwarz_operator_source": still_open[
                "selected_visible_Green_Schwarz_operator_source"
            ],
            "primitive_C1_contractions": still_open["primitive_C1_contractions"],
            "Yukawa_CKM_PMNS_magnitudes": still_open["Yukawa_CKM_PMNS_magnitudes"],
            "full_SM_closure": still_open["full_SM_closure"],
        },
        "relation_to_deresponse_gate": {
            "previous_status": deresponse["status"],
            "deresponse_source_origin_gap_partially_reduced": True,
            "removed_from_source_origin_gap": [
                "finite S3 twisted CP cancellation",
                "selected smooth S3 flat Deligne class and restriction table",
                "smooth S3 twisted Freed-Witten cancellation",
                "block-sector family/Higgs projector retention for this source",
            ],
            "remaining_source_origin_gap": [
                "coherent spectral zero-mode projector retention",
                "selected visible Green-Schwarz/operator source",
                "repo-level selected D_E/dotD/Riesz/Green files",
            ],
        },
        "next_object": {
            "name": "Selected_Qa_SU3_M1_Spectral_Projector_DE_DotD_Source_v1",
            "template": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
            "role": class_closure["verdict"]["next_closing_object"],
        },
        "guardrails": {
            "claims_coherent_spectral_zero_mode_projectors": guardrails[
                "claims_coherent_spectral_zero_mode_projectors"
            ],
            "claims_selected_D_E_dotD_constructed": guardrails[
                "claims_selected_D_E_dotD_constructed"
            ],
            "claims_visible_operator_source_constructed": guardrails[
                "claims_visible_operator_source_constructed"
            ],
            "claims_full_SM_closure": guardrails["claims_full_SM_closure"],
            "uses_benchmark_flavor_entries": guardrails["uses_benchmark_flavor_entries"],
            "uses_observed_flavor_data": guardrails["uses_observed_flavor_data"],
        },
        "honest_answer": (
            "The source-origin gap is now split. The selected smooth S3 flat "
            "Deligne/Freed-Witten/block-projector part is imported as closed, "
            "while the coherent spectral projector and selected D_E/dotD "
            "operator-source data remain open."
        ),
        "q79_verdict_carried_forward": class_closure["verdict"]["honest_answer"],
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
