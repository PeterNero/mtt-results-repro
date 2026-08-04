"""Build the heterotic projective-carrier or endomorphism-operator source packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")

INPUTS = {
    "post_hym_attack": DATA / "selected_heterotic_local_system_torsion_or_new_operator_attack.candidate.json",
    "source_template": DATA / "selected_heterotic_projective_or_endomorphism_operator_source.template.json",
    "projective_route_decision": NONSM / "certificates" / "selected_qa_su3_projective_clock_shift_or_endomorphism_route_decision_certificate.json",
    "color_connection_interface": NONSM / "certificates" / "selected_qa_su3_color_connection_local_system_torsion_interface_certificate.json",
    "color_bundle_fill_attempt": NONSM / "certificates" / "selected_qa_su3_color_bundle_operator_packet_fill_attempt_certificate.json",
    "endomorphism_hunt": NONSM / "certificates" / "selected_qa_su3_endomorphism_source_hunt_after_torsion_no_go_certificate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projective_carrier_or_endomorphism_operator_source_packet.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projective_carrier_or_endomorphism_operator_source_packet_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_endomorphism_threshold_value_packet.template.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveCarrier_or_EndomorphismOperator_SourcePacket_v1.md"

STATUS = "HETEROTIC_PROJECTIVE_CARRIER_OR_ENDOMORPHISM_SOURCE_PACKET_BUILT_ENDOMORPHISM_VALUE_CONTRACT_OPEN"
NEXT = "Selected_Heterotic_Endomorphism_Threshold_ValuePacket_Fill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build_value_template() -> dict[str, Any]:
    return {
        "schema": "SelectedHeteroticEndomorphismThresholdValuePacket.v1",
        "status": "OPEN_VALUES_REQUIRED",
        "selected_source": {
            "source_certificate": None,
            "branch_id": "qa_su3_compact_nil_iwasawa_threshold_branch",
            "same_branch_as_internal_lambda12": None,
            "target_fitting_used": False,
        },
        "geometry_and_bundle": {
            "internal_space": "compact Nil/Iwasawa Qa sector",
            "bundle_sheaf_twist_or_module": None,
            "structure_group": "SU3 or source-certified SU3 quotient",
            "chern_mukai_or_bianchi_packet": None,
            "freed_witten_or_projector_check": None,
        },
        "operator_domain": {
            "domain_after_p0_and_p_nonzero_quotient": None,
            "boundary_or_lattice_conditions": None,
            "zero_mode_policy": None,
            "ghost_or_BRST_policy": None,
            "trace_weights": None,
        },
        "operator_blocks": {
            "laplace_type_principal_symbol": None,
            "connection_or_curvature": None,
            "endomorphism_E_or_Weitzenbock_zero_order_block": None,
            "spectrum_or_heat_coefficients_or_torsion": None,
            "finite_part_regularization": None,
        },
        "normalization_and_output": {
            "reference_scale_or_action_unit": None,
            "qa_qc_su2_index_weights": None,
            "physical_threshold_convention": None,
            "computed_dimensionless_finite_part": None,
        },
        "forbidden": [
            "fill any value from measured electroweak data",
            "reuse the retired printed HYM matrices",
            "promote the U64 clock-shift carrier without this operator-domain bridge",
            "count FP/BRST quotient or shared-line projector twice",
        ],
    }


def build_projective_packet(route_decision: dict[str, Any]) -> dict[str, Any]:
    carrier = route_decision["route_decisions"][0]["mathematical_carrier"]
    return {
        "route": "projective_q64_clock_shift_carrier",
        "algebraic_carrier_certified": True,
        "phase": carrier["phase"],
        "phase_order": carrier["phase_order"],
        "minimal_dimension": carrier["minimal_irreducible_clock_shift_dimension"],
        "presentation": carrier["presentation"],
        "determinant_consistency": carrier["determinant_consistency"],
        "operator_domain_bridge_to_Qa_SU3_threshold_complex": False,
        "BRST_or_zero_mode_policy": False,
        "degreewise_torsion_or_zeta_finite_part": False,
        "trace_weights_and_normalization": False,
        "selected_closure": False,
        "verdict": "EXACT_AUXILIARY_CARRIER_NOT_A_THRESHOLD_PROOF",
    }


def build_endomorphism_contract(interface: dict[str, Any], fill_attempt: dict[str, Any], hunt: dict[str, Any]) -> dict[str, Any]:
    required = list(dict.fromkeys(
        interface["required_inputs"]
        + hunt["next_required_artifact"]["must_define"]
        + fill_attempt["next_required_artifact"]["must_find"]
    ))
    return {
        "route": "source_certified_endomorphism_E_full_operator",
        "selected_primary_route": True,
        "current_selected_source_found": fill_attempt["fill_result"]["same_branch_qa_su3_source_found"],
        "determinant_computable_now": fill_attempt["fill_result"]["determinant_computable_now"],
        "gate_results": fill_attempt["gate_results"],
        "required_payload_fields": required,
        "operator_formula_contract": {
            "laplace_type_form": "Delta_threshold = nabla_A^* nabla_A + E_Qa",
            "zero_order_block": "E_Qa must be emitted as the selected endomorphism_E or equivalent Weitzenbock block.",
            "finite_part": "logdet_or_torsion = selected heat/zeta/spectrum/Reidemeister finite part on the selected BRST quotient domain.",
            "normalization": "Use the selected gauge quotient and threshold convention before any comparison to data.",
        },
        "selected_closure": False,
        "verdict": "PRIMARY_OPEN_VALUE_CONTRACT",
    }


def build_global_measure_contract() -> dict[str, Any]:
    return {
        "route": "global_section_or_fundamental_domain_measure",
        "selected_primary_route": False,
        "required_proof": [
            "selected global section or fundamental domain measure",
            "proof the measure is distinct from local FP/BRST normalization",
            "finite determinant contribution with no target residual input",
        ],
        "selected_closure": False,
        "verdict": "BACKUP_ONLY_UNTIL_NO_DOUBLE_COUNT_PROOF",
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    post = load(INPUTS["post_hym_attack"])
    template = load(INPUTS["source_template"])
    route_decision = load(INPUTS["projective_route_decision"])
    interface = load(INPUTS["color_connection_interface"])
    fill_attempt = load(INPUTS["color_bundle_fill_attempt"])
    hunt = load(INPUTS["endomorphism_hunt"])
    value_template = build_value_template()

    projective = build_projective_packet(route_decision)
    endomorphism = build_endomorphism_contract(interface, fill_attempt, hunt)
    global_measure = build_global_measure_contract()

    candidate = {
        "candidate": "SelectedHeteroticProjectiveCarrierOrEndomorphismOperatorSourcePacket",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "post_hym_attack": post["status"],
            "projective_route_decision": route_decision["status"],
            "color_connection_interface": interface["status"],
            "color_bundle_fill_attempt": fill_attempt["status"],
            "endomorphism_hunt": hunt["status"],
        },
        "inherited_forbidden": template["forbidden"],
        "route_A_projective_carrier": projective,
        "route_B_endomorphism_operator": endomorphism,
        "route_C_global_measure": global_measure,
        "decision": {
            "projective_carrier_algebra_closed": True,
            "projective_carrier_selected_threshold_proof": False,
            "endomorphism_operator_contract_built": True,
            "selected_values_available": False,
            "measured_electroweak_closure": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "source_theorem": {
            "name": "ProjectiveCarrierOrEndomorphismOperatorSourcePacketTheorem",
            "proved": True,
            "statement": (
                "The selected q64 phase has an exact U64 clock-shift projective carrier, "
                "but this carrier is only an auxiliary representation until a selected "
                "operator-domain bridge, BRST policy, degreewise finite part, and trace "
                "normalization are emitted. Under the current source record, the only "
                "primary no-knob route to a physical heterotic/Qa-SU3 threshold is a "
                "same-branch selected endomorphism_E threshold value packet."
            ),
        },
        "next_value_template_path": rel(OUTPUT_TEMPLATE),
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "promotes_projective_carrier_as_closure": False,
            "promotes_retired_hym_matrix": False,
            "promotes_global_measure_without_no_double_count": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    cert = {
        "certificate": "SelectedHeteroticProjectiveCarrierOrEndomorphismOperatorSourcePacket",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "next_value_template_path": rel(OUTPUT_TEMPLATE),
        "projective_carrier_algebra_closed": True,
        "projective_carrier_selected_threshold_proof": False,
        "endomorphism_operator_contract_built": True,
        "selected_values_available": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, value_template, render_note(candidate, cert, value_template)


def render_note(candidate: dict[str, Any], cert: dict[str, Any], value_template: dict[str, Any]) -> str:
    return f"""# Selected Heterotic Projective Carrier or Endomorphism Operator Source Packet v1

## Result

```text
status = {candidate["status"]}
projective_carrier_algebra_closed = true
projective_carrier_selected_threshold_proof = false
endomorphism_operator_contract_built = true
selected_values_available = false
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Route A: Projective Carrier

```json
{json.dumps(candidate["route_A_projective_carrier"], indent=2, sort_keys=True)}
```

## Route B: Endomorphism Operator

```json
{json.dumps(candidate["route_B_endomorphism_operator"], indent=2, sort_keys=True)}
```

## Route C: Global Measure

```json
{json.dumps(candidate["route_C_global_measure"], indent=2, sort_keys=True)}
```

## Source Theorem

{candidate["source_theorem"]["statement"]}

## Next Value Template

```json
{json.dumps(value_template, indent=2, sort_keys=True)}
```

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, value_template, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_TEMPLATE, value_template)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_TEMPLATE, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
