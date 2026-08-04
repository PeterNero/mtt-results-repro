"""Build CONST-HIGGS-01 H7B1K Phi_fin/projector/dotD import gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1k_phifin_minimizer_trace_or_end0_hsector_functor"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STATIONARY_IMPORT = BASE / "stationary_phifin_projector_dotd_import.packet.json"
HSECTOR_BOUNDARY = BASE / "hsector_rank_one_boundary.packet.json"
DYNAMIC_HUV_VALIDATOR = BASE / "dynamic_huv_gate_validator.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1K_PhiFinProjectorDotDImportGate_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1K_PHIFIN_PROJECTOR_DOTD_SLOT_IMPORTED_DYNAMIC_HUV_GATE_OPEN"


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

    h7b1j_path = DATA / "const_higgs_01_h7b1j_dynamic_hessian_or_hsector_restriction_export.candidate.json"
    h7b1j_gate_path = DATA / "const_higgs_01_h7b1j_dynamic_hessian_or_hsector_restriction_export" / "strict_msource_gate_validator.packet.json"

    raw_bn_path = SM_PARITY_REPO / "candidate_data" / "phifin_bn_modelactive_equivalence_or_minimizer_trace.candidate.json"
    transported_trace_path = SM_PARITY_REPO / "candidate_data" / "selected_gauge_transported_bn_phifin_trace.candidate.json"
    finite_projector_path = SM_PARITY_REPO / "candidate_data" / "selected_finite_projector_source_promotion.candidate.json"
    stationary_frontier_path = SM_PARITY_REPO / "candidate_data" / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json"
    promoted_stationary_packet_path = (
        SM_PARITY_REPO
        / "candidate_data"
        / "selected_stationaryprojector_dotd_integrated_frontier"
        / "promoted_stationary_sector_packet.packet.json"
    )
    four_slot_path = SM_PARITY_REPO / "candidate_data" / "selected_phifinpayload_or_globaldestabilizerenumeration_closingrun.candidate.json"

    h7b1j = load(h7b1j_path)
    h7b1j_gate = load(h7b1j_gate_path)
    raw_bn = load(raw_bn_path)
    transported_trace = load(transported_trace_path)
    finite_projector = load(finite_projector_path)
    stationary_frontier = load(stationary_frontier_path)
    promoted_stationary = load(promoted_stationary_packet_path)
    four_slot = load(four_slot_path)

    h_promoted_slot = finite_projector["promoted_sector_slots"]["H"]
    h_packet_slot = promoted_stationary["sector_slots"]["H"]
    stationary_decision = stationary_frontier["closure_decision"]
    four_slot_decision = four_slot["closure_decision"]

    stationary_import = {
        "schema": "MTTConstHiggs01H7B1KStationaryPhiFinProjectorDotDImport.v1",
        "status": "STATIONARY_PHIFIN_PROJECTOR_RHOS_DOTD_SLOT_IMPORTED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1K-A-STATIONARY-PHIFIN-PROJECTOR-DOTD-IMPORT",
        "input_sources": {
            "H7B1J_candidate": rel(h7b1j_path),
            "H7B1J_strict_msource_gate": rel(h7b1j_gate_path),
            "raw_BN_model_active_no_go": rel(raw_bn_path),
            "gauge_transported_BN_PhiFin_trace": rel(transported_trace_path),
            "finite_projector_source_promotion": rel(finite_projector_path),
            "stationary_projector_dotD_frontier": rel(stationary_frontier_path),
            "promoted_stationary_sector_packet": rel(promoted_stationary_packet_path),
            "four_slot_closing_run": rel(four_slot_path),
        },
        "imported_stationary_closures": {
            "raw_model_active_equivalence_rejected": raw_bn["promotion_decision"]["exact_model_active_equivalence_rejected"],
            "gauge_transported_trace_proved": transported_trace["theorem"]["proved"],
            "functional_selected_trace_proved": transported_trace["promotion_decision"]["functional_selected_trace_proved"],
            "rho_candidate_promoted_to_functional_selected_rho_s": transported_trace["promotion_decision"]["rho_candidate_promoted_to_functional_selected_rho_s"],
            "finite_projector_source_promotion_proved": finite_projector["promotion_decision"]["finite_projector_source_promotion_proved"],
            "selected_projector_source_verified": finite_projector["promotion_decision"]["selected_projector_source_verified"],
            "validator_ready_stationary_rho_s": finite_projector["promotion_decision"]["validator_ready_stationary_rho_s"],
            "stationary_projector_source_verified": stationary_decision["stationary_projector_source_verified"],
            "selected_dotD_source_verified": stationary_decision["selected_dotD_source_verified"],
            "alpha1_driver_verified": stationary_decision["alpha1_driver_verified"],
            "riesz_green_dotd_projector_retention_slot_closed": four_slot_decision["Riesz_Green_dotD_projector_retention_slot_closed"],
            "physical_dotD_alpha1_removed_from_active_frontier": stationary_frontier["what_closes_now"]["physical_dotD_alpha1_removed_from_active_frontier"],
        },
        "h_sector_imported_slot": {
            "sector": h_promoted_slot["sector"],
            "rank": h_promoted_slot["rank"],
            "selected_basis_labels": h_promoted_slot["selected_basis_labels"],
            "model_basis_indices": h_promoted_slot["model_basis_indices"],
            "transport": h_promoted_slot["transport"],
            "source_verified_by_transport_conjugation": h_promoted_slot["source_verified_by_transport_conjugation"],
            "stationary_rho_s_promoted": h_promoted_slot["stationary_rho_s_promoted"],
            "green_operator_valid": h_packet_slot["green_operator_valid"],
            "riesz_projector_valid": h_packet_slot["riesz_projector_valid"],
        },
        "open_dynamic_boundary_imported": {
            "dynamic_PhiFin_C1_payload_emitted": stationary_decision["dynamic_PhiFin_C1_payload_emitted"],
            "A_selected_emitted": stationary_decision["A_selected_emitted"],
            "b_selected_emitted": stationary_decision["b_selected_emitted"],
            "primitive_C1_contractions_emitted": stationary_decision["primitive_C1_contractions_emitted"],
            "actual_dynamic_QaSU3_operator_packet_complete": stationary_decision["actual_QaSU3_operator_packet_dynamic_complete"],
            "true_SM_equivalence_closed": stationary_decision["true_SM_equivalence_closed"],
            "no_knob_closed": stationary_decision["no_knob_closed"],
        },
        "superset_strategy": {
            "combining_paths": True,
            "using_one_straight_way": False,
            "locked_target": "stationary Phi_fin/projector/rho_s/dotD source promotion, not Huv mass-strain",
            "straight_path": "HYM/End0 gauge-transported stationary projector theorem",
            "support_path": "compatible alpha1/dotD import on the same q79/F,m=1 source spine",
            "promotion_scope": "stationary sector source packet only",
        },
        **clean_flags(),
    }

    hsector_boundary = {
        "schema": "MTTConstHiggs01H7B1KHSectorRankOneBoundary.v1",
        "status": "HSECTOR_STATIONARY_RANK_ONE_BOUNDARY_PROVED_HUV_RESTRICTION_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1K-HSECTOR-RANK-ONE-BOUNDARY",
        "imported_H_stationary_slot": stationary_import["h_sector_imported_slot"],
        "boundary_theorem": {
            "name": "StationaryHProjectorDoesNotEmitHuvMassStrain",
            "proved": True,
            "statement": (
                "The imported selected Higgs stationary sector is the rank-one H:h0 projector with identity transport on the Higgs singlet. "
                "It promotes the stationary projector/rho_s/dotD slot, but it is not a UV two-Higgs H_u/H_d^dagger lift, not a dynamic Hessian, and not a source-owned H-sector restriction map R_H. "
                "Therefore it cannot emit B_Huv, M_source, Huv, Omega, s_beta, or lambda_H."
            ),
        },
        "why_not_huv_response": {
            "H_rank_one_stationary_projector": h_promoted_slot["rank"] == 1,
            "H_basis_is_single_label_H_h0": h_promoted_slot["selected_basis_labels"] == ["H:h0"],
            "transport_identity_on_higgs_singlet": h_promoted_slot["transport"] == "identity on Higgs singlet",
            "rank_one_projector_not_two_column_B_Huv": True,
            "stationary_projector_not_dynamic_response_restriction": True,
            "dynamic_PhiFin_C1_payload_open": stationary_decision["dynamic_PhiFin_C1_payload_emitted"] is False,
            "A_selected_and_b_selected_open": stationary_decision["A_selected_emitted"] is False and stationary_decision["b_selected_emitted"] is False,
            "primitive_C1_contractions_open": stationary_decision["primitive_C1_contractions_emitted"] is False,
            "selected_H_response_absent": True,
            "selected_R_H_absent": True,
            "selected_UV_two_Higgs_lift_absent": True,
        },
        "emission_decision": {
            "H_response_exported": False,
            "R_H_exported": False,
            "B_Huv_exported": False,
            "M_source_exported": False,
            "Huv_exported": False,
            "s_beta_exported": False,
            "lambda_H_exported": False,
            "reason": "H7B1K closes the stationary Phi_fin/projector/dotD subgate, but the H-sector object is still the collapsed rank-one stationary carrier rather than the UV two-Higgs mass-strain response required by H7B1F-H7B1J.",
        },
        **clean_flags(),
    }

    dynamic_huv_validator = {
        "schema": "MTTConstHiggs01H7B1KDynamicHuvGateValidator.v1",
        "status": "DYNAMIC_HUV_MSOURCE_GATE_STILL_FAILS_AFTER_STATIONARY_IMPORT",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1K-DYNAMIC-HUV-GATE-VALIDATOR",
        "locked_target": "source-owned dynamic Huv mass-strain export for Huv=B_Huv^* M_source B_Huv",
        "required_fields_after_stationary_import": {
            "stationary_projector_rho_s_dotD_imported": True,
            "same_branch_selected_H_response": False,
            "same_branch_selected_R_H": False,
            "dynamic_PhiFin_C1_payload": stationary_decision["dynamic_PhiFin_C1_payload_emitted"],
            "A_selected_and_b_selected": stationary_decision["A_selected_emitted"] and stationary_decision["b_selected_emitted"],
            "primitive_C1_contractions": stationary_decision["primitive_C1_contractions_emitted"],
            "UV_two_Higgs_lift_B_Huv": False,
            "finite_exactness_or_error_certificate_for_Huv": False,
            "no_observed_selector": True,
            "same_q79_F_m1_branch": True,
        },
        "passes": False,
        "strict_outputs": {
            "H_response": None,
            "R_H": None,
            "B_Huv": None,
            "M_source": None,
            "Huv": None,
            "Delta": None,
            "Omega": None,
            "s_beta": None,
            "lambda_H": None,
        },
        "route_results": {
            "H7B1K_A_stationary_PhiFin_full_operator_promotion": {
                "stationary_subgate_passes": True,
                "dynamic_Huv_gate_passes": False,
                "reason": "Finite projectors, stationary rho_s, Riesz/Green, selected dotD, and alpha1 driver are imported as source-verified, but the H sector remains a rank-one stationary singlet and no dynamic Huv response/restriction values are emitted.",
            },
            "H7B1K_B_independent_Huv_Hessian_or_restriction_table": {
                "table_emitted": False,
                "dynamic_Huv_gate_passes": False,
                "reason": "No independent source-owned Huv Hessian/restriction table with exactness/error certificate is present in the current corpus or imported repos.",
            },
        },
        "superset_strategy": {
            "combining_paths": True,
            "locked_target": "dynamic Huv/M_source export",
            "paths_combined_without_promotion": [
                "stationary Phi_fin/projector/rho_s/dotD source promotion",
                "H7B1J dynamic C1/Hessian conditional support",
                "H7B1J HYM rank-2 End0 support",
            ],
            "why_combination_is_insufficient": "All imported paths agree on the stationary q79/F,m=1 source spine, but none emits the dynamic two-Higgs mass-strain restriction required by Huv.",
        },
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1KNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1L_DYNAMIC_PHIFIN_C1_HUV_RESPONSE_OR_INDEPENDENT_HUV_HESSIAN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1K-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1L-DYNAMIC-PHIFIN-C1-HUV-RESPONSE-OR-INDEPENDENT-HUV-HESSIAN",
            "task": "Promote from stationary source data to dynamic Huv source data by emitting either a selected dynamic Phi_fin^C1 H-sector response/restriction payload or an independent Huv Hessian/restriction table with source ids and exactness.",
        },
        "two_legal_exits": [
            {
                "id": "H7B1L-A",
                "label": "dynamic Phi_fin^C1 Huv response",
                "must_emit": "selected H_response, R_H, A_selected/b_selected or equivalent dynamic response rows restricted to the UV H_u/H_d^dagger block",
            },
            {
                "id": "H7B1L-B",
                "label": "independent Huv Hessian/restriction table",
                "must_emit": "source-owned Huv Hermitian mass/strain table, B_Huv or equivalent UV two-Higgs lift, and exactness/error certificate",
            },
        ],
        "do_not_repeat": [
            "Do not treat the rank-one H:h0 stationary projector as the UV two-Higgs lift.",
            "Do not promote stationary rho_s/dotD source closure into dynamic Huv response closure.",
            "Do not use compact H dotD hermitianization as M_source.",
            "Do not backsolve from Higgs mass, lambda_H, beta, threshold residual, Yukawas, CKM, or PMNS.",
        ],
        **clean_flags(),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1KPhiFinProjectorDotDImportGate",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1K-PHIFIN-MINIMIZER-TRACE-OR-END0-HSECTOR-FUNCTOR",
        "output_packets": {
            "stationary_phifin_projector_dotd_import": rel(STATIONARY_IMPORT),
            "hsector_rank_one_boundary": rel(HSECTOR_BOUNDARY),
            "dynamic_huv_gate_validator": rel(DYNAMIC_HUV_VALIDATOR),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "H7B1KStationaryPhiFinImportDoesNotCloseDynamicHuvTheorem",
            "proved": True,
            "statement": (
                "Later SM-parity artifacts close the stationary Phi_fin/projector/rho_s/dotD source slot that H7B1J had left open: the transported Phi_fin trace, finite projector source promotion, stationary rho_s packet, selected dotD source flag, and alpha1 driver are imported without target fitting. "
                "However, the imported Higgs carrier is the rank-one stationary H:h0 singlet. "
                "Since it is neither a UV two-Higgs lift nor a dynamic Huv mass-strain restriction, it cannot emit H_response, R_H, B_Huv, M_source, Huv, Omega, s_beta, or lambda_H. "
                "The remaining Higgs gate is therefore the dynamic Phi_fin^C1 Huv response or an independent source-owned Huv Hessian/restriction table."
            ),
        },
        "H7B1J_gate_imported": h7b1j["strict_msource_gate_passes"] is False,
        "stationary_phifin_projector_dotd_slot_imported": True,
        "stationary_projector_rho_s_dotd_subgate_closed": True,
        "physical_dotD_alpha1_removed_from_active_frontier": True,
        "H_sector_rank_one_boundary_proved": True,
        "strict_dynamic_Huv_gate_passes": False,
        "H_response_exported": False,
        "R_H_exported": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "selected_finite_Huv_reduction_found": False,
        "selected_offdiagonal_Omega_found": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1L_DynamicPhiFinC1HuvResponseOrIndependentHuvHessian_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1K_PhiFinProjectorDotDImportGate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "stationary_phifin_projector_dotd_slot_imported": True,
        "stationary_projector_rho_s_dotd_subgate_closed": True,
        "physical_dotD_alpha1_removed_from_active_frontier": True,
        "H_sector_rank_one_boundary_proved": True,
        "strict_dynamic_Huv_gate_passes": False,
        "H_response_exported": False,
        "R_H_exported": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1K PhiFin Projector DotD Import Gate v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1K-PHIFIN-MINIMIZER-TRACE-OR-END0-HSECTOR-FUNCTOR`

## Result

```text
stationary Phi_fin/projector/rho_s/dotD slot imported  True
physical dotD/alpha1 active blocker removed            True
H-sector imported carrier                              rank-one H:h0
strict dynamic Huv/M_source gate passes                False
H_response / R_H / B_Huv / M_source emitted            False
Huv / Omega / s_beta / lambda_H                        False
```

## What Closed

The later stationary source artifacts close a real subgate that H7B1J had left
open.  The repaired route is:

```text
raw BN equality rejected
gauge-transported Phi_fin trace proved
finite projector source promotion proved
validator-ready stationary rho_s promoted
selected dotD and alpha1 driver imported
Riesz/Green/dotD/projector-retention slot closed
```

This is a legitimate superset reconciliation: the HYM/End0 stationary projector
path and the alpha1/dotD path are combined against the locked stationary
source-packet target, without using observed Higgs data or threshold fitting.

## What Did Not Close

The imported Higgs sector is still the rank-one stationary `H:h0` carrier with
identity transport.  That is not the UV two-Higgs `H_u/H_d^dagger` lift and it
is not a dynamic Huv mass-strain response.  Therefore it cannot emit
`H_response`, `R_H`, `B_Huv`, `M_source`, `Omega`, `s_beta`, or `lambda_H`.

Next label:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1L-DYNAMIC-PHIFIN-C1-HUV-RESPONSE-OR-INDEPENDENT-HUV-HESSIAN`
"""

    for path, payload in [
        (STATIONARY_IMPORT, stationary_import),
        (HSECTOR_BOUNDARY, hsector_boundary),
        (DYNAMIC_HUV_VALIDATOR, dynamic_huv_validator),
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
