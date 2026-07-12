"""Classify candidate visible-source functionals on the q79/q369 orbit."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"

ORBIT = CERTS / "visible_representative_selection_orbit_certificate.json"
DERESPONSE = CERTS / "selected_qa_su3_m1_deresponse_target_import_certificate.json"
S3_LADDER = CERTS / "selected_qa_su3_m1_s3_source_origin_ladder_certificate.json"
VISIBLE_ARCH = CERTS / "selected_qa_su3_visible_source_architecture_certificate.json"
PAYLOAD_MAP = CERTS / "common_de_dotd_riesz_green_payload_map_certificate.json"
ANTI = CERTS / "antiunitary_dedotd_equivalence_test_certificate.json"

OUTPUT = CERTS / "selected_visible_source_functional_on_orbit_classification_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    orbit = load(ORBIT)
    deresponse = load(DERESPONSE)
    s3 = load(S3_LADDER)
    visible_arch = load(VISIBLE_ARCH)
    payload = load(PAYLOAD_MAP)
    anti = load(ANTI)

    orbit_ready = all(
        orbit["closed_now"][key]
        for key in [
            "antiunitary_orbit_is_the_correct_current_object",
            "q79_and_q369_both_retained_in_full_orbit",
            "q79_q369_not_independent_knobs",
        ]
    )
    finite_equivalence_ready = anti["closed_now"][
        "operator_level_antiunitary_equivalence_for_current_finite_packets"
    ]
    m1_fixed_evidence = (
        deresponse["fixed_representative"]["q"] == 79
        and deresponse["fixed_representative"]["orientation"] == "F"
        and deresponse["fixed_representative"]["torsion_label_m"] == 1
        and deresponse["closed_now"]["m1_representative_fixed"]
    )
    s3_source_support = (
        s3["closed_now"]["selected_S3_flat_Deligne_class"]
        and s3["closed_now"]["finite_S3_CP_source_class_matches_q79_m1_twist"]
        and s3["closed_now"]["block_factorized_family_Higgs_projector_retention_for_this_source"]
    )
    architecture_ready = visible_arch["closed_now"]["ranked_architectures_built"]
    common_payload_targeted = payload["path_decision"][
        "construct_Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1_is_correct"
    ]

    candidates = {
        "F0_conjugation_invariant_orbit_functional": {
            "status": "CLOSED_AS_ORBIT_ONLY_NOT_VISIBLE_SELECTOR",
            "closes": [
                "keeps q79/q369 as one full antiunitary object",
                "prevents duplicate branch knobs",
            ],
            "fails_to_close": [
                "which representative is visible",
                "selected source flags",
                "primitive C1/Yukawa contractions on a representative",
            ],
            "verdict": "necessary baseline, insufficient visible selector",
        },
        "F1_time_oriented_m1_representative_functional": {
            "status": "CONDITIONAL_SUPPORT_NOT_SOURCE_THEOREM",
            "support": {
                "q79_F_m1_fixed_representative": m1_fixed_evidence,
                "finite_de_response_stack_validator_coherent_if_source_supplied": deresponse[
                    "closed_now"
                ]["finite_validator_stack_has_no_additional_algebraic_blocker"],
            },
            "fails_to_close": [
                "genuine selected source origin",
                "repo-level selected D_E/dotD data",
                "source flags without lifted assertions",
            ],
            "verdict": "best representative clue, but not yet a proof of visible selection",
        },
        "F2_S3_Deligne_Green_Schwarz_source_support_functional": {
            "status": "PARTIAL_SOURCE_SUPPORT_OPERATOR_EXIT_OPEN",
            "support": {
                "selected_S3_flat_Deligne_class": s3["closed_now"][
                    "selected_S3_flat_Deligne_class"
                ],
                "q79_m1_twist_match": s3["closed_now"][
                    "finite_S3_CP_source_class_matches_q79_m1_twist"
                ],
                "projector_retention_for_this_source": s3["closed_now"][
                    "block_factorized_family_Higgs_projector_retention_for_this_source"
                ],
            },
            "fails_to_close": [
                "coherent spectral zero-mode projectors",
                "selected visible Green-Schwarz/operator source",
                "selected D_E/dotD/Riesz/Green",
            ],
            "verdict": "strongest source support, must be connected to operator payload",
        },
        "F3_same_source_Chern_Weil_operator_functional": {
            "status": "NEXT_PROOF_TARGET",
            "support": {
                "visible_architecture_ranked": architecture_ready,
                "common_payload_map_selects_CW_source_first": common_payload_targeted,
            },
            "must_supply": payload["common_payload"],
            "verdict": "correct next functional if it derives the visible Chern-Weil row from the same selected source",
        },
    }

    output = {
        "certificate": "SelectedVisibleSourceFunctionalOnAntiunitaryOrbitClassification",
        "status": "VISIBLE_SOURCE_FUNCTIONAL_CLASSIFIED_CW_OPERATOR_SOURCE_NEXT",
        "inputs": {
            "orbit": str(ORBIT.relative_to(ROOT)),
            "antiunitary_dedotd": str(ANTI.relative_to(ROOT)),
            "deresponse": str(DERESPONSE.relative_to(ROOT)),
            "s3_source_origin_ladder": str(S3_LADDER.relative_to(ROOT)),
            "visible_source_architecture": str(VISIBLE_ARCH.relative_to(ROOT)),
            "common_payload_map": str(PAYLOAD_MAP.relative_to(ROOT)),
        },
        "closed_now": {
            "orbit_available_for_functional": orbit_ready,
            "finite_operator_packets_equivalent_on_orbit": finite_equivalence_ready,
            "candidate_functional_classes_ranked": True,
            "q79_F_m1_visible_representative_is_best_current_clue": m1_fixed_evidence,
            "S3_Deligne_GS_support_is_best_current_source_support": s3_source_support,
            "next_target_reduced_to_same_source_Chern_Weil_operator_functional": common_payload_targeted,
        },
        "candidates": candidates,
        "not_closed": {
            "visible_representative_selected_by_theorem": True,
            "selected_source_origin_flags": True,
            "same_source_Chern_Weil_operator_row": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "primitive_C1_contractions": True,
            "selected_Yukawa_matrices": True,
            "full_SM_closure": True,
        },
        "next_closing_object": {
            "name": "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1",
            "why_this_not_branch_selection_by_hand": [
                "it acts on the selected orbit through same-source operator data",
                "it derives the visible row before promoting D_E/dotD flags",
                "it can decide whether q79/F,m=1 is visible from source data rather than observed CP",
            ],
            "acceptance": [
                "derive visible Chern-Weil or equivalent operator row from selected S3/monad/GS source",
                "prove Pic0/quotient policy is harmless for the row",
                "emit selected D_E/Riesz/Green/dotD payload or a typed handoff to the validator",
                "do not use observed masses, CKM/PMNS, or CP sign",
            ],
        },
        "guardrails": {
            "claims_visible_q79_selected_now": False,
            "claims_q369_false_or_removed": False,
            "claims_selected_D_E_dotD_now": False,
            "claims_C1_or_Yukawa_closure": False,
            "claims_full_SM_closure": False,
            "uses_observed_cp_sign_or_masses": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "The visible-source functional is not fully proved yet. The allowed "
            "shape is now classified: retain the q79/q369 orbit, use q79/F,m=1 "
            "as the strongest current visible-representative clue, and close "
            "the proof through a same-source Chern-Weil/operator functional "
            "rather than by choosing q79 by hand."
        ),
    }

    if "--write-certificate" in __import__("sys").argv:
        OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
