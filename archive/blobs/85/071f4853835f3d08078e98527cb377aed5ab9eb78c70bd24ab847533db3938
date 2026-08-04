from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
THETA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\18 Theta-Closure & Execution Program\_md_v3_corrected")
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

M_THEORY_CERT = ROOT / "certificates" / "m_theory_modal_gap_dimensional_anchor_candidate_certificate.json"

THETA_I = THETA / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md"
THETA_II = THETA / "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md"
THETA_IV = THETA / "Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale.md"
FINITE_COHERENT = (
    OBSIDIAN
    / "5 Dirac Delta"
    / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"
)

OUT_CERT = ROOT / "certificates" / "selected_modal_gap_physical_anchor_gate_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    m_theory = load_json(M_THEORY_CERT)
    theta_i = read(THETA_I)
    theta_ii = read(THETA_II)
    theta_iv = read(THETA_IV)
    finite = read(FINITE_COHERENT)

    source_tests = {
        "theta_i_has_lambda_star_value": has(theta_i, "lambda_{\\ast} = 0.25"),
        "theta_i_declares_tev_scale_calibration_assumption": has(
            theta_i,
            "we introduce a calibration assumption",
            "E_{\\mathrm{gap,min}} := \\mu_\\Theta = 5~\\mathrm{TeV}",
        ),
        "theta_i_says_formalism_does_not_fix_identification": has(
            theta_i,
            "The MTT formalism itself does not fix this identification",
        ),
        "theta_ii_has_exact_lens_eigenvalue_ratio_data": has(
            theta_ii,
            "exact first nonzero Laplace--Beltrami eigenvalue",
            "\\lambda_{\\mathrm{lens}} \\ge",
        ),
        "theta_iv_identifies_lambda_theta_with_matching_scale": has(
            theta_iv,
            "\\Lambda_\\Theta \\sim \\mu_\\Theta",
            "conservative calibration scheme",
        ),
        "theta_iv_uses_planck_mass_for_tensor_bound": has(
            theta_iv,
            "M_{\\mathrm{Pl}}",
            "r \\;\\lesssim\\; \\left(\\frac{\\Lambda_\\Theta}{M_{\\mathrm{Pl}}}\\right)^2",
        ),
        "finite_coherent_ties_scale_to_internal_gap": has(
            finite,
            "A_{\\rm int}",
            "\\lambda_\\ast\\sim R^{-2}",
            "\\Lambda_{\\rm eff}",
            "finite coherent scale is not arbitrary",
        ),
    }

    candidates = [
        {
            "id": "internal_lambda_star",
            "value": "lambda_star = 0.25",
            "classification": "CLOSED_INTERNAL_DIMENSIONLESS_GAP",
            "why_not_physical_anchor": "It fixes an internal eigenvalue scale only; physical energy still requires a length/radius/action unit.",
        },
        {
            "id": "theta_mu_5_TeV",
            "value": "mu_Theta = 5 TeV",
            "classification": "FORBIDDEN_AS_NO_KNOB_ANCHOR_CALIBRATION_ASSUMPTION",
            "why_not_physical_anchor": "Theta I explicitly introduces it as a calibration assumption and says MTT does not fix the identification.",
        },
        {
            "id": "lambda_eff_from_tau",
            "value": "Lambda_eff = tau^{-1/2} ~ R^{-1}/sqrt(log(C_Q/epsilon_adm))",
            "classification": "STRUCTURAL_PHYSICAL_SLOT_INTERNAL_RADIUS_AND_TOLERANCE_OPEN",
            "why_not_physical_anchor": "It ties coherence scale to the internal spectral gap, but leaves physical R, C_Q, and epsilon_adm unselected.",
        },
        {
            "id": "lens_exact_first_eigenvalue",
            "value": "lambda_lens >= 2/(f2 R_lens)^2",
            "classification": "RATIO_OR_BOUND_NOT_ABSOLUTE_SCALE",
            "why_not_physical_anchor": "It gives a selected dimensionless shape/bound after radius choice, not a target-independent physical radius.",
        },
    ]

    closed_tests = {
        "m_theory_anchor_slot_formulated": m_theory["status"]
        == "M_THEORY_MODAL_GAP_ANCHOR_CANDIDATE_FORMULATED_DIMENSIONFUL_GAP_OPEN",
        "internal_lambda_star_identified": source_tests["theta_i_has_lambda_star_value"],
        "finite_coherent_scale_geometrically_tied_to_gap": source_tests["finite_coherent_ties_scale_to_internal_gap"],
        "lens_exact_eigenvalue_ratio_source_present": source_tests["theta_ii_has_exact_lens_eigenvalue_ratio_data"],
    }

    blocked_shortcuts = {
        "use_mu_theta_5TeV_as_prediction": source_tests["theta_i_declares_tev_scale_calibration_assumption"]
        and source_tests["theta_i_says_formalism_does_not_fix_identification"],
        "use_tensor_bound_to_infer_planck_scale": source_tests["theta_iv_uses_planck_mass_for_tensor_bound"],
        "use_lambda_eff_without_physical_R": True,
    }

    open_tests = {
        "selected_dimensionful_R_or_ell_p_computed": False,
        "selected_CQ_and_epsilon_adm_computed_as_physical_anchor": False,
        "selected_modal_gap_in_eV_or_inverse_meters_computed": False,
        "physical_GN_or_MPl_prediction_allowed": False,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_modal_gap_physical_anchor_gate",
        "status": "SELECTED_MODAL_GAP_PHYSICAL_ANCHOR_NOT_CLOSED_TEV_CALIBRATION_FORBIDDEN",
        "input_certificates": {
            "m_theory_modal_gap_dimensional_anchor_candidate": str(M_THEORY_CERT),
        },
        "source_files": {
            "theta_i": str(THETA_I),
            "theta_ii": str(THETA_II),
            "theta_iv": str(THETA_IV),
            "finite_coherent_projection": str(FINITE_COHERENT),
        },
        "source_tests": source_tests,
        "candidate_classification": candidates,
        "closed_tests": closed_tests,
        "blocked_shortcuts": blocked_shortcuts,
        "open_tests": open_tests,
        "next_viable_computation": {
            "id": "dimensionless_modal_gap_operator_on_selected_branch",
            "description": (
                "Compute the selected operator A_int on the rho_UV/central-circle/"
                "flux branch and its lowest positive eigenvalue in internal units. "
                "Then seek an independent physical unit theorem; do not use 5 TeV "
                "as a no-knob value."
            ),
            "minimum_schema": {
                "operator": "self-adjoint positive selected A_int or TT/closure operator",
                "domain": "selected physical quotient, with gauge zero modes removed",
                "spectrum": "lowest positive eigenvalue and multiplicity",
                "scale_status": "dimensionless unless a separate physical unit theorem is supplied",
            },
        },
        "verdict": {
            "modal_gap_internal_structure_available": True,
            "physical_modal_gap_anchor_available": False,
            "theta_5TeV_allowed_role": "phenomenological calibration or conservative benchmark only",
            "most_honest_current_claim": (
                "The corpus supports a gap-controlled physical-anchor route, but "
                "also explicitly forbids treating the present TeV matching scale as "
                "a derived no-knob anchor."
            ),
        },
        "guardrails": {
            "claims_mu_theta_5TeV_derived": False,
            "claims_physical_modal_gap_closed": False,
            "claims_physical_GN": False,
            "claims_physical_MPl": False,
            "forbids_calibration_as_prediction": True,
            "forbids_using_planck_mass_tensor_bound_to_predict_planck_mass": True,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
