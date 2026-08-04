from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

CONVERSION_CERT = ROOT / "certificates" / "gr_tt_aint_interface_conversion_requirements_certificate.json"
CLOSURE_CERT = ROOT / "certificates" / "closure_strain_stf_tensor_decomposition_certificate.json"
STF_CERT = ROOT / "certificates" / "selected_stf_hessian_form_certificate.json"

GR_SOURCE = (
    TEXPAPERS
    / "11 General Relativity & Geometry"
    / "_work"
    / "Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2"
    / "main.tex"
)
CLOSURE_SOURCE = (
    TEXPAPERS
    / "10 ProtoSpinor"
    / "_work"
    / "Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5"
    / "main.tex"
)

OUT_CERT = ROOT / "certificates" / "selected_gr_tt_aint_interface_data_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_gr_tt_aint_interface_data.template.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    conversion = load_json(CONVERSION_CERT)
    closure = load_json(CLOSURE_CERT)
    stf = load_json(STF_CERT)
    gr_source = read(GR_SOURCE)
    closure_source = read(CLOSURE_SOURCE)

    source_tests = {
        "gr_source_defines_spectral_gap_lambda_star": has_all(
            gr_source,
            ["\\lambda_{n,1}\\ge \\lambda_* > 0", "Off-harmonic leakage scales as $\\lambda_*^{-1}$"],
        ),
        "gr_source_defines_observable_projection": has_all(gr_source, ["\\mathcal P", "I\\circ \\Pi"]),
        "closure_source_defines_quadratic_cost_hessian": has_all(
            closure_source,
            ["\\mathcal{J}", "H", "quadratic normal form"],
        ),
        "closure_source_defines_induced_closure_metric": "induced closure metric" in closure_source,
        "source_derives_c_interface": "c_interface" in gr_source or "c_interface" in closure_source,
        "source_derives_A_GR_TT_equals_H_TT": "A_GR" in gr_source or "A_{GR" in gr_source,
        "source_selects_GR_internal_N_row": "selected N" in gr_source or "selected internal volume row" in gr_source,
    }

    tt_basis = closure["tt_reduction"]
    selected_form = stf["selected_form"]
    required = conversion["next_required_artifact"]["required_fields"]
    conversion_tables = conversion["required_conversion_tables"]

    packet = {
        "artifact": "Selected_GR_TT_Aint_Interface_Data",
        "purpose": (
            "Fill this packet only from selected MTT source data. Do not insert observed "
            "GR constants or choose a conversion factor to hit nil/Z64 values."
        ),
        "closed_structural_fields": {
            "domain_candidate": "local closure-strain 3x3 tensor sector restricted to TT plus/cross",
            "tt_basis": selected_form["basis"],
            "tt_hessian_form": selected_form["matrix"],
            "tt_hessian_condition": selected_form["condition"],
            "quotiented_directions_algebraic": [
                "antisymmetric gauge rotations",
                "scalar trace",
                "longitudinal/transverse-gauge components for propagation along z",
            ],
            "physical_tt_dimension": tt_basis["physical_dimension"],
        },
        "open_selection_fields": {
            "selected_N_or_internal_volume_row": None,
            "operator_relation_A_GR_TT_to_H_TT": None,
            "derived_c_interface": None,
            "proof_c_interface_equals_1": None,
            "quotient_projector_window_for_Aint": None,
            "lowest_positive_eigenvalue_after_quotienting": None,
        },
        "diagnostic_conversion_tables": conversion_tables,
        "allowed_status_values_after_fill": [
            "CLOSED_GR_TT_AINT_EQUALS_RESCALED_HTT",
            "CONDITIONAL_GR_TT_AINT_INTERFACE_CLOSED",
            "BLOCKED_OPERATOR_RELATION_UNSOURCED",
            "DISTINCT_GR_TT_COMPLEMENT_REQUIRED",
        ],
        "forbidden_fill_methods": [
            "choosing c_interface to make lambda_* equal 0.25",
            "choosing c_interface to make lambda_* equal 15",
            "using observed Newton/Planck units",
            "importing Z64 as GR gap without an operator identity",
        ],
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")

    closed_fields = {
        "tt_domain_candidate": True,
        "tt_basis": tt_basis["tt_basis_closed"],
        "tt_hessian_form": stf["closed_tests"]["hessian_form_closed"],
        "positive_internal_stiffness_rows": True,
    }
    open_fields = {
        "selected_N_or_internal_volume_row": not source_tests["source_selects_GR_internal_N_row"],
        "operator_relation_A_GR_TT_to_H_TT": not source_tests["source_derives_A_GR_TT_equals_H_TT"],
        "derived_c_interface": not source_tests["source_derives_c_interface"],
        "quotient_projector_window_for_Aint": True,
        "lowest_positive_eigenvalue_after_quotienting": True,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_gr_tt_aint_interface_data",
        "status": "SELECTED_GR_TT_AINT_INTERFACE_PACKET_BUILT_OPERATOR_RELATION_OPEN",
        "input_certificates": {
            "conversion_requirements": str(CONVERSION_CERT),
            "closure_strain_decomposition": str(CLOSURE_CERT),
            "selected_stf_hessian_form": str(STF_CERT),
        },
        "source_files": {
            "gr_reduction": str(GR_SOURCE),
            "closure_strain": str(CLOSURE_SOURCE),
        },
        "source_tests": source_tests,
        "packet_written": str(OUT_PACKET),
        "closed_fields": closed_fields,
        "open_fields": open_fields,
        "selected_data_status": {
            "selected_row_available": source_tests["source_selects_GR_internal_N_row"],
            "operator_relation_available": source_tests["source_derives_A_GR_TT_equals_H_TT"],
            "conversion_factor_available": source_tests["source_derives_c_interface"],
            "can_compute_GR_TT_modal_gap_now": False,
        },
        "candidate_consequence": {
            "if_scalar_interface_later_proved": (
                "Use the diagnostic conversion tables to check whether the derived "
                "c_interface selects nil, Z64, kappa_STF itself, or a distinct value."
            ),
            "if_no_scalar_interface": (
                "Build the full selected A_GR_TT operator on the TT quotient and compute "
                "its spectrum directly."
            ),
        },
        "next_required_proof": {
            "name": "GR_TT_Aint_Operator_Relation_Source_Theorem",
            "minimum_success_condition": (
                "A source-certified formula for A_GR_TT on the TT quotient, including "
                "its inner product and projector/window normalization."
            ),
            "then_compute": [
                "selected internal row",
                "c_interface if A_GR_TT is proportional to H_TT",
                "lowest positive eigenvalue if A_GR_TT is not proportional to H_TT",
                "branch decision: nil, Z64, kappa_STF, or distinct",
            ],
        },
        "guardrails": {
            "claims_selected_row": False,
            "claims_A_GR_TT_equals_H_TT": False,
            "claims_c_interface_derived": False,
            "claims_GR_TT_modal_gap_closed": False,
            "claims_Z64_is_GR_gap": False,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
