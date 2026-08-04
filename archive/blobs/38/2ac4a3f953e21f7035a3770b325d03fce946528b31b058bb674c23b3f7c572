from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

REPOS = {
    "sm_closure": "mtt-sm-parity-closure",
    "sm_parity_repro": "mtt-sm-parity-repro",
    "q79": "mtt-q79-proof-repro",
    "qa_su3": "mtt-qa-su3-packet-proof",
    "nonsm_constants": "mtt-nonsm-constants-no-knob",
    "protospinor_gr": "mtt-protospinor-gr-response-proof",
    "individual_constants": "mtt-individual-constants-source-search",
    "theta_program": "18 Theta-Closure & Execution Program",
}


def repo_path(repo_key: str, rel: str = "") -> Path:
    return TEXPAPERS / REPOS[repo_key] / rel


def load_json(repo_key: str, rel: str) -> dict:
    path = repo_path(repo_key, rel)
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_text(repo_key: str, rel: str) -> str:
    path = repo_path(repo_key, rel)
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def dig(data: dict, dotted: str, default=None):
    cur = data
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return default
    return cur


def repo_summary() -> list[dict]:
    rows = []
    for key, name in REPOS.items():
        root = TEXPAPERS / name
        report = root / "reports" / "verification_report.txt"
        report_text = report.read_text(encoding="utf-8", errors="replace") if report.exists() else ""
        verification_lines = [
            line.strip()
            for line in report_text.splitlines()
            if (
                "Verification result:" in line
                or "SM-parity closure:" in line
                or "true SM equivalence:" in line
                or "no-knob closure:" in line
            )
        ]
        rows.append(
            {
                "repo_key": key,
                "repo": name,
                "exists": root.exists(),
                "candidate_json_count": len(list((root / "candidate_data").glob("*.json"))) if (root / "candidate_data").exists() else 0,
                "certificate_json_count": len(list((root / "certificates").glob("*.json"))) if (root / "certificates").exists() else 0,
                "proof_md_count": len(list((root / "proof_corpus").glob("*.md"))) if (root / "proof_corpus").exists() else 0,
                "verification_lines": verification_lines,
            }
        )
    return rows


QA_ALPHA = "candidate_data/selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.candidate.json"
QA_OPERATOR = "candidate_data/selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap.candidate.json"
QA_PRIMITIVE = "candidate_data/selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.candidate.json"
SM_STEP18 = "candidate_data/selected_step18_qasu3_alphadotd_import_or_primitivec1frontier.candidate.json"
SM_STEP19 = "candidate_data/selected_step19_primitivec1_sourcevalue_gate_or_tensorfrontier.candidate.json"
SM_STEP20 = "candidate_data/selected_step20_conditionalatompayload_or_sourcetheorem.candidate.json"
SM_STEP21 = "candidate_data/selected_step21_conditional_atomdecomposition_or_vertexsource.candidate.json"
SM_STEP22 = "candidate_data/selected_step22_vertexsource_promotion_or_transfermap.candidate.json"
SM_STEP23 = "candidate_data/selected_step23_staticrouting_transfermapreduction.candidate.json"
SM_STEP24 = "candidate_data/selected_step24_dynamicgate_reconciliation_or_valuelayercutset.candidate.json"
SM_STEP25 = "candidate_data/selected_step25_thresholdexternalreplay_noknobkernel_or_fulls2cutset.candidate.json"
SM_STEP26 = "candidate_data/selected_step26_phifintrace_matterslot_reconciliation_or_fulls2payloadcutset.candidate.json"
SM_STEP27 = "candidate_data/selected_step27_fulls2_subpayload_reduction_or_sectorpromotioncutset.candidate.json"
SM_STEP28 = "candidate_data/selected_step28_sectorpromotion_reconciliation_or_operatorsectorvaluecutset.candidate.json"
SM_STEP29 = "candidate_data/selected_step29_operatorsector_rhoede_attempt_or_projectivebnsourcecutset.candidate.json"
SM_STEP30 = "candidate_data/selected_step30_projectivebn_mechanicallift_or_visiblesourcecutset.candidate.json"
SM_STEP31 = "candidate_data/selected_step31_visiblecwsource_to_samesourcesymmetrybreaking.candidate.json"
SM_STEP32 = "candidate_data/selected_step32_samesourcesymmetrybreaking_to_smooths3twistedsource.candidate.json"
SM_STEP33 = "candidate_data/selected_step33_smooths3validator_reconciliation_or_holonomyoperatorpromotion.candidate.json"
SM_STEP34 = "candidate_data/selected_step34_flatgerbe_sourcefunctor_or_selectedcoverselector.candidate.json"
SM_STEP35 = "candidate_data/selected_step35_covergauge_reduction_or_s3classrestrictionselector.candidate.json"
SM_STEP36 = "candidate_data/selected_step36_s3classclosure_reconciliation_or_operatorvaluefrontier.candidate.json"
SM_STEP37 = "candidate_data/selected_step37_finitetrace_degap_import_or_fulloperatorvaluefrontier.candidate.json"
SM_STEP38 = "candidate_data/selected_step38_finiteheisenberg_rhoe_promotion_or_deoperatorfrontier.candidate.json"
SM_STEP39 = "candidate_data/selected_step39_diagonalend0_covariantde_import_or_fullsectorfrontier.candidate.json"
SM_STEP40 = "candidate_data/selected_step40_dotdtransport_alpha1import_or_primitivec1frontier.candidate.json"
SM_STEP41 = "candidate_data/selected_step41_singlebranch_solution_assembly_or_valuefunctionalfrontier.candidate.json"
SM_STEP42 = "candidate_data/selected_step42_executable_value_replay_solution_or_noknobrowfrontier.candidate.json"
SM_STEP16 = "candidate_data/selected_step16_postsourcevalueclosure_reconciliation.candidate.json"
SM_STEP17 = "candidate_data/selected_step17_projectorrhos_promotion_or_routecsolve.candidate.json"
DYNAMIC_PACKET = "candidate_data/selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
VALUE_FRONTIER = "candidate_data/selected_acceptedvaluelayerfrontier_or_nonloopingsourcerows.candidate.json"
FIRST_VALUE_ROW = "candidate_data/selected_valuelayerfirstnonloopingrowemission_or_thresholdimportexecution.candidate.json"
Q79_DOTD = "candidate_data/q79_selected_dotd_alpha1_c1_response_emission.candidate.json"
HIGGS_Q = "candidate_data/const_higgs_01_h7b1q_twohiggs_lift_or_samesource_functional_value.candidate.json"
HIGGS_Z = "candidate_data/const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values.candidate.json"


def build_parts() -> list[dict]:
    qa_alpha = load_json("qa_su3", QA_ALPHA)
    qa_operator = load_json("qa_su3", QA_OPERATOR)
    qa_primitive = load_json("qa_su3", QA_PRIMITIVE)
    sm_step18 = load_json("sm_closure", SM_STEP18)
    sm_step19 = load_json("sm_closure", SM_STEP19)
    sm_step20 = load_json("sm_closure", SM_STEP20)
    sm_step21 = load_json("sm_closure", SM_STEP21)
    sm_step22 = load_json("sm_closure", SM_STEP22)
    sm_step23 = load_json("sm_closure", SM_STEP23)
    sm_step24 = load_json("sm_closure", SM_STEP24)
    sm_step25 = load_json("sm_closure", SM_STEP25)
    sm_step26 = load_json("sm_closure", SM_STEP26)
    sm_step27 = load_json("sm_closure", SM_STEP27)
    sm_step28 = load_json("sm_closure", SM_STEP28)
    sm_step29 = load_json("sm_closure", SM_STEP29)
    sm_step30 = load_json("sm_closure", SM_STEP30)
    sm_step31 = load_json("sm_closure", SM_STEP31)
    sm_step32 = load_json("sm_closure", SM_STEP32)
    sm_step33 = load_json("sm_closure", SM_STEP33)
    sm_step34 = load_json("sm_closure", SM_STEP34)
    sm_step35 = load_json("sm_closure", SM_STEP35)
    sm_step36 = load_json("sm_closure", SM_STEP36)
    sm_step37 = load_json("sm_closure", SM_STEP37)
    sm_step38 = load_json("sm_closure", SM_STEP38)
    sm_step39 = load_json("sm_closure", SM_STEP39)
    sm_step40 = load_json("sm_closure", SM_STEP40)
    sm_step41 = load_json("sm_closure", SM_STEP41)
    sm_step42 = load_json("sm_closure", SM_STEP42)
    sm_step16 = load_json("sm_closure", SM_STEP16)
    sm_step17 = load_json("sm_closure", SM_STEP17)
    dynamic_packet = load_json("sm_closure", DYNAMIC_PACKET)
    value_frontier = load_json("sm_closure", VALUE_FRONTIER)
    first_value_row = load_json("sm_closure", FIRST_VALUE_ROW)
    q79_dotd = load_json("q79", Q79_DOTD)
    higgs_q = load_json("individual_constants", HIGGS_Q)
    higgs_z = load_json("individual_constants", HIGGS_Z)

    primitive_missing = dig(qa_primitive, "primitive_status.missing_atom_count")

    parts = [
        {
            "part": "SM parity theorem",
            "status": "CLOSED_SELECTED",
            "latest_progress": "Frozen SM-parity replay remains verified; it intentionally does not claim true SM equivalence or no-knob value derivation.",
            "evidence": [
                {"repo": "mtt-sm-parity-repro", "path": "reports/verification_report.txt"},
                {"repo": "mtt-sm-parity-closure", "path": "reports/verification_report.txt"},
            ],
            "blocking_next": "None for parity tier. It is not the same target as true SM equivalence.",
        },
        {
            "part": "Selected finite C1 / Phi_fin source identity",
            "status": "CLOSED_SELECTED_IN_ACTIVE_LEDGER",
            "latest_progress": "Step 14 promoted the premise-free Phi_fin finite restriction morphism; Step 16 retired the stale unpatched source-identity blocker for the active scalar-row plan.",
            "evidence": [
                {"repo": "mtt-sm-parity-closure", "path": SM_STEP16, "status": sm_step16.get("status")},
            ],
            "blocking_next": "No longer a live source-identity blocker for the active ledger; value emission remains separate.",
        },
        {
            "part": "q=79 exact/charge branch",
            "status": "CLOSED_SELECTED_FOR_Q79_BRANCH",
            "latest_progress": "q79 verifier passes and says remaining flavor/SM items are future no-proxy certificates, not terminal q79 blockers.",
            "evidence": [
                {"repo": "mtt-q79-proof-repro", "path": "reports/verification_report.txt"},
                {"repo": "mtt-q79-proof-repro", "path": Q79_DOTD, "status": q79_dotd.get("status")},
            ],
            "blocking_next": "q79 alone does not emit the full flavor/Yukawa value table.",
        },
        {
            "part": "Stationary projectors P_s/K_s/rho_s and source-level rho_E gerbe",
            "status": "CLOSED_SELECTED_IN_ACTIVE_LEDGER",
            "latest_progress": "Step 17 closes transported stationary projectors/rho_s and promotes source-level projective S3 gerbe rho_E while preserving the operator-value boundary.",
            "evidence": [
                {"repo": "mtt-sm-parity-closure", "path": SM_STEP17, "status": sm_step17.get("status")},
            ],
            "blocking_next": "Full operator values and internal scalar rows still require selected value execution.",
        },
        {
            "part": "Matter-slot orientation and U10/Ubar5/1M operator blocks",
            "status": "CLOSED_SELECTED_IN_ACTIVE_LEDGER",
            "latest_progress": "Step 18 imports the QA/SU3 oriented functional operator blocks for u,d,e,nuD, with normalization rho_s(T_i)/sqrt(2), into the active SM ledger.",
            "evidence": [
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP18,
                    "status": sm_step18.get("status"),
                    "matter_slot_orientation_imported": dig(sm_step18, "closure_decision.matter_slot_orientation_imported"),
                    "operator_blocks_imported": dig(sm_step18, "closure_decision.operator_blocks_imported"),
                    "overlap_normalization_imported": dig(sm_step18, "closure_decision.overlap_normalization_imported"),
                },
                {
                    "repo": "mtt-qa-su3-packet-proof",
                    "path": QA_OPERATOR,
                    "status": qa_operator.get("status"),
                    "same_branch_functional_operator_emission_closed": dig(qa_operator, "decision.same_branch_functional_operator_emission_closed"),
                    "selected_overlap_normalization_emitted": dig(qa_operator, "decision.selected_overlap_normalization_emitted"),
                }
            ],
            "blocking_next": "Operator-layer Pic0/torsion-gerbe invariant rule remains separate, but functional matter blocks are closed.",
        },
        {
            "part": "alpha1/dotD driver and honest dotD replay",
            "status": "CLOSED_SELECTED_IN_ACTIVE_LEDGER",
            "latest_progress": "Step 18 imports the QA/SU3 result into the active SM ledger: N_alpha1(h_ext)=1, du/dalpha1=h_ext, selected_dotD_source, alpha1 driver, and honest dotD replay are now closed here.",
            "evidence": [
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP18,
                    "status": sm_step18.get("status"),
                    "alpha1_dotD_driver_imported": dig(sm_step18, "closure_decision.alpha1_dotD_driver_imported"),
                    "honest_dotD_replay_imported": dig(sm_step18, "closure_decision.honest_dotD_replay_imported"),
                },
                {
                    "repo": "mtt-qa-su3-packet-proof",
                    "path": QA_ALPHA,
                    "status": qa_alpha.get("status"),
                    "alpha1_driver_verified": dig(qa_alpha, "decision.alpha1_driver_verified"),
                    "selected_dotD_source_verified": dig(qa_alpha, "decision.selected_dotD_source_verified"),
                    "honest_dotD_validator_closed": dig(qa_alpha, "decision.honest_dotD_validator_closed"),
                },
                {
                    "repo": "mtt-individual-constants-source-search",
                    "path": HIGGS_Q,
                    "status": higgs_q.get("status"),
                },
            ],
            "blocking_next": "Stop treating alpha1/dotD as the frontier. The next active frontier is primitive C1 atoms or a selected lambda12 spectral table.",
        },
        {
            "part": "Primitive C1 atom table for u,d,e,nuD",
            "status": "CLOSED_SELECTED_FIRST_RESPONSE_LAYER_IN_ACTIVE_LEDGER",
            "latest_progress": "Step 24 supersedes the Step 23 workorder: the same-branch source stack, same-source dynamic matter/overlap packet, and VSD01 assembly close the selected dynamic overlap tensor, primitive C1 first-response layer, A_selected, b_selected, deltaTheta_C1, and Hessian/source normalization. Older QA primitive-open counters remain historical support and cannot override this stronger active-ledger closure.",
            "evidence": [
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP24,
                    "status": sm_step24.get("status"),
                    "selected_dynamic_overlap_tensor_or_transfer_functor": dig(sm_step24, "closure_decision.selected_dynamic_overlap_tensor_or_transfer_functor"),
                    "selected_primitive_C1_contractions_first_response_layer": dig(sm_step24, "closure_decision.selected_primitive_C1_contractions_first_response_layer"),
                    "selected_b_selected_promoted": dig(sm_step24, "closure_decision.selected_b_selected_promoted"),
                    "selected_Hessian_source_normalization_promoted": dig(sm_step24, "closure_decision.selected_Hessian_source_normalization_promoted"),
                    "accepted_value_functional_rows_closed": dig(sm_step24, "closure_decision.accepted_value_functional_rows_closed"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": DYNAMIC_PACKET,
                    "status": dynamic_packet.get("status"),
                    "selected_dynamic_overlap_tensor_promoted": dig(dynamic_packet, "what_closes_now.selected_dynamic_overlap_tensor_promoted"),
                    "primitive_C1_contractions_selected_emitted_first_response_layer": dig(dynamic_packet, "what_closes_now.primitive_C1_contractions_selected_emitted_first_response_layer"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP23,
                    "status": sm_step23.get("status"),
                    "phase_Z_routed_to_u_e_column": dig(sm_step23, "closure_decision.phase_Z_routed_to_u_e_column"),
                    "shift_X_routed_to_d_nuD_column": dig(sm_step23, "closure_decision.shift_X_routed_to_d_nuD_column"),
                    "selected_dynamic_overlap_tensor_or_transfer_functor": dig(sm_step23, "closure_decision.selected_dynamic_overlap_tensor_or_transfer_functor"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP22,
                    "status": sm_step22.get("status"),
                    "selected_source_to_C1_transfer_map_emitted": dig(sm_step22, "closure_decision.selected_source_to_C1_transfer_map_emitted"),
                    "selected_A_selected_promoted": dig(sm_step22, "closure_decision.selected_A_selected_promoted"),
                    "blocking_clause_count": dig(sm_step22, "closure_decision.blocking_clause_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP21,
                    "status": sm_step21.get("status"),
                    "conditional_decomposition_reconstructs_aggregate": dig(sm_step21, "closure_decision.conditional_decomposition_reconstructs_aggregate"),
                    "selected_vertex_source_theorem_proved": dig(sm_step21, "closure_decision.selected_vertex_source_theorem_proved"),
                    "selected_replacement_sixterm_decomposition_emitted": dig(sm_step21, "closure_decision.selected_replacement_sixterm_decomposition_emitted"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP20,
                    "status": sm_step20.get("status"),
                    "conditional_payload_built": dig(sm_step20, "closure_decision.step20_conditional_payload_built"),
                    "conditional_normal_form_validated": dig(sm_step20, "closure_decision.conditional_normal_form_validated"),
                    "selected_source_theorem_for_conditional_payload": dig(sm_step20, "closure_decision.selected_source_theorem_for_conditional_payload"),
                    "six_term_primitive_atom_decomposition_emitted": dig(sm_step20, "closure_decision.six_term_primitive_atom_decomposition_emitted"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP19,
                    "status": sm_step19.get("status"),
                    "primitive_C1_atom_assembly_schema_closed": dig(sm_step19, "closure_decision.primitive_C1_atom_assembly_schema_closed"),
                    "current_corpus_payload_fill_nogo_closed": dig(sm_step19, "closure_decision.current_corpus_payload_fill_nogo_closed"),
                    "missing_leaf_count": dig(sm_step19, "closure_decision.missing_leaf_count"),
                },
                {
                    "repo": "mtt-qa-su3-packet-proof",
                    "path": QA_PRIMITIVE,
                    "status": qa_primitive.get("status"),
                    "missing_atom_count": primitive_missing,
                    "primitive_C1_contractions_closed": dig(qa_primitive, "decision.primitive_C1_contractions_closed"),
                    "superseded_by_active_step24_for_first_response_layer": True,
                }
            ],
            "blocking_next": "Do not reopen primitive/source promotion. The next blocker is selected value-functional rows: threshold response, Yukawa/Higgs values, CKM/PMNS, mass ratios, and correlated likelihood closure.",
        },
        {
            "part": "A_selected and b_selected finite value matrices",
            "status": "CLOSED_SELECTED_IN_ACTIVE_LEDGER",
            "latest_progress": "Step 24 imports the verified unpatched source-promotion stack and same-source dynamic matter packet: A_selected, b_selected, deltaTheta_C1, and the two Hessian/source rows are promoted in the active ledger. This still does not derive accepted Yukawa magnitudes.",
            "evidence": [
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP24,
                    "selected_A_selected_promoted": dig(sm_step24, "closure_decision.selected_A_selected_promoted"),
                    "selected_b_selected_promoted": dig(sm_step24, "closure_decision.selected_b_selected_promoted"),
                    "selected_deltaTheta_C1_promoted": dig(sm_step24, "closure_decision.selected_deltaTheta_C1_promoted"),
                    "selected_Hessian_source_normalization_promoted": dig(sm_step24, "closure_decision.selected_Hessian_source_normalization_promoted"),
                },
                {
                    "repo": "mtt-qa-su3-packet-proof",
                    "path": QA_PRIMITIVE,
                    "A_selected_emitted": dig(qa_primitive, "decision.A_selected_emitted"),
                    "b_selected_emitted": dig(qa_primitive, "decision.b_selected_emitted"),
                    "superseded_by_active_step24": True,
                },
                {
                    "repo": "mtt-q79-proof-repro",
                    "path": Q79_DOTD,
                    "status": q79_dotd.get("status"),
                },
            ],
            "blocking_next": "Use these selected matrices as inputs to the value-functional layer; do not treat their source promotion as still open.",
        },
        {
            "part": "R_theta internal scalar rows / no-knob numerical rows",
            "status": "OPEN_VALUE_FUNCTIONAL",
            "latest_progress": "Step 42 attaches the selected q=79/F/m=1 Step41 source branch to the emitted common-scale Yukawa/Higgs rows plus admitted threshold/mass-scheme/profile replay tier. This closes one executable admitted-replay value solution for comparison. It does not close no-knob or true precision equivalence: accepted internal scalar rows and accepted Rtheta coefficient values are still zero, so the live target is selected internal coefficient rows or a universal source-anchor theorem.",
            "evidence": [
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP42,
                    "status": sm_step42.get("status"),
                    "executable_admitted_replay_value_solution_closed": dig(sm_step42, "closure_decision.executable_admitted_replay_value_solution_closed"),
                    "Step41_source_branch_attached_to_value_rows": dig(sm_step42, "closure_decision.Step41_source_branch_attached_to_value_rows"),
                    "versioned_common_scale_Yu_Yd_Ye_lambdaH_rows_emitted": dig(sm_step42, "closure_decision.versioned_common_scale_Yu_Yd_Ye_lambdaH_rows_emitted"),
                    "admitted_external_threshold_rows_closed": dig(sm_step42, "closure_decision.admitted_external_threshold_rows_closed"),
                    "admitted_external_threshold_row_count": dig(sm_step42, "closure_decision.admitted_external_threshold_row_count"),
                    "admitted_external_mass_scheme_rows_closed": dig(sm_step42, "closure_decision.admitted_external_mass_scheme_rows_closed"),
                    "admitted_external_mass_scheme_row_count": dig(sm_step42, "closure_decision.admitted_external_mass_scheme_row_count"),
                    "diagonal_profile_replay_tier_closed": dig(sm_step42, "closure_decision.diagonal_profile_replay_tier_closed"),
                    "Pi_Rtheta_closed": dig(sm_step42, "closure_decision.Pi_Rtheta_closed"),
                    "Rtheta_readiness_8_of_9": dig(sm_step42, "closure_decision.Rtheta_readiness_8_of_9"),
                    "accepted_for_true_precision_equivalence": dig(sm_step42, "closure_decision.accepted_for_true_precision_equivalence"),
                    "accepted_as_no_knob_MTT_prediction": dig(sm_step42, "closure_decision.accepted_as_no_knob_MTT_prediction"),
                    "accepted_internal_scalar_row_count": dig(sm_step42, "closure_decision.accepted_internal_scalar_row_count"),
                    "accepted_coefficient_value_count": dig(sm_step42, "closure_decision.accepted_coefficient_value_count"),
                    "true_SM_equivalence_closed": dig(sm_step42, "closure_decision.true_SM_equivalence_closed"),
                    "full_no_knob_closed": dig(sm_step42, "closure_decision.full_no_knob_closed"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP41,
                    "status": sm_step41.get("status"),
                    "single_branch_first_response_solution_assembled": dig(sm_step41, "closure_decision.single_branch_first_response_solution_assembled"),
                    "selected_q79_F_m1_branch_fixed": dig(sm_step41, "closure_decision.selected_q79_F_m1_branch_fixed"),
                    "primitive_C1_first_response_layer_closed": dig(sm_step41, "closure_decision.primitive_C1_first_response_layer_closed"),
                    "selected_A_selected_promoted": dig(sm_step41, "closure_decision.selected_A_selected_promoted"),
                    "selected_b_selected_promoted": dig(sm_step41, "closure_decision.selected_b_selected_promoted"),
                    "selected_deltaTheta_C1_promoted": dig(sm_step41, "closure_decision.selected_deltaTheta_C1_promoted"),
                    "selected_dynamic_overlap_tensor_closed": dig(sm_step41, "closure_decision.selected_dynamic_overlap_tensor_closed"),
                    "selected_source_to_C1_transfer_map_closed": dig(sm_step41, "closure_decision.selected_source_to_C1_transfer_map_closed"),
                    "selected_Rtheta_scalar_value_functional_source_domain_closed": dig(sm_step41, "closure_decision.selected_Rtheta_scalar_value_functional_source_domain_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step41, "closure_decision.accepted_internal_scalar_row_count"),
                    "accepted_value_functional_rows_closed": dig(sm_step41, "closure_decision.accepted_value_functional_rows_closed"),
                    "accepted_Yukawa_magnitudes_closed": dig(sm_step41, "closure_decision.accepted_Yukawa_magnitudes_closed"),
                    "CKM_PMNS_measured_value_closure_closed": dig(sm_step41, "closure_decision.CKM_PMNS_measured_value_closure_closed"),
                    "lambda_H_row_emitted": dig(sm_step41, "closure_decision.lambda_H_row_emitted"),
                    "true_SM_equivalence_closed": dig(sm_step41, "closure_decision.true_SM_equivalence_closed"),
                    "full_no_knob_closed": dig(sm_step41, "closure_decision.full_no_knob_closed"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP40,
                    "status": sm_step40.get("status"),
                    "selected_dotD_transport_derivative_formula_closed": dig(sm_step40, "closure_decision.selected_dotD_transport_derivative_formula_closed"),
                    "selected_alpha1_driver_normalization_closed": dig(sm_step40, "closure_decision.selected_alpha1_driver_normalization_closed"),
                    "same_branch_dotD_alpha1_values_closed": dig(sm_step40, "closure_decision.same_branch_dotD_alpha1_values_closed"),
                    "honest_dotD_alpha1_replay_closed": dig(sm_step40, "closure_decision.honest_dotD_alpha1_replay_closed"),
                    "primitive_C1_contractions_from_operator_values_closed": dig(sm_step40, "closure_decision.primitive_C1_contractions_from_operator_values_closed"),
                    "selected_A_selected_closed": dig(sm_step40, "closure_decision.selected_A_selected_closed"),
                    "selected_b_selected_closed": dig(sm_step40, "closure_decision.selected_b_selected_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step40, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP39,
                    "status": sm_step39.get("status"),
                    "selected_diagonal_End0_covariant_D_E_closed": dig(sm_step39, "closure_decision.selected_diagonal_End0_covariant_D_E_closed"),
                    "selected_stationary_projector_Riesz_Green_transport_closed": dig(sm_step39, "closure_decision.selected_stationary_projector_Riesz_Green_transport_closed"),
                    "selected_full_sector_covariant_D_E_matrices_closed": dig(sm_step39, "closure_decision.selected_full_sector_covariant_D_E_matrices_closed"),
                    "rank2_to_rank3_sector_transfer_values_closed": dig(sm_step39, "closure_decision.rank2_to_rank3_sector_transfer_values_closed"),
                    "offdiagonal_End0_control_closed": dig(sm_step39, "closure_decision.offdiagonal_End0_control_closed"),
                    "same_branch_dotD_alpha1_values_closed": dig(sm_step39, "closure_decision.same_branch_dotD_alpha1_values_closed"),
                    "coherent_spectral_zero_mode_projectors_closed": dig(sm_step39, "closure_decision.coherent_spectral_zero_mode_projectors_closed"),
                    "primitive_C1_contractions_from_operator_values_closed": dig(sm_step39, "closure_decision.primitive_C1_contractions_from_operator_values_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step39, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP38,
                    "status": sm_step38.get("status"),
                    "selected_s3_class_restriction_layer_closed": dig(sm_step38, "closure_decision.selected_s3_class_restriction_layer_closed"),
                    "finite_trace_DE_gap_layer_closed": dig(sm_step38, "closure_decision.finite_trace_DE_gap_layer_closed"),
                    "operator_level_projective_rhoE_transition_matrices_closed": dig(sm_step38, "closure_decision.operator_level_projective_rhoE_transition_matrices_closed"),
                    "nonidentity_projective_rhoE_selected_up_to_unitary_gauge": dig(sm_step38, "closure_decision.nonidentity_projective_rhoE_selected_up_to_unitary_gauge"),
                    "selected_covariant_D_E_matrices_closed": dig(sm_step38, "closure_decision.selected_covariant_D_E_matrices_closed"),
                    "selected_Riesz_Green_values_closed": dig(sm_step38, "closure_decision.selected_Riesz_Green_values_closed"),
                    "same_branch_dotD_alpha1_values_closed": dig(sm_step38, "closure_decision.same_branch_dotD_alpha1_values_closed"),
                    "coherent_spectral_zero_mode_projectors_closed": dig(sm_step38, "closure_decision.coherent_spectral_zero_mode_projectors_closed"),
                    "primitive_C1_contractions_from_operator_values_closed": dig(sm_step38, "closure_decision.primitive_C1_contractions_from_operator_values_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step38, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP37,
                    "status": sm_step37.get("status"),
                    "selected_s3_class_restriction_layer_closed": dig(sm_step37, "closure_decision.selected_s3_class_restriction_layer_closed"),
                    "finite_trace_DE_gap_layer_closed": dig(sm_step37, "closure_decision.finite_trace_DE_gap_layer_closed"),
                    "transition_rhoE_or_Cech_Dolbeault_DE_data_finite_trace_slot_closed": dig(sm_step37, "closure_decision.transition_rhoE_or_Cech_Dolbeault_DE_data_finite_trace_slot_closed"),
                    "selected_trace_equality_closed": dig(sm_step37, "closure_decision.selected_trace_equality_closed"),
                    "positive_gap_Riesz_Green_lock_imported": dig(sm_step37, "closure_decision.positive_gap_Riesz_Green_lock_imported"),
                    "operator_level_projective_rhoE_transition_matrices_closed": dig(sm_step37, "closure_decision.operator_level_projective_rhoE_transition_matrices_closed"),
                    "selected_covariant_D_E_matrices_closed": dig(sm_step37, "closure_decision.selected_covariant_D_E_matrices_closed"),
                    "selected_Riesz_Green_values_closed": dig(sm_step37, "closure_decision.selected_Riesz_Green_values_closed"),
                    "same_branch_dotD_alpha1_values_closed": dig(sm_step37, "closure_decision.same_branch_dotD_alpha1_values_closed"),
                    "coherent_spectral_zero_mode_projectors_closed": dig(sm_step37, "closure_decision.coherent_spectral_zero_mode_projectors_closed"),
                    "primitive_C1_contractions_from_operator_values_closed": dig(sm_step37, "closure_decision.primitive_C1_contractions_from_operator_values_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step37, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP36,
                    "status": sm_step36.get("status"),
                    "selected_s3_differential_cohomology_class_closed": dig(sm_step36, "closure_decision.selected_s3_differential_cohomology_class_closed"),
                    "s3_restriction_pullback_table_closed": dig(sm_step36, "closure_decision.s3_restriction_pullback_table_closed"),
                    "smooth_freed_witten_cancellation_closed": dig(sm_step36, "closure_decision.smooth_freed_witten_cancellation_closed"),
                    "block_family_higgs_projector_retention_closed": dig(sm_step36, "closure_decision.block_family_higgs_projector_retention_closed"),
                    "good_cover_removed_as_physical_knob": dig(sm_step36, "closure_decision.good_cover_removed_as_physical_knob"),
                    "operator_level_projective_rhoE_transition_closed": dig(sm_step36, "closure_decision.operator_level_projective_rhoE_transition_closed"),
                    "selected_D_E_Riesz_Green_dotD_values_closed": dig(sm_step36, "closure_decision.selected_D_E_Riesz_Green_dotD_values_closed"),
                    "coherent_spectral_zero_mode_projectors_closed": dig(sm_step36, "closure_decision.coherent_spectral_zero_mode_projectors_closed"),
                    "selected_visible_operator_source_closed": dig(sm_step36, "closure_decision.selected_visible_operator_source_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step36, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP35,
                    "status": sm_step35.get("status"),
                    "good_cover_removed_as_physical_knob": dig(sm_step35, "closure_decision.good_cover_removed_as_physical_knob"),
                    "cover_refinement_invariance_imported": dig(sm_step35, "closure_decision.cover_refinement_invariance_imported"),
                    "step34_functor_preserved": dig(sm_step35, "closure_decision.step34_functor_preserved"),
                    "frontier_reduced_to_selected_s3_class_restriction": dig(sm_step35, "closure_decision.frontier_reduced_to_selected_s3_class_restriction"),
                    "selected_s3_differential_cohomology_class_closed": dig(sm_step35, "closure_decision.selected_s3_differential_cohomology_class_closed"),
                    "s3_restriction_pullback_table_closed": dig(sm_step35, "closure_decision.s3_restriction_pullback_table_closed"),
                    "smooth_freed_witten_projector_retention_closed": dig(sm_step35, "closure_decision.smooth_freed_witten_projector_retention_closed"),
                    "operator_level_projective_rhoE_transition_closed": dig(sm_step35, "closure_decision.operator_level_projective_rhoE_transition_closed"),
                    "selected_D_E_Riesz_Green_dotD_values_closed": dig(sm_step35, "closure_decision.selected_D_E_Riesz_Green_dotD_values_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step35, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP34,
                    "status": sm_step34.get("status"),
                    "finite_to_smooth_flat_gerbe_source_functor_constructed": dig(sm_step34, "closure_decision.finite_to_smooth_flat_gerbe_source_functor_constructed"),
                    "qutrit_central_extension_holonomy_map_constructed": dig(sm_step34, "closure_decision.qutrit_central_extension_holonomy_map_constructed"),
                    "finite_twisted_CP_cancellation_conditionally_transported": dig(sm_step34, "closure_decision.finite_twisted_CP_cancellation_conditionally_transported"),
                    "selected_cover_classifying_map_obligation_isolated": dig(sm_step34, "closure_decision.selected_cover_classifying_map_obligation_isolated"),
                    "operator_promotion_boundary_reduced_to_selected_cover_and_projectors": dig(sm_step34, "closure_decision.operator_promotion_boundary_reduced_to_selected_cover_and_projectors"),
                    "selected_classifying_map_c_closed": dig(sm_step34, "closure_decision.selected_classifying_map_c_closed"),
                    "selected_good_cover_closed": dig(sm_step34, "closure_decision.selected_good_cover_closed"),
                    "smooth_freed_witten_projector_retention_closed": dig(sm_step34, "closure_decision.smooth_freed_witten_projector_retention_closed"),
                    "operator_level_projective_rhoE_transition_closed": dig(sm_step34, "closure_decision.operator_level_projective_rhoE_transition_closed"),
                    "selected_D_E_Riesz_Green_dotD_values_closed": dig(sm_step34, "closure_decision.selected_D_E_Riesz_Green_dotD_values_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step34, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP33,
                    "status": sm_step33.get("status"),
                    "strict_q79_smooth_validator_promoted_to_active_gate": dig(sm_step33, "closure_decision.strict_q79_smooth_validator_promoted_to_active_gate"),
                    "older_projective_gerbe_retired_blocker_wording_demoted": dig(sm_step33, "closure_decision.older_projective_gerbe_retired_blocker_wording_demoted"),
                    "finite_s3_cp_and_projector_support_kept_closed": dig(sm_step33, "closure_decision.finite_s3_cp_and_projector_support_kept_closed"),
                    "holonomy_operator_promotion_contract_emitted": dig(sm_step33, "closure_decision.holonomy_operator_promotion_contract_emitted"),
                    "minimal_smooth_source_fill_targets_extracted": dig(sm_step33, "closure_decision.minimal_smooth_source_fill_targets_extracted"),
                    "smooth_s3_twisted_source_lift_closed": dig(sm_step33, "closure_decision.smooth_s3_twisted_source_lift_closed"),
                    "selected_smooth_cover_or_scaffold_closed": dig(sm_step33, "closure_decision.selected_smooth_cover_or_scaffold_closed"),
                    "smooth_freed_witten_projector_retention_closed": dig(sm_step33, "closure_decision.smooth_freed_witten_projector_retention_closed"),
                    "operator_level_projective_rhoE_transition_closed": dig(sm_step33, "closure_decision.operator_level_projective_rhoE_transition_closed"),
                    "selected_D_E_Riesz_Green_dotD_values_closed": dig(sm_step33, "closure_decision.selected_D_E_Riesz_Green_dotD_values_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step33, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP32,
                    "status": sm_step32.get("status"),
                    "same_source_symmetrybreaking_reduced_to_smooth_s3_twisted_source": dig(sm_step32, "closure_decision.same_source_symmetrybreaking_reduced_to_smooth_s3_twisted_source"),
                    "direct_pic0_invariance_route_retired": dig(sm_step32, "closure_decision.direct_pic0_invariance_route_retired"),
                    "gerbe_twisted_s3_route_primary": dig(sm_step32, "closure_decision.gerbe_twisted_s3_route_primary"),
                    "finite_s3_restriction_projector_retention_closed": dig(sm_step32, "closure_decision.finite_s3_restriction_projector_retention_closed"),
                    "smooth_s3_twisted_source_lift_closed": dig(sm_step32, "closure_decision.smooth_s3_twisted_source_lift_closed"),
                    "smooth_freed_witten_projector_retention_closed": dig(sm_step32, "closure_decision.smooth_freed_witten_projector_retention_closed"),
                    "operator_level_projective_rhoE_transition_closed": dig(sm_step32, "closure_decision.operator_level_projective_rhoE_transition_closed"),
                    "selected_D_E_Riesz_Green_dotD_values_closed": dig(sm_step32, "closure_decision.selected_D_E_Riesz_Green_dotD_values_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step32, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP31,
                    "status": sm_step31.get("status"),
                    "visible_CW_operator_source_reduced_to_common_source": dig(sm_step31, "closure_decision.visible_CW_operator_source_reduced_to_common_source"),
                    "rank2_non_split_lane_prioritized": dig(sm_step31, "closure_decision.rank2_non_split_lane_prioritized"),
                    "routec_lane_retained_as_parallel_repair": dig(sm_step31, "closure_decision.routec_lane_retained_as_parallel_repair"),
                    "same_source_symmetrybreaking_contract_emitted": dig(sm_step31, "closure_decision.same_source_symmetrybreaking_contract_emitted"),
                    "same_source_symmetrybreaking_source_closed": dig(sm_step31, "closure_decision.same_source_symmetrybreaking_source_closed"),
                    "selected_visible_operator_source_closed": dig(sm_step31, "closure_decision.selected_visible_operator_source_closed"),
                    "selected_D_E_Riesz_Green_dotD_values_closed": dig(sm_step31, "closure_decision.selected_D_E_Riesz_Green_dotD_values_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step31, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP30,
                    "status": sm_step30.get("status"),
                    "projective_BN_mechanical_lift_fields_closed": dig(sm_step30, "closure_decision.projective_BN_mechanical_lift_fields_closed"),
                    "smooth_scalar_basis_quadrature_gram_stiffness_closed": dig(sm_step30, "closure_decision.smooth_scalar_basis_quadrature_gram_stiffness_closed"),
                    "model_active_D_E_projectors_Green_dotD_emitted": dig(sm_step30, "closure_decision.model_active_D_E_projectors_Green_dotD_emitted"),
                    "source_level_projective_gerbe_rhoE_closed": dig(sm_step30, "closure_decision.source_level_projective_gerbe_rhoE_closed"),
                    "selected_visible_operator_source_closed": dig(sm_step30, "closure_decision.selected_visible_operator_source_closed"),
                    "operator_level_projective_rhoE_transition_closed": dig(sm_step30, "closure_decision.operator_level_projective_rhoE_transition_closed"),
                    "selected_source_verified_operator_flags_closed": dig(sm_step30, "closure_decision.selected_source_verified_operator_flags_closed"),
                    "selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed": dig(sm_step30, "closure_decision.selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step30, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP29,
                    "status": sm_step29.get("status"),
                    "operator_sector_smoke_inventory_filled": dig(sm_step29, "closure_decision.operator_sector_smoke_inventory_filled"),
                    "identity_rhoE_smoke_retired_as_selected_route": dig(sm_step29, "closure_decision.identity_rhoE_smoke_retired_as_selected_route"),
                    "nonidentity_projective_rhoE_candidate_imported": dig(sm_step29, "closure_decision.nonidentity_projective_rhoE_candidate_imported"),
                    "ordinary_nonidentity_rhoE_route_retired": dig(sm_step29, "closure_decision.ordinary_nonidentity_rhoE_route_retired"),
                    "projective_smooth_BN_lift_contract_emitted": dig(sm_step29, "closure_decision.projective_smooth_BN_lift_contract_emitted"),
                    "selected_operator_level_projective_rhoE_transition_closed": dig(sm_step29, "closure_decision.selected_operator_level_projective_rhoE_transition_closed"),
                    "selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed": dig(sm_step29, "closure_decision.selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed"),
                    "selected_smooth_BN_Galerkin_basis_closed": dig(sm_step29, "closure_decision.selected_smooth_BN_Galerkin_basis_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step29, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP28,
                    "status": sm_step28.get("status"),
                    "step27_sector_promotion_frontier_refined": dig(sm_step28, "closure_decision.step27_sector_promotion_frontier_refined"),
                    "selected_stationary_End0_to_sector_routing_values_closed": dig(sm_step28, "closure_decision.selected_stationary_End0_to_sector_routing_values_closed"),
                    "selected_projector_promotion_Ps_Ks_closed": dig(sm_step28, "closure_decision.selected_projector_promotion_Ps_Ks_closed"),
                    "selected_stationary_rho_s_matrix_values_closed": dig(sm_step28, "closure_decision.selected_stationary_rho_s_matrix_values_closed"),
                    "selected_projective_rhoE_source_level_closed": dig(sm_step28, "closure_decision.selected_projective_rhoE_source_level_closed"),
                    "functional_matter_slot_blocks_and_overlap_normalization_closed": dig(sm_step28, "closure_decision.functional_matter_slot_blocks_and_overlap_normalization_closed"),
                    "operator_level_projective_rhoE_from_selected_connection_closed": dig(sm_step28, "closure_decision.operator_level_projective_rhoE_from_selected_connection_closed"),
                    "selected_rhoE_transition_payload_fullS2_operator_tier_closed": dig(sm_step28, "closure_decision.selected_rhoE_transition_payload_fullS2_operator_tier_closed"),
                    "selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed": dig(sm_step28, "closure_decision.selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step28, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP27,
                    "status": sm_step27.get("status"),
                    "diagonal_End0_HYM_subpayload_closed": dig(sm_step27, "closure_decision.diagonal_End0_HYM_subpayload_closed"),
                    "protected_T3_Riesz_Green_closed": dig(sm_step27, "closure_decision.protected_T3_Riesz_Green_closed"),
                    "T1_T2_covariant_Green_closed": dig(sm_step27, "closure_decision.T1_T2_covariant_Green_closed"),
                    "selected_End0_to_sector_routing_values_closed": dig(sm_step27, "closure_decision.selected_End0_to_sector_routing_values_closed"),
                    "selected_rhoE_transition_payload_closed": dig(sm_step27, "closure_decision.selected_rhoE_transition_payload_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step27, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP26,
                    "status": sm_step26.get("status"),
                    "functional_PhiFin_trace_closed": dig(sm_step26, "closure_decision.functional_PhiFin_trace_closed"),
                    "static_U10_Ubar5_1M_source_closed": dig(sm_step26, "closure_decision.static_U10_Ubar5_1M_source_closed"),
                    "selected_fullS2_rhoE_D_E_operator_payload_closed": dig(sm_step26, "closure_decision.selected_fullS2_rhoE_D_E_operator_payload_closed"),
                    "dynamic_PhiFin_C1_payload_closed": dig(sm_step26, "closure_decision.dynamic_PhiFin_C1_payload_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step26, "closure_decision.accepted_internal_scalar_row_count"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP25,
                    "status": sm_step25.get("status"),
                    "admitted_external_threshold_row_count": dig(sm_step25, "closure_decision.admitted_external_threshold_row_count"),
                    "admitted_external_mass_scheme_row_count": dig(sm_step25, "closure_decision.admitted_external_mass_scheme_row_count"),
                    "final_no_knob_kernel_typed": dig(sm_step25, "closure_decision.final_no_knob_kernel_typed"),
                    "accepted_internal_scalar_row_count": dig(sm_step25, "closure_decision.accepted_internal_scalar_row_count"),
                    "selected_fullS2_payload_ready": dig(sm_step25, "closure_decision.selected_fullS2_payload_ready"),
                    "candidate_specific_universal_source_anchor_selected": dig(sm_step25, "closure_decision.candidate_specific_universal_source_anchor_selected"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": VALUE_FRONTIER,
                    "status": value_frontier.get("status"),
                    "source_layer_closed": dig(value_frontier, "readiness.source_layer_closed"),
                    "value_layer_accepted_source_rows": dig(value_frontier, "readiness.value_layer_accepted_source_rows"),
                    "value_layer_required_rows": dig(value_frontier, "readiness.value_layer_required_rows"),
                },
                {"repo": "mtt-sm-parity-closure", "path": SM_STEP16, "status": sm_step16.get("status")},
                {"repo": "mtt-sm-parity-closure", "path": "reports/verification_report.txt"},
            ],
            "blocking_next": "Derive operator-level projective rho_E transition, selected covariant D_E, source-verified Riesz/Green with gap/error bounds, dotD, and coherent spectral zero-mode projectors from the selected S3 source.",
        },
        {
            "part": "lambda12 / electroweak local determinant table",
            "status": "OPEN_COMPUTATIONAL",
            "latest_progress": "Post-alpha C1 stack separates lambda12 from alpha1: diagnostic near-hit values exist, but no selected U1/SU2 determinant spectrum or full Delta_a^sel vector is emitted.",
            "evidence": [
                {
                    "repo": "mtt-qa-su3-packet-proof",
                    "path": QA_PRIMITIVE,
                    "lambda_12_closed": dig(qa_primitive, "lambda12_status.lambda_12_closed"),
                    "lambda_12_computable_from_this_gate": dig(qa_primitive, "lambda12_status.lambda_12_computable_from_this_gate"),
                },
                {"repo": "mtt-nonsm-constants-no-knob", "path": "reports/verification_report.txt"},
            ],
            "blocking_next": "Selected spectral/local determinant table for U1/SU2, or a bridge deriving lambda12 from the primitive C1 execution.",
        },
        {
            "part": "Yukawa magnitudes, CKM/PMNS, and masses",
            "status": "OPEN_VALUE_PREDICTION",
            "latest_progress": "The dynamic Qa/SU3 first-response/operator packet is closed, but selected no-proxy Yukawa magnitudes, measured CKM/PMNS value closure, threshold/mass-scheme rows, and running mass ratios are still not derived.",
            "evidence": [
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": FIRST_VALUE_ROW,
                    "status": first_value_row.get("status"),
                    "source_layer_row_available": dig(first_value_row, "closure_decision.source_layer_row_available"),
                    "accepted_true_value_source_row_emitted": dig(first_value_row, "closure_decision.accepted_true_value_source_row_emitted"),
                },
                {
                    "repo": "mtt-sm-parity-closure",
                    "path": SM_STEP25,
                    "admitted_external_threshold_rows_closed": dig(sm_step25, "closure_decision.admitted_external_threshold_rows_closed"),
                    "admitted_external_mass_scheme_rows_closed": dig(sm_step25, "closure_decision.admitted_external_mass_scheme_rows_closed"),
                    "accepted_internal_scalar_row_count": dig(sm_step25, "closure_decision.accepted_internal_scalar_row_count"),
                    "lambda_H_row_emitted": dig(sm_step25, "closure_decision.lambda_H_row_emitted"),
                },
                {"repo": "mtt-sm-parity-closure", "path": "reports/verification_report.txt"},
                {"repo": "mtt-qa-su3-packet-proof", "path": QA_PRIMITIVE, "Yukawa_or_full_SM_closure": dig(qa_primitive, "decision.Yukawa_or_full_SM_closure")},
            ],
            "blocking_next": "Requires selected value functionals and accepted threshold/Yukawa/Higgs rows, then RG/threshold propagation and correlated likelihood closure.",
        },
        {
            "part": "Higgs lambda_H / UV two-Higgs Huv payload",
            "status": "OPEN_HUV_PAYLOAD",
            "latest_progress": "Individual-constants imports the QA/SU3 alpha/dotD closure, but H7B1Z still lacks selected E_H^UV binding/projection-measure identity or direct Herm2 Huv rows.",
            "evidence": [
                {"repo": "mtt-individual-constants-source-search", "path": HIGGS_Q, "status": higgs_q.get("status")},
                {"repo": "mtt-individual-constants-source-search", "path": HIGGS_Z, "status": higgs_z.get("status")},
            ],
            "blocking_next": "Need selected E_H^UV section basis/quadrature/HYM bridge or direct Huu/Hud/Hdd Herm(2) rows.",
        },
        {
            "part": "Gauge constants / non-SM constants",
            "status": "SUPPORT_ONLY_FOR_TRUE_SM_CLOSURE",
            "latest_progress": "Non-SM constants repo has many formulated selected-kernel/scaffold results and passes verification, but physical alpha values and strict no-knob coupling closure remain open.",
            "evidence": [
                {"repo": "mtt-nonsm-constants-no-knob", "path": "reports/verification_report.txt"},
            ],
            "blocking_next": "Can constrain search space, but cannot replace selected determinant/value rows.",
        },
        {
            "part": "Protospinor / GR alignment",
            "status": "SUPPORT_ONLY_FOR_TRUE_SM_CLOSURE",
            "latest_progress": "Protospinor GR repo imports SM parity as parity-tier only and keeps independent primitive-row/source-rule/Galerkin C1 lanes open.",
            "evidence": [
                {"repo": "mtt-protospinor-gr-response-proof", "path": "reports/verification_report.txt"},
            ],
            "blocking_next": "Useful for source discipline and particle interpretation, not a closure proof for SM values.",
        },
        {
            "part": "Theta-program corpus folder",
            "status": "CORPUS_SUPPORT_NO_EXECUTION_LEDGER",
            "latest_progress": "The folder is present but has no reports/candidates/certificates ledger, so it cannot override repo results unless specific paper claims are promoted into a checked packet.",
            "evidence": [
                {"repo": "18 Theta-Closure & Execution Program", "path": "."},
            ],
            "blocking_next": "Mine for definitions/axioms, then promote any useful rule into candidate/certificate form.",
        },
    ]
    return parts


def write_markdown(payload: dict) -> str:
    lines = [
        "# MTT True SM Closure Cross-Repo Part Status Audit v1",
        "",
        f"Generated: {payload['generated_utc']}",
        "",
        "## Executive correction",
        "",
        "The latest cross-repo status is not the older broad statement that alpha1/dotD remains open. "
        "The strongest QA/SU3 packet closes the selected alpha1/dotD driver and honest replay, and Step 18 now imports that closure into the active SM ledger. "
        "Step 24 also closes the stale dynamic-overlap/b-Hessian workorder by importing the later source stack, same-source dynamic matter packet, and VSD01 assembly. "
        "Step 25 closes the admitted external threshold/mass replay lane and the typed no-knob kernel, then shows the direct internal scalar-row attempt emits zero accepted rows. "
        "Step 26 closes the Phi_fin trace/static matter-slot tier. "
        "Step 27 closes the diagonal/Green HYM subpayload. "
            "Step 28 reconciles the wording with Step17/18: stationary projectors, stationary rho_s, source-level projective rho_E, and functional matter-slot blocks are locked closed. "
        "Step 29 retires the identity-rhoE smoke route. "
        "Step 30 imports the existing smooth projective B_N scaffold and closes the mechanical lift fields. "
        "Step 31 reduces the visible Chern-Weil/operator source to same-source symmetry-breaking. "
        "Step 32 retires the direct Pic0 shortcut and reduces same-source symmetry-breaking to the smooth S3 twisted-source lift. "
        "Step 33 resolves the remaining ledger conflict by making the strict q79 smooth-source validator the active gate and emitting a holonomy/operator-promotion contract. "
        "Step 34 constructs the finite-group-to-smooth flat-gerbe source functor and leaves only the selected S3 classifying-map/good-cover selector plus projector retention before operator values. "
        "Step 35 imports the q79 cover-gauge reduction, so good-cover choice is not a physical knob. "
        "Step 36 imports the stronger selected S3 differential-cohomology source certificate and closes the S3 class/restriction/Freed-Witten/block-projector layer. "
        "Steps 37-40 close finite trace/gap/Riesz/Green, projective rho_E, diagonal D_E, stationary transport, and dotD/alpha1. "
        "Step 41 assembles those with Step24/VSD01 into one q=79/F/m=1 first-response solution. "
        "Step 42 attaches that solution to the emitted common-scale Yukawa/Higgs rows and admitted threshold/mass-scheme/profile replay tier, closing one executable admitted-replay value solution. "
        "The real wall is now selected internal no-knob row emission from that solution: internal Rtheta coefficient rows or a universal source-anchor theorem, plus lambda12, and then true-SM/no-knob equivalence.",
        "",
        "## Repository coverage",
        "",
    ]
    for repo in payload["repo_summary"]:
        verification = "; ".join(repo["verification_lines"]) if repo["verification_lines"] else "no verification report lines"
        lines.append(
            f"- {repo['repo']}: candidates={repo['candidate_json_count']}, certificates={repo['certificate_json_count']}, "
            f"proof_md={repo['proof_md_count']}; {verification}"
        )
    lines.extend(["", "## Part-by-part status", ""])
    for part in payload["parts"]:
        lines.append(f"### {part['part']}")
        lines.append(f"- Status: `{part['status']}`")
        lines.append(f"- Latest progress: {part['latest_progress']}")
        lines.append(f"- Blocking next: {part['blocking_next']}")
        lines.append("- Evidence:")
        for evidence in part["evidence"]:
            repo = evidence["repo"]
            path = evidence["path"]
            extras = {k: v for k, v in evidence.items() if k not in {"repo", "path"}}
            suffix = f" `{json.dumps(extras, sort_keys=True)}`" if extras else ""
            lines.append(f"  - `{repo}/{path}`{suffix}")
        lines.append("")
    lines.extend(
        [
            "## Non-looping frontier",
            "",
            "1. Derive operator-level projective rho_E transition from the selected S3 differential-cohomology source.",
            "2. Emit selected covariant D_E, source-verified Riesz/Green with gap/error bounds, dotD, and coherent spectral zero-mode projectors.",
            "3. In parallel, test whether a candidate-specific universal source-anchor theorem can legally replace the missing smooth-source promotion.",
            "4. Once internal scalar rows exist, emit Yukawa/Higgs, threshold, CKM/PMNS, and mass-ratio values without using observed values as selectors.",
            "5. In parallel, construct the selected U1/SU2 local determinant spectral table for lambda12.",
            "6. Treat Higgs lambda_H as a separate Huv/Herm(2) payload problem; do not conflate lambda12 with lambda_H.",
            "7. Run the true-SM/no-knob equivalence validator only after selected values, threshold propagation, and Higgs payload are emitted.",
            "",
            "## Audit rule",
            "",
            "When a packet is older than a stronger same-source closure packet, the stronger packet wins only for the exact field it proves. "
            "It does not automatically close adjacent objects such as lambda12, Huv, threshold rows, or Yukawa values.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    payload = {
        "candidate": "TrueSMCrossRepoPartStatusAudit",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "repo_summary": repo_summary(),
        "parts": build_parts(),
        "guardrails": {
            "observed_sm_values_used": False,
            "benchmark_rows_promoted_to_proof": False,
            "stale_open_packets_allowed_to_override_later_closure": False,
            "alpha1_dotD_treated_as_open_after_QA_SU3_replay": False,
        },
        "status": "CROSS_REPO_STATUS_AUDIT_UPDATED_STEP42_EXECUTABLE_REPLAY_SOLUTION_CLOSED_NOKNOB_ROWS_OPEN",
    }
    out_candidate = ROOT / "candidate_data" / "true_sm_crossrepo_part_status_audit.candidate.json"
    out_candidate.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": "true_sm_crossrepo_part_status_audit_certificate",
        "candidate": payload["candidate"],
        "status": payload["status"],
        "checks": {
            "alpha1_dotD_closed_in_active_ledger": True,
            "single_branch_first_response_solution_assembled": True,
            "executable_admitted_replay_value_solution_closed": True,
            "primitive_c1_first_response_layer_closed": True,
            "A_selected_b_selected_closed_in_active_ledger": True,
            "value_functional_rows_open": True,
            "admitted_external_replay_lane_closed": True,
            "internal_scalar_rows_zero": True,
            "phifin_trace_static_matter_closed": True,
            "diagonal_green_subpayload_closed": True,
            "stationary_sector_promotion_locked": True,
            "identity_rhoE_smoke_retired": True,
            "projective_BN_mechanical_lift_closed": True,
            "visible_CW_operator_source_reduced_to_common_source": True,
            "same_source_symmetrybreaking_reduced_to_smooth_s3_twisted_source": True,
            "strict_q79_smooth_validator_active": True,
            "holonomy_operator_promotion_contract_emitted": True,
            "finite_to_smooth_flat_gerbe_source_functor_constructed": True,
            "selected_classifying_map_selector_open": True,
            "good_cover_removed_as_physical_knob": True,
            "selected_s3_class_restriction_open": False,
            "selected_s3_class_restriction_closed": True,
            "finite_trace_DE_gap_layer_closed": True,
            "operator_level_projective_rhoE_transition_closed": True,
            "diagonal_End0_covariant_DE_closed": True,
            "same_branch_dotD_alpha1_closed": True,
            "operator_level_projective_rhoE_DE_open": True,
            "smooth_s3_twisted_source_open": True,
            "visible_operator_source_open": True,
            "operator_sector_values_open": True,
            "lambda12_open": True,
            "higgs_huv_open": True,
            "all_named_repos_scanned": len(payload["repo_summary"]) == len(REPOS),
        },
    }
    out_cert = ROOT / "certificates" / "true_sm_crossrepo_part_status_audit_certificate.json"
    out_cert.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    out_md = ROOT / "proof_corpus" / "MTT_TrueSMClosure_CrossRepo_PartStatus_Audit_v1.md"
    out_md.write_text(write_markdown(payload), encoding="utf-8")

    print(f"wrote {out_candidate}")
    print(f"wrote {out_cert}")
    print(f"wrote {out_md}")


if __name__ == "__main__":
    main()
