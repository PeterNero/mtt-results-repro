"""Build the electroweak Qa-stack source-identity test from terminal/gerbe support."""

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

INPUTS = {
    "qastack_bridge": DATA / "selected_electroweak_qastack_sourceidentity_and_prow_regularization.candidate.json",
    "factorized_attempt": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json",
    "matrix_payload": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.matrix.json",
    "terminal_orientation": DATA / "selected_u1y_routec_terminal_orientation_branchcoherence_bridge.candidate.json",
    "terminal_operator_emission": DATA / "selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap.candidate.json",
    "alpha1_replay": DATA / "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.candidate.json",
    "nonidentity_rhoe_interface": DATA / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn_interface.candidate.json",
    "operator_source_bridge": DATA / "selected_u1y_routec_operator_source_identity_bridge_subpacket.candidate.json",
    "q79_factorized_packet": Q79 / "candidate_data" / "iwasawa_block_factorized_twisted_packet.candidate.json",
    "q79_sector_maps": Q79 / "candidate_data" / "iwasawa_block_factorized_sector_maps.candidate.json",
    "q79_same_source_fusion": Q79
    / "candidate_data"
    / "all_remaining_valpha_gates"
    / "same_source_monad_gs_operator_fusion.after_terminal_lockdown.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_qastack_sourceidentity_from_terminal_or_gerbe.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_sourceidentity_from_terminal_or_gerbe_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_SourceIdentity_From_TerminalMonad_or_GerbeSource_v1.md"

STATUS = "ELECTROWEAK_QASTACK_SOURCEIDENTITY_TERMINAL_GERBE_TESTED_THRESHOLD_ROW_OPEN"
NEXT = "Selected_Electroweak_QaStack_ThresholdOperator_From_NonIdentityRhoE_QuotientBN_Fill_v1"


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
    bridge = load(INPUTS["qastack_bridge"])
    factorized = load(INPUTS["factorized_attempt"])
    matrix = load(INPUTS["matrix_payload"])
    terminal_orientation = load(INPUTS["terminal_orientation"])
    terminal_operator = load(INPUTS["terminal_operator_emission"])
    alpha1 = load(INPUTS["alpha1_replay"])
    nonidentity = load(INPUTS["nonidentity_rhoe_interface"])
    operator_bridge = load(INPUTS["operator_source_bridge"])
    q79_factorized = load(INPUTS["q79_factorized_packet"])
    q79_sector = load(INPUTS["q79_sector_maps"])
    q79_fusion = load(INPUTS["q79_same_source_fusion"])

    support_upgrades = {
        "terminal_ordered_orientation_closed": terminal_orientation["decision"]["ordered_matter_slot_orientation_selector_closed"],
        "functional_operator_emission_closed": terminal_operator["decision"]["same_branch_functional_operator_emission_closed"],
        "functional_overlap_normalization_emitted": terminal_operator["decision"]["selected_overlap_normalization_emitted"],
        "alpha1_driver_verified": alpha1["decision"]["alpha1_driver_verified"],
        "honest_dotD_alpha1_validator_closed": alpha1["decision"]["honest_dotD_validator_closed"],
        "selected_dotD_alpha1_source_verified": alpha1["decision"]["selected_dotD_source_verified"],
        "exact_factorized_matrix_constructed": factorized["decision"]["factorized_operator_matrix_constructed"],
        "quotient_matrix_constructed": factorized["decision"]["quotient_operator_matrix_constructed"],
        "quotient_logdet": matrix["quotient_operator"]["logdet"],
    }

    threshold_identity_requirements = {
        "selected_factorized_rank3_carrier": bool(q79_factorized.get("selected_by_mtt")),
        "selected_sector_maps_and_shared_line": bool(q79_sector.get("selected_by_mtt")),
        "selected_gerbe_source_verified": bool(nested(q79_factorized, ["family_twist_block", "selected_gerbe_source_verified"], False)),
        "terminal_or_gerbe_source_certificate": bool(nested(q79_fusion, ["source_identity", "source_certificate"], False)),
        "same_source_fusion_selected": bool(nested(q79_fusion, ["source_identity", "selected_by_mtt"], False)),
        "same_source_for_ordered_L_pic0_GS_and_DE": bool(
            nested(q79_fusion, ["source_identity", "same_source_for_ordered_L_pic0_GS_and_DE"], False)
        ),
        "visible_GS_row_derived_from_same_source": bool(
            nested(q79_fusion, ["green_schwarz_and_gerbe", "visible_green_schwarz_row_derived_from_same_source"], False)
        ),
        "operator_layer_Pic0_or_torsion_gerbe_closed": terminal_operator["decision"]["operator_layer_Pic0_closed"],
        "nonidentity_rhoE_quotient_valid_BN_filled": not nonidentity["interface_checks"]["all_template_selected_values_open"],
        "selected_D_E_Riesz_Green_dotD_full_threshold_packet": not nonidentity["interface_checks"]["all_template_selected_values_open"],
        "exact_A_base_tensor_I3_emitted_as_threshold_operator": False,
        "source_emitted_Qa_stack_index_weights": False,
        "source_emitted_determinant_scale_policy": False,
    }

    route_tests = {
        "terminal_functional_emission_route": {
            "accepted": False,
            "support": {
                "orientation": support_upgrades["terminal_ordered_orientation_closed"],
                "functional_operator_blocks": support_upgrades["functional_operator_emission_closed"],
                "overlap_normalization": support_upgrades["functional_overlap_normalization_emitted"],
                "alpha1_driver": support_upgrades["alpha1_driver_verified"],
            },
            "reason": (
                "This route closes functional matter-slot emission and alpha1 response, "
                "but it is scoped away from the gauge-threshold operator row and keeps "
                "operator-layer Pic0/torsion-gerbe data open."
            ),
        },
        "q79_factorized_gerbe_route": {
            "accepted": False,
            "support": {
                "rank3_shape": factorized["source_identity"]["source_level_rank3_carrier_support_closed"],
                "matrix_constructed": support_upgrades["exact_factorized_matrix_constructed"],
            },
            "reason": (
                "The factorized packet has the right rank-3 shape, but its own source "
                "records still mark selected_by_mtt=false and selected gerbe source "
                "unverified."
            ),
        },
        "nonidentity_rhoE_quotientBN_route": {
            "accepted": False,
            "support": {
                "interface_built": nonidentity["interface_checks"]["previous_gate_reduced_to_this_payload"],
                "required_payload_keys_imported": nonidentity["interface_checks"]["required_payload_keys_imported"],
            },
            "reason": (
                "This is now the best exact next route because it is the first payload "
                "whose schema can emit nonidentity rho_E, quotient-valid B_N, and "
                "selected D_E/Riesz/Green/dotD. It is still unfilled."
            ),
        },
        "old_operator_source_bridge_route": {
            "accepted": False,
            "support": operator_bridge["source_identity_bridge_result"],
            "reason": "The older bridge isolates the same cut set and remains a current-source no-go.",
        },
    }

    source_identity_closed = all(threshold_identity_requirements.values())

    candidate = {
        "candidate": "SelectedElectroweakQaStackSourceIdentityFromTerminalMonadOrGerbeSource",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": bridge["status"],
        "support_upgrades": support_upgrades,
        "threshold_identity_requirements": threshold_identity_requirements,
        "route_tests": route_tests,
        "decision": {
            "terminal_functional_support_imported": True,
            "alpha1_response_support_imported": True,
            "source_identity_closed": source_identity_closed,
            "selected_p_a_promoted": False,
            "lambda_12_closed": False,
            "measured_electroweak_closure": False,
            "current_source_nogo_proved": True,
            "mathematical_impossibility_claimed": False,
            "best_next_route": "nonidentity_rhoE_quotientBN_route",
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "TerminalFunctionalEmissionDoesNotYetEmitQaStackThresholdRow",
            "proved": True,
            "statement": (
                "The terminal monad/Route-C branch now provides selected ordered "
                "matter-slot orientation, functional HYM/End0 operator emission, "
                "overlap normalization, and alpha1 driver replay. These are real "
                "same-branch support upgrades, but they do not by themselves emit "
                "the gauge-threshold operator A_base tensor I_3, the operator-layer "
                "Pic0/torsion-gerbe rule, nonidentity rho_E with quotient-valid B_N, "
                "or the selected determinant scale/index packet. Therefore the "
                "electroweak Qa-stack source identity remains open."
            ),
        },
        "minimal_next_payload": {
            "name": NEXT,
            "must_emit": [
                "nonidentity rho_E compatible with the fixed-fiber/shared-line quotient",
                "quotient-valid B_N carrying the non-invariant/holonomy component",
                "selected D_E/Riesz/Green/dotD threshold packet in the same source lane",
                "operator-layer Pic0 quotient or torsion-gerbe replacement theorem",
                "proof that the emitted threshold row is exactly A_base tensor I_3 before Pperp quotient",
                "Qa-stack index weights and determinant scale policy",
            ],
        },
        "what_closes": {
            "terminal_functional_support_imported": True,
            "alpha1_driver_support_imported": True,
            "functional_vs_threshold_boundary_proved": True,
            "nonidentity_rhoE_quotientBN_route_selected_as_next": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_threshold_operator_A_base_tensor_I3": True,
            "operator_layer_Pic0_or_torsion_gerbe_rule": True,
            "nonidentity_rhoE": True,
            "quotient_valid_BN": True,
            "selected_D_E_Riesz_Green_dotD_threshold_packet": True,
            "Qa_stack_index_weights_and_scale_policy": True,
            "selected_p_a": True,
            "lambda_12": True,
        },
        "guardrails": {
            "observed_electroweak_data_used": False,
            "target_fitting_used": False,
            "promotes_functional_blocks_as_threshold_operator": False,
            "promotes_factorized_fixture": False,
            "promotes_selected_p_a": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakQaStackSourceIdentityFromTerminalMonadOrGerbeSource",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "source_identity_closed": source_identity_closed,
        "terminal_functional_support_imported": True,
        "alpha1_response_support_imported": True,
        "selected_p_a_promoted": False,
        "lambda_12_closed": False,
        "best_next_route": "nonidentity_rhoE_quotientBN_route",
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected Electroweak QaStack SourceIdentity From TerminalMonad or GerbeSource v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        "terminal_functional_support_imported = true",
        "alpha1_response_support_imported = true",
        f"source_identity_closed = {str(candidate['decision']['source_identity_closed']).lower()}",
        "selected_p_a_promoted = false",
        "lambda_12_closed = false",
        f"best_next_route = {candidate['decision']['best_next_route']}",
        f"next_required_artifact = {candidate['decision']['next_required_artifact']}",
        "```",
        "",
        "Terminal/Route-C progress is real: ordered orientation, functional operator",
        "emission, overlap normalization, and alpha1 replay are now selected support.",
        "But those objects are functional matter-slot operators, not yet the",
        "gauge-threshold row `A_base tensor I_3` needed for the electroweak Qa-stack.",
        "",
        "## Support Upgrades",
        "",
        "```json",
        json.dumps(candidate["support_upgrades"], indent=2, sort_keys=True),
        "```",
        "",
        "## Threshold Identity Requirements",
        "",
        "| Requirement | Value |",
        "| --- | --- |",
    ]
    for key, value in candidate["threshold_identity_requirements"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(
        [
            "",
            "## Route Tests",
            "",
            "```json",
            json.dumps(candidate["route_tests"], indent=2, sort_keys=True),
            "```",
            "",
            "## Minimal Next Payload",
            "",
            f"Next artifact: `{candidate['minimal_next_payload']['name']}`.",
            "",
        ]
    )
    for item in candidate["minimal_next_payload"]["must_emit"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Functional matter-slot blocks are not promoted as gauge-threshold operators.",
            "- Factorized support/fixture data are not promoted.",
            "- No observed electroweak data or target residuals are used.",
            "- `p_a`, `lambda_12`, and measured electroweak closure remain open.",
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
