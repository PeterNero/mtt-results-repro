"""Build CONST-HIGGS-01 H7B1H near-hit source-export audit."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79_REPO = TEXPAPERS / "mtt-q79-proof-repro"
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"
CORPUS_ROOT = Path("C:/ObsidianVault/BrainOfNerodes/Papers/Modal Triplet Theory")

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1h_nearhit_source_export_audit"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RANK_ONE_REJECTION = BASE / "rank_one_higgs_projector_rejection.packet.json"
VALPHA_REJECTION = BASE / "conditional_valpha_msource_rejection.packet.json"
NEARHIT_SCAN = BASE / "current_nearhit_scan.packet.json"
ROUTE_DECISION = BASE / "source_export_route_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1H_NearHitSourceExportAudit_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1H_NEARHIT_SOURCE_EXPORT_AUDIT_BUILT_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def clean_flags() -> dict[str, bool]:
    return {
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1g_path = DATA / "const_higgs_01_h7b1g_fill_bhuv_or_msource.candidate.json"
    h7b1g_bhuv_request_path = DATA / "const_higgs_01_h7b1g_fill_bhuv_or_msource" / "bhuv_minimal_lift_payload_request.packet.json"
    h7b1g_msource_request_path = DATA / "const_higgs_01_h7b1g_fill_bhuv_or_msource" / "msource_minimal_operator_payload_request.packet.json"
    finite_projector_path = SM_PARITY_REPO / "candidate_data" / "selected_finite_projector_source_promotion.candidate.json"
    s3_projector_path = SM_PARITY_REPO / "candidate_data" / "selected_s3_class_restriction_projector_retention.candidate.json"
    visible_gs_path = SM_PARITY_REPO / "candidate_data" / "selected_visible_green_schwarz_operator_source.candidate.json"
    valpha_sufficiency_path = Q79_REPO / "candidate_data" / "selected_valpha_operator_source_sufficiency.candidate.json"
    dotd_c1_path = Q79_REPO / "candidate_data" / "q79_selected_dotd_alpha1_c1_response_emission.candidate.json"
    valpha_all_gates_path = Q79_REPO / "candidate_data" / "all_remaining_valpha_gates_attempt.candidate.json"
    rhoe_ansatz_path = Q79_REPO / "candidate_data" / "visible_rhoE_source_ansatz_search.candidate.json"
    execution_ii_path = CORPUS_ROOT / "18 Theta-Closure & Execution Program" / "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md"

    h7b1g = load(h7b1g_path)
    h7b1g_bhuv_request = load(h7b1g_bhuv_request_path)
    h7b1g_msource_request = load(h7b1g_msource_request_path)
    finite_projector = load(finite_projector_path)
    s3_projector = load(s3_projector_path)
    visible_gs = load(visible_gs_path)
    valpha_sufficiency = load(valpha_sufficiency_path)
    dotd_c1 = load(dotd_c1_path)
    valpha_all_gates = load(valpha_all_gates_path)
    rhoe_ansatz = load(rhoe_ansatz_path)

    h_sector = finite_projector["promoted_sector_slots"]["H"]
    s3_packet = s3_projector["projector_retention_packet"]
    visible_gs_import = visible_gs["imported_results"]
    dotd_frontier = dotd_c1["dotd_alpha1_frontier"]

    rank_one_rejection = {
        "schema": "MTTConstHiggs01H7B1HRankOneProjectorRejection.v1",
        "status": "RANK_ONE_HIGGS_PROJECTOR_NOT_BHUV",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1H-RANK-ONE-PROJECTOR-REJECTION",
        "input_sources": {
            "finite_projector_source_promotion": rel(finite_projector_path),
            "s3_projector_retention": rel(s3_projector_path),
            "H7B1G_B_Huv_request": rel(h7b1g_bhuv_request_path),
        },
        "support_imported": {
            "finite_stationary_projector_replay": finite_projector["what_closes_now"]["finite_stationary_projector_replay"],
            "selected_projector_source_verified": finite_projector["promotion_decision"]["selected_projector_source_verified"],
            "H_sector_projector_rank": h_sector["rank"],
            "H_sector_transport": h_sector["transport"],
            "H_sector_selected_basis_labels": h_sector["selected_basis_labels"],
            "block_factorized_family_Higgs_projector_retention": s3_packet["finite_projector_architecture_retained"],
            "higgs_projector_description": s3_packet["higgs_projector"],
        },
        "why_not_B_Huv": {
            "B_Huv_requires_two_columns": h7b1g_bhuv_request["must_emit"][1],
            "B_Huv_requires_source_orthonormality": h7b1g_bhuv_request["acceptance_tests"]["source_orthonormality_required"],
            "current_H_projector_is_rank_one_collapsed_line": h_sector["rank"] == 1,
            "current_H_transport_is_identity_on_singlet": h_sector["transport"] == "identity on Higgs singlet",
            "no_Hu_Hd_dagger_two_column_lift": True,
            "no_color_triplet_decoupling_certificate": True,
            "no_two_Higgs_metric_or_light_projector": True,
        },
        "promotion_decision": {
            "rank_one_H_projector_promoted_to_B_Huv": False,
            "B_Huv_value_emitted": False,
            "safe_support_for_future_B_Huv": True,
        },
        **clean_flags(),
    }

    valpha_rejection = {
        "schema": "MTTConstHiggs01H7B1HConditionalVAlphaMSourceRejection.v1",
        "status": "CONDITIONAL_VALPHA_VALIDATOR_SUCCESS_NOT_MSOURCE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1H-CONDITIONAL-VALPHA-MSOURCE-REJECTION",
        "input_sources": {
            "valpha_operator_source_sufficiency": rel(valpha_sufficiency_path),
            "visible_gs_operator_source": rel(visible_gs_path),
            "q79_dotd_c1_response": rel(dotd_c1_path),
            "all_remaining_valpha_gates": rel(valpha_all_gates_path),
            "visible_rhoE_ansatz_search": rel(rhoe_ansatz_path),
            "H7B1G_M_source_request": rel(h7b1g_msource_request_path),
        },
        "support_imported": {
            "conditional_valpha_top_report_passes": valpha_sufficiency["hypothetical_top_report"]["status"] == "PASS",
            "conditional_theorem_proved": valpha_sufficiency["conditional_theorem"]["proved"],
            "actual_packet_status": valpha_sufficiency["actual_packet_validation"]["status"],
            "actual_packet_open_item_count": valpha_sufficiency["actual_packet_validation"]["open_item_count"],
            "visible_gs_gate_reduces_to_operator_source": visible_gs["theorem"]["proved"],
            "selected_DE_gap_Riesz_Green_layer_carried": dotd_frontier["selected_DE_gap_layer"]["D_E_gap_Riesz_Green_layer_locked"],
            "same_basis_dotD_value_matrices_available": dotd_frontier["closed_finite_prefix"]["dotD_alpha1_value_matrices_emitted"],
            "ordinary_rhoE_source_routes_retired": rhoe_ansatz["calculation_results"]["ordinary_constant_carriers_blocked"],
            "selected_response_or_twist_route_survives": rhoe_ansatz["surviving_routes"]["primary"],
        },
        "why_not_M_source": {
            "M_source_requires_Hermitian_mass_strain_operator": h7b1g_msource_request["must_emit"][3],
            "M_source_requires_H_sector_restriction": h7b1g_msource_request["must_emit"][4],
            "hypothetical_flags_are_not_physical_proof": valpha_sufficiency["guardrails"]["claims_hypothetical_flags_are_physical_proof"] is False,
            "claims_D_E_dotD_constructed": valpha_sufficiency["guardrails"]["claims_D_E_dotD_constructed"],
            "claims_selected_source_constructed": valpha_sufficiency["guardrails"]["claims_selected_source_constructed"],
            "selected_visible_operator_source_constructed": visible_gs["gate_results"]["selected_visible_operator_source_constructed"],
            "selected_D_E_dotD_Riesz_Green_constructed": visible_gs["gate_results"]["selected_D_E_dotD_Riesz_Green_constructed"],
            "selected_dotD_source_theorem_open": dotd_frontier["remaining_gates"]["selected_dotD_source_theorem"],
            "same_branch_alpha1_driver_theorem_open": dotd_frontier["remaining_gates"]["same_branch_alpha1_driver_theorem"],
            "selected_Hess_Xi_finite_blocks_open": dotd_c1["c1_response_emission_contract"]["not_closed"]["selected_Hess_Xi_finite_blocks"],
        },
        "promotion_decision": {
            "conditional_valpha_promoted_to_M_source": False,
            "M_source_value_emitted": False,
            "safe_support_for_future_M_source": True,
        },
        **clean_flags(),
    }

    nearhit_scan = {
        "schema": "MTTConstHiggs01H7B1HCurrentNearhitScan.v1",
        "status": "NEARHITS_CLASSIFIED_NO_VALUE_EXPORT",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1H-CURRENT-NEARHIT-SCAN",
        "near_hits": {
            "rank_one_H_projector": {
                "support_level": "selected finite projector/source verification",
                "promotable_to_B_Huv": False,
                "reason": "rank-one collapsed H line, not the two-column UV lift (H_u,H_d^dagger)",
            },
            "block_family_Higgs_projector_retention": {
                "support_level": "finite packet compatibility",
                "promotable_to_B_Huv": False,
                "reason": "retains family/Higgs block architecture but does not emit physical light-doublet lift or two-Higgs metric",
            },
            "conditional_valpha_validator_pass": {
                "support_level": "conditional sufficiency",
                "promotable_to_M_source": False,
                "reason": "passes only after hypothetical selected-source flags are supplied",
            },
            "selected_DE_gap_and_dotD_value_prefix": {
                "support_level": "strongest M_source-adjacent prefix",
                "promotable_to_M_source": False,
                "reason": "selected source derivative, alpha1 driver, Hessian blocks, and H-sector Hermitian restriction remain open",
            },
            "execution_ii_split_hym_yukawa_shape": {
                "source": str(execution_ii_path).replace("\\", "/"),
                "source_exists": execution_ii_path.exists(),
                "support_level": "method and shape only",
                "promotable_to_selector": False,
                "reason": "the paper gives a magnetized-brane/split-HYM Yukawa shape and then benchmark local flavor parameters; this cannot select B_Huv or M_source under no-knob guardrails",
            },
        },
        "no_values_exported": {
            "B_Huv": True,
            "M_source": True,
            "Huv": True,
            "Omega": True,
            "s_beta": True,
            "lambda_H": True,
        },
        **clean_flags(),
    }

    route_decision = {
        "schema": "MTTConstHiggs01H7B1HSourceExportRouteDecision.v1",
        "status": "TRY_MSOURCE_FIRST_BHUV_WATCH_REMAINS_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1H-SOURCE-EXPORT-ROUTE-DECISION",
        "route_scores": {
            "B_Huv_first": {
                "score": 2,
                "strengths": [
                    "E6/q79 channel labels are closed",
                    "static SM-slot routing is closed",
                    "rank-one H projector support is real",
                ],
                "blockers": [
                    "current support collapses to one H line",
                    "no physical doublet lift",
                    "no two-column metric/projector",
                    "no color-triplet decoupling certificate",
                ],
            },
            "M_source_first": {
                "score": 4,
                "strengths": [
                    "selected D_E/gap/Riesz/Green prefix is carried",
                    "same-basis dotD value matrices are available",
                    "V_alpha sufficiency validator has no hidden matrix defect",
                    "ordinary rhoE shortcuts are retired, narrowing the response/twist route",
                ],
                "blockers": [
                    "selected source derivative/tangent theorem",
                    "same-branch alpha1 driver",
                    "finite Hess_Xi/H-sector Hermitian restriction",
                    "no lifted-flag promotion",
                ],
            },
        },
        "selected_next_route": "M_source_first",
        "reason": (
            "The B_Huv side currently has only collapsed rank-one Higgs-line support, while the M_source side has a stronger operator prefix: selected D_E/gap support and same-basis dotD values. "
            "Therefore the next constructive attempt should try to turn the selected response/tangent/Hessian prefix into a same-source Hermitian H-sector operator, without promoting hypothetical flags."
        ),
        "exact_next_payload": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1I-MSOURCE-FROM-SELECTED-RESPONSE-PREFIX",
            "must_emit": [
                "selected tangent or retarded derivative source for the q79/F,m=1 operator packet",
                "same-branch alpha1/response driver with honest no-lift replay",
                "finite Hess_Xi or mass/strain block on the selected source space",
                "H-sector restriction map producing a Hermitian M_source",
                "certificate that B_Huv is not needed to verify M_source itself, only to compute H_uv",
            ],
        },
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1HNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1I_MSOURCE_FROM_SELECTED_RESPONSE_PREFIX",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1H-NEXT",
        "primary_next": route_decision["exact_next_payload"],
        "watch_parallel": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / BHUV-WATCH",
            "task": "Continue watching for a real rank-two Higgs lift, two-Higgs metric/projector, or color-triplet decoupling theorem, but do not promote rank-one H projector data.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1HNearhitSourceExportAudit",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1H-NEARHIT-SOURCE-EXPORT-AUDIT",
        "output_packets": {
            "rank_one_higgs_projector_rejection": rel(RANK_ONE_REJECTION),
            "conditional_valpha_msource_rejection": rel(VALPHA_REJECTION),
            "current_nearhit_scan": rel(NEARHIT_SCAN),
            "source_export_route_decision": rel(ROUTE_DECISION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "H7B1HNearHitNonPromotionTheorem",
            "proved": True,
            "statement": (
                "Current near hits strengthen the support but do not export either H7B1G payload. "
                "The selected rank-one H projector and block-family/Higgs retention cannot be promoted to the two-column B_Huv lift. "
                "The V_alpha sufficiency validator and selected D_E/dotD prefix cannot be promoted to M_source without the actual selected-source derivative/Hessian/H-sector restriction. "
                "Thus H7B1H selects M_source-first as the next constructive route while keeping B_Huv on watch."
            ),
        },
        "rank_one_H_projector_promoted_to_B_Huv": False,
        "conditional_valpha_promoted_to_M_source": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "selected_finite_Huv_reduction_found": False,
        "selected_offdiagonal_Omega_found": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "selected_next_route": route_decision["selected_next_route"],
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1I_MSourceFromSelectedResponsePrefix_v1",
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1H_NearHitSourceExportAudit_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "rank_one_H_projector_promoted_to_B_Huv": False,
        "conditional_valpha_promoted_to_M_source": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "selected_next_route": route_decision["selected_next_route"],
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1H Near-Hit Source Export Audit v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1H-NEARHIT-SOURCE-EXPORT-AUDIT`

## Result

```text
rank-one H projector support              True
rank-one H projector -> B_Huv             False
conditional V_alpha sufficiency           True
conditional V_alpha -> M_source           False
B_Huv value emitted                       False
M_source value emitted                    False
H_uv / Omega / s_beta / lambda_H          False
selected next route                       {route_decision["selected_next_route"]}
```

## Why This Matters

H7B1H stops two tempting but invalid promotions:

1. The selected finite projector packet gives a real rank-one H-sector
   projector, but it is the collapsed low-energy Higgs line.  It is not the
   two-column UV lift `B_Huv=(H_u,H_d^dagger)`.
2. The `V_alpha` sufficiency packet proves the validator stack has no hidden
   matrix defect if a real selected-source certificate is supplied.  It is not
   itself a theorem-derived Hermitian `M_source`.

## Next Route

The best next construction is:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1I-MSOURCE-FROM-SELECTED-RESPONSE-PREFIX`

This attacks `M_source` first, using the selected D_E/gap prefix and same-basis
dotD value matrices as support, while requiring an actual selected tangent,
response driver, Hessian/mass-strain block, and H-sector restriction.
"""

    for path, payload in [
        (RANK_ONE_REJECTION, rank_one_rejection),
        (VALPHA_REJECTION, valpha_rejection),
        (NEARHIT_SCAN, nearhit_scan),
        (ROUTE_DECISION, route_decision),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
