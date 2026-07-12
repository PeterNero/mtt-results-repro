"""Fill attempt for the selected heterotic endomorphism threshold value packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "source_packet": DATA / "selected_heterotic_projective_carrier_or_endomorphism_operator_source_packet.candidate.json",
    "value_template": DATA / "selected_heterotic_endomorphism_threshold_value_packet.template.json",
    "color_bundle_fill_attempt": DATA / "color_bundle_operator_packet_fill_attempt.candidate.json",
    "strominger_kernel": DATA / "selected_heterotic_strominger_electroweak_threshold_kernel.candidate.json",
    "analytic_torsion_payload": DATA / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_endomorphism_threshold_valuepacket_fill.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_endomorphism_threshold_valuepacket_fill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_Endomorphism_Threshold_ValuePacket_Fill_v1.md"

STATUS = "HETEROTIC_ENDOMORPHISM_THRESHOLD_VALUEPACKET_FILL_ATTEMPT_BLOCKED_SOURCE_VALUES_OPEN"
NEXT = "Selected_Heterotic_SourceCertificate_or_DirectOperatorEmission_Search_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def mark(value: Any) -> bool:
    return value is not None and value is not False


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    source_packet = load(INPUTS["source_packet"])
    template = load(INPUTS["value_template"])
    color_fill = load(INPUTS["color_bundle_fill_attempt"])
    strominger = load(INPUTS["strominger_kernel"])
    torsion = load(INPUTS["analytic_torsion_payload"])

    partial = color_fill["partial_packet"]
    filled_packet = {
        "selected_source": {
            "source_certificate": None,
            "branch_id": template["selected_source"]["branch_id"],
            "same_branch_as_internal_lambda12": False,
            "target_fitting_used": False,
        },
        "geometry_and_bundle": {
            "internal_space": template["geometry_and_bundle"]["internal_space"],
            "bundle_sheaf_twist_or_module": partial["color_source"]["bundle_or_sheaf"],
            "structure_group": partial["color_source"]["structure_group"],
            "chern_mukai_or_bianchi_packet": partial["color_source"]["chern_or_mukai_data"],
            "freed_witten_or_projector_check": partial["color_source"]["freed_witten_or_bianchi_check"],
            "support_imported_from_strominger_kernel": strominger["status"],
        },
        "operator_domain": {
            "domain_after_p0_and_p_nonzero_quotient": "partial imported Qa quotient policy; not a selected determinant domain",
            "boundary_or_lattice_conditions": partial["operator_domain"]["boundary_or_lattice_conditions"],
            "zero_mode_policy": partial["operator_domain"]["zero_mode_policy"],
            "ghost_or_BRST_policy": {
                "p0_rule": partial["operator_domain"]["p0_rule"],
                "p_nonzero_rule": partial["operator_domain"]["p_nonzero_rule"],
            },
            "trace_weights": partial["normalization"]["trace_normalization"],
        },
        "operator_blocks": {
            "laplace_type_principal_symbol": partial["operator_blocks"]["laplace_type_principal_symbol"],
            "connection_or_curvature": partial["connection_or_residual"]["connection_data"],
            "endomorphism_E_or_Weitzenbock_zero_order_block": partial["operator_blocks"]["endomorphism_E"],
            "spectrum_or_heat_coefficients_or_torsion": {
                "spectrum": partial["operator_blocks"]["spectrum"],
                "heat_coefficients": partial["operator_blocks"]["heat_coefficient_table"],
                "analytic_or_reidemeister_torsion": partial["operator_blocks"]["analytic_or_reidemeister_torsion"],
                "torsion_payload_status": torsion["status"],
            },
            "finite_part_regularization": None,
        },
        "normalization_and_output": {
            "reference_scale_or_action_unit": partial["normalization"]["reference_scale_squared"],
            "qa_qc_su2_index_weights": None,
            "physical_threshold_convention": None,
            "computed_dimensionless_finite_part": None,
        },
    }

    required_flags = {
        "source_certificate": mark(filled_packet["selected_source"]["source_certificate"]),
        "same_branch_identity": filled_packet["selected_source"]["same_branch_as_internal_lambda12"] is True,
        "bundle_or_twist": mark(filled_packet["geometry_and_bundle"]["bundle_sheaf_twist_or_module"]),
        "chern_bianchi_packet": mark(filled_packet["geometry_and_bundle"]["chern_mukai_or_bianchi_packet"]),
        "freed_witten_or_projector": mark(filled_packet["geometry_and_bundle"]["freed_witten_or_projector_check"]),
        "selected_domain": filled_packet["operator_domain"]["domain_after_p0_and_p_nonzero_quotient"] not in (None, "partial imported Qa quotient policy; not a selected determinant domain"),
        "trace_weights": mark(filled_packet["operator_domain"]["trace_weights"]),
        "connection_or_curvature": mark(filled_packet["operator_blocks"]["connection_or_curvature"]),
        "endomorphism_E": mark(filled_packet["operator_blocks"]["endomorphism_E_or_Weitzenbock_zero_order_block"]),
        "finite_part_data": any(
            mark(filled_packet["operator_blocks"]["spectrum_or_heat_coefficients_or_torsion"][key])
            for key in ["spectrum", "heat_coefficients", "analytic_or_reidemeister_torsion"]
        ),
        "finite_part_regularization": mark(filled_packet["operator_blocks"]["finite_part_regularization"]),
        "physical_threshold_convention": mark(filled_packet["normalization_and_output"]["physical_threshold_convention"]),
        "computed_dimensionless_finite_part": mark(filled_packet["normalization_and_output"]["computed_dimensionless_finite_part"]),
    }
    missing = [key for key, value in required_flags.items() if value is False]

    candidate = {
        "candidate": "SelectedHeteroticEndomorphismThresholdValuePacketFill",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "source_packet": source_packet["status"],
            "color_bundle_fill_attempt": color_fill["status"],
            "strominger_kernel": strominger["status"],
            "analytic_torsion_payload": torsion["status"],
        },
        "filled_packet": filled_packet,
        "required_flags": required_flags,
        "missing_fields": missing,
        "positive_progress": {
            "operator_packet_shape_fixed": True,
            "compact_nil_iwasawa_branch_named": True,
            "quotient_policy_partially_imported": True,
            "strominger_support_available": True,
        },
        "decision": {
            "template_filled_enough_for_determinant": False,
            "selected_values_available": False,
            "physical_electroweak_threshold_closure": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "EndomorphismThresholdValuePacketCurrentSourceNoGo",
            "proved": True,
            "statement": (
                "The current records fix the required endomorphism-threshold packet shape and "
                "partially import the compact Nil/Iwasawa quotient policy, but they do not emit "
                "a same-branch selected source certificate, SU3 bundle/sheaf/twist, Chern/Bianchi "
                "packet, connection/curvature, endomorphism_E block, finite spectrum/heat/torsion "
                "data, trace weights, or physical threshold convention. Therefore no determinant "
                "finite part can be promoted from the current source record."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "promotes_partial_quotient_policy": False,
            "promotes_strominger_support_as_threshold_value": False,
            "promotes_retired_hym_matrix": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    cert = {
        "certificate": "SelectedHeteroticEndomorphismThresholdValuePacketFill",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "missing_field_count": len(missing),
        "template_filled_enough_for_determinant": False,
        "selected_values_available": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Heterotic Endomorphism Threshold ValuePacket Fill v1

## Result

```text
status = {candidate["status"]}
missing_field_count = {len(candidate["missing_fields"])}
template_filled_enough_for_determinant = false
selected_values_available = false
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Filled Packet

```json
{json.dumps(candidate["filled_packet"], indent=2, sort_keys=True)}
```

## Missing Fields

```json
{json.dumps(candidate["missing_fields"], indent=2, sort_keys=True)}
```

## Theorem

{candidate["theorem"]["statement"]}

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
