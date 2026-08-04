"""Build the Qa/SU3 color-connection/local-system torsion interface."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GATE_CERT = (
    ROOT
    / "certificates"
    / "selected_qa_su3_color_bundle_connection_or_global_section_determinant_certificate.json"
)
TEMPLATE = (
    ROOT
    / "certificates"
    / "selected_qa_su3_color_connection_local_system_torsion.template.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def missing_template_fields(template: dict) -> list[str]:
    op = template["selected_qa_su3_operator"]
    missing: list[str] = []
    if op["branch"] is None:
        missing.append("selected_qa_su3_operator.branch")
    if op["geometry"]["internal_space"] is None:
        missing.append("selected_qa_su3_operator.geometry.internal_space")
    if op["color_bundle"]["representation"] is None:
        missing.append("selected_qa_su3_operator.color_bundle.representation")
    if op["color_bundle"]["trace_normalization"] is None:
        missing.append("selected_qa_su3_operator.color_bundle.trace_normalization")
    if op["color_bundle"]["bundle_or_local_system"] is None:
        missing.append("selected_qa_su3_operator.color_bundle.bundle_or_local_system")
    if op["brst_domain"]["physical_quotient"] is None:
        missing.append("selected_qa_su3_operator.brst_domain.physical_quotient")
    if op["brst_domain"]["zero_mode_rule"] is None:
        missing.append("selected_qa_su3_operator.brst_domain.zero_mode_rule")
    if op["brst_domain"]["ghost_rule"] is None:
        missing.append("selected_qa_su3_operator.brst_domain.ghost_rule")

    branch = op["branch"]
    if branch == "selected_su3_color_connection_spectrum":
        for field in ("connection_type", "connection_data", "curvature_or_flux_data", "endomorphism_E"):
            if op["connection"][field] is None:
                missing.append(f"selected_qa_su3_operator.connection.{field}")
        if op["spectrum_modes"] is None:
            missing.append("selected_qa_su3_operator.spectrum_modes")
    elif branch == "acyclic_local_system_torsion":
        if op["analytic_torsion"] is None:
            missing.append("selected_qa_su3_operator.analytic_torsion")
    elif branch == "global_section_measure":
        if op["connection"]["connection_data"] is None:
            missing.append("selected_qa_su3_operator.connection.connection_data_as_global_measure")
    else:
        missing.append("selected valid branch-specific determinant data")
    return missing


def main() -> None:
    gate = load(GATE_CERT)
    template = load(TEMPLATE)
    missing = missing_template_fields(template)

    output = {
        "status": "QA_SU3_COLOR_CONNECTION_LOCAL_SYSTEM_TORSION_INTERFACE_BUILT_VALUES_OPEN",
        "input_gate_status": gate["status"],
        "open_template": str(TEMPLATE.relative_to(ROOT)),
        "allowed_branches": template["allowed_branches"],
        "accounting_formulas": {
            "spectrum_logdet_response": (
                "sum_j multiplicity_j * index_weight_j * log(eigenvalue_j / reference_scale_squared)"
            ),
            "ray_singer_log_torsion_response": (
                "1/2 * sum_q (-1)^q * q * weight_q * zeta_derivative_at_zero_q"
            ),
            "global_section_measure_response": (
                "log(selected_global_section_or_fundamental_domain_measure / local_FP_slice_measure)"
            ),
        },
        "required_inputs": template["remaining_required_data"],
        "missing_template_fields": missing,
        "template_refuses_to_compute": bool(missing),
        "handoff_to_prior_gate": {
            "needed_log_response_for_new_selected_source": gate["input_obstruction"][
                "needed_log_response_for_new_selected_source"
            ],
            "best_next_computation": gate["ranking"]["best_next_computation"],
            "parallel_mathematical_computation": gate["ranking"][
                "parallel_mathematical_computation"
            ],
        },
        "no_knob_rules": template["no_knob_rules"],
        "verdict": {
            "interface_built": True,
            "selected_values_available": False,
            "can_compute_numeric_response_now": False,
            "target_fitting_used": False,
            "next_required_artifact": "Fill_Selected_Qa_SU3_Color_Connection_or_Torsion_Template_From_Source_Data",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
