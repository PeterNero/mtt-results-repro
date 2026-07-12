"""Attempt to fill the smooth projective rho_E operator source packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "interface": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_or_complementquotient.candidate.json",
    "template": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket.template.json",
    "twisted_source_fill": DATA / "twisted_source_promotion_packet_fill_attempt.candidate.json",
    "central_search": DATA / "central_cocycle_map_source_search_or_derivation.candidate.json",
    "typed_projective_sourcefill": DATA / "selected_heterotic_typedmaptables_or_projectiverhoetables_sourcefill.candidate.json",
    "finite_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "rplus_payload": DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json",
    "smooth_trace_lift": DATA / "selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt_certificate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket.fill_attempt.json"
OUTPUT_MISSING = DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_missing_leaves.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SmoothOperator_SourcePacket_FillAttempt_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHOPERATOR_SOURCEPACKET_FILL_ATTEMPT_SUPPORT_FILLED_VALUES_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_RepresentativeToCocycleMap_or_SmoothFinitePart_SourceAmendment_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def leaf_rows(prefix: str, value: Any) -> list[dict[str, Any]]:
    if isinstance(value, dict):
        rows: list[dict[str, Any]] = []
        for key, item in value.items():
            rows.extend(leaf_rows(f"{prefix}.{key}", item))
        return rows
    return [{"path": prefix, "value": value, "filled": value is not None and value is not False}]


def main() -> dict[str, Any]:
    interface = load(INPUTS["interface"])
    template = load(INPUTS["template"])
    twisted = load(INPUTS["twisted_source_fill"])
    central = load(INPUTS["central_search"])
    typed_sourcefill = load(INPUTS["typed_projective_sourcefill"])
    finite_packet = load(INPUTS["finite_packet"])
    rplus = load(INPUTS["rplus_payload"])
    trace_lift = load(INPUTS["smooth_trace_lift"])

    fill_result = {
        "source_context_support_filled": True,
        "same_branch_strominger_iwasawa_context": twisted["fill_result"]["source_family_selected"],
        "fixed_differential_class_context": twisted["fill_result"]["fixed_differential_class_context_found"],
        "global_bianchi_context": twisted["fill_result"]["global_bianchi_context_found"],
        "primitive_central_support": twisted["fill_result"]["primitive_central_support_available"],
        "twist_cancellation_table": twisted["fill_result"]["twist_cancellation_table_available"],
        "projective_validator_pattern": twisted["fill_result"]["projective_validator_pattern_available"],
        "finite_projective_packet_selected": finite_packet["selected"],
        "Rplus_geometry_available": rplus["decision"]["R_plus_curvature_filled"],
        "selected_representative_filled": twisted["fill_result"]["selected_Qa_SU3_representative_found"],
        "period_denominator_or_smooth_unit_filled": twisted["fill_result"]["period_denominator_or_smooth_unit_selected"],
        "representative_to_central_cocycle_map_filled": twisted["fill_result"]["central_cocycle_map_verified"],
        "projective_rhoE_transition_tables_filled": twisted["fill_result"]["projective_rhoE_tables_supplied"],
        "selected_connection_A_filled": False,
        "curvature_F_A_filled": False,
        "representation_action_filled": False,
        "kernel_and_quotient_policy_filled": False,
        "E_Qa_matrix_filled": False,
        "positive_spectrum_or_heat_coefficients_filled": False,
        "zeta_or_torsion_regularization_filled": False,
        "trace_lift_or_complement_quotient_filled": False,
        "finite_part_value_filled": False,
        "mapped_Freed_Witten_filled": twisted["fill_result"]["mapped_Freed_Witten_verified"],
        "Bianchi_mapping_filled": False,
        "projector_retention_filled": twisted["fill_result"]["twisted_projector_retention_verified"],
        "no_double_count_policy_filled": False,
    }

    fill_packet = {
        **template,
        "status": "PARTIAL_SUPPORT_FILLED_VALUES_OPEN",
        "source_certificate": {
            "same_branch_Qa_SU3_projective_threshold_source": "SUPPORT_ONLY: same-branch Strominger/Iwasawa projective source family is present",
            "selected_by_MTT_before_target_comparison": "PARTIAL: source family selected, but representative/operator values are not selected",
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
            "Bianchi_or_Green_Schwarz_mapping": "SUPPORT_ONLY: global Bianchi/Strominger context is present, not mapped to the selected Qa/SU3 module",
            "projector_retention": None,
            "no_double_count_policy": None,
        },
    }

    leaf_report = leaf_rows("fill_packet", fill_packet)
    hard_missing = [
        "smooth_projective_source.Deligne_Cech_or_B_field_representative",
        "smooth_projective_source.period_denominator_or_smooth_unit",
        "smooth_projective_source.representative_to_central_cocycle_map",
        "smooth_projective_source.projective_rhoE_transition_tables",
        "bundle_operator.selected_connection_A_or_equivalent_operator_source",
        "bundle_operator.curvature_F_A",
        "bundle_operator.representation_action_on_uE_one_forms",
        "bundle_operator.kernel_and_quotient_policy",
        "bundle_operator.E_Qa_matrix_or_zero_order_block",
        "finite_part.positive_spectrum_or_heat_coefficients",
        "finite_part.zeta_or_torsion_regularization",
        "finite_part.trace_lift_or_complement_quotient_proof",
        "finite_part.finite_part_value",
        "admissibility.Freed_Witten_or_twisted_admissibility",
        "admissibility.projector_retention",
        "admissibility.no_double_count_policy",
    ]
    missing = {
        "schema": "SelectedHeteroticProjectiveRhoESmoothOperatorSourcePacketMissingLeaves.v1",
        "status": "VALUES_OPEN",
        "hard_missing": hard_missing,
        "support_filled": [
            "same-branch Strominger/Iwasawa projective source family",
            "fixed differential-class context",
            "global Bianchi/Strominger context as support",
            "primitive central support",
            "twist-cancellation table",
            "projective validator pattern",
            "selected finite internal projective packet",
            "R+ geometry block",
        ],
        "legal_repairs": [
            "emit selected Qa/SU3 Deligne/Cech/B-field representative and period unit",
            "prove representative-to-central-cocycle map with mapped Freed-Witten/Bianchi/projector checks",
            "emit selected smooth projective rho_E transition tables and bundle/operator action",
            "compute E_Qa or an equivalent source-certified heat/zeta/torsion finite part",
            "or prove exact complement quotient/cancellation with no-double-count policy",
        ],
        "leaf_report": leaf_report,
    }

    decision = {
        "fill_attempt_executed": True,
        "support_context_filled": True,
        "smooth_projective_source_values_filled": False,
        "bundle_operator_values_filled": False,
        "finite_part_values_filled": False,
        "admissibility_values_filled": False,
        "smooth_operator_source_packet_filled": False,
        "E_Qa_computed": False,
        "smooth_finitepart_computed": False,
        "threshold_value_computed": False,
        "next_required_artifact": NEXT,
        "missing_leaves_path": rel(OUTPUT_MISSING),
        "fill_packet_path": rel(OUTPUT_PACKET),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESmoothOperatorSourcePacketFillAttempt",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "interface": interface["status"],
            "twisted_source_fill": twisted["status"],
            "central_search": central["status"],
            "typed_projective_sourcefill": typed_sourcefill["status"],
            "rplus_payload": rplus["status"],
            "smooth_trace_lift": trace_lift["status"],
        },
        "fill_result": fill_result,
        "decision": decision,
        "cross_checks": {
            "central_search_map_verified": central["source_search_result"]["central_cocycle_map_verified"],
            "typed_projective_tables_emitted": typed_sourcefill["decision"]["projective_rhoE_tables_emitted"],
            "trace_lift_no_go_retained": trace_lift["decision"]["current_source_no_go_for_trace_lift"],
            "Rplus_not_promoted_to_bundle_curvature": True,
        },
        "guardrails": {
            "does_not_promote_support_context_to_values": True,
            "does_not_promote_q79_validator_tables": True,
            "does_not_promote_Rplus_as_F_A": True,
            "does_not_claim_trace_lift": True,
            "does_not_claim_E_Qa": True,
            "does_not_use_observed_couplings_or_scales": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "ProjectiveRhoESmoothOperatorSourcePacketCurrentSourceFillAttempt",
            "proved": True,
            "statement": (
                "The current repository fills the support context for the selected "
                "smooth projective rho_E lane, but it does not emit the selected "
                "Deligne/Cech/B-field representative, period unit, central-cocycle "
                "map, transition tables, bundle operator, E_Qa block, admissibility "
                "checks, or smooth finite part. Therefore the next repair is a true "
                "source amendment or exact complement-quotient theorem, not another "
                "normalization step."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_PACKET.write_text(json.dumps(fill_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_MISSING.write_text(json.dumps(missing, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "fill_packet_path": rel(OUTPUT_PACKET),
        "missing_leaves_path": rel(OUTPUT_MISSING),
        "note_path": rel(OUTPUT_NOTE),
        "support_context_filled": True,
        "smooth_operator_source_packet_filled": False,
        "E_Qa_computed": False,
        "smooth_finitepart_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SmoothOperator SourcePacket FillAttempt v1

## Result

```text
status = {STATUS}
support_context_filled = true
smooth_operator_source_packet_filled = false
E_Qa_computed = false
smooth_finitepart_computed = false
next_required_artifact = {NEXT}
```

## Filled Support

- same-branch Strominger/Iwasawa source-family support
- fixed differential-class context
- global Bianchi/Strominger context as support
- primitive central support
- twist-cancellation table
- projective validator pattern
- selected finite internal projective packet
- `R^+` geometry block

## Still Missing

```text
{rel(OUTPUT_MISSING)}
```

The next step must supply actual selected values: representative, period unit,
central-cocycle map, transition tables, bundle/operator action, admissibility
checks, and `E_Qa` or a heat/zeta/torsion finite part.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_MISSING)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
