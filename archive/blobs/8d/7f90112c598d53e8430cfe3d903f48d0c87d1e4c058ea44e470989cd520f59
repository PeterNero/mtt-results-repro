"""Build the selected U1/Y Route-C hybrid Galerkin overlap source packet gate."""

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
    "matter_slot_overlap_gate": DATA / "selected_u1y_routec_matter_slot_overlap_normalization_source.candidate.json",
    "q79_matter_slot_overlap_reduction": Q79
    / "candidate_data"
    / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json",
    "q79_matter_slot_transversality_attempt": Q79
    / "candidate_data"
    / "selected_matter_slot_transversality_source_attempt.candidate.json",
    "q79_su5_qutrit_fixture": Q79 / "candidate_data" / "selected_su5_qutrit_polarization.unselected_fixture.json",
    "q79_su5_qutrit_fill_certificate": Q79
    / "certificates"
    / "selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json",
    "sm_operator_overlap_packet": SM
    / "candidate_data"
    / "selected_routec_selected_operator_source_and_overlap_tensor_packet.candidate.json",
    "sm_same_source_contract": SM
    / "candidate_data"
    / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_hybrid_galerkin_overlap_source_packet.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_hybrid_galerkin_overlap_source_packet_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_Hybrid_Galerkin_Overlap_Source_Packet_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    parent = load(INPUTS["matter_slot_overlap_gate"])
    q79_reduction = load(INPUTS["q79_matter_slot_overlap_reduction"])
    transversality = load(INPUTS["q79_matter_slot_transversality_attempt"])
    qutrit_fixture = load(INPUTS["q79_su5_qutrit_fixture"])
    qutrit_fill = load(INPUTS["q79_su5_qutrit_fill_certificate"])
    sm_overlap = load(INPUTS["sm_operator_overlap_packet"])
    sm_contract = load(INPUTS["sm_same_source_contract"])

    same_source = q79_reduction["matter_slot_overlap_reduction"]["same_source_operator_packet"]
    required_fields = same_source["required_fields"]
    selected_fields = {
        key: bool(value["selected_emitted"]) for key, value in required_fields.items()
    }
    support_fields = {
        key: bool(value["current_support"]) for key, value in required_fields.items()
    }

    field_rows = []
    for key, value in required_fields.items():
        field_rows.append(
            {
                "field": key,
                "required": value["required"],
                "support_present": bool(value["current_support"]),
                "selected_emitted": bool(value["selected_emitted"]),
                "status": "SELECTED_EMITTED" if value["selected_emitted"] else "OPEN_SELECTED_VALUE",
            }
        )

    validator_inputs = {
        "selected_source_verified": transversality["calculation_results"]["selected_source_verified"],
        "matter_slot_transversality_promotes": transversality["calculation_results"][
            "promotes_su5_matter_slot_transversality"
        ],
        "honest_route_c_residual_pass": transversality["route_c_status"]["honest_route_c_residual_pass"],
        "honest_de_action_pass": transversality["route_c_status"]["honest_de_action_pass"],
        "honest_riesz_gap_pass": transversality["route_c_status"]["honest_riesz_gap_pass"],
        "honest_reduced_green_pass": transversality["route_c_status"]["honest_reduced_green_pass"],
        "honest_dotd_response_pass": transversality["route_c_status"]["honest_dotd_response_pass"],
        "qutrit_fixture_selected_by_mtt": qutrit_fixture["source"]["selected_by_mtt"],
        "qutrit_fixture_only": qutrit_fixture["source"]["fixture_only"],
        "qutrit_finite_validator_passes": qutrit_fill["calculation_results"]["validator_passes_finite_algebra"],
        "qutrit_promotes_to_selected": qutrit_fill["calculation_results"]["promotes_to_selected_heavy_link_input"],
    }

    candidate = {
        "candidate": "SelectedU1YRouteCHybridGalerkinOverlapSourcePacket",
        "status": "U1Y_ROUTEC_HYBRID_GALERKIN_OVERLAP_PACKET_BUILT_VALUES_OPEN",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": parent["status"],
        "same_source_field_counts": same_source["field_counts"],
        "selected_fields": selected_fields,
        "support_fields": support_fields,
        "field_rows": field_rows,
        "validator_inputs": validator_inputs,
        "hybrid_packet_result": {
            "packet_constructed": True,
            "packet_closed": False,
            "all_required_fields_selected": same_source["all_required_fields_selected"],
            "selected_emitted_count": same_source["field_counts"]["selected_emitted"],
            "support_present_count": same_source["field_counts"]["support_present"],
            "required_count": same_source["field_counts"]["required"],
            "first_missing_selected_fields": same_source["first_missing_selected_fields"],
            "target_fitting_used": False,
        },
        "no_go_scope": {
            "current_source_record_no_go": True,
            "mathematical_impossibility_claimed": False,
            "reason": [
                "the finite qutrit/SU5 fixture validates algebra but is fixture_only and not selected_by_mtt",
                "the honest Route-C Galerkin packet has selected_source_verified=false",
                "honest residual, D_E, Riesz, reduced Green, and dotD validators do not all pass",
                "the same-source contract has zero selected fields emitted",
            ],
        },
        "what_closes": {
            "hybrid_packet_contract_imported": True,
            "seven_required_fields_enumerated": True,
            "support_vs_selected_audited": True,
            "finite_su5_fixture_rejected_as_selected": True,
            "routec_honest_validator_failures_retained": True,
            "single_next_fill_or_nogo_artifact_identified": True,
        },
        "what_remains_open": {
            "source_identity": not selected_fields["source_identity"],
            "matter_slot_charge": not selected_fields["matter_slot_charge"],
            "singlet_neutrino_rule": not selected_fields["singlet_neutrino_rule"],
            "operator_values": not selected_fields["operator_values"],
            "overlap_transfer": not selected_fields["overlap_transfer"],
            "normalization": not selected_fields["normalization"],
            "primitive_contractions": not selected_fields["primitive_contractions"],
            "A_selected_and_b_selected": True,
            "lambda_12": True,
            "full_SM_or_no_knob_closure": True,
        },
        "decision": {
            "best_next_artifact": "Selected_U1Y_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1",
            "selected_packet_closed": False,
            "current_source_record_no_go": True,
            "conditional_support_broad": same_source["source_level_support_broad"],
            "selected_values_open": same_source["selected_values_open"],
            "target_fitting_used": False,
        },
        "next_artifact_contract": {
            "name": "Selected_U1Y_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1",
            "must_either": [
                "fill all seven required fields from one same-source packet and rerun validators",
                "or prove a no-go for the current source record that identifies the exact source amendment needed",
            ],
            "required_fields": list(required_fields.keys()),
            "must_reject": sm_contract["validator_contract"]["must_reject"],
        },
        "guardrails": {
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_lambda12": False,
            "claims_full_sm_closure": False,
            "uses_locked_target_columns_as_selector": False,
            "uses_observed_masses_or_ckm_inputs": False,
            "promotes_fixture_as_selected": False,
        },
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCHybridGalerkinOverlapSourcePacket",
        "status": candidate["status"],
        "packet_closed": False,
        "current_source_record_no_go": True,
        "selected_emitted_count": same_source["field_counts"]["selected_emitted"],
        "support_present_count": same_source["field_counts"]["support_present"],
        "required_count": same_source["field_counts"]["required"],
        "next_artifact": candidate["decision"]["best_next_artifact"],
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C Hybrid Galerkin Overlap Source Packet v1",
        "",
        "## Result",
        "",
        "```text",
        f"packet_closed = {str(candidate['hybrid_packet_result']['packet_closed']).lower()}",
        f"current_source_record_no_go = {str(candidate['decision']['current_source_record_no_go']).lower()}",
        f"required_count = {candidate['hybrid_packet_result']['required_count']}",
        f"support_present_count = {candidate['hybrid_packet_result']['support_present_count']}",
        f"selected_emitted_count = {candidate['hybrid_packet_result']['selected_emitted_count']}",
        f"lambda_12_closed = {str(cert['lambda_12_closed']).lower()}",
        f"best_next_artifact = {candidate['decision']['best_next_artifact']}",
        "```",
        "",
        "The hybrid Galerkin/overlap packet is now built as a strict same-source",
        "fill-or-no-go gate. It does not close the source. It proves that the",
        "current record has broad conditional support but emits none of the seven",
        "required selected same-source fields.",
        "",
        "## Required Fields",
        "",
        "| Field | Support | Selected | Status |",
        "| --- | --- | --- | --- |",
    ]
    for row in candidate["field_rows"]:
        lines.append(
            f"| `{row['field']}` | `{str(row['support_present']).lower()}` | `{str(row['selected_emitted']).lower()}` | `{row['status']}` |"
        )
    lines.extend(
        [
            "",
            "## Current No-Go Scope",
            "",
        ]
    )
    for reason in candidate["no_go_scope"]["reason"]:
        lines.append(f"- {reason}")
    lines.extend(
        [
            "",
            "This is a no-go for the current source record only. It is not a proof",
            "that the selected packet cannot exist.",
            "",
            "## Next Artifact",
            "",
            f"`{candidate['next_artifact_contract']['name']}` must either:",
            "",
        ]
    )
    for item in candidate["next_artifact_contract"]["must_either"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "It must reject:",
            "",
        ]
    )
    for item in candidate["next_artifact_contract"]["must_reject"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not promote finite SU5/qutrit fixture data as selected.",
            "- Do not promote lifted selected-source flags.",
            "- Do not use locked target columns as source selectors.",
            "- Do not claim `A_selected`, `b_selected`, `lambda_12`, or full SM closure.",
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
