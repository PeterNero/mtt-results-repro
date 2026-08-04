from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
M_THEORY_SOURCE = (
    OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_M_theory.md"
)

ANCHOR_CANDIDATES = ROOT / "certificates" / "target_independent_dimensional_anchor_candidates_certificate.json"
SCALE_GATE = ROOT / "certificates" / "physical_scale_lifting_anchor_gate_certificate.json"
STF_SCALE = ROOT / "certificates" / "stf_hessian_scale_to_geff_relation_certificate.json"

OUT_CERT = ROOT / "certificates" / "m_theory_modal_gap_dimensional_anchor_candidate_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    anchor_candidates = load_json(ANCHOR_CANDIDATES)
    scale_gate = load_json(SCALE_GATE)
    stf_scale = load_json(STF_SCALE)
    source = M_THEORY_SOURCE.read_text(encoding="utf-8", errors="replace")

    source_tests = {
        "m_theory_source_present": M_THEORY_SOURCE.exists(),
        "planck_relation_source_present": contains_all(
            source,
            ["MP-from-11D", "Vol}(X_7)", "kappa_{11}", "M_{\\mathrm{P}}"],
        ),
        "gauge_matrix_source_present": contains_all(
            source,
            ["gauge-matrix", "f_{ab}", "omega_a", "kappa_{11}"],
        ),
        "modal_gap_condition_source_present": contains_all(
            source,
            ["No free continuous parameters remain once the modal gap scales", "topological integers are chosen"],
        ),
        "relative_scale_statement_source_present": contains_all(
            source,
            ["relative placement", "fixed functions of the modal gap(s)", "Vol}(X_7)"],
        ),
    }

    imported = scale_gate["imported_internal_scale_lift"]
    stf_formula = stf_scale["relation"]

    # The M-theory corpus gives the right physical normalization shape, but it
    # explicitly depends on kappa_11 / l_p or on dimensionful modal gap scales.
    # That makes it a strong candidate route, not a closed prediction.
    candidate = {
        "id": "m_theory_modal_gap_planck_anchor",
        "quantity_to_anchor": {
            "dimensionful_quantity": "ell_p or equivalently kappa_11 / modal gap energy",
            "physical_units": "length, action-normalized gravitational coupling, or energy",
            "invariant_output_after_anchor": "G_eff and kappa_STF in physical units",
        },
        "source_formula": {
            "corpus_file": str(M_THEORY_SOURCE),
            "relation": "1/(2 kappa_4^2) = Vol(X_7)/(2 kappa_11^2), so M_P^2 is proportional to Vol(X_7)/ell_p^9 up to conventions",
            "gauge_relation": "f_ab = (1/(2 kappa_11^2)) integral_X7 omega_a wedge *_7 omega_b",
            "selection_claim": "4D data are fixed once modal gap scales and topological integers are chosen",
        },
        "closed_internal_inputs": {
            "rho_UV": imported["rho_UV"],
            "R_star": imported["R_star"],
            "s_star": imported["s_star_from_rho"],
            "stf_internal_relation": stf_formula,
        },
        "positive_result": (
            "The M-theory route supplies the correct dimensional slot: a single "
            "fundamental length/action scale fixes the 4D Planck normalization, "
            "gauge kinetic normalizations, and the TT Hessian scale together."
        ),
        "blocker": (
            "The source still conditions closure on modal gap scales. The current "
            "verified corpus does not compute a target-independent physical value "
            "for that dimensionful modal gap, ell_p, kappa_11, or alpha_prime."
        ),
    }

    closed_tests = {
        "internal_scale_lift_available": anchor_candidates["verdict"]["internal_scale_lift_available"],
        "stf_to_geff_relation_available": stf_scale["status"] == "STF_HESSIAN_SCALE_TIED_TO_GEFF_ABSOLUTE_NORMALIZATION_OPEN",
        "m_theory_planck_slot_identified": source_tests["planck_relation_source_present"],
        "m_theory_gauge_slot_identified": source_tests["gauge_matrix_source_present"],
        "source_says_modal_gap_and_topology_fix_relative_data": source_tests["modal_gap_condition_source_present"]
        and source_tests["relative_scale_statement_source_present"],
    }

    open_tests = {
        "dimensionful_modal_gap_value_computed": False,
        "ell_p_or_kappa11_selected_without_backsolve": False,
        "alpha_prime_or_string_length_selected_without_backsolve": False,
        "physical_newton_or_planck_prediction_allowed": False,
    }

    next_theorem = {
        "name": "Selected_Modal_Gap_Physical_Anchor_Theorem",
        "must_prove": [
            "construct the selected modal-gap operator on the same MTT branch as rho_UV",
            "show its lowest nonzero gap has a unique positive value in physical units",
            "prove the value is not obtained from G_N, M_Pl, H0, rho_DE, or absolute particle masses",
            "map that gap to ell_p, kappa_11, or alpha_prime with fixed conventions",
            "only then compute physical G_eff and kappa_STF",
        ],
        "candidate_equations_after_closure": [
            "kappa_4^-2 = kappa_11^-2 Vol(X_7)",
            "G_eff = G_10 / Vol_int in the repository TT convention",
            "kappa_STF = (32*pi*G_eff)^-1",
        ],
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "m_theory_modal_gap_dimensional_anchor_candidate",
        "status": "M_THEORY_MODAL_GAP_ANCHOR_CANDIDATE_FORMULATED_DIMENSIONFUL_GAP_OPEN",
        "input_certificates": {
            "target_independent_dimensional_anchor_candidates": str(ANCHOR_CANDIDATES),
            "physical_scale_lifting_anchor_gate": str(SCALE_GATE),
            "stf_hessian_scale_to_geff_relation": str(STF_SCALE),
        },
        "source_tests": source_tests,
        "candidate": candidate,
        "closed_tests": closed_tests,
        "open_tests": open_tests,
        "next_theorem": next_theorem,
        "verdict": {
            "route_promoted": "E_topological_flux_integer_minimization_plus_rhoUV -> m_theory_modal_gap_planck_anchor",
            "physical_dimensionful_anchor_available": False,
            "newton_or_planck_prediction_allowed_now": False,
            "most_honest_current_claim": (
                "The M-theory corpus gives the correct no-knob normalization slot, "
                "but full physical closure now requires a selected physical modal-gap value."
            ),
        },
        "guardrails": {
            "claims_physical_GN": False,
            "claims_physical_MPl": False,
            "claims_dimensionful_modal_gap_closed": False,
            "forbids_observed_GN_or_MPl_backsolve": True,
            "forbids_relative_scale_fix_as_absolute_prediction": True,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
