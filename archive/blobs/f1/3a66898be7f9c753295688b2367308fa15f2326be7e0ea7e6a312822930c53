"""Build E_H^UV section-source identity or direct Herm(2) Huv row emission.

This imports the late constants-repo H7B1S/T/U/V/W/X sequence into the active
SM no-knob value frontier.  The purpose is to separate three layers that were
easy to blur:

* ordered UV-Higgs labels and quotient scaffold, now closed as support;
* typed finite E_H^UV section/source basis plus projection measure, still open;
* direct Herm(2) Huv rows, still absent.

The artifact therefore advances the current target without promoting labels,
conditional reduction diagnostics, or finite-trace analogy into the missing H
K-threshold source row.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
CONSTANTS = TEXPAPERS / "mtt-individual-constants-source-search"
CONST_DATA = CONSTANTS / "candidate_data"

SLUG = "selected_ehuvsectionsourceidentity_or_directherm2huvrowemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CONST_IMPORT = PACKET_DIR / "late_h7b1_sequence_import.packet.json"
ORDERED_SCAFFOLD = PACKET_DIR / "ehuv_ordered_quotient_scaffold_clause.packet.json"
BRIDGE_REDUCTION = PACKET_DIR / "sectionring_quadrature_bridge_reduction.packet.json"
DIRECT_RECHECK = PACKET_DIR / "direct_herm2_huv_payload_recheck.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_section_source_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_section_source_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_EHUvSectionSourceIdentity_or_DirectHerm2HuvRowEmission_v1.md"

PREVIOUS = DATA / "selected_ehuvbindingtraceidentity_or_directhuvrows_to_hkthresholdemission.candidate.json"
PREVIOUS_HK_GATE = (
    DATA
    / "selected_ehuvbindingtraceidentity_or_directhuvrows_to_hkthresholdemission"
    / "hk_threshold_gate_after_ehuv_attempt.packet.json"
)
PREVIOUS_BINDING = (
    DATA
    / "selected_ehuvbindingtraceidentity_or_directhuvrows_to_hkthresholdemission"
    / "ehuv_binding_trace_identity_attempt.packet.json"
)

H7B1S = CONST_DATA / "const_higgs_01_h7b1s_huv_bridge_functor_or_nonlinear_hym_row_execution.candidate.json"
H7B1T = CONST_DATA / "const_higgs_01_h7b1t_uv_higgs_plane_binding_or_minimal_lift_theorem.candidate.json"
H7B1U = CONST_DATA / "const_higgs_01_h7b1u_source_bound_metric_and_finite_reduction.candidate.json"
H7B1V = CONST_DATA / "const_higgs_01_h7b1v_reduction_selector_or_direct_herm2_huv_source.candidate.json"
H7B1W = CONST_DATA / "const_higgs_01_h7b1w_finite_trace_hym_binding_or_direct_huv_payload.candidate.json"
H7B1X = CONST_DATA / "const_higgs_01_h7b1x_selected_higgs_hym_sectionring_quadrature_or_direct_huv_rows.candidate.json"

H7B1X_ORDERED = (
    CONST_DATA
    / "const_higgs_01_h7b1x_selected_higgs_hym_sectionring_quadrature_or_direct_huv_rows"
    / "ordered_higgs_channel_label_import.packet.json"
)
H7B1X_BRIDGE = (
    CONST_DATA
    / "const_higgs_01_h7b1x_selected_higgs_hym_sectionring_quadrature_or_direct_huv_rows"
    / "bridge_validator_replay.packet.json"
)
H7B1X_REQUEST = (
    CONST_DATA
    / "const_higgs_01_h7b1x_selected_higgs_hym_sectionring_quadrature_or_direct_huv_rows"
    / "section_basis_quadrature_payload_request.packet.json"
)
H7B1W_TRACE = (
    CONST_DATA
    / "const_higgs_01_h7b1w_finite_trace_hym_binding_or_direct_huv_payload"
    / "finite_trace_binding_attempt.packet.json"
)
H7B1W_DIRECT = (
    CONST_DATA
    / "const_higgs_01_h7b1w_finite_trace_hym_binding_or_direct_huv_payload"
    / "direct_huv_payload_attempt.packet.json"
)
H7B1W_EXTERNAL = (
    CONST_DATA
    / "const_higgs_01_h7b1w_finite_trace_hym_binding_or_direct_huv_payload"
    / "external_hym_quadrature_criterion.packet.json"
)
H7B1U_REDUCTION = (
    CONST_DATA
    / "const_higgs_01_h7b1u_source_bound_metric_and_finite_reduction"
    / "conditional_finite_reduction_execution.packet.json"
)

STATUS = (
    "MTT_SELECTED_EHUVSECTIONSOURCEIDENTITY_OR_DIRECTHERM2HUVROWEMISSION_"
    "IMPORTED_ORDERED_SCAFFOLD_BRIDGE_C2_C6_OPEN"
)
NEXT = "MTT_Selected_HiggsHYMSectionRingQuadratureBridgeTheorem_or_DirectHuvPayload_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing EHUv section-source inputs: " + ", ".join(missing))


def clause_closed(bridge: dict[str, Any], clause: str) -> bool:
    return bool(bridge["clauses"][clause]["closed"])


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_HK_GATE,
        PREVIOUS_BINDING,
        H7B1S,
        H7B1T,
        H7B1U,
        H7B1V,
        H7B1W,
        H7B1X,
        H7B1X_ORDERED,
        H7B1X_BRIDGE,
        H7B1X_REQUEST,
        H7B1W_TRACE,
        H7B1W_DIRECT,
        H7B1W_EXTERNAL,
        H7B1U_REDUCTION,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_hk = load(PREVIOUS_HK_GATE)
    previous_binding = load(PREVIOUS_BINDING)
    h7b1s = load(H7B1S)
    h7b1t = load(H7B1T)
    h7b1u = load(H7B1U)
    h7b1v = load(H7B1V)
    h7b1w = load(H7B1W)
    h7b1x = load(H7B1X)
    ordered = load(H7B1X_ORDERED)
    bridge = load(H7B1X_BRIDGE)
    request = load(H7B1X_REQUEST)
    trace_attempt = load(H7B1W_TRACE)
    direct_attempt = load(H7B1W_DIRECT)
    external = load(H7B1W_EXTERNAL)
    reduction = load(H7B1U_REDUCTION)

    constants_import = {
        "schema": "MTTLateH7B1SequenceImport.v1",
        "status": "LATE_H7B1_SEQUENCE_IMPORTED_NO_HUV_PAYLOAD",
        "closure_claimed": True,
        "imported_sequence": {
            "H7B1S": {
                "status": h7b1s["status"],
                "minimal_missing_theorem_built": h7b1s["minimal_missing_theorem_built"],
                "UV_Higgs_plane_binding_closed": h7b1s["UV_Higgs_plane_binding_closed"],
            },
            "H7B1T": {
                "status": h7b1t["status"],
                "formal_UV_exact_sequence_scaffold_closed": h7b1t[
                    "formal_UV_exact_sequence_scaffold_closed"
                ],
                "conditional_G_minimal_lift_formula_proved": h7b1t[
                    "conditional_G_minimal_lift_formula_proved"
                ],
                "source_metric_bound_to_E_H_UV": h7b1t["source_metric_bound_to_E_H_UV"],
            },
            "H7B1U": {
                "status": h7b1u["status"],
                "conditional_finite_reduction_executable": h7b1u[
                    "conditional_finite_reduction_executable"
                ],
                "source_metric_bound_to_E_H_UV": h7b1u["source_metric_bound_to_E_H_UV"],
            },
            "H7B1V": {
                "status": h7b1v["status"],
                "finite_Weyl_trace_measure_derived": h7b1v["finite_Weyl_trace_measure_derived"],
                "uniform_reduction_best_current_source_aligned_candidate": h7b1v[
                    "uniform_reduction_best_current_source_aligned_candidate"
                ],
                "trace_to_HYM_grid_binding_closed": h7b1v["trace_to_HYM_grid_binding_closed"],
            },
            "H7B1W": {
                "status": h7b1w["status"],
                "selected_Higgs_HYM_quadrature_bridge_criterion_emitted": h7b1w[
                    "selected_Higgs_HYM_quadrature_bridge_criterion_emitted"
                ],
                "finite_trace_HYM_binding_closed": h7b1w["finite_trace_HYM_binding_closed"],
                "direct_Herm2_Huv_payload_emitted": h7b1w[
                    "direct_Herm2_Huv_payload_emitted"
                ],
            },
            "H7B1X": {
                "status": h7b1x["status"],
                "E_H_UV_exact_sequence_scaffold_closed": h7b1x[
                    "E_H_UV_exact_sequence_scaffold_closed"
                ],
                "ordered_Hu_Hd_channel_scaffold_closed": h7b1x[
                    "ordered_Hu_Hd_channel_scaffold_closed"
                ],
                "bridge_validator_first_clause_filled": h7b1x[
                    "bridge_validator_first_clause_filled"
                ],
                "selected_E_H_UV_section_basis_emitted": h7b1x[
                    "selected_E_H_UV_section_basis_emitted"
                ],
            },
        },
        "decision": {
            "ordered_scaffold_closure_imported": True,
            "bridge_criterion_imported": True,
            "direct_Huv_payload_imported": False,
            "selected_s_beta_imported": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    ordered_scaffold = {
        "schema": "MTTEHUvOrderedQuotientScaffoldClause.v1",
        "status": "EHUV_ORDERED_QUOTIENT_SCAFFOLD_IMPORTED_C1_CLOSED_C2_OPEN",
        "closure_claimed": True,
        "validator_clause": "C1_branch_and_ordered_channel_labels",
        "validator_clause_closed": clause_closed(bridge, "C1_branch_and_ordered_channel_labels"),
        "closed_support": ordered["closed_support"],
        "ordered_channel_map": ordered["ordered_channel_map"],
        "ordered_label_ids_emitted": [
            "H7B1X:E_H_UV:ordered_label:H_u",
            "H7B1X:E_H_UV:ordered_label:H_d^dagger",
        ],
        "formal_quotient_scaffold": {
            "bundle_or_plane": "E_H^UV",
            "basis_labels": ordered["ordered_channel_map"]["E_H_UV_basis_labels"],
            "quotient": ordered["ordered_channel_map"]["quotient"],
            "low_energy_projection": ordered["ordered_channel_map"]["low_energy_projection"],
        },
        "not_promoted_to_section_basis": {
            "selected_E_H_UV_section_basis_emitted": h7b1x["selected_E_H_UV_section_basis_emitted"],
            "finite_section_source_ids_emitted": False,
            "section_basis_exactness_certificate_emitted": False,
            "reason": (
                "H7B1X closes ordered labels and the quotient scaffold only.  Its own "
                "payload request forbids treating ordered Hu/Hd labels as finite basis vectors."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    bridge_reduction = {
        "schema": "MTTSectionRingQuadratureBridgeReduction.v1",
        "status": "SECTIONRING_QUADRATURE_BRIDGE_REDUCED_TO_C2_C6",
        "closure_claimed": True,
        "bridge_validator_name": bridge["validator_name"],
        "h7b1w_bridge_criterion": trace_attempt["bridge_criterion"],
        "method_only_external_criterion": external["criterion_imported"],
        "validator_clauses": bridge["clauses"],
        "clause_status": {
            "C1_branch_and_ordered_channel_labels": clause_closed(
                bridge, "C1_branch_and_ordered_channel_labels"
            ),
            "C2_typed_E_H_UV_section_basis_or_finite_quotient": clause_closed(
                bridge, "C2_typed_E_H_UV_section_basis_or_finite_quotient"
            ),
            "C3_selected_HYM_metric_or_connection_fixed_point": clause_closed(
                bridge, "C3_selected_HYM_metric_or_connection_fixed_point"
            ),
            "C4_quadrature_weights_and_trace_normalization": clause_closed(
                bridge, "C4_quadrature_weights_and_trace_normalization"
            ),
            "C5_trace_to_H7B1U_grid_and_projection_measure_identity": clause_closed(
                bridge, "C5_trace_to_H7B1U_grid_and_projection_measure_identity"
            ),
            "C6_no_extra_boundary_or_source_term": clause_closed(
                bridge, "C6_no_extra_boundary_or_source_term"
            ),
        },
        "conditional_reduction_executed_not_selected": {
            "formula": reduction["conditional_local_formula"],
            "values": reduction["conditional_reduction_candidates_not_selected"],
            "replay_certificate": reduction["replay_certificate"],
            "selected_finite_reduction_policy_promoted": reduction["decision"][
                "selected_finite_reduction_policy_promoted"
            ],
            "selected_s_beta_promoted": reduction["decision"]["selected_s_beta_promoted"],
        },
        "h7b1w_missing_payload": trace_attempt["missing_payload"],
        "request_must_emit_next": request["must_emit_next"],
        "forbidden_promotions": request["forbidden_promotions"],
        "decision": {
            "bridge_validator_complete": bridge["decision"]["bridge_validator_complete"],
            "uniform_mean_can_be_promoted_now": bridge["decision"][
                "uniform_mean_can_be_promoted_now"
            ],
            "selected_s_beta_promoted": bridge["decision"]["selected_s_beta_promoted"],
            "finite_trace_HYM_binding_closed": trace_attempt["decision"][
                "finite_trace_HYM_binding_closed"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    direct_recheck = {
        "schema": "MTTDirectHerm2HuvPayloadRecheck.v1",
        "status": "DIRECT_HERM2_HUV_PAYLOAD_RECHECKED_VALUES_ABSENT",
        "closure_claimed": True,
        "actual_outputs": direct_attempt["actual_outputs"],
        "payload_requirements": direct_attempt["payload_requirements"],
        "decision": direct_attempt["decision"],
        "accepted_as_H_K_source_row": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hk_gate = {
        "schema": "MTTHKThresholdGateAfterSectionSourceAttempt.v1",
        "status": "H_K_THRESHOLD_GATE_RECHECKED_SECTION_SOURCE_OPEN",
        "closure_claimed": True,
        "required_output": "K_threshold.Omega_H.lambda",
        "source_equation": previous_hk["source_equation"],
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": {
            "ordered_quotient_scaffold_closed": True,
            "finite_section_source_ids_emitted": False,
            "section_basis_exactness_certificate_emitted": False,
            "selected_HYM_metric_or_connection_on_E_H_UV": False,
            "quadrature_weights_and_trace_normalization_emitted": False,
            "trace_to_H7B1U_grid_identity_emitted": False,
            "projection_measure_equality_emitted": False,
            "no_extra_boundary_source_term_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        },
        "conditional_consequent_current": {
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterEHUvSectionSourceAttempt.v1",
        "status": "NEXT_FRONTIER_HIGGS_HYM_SECTIONRING_BRIDGE_OR_DIRECT_HUV_PAYLOAD",
        "closure_claimed": True,
        "closed_here": [
            "late constants H7B1S/T/U/V/W/X sequence imported",
            "ordered E_H^UV label and quotient scaffold imported",
            "bridge validator C1 clause closed in the active SM H-row ledger",
            "H7B1W bridge criterion imported as the exact C2-C6 acceptance contract",
            "conditional finite reductions replayed only as diagnostics",
            "direct Herm2 Huv payload route rechecked with all values absent",
            "H K-threshold gate rechecked at 9/10",
        ],
        "still_open": [
            "C2 typed E_H^UV section basis or finite quotient basis",
            "C3 selected HYM or balanced metric/connection fixed point on E_H^UV",
            "C4 finite quadrature weights and trace normalization on that basis",
            "C5 trace-to-H7B1U grid identity and Higgs projection-measure equality",
            "C6 same-source no-extra-boundary/source theorem",
            "direct B_Huv+M_source or Huu,Hud,Hdd rows",
            "selected s_beta or equivalent H quartic/threshold functional",
            "K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedEHUvSectionSourceIdentityOrDirectHerm2HuvRowEmission",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "EHUvSectionSourceIdentityRouteExecutionTheorem",
            "proved": True,
            "statement": (
                "The active H-row target now imports the late H7B1S/T/U/V/W/X constants "
                "sequence.  Ordered E_H^UV labels and the quotient scaffold close the bridge "
                "validator C1 clause, but they do not emit finite section source IDs, a "
                "section exactness certificate, the E_H^UV HYM metric/projection measure, or "
                "direct Herm(2) Huv rows.  The remaining theorem is the full selected "
                "Higgs HYM section-ring/quadrature bridge C2-C6, or a direct Huv payload."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "late_H7B1_sequence_imported": True,
            "ordered_E_H_UV_quotient_scaffold_closed": True,
            "bridge_validator_C1_closed": True,
            "bridge_validator_C2_closed": False,
            "bridge_validator_C3_closed": False,
            "bridge_validator_C4_closed": False,
            "bridge_validator_C5_closed": False,
            "bridge_validator_C6_closed": False,
            "finite_section_source_ids_emitted": False,
            "section_basis_exactness_certificate_emitted": False,
            "selected_HYM_metric_or_connection_on_E_H_UV_emitted": False,
            "quadrature_weights_and_trace_normalization_emitted": False,
            "trace_to_H7B1U_grid_identity_emitted": False,
            "projection_measure_equality_emitted": False,
            "no_extra_boundary_source_term_for_Higgs_projection": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": previous_hk[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": previous_hk[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "late_h7b1_sequence_import": rel(CONST_IMPORT),
            "ehuv_ordered_quotient_scaffold_clause": rel(ORDERED_SCAFFOLD),
            "sectionring_quadrature_bridge_reduction": rel(BRIDGE_REDUCTION),
            "direct_herm2_huv_payload_recheck": rel(DIRECT_RECHECK),
            "hk_threshold_gate_after_section_source_attempt": rel(HK_GATE),
            "next_cutset_after_section_source_attempt": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedEHUvSectionSourceIdentityOrDirectHerm2HuvRowEmissionCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "late_H7B1_sequence_imported": True,
        "ordered_E_H_UV_quotient_scaffold_closed": True,
        "bridge_validator_C1_closed": True,
        "bridge_validator_C2_to_C6_closed": False,
        "finite_section_source_ids_emitted": False,
        "section_basis_exactness_certificate_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "selected_s_beta_value_found": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "accepted_internal_scalar_value_row_count": 0,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected EHUvSectionSourceIdentity or DirectHerm2HuvRowEmission v1

Status: `{STATUS}`

## What Closed

- imported constants H7B1S/T/U/V/W/X into the active SM H-row ledger
- closed the ordered `E_H^UV=span(H_u,H_d^dagger)` label/quotient scaffold
- closed bridge-validator C1: branch identity and ordered channel labels
- imported the H7B1W bridge criterion as the exact C2-C6 acceptance contract
- replayed conditional finite reductions only as diagnostics
- rechecked direct Herm(2) Huv payload: `false`
- H K-threshold gate remains: `{previous_hk["accepted_selected_K_source_row_count"]}/{previous_hk["selected_K_threshold_row_count_required"]}`

## Still Open

- C2 typed `E_H^UV` section basis or finite quotient basis
- C3 selected HYM/balanced metric or connection fixed point on `E_H^UV`
- C4 finite quadrature weights and trace normalization
- C5 trace-to-H7B1U grid identity and Higgs projection-measure equality
- C6 same-source no-extra-boundary/source theorem
- direct `B_Huv+M_source` or `Huu,Hud,Hdd` rows
- selected `s_beta` or equivalent H quartic/threshold functional
- selected `K_threshold.Omega_H.lambda`: `false`

Next required artifact: `{NEXT}`
"""

    write_json(CONST_IMPORT, constants_import)
    write_json(ORDERED_SCAFFOLD, ordered_scaffold)
    write_json(BRIDGE_REDUCTION, bridge_reduction)
    write_json(DIRECT_RECHECK, direct_recheck)
    write_json(HK_GATE, hk_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
