"""Build the U1/Y Route-C source-emission minimal subpacket attack plan."""

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
    "previous_fill_or_nogo": DATA / "selected_u1y_routec_samesource_operatorpacket_fill_or_nogo.candidate.json",
    "u1y_hybrid_packet": DATA / "selected_u1y_routec_hybrid_galerkin_overlap_source_packet.candidate.json",
    "sm_minimal_subpacket_plan": SM
    / "candidate_data"
    / "selected_routec_sourceemission_minimal_subpacket_attack_plan.candidate.json",
    "sm_same_source_symmetry_breaker": SM / "candidate_data" / "same_source_symmetry_breaking_source.candidate.json",
    "sm_visible_gs_operator_source": SM / "candidate_data" / "selected_visible_green_schwarz_operator_source.candidate.json",
    "q79_all_remaining_valpha_gates": Q79 / "certificates" / "all_remaining_valpha_gates_attempt_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_sourceemission_minimal_subpacket_attack_plan.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_sourceemission_minimal_subpacket_attack_plan_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1.md"

STATUS = "U1Y_ROUTEC_SOURCEEMISSION_MINIMAL_SUBPACKET_ATTACK_PLAN_BUILT"
NEXT = "Selected_U1Y_RouteC_OperatorSourceIdentity_Bridge_Subpacket_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    previous = load(INPUTS["previous_fill_or_nogo"])
    hybrid = load(INPUTS["u1y_hybrid_packet"])
    sm_plan = load(INPUTS["sm_minimal_subpacket_plan"])
    symmetry = load(INPUTS["sm_same_source_symmetry_breaker"])
    visible = load(INPUTS["sm_visible_gs_operator_source"])
    q79_gates = load(INPUTS["q79_all_remaining_valpha_gates"])

    selected_valpha = q79_gates["selected_valpha_validator"]
    same_source_fusion = q79_gates["same_source_fusion_validator"]
    primitive_gate = q79_gates["primitive_and_sm_gates"]["PrimitiveC1Contractions"]

    dependency_order = [
        {
            "id": "S1_source_identity_bridge",
            "priority": 1,
            "next_artifact": NEXT,
            "reason": "Every same-source field depends on one selected visible/Route-C/V_alpha operator-source identity; current source-level S3/GS support is not enough.",
            "must_emit": [
                "selected q79/F,m=1 visible bundle/sheaf, V_alpha, or finite Route-C source identity",
                "same-source bridge from selected S3/Green-Schwarz support to the operator source",
                "Pic0 selection or physical quotient rule at the operator layer",
                "HYM/Strominger residual or Route-C residual with selected_source_verified true",
            ],
            "current_blockers": {
                "selected_valpha_open_items": selected_valpha["open_item_count"],
                "same_source_fusion_open_items": same_source_fusion["open_item_count"],
                "operator_layer_Pic0": q79_gates["gate_summary"]["OperatorLayerPic0Recheck"],
                "same_source_ChernWeil_GS": q79_gates["gate_summary"]["SameSourceChernWeilGSRow"],
                "stability_or_routec": q79_gates["gate_summary"]["SelectedNonSplitVAlphaStabilityOrRouteCResidual"],
            },
            "retired_old_blockers": q79_gates["newly_retired_by_after_lockdown_attempts"],
        },
        {
            "id": "S2_operator_values_payload",
            "priority": 2,
            "next_artifact": "Selected_U1Y_RouteC_DE_DotD_Green_SourceEmission_Subpacket_v1",
            "reason": "D_E, Riesz/Green, and dotD are the validator backbone; they must be emitted after, and from, the selected operator source.",
            "must_emit": [
                "selected D_E action for Q,u,d,L,e,N,H or the U1/Y reduced sector",
                "selected Riesz projector and reduced Green operators",
                "selected dotD_alpha1 with same-branch derivative verification",
                "coherent spectral projector retention for the same source",
            ],
            "current_blockers": {
                "same_source_DE_rhoE_Riesz_Green_dotD": q79_gates["gate_summary"]["SameSourceDErhoERieszGreenDotD"],
                "same_source_fusion_validator_open_items": same_source_fusion["open_items"],
                "visible_operator_cut_set": visible["imported_results"]["visible_operator_after_s3"]["still_open_cut_set"],
            },
        },
        {
            "id": "S3_matter_overlap_payload",
            "priority": 3,
            "next_artifact": "Selected_U1Y_RouteC_MatterSlot_Overlap_SourceEmission_Subpacket_v1",
            "reason": "Matter-slot charge, the 1_M neutrino rule, overlap transfer, and normalization cannot promote while the sector basis/operator source is support-only.",
            "must_emit": [
                "selected matter-slot charge table: 10_M -> u/e and non-10 plus 1_M -> d/nuD",
                "selected 1_M Dirac-neutrino routing rule",
                "selected source-to-C1 overlap-transfer functor",
                "selected trace/inner-product/Hessian normalization",
            ],
            "current_blockers": {
                "source_identity": previous["what_remains_open"]["source_identity"],
                "matter_slot_charge": previous["what_remains_open"]["matter_slot_charge"],
                "singlet_neutrino_rule": previous["what_remains_open"]["singlet_neutrino_rule"],
                "overlap_transfer": previous["what_remains_open"]["overlap_transfer"],
                "normalization": previous["what_remains_open"]["normalization"],
            },
        },
        {
            "id": "S4_primitive_contractions_payload",
            "priority": 4,
            "next_artifact": "Selected_U1Y_RouteC_PrimitiveC1_Contractions_Subpacket_v1",
            "reason": "Primitive C1/Yukawa contractions are last: they require selected source identity, operators, sector routing, and overlap normalization.",
            "must_emit": [
                "24 primitive C1 contraction matrices or a reduced U1/Y theorem explaining the quotient",
                "zero-mode response orientations",
                "explicit vertex and basis-connection data",
                "proof the contractions are theorem-derived from the same source",
            ],
            "current_blockers": {
                "primitive_gate_status": primitive_gate["status"],
                "missing_primitive_count": primitive_gate["missing_primitive_count"],
                "selected_missing_data_first_blocker": primitive_gate["selected_missing_data_first_blocker"],
            },
        },
    ]

    candidate = {
        "candidate": "SelectedU1YRouteCSourceEmissionMinimalSubpacketAttackPlan",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": previous["status"],
        "u1y_hybrid_status": hybrid["status"],
        "sm_plan_status": sm_plan["status"],
        "strategy": {
            "why_not_fill_all_at_once": "The same-source validator rejected all seven fields; the first dependency is operator-source identity, not overlap algebra.",
            "minimal_first_subpacket": NEXT,
            "dependency_order": dependency_order,
            "promotion_condition": "Only after S1-S4 pass with selected_emitted=true, same_source=true, and theorem_derived=true may A_selected, b_selected, lambda_12, or U1/Y closure be recomputed.",
            "best_live_route": "source identity bridge via selected V_alpha/Route-C operator source plus Pic0 quotient and same-source D_E/dotD payload",
        },
        "acceptance_contract": {
            "must_make_same_source_validator_pass": True,
            "required_field_flags": {
                "selected_emitted": True,
                "same_source": True,
                "theorem_derived": True,
            },
            "packet_flags": {
                "one_same_source": True,
                "promote_to_A_selected": True,
                "promote_to_b_selected": True,
                "observed_data_used": False,
                "target_fitting_used": False,
            },
            "forbidden_provenance": [
                "support_shape_only",
                "locked_target_selection",
                "unselected_fixture",
                "lifted_flag",
                "observed_sm_data",
                "benchmark_matrix",
            ],
        },
        "what_closes_now": {
            "minimal_dependency_order_built": True,
            "first_subpacket_selected": True,
            "obsolete_ordered_source_blockers_retired": True,
            "fill_nogo_converted_to_source_emission_plan": True,
            "validator_acceptance_contract_made_explicit": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            **previous["what_remains_open"],
            "operator_layer_Pic0": True,
            "same_source_DE_Riesz_Green_dotD": True,
            "same_source_ChernWeil_GS_row": True,
            "selected_source_identity_bridge": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCSourceEmissionMinimalSubpacketAttackPlan",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "next_required_artifact": NEXT,
        "dependency_count": len(dependency_order),
        "first_subpacket": dependency_order[0]["id"],
        "obsolete_ordered_source_blockers_retired": True,
        "closure_claimed": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C SourceEmission Minimal Subpacket Attack Plan v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"minimal_first_subpacket = {candidate['strategy']['minimal_first_subpacket']}",
        f"dependency_count = {cert['dependency_count']}",
        f"closure_claimed = {str(candidate['closure_claimed']).lower()}",
        f"lambda_12_closed = {str(cert['lambda_12_closed']).lower()}",
        "```",
        "",
        "The seven-field same-source packet is now decomposed into the smallest",
        "source-emission gates that can make the validator pass. The first true",
        "gate is not a numerical overlap calculation; it is the selected",
        "operator-source identity bridge.",
        "",
        "A useful update from the q79 side is retained: older ordered-source",
        "validator failures are now retired after terminal-lockdown attempts.",
        "The live blocker is therefore sharper: operator-layer Pic0, same-source",
        "Chern-Weil/GS, D_E/Riesz/Green/dotD, and primitive C1 data.",
        "",
        "## Dependency Order",
        "",
    ]
    for item in candidate["strategy"]["dependency_order"]:
        lines.extend(
            [
                f"### {item['priority']}. {item['id']}",
                "",
                f"Next artifact: `{item['next_artifact']}`.",
                "",
                item["reason"],
                "",
                "Must emit:",
            ]
        )
        for required in item["must_emit"]:
            lines.append(f"- {required}")
        lines.append("")
    lines.extend(
        [
            "## Acceptance Contract",
            "",
            "Every required field must satisfy:",
            "",
            "- `selected_emitted = true`",
            "- `same_source = true`",
            "- `theorem_derived = true`",
            "",
            "The packet must also set `one_same_source`, `promote_to_A_selected`,",
            "and `promote_to_b_selected` to true while keeping observed data and",
            "target fitting false.",
            "",
            "Forbidden provenance remains: support-only shapes, locked target",
            "selection, fixtures, lifted flags, observed data, and benchmark matrices.",
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
