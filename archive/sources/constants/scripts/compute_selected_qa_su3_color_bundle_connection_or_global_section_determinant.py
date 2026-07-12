"""Reduce the Qa/SU3 color-bundle/global-section determinant gate.

The previous source hunt selected the next legitimate routes after the compact
Nil Hodge branch was fully computed and obstructed.  This script turns those
routes into an auditable determinant interface.  It deliberately refuses to
insert the required residual as a projector factor.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_HUNT_CERT = (
    ROOT / "certificates" / "selected_qa_su3_alternative_operator_or_projector_source_hunt_certificate.json"
)
WEITZ_CERT = ROOT / "certificates" / "selected_qa_su3_canonical_bundle_weitzenbock_certificate.json"
BRST_CERT = ROOT / "certificates" / "selected_qa_su3_brst_determinant_with_weitzenbock_certificate.json"
PNZ_CERT = ROOT / "certificates" / "selected_qa_su3_pnonzero_physical_quotient_determinant_certificate.json"

CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
SOURCES = {
    "heterotic_flux": CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md",
    "gauge_fixing": CORPUS
    / "5 Dirac Delta"
    / "Gauge_Fixing_as_Admissible_Section_Selection_in_Modal_Triplet_Theory.md",
    "topology_constraints": CORPUS
    / "13 Standard Model & Topology-Only Constraints"
    / "Topology_Only_Constraints_and_Forbidden_Operators_in_Modal_Triplet_Theory.md",
    "ncg": CORPUS
    / "15 Discrete & Spectral & Operator Geometric Theories"
    / "Modal_Triplet_Theory__From_MTT_to_Noncommutative_Geometry_v3.md",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def source_terms(path: Path, terms: list[str]) -> dict:
    if not path.exists():
        return {
            "path": str(path),
            "present": False,
            "contains_all_terms": False,
            "missing_terms": terms,
        }
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    missing = [term for term in terms if term.lower() not in text]
    return {
        "path": str(path),
        "present": True,
        "contains_all_terms": not missing,
        "missing_terms": missing,
    }


def main() -> None:
    source_hunt = load(SOURCE_HUNT_CERT)
    weitz = load(WEITZ_CERT)
    brst = load(BRST_CERT)
    pnz = load(PNZ_CERT)

    required_response = float(
        source_hunt["input_obstruction"]["needed_log_response_for_any_new_factor"]
    )
    selected_qa = float(source_hunt["input_obstruction"]["selected_unweighted_Qa"])
    required_qa = float(source_hunt["input_obstruction"]["required_unweighted_Qa"])

    source_checks = {
        "heterotic_flux": source_terms(
            SOURCES["heterotic_flux"],
            ["Bismut connection", "Tr}F", "left-invariant", "discrete"],
        ),
        "gauge_fixing": source_terms(
            SOURCES["gauge_fixing"],
            ["Faddeev--Popov", "Gribov", "global", "section"],
        ),
        "topology_constraints": source_terms(
            SOURCES["topology_constraints"],
            ["global section", "connection", "SU(3)", "anomaly"],
        ),
        "ncg": source_terms(
            SOURCES["ncg"],
            ["inner fluctuations", "spectral action", "SU(3)", "finite connection"],
        ),
    }

    prior_exhausted_inputs = {
        "canonical_nil_tangent_weitzenbock": {
            "status": weitz["status"],
            "already_used_in_hodge_oneform_spectrum": brst["selected_weitzenbock_inclusion"][
                "E_is_already_in_sourced_hodge_oneform_spectrum"
            ],
            "may_be_added_again": False,
        },
        "local_fp_brs_quotient": {
            "pnonzero_status": pnz["status"],
            "selected_pnonzero_response": pnz["finite_parts"][
                "selected_pnonzero_physical_quotient_response"
            ],
            "may_be_reused_as_extra": False,
        },
    }

    determinant_routes = {
        "selected_su3_color_connection": {
            "status": "OPEN_SELECTED_CONNECTION_AND_SPECTRUM_REQUIRED",
            "legal": True,
            "operator_form": (
                "D_Qa,color = -(nabla_A^* nabla_A on BRST physical SU3 color bundle) + E(A,R_+,F)"
            ),
            "source_support": [
                "heterotic_flux",
                "ncg",
                "topology_constraints",
            ],
            "available_now": {
                "gauge_group": "SU3 color factor is corpus-supported",
                "canonical_nil_tangent_E": "computed but already counted",
                "torsional_flux_selection_principle": "structural source present",
            },
            "missing_selected_data": [
                "explicit SU3 color bundle or local system over the compact Nil/Iwasawa branch",
                "selected connection A or flux-twisted connection entering the Qa threshold operator",
                "curvature endomorphism E(A,R_+,F) in the physical BRST quotient",
                "zeta/heat/analytic-torsion finite part computed from that operator",
                "proof the data are selected before comparison with the Qa residual",
            ],
            "needed_log_response_if_it_closes_alone": required_response,
        },
        "global_section_or_gribov_measure": {
            "status": "OPEN_SELECTED_FUNDAMENTAL_DOMAIN_MEASURE_REQUIRED",
            "legal": True,
            "operator_form": (
                "finite measure ratio between the local FP slice and selected global admissible section/fundamental domain"
            ),
            "source_support": ["gauge_fixing", "topology_constraints"],
            "available_now": {
                "global_section_failure": "corpus-supported structural possibility",
                "local_fp_jacobian": "already counted",
            },
            "missing_selected_data": [
                "selected SU3/Nil configuration space and gauge action",
                "selected fundamental modular region or admissible global-section atlas",
                "finite measure ratio/Jacobian for that region",
                "proof this is not the already-counted local FP determinant",
            ],
            "needed_log_response_if_it_closes_alone": required_response,
        },
        "acyclic_local_system_torsion": {
            "status": "OPEN_LOCAL_SYSTEM_AND_TORSION_FORMULA_REQUIRED",
            "legal": True,
            "operator_form": (
                "Ray-Singer/Reidemeister torsion of the selected acyclic p!=0 Nil local system"
            ),
            "source_support": ["heterotic_flux", "topology_constraints"],
            "available_now": {
                "p_nonzero_hodge_complex_acyclic": True,
                "analytic_torsion_is_natural_invariant": True,
            },
            "missing_selected_data": [
                "selected lattice character or flat local system",
                "color trace/representation weight",
                "torsion normalization convention compatible with the BRST determinant",
                "closed formula or computable spectrum for the selected compact Nil local system",
            ],
            "needed_log_response_if_it_closes_alone": required_response,
        },
    }

    impossible_shortcuts = {
        "add_canonical_weitzenbock_again": {
            "rejected": True,
            "reason": "The sourced co-closed one-form determinant is already a Hodge determinant and already contains the canonical Nil Weitzenbock term.",
        },
        "reuse_local_fp_brs_jacobian": {
            "rejected": True,
            "reason": "The p=0 and p!=0 BRST quotient rules already counted the local quotient determinant.",
        },
        "choose_finite_coherent_filter_factor_by_residual": {
            "rejected": True,
            "reason": "The required response is known, but selecting a filter factor from it would be target fitting.",
        },
    }

    output = {
        "status": "QA_SU3_COLOR_BUNDLE_OR_GLOBAL_SECTION_DETERMINANT_REDUCED_VALUES_OPEN",
        "input_obstruction": {
            "selected_unweighted_Qa": selected_qa,
            "required_unweighted_Qa": required_qa,
            "selected_minus_required": selected_qa - required_qa,
            "needed_log_response_for_new_selected_source": required_response,
        },
        "source_checks": source_checks,
        "prior_exhausted_inputs": prior_exhausted_inputs,
        "determinant_routes": determinant_routes,
        "impossible_shortcuts": impossible_shortcuts,
        "ranking": {
            "best_next_computation": "selected_su3_color_connection",
            "parallel_mathematical_computation": "acyclic_local_system_torsion",
            "fallback_global_measure_computation": "global_section_or_gribov_measure",
        },
        "next_required_artifact": "Selected_Qa_SU3_Color_Connection_Local_System_Torsion_Interface_v1",
        "verdict": {
            "new_numeric_closure": False,
            "target_fitting_used": False,
            "compact_nil_branch_remains_retired_as_final_proof": True,
            "next_gate_reduced_to_selected_operator_data": True,
            "full_SM_closure_achieved": False,
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
