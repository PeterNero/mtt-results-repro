"""Build smooth-operator source packet or complement-quotient interface."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "required_packet": DATA / "selected_heterotic_projectiverhoe_smooth_operator_source_packet_required.json",
    "trace_lift_gate": DATA / "selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart.candidate.json",
    "twisted_source_fill": DATA / "twisted_source_promotion_packet_fill_attempt.candidate.json",
    "rplus_payload": DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json",
    "finite_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "complement_gate": DATA / "complement_spectrum_or_smooth_operator_source.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_or_complementquotient.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_or_complementquotient_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket.template.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SmoothOperator_SourcePacket_or_ComplementQuotientTheorem_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHOPERATOR_SOURCEPACKET_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothOperator_SourcePacket_FillAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    required = load(INPUTS["required_packet"])
    trace_gate = load(INPUTS["trace_lift_gate"])
    twisted = load(INPUTS["twisted_source_fill"])
    rplus = load(INPUTS["rplus_payload"])
    finite_packet = load(INPUTS["finite_packet"])
    complement = load(INPUTS["complement_gate"])

    complement_lane = {
        "lane_id": "A_exact_complement_quotient_or_cancellation",
        "accepted_if": {
            "smooth_complement_outside_QaSU3_threshold_response": None,
            "BRST_or_coherent_sector_exact_cancellation": None,
            "no_double_count_of_FP_BRST_or_GR_surface_determinants": None,
            "finite_projective_packet_is_entire_selected_threshold_domain": None,
        },
        "current_support": {
            "finite_internal_quotient_policy_closed": trace_gate["lanes"]["complement_quotient"]["support"]["finite_internal_quotient_policy_closed"],
            "conditional_log2008_isolated": complement["reduced_determinant_conditional"]["value"] == "log(2008)",
            "GR_internal_separation_used": trace_gate["lanes"]["complement_quotient"]["support"]["GR_internal_separation_already_used"],
        },
        "closes_now": False,
        "why_not": "current source gives internal routing support but not an exact smooth complement quotient/cancellation theorem",
    }

    smooth_packet_lane = {
        "lane_id": "B_selected_smooth_operator_source_packet",
        "accepted_if": required["minimum_smooth_operator_payload"],
        "current_support": {
            "same_branch_strominger_iwasawa_context": twisted["fill_result"]["source_family_selected"],
            "fixed_differential_class_context": twisted["fill_result"]["fixed_differential_class_context_found"],
            "primitive_central_support": twisted["fill_result"]["primitive_central_support_available"],
            "twist_cancellation_table": twisted["fill_result"]["twist_cancellation_table_available"],
            "projective_validator_pattern": twisted["fill_result"]["projective_validator_pattern_available"],
            "Rplus_geometry_available": rplus["decision"]["R_plus_curvature_filled"],
            "finite_projective_packet_selected": finite_packet["selected"],
        },
        "current_missing": {
            "selected_Qa_SU3_representative_found": twisted["fill_result"]["selected_Qa_SU3_representative_found"],
            "period_denominator_or_smooth_unit_selected": twisted["fill_result"]["period_denominator_or_smooth_unit_selected"],
            "central_cocycle_map_verified": twisted["fill_result"]["central_cocycle_map_verified"],
            "projective_rhoE_tables_supplied": twisted["fill_result"]["projective_rhoE_tables_supplied"],
            "selected_D_E_dotD_response_supplied": twisted["fill_result"]["selected_D_E_dotD_response_supplied"],
            "mapped_Freed_Witten_verified": twisted["fill_result"]["mapped_Freed_Witten_verified"],
            "twisted_projector_retention_verified": twisted["fill_result"]["twisted_projector_retention_verified"],
            "E_Qa_matrix_or_finitepart_table": False,
        },
        "closes_now": False,
        "why_not": "source context is strong, but selected representative, cocycle map, response tables, and finite part are absent",
    }

    torsion_lane = {
        "lane_id": "C_source_certified_heat_zeta_torsion_replacement",
        "accepted_if": {
            "selected_threshold_operator_or_torsion_complex": None,
            "positive_spectrum_or_acyclic_torsion_complex": None,
            "regularization_scale_and_zero_mode_policy": None,
            "trace_weight_or_index_policy": None,
            "proof_same_branch_as_projective_rhoE_packet": None,
        },
        "current_support": {
            "finite_internal_response_packet_available": finite_packet["selected"],
            "twisted_source_context_available": twisted["fill_result"]["source_family_selected"],
        },
        "closes_now": False,
        "why_not": "no source-certified heat/zeta/torsion finite-part table is emitted",
    }

    template = {
        "schema": "SelectedHeteroticProjectiveRhoESmoothOperatorSourcePacket.Template.v1",
        "status": "OPEN_VALUES_REQUIRED",
        "next_required_artifact": NEXT,
        "source_certificate": {
            "same_branch_Qa_SU3_projective_threshold_source": None,
            "selected_by_MTT_before_target_comparison": None,
            "no_observed_coupling_or_scale_input": True,
        },
        "smooth_projective_source": {
            "Deligne_Cech_or_B_field_representative": None,
            "period_denominator_or_smooth_unit": None,
            "representative_to_central_cocycle_map": None,
            "projective_rhoE_transition_tables": None,
        },
        "bundle_operator": {
            "selected_connection_A_or_equivalent_operator_source": None,
            "curvature_F_A": None,
            "representation_action_on_uE_one_forms": None,
            "kernel_and_quotient_policy": None,
            "E_Qa_matrix_or_zero_order_block": None,
        },
        "finite_part": {
            "positive_spectrum_or_heat_coefficients": None,
            "zeta_or_torsion_regularization": None,
            "trace_lift_or_complement_quotient_proof": None,
            "finite_part_value": None,
        },
        "admissibility": {
            "Freed_Witten_or_twisted_admissibility": None,
            "Bianchi_or_Green_Schwarz_mapping": None,
            "projector_retention": None,
            "no_double_count_policy": None,
        },
        "forbidden_shortcuts": required["forbidden_shortcuts"],
    }

    decision = {
        "interface_built": True,
        "complement_quotient_theorem_closed": False,
        "smooth_operator_source_packet_filled": False,
        "heat_zeta_torsion_replacement_filled": False,
        "E_Qa_computed": False,
        "best_next_lane": "B_selected_smooth_operator_source_packet",
        "next_required_artifact": NEXT,
        "template_path": rel(OUTPUT_TEMPLATE),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESmoothOperatorSourcePacketOrComplementQuotientTheorem",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "trace_lift_gate": trace_gate["status"],
            "twisted_source_fill": twisted["status"],
            "rplus_payload": rplus["status"],
            "complement_gate": complement["status"],
        },
        "lanes": {
            "complement_quotient": complement_lane,
            "smooth_operator_source_packet": smooth_packet_lane,
            "heat_zeta_torsion_replacement": torsion_lane,
        },
        "decision": decision,
        "guardrails": {
            "does_not_fill_template_by_convenience": True,
            "does_not_promote_q79_validator_tables": True,
            "does_not_promote_Rplus_as_bundle_curvature": True,
            "does_not_claim_complement_cancellation": True,
            "does_not_claim_E_Qa": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "ProjectiveRhoESmoothOperatorSourcePacketInterfaceTheorem",
            "proved": True,
            "statement": (
                "The smooth closure problem is now reduced to three accepted payloads: "
                "an exact smooth complement quotient/cancellation theorem, a selected "
                "smooth projective rho_E bundle/operator source packet, or a source-"
                "certified heat/zeta/torsion finite-part replacement. Current data give "
                "support for the projective/Strominger source context and R+ geometry, "
                "but fill none of the required source values."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "interface_built": True,
        "smooth_operator_source_packet_filled": False,
        "complement_quotient_theorem_closed": False,
        "E_Qa_computed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SmoothOperator SourcePacket or ComplementQuotientTheorem v1

## Result

```text
status = {STATUS}
interface_built = true
smooth_operator_source_packet_filled = false
complement_quotient_theorem_closed = false
E_Qa_computed = false
next_required_artifact = {NEXT}
```

## Best Next Lane

The strongest live lane is the smooth projective source packet. It already has
same-branch Strominger/Iwasawa context, fixed differential-class context,
primitive central support, twist-cancellation support, projective validator
patterns, `R^+` geometry, and the selected finite projective packet.

It still needs the actual selected values:

```text
{rel(OUTPUT_TEMPLATE)}
```

The complement-quotient route remains legal, but it needs an exact theorem that
the smooth complement is outside the Qa/SU3 response or cancels without double
counting.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_TEMPLATE)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
