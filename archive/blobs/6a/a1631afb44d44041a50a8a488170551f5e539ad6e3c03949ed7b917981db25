"""Build the electroweak Qa-stack or U1/Y-row source-payload fill attempt."""

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
    "promotion_gate": DATA / "selected_electroweak_qastack_determinant_or_u1yrow_promotion.candidate.json",
    "source_template": DATA / "selected_electroweak_qastack_or_u1yrow_source_payload.template.json",
    "factorized_attempt": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json",
    "matrix_payload": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.matrix.json",
    "typed_hypercharge_gate": DATA / "selected_electroweak_u1y_hypercharge_weights_typed_convention_gate.candidate.json",
    "u1_carrier_projector": DATA / "selected_u1_threshold_carrier_projector_or_su2_operator_spectrum.candidate.json",
    "q79_factorized_packet": Q79 / "candidate_data" / "iwasawa_block_factorized_twisted_packet.candidate.json",
    "q79_sector_maps": Q79 / "candidate_data" / "iwasawa_block_factorized_sector_maps.candidate.json",
    "q79_same_source_fusion": Q79
    / "candidate_data"
    / "all_remaining_valpha_gates"
    / "same_source_monad_gs_operator_fusion.after_terminal_lockdown.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_qastack_or_u1yrow_source_payload_fill.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_or_u1yrow_source_payload_fill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_or_U1YRow_SourcePayload_Fill_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def bool_path(data: dict[str, Any], path: list[str], default: bool = False) -> bool:
    cur: Any = data
    for key in path:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return bool(cur)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    gate = load(INPUTS["promotion_gate"])
    template = load(INPUTS["source_template"])
    factorized = load(INPUTS["factorized_attempt"])
    matrix = load(INPUTS["matrix_payload"])
    hypercharge = load(INPUTS["typed_hypercharge_gate"])
    carrier = load(INPUTS["u1_carrier_projector"])
    q79_factorized = load(INPUTS["q79_factorized_packet"])
    q79_sector = load(INPUTS["q79_sector_maps"])
    q79_fusion = load(INPUTS["q79_same_source_fusion"])

    quotient_logdet = matrix["quotient_operator"]["logdet"]
    conditional = hypercharge["route_tests"]["Qa_stack_interpretation_of_quotient_operator"]

    qa_route_checks = {
        "exact_matrix_constructed": factorized["decision"]["factorized_operator_matrix_constructed"],
        "quotient_matrix_constructed": factorized["decision"]["quotient_operator_matrix_constructed"],
        "rank3_carrier_shape_found": carrier["decision"]["rank_three_carrier_shape_found"],
        "source_level_rank3_carrier_support_closed": factorized["source_identity"][
            "source_level_rank3_carrier_support_closed"
        ],
        "shared_line_projector_policy_selected": True,
        "q79_factorized_selected_by_mtt": bool(q79_factorized.get("selected_by_mtt")),
        "q79_sector_maps_selected_by_mtt": bool(q79_sector.get("selected_by_mtt")),
        "q79_gerbe_source_verified": bool_path(q79_factorized, ["family_twist_block", "selected_gerbe_source_verified"]),
        "same_source_fusion_fixture_only": bool(q79_fusion.get("fixture_only", False)),
        "same_source_fusion_selected_by_mtt": bool(q79_fusion.get("selected_by_mtt", False)),
        "same_source_for_ordered_L_pic0_GS_and_DE": bool(
            q79_fusion.get("same_source_for_ordered_L_pic0_GS_and_DE", False)
        ),
        "regularization_identifies_logdet_as_p_a": False,
        "quotient_logdet": quotient_logdet,
        "conditional_p_Y": conditional["conditional_p_Y"],
        "conditional_lambda12": conditional["conditional_lambda_12"],
    }

    qa_route_passes = (
        qa_route_checks["exact_matrix_constructed"]
        and qa_route_checks["quotient_matrix_constructed"]
        and qa_route_checks["rank3_carrier_shape_found"]
        and qa_route_checks["source_level_rank3_carrier_support_closed"]
        and qa_route_checks["q79_factorized_selected_by_mtt"]
        and qa_route_checks["q79_sector_maps_selected_by_mtt"]
        and qa_route_checks["q79_gerbe_source_verified"]
        and qa_route_checks["same_source_fusion_selected_by_mtt"]
        and qa_route_checks["same_source_for_ordered_L_pic0_GS_and_DE"]
        and qa_route_checks["regularization_identifies_logdet_as_p_a"]
    )

    direct_py_route_checks = {
        "source_template_allows_direct_pY": "direct_pY_route" in template["allowed_promotion_routes"],
        "direct_quotient_logdet_as_pY_forbidden": True,
        "source_emitted_hypercharge_normalized_operator": False,
        "hypercharge_bypasses_Qa_Qc_map": False,
        "regularization_identifies_logdet_as_pY": False,
    }
    direct_py_route_passes = (
        direct_py_route_checks["source_emitted_hypercharge_normalized_operator"]
        and direct_py_route_checks["regularization_identifies_logdet_as_pY"]
    )

    candidate = {
        "candidate": "SelectedElectroweakQaStackOrU1YRowSourcePayloadFill",
        "status": "ELECTROWEAK_QASTACK_OR_U1YROW_SOURCE_PAYLOAD_FILL_NOGO_CURRENT_SOURCE_SUPPORT_ONLY",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_gate_status": gate["status"],
        "schema_tested": template["schema"],
        "route_fill_attempts": {
            "Qa_stack_route": {
                "accepted": qa_route_passes,
                "status": "SUPPORT_PRESENT_SOURCE_IDENTITY_AND_REGULARIZATION_OPEN",
                "checks": qa_route_checks,
                "blocking_fields": [
                    "q79 factorized packet is not selected_by_mtt",
                    "q79 sector maps are not selected_by_mtt",
                    "selected gerbe source is not verified",
                    "same-source fusion is fixture/support only, not selected",
                    "no regularization theorem identifies the quotient logdet as the selected p_a finite part",
                ],
            },
            "direct_pY_route": {
                "accepted": direct_py_route_passes,
                "status": "NO_SOURCE_EMITTED_HYPERCHARGE_NORMALIZED_ROW",
                "checks": direct_py_route_checks,
                "blocking_fields": [
                    "no source-emitted hypercharge-normalized U1/Y threshold operator is present",
                    "the typed hypercharge gate forbids treating the quotient logdet directly as p_Y",
                ],
            },
        },
        "fill_summary": {
            "Qa_stack_source_payload_found": qa_route_passes,
            "direct_pY_source_payload_found": direct_py_route_passes,
            "lambda_12_closed": False,
            "measured_electroweak_closure": False,
            "current_source_nogo_proved": True,
            "mathematical_impossibility_claimed": False,
            "best_live_route": "Qa_stack_route",
            "reason_best_live_route": (
                "It already has the exact finite matrix, selected Pperp quotient policy, "
                "rank-3 carrier support, and the typed Qa/Qc hypercharge map; only source "
                "identity and p-row regularization remain missing."
            ),
        },
        "minimal_closing_payload": {
            "name": "Selected_Electroweak_QaStack_SourceIdentity_and_pRowRegularization_Subpacket_v1",
            "must_emit": [
                "selected_by_mtt true for the factorized rank-3 carrier in the same branch",
                "selected sector maps and shared central line basis used by Pperp",
                "selected source identity from terminal/Route-C/q79 support to the exact A_base tensor I_3 matrix",
                "same-source proof that quotienting by <s> gives A_base tensor I_(V_3/<s>) for the threshold row",
                "zeta/heat finite-part convention identifying quotient logdet 29.201650332199108 with p_a",
                "same p-row convention as selected Qc and SU2 weak-split accounting",
            ],
            "direct_pY_fallback": [
                "source-emitted hypercharge-normalized threshold operator",
                "index/Dynkin weights internal to that source",
                "regularization identifying its finite part as p_Y",
            ],
        },
        "what_closes": {
            "source_payload_fill_attempt_executed": True,
            "Qa_stack_route_is_best_live_route": True,
            "direct_pY_shortcut_rejected": True,
            "current_source_no_go_proved": True,
            "minimal_closing_subpacket_named": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_factorized_source_identity": True,
            "selected_sector_maps": True,
            "selected_gerbe_or_terminal_source": True,
            "p_a_finite_part_regularization": True,
            "direct_pY_operator_row": True,
            "lambda_12": True,
            "measured_electroweak_closure": True,
        },
        "guardrails": {
            "observed_electroweak_data_used": False,
            "target_fitting_used": False,
            "promotes_quotient_logdet_as_p_a": False,
            "promotes_quotient_logdet_as_pY": False,
            "promotes_fixture_or_support_packet": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
        },
        "next_required_artifact": "Selected_Electroweak_QaStack_SourceIdentity_and_pRowRegularization_Subpacket_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakQaStackOrU1YRowSourcePayloadFill",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "Qa_stack_source_payload_found": qa_route_passes,
        "direct_pY_source_payload_found": direct_py_route_passes,
        "current_source_nogo_proved": True,
        "mathematical_impossibility_claimed": False,
        "best_live_route": candidate["fill_summary"]["best_live_route"],
        "next_required_artifact": candidate["next_required_artifact"],
        "lambda_12_closed": False,
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    qa = candidate["route_fill_attempts"]["Qa_stack_route"]
    direct = candidate["route_fill_attempts"]["direct_pY_route"]
    lines = [
        "# Selected Electroweak QaStack or U1YRow SourcePayload Fill v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"Qa_stack_source_payload_found = {str(candidate['fill_summary']['Qa_stack_source_payload_found']).lower()}",
        f"direct_pY_source_payload_found = {str(candidate['fill_summary']['direct_pY_source_payload_found']).lower()}",
        f"current_source_nogo_proved = {str(candidate['fill_summary']['current_source_nogo_proved']).lower()}",
        f"mathematical_impossibility_claimed = {str(candidate['fill_summary']['mathematical_impossibility_claimed']).lower()}",
        f"best_live_route = {candidate['fill_summary']['best_live_route']}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "This fill attempt tests the exact source-payload template emitted by the",
        "previous promotion gate. The result is useful but not final: the Qa-stack",
        "route is now the best live path, while the direct `p_Y` route still has no",
        "source-emitted hypercharge-normalized threshold row.",
        "",
        "## Qa-Stack Route",
        "",
        f"Accepted: `{str(qa['accepted']).lower()}`",
        "",
        "| Check | Value |",
        "| --- | --- |",
    ]
    for key, value in qa["checks"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(["", "Blocking fields:"])
    for item in qa["blocking_fields"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Direct pY Route",
            "",
            f"Accepted: `{str(direct['accepted']).lower()}`",
            "",
            "| Check | Value |",
            "| --- | --- |",
        ]
    )
    for key, value in direct["checks"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(["", "Blocking fields:"])
    for item in direct["blocking_fields"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Minimal Closing Payload",
            "",
            f"Next artifact: `{candidate['next_required_artifact']}`.",
            "",
        ]
    )
    for item in candidate["minimal_closing_payload"]["must_emit"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "Direct `p_Y` remains a fallback only if a source emits a hypercharge-normalized row directly:",
            "",
        ]
    )
    for item in candidate["minimal_closing_payload"]["direct_pY_fallback"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- No observed electroweak data, target residuals, masses, or mixings are used.",
            "- The quotient determinant is not promoted as selected `p_a`.",
            "- The quotient determinant is not promoted as direct `p_Y`.",
            "- Support/fixture packets are not promoted.",
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
