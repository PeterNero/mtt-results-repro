"""Build the U1/Y Route-C selected visible operator source or primitive C1 gate."""

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
    "u1y_samesource_packet_gate": DATA / "selected_u1y_routec_samesource_matter_slot_overlap_operatorpacket_or_selected_residual.candidate.json",
    "q79_visible_operator_or_primitive_c1": Q79 / "certificates" / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions_certificate.json",
    "q79_de_green_dotd_source_gate": Q79 / "certificates" / "q79_selected_de_green_dotd_source_for_primitive_c1_certificate.json",
    "q79_same_source_operator_provenance": Q79 / "certificates" / "q79_same_source_operator_provenance_or_selected_routec_solve_certificate.json",
    "q79_selected_monad_l2_operator_frontier": Q79 / "certificates" / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual_certificate.json",
    "q79_ah_goodcover_hym_bridge": Q79 / "certificates" / "q79_selected_ah_goodcover_promotion_hym_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_selected_visible_operator_source_or_primitive_c1_contractions.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_selected_visible_operator_source_or_primitive_c1_contractions_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_SelectedVisibleOperatorSource_or_PrimitiveC1Contractions_v1.md"

STATUS = "U1Y_ROUTEC_VISIBLE_OPERATOR_OR_PRIMITIVE_C1_REDUCED_SOURCE_CERT_OR_TYPED_DE_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedSourceCertificate_or_TypedDEConstruction_v1"


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
    local_parent = load(INPUTS["u1y_samesource_packet_gate"])
    visible_or_c1 = load(INPUTS["q79_visible_operator_or_primitive_c1"])
    de_green = load(INPUTS["q79_de_green_dotd_source_gate"])
    provenance = load(INPUTS["q79_same_source_operator_provenance"])
    monad_frontier = load(INPUTS["q79_selected_monad_l2_operator_frontier"])
    ah_hym = load(INPUTS["q79_ah_goodcover_hym_bridge"])

    source_lane = visible_or_c1["source_lane"]
    primitive_lane = visible_or_c1["primitive_c1_lane"]
    missing_scan = visible_or_c1["selected_missing_data_scan"]
    routec_stack = de_green["current_routec_stack"]
    source_gate = de_green["primitive_c1_source_gate"]
    same_source_reduction = provenance["same_source_reduction"]
    monad_route = monad_frontier["operator_pic0_and_routec_residual_frontier"]
    hym_bridge = ah_hym["promotion_summary"]

    decision = {
        "selected_ordered_source_subvalidator_passes": source_lane["subvalidators"]["ordered_source"]["exit_code"] == 0,
        "selected_s3_class_subvalidator_passes": source_lane["subvalidators"]["s3_class_restriction"]["exit_code"] == 0,
        "selected_visible_operator_source_validator_passes": False,
        "current_routec_arithmetic_passes_if_selected_flags_supplied": routec_stack["hypothetical_selected_flags_all_pass"],
        "honest_current_routec_stack_rejected_without_selected_source": True,
        "first_blocking_layer": missing_scan["first_blocking_layer"],
        "primitive_c1_contract_atom_count": primitive_lane["contract_atom_count"],
        "primitive_c1_missing_atom_count": primitive_lane["missing_atom_count"],
        "primitive_c1_matrices_emitted": False,
        "selected_DE_Green_dotD_source_proved": False,
        "selected_source_certificate_emitted": False,
        "typed_DE_construction_emitted": False,
        "A_selected_or_b_selected_emitted": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    reduction = {
        "visible_operator_source_lane": {
            "status": visible_or_c1["status"],
            "validator_status": source_lane["validator_status"],
            "open_items": source_lane["open_items"],
            "subvalidators": source_lane["subvalidators"],
            "selected_missing_data_scan": missing_scan,
        },
        "primitive_c1_lane": {
            "status": source_gate["status"],
            "atom_count": primitive_lane["contract_atom_count"],
            "missing_atom_count": primitive_lane["missing_atom_count"],
            "missing_atoms": primitive_lane["missing_atoms"],
            "sector_slots": source_gate["sector_slots"],
            "terms": source_gate["terms"],
        },
        "de_green_dotd_source_lane": {
            "status": de_green["status"],
            "original_failures_are_source_or_provenance_flags": routec_stack["original_failures_are_source_or_provenance_flags"],
            "hypothetical_selected_flags_validators": routec_stack["hypothetical_selected_flags_validators"],
            "interpretation": routec_stack["interpretation"],
            "next_required_artifact": de_green["next_required_artifact"],
        },
        "same_source_operator_provenance_lane": {
            "status": provenance["status"],
            "honest_current_open_items": same_source_reduction["honest_current_open_items"],
            "diagnostic_full_plumbing_passes": same_source_reduction["full_plumbing_diagnostic_status"] == "PASS",
            "no_primitive_diagnostic_open_items": same_source_reduction["no_primitive_open_items"],
        },
        "monad_l2_and_hym_bridge_support": {
            "selected_monad_l2_status": monad_frontier["status"],
            "selected_monad_l2_closes": monad_frontier["what_closes_now"],
            "conditional_hym_bridge_status": ah_hym["status"],
            "conditional_hym_bridge_summary": hym_bridge,
        },
    }

    theorem = {
        "name": "U1YRouteCVisibleOperatorOrPrimitiveC1ReductionTheorem",
        "proved": True,
        "statement": (
            "The U1/Y Route-C visible operator source and primitive C1 target is "
            "now executable but not closed. The selected ordered source and S3 "
            "restriction subvalidators pass, and the finite Route-C D_E/Riesz/"
            "Green/dotD arithmetic has no validator-detected obstruction under "
            "diagnostic selected-source flags. The honest packet still fails "
            "because selected source provenance, same-source Chern-Weil/GS row, "
            "operator execution, same-branch derivative, orientation selection, "
            "and all 24 primitive C1 matrices are absent. Therefore the next "
            "decisive object is a selected Route-C source certificate or a typed "
            "D_E construction from selected monad/Cech data."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCSelectedVisibleOperatorSourceOrPrimitiveC1Contractions",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            key: status_of(key, data)
            for key, data in {
                "u1y_samesource_packet_gate": local_parent,
                "q79_visible_operator_or_primitive_c1": visible_or_c1,
                "q79_de_green_dotd_source_gate": de_green,
                "q79_same_source_operator_provenance": provenance,
                "q79_selected_monad_l2_operator_frontier": monad_frontier,
                "q79_ah_goodcover_hym_bridge": ah_hym,
            }.items()
        },
        "decision": decision,
        "reduction": reduction,
        "theorem": theorem,
        "what_closes_now": {
            "visible_operator_source_validator_contract_imported": True,
            "selected_ordered_source_subvalidator_pass_imported": True,
            "selected_s3_class_subvalidator_pass_imported": True,
            "routec_arithmetic_reduced_to_selected_source_provenance": True,
            "primitive_c1_24_atom_dependency_map_imported": True,
            "next_decisive_source_certificate_or_typed_DE_target_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_visible_bundle_operator_source_certificate": True,
            "selected_RouteC_source_certificate": True,
            "typed_DE_construction_from_selected_monad_or_Cech_data": True,
            "same_source_ChernWeil_GS_row": True,
            "selected_DE_rhoE_Riesz_Green_dotD": True,
            "selected_DeltaTheta_C1_Hessian_or_kernel_derivative": True,
            "orientation_selection_justified_by_same_source": True,
            "all_24_primitive_C1_3x3_matrices": True,
            "selected_C1_response_matrices": True,
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
            "claims_selected_DE_Green_dotD_source": False,
            "claims_primitive_C1_values": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "promotes_diagnostic_selected_flags": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCSelectedVisibleOperatorSourceOrPrimitiveC1Contractions",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "selected_ordered_source_subvalidator_passes": decision["selected_ordered_source_subvalidator_passes"],
        "selected_s3_class_subvalidator_passes": decision["selected_s3_class_subvalidator_passes"],
        "current_routec_arithmetic_passes_if_selected_flags_supplied": decision["current_routec_arithmetic_passes_if_selected_flags_supplied"],
        "selected_visible_operator_source_closed": False,
        "selected_DE_Green_dotD_source_proved": False,
        "primitive_c1_missing_atom_count": decision["primitive_c1_missing_atom_count"],
        "primitive_c1_matrices_emitted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    primitive = candidate["reduction"]["primitive_c1_lane"]
    lines = [
        "# Selected U1Y Route-C SelectedVisibleOperatorSource or PrimitiveC1Contractions v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"selected_ordered_source_subvalidator_passes = {str(cert['selected_ordered_source_subvalidator_passes']).lower()}",
        f"selected_s3_class_subvalidator_passes = {str(cert['selected_s3_class_subvalidator_passes']).lower()}",
        f"current_routec_arithmetic_passes_if_selected_flags_supplied = {str(cert['current_routec_arithmetic_passes_if_selected_flags_supplied']).lower()}",
        f"selected_visible_operator_source_closed = {str(cert['selected_visible_operator_source_closed']).lower()}",
        f"selected_DE_Green_dotD_source_proved = {str(cert['selected_DE_Green_dotD_source_proved']).lower()}",
        f"primitive_c1_missing_atom_count = {cert['primitive_c1_missing_atom_count']}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "This gate does not close by calculation. It shows the finite Route-C stack",
        "has no detected arithmetic obstruction after hypothetical selected-source",
        "flags, while the honest packet still lacks a source certificate or typed",
        "`D_E` construction. Primitive C1 remains blocked until those source data",
        "exist.",
        "",
        "## Primitive C1 Slots",
        "",
    ]
    for sector, slots in primitive["sector_slots"].items():
        lines.append(f"- `{sector}`: left `{slots['left']}`, right `{slots['right']}`, Higgs `{slots['higgs']}`")
    lines.extend(
        [
            "",
            "## Required Terms Per Sector",
            "",
        ]
    )
    for term in primitive["terms"]:
        lines.append(f"- `{term}`")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not promote diagnostic selected-source flags.",
            "- Do not treat selected ordered source plus S3 restriction as a complete visible operator source.",
            "- Do not fill primitive C1 matrices from benchmark or observed flavor data.",
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
