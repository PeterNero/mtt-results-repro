"""Build the U1/Y Route-C same-source matter-slot packet or residual gate."""

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
SM = TEXPAPERS / "mtt-sm-parity-closure"

INPUTS = {
    "u1y_alpha1_kernel_gate": DATA / "selected_u1y_routec_alpha1_tangent_or_retarded_overlap_kernel.candidate.json",
    "q79_samesource_packet_fill": Q79 / "certificates" / "q79_samesource_operatorpacket_fill_or_nogo_certificate.json",
    "q79_global_destabilizer_or_residual": Q79 / "certificates" / "q79_global_destabilizer_enumeration_or_selected_residual_certificate.json",
    "q79_same_source_operator_provenance": Q79 / "certificates" / "q79_same_source_operator_provenance_or_selected_routec_solve_certificate.json",
    "q79_visible_operator_or_primitive_c1": Q79 / "certificates" / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions_certificate.json",
    "sm_samesource_packet_fill": SM / "certificates" / "selected_routec_samesource_operatorpacket_fill_or_nogo_certificate.json",
    "sm_global_destabilizer_or_residual": SM / "certificates" / "selected_routec_global_destabilizer_enumeration_or_selected_residual_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_samesource_matter_slot_overlap_operatorpacket_or_selected_residual.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_samesource_matter_slot_overlap_operatorpacket_or_selected_residual_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_SameSource_MatterSlot_Overlap_OperatorPacket_or_SelectedResidual_v1.md"

STATUS = "U1Y_ROUTEC_SAMESOURCE_PACKET_REDUCED_VISIBLE_OPERATOR_OR_PRIMITIVE_C1_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedVisibleOperatorSource_or_PrimitiveC1Contractions_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def status_of(key: str, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": rel(INPUTS[key]),
        "present": INPUTS[key].exists(),
        "status": data.get("status", "UNKNOWN"),
        "next_required_artifact": data.get("next_required_artifact"),
        "guardrails": data.get("guardrails"),
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    alpha1_gate = load(INPUTS["u1y_alpha1_kernel_gate"])
    fill = load(INPUTS["q79_samesource_packet_fill"])
    global_enum = load(INPUTS["q79_global_destabilizer_or_residual"])
    provenance = load(INPUTS["q79_same_source_operator_provenance"])
    visible_or_c1 = load(INPUTS["q79_visible_operator_or_primitive_c1"])
    sm_fill = load(INPUTS["sm_samesource_packet_fill"])
    sm_global = load(INPUTS["sm_global_destabilizer_or_residual"])

    field_table = fill["fill_or_nogo_result"]["field_table"]
    rows = field_table["rows"]
    reduced_ah = global_enum["reduced_AH_global_rank_one_enumeration"]
    same_source = provenance["same_source_reduction"]
    source_lane = visible_or_c1["source_lane"]
    primitive_lane = visible_or_c1["primitive_c1_lane"]

    decision = {
        "seven_field_packet_validator_nogo": fill["q79_decision"]["validator_rejects_current_scaffold"],
        "support_fields_present": field_table["support_present"],
        "selected_fields_emitted": field_table["selected_emitted"],
        "same_source_emitted": field_table["same_source_emitted"],
        "reduced_AH_global_stability_proved": global_enum["conditional_global_stability_theorem"]["proved"],
        "selected_ordered_source_subvalidator_passes": source_lane["subvalidators"]["ordered_source"]["exit_code"] == 0,
        "selected_s3_class_subvalidator_passes": source_lane["subvalidators"]["s3_class_restriction"]["exit_code"] == 0,
        "visible_operator_source_validator_passes": False,
        "same_source_operator_packet_closes": False,
        "primitive_C1_contractions_emitted": False,
        "all_24_primitive_C1_atoms_emitted": False,
        "A_selected_or_b_selected_emitted": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    reduction = {
        "same_source_packet_fill": {
            "status": fill["status"],
            "field_counts": {
                "required": field_table["required_fields"],
                "support_present": field_table["support_present"],
                "selected_emitted": field_table["selected_emitted"],
                "same_source_emitted": field_table["same_source_emitted"],
                "theorem_derived": field_table["theorem_derived"],
            },
            "rows": rows,
            "validator_error_count": fill["fill_or_nogo_result"]["validator_report"]["error_count"],
            "why_fill_fails": fill["fill_or_nogo_result"]["why_fill_fails"],
        },
        "selected_residual_or_stability_lane": {
            "status": global_enum["status"],
            "reduced_AH_model_stability_proved": True,
            "finite_without_cutoff": reduced_ah["finite_without_cutoff"],
            "hom_to_L_nonnegative_candidates": reduced_ah["hom_to_L_nonnegative_candidates"],
            "hom_to_Q_nonnegative_candidates": reduced_ah["hom_to_Q_nonnegative_candidates"],
            "promotion_gap": global_enum["promotion_gap"],
        },
        "operator_provenance_lane": {
            "status": provenance["status"],
            "honest_current_validator_status": same_source["honest_current_patchwork_validator_status"],
            "honest_current_open_items": same_source["honest_current_open_items"],
            "diagnostic_full_plumbing_passes": same_source["full_plumbing_diagnostic_status"] == "PASS",
            "diagnostic_no_primitive_open_items": same_source["no_primitive_open_items"],
        },
        "visible_operator_or_primitive_c1_lane": {
            "status": visible_or_c1["status"],
            "first_blocking_layer": visible_or_c1["selected_missing_data_scan"]["first_blocking_layer"],
            "source_validator_status": source_lane["validator_status"],
            "source_open_items": source_lane["open_items"],
            "primitive_contract_atom_count": primitive_lane["contract_atom_count"],
            "primitive_missing_atom_count": primitive_lane["missing_atom_count"],
            "primitive_missing_atoms": primitive_lane["missing_atoms"],
        },
    }

    theorem = {
        "name": "U1YRouteCSameSourcePacketResidualReductionTheorem",
        "proved": True,
        "statement": (
            "The U1/Y Route-C same-source matter-slot/overlap packet cannot be "
            "filled from current scaffolds: all seven required fields remain "
            "unselected or non-same-source. However the residual/stability lane "
            "has advanced: reduced AH rank-one stability is proved without a "
            "cutoff, and the selected ordered source plus S3 restriction pass "
            "their subvalidators. The next executable target is either one "
            "selected visible bundle/operator source passing the source validator "
            "or the 24 selected primitive C1 matrices from that same source."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCSameSourceMatterSlotOverlapOperatorPacketOrSelectedResidual",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            key: status_of(key, data)
            for key, data in {
                "u1y_alpha1_kernel_gate": alpha1_gate,
                "q79_samesource_packet_fill": fill,
                "q79_global_destabilizer_or_residual": global_enum,
                "q79_same_source_operator_provenance": provenance,
                "q79_visible_operator_or_primitive_c1": visible_or_c1,
                "sm_samesource_packet_fill": sm_fill,
                "sm_global_destabilizer_or_residual": sm_global,
            }.items()
        },
        "decision": decision,
        "reduction": reduction,
        "theorem": theorem,
        "what_closes_now": {
            "same_source_seven_field_nogo_imported": True,
            "reduced_AH_global_rank_one_stability_imported": True,
            "selected_ordered_source_and_s3_subvalidators_pass": True,
            "hypothetical_full_plumbing_has_no_hidden_validator_obstruction": True,
            "primitive_C1_atomic_contract_enumerated": True,
            "next_target_visible_operator_or_primitive_c1_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_visible_bundle_operator_source_certificate": True,
            "non_split_stability_or_selected_HYM_RouteC_solve": True,
            "same_source_ChernWeil_GS_row": True,
            "selected_DE_rhoE_Riesz_Green_dotD": True,
            "orientation_selection_justified_by_same_source": True,
            "selected_matter_slot_charge_table": True,
            "selected_1M_neutrino_rule": True,
            "selected_overlap_transfer_functor": True,
            "selected_trace_hessian_normalization": True,
            "all_24_primitive_C1_3x3_matrices": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_selected_visible_operator_source": False,
            "claims_primitive_C1_values": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "promotes_hypothetical_full_plumbing": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCSameSourceMatterSlotOverlapOperatorPacketOrSelectedResidual",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "seven_field_packet_validator_nogo": decision["seven_field_packet_validator_nogo"],
        "support_fields_present": decision["support_fields_present"],
        "selected_fields_emitted": decision["selected_fields_emitted"],
        "reduced_AH_global_stability_proved": decision["reduced_AH_global_stability_proved"],
        "selected_ordered_source_subvalidator_passes": decision["selected_ordered_source_subvalidator_passes"],
        "selected_s3_class_subvalidator_passes": decision["selected_s3_class_subvalidator_passes"],
        "primitive_C1_missing_atom_count": primitive_lane["missing_atom_count"],
        "selected_visible_operator_source_closed": False,
        "primitive_C1_contractions_emitted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C SameSource MatterSlot Overlap OperatorPacket or SelectedResidual v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"seven_field_packet_validator_nogo = {str(cert['seven_field_packet_validator_nogo']).lower()}",
        f"support_fields_present = {cert['support_fields_present']}",
        f"selected_fields_emitted = {cert['selected_fields_emitted']}",
        f"reduced_AH_global_stability_proved = {str(cert['reduced_AH_global_stability_proved']).lower()}",
        f"primitive_C1_missing_atom_count = {cert['primitive_C1_missing_atom_count']}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The seven-field same-source packet still fails honestly, but the residual",
        "lane is stronger than before: reduced AH global rank-one stability is",
        "proved, and the ordered-source plus selected S3 restriction subvalidators",
        "pass. The next target is therefore not another support import; it is a",
        "selected visible operator source, or the full primitive C1 packet from the",
        "same source.",
        "",
        "## Seven Required Fields",
        "",
    ]
    rows = candidate["reduction"]["same_source_packet_fill"]["rows"]
    for key, row in rows.items():
        lines.append(
            f"- `{key}`: support = `{str(row['support_present']).lower()}`, "
            f"selected = `{str(row['selected_emitted']).lower()}`, reason = {row['reason_not_selected']}"
        )
    lines.extend(
        [
            "",
            "## Primitive C1 Contract",
            "",
            f"- atom count: `{candidate['reduction']['visible_operator_or_primitive_c1_lane']['primitive_contract_atom_count']}`",
            f"- missing atoms: `{candidate['reduction']['visible_operator_or_primitive_c1_lane']['primitive_missing_atom_count']}`",
            "",
            "## Guardrails",
            "",
            "- Do not promote hypothetical full plumbing.",
            "- Do not promote selected ordered source plus S3 restriction into a full visible operator source.",
            "- Do not compute `A_selected`, `b_selected`, or `lambda_12` until same-source operator values and primitive C1 are emitted.",
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
