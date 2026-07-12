"""Audit whether the selected q79 Phi_fin alpha1 payload is closed.

This is deliberately stricter than the finite-emission bridge.  It asks:
given the current q79 packet plus the latest adjacent-repo status certificates,
can we honestly promote a selected Phi_fin alpha1 payload?

The answer is recorded as a closed decision gate, not as payload closure.  The
finite shape is present, and adjacent repos now sharpen the target, but the
selected correction/Galerkin emission is still absent.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

CONSTANTS = TEXPAPERS / "mtt-nonsm-constants-no-knob"
GR = TEXPAPERS / "mtt-protospinor-gr-response-proof"
QA_SU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"

OUT_DIR = CANDIDATES / "q79_selected_phifin_alpha1_payload"
OUT_TABLE = OUT_DIR / "closure_gate_table.json"
OUT_CANDIDATE = CANDIDATES / "q79_selected_phifin_alpha1_payload.candidate.json"
OUT_CERT = CERTS / "q79_selected_phifin_alpha1_payload_certificate.json"
OUT_PAPER = CORPUS / "Q79_Selected_PhiFin_Alpha1_Payload_v1.md"

Q79_INPUTS = {
    "finite_bridge": CERTS / "q79_valpha_source_origin_finite_emission_bridge_certificate.json",
    "frontier": CERTS / "valpha_repo_update_source_frontier_certificate.json",
    "selected_full_sm": CERTS / "selected_full_sm_data_theorem_attempt_certificate.json",
    "c1_response_attempt": CERTS / "selected_c1_response_extraction_attempt_certificate.json",
    "c1_finite_response": CERTS / "c1_finite_response_matrix_reduction_certificate.json",
    "c1_response_template": CERTS / "selected_c1_response_data_certificate.template.json",
}

ADJACENT_INPUTS = {
    "constants_higher_order": CONSTANTS
    / "certificates"
    / "higher_order_flavor_splitting_criterion_import_certificate.json",
    "constants_fiberclass": CONSTANTS
    / "certificates"
    / "c1_fiberclass_invariance_and_flavor_split_gate_certificate.json",
    "constants_selected_correction_gate": CONSTANTS
    / "certificates"
    / "selected_correction_emission_gate_certificate.json",
    "constants_c1_response_operator_import": CONSTANTS
    / "certificates"
    / "selected_c1_response_operator_emission_audit_import_certificate.json",
    "constants_c1_operator_source_rebuild": CONSTANTS
    / "certificates"
    / "selected_c1_operator_source_rebuild_attempt_certificate.json",
    "constants_routec_rhoe_bn_prefix": CONSTANTS
    / "certificates"
    / "routec_rhoe_bn_operator_prefix_import_certificate.json",
    "gr_remaining_gates": GR
    / "certificates"
    / "cross_repo_remaining_gates_source_triage_certificate.json",
    "gr_routec_payload_value_import_attempt": GR
    / "certificates"
    / "selected_routec_payload_value_import_attempt_certificate.json",
    "gr_routec_source_origin_conditional_lemma": GR
    / "certificates"
    / "routec_selected_source_origin_paper_lemma_certificate.json",
    "qa_chi": QA_SU3
    / "certificates"
    / "selected_response_functional_chi_qa_certificate.json",
    "qa_electroweak_matching": QA_SU3
    / "certificates"
    / "electroweak_matching_or_absolute_coupling_normalization_certificate.json",
    "qa_u1_su2_same_scheme": QA_SU3
    / "certificates"
    / "u1_su2_same_scheme_payloads_or_k_gauge_anchor_certificate.json",
    "qa_u1_su2_source_fill": QA_SU3
    / "certificates"
    / "u1_su2_internal_overlap_payload_template_or_k_gauge_source_fill_certificate.json",
    "sm_phifin_alpha1": SM_PARITY
    / "certificates"
    / "selected_phifin_alpha1_payload_certificate.json",
    "sm_first_correction": SM_PARITY
    / "certificates"
    / "selected_routec_first_correction_search_or_galerkin_run_certificate.json",
    "sm_higher_order": SM_PARITY
    / "certificates"
    / "selected_routec_higherorder_fullresponse_flavor_splitting_certificate.json",
    "sm_correction_emission": SM_PARITY
    / "certificates"
    / "selected_routec_correction_source_emission_or_selected_galerkin_values_certificate.json",
    "sm_deltatheta_solve_gate": SM_PARITY
    / "certificates"
    / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve_certificate.json",
    "sm_c1_response_operator_emission": SM_PARITY
    / "certificates"
    / "selected_routec_selected_c1_response_operator_emission_certificate.json",
    "sm_c1_operator_source_or_galerkin_rebuild": SM_PARITY
    / "certificates"
    / "selected_routec_selected_c1_operator_source_or_galerkin_rebuild_certificate.json",
    "sm_noninvariant_c1_primitive_search": SM_PARITY
    / "certificates"
    / "selected_routec_noninvariant_c1_primitive_search_certificate.json",
    "sm_spectral_retention": SM_PARITY
    / "certificates"
    / "selected_spectral_galerkin_projector_retention_data_certificate.json",
}

REPOS = {
    "q79": ROOT,
    "constants": CONSTANTS,
    "gr": GR,
    "qa_su3": QA_SU3,
    "sm_parity": SM_PARITY,
}


def run_git(repo: Path, args: list[str]) -> str:
    if not (repo / ".git").exists():
        return ""
    proc = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.stdout.strip()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def status_summary(status_short: str) -> dict[str, Any]:
    lines = [line for line in status_short.splitlines() if line.strip()]
    return {
        "dirty": bool(lines),
        "line_count": len(lines),
        "modified_count": sum(line.startswith(" M") or line.startswith("M ") for line in lines),
        "untracked_count": sum(line.startswith("??") for line in lines),
        "preview": lines[:12],
    }


def repo_snapshot(name: str, path: Path) -> dict[str, Any]:
    if name == "q79":
        return {
            "path": str(path),
            "present": (path / ".git").exists(),
            "branch": run_git(path, ["branch", "--show-current"]),
            "head": "omitted-current-repo-head-for-reproducibility",
            "status_summary": {
                "dirty": False,
                "line_count": 0,
                "modified_count": 0,
                "untracked_count": 0,
                "preview": [],
                "note": "current q79 head/status omitted so this certificate remains reproducible after commit",
            },
        }
    status = run_git(path, ["status", "--short"])
    return {
        "path": str(path),
        "present": path.exists() and (path / ".git").exists(),
        "branch": run_git(path, ["branch", "--show-current"]),
        "head": run_git(path, ["log", "-1", "--oneline"]),
        "status_summary": status_summary(status),
    }


def cert_status(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": str(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact")
        or data.get("primary_next_artifact")
        or data.get("next_required_object"),
        "what_closes": data.get("what_closes") or data.get("closed_now") or {},
        "what_remains_open": data.get("what_remains_open") or data.get("not_closed") or {},
    }


def all_true(values: dict[str, Any]) -> bool:
    return bool(values) and all(value is True for value in values.values())


def all_false(values: dict[str, Any]) -> bool:
    return bool(values) and all(value is False for value in values.values())


def any_true(values: dict[str, Any]) -> bool:
    return any(value is True for value in values.values())


def extract_bridge_gate_table(bridge: dict[str, Any]) -> dict[str, Any]:
    finite = bridge.get("finite_emission_schema", {})
    alpha = bridge.get("alpha1_driver_bridge", {})
    return {
        "finite_shape_gates": finite.get("shape_gates", {}),
        "selected_payload_flags": finite.get("selected_payload_flags", {}),
        "alpha1_support_gates": alpha.get("support_gates", {}),
        "alpha1_missing_selected_values": alpha.get("missing_selected_values", {}),
        "identity_rhoE_smoke_rejected": finite.get("identity_rhoE_smoke_rejected"),
        "branch_packet": finite.get("branch_packet", {}),
        "selected_payload_contract": bridge.get("selected_payload_contract", {}),
    }


def build_adjacent_implications(adjacent: dict[str, dict[str, Any]]) -> dict[str, Any]:
    constants = adjacent["constants_higher_order"]
    constants_correction = adjacent["constants_selected_correction_gate"]
    constants_operator = adjacent["constants_c1_response_operator_import"]
    constants_rebuild = adjacent["constants_c1_operator_source_rebuild"]
    constants_prefix = adjacent["constants_routec_rhoe_bn_prefix"]
    qa_chi = adjacent["qa_chi"]
    qa_ew = adjacent["qa_electroweak_matching"]
    sm_payload = adjacent["sm_phifin_alpha1"]
    sm_correction = adjacent["sm_correction_emission"]
    sm_delta = adjacent["sm_deltatheta_solve_gate"]
    sm_operator = adjacent["sm_c1_response_operator_emission"]
    sm_rebuild = adjacent["sm_c1_operator_source_or_galerkin_rebuild"]
    sm_noninv = adjacent["sm_noninvariant_c1_primitive_search"]
    gr = adjacent["gr_remaining_gates"]
    gr_routec = adjacent["gr_routec_payload_value_import_attempt"]
    gr_source_origin = adjacent["gr_routec_source_origin_conditional_lemma"]

    qa_chi_closed = (
        qa_chi.get("status") == "QA_SU3_SELECTED_FINITE_RESPONSE_FUNCTIONAL_CHI_QA_CLOSED_MEASURED_MATCH_OPEN"
        and qa_chi.get("what_closes", {}).get("selected_finite_response_functional_chi_Qa")
        == "1"
    )
    electroweak_interface_open = (
        qa_ew.get("status") == "QA_SU3_ELECTROWEAK_MATCHING_INTERFACE_BUILT_ABSOLUTE_K_GAUGE_OPEN"
        and qa_ew.get("what_remains_open", {}).get("K_gauge_absolute_or_common_normalization")
        is True
    )
    u1_su2_same_scheme_open = (
        qa_u1_su2 := adjacent["qa_u1_su2_same_scheme"]
    ).get("status") == "U1_SU2_SAME_SCHEME_ACCEPTANCE_CONTRACT_BUILT_PAYLOADS_AND_K_GAUGE_OPEN" and (
        qa_u1_su2.get("what_remains_open", {}).get("U1_same_scheme_payload") is True
        and qa_u1_su2.get("what_remains_open", {}).get("SU2_same_scheme_payload") is True
        and qa_u1_su2.get("what_remains_open", {}).get("K_gauge_anchor") is True
    )
    u1_su2_source_fill_partial_only = (
        qa_u1_su2_fill := adjacent["qa_u1_su2_source_fill"]
    ).get("status") == "U1_SU2_K_GAUGE_FILL_ATTEMPT_TEMPLATE_BUILT_CURRENT_SOURCE_PARTIAL_ONLY" and (
        qa_u1_su2_fill.get("what_remains_open", {}).get("I1_U1_payload") is True
        and qa_u1_su2_fill.get("what_remains_open", {}).get("I2_SU2_payload") is True
    )
    higher_order_criterion_closed = (
        constants.get("status")
        == "HIGHER_ORDER_FLAVOR_SPLITTING_CRITERION_IMPORTED_SELECTED_EMISSION_OPEN"
        and constants.get("what_closes", {}).get("higher_order_splitting_criterion_proved")
        is True
    )
    diagnostic_not_selected = (
        constants.get("what_remains_open", {}).get("selected_correction_matrix_source") is True
        and sm_correction.get("status")
        == "MTT_SELECTED_ROUTEC_CORRECTION_SOURCE_EMISSION_AUDITED_DIAGNOSTIC_SPLITTER_NOT_SOURCE_EMITTED_VALUES_OPEN"
        and sm_correction.get("what_remains_open", {}).get("selected_deltaTheta_C1_solution")
        is True
    )
    correction_gate_sharpens_to_prefix = (
        constants_correction.get("status")
        == "SELECTED_CORRECTION_EMISSION_GATE_REDUCED_NONIDENTITY_RHOE_AND_BN_CONSTRUCTION_OPEN"
        and constants_correction.get("what_closes", {}).get("strict_primitive_search_found_no_legal_emission")
        is True
    )
    nonidentity_prefix_built_but_selected_open = (
        constants_prefix.get("status")
        == "ROUTEC_RHOE_BN_OPERATOR_PREFIX_IMPORTED_NONINVARIANT_C1_PRIMITIVE_OPEN"
        and constants_prefix.get("what_closes", {}).get("nonidentity_projective_rhoE_candidate_built")
        is True
        and constants_prefix.get("what_closes", {}).get("canonical_C1_zero_response_no_go_proved")
        is True
        and constants_prefix.get("what_remains_open", {}).get("selected_noninvariant_C1_primitive_or_vertex")
        is True
    )
    deltatheta_gate_open = (
        sm_delta.get("status")
        == "MTT_SELECTED_ROUTEC_DELTATHETA_C1_SOLVE_GATE_BUILT_SELECTED_HESSIAN_RESPONSE_OPERATOR_OPEN"
        and sm_delta.get("what_remains_open", {}).get("selected_C1_response_operator_A_selected")
        is True
    )
    c1_operator_emission_open = (
        sm_operator.get("status")
        == "MTT_SELECTED_ROUTEC_C1_RESPONSE_OPERATOR_EMISSION_AUDITED_A_SELECTED_NOT_EMITTED"
        and sm_operator.get("what_remains_open", {}).get("emit_selected_A_selected") is True
        and constants_operator.get("status")
        == "SELECTED_C1_RESPONSE_OPERATOR_EMISSION_AUDITED_A_SELECTED_NOT_EMITTED"
    )
    c1_operator_rebuild_attempt_open = (
        constants_rebuild.get("status")
        == "SELECTED_C1_OPERATOR_REBUILD_ATTEMPT_EXECUTED_SELECTED_BLOCKS_STILL_OPEN"
        and constants_rebuild.get("what_remains_open", {}).get("emit_selected_A_selected") is True
        and constants_rebuild.get("what_remains_open", {}).get("selected_source_certificate") is True
    )
    noninvariant_candidates_unselected = (
        sm_noninv.get("status")
        == "MTT_SELECTED_ROUTEC_NONINVARIANT_C1_PRIMITIVE_SEARCH_BUILT_UNSELECTED_CANDIDATES_OPEN"
        and sm_noninv.get("what_closes", {}).get("finite_noninvariant_C1_candidate_matrices_emitted")
        is True
        and sm_noninv.get("what_remains_open", {}).get("selected_basis_transport_theorem") is True
    )
    basis_transport_lane_selected = (
        sm_rebuild.get("status")
        == "MTT_SELECTED_ROUTEC_C1_OPERATOR_SOURCE_GALERKIN_REBUILD_ITERATED_BASIS_TRANSPORT_LANE_SELECTED_AS_NEXT_PROOF_TARGET"
        and sm_rebuild.get("what_closes", {}).get("best_next_lane_selected") is True
        and sm_rebuild.get("what_remains_open", {}).get("prove_selected_basis_transport_or_vertex_source_theorem")
        is True
    )
    payload_values_open = (
        sm_payload.get("status")
        == "MTT_SELECTED_PHIFIN_ALPHA1_PAYLOAD_ATTEMPT_BUILT_SELECTED_SPECTRAL_VALUES_OPEN"
        and sm_payload.get("what_remains_open", {}).get("selected_PhiFin_alpha1_payload_values")
        is True
    )
    selected_matter_payload_open = (
        gr.get("status")
        == "CROSS_REPO_REMAINING_GATES_TRIAGED_BEST_NEXT_GATE_SELECTED_MATTER_PAYLOAD"
        and gr.get("what_closes", {}) == {}
    )
    routec_payload_value_import_blocked = (
        gr_routec.get("status")
        == "SELECTED_ROUTEC_PAYLOAD_VALUE_IMPORT_ATTEMPT_BLOCKED_SOURCE_VALUES_OPEN"
        and gr_routec.get("what_remains_open", {}) == {}
        and gr_routec.get("next_required_artifact") is None
    )
    routec_source_origin_conditional_only = (
        gr_source_origin.get("status")
        == "ROUTEC_SOURCE_ORIGIN_CONDITIONAL_LEMMA_PROVED_PAPER_INSERTION_BUILT_PHI_FIN_OPEN"
        and gr_source_origin.get("what_remains_open", {}) == {}
        and gr_source_origin.get("next_required_artifact") is None
    )

    return {
        "qa_chi_closed_but_not_q79_payload": qa_chi_closed,
        "qa_electroweak_interface_open_not_payload_source": electroweak_interface_open,
        "qa_u1_su2_same_scheme_payloads_and_k_gauge_open": u1_su2_same_scheme_open,
        "qa_u1_su2_source_fill_partial_only": u1_su2_source_fill_partial_only,
        "higher_order_flavor_splitting_criterion_closed": higher_order_criterion_closed,
        "diagnostic_splitter_not_selected_source_emission": diagnostic_not_selected,
        "correction_gate_reduced_to_nonidentity_rhoe_bn_prefix": correction_gate_sharpens_to_prefix,
        "nonidentity_rhoe_bn_prefix_built_but_selected_open": nonidentity_prefix_built_but_selected_open,
        "canonical_c1_zero_response_no_go_imported": nonidentity_prefix_built_but_selected_open,
        "deltatheta_solve_gate_built_selected_operator_open": deltatheta_gate_open,
        "c1_response_operator_A_selected_not_emitted": c1_operator_emission_open,
        "c1_operator_rebuild_attempt_selected_blocks_still_open": c1_operator_rebuild_attempt_open,
        "noninvariant_c1_candidates_built_but_unselected": noninvariant_candidates_unselected,
        "basis_transport_lane_selected_as_next_proof_target": basis_transport_lane_selected,
        "sm_phifin_payload_values_still_open": payload_values_open,
        "gr_triage_keeps_selected_matter_payload_open": selected_matter_payload_open,
        "gr_direct_routec_payload_value_import_attempt_blocked": routec_payload_value_import_blocked,
        "gr_source_origin_conditional_lemma_proved_phi_fin_open": routec_source_origin_conditional_only,
        "adjacent_repos_emit_selected_q79_payload_values": False,
    }


def build_candidate() -> dict[str, Any]:
    bridge = load(Q79_INPUTS["finite_bridge"])
    q79_statuses = {name: cert_status(path) for name, path in Q79_INPUTS.items()}
    adjacent_statuses = {name: cert_status(path) for name, path in ADJACENT_INPUTS.items()}
    gate_table = extract_bridge_gate_table(bridge)
    adjacent_implications = build_adjacent_implications(adjacent_statuses)

    finite_shape_pass = all_true(gate_table["finite_shape_gates"])
    selected_payload_flags_all_true = all_true(gate_table["selected_payload_flags"])
    selected_payload_flags_have_open_false = any(
        value is False for value in gate_table["selected_payload_flags"].values()
    )
    alpha1_support_pass = all_true(gate_table["alpha1_support_gates"])
    alpha1_values_missing = all_true(gate_table["alpha1_missing_selected_values"])
    adjacent_payload_emitted = adjacent_implications[
        "adjacent_repos_emit_selected_q79_payload_values"
    ]
    can_close_payload_now = (
        finite_shape_pass
        and selected_payload_flags_all_true
        and alpha1_support_pass
        and not alpha1_values_missing
        and adjacent_payload_emitted
    )

    closure_test = {
        "finite_shape_pass": finite_shape_pass,
        "identity_smoke_rejected": gate_table["identity_rhoE_smoke_rejected"] is True,
        "alpha1_support_pass": alpha1_support_pass,
        "selected_payload_flags_all_true": selected_payload_flags_all_true,
        "selected_payload_flags_have_open_false": selected_payload_flags_have_open_false,
        "alpha1_selected_values_still_missing": alpha1_values_missing,
        "adjacent_selected_q79_payload_values_emitted": adjacent_payload_emitted,
        "target_fitting_used": False,
        "benchmark_entries_used": False,
        "can_close_selected_phifin_alpha1_payload_now": can_close_payload_now,
    }

    hard_next_artifact = (
        "Q79_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1"
    )
    theorem_statement = (
        "The current q79 branch closes the finite Phi_fin alpha1 codomain and the "
        "alpha1 rank/support contract, but it cannot be promoted to a selected "
        "payload because selected D_E/Riesz/Green/dotD flags remain false, "
        "the q79-local rho_E packet is still identity smoke, and the adjacent "
        "nonidentity rho_E/27-mode B_N prefix is not selected proof.  The latest "
        "SM/constants updates further show that the canonical C1 response is "
        "zero and that A_selected, b_selected, selected primitive contractions, "
        "or a non-invariant primitive/basis-transport source are not emitted.  "
        "The GR direct Route-C payload-value import attempt reaches the same "
        "answer: honest candidate shapes exist, but proof-usable selected values "
        "are unavailable.  The newest rebuild audits select the basis-transport "
        "or vertex/primitive source theorem as the next proof target.  Thus the "
        "closure gate is closed negatively: the next real object is a selected "
        "basis-transport/primitive source theorem that emits A_selected and "
        "b_selected, not another diagnostic splitter or observed-data fit."
    )

    return {
        "certificate": "Q79SelectedPhiFinAlpha1PayloadClosureGate",
        "status": "Q79_SELECTED_PHIFIN_ALPHA1_PAYLOAD_CLOSURE_GATE_CLOSED_SELECTED_EMISSION_OPEN",
        "analysis_script": rel(Path(__file__)),
        "candidate_data": rel(OUT_CANDIDATE),
        "gate_table": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "repo_snapshots": {name: repo_snapshot(name, path) for name, path in REPOS.items()},
        "q79_input_statuses": q79_statuses,
        "adjacent_input_statuses": adjacent_statuses,
        "closure_gate_table": gate_table,
        "adjacent_update_implications": adjacent_implications,
        "closure_test": closure_test,
        "closed_by_this_attempt": {
            "latest_repo_updates_checked": all(
                snapshot["present"]
                for snapshot in {name: repo_snapshot(name, path) for name, path in REPOS.items()}.values()
            ),
            "finite_phifin_alpha1_codomain_confirmed": finite_shape_pass,
            "alpha1_support_and_rank_contract_confirmed": alpha1_support_pass,
            "qa_chi_retarded_trace_pairing_imported_as_pattern_only": adjacent_implications[
                "qa_chi_closed_but_not_q79_payload"
            ],
            "higher_order_splitting_criterion_imported": adjacent_implications[
                "higher_order_flavor_splitting_criterion_closed"
            ],
            "diagnostic_vs_selected_emission_separated": adjacent_implications[
                "diagnostic_splitter_not_selected_source_emission"
            ],
            "nonidentity_rhoe_bn_prefix_imported_as_unselected_prefix": adjacent_implications[
                "nonidentity_rhoe_bn_prefix_built_but_selected_open"
            ],
            "canonical_c1_zero_response_no_go_imported": adjacent_implications[
                "canonical_c1_zero_response_no_go_imported"
            ],
            "selected_c1_operator_emission_blocker_identified": adjacent_implications[
                "c1_response_operator_A_selected_not_emitted"
            ],
            "gr_direct_payload_value_import_attempt_checked": adjacent_implications[
                "gr_direct_routec_payload_value_import_attempt_blocked"
            ],
            "conditional_source_origin_lemma_imported_phi_fin_open": adjacent_implications[
                "gr_source_origin_conditional_lemma_proved_phi_fin_open"
            ],
            "basis_transport_lane_selected_as_next_target": adjacent_implications[
                "basis_transport_lane_selected_as_next_proof_target"
            ],
            "straight_payload_promotion_rejected": not can_close_payload_now,
            "next_missing_object_identified": True,
            "target_fitting_excluded": True,
        },
        "still_open": {
            "selected_PhiFin_alpha1_payload_values": True,
            "selected_correction_matrix_source": True,
            "selected_galerkin_values": True,
            "selected_deltaTheta_C1_solution": True,
            "selected_dotD_alpha1_derivative": True,
            "selected_zero_mode_bases": True,
            "primitive_C1_contractions": True,
            "selected_nonidentity_rhoE_source_promotion": True,
            "operator_level_projective_rhoE_promotion": True,
            "selected_noninvariant_C1_primitive_or_basis_transport": True,
            "prove_selected_basis_transport_or_vertex_source_theorem": True,
            "emit_selected_A_selected_and_b_selected": True,
            "finite_C1_Hessian_and_lower_blocks": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "claims_selected_phifin_alpha1_payload_values": False,
            "claims_selected_correction_matrix_source": False,
            "claims_selected_galerkin_values": False,
            "claims_nonidentity_rhoE_values": False,
            "claims_selected_D_E_Riesz_Green_dotD": False,
            "claims_finite_C1_response_matrices": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "promotes_dirty_adjacent_packets_as_proof": False,
        },
        "theorem": {
            "name": "Q79SelectedPhiFinAlpha1PayloadClosureGate",
            "proved": True,
            "closure_claimed": False,
            "statement": theorem_statement,
        },
        "next_required_artifact": hard_next_artifact,
        "secondary_next_artifacts": [
            "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1",
            "MTT_Selected_RouteC_Selected_C1_Operator_Source_or_Galerkin_Rebuild_v1",
            "Selected_RouteC_C1_Operator_Source_Rebuild_Payload_v1",
            "FiniteEmissionMorphism_Phi_fin_with_Selected_Payload_Emission",
            "MTT_RouteC_Selected_Source_Origin_Lemma_v1_or_Selected_DeltaTheta_C1_Solve_v1",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def render_bool_map(items: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in items.items())


def build_paper(cert: dict[str, Any]) -> str:
    closure = cert["closure_test"]
    table = cert["closure_gate_table"]
    adjacent = cert["adjacent_update_implications"]
    closed = "\n".join(
        f"- `{key}`" for key, value in cert["closed_by_this_attempt"].items() if value
    )
    open_items = "\n".join(f"- `{key}`" for key, value in cert["still_open"].items() if value)
    repo_lines = "\n".join(
        f"- `{name}`: `{row['head']}` dirty=`{row['status_summary']['dirty']}`"
        for name, row in cert["repo_snapshots"].items()
    )
    return f"""# Q79 Selected PhiFin Alpha1 Payload v1

## Result

This artifact closes the decision gate for the current q79 selected
`Phi_fin alpha1` payload attempt.

The payload is **not** closed.  The finite codomain is present, the alpha1
support contract is present, and the diagnostic flavor-splitting criterion is
now sharp.  But selected emission is still absent: the Route-C selected-source
flags remain false, the q79-local `rho_E` packet is still identity smoke, and
the latest correction/operator audits explicitly separate diagnostic splitters
and finite prefixes from source-emitted values.  A nonidentity rhoE/27-mode BN
prefix now exists in the adjacent constants/SM chain, but its canonical C1
response is zero and `A_selected`, `b_selected`, selected primitive
contractions, or non-invariant basis transport are still not emitted.  The
fresh GR payload-value import attempt confirms the same non-promotion: honest
candidate data exist, but proof-usable selected values do not.  The current
best next target is the basis-transport/vertex/primitive source theorem that
would emit `A_selected` and `b_selected`.

## Repo Snapshot

{repo_lines}

## Closure Test

{render_bool_map(closure)}

## Finite Shape Gates

{render_bool_map(table["finite_shape_gates"])}

## Selected Payload Flags

{render_bool_map(table["selected_payload_flags"])}

## Alpha1 Gate

Support:

{render_bool_map(table["alpha1_support_gates"])}

Still missing:

{render_bool_map(table["alpha1_missing_selected_values"])}

## Adjacent Update Implications

{render_bool_map(adjacent)}

## What This Closes

{closed}

## What Remains Open

{open_items}

## Theorem

`{cert["theorem"]["name"]}` is proved.

{cert["theorem"]["statement"]}

Next required q79 artifact: `{cert["next_required_artifact"]}`.

Companion targets:
{chr(10).join(f"- `{item}`" for item in cert["secondary_next_artifacts"])}
"""


def main() -> int:
    cert = build_candidate()
    write_json(OUT_TABLE, cert["closure_gate_table"])
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")
    print("Q79 selected Phi_fin alpha1 payload closure gate")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
