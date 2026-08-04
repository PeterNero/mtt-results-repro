"""Build the selected Qa/SU3 color-bundle operator packet interface.

This is an interface, not a determinant computation.  It defines the exact
packet that must be supplied before the Qa/SU3 determinant can be computed
without target fitting.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"

SOURCE_HUNT = CERTS / "selected_qa_su3_endomorphism_source_hunt_after_torsion_no_go_certificate.json"
P0 = CERTS / "selected_qa_su3_p0_ghost_measure_normalization_certificate.json"
PNONZERO = CERTS / "selected_qa_su3_pnonzero_physical_quotient_determinant_certificate.json"
PROJECTIVE_DECISION = CERTS / "selected_qa_su3_projective_clock_shift_or_endomorphism_route_decision_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    source_hunt = load(SOURCE_HUNT)
    p0 = load(P0)
    pnonzero = load(PNONZERO)
    projective = load(PROJECTIVE_DECISION)

    packet_template = {
        "status": "OPEN_SELECTED_QA_SU3_COLOR_BUNDLE_OPERATOR_PACKET_REQUIRED",
        "description": (
            "Fill this only with selected Qa/SU3 color-bundle operator data chosen "
            "before comparison with the Qa residual."
        ),
        "selected_packet": {
            "branch_id": None,
            "source_certificate": None,
            "selection_rule": None,
            "operator_domain": {
                "geometry": "compact Nil/Iwasawa Qa branch",
                "gauge_factor": "SU3",
                "representation": None,
                "p0_rule": "import selected p0 ghost measure normalization",
                "p_nonzero_rule": "import selected p!=0 physical quotient determinant domain",
                "boundary_or_lattice_conditions": None,
                "zero_mode_policy": None,
            },
            "color_source": {
                "bundle_or_sheaf": None,
                "rank": None,
                "structure_group": None,
                "chern_or_mukai_data": None,
                "gerbe_or_twist_data": None,
                "freed_witten_or_bianchi_check": None,
            },
            "connection_or_residual": {
                "connection_type": None,
                "connection_data": None,
                "curvature_data": None,
                "hym_or_strominger_residual": None,
                "retired_hym_matrix_used": False,
            },
            "operator_blocks": {
                "laplace_type_principal_symbol": None,
                "endomorphism_E": None,
                "heat_coefficient_table": None,
                "spectrum": None,
                "analytic_or_reidemeister_torsion": None,
            },
            "normalization": {
                "trace_normalization": None,
                "gauge_quotient_scheme": None,
                "reference_scale_squared": 1.0,
                "target_residual_used": False,
            },
        },
        "promotion_gates": [
            {
                "id": "source_selection",
                "required": [
                    "branch_id",
                    "source_certificate",
                    "selection_rule",
                    "color_source.bundle_or_sheaf",
                ],
            },
            {
                "id": "domain_compatibility",
                "required": [
                    "operator_domain.representation",
                    "operator_domain.boundary_or_lattice_conditions",
                    "operator_domain.zero_mode_policy",
                ],
            },
            {
                "id": "geometry_and_anomaly",
                "required": [
                    "color_source.structure_group",
                    "color_source.chern_or_mukai_data",
                    "color_source.freed_witten_or_bianchi_check",
                ],
            },
            {
                "id": "operator_data",
                "required": [
                    "connection_or_residual.connection_type",
                    "connection_or_residual.curvature_data",
                    "operator_blocks.laplace_type_principal_symbol",
                    "operator_blocks.endomorphism_E",
                ],
            },
            {
                "id": "finite_part_data",
                "requires_one_of": [
                    "operator_blocks.heat_coefficient_table",
                    "operator_blocks.spectrum",
                    "operator_blocks.analytic_or_reidemeister_torsion",
                ],
            },
            {
                "id": "normalization",
                "required": [
                    "normalization.trace_normalization",
                    "normalization.gauge_quotient_scheme",
                ],
            },
        ],
        "forbidden_inputs": [
            "observed Qa/SU3 residual",
            "retired explicit HYM matrix entries",
            "rank-one q64 compact-Nil local-system character",
            "SU3 scalar-center q64 phase",
            "visible qutrit/F3^2 source as direct q64/U64 Qa/SU3 source",
            "local FP/BRST quotient counted a second time",
        ],
    }

    open_fields = [
        gate.get("required", []) for gate in packet_template["promotion_gates"] if "required" in gate
    ]
    flattened_open = [item for group in open_fields for item in group]
    flattened_open.extend(["one of: heat_coefficient_table, spectrum, analytic_or_reidemeister_torsion"])

    output = {
        "certificate": "SelectedQaSU3ColorBundleOperatorPacketInterface",
        "status": "QA_SU3_COLOR_BUNDLE_OPERATOR_PACKET_INTERFACE_BUILT_VALUES_OPEN",
        "input_status": {
            "source_hunt": source_hunt["status"],
            "p0_rule": p0["status"],
            "p_nonzero_rule": pnonzero["status"],
            "projective_decision": projective["status"],
        },
        "packet_template": packet_template,
        "interface_result": {
            "interface_built": True,
            "template_filled": False,
            "selected_qa_su3_operator_packet_available": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "full_sm_closure_achieved": False,
            "target_fitting_used": False,
        },
        "remaining_open_fields": flattened_open,
        "computed_numeric_response": None,
        "do_not_use": packet_template["forbidden_inputs"],
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Color_Bundle_Operator_Packet_Fill_Attempt_v1",
            "must_supply": [
                "a selected source certificate for the color bundle/sheaf/twist",
                "domain compatibility with the selected p0 and p!=0 quotient rules",
                "connection or residual data",
                "endomorphism_E or equivalent heat operator block",
                "one computable finite-part object: heat table, spectrum, or torsion",
            ],
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
