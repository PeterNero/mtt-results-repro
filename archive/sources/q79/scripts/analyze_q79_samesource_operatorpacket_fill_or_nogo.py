"""Analyze the q79 same-source operator-packet fill/no-go theorem.

The previous q79 theorem reduced the selected matter-slot charge and overlap
normalization problem to the same seven-field same-source packet used by the
SM-parity execution repo.  This script imports the actual fill attempt, records
the validator no-go, and advances the q79 next target to the current downstream
frontier: stability/HYM or honest Route-C residual source data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

OUT_DIR = CANDIDATES / "q79_samesource_operatorpacket_fill_or_nogo"
OUT_TABLE = OUT_DIR / "field_validation_table.json"
OUT_CANDIDATE = CANDIDATES / "q79_samesource_operatorpacket_fill_or_nogo.candidate.json"
OUT_CERT = CERTS / "q79_samesource_operatorpacket_fill_or_nogo_certificate.json"
OUT_PAPER = CORPUS / "Q79_Selected_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1.md"

STATUS = "Q79_SAMESOURCE_OPERATORPACKET_FILL_ATTEMPT_NOGO_CURRENT_SCAFFOLDS_SUPPORT_ONLY"
NEXT = "Q79_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1"

Q79_INPUTS = {
    "matter_slot_overlap_reduction": CERTS
    / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json",
    "conditional_weylpair_A": CERTS
    / "q79_routec_weylpair_aselected_assembly_or_source_proof_certificate.json",
    "sector_charge_reduction": CERTS / "q79_routec_weylpair_sector_charge_or_chirality_certificate.json",
    "source_provenance": CERTS / "q79_routec_weylpair_source_provenance_lemma_certificate.json",
}

SM_INPUTS = {
    "fill_or_nogo_certificate": SM
    / "certificates"
    / "selected_routec_samesource_operatorpacket_fill_or_nogo_certificate.json",
    "fill_or_nogo_candidate": SM
    / "candidate_data"
    / "selected_routec_samesource_operatorpacket_fill_or_nogo.candidate.json",
    "minimal_subpacket_plan_certificate": SM
    / "certificates"
    / "selected_routec_sourceemission_minimal_subpacket_attack_plan_certificate.json",
    "minimal_subpacket_plan_candidate": SM
    / "candidate_data"
    / "selected_routec_sourceemission_minimal_subpacket_attack_plan.candidate.json",
    "operator_source_identity_certificate": SM
    / "certificates"
    / "selected_routec_operatorsourceidentity_subpacket_certificate.json",
    "operator_source_identity_candidate": SM
    / "candidate_data"
    / "selected_routec_operatorsourceidentity_subpacket.candidate.json",
    "rank2_l2_or_routec_residual_certificate": SM
    / "certificates"
    / "selected_routec_rank2_l2_or_routec_residual_fill_certificate.json",
    "rank2_l2_or_routec_residual_candidate": SM
    / "candidate_data"
    / "selected_routec_rank2_l2_or_routec_residual_fill.candidate.json",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def status_record(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": str(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
        "what_closes": data.get("what_closes") or data.get("what_closes_now") or {},
        "what_remains_open": data.get("what_remains_open") or data.get("still_open") or {},
    }


def build_field_table(fill: dict[str, Any]) -> dict[str, Any]:
    packet = fill["attempted_selected_packet"]
    fields = packet["fields"]
    rows: dict[str, dict[str, Any]] = {}
    for name, row in fields.items():
        rows[name] = {
            "required": row["required"],
            "support_present": row["support_present"],
            "selected_emitted": row["selected_emitted"],
            "same_source": row["same_source"],
            "theorem_derived": row["theorem_derived"],
            "provenance": row["provenance"],
            "reason_not_selected": row["reason_not_selected"],
        }
    return {
        "required_fields": len(rows),
        "support_present": sum(1 for row in rows.values() if row["support_present"] is True),
        "selected_emitted": sum(1 for row in rows.values() if row["selected_emitted"] is True),
        "same_source_emitted": sum(1 for row in rows.values() if row["same_source"] is True),
        "theorem_derived": sum(1 for row in rows.values() if row["theorem_derived"] is True),
        "rows": rows,
    }


def downstream_frontier(sm: dict[str, dict[str, Any]]) -> dict[str, Any]:
    plan = sm["minimal_subpacket_plan_candidate"]
    operator = sm["operator_source_identity_candidate"]
    rank2 = sm["rank2_l2_or_routec_residual_candidate"]

    l2 = rank2.get("rank2_l2_fill", {})
    ordered = rank2.get("ordered_source_fill", {})
    operator_impact = rank2.get("operator_identity_impact", {})

    return {
        "minimal_attack_plan": {
            "status": plan.get("status"),
            "first_subpacket": plan.get("strategy", {}).get("minimal_first_subpacket"),
            "dependency_order": [
                item.get("id") for item in plan.get("strategy", {}).get("dependency_order", [])
            ],
            "next_required_artifact": plan.get("next_required_artifact"),
        },
        "operator_source_identity_subpacket": {
            "status": operator.get("status"),
            "operator_identity_closed": operator.get("operator_identity_verdict", {}).get(
                "subpacket_closed"
            ),
            "rank2_or_routec_fill_required": operator.get("operator_identity_verdict", {}).get(
                "rank2_or_routec_fill_required"
            ),
            "rank2_lane_priority": operator.get("lane_evaluation", {})
            .get("rank2_non_split_valpha", {})
            .get("priority"),
            "routec_lane_priority": operator.get("lane_evaluation", {})
            .get("route_c_finite_hym_strominger", {})
            .get("priority"),
            "next_required_artifact": operator.get("next_required_artifact"),
        },
        "rank2_l2_checkpoint": {
            "status": rank2.get("status"),
            "rank2_l2_validator_exit_code": l2.get("validator", {}).get("exit_code"),
            "ordered_source_validator_exit_code": ordered.get("validator", {}).get("exit_code"),
            "h1": l2.get("reported_cohomology", {}).get("h1"),
            "nonzero_ext_class_selected": l2.get("closed_now", {}).get(
                "nonzero_ext_class_selected"
            ),
            "rank2_arithmetic_blocker_retired": operator_impact.get("rank2_l2_blocker_retired"),
            "selected_operator_identity_closed": operator_impact.get(
                "selected_operator_identity_closed"
            ),
            "what_closes": rank2.get("what_closes_now", {}),
            "what_remains_open": rank2.get("what_remains_open", {}),
            "next_required_artifact": rank2.get("next_required_artifact"),
        },
        "q79_next_required_artifact": NEXT,
    }


def build_candidate() -> dict[str, Any]:
    q79 = {name: load(path) for name, path in Q79_INPUTS.items()}
    sm = {name: load(path) for name, path in SM_INPUTS.items()}

    fill = sm["fill_or_nogo_candidate"]
    fill_cert = sm["fill_or_nogo_certificate"]
    field_table = build_field_table(fill)
    validator = fill["validator_report"]
    packet_flags = fill["attempted_selected_packet"]["packet_flags"]
    summary = fill["fill_summary"]
    previous_reduction = q79["matter_slot_overlap_reduction"]

    fill_no_go = {
        "imported_sm_status": fill.get("status"),
        "imported_sm_certificate_status": fill_cert.get("status"),
        "field_table": field_table,
        "fill_summary": summary,
        "validator_report": {
            "ok": validator.get("ok"),
            "exit_code": validator.get("exit_code"),
            "error_count": len(validator.get("errors", [])),
            "required_fields": validator.get("required_fields", []),
            "errors": validator.get("errors", []),
        },
        "packet_flags": packet_flags,
        "conditional_data_retained": fill["attempted_selected_packet"][
            "conditional_data_retained"
        ],
        "why_fill_fails": fill["why_fill_fails"],
    }

    decision = {
        "fill_attempt_executed": fill.get("what_closes_now", {}).get("fill_attempt_executed")
        is True,
        "validator_rejects_current_scaffold": validator.get("exit_code") == 1
        and validator.get("ok") is False,
        "current_scaffold_nogo_proved": summary.get("nogo_for_current_scaffolds") is True,
        "same_source_packet_values_emitted": summary.get("selected_emitted") == 7,
        "promote_conditional_A_to_A_selected": packet_flags.get("promote_to_A_selected") is True,
        "emit_b_selected": packet_flags.get("promote_to_b_selected") is True,
        "target_fitting_used": fill.get("target_fitting_used") is True,
        "full_SM_or_no_knob_closure": False,
    }

    frontier = downstream_frontier(sm)
    rank2_open = frontier["rank2_l2_checkpoint"]["what_remains_open"]

    return {
        "certificate": "Q79SameSourceOperatorPacketFillOrNoGo",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "table_path": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "q79_input_statuses": {name: status_record(path) for name, path in Q79_INPUTS.items()},
        "sm_input_statuses": {name: status_record(path) for name, path in SM_INPUTS.items()},
        "previous_q79_reduction_status": previous_reduction.get("status"),
        "fill_or_nogo_result": fill_no_go,
        "q79_decision": decision,
        "downstream_frontier_import": frontier,
        "what_closes_now": {
            "same_source_packet_fill_attempt_imported": True,
            "seven_field_validator_no_go_recorded": decision["validator_rejects_current_scaffold"],
            "conditional_A_guardrail_preserved": not decision[
                "promote_conditional_A_to_A_selected"
            ],
            "b_selected_guardrail_preserved": not decision["emit_b_selected"],
            "downstream_frontier_advanced_to_stability_or_routec_residual": (
                frontier["rank2_l2_checkpoint"]["next_required_artifact"]
                == "MTT_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1"
            ),
            "target_fitting_excluded": not decision["target_fitting_used"],
        },
        "what_remains_open": {
            "selected_visible_operator_source": rank2_open.get(
                "selected_operator_identity_closed"
            )
            is False,
            "non_split_stability_or_hym_proved": rank2_open.get(
                "non_split_stability_or_hym_proved"
            )
            is True,
            "selected_route_c_residual_pass": rank2_open.get("selected_route_c_residual_pass")
            is True,
            "operator_layer_pic0_recheck": rank2_open.get("operator_layer_pic0_recheck")
            is True,
            "same_source_Chern_Weil_GS_derivation": rank2_open.get(
                "same_source_ChernWeil_GS_derivation",
                rank2_open.get("same_source_Chern_Weil_GS_derivation"),
            )
            is True,
            "same_source_D_E_rhoE_Riesz_Green_dotD": rank2_open.get(
                "same_source_D_E_rhoE_Riesz_Green_dotD"
            )
            is True,
            "primitive_C1_contractions": rank2_open.get("primitive_C1_contractions") is True,
            "terminal_section_theorem_unconditional_promotion": rank2_open.get(
                "terminal_section_theorem_unconditional_promotion"
            )
            is True,
            "selected_matter_slot_charge_table": True,
            "selected_1M_neutrino_rule": True,
            "selected_overlap_transfer_functor": True,
            "selected_trace_hessian_normalization": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "uses_observed_masses_or_ckm_inputs": False,
            "uses_benchmark_flavor_entries": False,
            "uses_locked_target_columns_as_selector": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_selected_matter_slot_charge": False,
            "claims_selected_overlap_normalization": False,
            "claims_full_sm_closure": False,
        },
        "theorem": {
            "name": "Q79SelectedRouteCSameSourceOperatorPacketFillOrNoGoTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The selected same-source operator packet cannot be filled from the "
                "current scaffolds.  The imported validator rejects all seven fields "
                "as support-only, conditional, target-localized, or absent: source "
                "identity, matter-slot charge, the 1_M neutrino rule, operator "
                "values, overlap transfer, normalization, and primitive contractions. "
                "The downstream SM execution has already converted this no-go into "
                "a subpacket attack, reduced operator-source identity to rank-two "
                "or Route-C fill values, and closed the rank-two L2 arithmetic input; "
                "the current frontier is stability/HYM or an honest selected Route-C "
                "residual source, with A_selected and b_selected still unclaimed."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }


def render_bool_map(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def render_fields(table: dict[str, Any]) -> str:
    lines = []
    for name, row in table["rows"].items():
        lines.append(
            "- `{name}`: support=`{support}`, selected=`{selected}`, same_source=`{same}`, "
            "theorem_derived=`{derived}`, provenance=`{provenance}`".format(
                name=name,
                support=row["support_present"],
                selected=row["selected_emitted"],
                same=row["same_source"],
                derived=row["theorem_derived"],
                provenance=row["provenance"],
            )
        )
    return "\n".join(lines)


def build_paper(data: dict[str, Any]) -> str:
    fill = data["fill_or_nogo_result"]
    frontier = data["downstream_frontier_import"]
    rank2 = frontier["rank2_l2_checkpoint"]
    return f"""# Q79 Selected Route-C SameSource OperatorPacket Fill or NoGo v1

## Result

The same-source operator packet fill is a **validator-backed no-go for the
current scaffolds**.

The imported SM-parity fill attempt has seven required fields, six support
fields, and zero selected-emitted fields.  The validator exit code is
`{fill["validator_report"]["exit_code"]}`, with `ok={fill["validator_report"]["ok"]}`.

This means the conditional Weyl-pair operator remains useful algebraic support,
but it is not `A_selected`, it does not emit `b_selected`, and it does not close
the selected SM data theorem.

## Field Table

- required fields: `{fill["field_table"]["required_fields"]}`
- support present: `{fill["field_table"]["support_present"]}`
- selected emitted: `{fill["field_table"]["selected_emitted"]}`
- same-source emitted: `{fill["field_table"]["same_source_emitted"]}`
- theorem-derived: `{fill["field_table"]["theorem_derived"]}`

{render_fields(fill["field_table"])}

## Why The Fill Fails

{chr(10).join(f"- {item}" for item in fill["why_fill_fails"])}

## Downstream Frontier

The no-go has already been decomposed on the SM side:

- minimal attack plan: `{frontier["minimal_attack_plan"]["status"]}`
- operator-source identity: `{frontier["operator_source_identity_subpacket"]["status"]}`
- rank-two L2 checkpoint: `{rank2["status"]}`
- rank-two L2 validator exit code: `{rank2["rank2_l2_validator_exit_code"]}`
- ordered-source validator exit code: `{rank2["ordered_source_validator_exit_code"]}`
- selected `h1`: `{rank2["h1"]}`
- nonzero Ext class selected: `{rank2["nonzero_ext_class_selected"]}`
- selected operator identity closed: `{rank2["selected_operator_identity_closed"]}`

So the next honest q79-local target is not another seven-field bulk fill.  It is
the current frontier imported from the downstream execution:
`{data["next_required_artifact"]}`.

## Decision

{render_bool_map(data["q79_decision"])}

## What This Closes

{render_bool_map(data["what_closes_now"])}

## What Remains Open

{render_bool_map(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved as a no-go/reduction theorem.

{data["theorem"]["statement"]}
"""


def main() -> int:
    data = build_candidate()
    write_json(OUT_TABLE, data["fill_or_nogo_result"]["field_table"])
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 same-source operator-packet fill/no-go")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
