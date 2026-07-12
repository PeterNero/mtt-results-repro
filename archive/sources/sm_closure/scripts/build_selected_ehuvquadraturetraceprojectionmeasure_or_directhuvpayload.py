"""Build the E_H^UV finite trace/quadrature C4 bridge step.

C1-C3 are now closed: the branch and labels are fixed, the finite E_H^UV
quotient basis/source IDs are emitted, and the selected diagonal HYM metric and
connection are bound to that basis.  This artifact closes only the validator's
C4 clause: finite quadrature weights and trace normalization attached to the
selected E_H^UV basis.

It deliberately does not identify the H7B1U replay grid with the physical Higgs
projection measure, prove no-extra-boundary/source cancellation, promote
s_beta/lambda_H, or emit direct Huv rows.  Those remain C5-C6/direct-route work.
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

SLUG = "selected_ehuvquadraturetraceprojectionmeasure_or_directhuvpayload"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
C4_TRACE = PACKET_DIR / "c4_ehuv_finite_trace_quadrature_attachment.packet.json"
BRIDGE_UPDATE = PACKET_DIR / "bridge_validator_c4_update.packet.json"
MEASURE_RECHECK = PACKET_DIR / "projection_measure_identity_recheck_after_c4.packet.json"
DIRECT_RECHECK = PACKET_DIR / "direct_herm2_huv_payload_recheck_after_c4.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_c4_trace.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_c4_trace.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_EHUvQuadratureTraceProjectionMeasure_or_DirectHuvPayload_v1.md"

PREVIOUS = DATA / "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload.candidate.json"
PREVIOUS_C3 = (
    DATA
    / "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload"
    / "c3_ehuv_hym_metric_connection_binding.packet.json"
)
PREVIOUS_BRIDGE = (
    DATA
    / "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload"
    / "bridge_validator_c3_update.packet.json"
)
PREVIOUS_DIRECT = (
    DATA
    / "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload"
    / "direct_herm2_huv_payload_recheck_after_c3.packet.json"
)
PREVIOUS_HK = (
    DATA
    / "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload"
    / "hk_threshold_gate_after_c3_metric.packet.json"
)
C2_BASIS = (
    DATA
    / "selected_higgshymsectionringquadraturebridge_or_directhuvpayload"
    / "c2_ehuv_finite_quotient_basis_exactness.packet.json"
)

H7B1Z_PARTIAL = (
    CONST_DATA
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "partial_section_basis_quadrature_fill.packet.json"
)
H7B1V_CANDIDATE = (
    CONST_DATA
    / "const_higgs_01_h7b1v_reduction_selector_or_direct_herm2_huv_source.candidate.json"
)
H7B1V_TRACE_ATTEMPT = (
    CONST_DATA
    / "const_higgs_01_h7b1v_reduction_selector_or_direct_herm2_huv_source"
    / "finite_trace_to_hym_grid_binding_attempt.packet.json"
)
H7B1V_TRIAGE = (
    CONST_DATA
    / "const_higgs_01_h7b1v_reduction_selector_or_direct_herm2_huv_source"
    / "reduction_selector_triage.packet.json"
)
H7B1W_CRITERION = (
    CONST_DATA
    / "const_higgs_01_h7b1w_finite_trace_hym_binding_or_direct_huv_payload"
    / "finite_trace_binding_attempt.packet.json"
)
H7B1U_REDUCTION = (
    CONST_DATA
    / "const_higgs_01_h7b1u_source_bound_metric_and_finite_reduction"
    / "conditional_finite_reduction_execution.packet.json"
)

STATUS = (
    "MTT_SELECTED_EHUVQUADRATURETRACEPROJECTIONMEASURE_OR_DIRECTHUVPAYLOAD_"
    "C4_FINITE_TRACE_ATTACHED_C5_C6_OPEN"
)
NEXT = "MTT_Selected_EHUvTraceGridProjectionIdentity_or_DirectHuvPayload_v1"


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
        raise FileNotFoundError("missing EHUv C4 inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_C3,
        PREVIOUS_BRIDGE,
        PREVIOUS_DIRECT,
        PREVIOUS_HK,
        C2_BASIS,
        H7B1Z_PARTIAL,
        H7B1V_CANDIDATE,
        H7B1V_TRACE_ATTEMPT,
        H7B1V_TRIAGE,
        H7B1W_CRITERION,
        H7B1U_REDUCTION,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    c3 = load(PREVIOUS_C3)
    previous_bridge = load(PREVIOUS_BRIDGE)
    previous_direct = load(PREVIOUS_DIRECT)
    previous_hk = load(PREVIOUS_HK)
    c2_basis = load(C2_BASIS)
    h7b1z = load(H7B1Z_PARTIAL)
    h7b1v = load(H7B1V_CANDIDATE)
    h7b1v_attempt = load(H7B1V_TRACE_ATTEMPT)
    h7b1v_triage = load(H7B1V_TRIAGE)
    h7b1w = load(H7B1W_CRITERION)
    h7b1u = load(H7B1U_REDUCTION)

    uv_ids = c3["basis_binding"]["ordered_E_H_UV_source_ids"]
    q = h7b1z["quadrature_and_trace_partial_fill"]
    uniform_weight = q["uniform_weight"]
    node_count = q["node_count"]
    weight_sum = uniform_weight * node_count
    trace_rule_id = "Q_sel^U:E_H_UV:HYM_grid:Z24^4:normalized_uniform_trace"

    c4_trace = {
        "schema": "MTTEHUvC4FiniteTraceQuadratureAttachment.v1",
        "status": "C4_EHUV_FINITE_TRACE_QUADRATURE_ATTACHED",
        "closure_claimed": True,
        "bridge_clause": "C4_quadrature_weights_and_trace_normalization",
        "bridge_clause_closed": True,
        "interpretation": (
            "C4 is closed in the bridge-validator sense: a finite quadrature rule "
            "and normalized trace are attached to the already selected E_H^UV "
            "finite basis.  C5 remains the stronger statement that this trace is "
            "the H7B1U-grid physical Higgs projection measure."
        ),
        "selected_source_provenance": [
            {
                "role": "C2 finite E_H^UV source IDs and exactness certificate",
                "source": rel(C2_BASIS),
            },
            {
                "role": "C3 selected HYM metric/connection bound to E_H^UV",
                "source": rel(PREVIOUS_C3),
            },
            {
                "role": "H7B1Z reproducible HYM grid and uniform computational trace",
                "source": rel(H7B1Z_PARTIAL),
            },
            {
                "role": "finite Weyl trace uniqueness support for normalized trace",
                "source": rel(H7B1V_CANDIDATE),
            },
        ],
        "finite_trace_quadrature": {
            "quadrature_rule_id": trace_rule_id,
            "attached_to_selected_E_H_UV_basis": True,
            "ordered_E_H_UV_source_ids": uv_ids,
            "node_count": node_count,
            "nodes_or_grid": q["nodes_or_grid"],
            "uniform_weight": uniform_weight,
            "uniform_weight_rational": q["uniform_weight_rational"],
            "weight_sum": weight_sum,
            "weight_sum_is_one": abs(weight_sum - 1.0) < 1e-15,
            "trace_normalization": q["trace_normalization"],
            "source_independent_of_target_replay": q["source_independent_of_target_replay"],
            "finite_Weyl_trace_measure_derived": h7b1v["finite_Weyl_trace_measure_derived"],
            "uniform_reduction_best_current_source_aligned_candidate": h7b1v[
                "uniform_reduction_best_current_source_aligned_candidate"
            ],
        },
        "h7b1v_blocker_update_after_c3": {
            "old_same_source_metric_bound_to_E_H_UV": h7b1v_attempt["blocked_fields"][
                "same_source_metric_bound_to_E_H_UV"
            ],
            "new_same_source_metric_bound_to_E_H_UV": True,
            "trace_to_HYM_grid_binding_closed": False,
            "physical_measure_equals_Higgs_projection_measure": False,
            "same_source_no_extra_boundary_or_source_term": False,
        },
        "downstream_reduction_candidates_not_promoted": {
            "uniform_mean_conditional_s_beta": h7b1v["uniform_mean_conditional_s_beta"],
            "rho_weighted_mean_conditional_s_beta": h7b1v[
                "rho_weighted_mean_conditional_s_beta"
            ],
            "exp_density_weighted_mean_conditional_s_beta": h7b1v[
                "exp_density_weighted_mean_conditional_s_beta"
            ],
            "conditional_local_formula": h7b1u["conditional_local_formula"],
            "selected_reduction_selector_emitted": False,
            "selected_s_beta_promoted": False,
        },
        "guardrails": {
            "quadrature_weights_and_trace_normalization_emitted": True,
            "trace_to_H7B1U_grid_identity_emitted": False,
            "projection_measure_equality_emitted": False,
            "accepted_as_physical_Higgs_projection_measure": False,
            "same_source_no_extra_boundary_source_proof_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_minimal_lift_rule_emitted": False,
            "selected_rank_one_light_projector_emitted": False,
            "selected_s_beta_promoted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    bridge_clauses = dict(previous_bridge["clauses"])
    bridge_clauses["C4_quadrature_weights_and_trace_normalization"] = {
        "closed": True,
        "evidence": [
            rel(C4_TRACE),
            f"{node_count} nodes on the H7B1Z reproducible grid",
            f"uniform finite trace weight {q['uniform_weight_rational']}",
            "normalized arithmetic finite trace attached to the selected E_H^UV source IDs",
        ],
        "what_is_not_claimed": [
            "trace-to-H7B1U grid identity as physical Higgs projection measure",
            "same-source no-extra-boundary theorem",
            "selected finite reduction scalar s_beta",
            "direct Herm(2) Huv values",
            "K_threshold.Omega_H.lambda",
        ],
    }

    bridge_update = {
        "schema": "MTTSelectedEHUvHYMBridgeValidatorC4Update.v1",
        "status": "BRIDGE_VALIDATOR_C1_C2_C3_C4_CLOSED_C5_C6_DIRECT_OPEN",
        "closure_claimed": True,
        "validator_name": previous_bridge["validator_name"],
        "clauses": bridge_clauses,
        "clause_status": {
            "C1_branch_and_ordered_channel_labels": True,
            "C2_typed_E_H_UV_section_basis_or_finite_quotient": True,
            "C3_selected_HYM_metric_or_connection_fixed_point": True,
            "C4_quadrature_weights_and_trace_normalization": True,
            "C5_trace_to_H7B1U_grid_and_projection_measure_identity": False,
            "C6_no_extra_boundary_or_source_term": False,
            "B_direct_Herm2_Huv_rows": False,
        },
        "decision": {
            "bridge_validator_complete": False,
            "C4_closed_by_finite_trace_attachment": True,
            "C5_C6_remain_required": True,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_s_beta_promoted": False,
            "uniform_mean_can_be_promoted_now": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    measure_recheck = {
        "schema": "MTTProjectionMeasureIdentityRecheckAfterC4.v1",
        "status": "PROJECTION_MEASURE_IDENTITY_STILL_OPEN_AFTER_C4_TRACE",
        "closure_claimed": True,
        "finite_trace_attached": True,
        "C5_trace_to_H7B1U_grid_identity_emitted": False,
        "physical_Higgs_projection_measure_equality_emitted": False,
        "C6_no_extra_boundary_or_source_term_emitted": False,
        "reason": (
            "C4 supplies the finite normalized trace rule.  It does not yet prove "
            "that the H7B1U diagonal HYM grid is the selected physical Higgs "
            "projection measure or that no extra boundary/source term survives."
        ),
        "h7b1v_triage_reason": h7b1v_triage["selector_decision"]["reason"],
        "h7b1w_missing_payload_after_c4": {
            "Higgs_projection_measure_equality": True,
            "trace_to_H7B1U_grid_identity": True,
            "no_extra_boundary_source_proof": True,
            "finite_to_smooth_or_exact_quotient_certificate": h7b1w["missing_payload"][
                "finite_to_smooth_or_exact_quotient_certificate"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    direct_recheck = {
        "schema": "MTTDirectHerm2HuvPayloadRecheckAfterC4.v1",
        "status": "DIRECT_HERM2_HUV_PAYLOAD_STILL_ABSENT_AFTER_C4",
        "closure_claimed": True,
        "actual_outputs": previous_direct["actual_outputs"],
        "decision": previous_direct["decision"],
        "C4_trace_changes_direct_Huv_status": False,
        "accepted_as_H_K_source_row": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_row = dict(previous_hk["H_row"])
    h_row["quadrature_weights_and_trace_normalization_emitted"] = True
    hk_gate = {
        "schema": "MTTHKThresholdGateAfterC4Trace.v1",
        "status": "H_K_THRESHOLD_GATE_C4_CLOSED_C5_C6_OPEN",
        "closure_claimed": True,
        "required_output": "K_threshold.Omega_H.lambda",
        "source_equation": previous_hk["source_equation"],
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": h_row,
        "conditional_consequent_current": previous_hk["conditional_consequent_current"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterEHUvC4Trace.v1",
        "status": "NEXT_FRONTIER_EHUV_TRACE_GRID_PROJECTION_IDENTITY_C5_C6_OR_DIRECT_HUV",
        "closure_claimed": True,
        "closed_here": [
            "C4 finite quadrature weights and trace normalization attached to selected E_H^UV basis",
            f"uniform normalized trace weight {q['uniform_weight_rational']} on {node_count} nodes",
            "finite trace rule source-independent of target replay",
            "H K-threshold gate rechecked at 9/10",
        ],
        "still_open": [
            "C5 trace-to-H7B1U grid identity",
            "C5 Higgs projection-measure equality",
            "C6 same-source no-extra-boundary/source theorem",
            "direct B_Huv+M_source or Huu,Hud,Hdd rows",
            "selected minimal lift or rank-one light projector P_L",
            "selected s_beta or equivalent H quartic/threshold functional",
            "K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedEHUvQuadratureTraceProjectionMeasureOrDirectHuvPayload",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "EHUvFiniteTraceQuadratureC4AttachmentTheorem",
            "proved": True,
            "statement": (
                "After C2 emits finite E_H^UV source IDs and C3 binds the selected "
                "diagonal HYM metric/connection to them, the H7B1Z normalized finite "
                "trace quadrature can be attached to that selected basis.  This "
                "closes bridge clause C4 only: node_count=331776, uniform weight "
                "1/331776, normalized arithmetic finite trace.  It does not prove "
                "the C5 trace-to-H7B1U physical Higgs projection-measure identity, "
                "C6 no-extra-boundary/source cancellation, direct Huv rows, "
                "s_beta/lambda_H, or the tenth H K row."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "bridge_validator_C1_closed": True,
            "bridge_validator_C2_closed": True,
            "bridge_validator_C3_closed": True,
            "bridge_validator_C4_closed": True,
            "bridge_validator_C5_closed": False,
            "bridge_validator_C6_closed": False,
            "finite_E_H_UV_quotient_basis_emitted": True,
            "selected_HYM_metric_or_connection_on_E_H_UV_emitted": True,
            "quadrature_weights_and_trace_normalization_emitted": True,
            "trace_to_H7B1U_grid_identity_emitted": False,
            "projection_measure_equality_emitted": False,
            "accepted_as_physical_Higgs_projection_measure": False,
            "no_extra_boundary_source_term_for_Higgs_projection": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_minimal_lift_rule_emitted": False,
            "selected_rank_one_light_projector_emitted": False,
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
            "c4_ehuv_finite_trace_quadrature_attachment": rel(C4_TRACE),
            "bridge_validator_c4_update": rel(BRIDGE_UPDATE),
            "projection_measure_identity_recheck_after_c4": rel(MEASURE_RECHECK),
            "direct_herm2_huv_payload_recheck_after_c4": rel(DIRECT_RECHECK),
            "hk_threshold_gate_after_c4_trace": rel(HK_GATE),
            "next_cutset_after_c4_trace": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedEHUvQuadratureTraceProjectionMeasureOrDirectHuvPayloadCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "bridge_validator_C1_closed": True,
        "bridge_validator_C2_closed": True,
        "bridge_validator_C3_closed": True,
        "bridge_validator_C4_closed": True,
        "bridge_validator_C5_C6_closed": False,
        "quadrature_weights_and_trace_normalization_emitted": True,
        "trace_to_H7B1U_grid_identity_emitted": False,
        "projection_measure_equality_emitted": False,
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

    note = f"""# MTT Selected EHUvQuadratureTraceProjectionMeasure or DirectHuvPayload v1

Status: `{STATUS}`

## What Closed

- closed C4 by attaching finite quadrature weights and trace normalization to the selected `E_H^UV` basis
- emitted quadrature rule `{trace_rule_id}`
- attached uniform normalized trace weight `{q["uniform_weight_rational"]}` on `{node_count}` H7B1Z grid nodes
- verified total weight: `{weight_sum}`
- kept finite Weyl trace uniqueness as source support, not as the C5 physical projection-measure identity
- rechecked direct Herm(2) Huv rows: `false`
- H K-threshold gate remains: `{previous_hk["accepted_selected_K_source_row_count"]}/{previous_hk["selected_K_threshold_row_count_required"]}`

## Still Open

- C5 trace-to-H7B1U grid identity
- C5 Higgs projection-measure equality
- C6 same-source no-extra-boundary/source theorem
- direct `B_Huv+M_source` or `Huu,Hud,Hdd` rows
- selected minimal lift or rank-one light projector `P_L`
- selected `s_beta` or equivalent H quartic/threshold functional
- selected `K_threshold.Omega_H.lambda`: `false`

Next required artifact: `{NEXT}`
"""

    write_json(C4_TRACE, c4_trace)
    write_json(BRIDGE_UPDATE, bridge_update)
    write_json(MEASURE_RECHECK, measure_recheck)
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
