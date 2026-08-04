"""Build the Qa/SU3 color-bundle operator packet interface."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")

SOLVE_ATTEMPT = DATA / "selected_finite_source_solve_attempt.candidate.json"
OUTPUT_DATA = DATA / "color_bundle_operator_packet_interface.candidate.json"
OUTPUT_CERT = CERTS / "color_bundle_operator_packet_interface_certificate.json"

EXTERNAL_CERTS = {
    "p0_rule": NONSM / "certificates" / "selected_qa_su3_p0_ghost_measure_normalization_certificate.json",
    "p_nonzero_rule": NONSM / "certificates" / "selected_qa_su3_pnonzero_physical_quotient_determinant_certificate.json",
    "projective_decision": NONSM
    / "certificates"
    / "selected_qa_su3_projective_clock_shift_or_endomorphism_route_decision_certificate.json",
    "source_hunt": NONSM / "certificates" / "selected_qa_su3_endomorphism_source_hunt_after_torsion_no_go_certificate.json",
}


def load_status(path: Path) -> dict[str, object]:
    if not path.exists():
        return {"present": False, "path": str(path), "status": "MISSING"}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {"present": True, "path": str(path), "status": data.get("status", "UNKNOWN")}


def main() -> None:
    solve = json.loads(SOLVE_ATTEMPT.read_text(encoding="utf-8"))
    imported = {name: load_status(path) for name, path in EXTERNAL_CERTS.items()}
    packet_template = {
        "status": "OPEN_SELECTED_QA_SU3_COLOR_BUNDLE_OPERATOR_PACKET_REQUIRED",
        "description": "Fill only with selected Qa/SU3 color-bundle operator data chosen before comparison with the Qa residual.",
        "selected_packet": {
            "branch_id": None,
            "source_certificate": None,
            "selection_rule": None,
            "operator_domain": {
                "geometry": "compact Nil/Iwasawa Qa branch",
                "gauge_factor": "SU3",
                "p0_rule": imported["p0_rule"]["status"],
                "p_nonzero_rule": imported["p_nonzero_rule"]["status"],
                "representation": None,
                "boundary_or_lattice_conditions": None,
                "zero_mode_policy": None,
            },
            "color_source": {
                "bundle_or_sheaf": None,
                "rank": None,
                "structure_group": None,
                "chern_or_mukai_data": None,
                "freed_witten_or_bianchi_check": None,
                "gerbe_or_twist_data": None,
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
            {"id": "source_selection", "required": ["branch_id", "source_certificate", "selection_rule", "color_source.bundle_or_sheaf"]},
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
            {"id": "normalization", "required": ["normalization.trace_normalization", "normalization.gauge_quotient_scheme"]},
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
    candidate = {
        "candidate": "SelectedQaSU3ColorBundleOperatorPacketInterface",
        "status": "COLOR_BUNDLE_OPERATOR_PACKET_INTERFACE_BUILT_VALUES_OPEN",
        "input_statuses": {
            "selected_finite_source_solve_attempt": solve["status"],
            **{name: row["status"] for name, row in imported.items()},
        },
        "external_certificates": imported,
        "packet_template": packet_template,
        "remaining_open_fields": [
            "branch_id",
            "source_certificate",
            "selection_rule",
            "color_source.bundle_or_sheaf",
            "operator_domain.representation",
            "operator_domain.boundary_or_lattice_conditions",
            "operator_domain.zero_mode_policy",
            "color_source.structure_group",
            "color_source.chern_or_mukai_data",
            "color_source.freed_witten_or_bianchi_check",
            "connection_or_residual.connection_type",
            "connection_or_residual.curvature_data",
            "operator_blocks.laplace_type_principal_symbol",
            "operator_blocks.endomorphism_E",
            "normalization.trace_normalization",
            "normalization.gauge_quotient_scheme",
            "one of: heat_coefficient_table, spectrum, analytic_or_reidemeister_torsion",
        ],
        "interface_result": {
            "interface_built": True,
            "template_filled": False,
            "selected_qa_su3_operator_packet_available": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "full_sm_closure_achieved": False,
            "target_fitting_used": False,
        },
        "decision": {
            "result": "Color-bundle operator packet interface built; determinant problem remains open.",
            "why": "The current source solve identifies endomorphism_E/full threshold operator data as the primary missing object.",
            "next_move": "Attempt to fill this interface from source-certified MTT/Strominger/Fu-Yau/bundle/gerbe/operator data.",
        },
        "next_required_artifact": "Selected_Qa_SU3_Color_Bundle_Operator_Packet_Fill_Attempt_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3ColorBundleOperatorPacketInterface",
        "status": "QA_SU3_COLOR_BUNDLE_OPERATOR_PACKET_INTERFACE_BUILT_VALUES_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "operator_packet_interface_built": True,
            "p0_and_p_nonzero_quotient_status_imported": imported["p0_rule"]["present"] and imported["p_nonzero_rule"]["present"],
            "forbidden_inputs_fixed": True,
            "promotion_gates_defined": len(packet_template["promotion_gates"]) == 6,
        },
        "what_remains_open": {
            "selected_operator_packet": True,
            "endomorphism_E_or_equivalent_zero_order_block": True,
            "heat_spectrum_torsion_or_determinant_finite_part": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
