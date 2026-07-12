"""Build the electroweak Qa-stack source-identity and p-row regularization subpacket."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

INPUTS = {
    "source_payload_fill": DATA / "selected_electroweak_qastack_or_u1yrow_source_payload_fill.candidate.json",
    "factorized_attempt": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json",
    "matrix_payload": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.matrix.json",
    "quotient_lemma": DATA / "selected_electroweak_u1y_quotientdeterminant_lemma.candidate.json",
    "local_det_interface": NONSM / "certificates" / "selected_local_determinant_computation_interface_certificate.json",
    "typed_hypercharge_gate": DATA / "selected_electroweak_u1y_hypercharge_weights_typed_convention_gate.candidate.json",
    "q79_factorized_packet": Q79 / "candidate_data" / "iwasawa_block_factorized_twisted_packet.candidate.json",
    "q79_sector_maps": Q79 / "candidate_data" / "iwasawa_block_factorized_sector_maps.candidate.json",
    "q79_same_source_fusion": Q79
    / "candidate_data"
    / "all_remaining_valpha_gates"
    / "same_source_monad_gs_operator_fusion.after_terminal_lockdown.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_qastack_sourceidentity_and_prow_regularization.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_sourceidentity_and_prow_regularization_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_SourceIdentity_and_pRowRegularization_Subpacket_v1.md"

STATUS = "ELECTROWEAK_QASTACK_SOURCEIDENTITY_OPEN_PROW_REGULARIZATION_CONDITIONAL_BRIDGE_BUILT"
NEXT = "Selected_Electroweak_QaStack_SourceIdentity_From_TerminalMonad_or_GerbeSource_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def nested(data: dict[str, Any], path: list[str], default: Any = None) -> Any:
    cur: Any = data
    for key in path:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    fill = load(INPUTS["source_payload_fill"])
    factorized = load(INPUTS["factorized_attempt"])
    matrix = load(INPUTS["matrix_payload"])
    quotient = load(INPUTS["quotient_lemma"])
    local_det = load(INPUTS["local_det_interface"])
    hypercharge = load(INPUTS["typed_hypercharge_gate"])
    q79_factorized = load(INPUTS["q79_factorized_packet"])
    q79_sector = load(INPUTS["q79_sector_maps"])
    q79_fusion = load(INPUTS["q79_same_source_fusion"])

    quotient_logdet = matrix["quotient_operator"]["logdet"]
    conditional_route = hypercharge["route_tests"]["Qa_stack_interpretation_of_quotient_operator"]

    source_identity_checks = {
        "exact_A_base_tensor_I3_matrix_constructed": factorized["decision"]["factorized_operator_matrix_constructed"],
        "quotient_matrix_constructed": factorized["decision"]["quotient_operator_matrix_constructed"],
        "same_source_as_27mode_DE_gap_layer": factorized["source_identity"]["same_source_as_27mode_DE_gap_layer"],
        "same_source_as_Pperp_trace_policy": factorized["source_identity"]["same_source_as_Pperp_trace_policy"],
        "rank3_carrier_support_closed": factorized["source_identity"]["source_level_rank3_carrier_support_closed"],
        "q79_factorized_selected_by_mtt": bool(q79_factorized.get("selected_by_mtt")),
        "q79_sector_maps_selected_by_mtt": bool(q79_sector.get("selected_by_mtt")),
        "q79_selected_gerbe_source_verified": bool(nested(q79_factorized, ["family_twist_block", "selected_gerbe_source_verified"], False)),
        "q79_fusion_selected_by_mtt": bool(nested(q79_fusion, ["source_identity", "selected_by_mtt"], False)),
        "q79_fusion_fixture_only": bool(nested(q79_fusion, ["source_identity", "fixture_only"], False)),
        "same_source_for_ordered_L_pic0_GS_and_DE": bool(
            nested(q79_fusion, ["source_identity", "same_source_for_ordered_L_pic0_GS_and_DE"], False)
        ),
        "visible_GS_row_derived_from_same_source": bool(
            nested(q79_fusion, ["green_schwarz_and_gerbe", "visible_green_schwarz_row_derived_from_same_source"], False)
        ),
        "DE_operator_response_pass": bool(nested(q79_fusion, ["operator_response", "de_action_pass"], False)),
        "reduced_green_pass": bool(nested(q79_fusion, ["operator_response", "reduced_green_pass"], False)),
        "dotd_response_pass": bool(nested(q79_fusion, ["operator_response", "dotd_response_pass"], False)),
    }
    source_identity_closed = all(
        source_identity_checks[key]
        for key in [
            "exact_A_base_tensor_I3_matrix_constructed",
            "quotient_matrix_constructed",
            "same_source_as_27mode_DE_gap_layer",
            "same_source_as_Pperp_trace_policy",
            "rank3_carrier_support_closed",
            "q79_factorized_selected_by_mtt",
            "q79_sector_maps_selected_by_mtt",
            "q79_selected_gerbe_source_verified",
            "q79_fusion_selected_by_mtt",
            "same_source_for_ordered_L_pic0_GS_and_DE",
            "visible_GS_row_derived_from_same_source",
            "DE_operator_response_pass",
            "reduced_green_pass",
            "dotd_response_pass",
        ]
    )

    regularization_bridge = {
        "conditional_bridge_proved": True,
        "bridge_condition": "selected source identity emits the exact quotient positive spectrum as the Qa-stack threshold row",
        "uses_local_det_formula": local_det["formula"]["per_factor"],
        "uses_quotient_regularization": quotient["functional_components_after_lemma"]["regularization_finite_part"],
        "finite_positive_spectrum": quotient["quotient_positive_spectrum"],
        "index_weights_required_from_source": "unit Qa-stack threshold weights or source-emitted replacements",
        "scale_policy_required_from_source": "mu=1 in selected internal determinant units or an explicitly selected mu-shift/cancellation theorem",
        "conditional_p_a": quotient_logdet,
        "conditional_p_Y": conditional_route["conditional_p_Y"],
        "conditional_lambda12": conditional_route["conditional_lambda_12"],
        "promotes_p_a_now": False,
        "reason_not_promoted": "The local determinant interface is closed, but selected spectra, index weights, and scale policy are still physics inputs supplied by source identity.",
    }

    candidate = {
        "candidate": "SelectedElectroweakQaStackSourceIdentityAndPRowRegularization",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_fill_status": fill["status"],
        "source_identity_checks": source_identity_checks,
        "regularization_bridge": regularization_bridge,
        "decision": {
            "source_identity_closed": source_identity_closed,
            "p_row_regularization_bridge_conditional_closed": True,
            "selected_p_a_promoted": False,
            "lambda_12_closed": False,
            "measured_electroweak_closure": False,
            "current_source_nogo_proved": True,
            "mathematical_impossibility_claimed": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "QaStackPRowRegularizationConditionalBridge",
            "proved": True,
            "statement": (
                "If a selected same-branch source emits the exact A_base tensor I_3 "
                "threshold operator, its shared-line quotient, unit or source-specified "
                "Qa-stack index weights, and the selected internal determinant scale, "
                "then the finite positive zeta/logdet quotient lemma and local determinant "
                "interface identify p_a with the quotient logdet. The present corpus has "
                "the algebraic bridge but not the selected source identity, so p_a and "
                "lambda_12 remain unpromoted."
            ),
        },
        "minimal_source_identity_payload": {
            "name": NEXT,
            "must_emit": [
                "selected_by_mtt=true for the factorized rank-3 carrier",
                "selected_by_mtt=true for sector maps and the shared central line basis",
                "selected gerbe/terminal source certificate rather than fixture support",
                "same-source bridge from ordered terminal monad/Pic0/GS data to the exact threshold operator",
                "D_E/Riesz/Green/dotD operator-response pass in the same source lane",
                "source-specified Qa-stack index weights and determinant scale policy",
            ],
        },
        "what_closes": {
            "conditional_p_row_regularization_bridge": True,
            "source_identity_gap_localized": True,
            "direct_regularization_mystery_retired": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_source_identity_for_A_base_tensor_I3": True,
            "selected_factorized_carrier": True,
            "selected_sector_maps_and_shared_line": True,
            "same_source_terminal_or_gerbe_certificate": True,
            "source_emitted_index_weights_and_scale": True,
            "selected_p_a": True,
            "lambda_12": True,
            "measured_electroweak_closure": True,
        },
        "guardrails": {
            "observed_electroweak_data_used": False,
            "target_fitting_used": False,
            "promotes_conditional_p_a": False,
            "promotes_lambda12": False,
            "promotes_fixture_support": False,
            "claims_measured_electroweak_closure": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakQaStackSourceIdentityAndPRowRegularization",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "source_identity_closed": source_identity_closed,
        "p_row_regularization_bridge_conditional_closed": True,
        "selected_p_a_promoted": False,
        "conditional_p_a": quotient_logdet,
        "conditional_lambda12": conditional_route["conditional_lambda_12"],
        "next_required_artifact": NEXT,
        "lambda_12_closed": False,
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected Electroweak QaStack SourceIdentity and pRowRegularization Subpacket v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"source_identity_closed = {str(candidate['decision']['source_identity_closed']).lower()}",
        "p_row_regularization_bridge_conditional_closed = true",
        "selected_p_a_promoted = false",
        "lambda_12_closed = false",
        f"next_required_artifact = {candidate['decision']['next_required_artifact']}",
        "```",
        "",
        "The p-row regularization problem splits cleanly from the source-identity",
        "problem. Once a selected source emits the exact quotient positive spectrum",
        "with Qa-stack weights and internal determinant scale, the finite quotient",
        "zeta/logdet lemma plugs into the local determinant interface. That is a",
        "conditional bridge, not a promotion.",
        "",
        "## Source Identity Checks",
        "",
        "| Check | Value |",
        "| --- | --- |",
    ]
    for key, value in candidate["source_identity_checks"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(
        [
            "",
            "## Conditional Regularization Bridge",
            "",
            "```json",
            json.dumps(candidate["regularization_bridge"], indent=2, sort_keys=True),
            "```",
            "",
            "## Minimal Source Identity Payload",
            "",
            f"Next artifact: `{candidate['minimal_source_identity_payload']['name']}`.",
            "",
        ]
    )
    for item in candidate["minimal_source_identity_payload"]["must_emit"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- No observed electroweak data or target residuals are used.",
            "- The conditional `p_a` value is not promoted.",
            "- Fixture/support packets are not promoted.",
            "- `lambda_12` and measured electroweak closure remain open.",
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
    DATA.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    PROOF.mkdir(parents=True, exist_ok=True)
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
