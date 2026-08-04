"""Build the U1/Y Route-C operator-source identity bridge subpacket."""

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
    "sourceemission_plan": DATA / "selected_u1y_routec_sourceemission_minimal_subpacket_attack_plan.candidate.json",
    "same_source_fill_nogo": DATA / "selected_u1y_routec_samesource_operatorpacket_fill_or_nogo.candidate.json",
    "sm_visible_gs_operator_source": SM / "candidate_data" / "selected_visible_green_schwarz_operator_source.candidate.json",
    "sm_same_source_symmetry_breaker": SM / "candidate_data" / "same_source_symmetry_breaking_source.candidate.json",
    "q79_all_remaining_valpha_gates": Q79 / "certificates" / "all_remaining_valpha_gates_attempt_certificate.json",
    "q79_valpha_s3_attempt": Q79
    / "candidate_data"
    / "selected_qa_su3_same_source_valpha_s3_operator_packet_attempt.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_operator_source_identity_bridge_subpacket.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_operator_source_identity_bridge_subpacket_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_OperatorSourceIdentity_Bridge_Subpacket_v1.md"

STATUS = "U1Y_ROUTEC_OPERATOR_SOURCE_IDENTITY_BRIDGE_CURRENT_SOURCE_NOGO"
NEXT = "Selected_U1Y_RouteC_OperatorLayerPic0_or_SelectedResidual_Source_Subpacket_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    plan = load(INPUTS["sourceemission_plan"])
    fill_nogo = load(INPUTS["same_source_fill_nogo"])
    visible = load(INPUTS["sm_visible_gs_operator_source"])
    symmetry = load(INPUTS["sm_same_source_symmetry_breaker"])
    q79_gates = load(INPUTS["q79_all_remaining_valpha_gates"])
    q79_attempt = load(INPUTS["q79_valpha_s3_attempt"])

    visible_results = visible["gate_results"]
    q79_summary = q79_gates["gate_summary"]
    selected_valpha = q79_gates["selected_valpha_validator"]
    same_source_fusion = q79_gates["same_source_fusion_validator"]

    bridge_requirements = {
        "selected_operator_source_identity": {
            "required": "selected q79/F,m=1 visible bundle/sheaf, V_alpha, or finite Route-C source identity",
            "support_present": True,
            "selected_emitted": False,
            "same_source": False,
            "theorem_derived": False,
            "evidence": [
                visible["imported_results"]["selected_s3_source"]["status"],
                visible["imported_results"]["visible_gs_curvature"]["status"],
                q79_attempt["status"],
            ],
            "blocker": "selected visible operator source is not constructed",
        },
        "s3_gs_to_operator_bridge": {
            "required": "same-source bridge from selected S3/Green-Schwarz support to operator source",
            "support_present": True,
            "selected_emitted": False,
            "same_source": False,
            "theorem_derived": False,
            "evidence": [
                visible["superset_mode"]["superset_convergence"]["locked_target"],
                visible["theorem"]["statement"],
            ],
            "blocker": "convergence target is identified, but same-source operator payload is not emitted",
        },
        "operator_layer_pic0": {
            "required": "Pic0 selection or physical quotient rule at operator layer",
            "support_present": True,
            "selected_emitted": False,
            "same_source": False,
            "theorem_derived": False,
            "evidence": [
                symmetry["inherited_frontier"]["must_supply"][2],
                q79_summary["OperatorLayerPic0Recheck"],
            ],
            "blocker": "operator-layer Pic0 remains open",
        },
        "selected_residual_or_hym": {
            "required": "HYM/Strominger residual or Route-C residual with selected_source_verified true",
            "support_present": True,
            "selected_emitted": False,
            "same_source": False,
            "theorem_derived": False,
            "evidence": [
                q79_summary["SelectedNonSplitVAlphaStabilityOrRouteCResidual"],
                visible["imported_results"]["selected_hym_operator_source_attempt"]["status"],
            ],
            "blocker": "stability/non-split input is partial and residual selected-source flags fail",
        },
    }

    route_evaluation = {
        "s3_gs_convergence_route": {
            "support_level": "STRONG_SUPPORT_NOT_PROMOTION",
            "passes_bridge": False,
            "closed_support": {
                "selected_s3_source_closed": visible_results["selected_s3_source_closed"],
                "visible_green_schwarz_curvature_closed": visible_results["visible_green_schwarz_curvature_closed"],
                "old_s3_fw_projector_blockers_retired": visible_results["old_s3_fw_projector_blockers_retired"],
            },
            "open": visible["imported_results"]["visible_operator_after_s3"]["still_open_cut_set"],
        },
        "terminal_valpha_route": {
            "support_level": "UPDATED_PARTIAL",
            "passes_bridge": False,
            "retired": q79_gates["newly_retired_by_after_lockdown_attempts"],
            "open_item_count": selected_valpha["open_item_count"],
            "first_open_items": selected_valpha["open_items"][:8],
        },
        "same_source_fusion_route": {
            "support_level": "VALIDATOR_REACHES_OPERATOR_LAYER",
            "passes_bridge": False,
            "open_item_count": same_source_fusion["open_item_count"],
            "open_items": same_source_fusion["open_items"],
        },
        "routec_residual_route": {
            "support_level": "VALIDATOR_READY_NOT_SELECTED",
            "passes_bridge": False,
            "selected_source_verified": False,
            "required_next": "selected residual/HYM/Strominger source certificate with selected_source_verified=true",
        },
    }

    hard_cut_set = [
        "selected_by_mtt/source_certificate for the visible operator source",
        "operator-layer Pic0 selection or physical quotient",
        "same-source Chern-Weil/Green-Schwarz row derivation",
        "HYM/Strominger or Route-C residual with selected_source_verified=true",
        "selected D_E/Riesz/Green/dotD evidence from that same source",
    ]

    candidate = {
        "candidate": "SelectedU1YRouteCOperatorSourceIdentityBridgeSubpacket",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": plan["status"],
        "bridge_requirements": bridge_requirements,
        "route_evaluation": route_evaluation,
        "hard_cut_set": hard_cut_set,
        "source_identity_bridge_result": {
            "bridge_closed": False,
            "selected_operator_source_identity_emitted": False,
            "same_source_bridge_proved": False,
            "operator_layer_pic0_closed": False,
            "selected_residual_or_hym_closed": False,
            "current_source_nogo": True,
            "mathematical_impossibility_claimed": False,
        },
        "what_closes_now": {
            "operator_source_identity_bridge_attempted": True,
            "s3_gs_support_convergence_retained": True,
            "obsolete_ordered_source_blockers_retired": True,
            "operator_layer_cut_set_isolated": True,
            "current_source_nogo_proved": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            **fill_nogo["what_remains_open"],
            "selected_operator_source_identity": True,
            "s3_gs_to_operator_bridge": True,
            "operator_layer_Pic0": True,
            "selected_residual_or_hym": True,
            "same_source_DE_Riesz_Green_dotD": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_lambda12": False,
            "claims_full_closure": False,
            "promotes_support_as_selected": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "target_fitting_used": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCOperatorSourceIdentityBridgeSubpacket",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "bridge_closed": False,
        "current_source_nogo": True,
        "mathematical_impossibility_claimed": False,
        "support_requirements": sum(1 for item in bridge_requirements.values() if item["support_present"]),
        "selected_requirements": sum(1 for item in bridge_requirements.values() if item["selected_emitted"]),
        "hard_cut_set_count": len(hard_cut_set),
        "next_required_artifact": NEXT,
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C OperatorSourceIdentity Bridge Subpacket v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"bridge_closed = {str(cert['bridge_closed']).lower()}",
        f"current_source_nogo = {str(cert['current_source_nogo']).lower()}",
        f"support_requirements = {cert['support_requirements']}",
        f"selected_requirements = {cert['selected_requirements']}",
        f"mathematical_impossibility_claimed = {str(cert['mathematical_impossibility_claimed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The selected S3/Green-Schwarz support and the updated terminal V_alpha",
        "attempts converge on the same target: a q79/F,m=1 visible operator",
        "source. The bridge still does not close, because support convergence",
        "is not the same thing as selected operator-source emission.",
        "",
        "## Bridge Requirements",
        "",
        "| Requirement | Support | Selected | Same Source | Blocker |",
        "| --- | --- | --- | --- | --- |",
    ]
    for key, row in candidate["bridge_requirements"].items():
        lines.append(
            f"| `{key}` | `{str(row['support_present']).lower()}` | "
            f"`{str(row['selected_emitted']).lower()}` | `{str(row['same_source']).lower()}` | {row['blocker']} |"
        )
    lines.extend(
        [
            "",
            "## Hard Cut Set",
            "",
        ]
    )
    for item in candidate["hard_cut_set"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Verdict",
            "",
            "This is a current-source no-go, not an impossibility theorem. The next",
            "productive target is to close either operator-layer Pic0 or the selected",
            "residual/HYM/Strominger source certificate while preserving same-source",
            "identity.",
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
