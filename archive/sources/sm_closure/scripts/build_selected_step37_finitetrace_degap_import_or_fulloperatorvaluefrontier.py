"""Build Step 37 finite-trace D_E/gap import and full-operator frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step37_finitetrace_degap_import_or_fulloperatorvaluefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRACE_IMPORT = PACKET_DIR / "step37_finite_trace_degap_import.packet.json"
FRONTIER = PACKET_DIR / "step37_full_operator_value_frontier.packet.json"
CONTRACT = PACKET_DIR / "step37_next_operator_value_construction_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step37_FiniteTraceDEGapImport_or_FullOperatorValueFrontier_v1.md"

STEP36 = DATA / "selected_step36_s3classclosure_reconciliation_or_operatorvaluefrontier.candidate.json"
STEP36_FRONTIER = DATA / "selected_step36_s3classclosure_reconciliation_or_operatorvaluefrontier" / "step36_operator_value_frontier.packet.json"
TRACE_CANDIDATE = DATA / "selected_tracepayload_or_fullhymoperatoremission.candidate.json"
TRACE_RECON = DATA / "selected_tracepayload_or_fullhymoperatoremission" / "selected_trace_payload_reconciliation.packet.json"
TRACE_SLOT = DATA / "selected_tracepayload_or_fullhymoperatoremission" / "transition_rhoe_or_cech_dolbeault_de_slot_closure.packet.json"
TRACE_POST = DATA / "selected_tracepayload_or_fullhymoperatoremission" / "post_seven_slot_true_equivalence_frontier.packet.json"
HYM_PROMOTION = DATA / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution.candidate.json"
VISIBLE_PAYLOAD = DATA / "selected_visibleoperatorpayload_or_routechymresidual.candidate.json"
SPECTRAL = DATA / "selected_spectral_galerkin_projector_retention_data.candidate.json"
VISIBLE_GS = DATA / "selected_visible_green_schwarz_operator_source.candidate.json"

STATUS = "MTT_SELECTED_STEP37_FINITE_TRACE_DEGAP_IMPORTED_FULL_OPERATOR_VALUES_OPEN"
NEXT = "MTT_Selected_FullOperatorValuePacket_ProjectiveRhoE_DE_RieszGreen_DotD_ZeroModes_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP36,
        STEP36_FRONTIER,
        TRACE_CANDIDATE,
        TRACE_RECON,
        TRACE_SLOT,
        TRACE_POST,
        HYM_PROMOTION,
        VISIBLE_PAYLOAD,
        SPECTRAL,
        VISIBLE_GS,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 37 inputs: " + ", ".join(missing))

    step36 = load(STEP36)
    step36_frontier = load(STEP36_FRONTIER)
    trace = load(TRACE_CANDIDATE)
    trace_recon = load(TRACE_RECON)
    trace_slot = load(TRACE_SLOT)
    trace_post = load(TRACE_POST)
    hym_promotion = load(HYM_PROMOTION)
    visible_payload = load(VISIBLE_PAYLOAD)
    spectral = load(SPECTRAL)
    visible_gs = load(VISIBLE_GS)

    trace_payload = trace_recon["selected_trace_payload"]
    trace_import_checks = {
        "step36_s3_class_frontier_closed": step36["closure_decision"]["selected_s3_differential_cohomology_class_closed"]
        and step36["closure_decision"]["s3_restriction_pullback_table_closed"],
        "step36_operator_values_open_before_import": step36["closure_decision"]["selected_D_E_Riesz_Green_dotD_values_closed"] is False,
        "selected_trace_payload_theorem_proved": trace["theorem"]["proved"] is True,
        "transition_slot_closed_at_finite_trace_layer": trace["closure_decision"][
            "transition_rhoE_or_Cech_Dolbeault_DE_data_closed"
        ]
        is True,
        "selected_trace_equality_proved": trace_payload["selected_trace_equality"]["proved"] is True,
        "selected_gap_lower_bound_positive": trace_payload["selected_gap_lower_bound"] > 0,
        "riesz_green_layer_locked": trace["what_closes_now"]["D_E_gap_Riesz_Green_layer_locked"] is True,
        "full_operator_packet_not_claimed_by_trace_import": trace["closure_decision"][
            "actual_dynamic_QaSU3_operator_packet_closed"
        ]
        is False,
        "full_s2_value_emission_still_open": trace["what_remains_open"]["full_S2_value_emission"] is True,
        "dotd_and_c1_still_open": trace["what_remains_open"]["selected_dotD_alpha1_source_identity"] is True
        and trace["what_remains_open"]["primitive_C1_response"] is True,
        "no_observed_or_benchmark_inputs": trace["observed_data_used_as_selector"] is False
        and trace["target_fitting_used"] is False,
    }
    finite_trace_import_closes = all(trace_import_checks.values())

    trace_import = {
        "schema": "MTTStep37FiniteTraceDEGapImport.v1",
        "status": "FINITE_TRACE_DE_GAP_LAYER_IMPORTED_FROM_SELECTED_TRACE_PAYLOAD",
        "imported_from": {
            "step36": rel(STEP36),
            "selected_trace_payload": rel(TRACE_CANDIDATE),
            "selected_trace_reconciliation": rel(TRACE_RECON),
            "transition_slot_closure": rel(TRACE_SLOT),
        },
        "selected_branch": trace_payload["branch"],
        "basis_id": trace_payload["basis_id"],
        "basis_dimension": trace_payload["basis_dimension"],
        "trace_payload_level": trace_payload["level"],
        "selected_trace_equality": trace_payload["selected_trace_equality"],
        "selected_gap_lower_bound": trace_payload["selected_gap_lower_bound"],
        "selected_green_norm_bound": trace_payload["selected_green_norm_bound"],
        "zero_cluster_indices": trace_payload["zero_cluster_indices"],
        "proof_checks": trace_import_checks,
        "closure_result": {
            "finite_trace_DE_gap_layer_closed": finite_trace_import_closes,
            "transition_rhoE_or_Cech_Dolbeault_DE_data_finite_trace_slot_closed": finite_trace_import_closes,
            "operator_level_projective_rhoE_transition_matrices_closed": False,
            "selected_fullS2_DE_Riesz_Green_dotD_values_closed": False,
            "coherent_spectral_zero_mode_projectors_closed": False,
            "selected_visible_operator_source_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "scope_guard": (
            "This imports the selected Phi_fin finite trace D_E/gap/Riesz/Green layer. "
            "It is not a full operator-value emission and cannot be used as D_E, dotD, C1, "
            "Yukawa, CKM, PMNS, or mass data."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(TRACE_IMPORT, trace_import)

    full_operator_frontier = {
        "schema": "MTTStep37FullOperatorValueFrontier.v1",
        "status": "FULL_OPERATOR_VALUE_PACKET_REMAINS_THE_FRONTIER",
        "closed_support_now_available": {
            "selected_S3_flat_Deligne_class": step36["closure_decision"]["selected_s3_differential_cohomology_class_closed"],
            "selected_S3_pullback_restriction_table": step36["closure_decision"]["s3_restriction_pullback_table_closed"],
            "smooth_Freed_Witten_cancellation": step36["closure_decision"]["smooth_freed_witten_cancellation_closed"],
            "block_family_Higgs_projector_retention": step36["closure_decision"]["block_family_higgs_projector_retention_closed"],
            "visible_Green_Schwarz_curvature_support": visible_gs["gate_results"]["visible_green_schwarz_curvature_closed"],
            "finite_trace_DE_gap_layer": finite_trace_import_closes,
        },
        "still_missing_as_values": {
            "projective_rho_E_transition_matrices": True,
            "selected_covariant_D_E_matrices_on_projective_BN_lift": True,
            "source_verified_Riesz_projectors": True,
            "source_verified_reduced_Green_operators": True,
            "same_branch_dotD_alpha1_matrices": True,
            "coherent_spectral_zero_mode_projectors": True,
            "primitive_C1_overlap_contractions_from_these_values": True,
            "internal_R_theta_scalar_rows": True,
        },
        "why_existing_packets_do_not_close_full_values": {
            "tracepayload_scope": trace["theorem"]["statement"],
            "hym_promotion_scope": hym_promotion["theorem"]["statement"],
            "visible_payload_scope": visible_payload["theorem"]["statement"],
            "spectral_projector_scope": spectral["theorem"]["statement"],
        },
        "demoted_stale_blocker_phrases": [
            "transition/rho_E/Cech-Dolbeault D_E data is fully open",
            "finite D_E/gap trace payload missing",
        ],
        "remaining_live_blocker_phrase": (
            "full same-source operator-value packet missing: rho_E transition matrices, covariant D_E, "
            "Riesz/Green, dotD, coherent zero-mode projectors, and primitive C1 values"
        ),
        "accepted_internal_scalar_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(FRONTIER, full_operator_frontier)

    contract = {
        "schema": "MTTStep37NextOperatorValueConstructionContract.v1",
        "target": NEXT,
        "must_emit_same_source_payload": [
            "non-identity projective rho_E transition matrices on the selected projective B_N basis",
            "finite connection/metric tables compatible with the selected S3 Deligne class and visible GS row",
            "covariant D_E matrices sector by sector in the same basis",
            "Riesz projectors defined by the selected spectral contour with an explicit positive complement gap",
            "reduced Green operators with norm and truncation/error certificates",
            "dotD_alpha1 matrices obtained as the same-branch derivative of the emitted D_E package",
            "ordered zero-mode bases and coherent spectral projectors retained under the selected S3 block action",
            "primitive C1 contractions computed from the emitted zero modes, Green response, and dotD payload",
        ],
        "acceptance_tests": {
            "same_source": "Every emitted value must cite the same q79/F,m=1 selected S3/GS/Phi_fin branch.",
            "non_identity": "rho_E cannot be the identity smoke packet or only a trace scalar.",
            "projective_cocycle": "transition matrices must satisfy the selected central-cocycle law and the S3 restriction table.",
            "operator_equations": "D_E, Riesz, Green, dotD, and C1 tensors must satisfy the existing validators without lifted source flags.",
            "gap": "Riesz contour and Green inverse require a positive gap with error bounds.",
            "no_proxy_fit": "Observed SM masses, mixings, or benchmark rows cannot select or tune the packet.",
        },
        "minimum_closure_keys_for_next_candidate": {
            "operator_level_projective_rhoE_transition_matrices_closed": True,
            "selected_covariant_D_E_matrices_closed": True,
            "selected_Riesz_Green_values_closed": True,
            "same_branch_dotD_alpha1_values_closed": True,
            "coherent_spectral_zero_mode_projectors_closed": True,
            "primitive_C1_contractions_from_operator_values_closed": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CONTRACT, contract)

    candidate = {
        "candidate": "MTTSelectedStep37FiniteTraceDEGapImportOrFullOperatorValueFrontier",
        "status": STATUS,
        "inputs": {
            "step36": rel(STEP36),
            "step36_frontier": rel(STEP36_FRONTIER),
            "selected_trace_payload": rel(TRACE_CANDIDATE),
            "selected_trace_reconciliation": rel(TRACE_RECON),
            "transition_slot_closure": rel(TRACE_SLOT),
            "post_trace_frontier": rel(TRACE_POST),
            "hym_promotion_scope_check": rel(HYM_PROMOTION),
            "visible_payload_scope_check": rel(VISIBLE_PAYLOAD),
            "spectral_projector_scope_check": rel(SPECTRAL),
            "visible_gs_scope_check": rel(VISIBLE_GS),
        },
        "output_packets": {
            "finite_trace_degap_import": rel(TRACE_IMPORT),
            "full_operator_value_frontier": rel(FRONTIER),
            "next_operator_value_construction_contract": rel(CONTRACT),
        },
        "theorem": {
            "name": "Step37FiniteTraceDEGapImportTheorem",
            "proved": finite_trace_import_closes,
            "statement": (
                "After Step36 closes the selected S3 class/restriction layer, the already-verified "
                "selected trace payload imports the q79/F,m=1 Phi_fin finite trace D_E/gap/Riesz/Green "
                "layer into the active frontier. Therefore the old transition-trace blocker is retired. "
                "The remaining live target is stronger: emit the full same-source operator-value packet, "
                "not just trace/gap data."
            ),
        },
        "closure_decision": {
            "selected_s3_class_restriction_layer_closed": True,
            "finite_trace_DE_gap_layer_closed": finite_trace_import_closes,
            "transition_rhoE_or_Cech_Dolbeault_DE_data_finite_trace_slot_closed": finite_trace_import_closes,
            "selected_trace_equality_closed": finite_trace_import_closes,
            "positive_gap_Riesz_Green_lock_imported": finite_trace_import_closes,
            "operator_level_projective_rhoE_transition_matrices_closed": False,
            "selected_covariant_D_E_matrices_closed": False,
            "selected_Riesz_Green_values_closed": False,
            "same_branch_dotD_alpha1_values_closed": False,
            "coherent_spectral_zero_mode_projectors_closed": False,
            "primitive_C1_contractions_from_operator_values_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": finite_trace_import_closes,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step37_FiniteTraceDEGapImport_or_FullOperatorValueFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "finite_trace_DE_gap_layer_closed": finite_trace_import_closes,
        "transition_rhoE_or_Cech_Dolbeault_DE_data_finite_trace_slot_closed": finite_trace_import_closes,
        "selected_trace_equality_closed": finite_trace_import_closes,
        "positive_gap_Riesz_Green_lock_imported": finite_trace_import_closes,
        "full_operator_value_packet_closed": False,
        "operator_level_projective_rhoE_transition_matrices_closed": False,
        "selected_covariant_D_E_matrices_closed": False,
        "selected_Riesz_Green_values_closed": False,
        "same_branch_dotD_alpha1_values_closed": False,
        "coherent_spectral_zero_mode_projectors_closed": False,
        "primitive_C1_contractions_from_operator_values_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step37 FiniteTraceDEGapImport or FullOperatorValueFrontier v1

Status: `{STATUS}`.

Step37 imports the already-verified selected trace payload into the active
post-Step36 frontier. This closes the finite trace `D_E`/gap/Riesz/Green layer
for the selected q79/F,m=1 `Phi_fin` branch.

This retires the stale blocker phrase "transition trace/D_E gap data missing."

It does not close:

- full projective `rho_E` transition matrices
- selected covariant `D_E` matrices
- selected Riesz/Green values as full operators
- same-branch `dotD_alpha1`
- coherent spectral zero-mode projectors
- primitive C1 contractions from these values
- internal `R_theta` scalar rows or true SM equivalence

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
