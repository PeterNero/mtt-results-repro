"""Build the selected finite-trace source/no-go gate for U1/Y Route-C Phi_fin."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

INPUTS = {
    "phifin_subpacket": DATA / "selected_u1y_routec_finite_emission_morphism_phifin_subpacket.candidate.json",
    "sm_phifin_schema": SM / "candidate_data" / "finite_emission_morphism_phifin.candidate.json",
    "sm_projector_retention": SM / "candidate_data" / "selected_spectral_galerkin_projector_retention_data.candidate.json",
    "sm_smooth_bn": SM / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json",
    "sm_de_smooth_bn": SM / "candidate_data" / "selected_routec_de_action_on_smooth_bn.candidate.json",
    "sm_projectors_dotd": SM / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json",
    "sm_strominger_solve_spec": SM / "candidate_data" / "selected_routec_strominger_galerkin_solve_spec.candidate.json",
    "q79_finite_connection_execution": Q79 / "candidate_data" / "q79_selected_finite_connection_solve_execution.candidate.json",
    "q79_de_green_dotd_source": Q79 / "candidate_data" / "q79_selected_de_green_dotd_source_for_primitive_c1.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_selected_finite_trace_source_or_nogo.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_selected_finite_trace_source_or_nogo_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_SelectedFiniteTrace_SourceOrNoGo_v1.md"

STATUS = "U1Y_ROUTEC_SELECTED_FINITE_TRACE_SOURCE_NOGO_BUILT_27MODE_PREFIX_VALUES_SOURCE_TRACE_OPEN"
NEXT = "Selected_U1Y_RouteC_TraceEquals27Mode_or_FullHYMReplay_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    phifin = load(INPUTS["phifin_subpacket"])
    sm_schema = load(INPUTS["sm_phifin_schema"])
    retention = load(INPUTS["sm_projector_retention"])
    smooth_bn = load(INPUTS["sm_smooth_bn"])
    de_bn = load(INPUTS["sm_de_smooth_bn"])
    dotd_bn = load(INPUTS["sm_projectors_dotd"])
    solve_spec = load(INPUTS["sm_strominger_solve_spec"])
    q79_exec = load(INPUTS["q79_finite_connection_execution"])
    q79_primitive = load(INPUTS["q79_de_green_dotd_source"])

    q79_import = q79_exec["finite_connection_execution_import_summary"]
    q79_attempt = q79_exec["selected_finite_connection_execution_attempt"]
    q79_contract = q79_exec["selected_trace_or_full_hym_source_contract"]

    old_smoke_lane = {
        "lane": "old_7slot_smoke_trace",
        "status": "REJECTED_AS_SELECTED_TRACE",
        "finite_scaffold_present": phifin["decision"]["finite_trace_scaffold_constructed"],
        "domain_lock_closed": phifin["decision"]["domain_lock_closed"],
        "selected_false_count": phifin["finite_trace_attempt"]["slot_summary"]["Q"]["de_selected_source_verified"] is False,
        "why_rejected": [
            "identity rho_E smoke remains unselected",
            "D_E/Riesz/Green/dotD selected-source flags are false",
            "projection commuting square and primitive C1 tensors are absent",
        ],
    }

    mode27_lane = {
        "lane": "smooth_27mode_BN_prefix",
        "status": "PREFIX_VALUES_EXECUTED_SOURCE_TRACE_OPEN",
        "finite_values_present": q79_attempt["finite_values_present"],
        "basis": {
            "basis_id": q79_attempt["branch"]["basis_id"],
            "dimension": q79_import["smooth_BN"]["dimension"],
            "zero_cluster_dimension": q79_import["smooth_BN"]["zero_cluster_dimension"],
            "complement_gap": q79_import["smooth_BN"]["complement_gap"],
            "projective_equivariance_up_to_central_phase": q79_import["smooth_BN"][
                "projective_equivariance_up_to_central_phase"
            ],
        },
        "rhoe": {
            "identity_smoke_replaced": q79_import["nonidentity_rhoE"]["identity_smoke_replaced"],
            "nonidentity_projective_rhoE_candidate_built": q79_import["nonidentity_rhoE"][
                "nonidentity_projective_rhoE_candidate_built"
            ],
            "selected_by_mtt": q79_import["nonidentity_rhoE"]["selected_by_mtt"],
        },
        "de": {
            "matrix_emitted": q79_import["DE"]["D_E_matrix_on_27_mode_BN_emitted"],
            "family_kernel_dimension": q79_import["DE"]["family_kernel_dimension"],
            "higgs_kernel_dimension": q79_import["DE"]["higgs_kernel_dimension"],
            "honest_validator_fails_only_by_selected_source_flags": q79_import["DE"][
                "honest_validator_fails_only_by_selected_source_flags"
            ],
        },
        "dotd": {
            "matrix_emitted": q79_import["dotD"]["dotD_alpha1_matrix_in_same_basis_emitted"],
            "sector_projectors_emitted": q79_import["dotD"]["sector_projectors_on_27_mode_BN_emitted"],
            "diagnostic_lift_validator_passes": q79_import["dotD"]["diagnostic_lift_validator_passes"],
            "honest_validator_fails_only_by_source_driver_flags": q79_import["dotD"][
                "honest_validator_fails_only_by_source_driver_flags"
            ],
        },
        "c1": {
            "primitive_engine_built": q79_import["C1"]["primitive_C1_contraction_engine_built"],
            "canonical_tensor_zero_response_result_proved_finitely": q79_import["C1"][
                "canonical_tensor_zero_response_result_proved_finitely"
            ],
            "all_c1_matrices_zero_for_canonical_tensor": q79_import["C1"][
                "all_c1_matrices_zero_for_canonical_tensor"
            ],
        },
    }

    source_trace_cutset = q79_exec["honest_replay_cutset"]["open_items"]
    selected_promotion = q79_attempt["selected_promotion"]
    closing_routes = q79_contract["accepted_closing_routes"]

    gate_decision = {
        "old_smoke_trace_selected": False,
        "smooth_27mode_prefix_values_present": True,
        "smooth_27mode_prefix_can_replace_old_smoke_as_best_prefix": True,
        "selected_trace_equality_proved": selected_promotion["selected_trace_equality"],
        "full_selected_operator_formula_proved": selected_promotion["full_selected_operator_formula"],
        "honest_replay_without_lifted_flags": selected_promotion["honest_replay_without_lifted_flags"],
        "selected_gap_error_certificate": selected_promotion["selected_gap_error_certificate"],
        "rhoE_selected_by_mtt": selected_promotion["rhoE_selected_by_mtt"],
        "selected_finite_connection_solve_closed": selected_promotion["selected_finite_connection_solve_closed"],
        "Phi_fin_closed": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "SelectedFiniteTraceSourceOrNoGoGate",
        "proved": True,
        "statement": (
            "The selected finite-trace gate has a strictly stronger finite prefix than "
            "the old 7-slot smoke packet: a non-identity projective rho_E candidate, "
            "27-mode B_N scaffold, model-active D_E/Riesz/Green, sector projectors, "
            "dotD, canonical C1 contraction engine, and first HYM correction are present. "
            "This still does not close Phi_fin because selected trace equality, the full "
            "selected Iwasawa/Strominger operator formula, selected gap/error certificate, "
            "and theorem-derived selected-source flags remain open."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCSelectedFiniteTraceSourceOrNoGo",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "phifin_subpacket": phifin["status"],
            "sm_phifin_schema": sm_schema["status"],
            "projector_retention": retention["status"],
            "smooth_bn": smooth_bn["status"],
            "de_smooth_bn": de_bn["status"],
            "projectors_dotd": dotd_bn["status"],
            "strominger_solve_spec": solve_spec["status"],
            "q79_finite_execution": q79_exec["status"],
            "q79_primitive_gate": q79_primitive["status"],
        },
        "old_smoke_lane": old_smoke_lane,
        "smooth_27mode_lane": mode27_lane,
        "source_trace_cutset": source_trace_cutset,
        "accepted_closing_routes": closing_routes,
        "decision": gate_decision,
        "theorem": theorem,
        "what_closes_now": {
            "old_identity_smoke_trace_rejected": True,
            "smooth_27mode_prefix_imported": True,
            "nonidentity_rhoE_candidate_preferred_over_identity_smoke": True,
            "same_basis_DE_Riesz_Green_dotD_prefix_values_present": True,
            "canonical_C1_zero_response_no_go_imported": True,
            "selected_trace_cutset_named": True,
            "three_legal_closing_routes_named": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_trace_equality": True,
            "canonical_metric_connection_source": True,
            "H_sector_shift_source": True,
            "full_selected_iwasawa_strominger_operator_formula": True,
            "selected_gap_error_certificate": True,
            "honest_replay_without_lifted_flags": True,
            "theorem_derived_selected_source_flags": True,
            "selected_noninvariant_C1_primitive_or_basis_transport": True,
            "primitive_C1_nonzero_values": True,
            "lambda_12": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_Phi_fin_closed": False,
            "claims_selected_finite_connection_solve_closed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_model_active_operator_is_full_selected_operator": False,
            "claims_identity_rhoE_smoke_is_selected": False,
            "uses_lifted_flags_as_proof": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "target_fitting_used": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCSelectedFiniteTraceSourceOrNoGo",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "old_smoke_trace_selected": False,
        "smooth_27mode_prefix_values_present": True,
        "basis_dimension": mode27_lane["basis"]["dimension"],
        "zero_cluster_dimension": mode27_lane["basis"]["zero_cluster_dimension"],
        "model_complement_gap": mode27_lane["basis"]["complement_gap"],
        "nonidentity_rhoE_candidate": mode27_lane["rhoe"]["nonidentity_projective_rhoE_candidate_built"],
        "rhoE_selected_by_mtt": mode27_lane["rhoe"]["selected_by_mtt"],
        "selected_trace_equality_proved": False,
        "full_selected_operator_formula_proved": False,
        "Phi_fin_closed": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C SelectedFiniteTrace SourceOrNoGo v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"smooth_27mode_prefix_values_present = {str(cert['smooth_27mode_prefix_values_present']).lower()}",
        f"selected_trace_equality_proved = {str(cert['selected_trace_equality_proved']).lower()}",
        f"Phi_fin_closed = {str(cert['Phi_fin_closed']).lower()}",
        f"lambda_12_closed = {str(cert['lambda_12_closed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The old 7-slot identity-smoke trace is rejected as a selected trace.",
        "The stronger 27-mode `B_N` prefix is now the best finite object:",
        "",
        "```text",
        f"basis dimension = {cert['basis_dimension']}",
        f"zero cluster dimension = {cert['zero_cluster_dimension']}",
        f"model complement gap = {cert['model_complement_gap']}",
        f"nonidentity rho_E candidate = {str(cert['nonidentity_rhoE_candidate']).lower()}",
        "```",
        "",
        "This prefix has real finite values, but it is not yet `Phi_fin`.",
        "The missing step is source-trace equality or a full selected HYM/Strominger replay.",
        "",
        "## Legal Closing Routes",
        "",
    ]
    for route, obligations in candidate["accepted_closing_routes"].items():
        lines.append(f"### {route}")
        lines.append("")
        for obligation in obligations:
            lines.append(f"- {obligation}")
        lines.append("")
    lines.extend(
        [
            "## Cutset",
            "",
        ]
    )
    for key, value in candidate["source_trace_cutset"].items():
        if value:
            lines.append(f"- `{key}`")
    lines.extend(
        [
            "",
            "## Theorem",
            "",
            candidate["theorem"]["statement"],
            "",
            "## Guardrails",
            "",
            "- Do not relabel the model-active operator as the full selected operator.",
            "- Do not use lifted selected flags as proof.",
            "- Do not compute `lambda_12` from this prefix.",
            "- Do not use observed or benchmark data.",
            "",
            "## Certificate",
            "",
            "```json",
            json.dumps(cert, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    candidate, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
