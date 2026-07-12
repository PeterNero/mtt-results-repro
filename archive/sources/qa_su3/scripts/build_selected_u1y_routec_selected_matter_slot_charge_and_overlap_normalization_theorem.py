"""Build the selected U1/Y Route-C matter-slot charge/overlap theorem gate."""

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
    "u1y_value_gate": DATA / "selected_u1y_routec_samesource_chernweil_operator_functional_value.candidate.json",
    "u1y_prior_matter_gate": DATA / "selected_u1y_routec_matter_slot_overlap_normalization_source.candidate.json",
    "q79_matter_theorem": Q79 / "candidate_data" / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json",
    "q79_same_source_operator_packet": Q79 / "candidate_data" / "q79_samesource_operatorpacket_fill_or_nogo.candidate.json",
    "sm_matter_theorem": SM / "candidate_data" / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json",
    "sm_same_source_operator_packet": SM / "candidate_data" / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json",
    "sm_c1_routing_normalization": SM / "candidate_data" / "selected_routec_selected_c1_routing_normalization_and_overlap_source_packet.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1.md"

STATUS = "U1Y_ROUTEC_SELECTED_MATTERSLOT_CHARGE_OVERLAP_THEOREM_REDUCED_SAMESOURCE_OPERATOR_PACKET_OPEN"
NEXT = "Selected_U1Y_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def status(path: Path, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": rel(path),
        "present": path.exists(),
        "status": data.get("status", data.get("certificate", "UNKNOWN")),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    u1y_value = load(INPUTS["u1y_value_gate"])
    u1y_prior = load(INPUTS["u1y_prior_matter_gate"])
    q79_theorem = load(INPUTS["q79_matter_theorem"])
    q79_packet = load(INPUTS["q79_same_source_operator_packet"])
    sm_theorem = load(INPUTS["sm_matter_theorem"])
    sm_packet = load(INPUTS["sm_same_source_operator_packet"])
    sm_c1 = load(INPUTS["sm_c1_routing_normalization"])

    q79_reduction = q79_theorem["matter_slot_overlap_reduction"]
    same_source_packet = q79_reduction["same_source_operator_packet"]
    required_fields = same_source_packet["required_fields"]

    theorem = {
        "name": "U1YRouteCSelectedMatterSlotChargeAndOverlapNormalizationReductionTheorem",
        "proved": True,
        "closure_claimed": False,
        "statement": (
            "For the selected U1/Y Route-C alpha1 branch, the matter-slot charge "
            "and overlap-normalization theorem reduces to a single same-source "
            "operator packet. Finite SU(5) transversality, qutrit Weyl support, "
            "conditional C1 routing Z->{u,e}, X->{d,nuD}, and conditional "
            "normalization are already available and exact. They are not sufficient "
            "as proof because the selected same-source packet emits zero of seven "
            "required selected fields: source identity, matter-slot charge, 1_M "
            "Dirac-neutrino rule, operator values, overlap transfer, normalization, "
            "and primitive contractions. If those fields are emitted by one source, "
            "then N_alpha1(h_ext)=1 promotes to du/dalpha1=h_ext and the U1/Y "
            "dotD_alpha1 driver can be verified by theorem."
        ),
        "proof_steps": [
            "Import q79 theorem: finite SU(5) transversality, source-level Weyl support, and conditional C1 routing/normalization are present.",
            "Import SM theorem: the same matter-slot and overlap-normalization theorem is reduced to the same-source operator packet.",
            "Check the same-source packet contract: seven fields are required, six have support, zero are selected-emitted.",
            "The only missing support field is the 1_M Dirac-neutrino routing rule; the other six still fail selected-emission/provenance.",
            "Therefore the finite algebra is not the blocker; selected same-source emission is the blocker.",
            "Connect to U1/Y alpha1 value gate: selected emission of these fields is sufficient to promote N_alpha1(h_ext)=1 to du/dalpha1=h_ext.",
        ],
    }

    field_table = {
        key: {
            "required": value["required"],
            "current_support": value["current_support"],
            "selected_emitted": value["selected_emitted"],
            "blocks_promotion": not value["selected_emitted"],
        }
        for key, value in required_fields.items()
    }

    promotion_theorem = {
        "if_all_same_source_fields_selected": {
            "selected_matter_slot_charge_closed": True,
            "selected_overlap_normalization_closed": True,
            "selected_transfer_normalization_closed": True,
            "selected_value_N_alpha1_h_ext_promoted": True,
            "du_dalpha1_equals_h_ext_emitted": True,
            "alpha1_driver_verified": True,
            "honest_dotD_replay_enabled": True,
        },
        "currently": {
            "field_count_required": same_source_packet["field_counts"]["required"],
            "field_count_support_present": same_source_packet["field_counts"]["support_present"],
            "field_count_selected_emitted": same_source_packet["field_counts"]["selected_emitted"],
            "selected_value_N_alpha1_h_ext_promoted": False,
            "du_dalpha1_equals_h_ext_emitted": False,
            "alpha1_driver_verified": False,
            "honest_dotD_replay_enabled": False,
        },
    }

    decision = {
        "matter_slot_charge_overlap_theorem_constructed": True,
        "theorem_reduction_proved": True,
        "finite_algebra_is_not_blocker": q79_reduction["decision"]["finite_algebra_is_not_blocker"],
        "conditional_routing_and_normalization_exact": q79_reduction["proved_imported_support"]["conditional_routing_and_normalization_exact"],
        "same_source_operator_packet_required": q79_reduction["decision"]["same_source_operator_packet_required"],
        "same_source_packet_values_emitted": False,
        "selected_matter_slot_charge_closed": False,
        "selected_overlap_normalization_closed": False,
        "selected_transfer_normalization_closed": False,
        "selected_value_N_alpha1_h_ext_promoted": False,
        "du_dalpha1_equals_h_ext_emitted": False,
        "alpha1_driver_verified_now": False,
        "honest_dotD_validator_closed_now": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCSelectedMatterSlotChargeAndOverlapNormalizationTheorem",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {key: status(path, load(path)) for key, path in INPUTS.items()},
        "theorem": theorem,
        "field_table": field_table,
        "same_source_operator_packet_summary": {
            "contract_status": same_source_packet["contract_status"],
            "field_counts": same_source_packet["field_counts"],
            "first_missing_selected_fields": same_source_packet["first_missing_selected_fields"],
            "support_fields": same_source_packet["support_fields"],
            "selected_fields": same_source_packet["selected_fields"],
            "packet_closed": same_source_packet["packet_closed"],
        },
        "support_closures": {
            "finite_su5_transversality_under_source_hypothesis_closed": q79_reduction["proved_imported_support"]["finite_su5_transversality_under_source_hypothesis_closed"],
            "source_level_weyl_carrier_closed": q79_reduction["proved_imported_support"]["source_level_weyl_carrier_closed"],
            "conditional_A_rank_and_solve_closed": q79_reduction["proved_imported_support"]["conditional_A_rank_and_solve_closed"],
            "conditional_source_to_c1_transfer_exact": q79_reduction["proved_imported_support"]["conditional_source_to_c1_transfer_exact"],
            "conditional_routing_and_normalization_exact": q79_reduction["proved_imported_support"]["conditional_routing_and_normalization_exact"],
            "su5_e6_partition_matches_required_route": q79_reduction["proved_imported_support"]["su5_e6_partition_matches_required_route"],
            "candidate_value_N_alpha1_h_ext": u1y_value["decision"]["support_candidate_value_N_alpha1_h_ext"],
        },
        "promotion_theorem": promotion_theorem,
        "decision": decision,
        "what_closes_now": {
            "matter_slot_charge_overlap_theorem_reduction": True,
            "support_vs_selected_field_counts_imported": True,
            "alpha1_value_promotion_boundary_defined": True,
            "same_source_operator_packet_identified_as_only_current_gate": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "emit_selected_source_identity": True,
            "emit_selected_matter_slot_charge": True,
            "prove_selected_1M_neutrino_rule": True,
            "emit_selected_DE_dotD_Riesz_Green_operator_values": True,
            "emit_selected_overlap_transfer_functor": True,
            "emit_selected_normalization_and_b_selected": True,
            "emit_selected_primitive_contractions": True,
            "promote_N_alpha1_h_ext_to_selected_value": True,
            "honest_dotD_alpha1_replay": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_matter_slot_charge": False,
            "claims_selected_overlap_normalization": False,
            "claims_selected_N_alpha1_value": False,
            "claims_alpha1_driver_verified": False,
            "claims_honest_dotD_validator_closed": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_full_sm_closure": False,
            "uses_locked_target_columns_as_selector": False,
            "uses_observed_or_benchmark_inputs": False,
            "uses_diagnostic_lift_as_proof": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCSelectedMatterSlotChargeAndOverlapNormalizationTheorem",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "theorem_reduction_proved": True,
        "finite_algebra_is_not_blocker": True,
        "same_source_packet_required": True,
        "field_count_required": same_source_packet["field_counts"]["required"],
        "field_count_support_present": same_source_packet["field_counts"]["support_present"],
        "field_count_selected_emitted": same_source_packet["field_counts"]["selected_emitted"],
        "candidate_value_N_alpha1_h_ext": u1y_value["decision"]["support_candidate_value_N_alpha1_h_ext"],
        "selected_value_N_alpha1_h_ext_promoted": False,
        "alpha1_driver_verified_now": False,
        "honest_dotD_validator_closed_now": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C Selected MatterSlot Charge and Overlap Normalization Theorem v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"theorem_reduction_proved = {str(cert['theorem_reduction_proved']).lower()}",
        f"finite_algebra_is_not_blocker = {str(cert['finite_algebra_is_not_blocker']).lower()}",
        f"field_count_required = {cert['field_count_required']}",
        f"field_count_support_present = {cert['field_count_support_present']}",
        f"field_count_selected_emitted = {cert['field_count_selected_emitted']}",
        f"candidate_value_N_alpha1_h_ext = {cert['candidate_value_N_alpha1_h_ext']}",
        f"selected_value_N_alpha1_h_ext_promoted = {str(cert['selected_value_N_alpha1_h_ext_promoted']).lower()}",
        f"alpha1_driver_verified_now = {str(cert['alpha1_driver_verified_now']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "## Theorem",
        "",
        candidate["theorem"]["statement"],
        "",
        "## Same-Source Field Table",
        "",
        "| Field | Support | Selected | Required |",
        "| --- | --- | --- | --- |",
    ]
    for field, row in candidate["field_table"].items():
        lines.append(
            f"| `{field}` | `{str(row['current_support']).lower()}` | "
            f"`{str(row['selected_emitted']).lower()}` | {row['required']} |"
        )
    lines.extend(
        [
            "",
            "## Promotion Boundary",
            "",
            "If the seven fields are emitted by one selected source, this theorem",
            "promotes `N_alpha1(h_ext)=1` to `du/dalpha1=h_ext`, flips",
            "`alpha1_driver_verified` by theorem, and enables honest dotD replay.",
            "At present, zero fields are selected-emitted, so this packet is a",
            "closed reduction rather than final dotD closure.",
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
    missing = [str(path) for path in INPUTS.values() if not path.exists()]
    if missing:
        print("Missing inputs:")
        print("\n".join(missing))
        return 1
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
