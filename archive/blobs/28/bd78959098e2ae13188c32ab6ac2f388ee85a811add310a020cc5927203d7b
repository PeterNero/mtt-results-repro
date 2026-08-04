"""Build the next Qa/SU3 source-hunt gate after the compact-Nil obstruction.

The prior theorem proves that the compact Nil Hodge/BRST branch is fully
computed but overshoots the required Qa value. This script does not fit a new
number. It classifies the remaining corpus-legal mechanisms that could still
alter the selected SU3 threshold determinant.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_qa_su3_final_obstruction_or_projector_resolution_certificate.json"
CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")


SOURCES = {
    "finite_coherent_projection": CORPUS
    / "5 Dirac Delta"
    / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md",
    "gauge_fixing_projection": CORPUS
    / "5 Dirac Delta"
    / "Gauge_Fixing_as_Admissible_Section_Selection_in_Modal_Triplet_Theory.md",
    "superset_core": CORPUS
    / "3 Core Foundations"
    / "Modal_Triplet_Theory__MTT_as_a_Superset_v2.md",
}


def source_status(path: Path, required_terms: list[str]) -> dict:
    if not path.exists():
        return {
            "path": str(path),
            "present": False,
            "contains_required_terms": False,
            "missing_terms": required_terms,
        }
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    missing = [term for term in required_terms if term.lower() not in text]
    return {
        "path": str(path),
        "present": True,
        "contains_required_terms": not missing,
        "missing_terms": missing,
    }


def main() -> None:
    obstruction = json.loads(CERT.read_text(encoding="utf-8"))
    excess = float(obstruction["computed_branch"]["excess_selected_minus_required"])

    candidates = [
        {
            "id": "local_fp_brs_quotient_jacobian",
            "status": "EXHAUSTED_ALREADY_COUNTED",
            "legal_as_extra_correction": False,
            "reason": (
                "Gauge-fixing/FP/BRST projection Jacobians are real corpus sources, "
                "but the p=0 and p!=0 Qa/SU3 BRST quotient rules have already counted "
                "the local quotient determinant. Reusing it would double-count."
            ),
            "source": "gauge_fixing_projection",
        },
        {
            "id": "finite_coherent_filter_normalization",
            "status": "OPEN_NOT_SELECTED_NUMERICALLY",
            "legal_as_extra_correction": True,
            "reason": (
                "The finite coherent filter B_adm=P chi(A) exp(-tau A) chi(A) P "
                "is corpus-native. It can affect determinant weights only after "
                "A, tau, chi, and the physical quotient domain are selected before "
                "comparison. The current corpus does not select the needed factor."
            ),
            "needed_log_response_if_used_alone": -excess,
            "source": "finite_coherent_projection",
        },
        {
            "id": "soft_gauge_tube_width",
            "status": "REJECTED_AS_GAUGE_PARAMETER_OR_REGULATOR",
            "legal_as_extra_correction": False,
            "reason": (
                "A soft gauge tube epsilon is a representative-selection width. "
                "Without an independent physical selection theorem it is a gauge "
                "or regulator convention, not a no-knob threshold prediction."
            ),
            "source": "gauge_fixing_projection",
        },
        {
            "id": "global_section_gribov_or_fundamental_domain_measure",
            "status": "PROMISING_OPEN",
            "legal_as_extra_correction": True,
            "reason": (
                "The local FP quotient is already counted, but a non-Abelian global "
                "section obstruction or selected fundamental modular region could "
                "supply a separate finite measure factor. The corpus states the "
                "structural possibility but does not yet select the SU3/Nil domain "
                "or compute its determinant."
            ),
            "needed_log_response_if_used_alone": -excess,
            "source": "gauge_fixing_projection",
        },
        {
            "id": "nontrivial_su3_color_bundle_connection_endomorphism",
            "status": "BEST_NEXT_OPEN_GATE",
            "legal_as_extra_correction": True,
            "reason": (
                "The current Weitzenbock calculation used the canonical Nil tangent "
                "bundle data and correctly avoided double-counting. A different "
                "selected SU3 color bundle, connection curvature, or flux-twisted "
                "endomorphism would be a genuinely different threshold operator, "
                "not an added fitted projector."
            ),
            "needed_log_response_if_used_alone": -excess,
            "source": "finite_coherent_projection",
        },
        {
            "id": "ray_singer_or_reidemeister_torsion_local_system",
            "status": "PROMISING_OPEN",
            "legal_as_extra_correction": True,
            "reason": (
                "The p!=0 Nil Hodge complex is acyclic, so analytic torsion is the "
                "mathematically natural invariant to audit next. It is legal only "
                "if the selected local system, lattice character, and color trace "
                "are fixed independently."
            ),
            "needed_log_response_if_used_alone": -excess,
            "source": "superset_core",
        },
        {
            "id": "complex_nesting_shared_circle_rotation",
            "status": "OPEN_WEAK_DIRECT_LINK_TO_QA",
            "legal_as_extra_correction": False,
            "reason": (
                "Complex nesting and shared-circle projection are important for "
                "phase/weak-split structure, but current evidence links them more "
                "directly to U1/SU2 and hypercharge normalization than to an SU3 "
                "Nil determinant correction."
            ),
            "source": "superset_core",
        },
    ]

    source_checks = {
        "finite_coherent_projection": source_status(
            SOURCES["finite_coherent_projection"],
            ["B_{\\rm adm}", "P\\chi(A)", "e^{-\\tau A}", "gauge sectors"],
        ),
        "gauge_fixing_projection": source_status(
            SOURCES["gauge_fixing_projection"],
            ["Faddeev--Popov", "projection Jacobian", "BRST", "Gribov"],
        ),
        "superset_core": source_status(
            SOURCES["superset_core"],
            ["projector", "Nil", "SU(3)", "coherent"],
        ),
    }

    out = {
        "status": "QA_SU3_ALTERNATIVE_OPERATOR_OR_PROJECTOR_SOURCE_HUNT_CERTIFIED_OPEN",
        "input_obstruction": {
            "status": obstruction["status"],
            "selected_unweighted_Qa": obstruction["computed_branch"]["selected_unweighted_Qa"],
            "required_unweighted_Qa": obstruction["computed_branch"]["required_unweighted_Qa"],
            "excess_selected_minus_required": excess,
            "needed_log_response_for_any_new_factor": -excess,
            "target_fitting_used_so_far": obstruction["verdict"]["target_fitting_used"],
        },
        "source_checks": source_checks,
        "candidate_routes": candidates,
        "ranking": {
            "best_next_route": "nontrivial_su3_color_bundle_connection_endomorphism",
            "second_route": "global_section_gribov_or_fundamental_domain_measure",
            "mathematical_invariant_route": "ray_singer_or_reidemeister_torsion_local_system",
            "do_not_use_as_extra": [
                "local_fp_brs_quotient_jacobian",
                "soft_gauge_tube_width",
                "complex_nesting_shared_circle_rotation",
            ],
        },
        "next_required_artifact": (
            "Selected_Qa_SU3_Color_Bundle_Connection_or_Global_Section_Determinant_v1"
        ),
        "verdict": {
            "full_SM_closure_achieved": False,
            "compact_nil_branch_retired_as_final_Qa_proof": True,
            "source_hunt_complete_enough_to_choose_next_gate": True,
            "target_fitting_used": False,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
