from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

SCALE_GATE = ROOT / "certificates" / "physical_scale_lifting_anchor_gate_certificate.json"
ABS_CANDIDATES = NONSM / "certificates" / "absolute_normalization_candidate_gate_certificate.json"
PHYSICAL_ACTION = NONSM / "certificates" / "physical_action_normalization_gate_certificate.json"
FINAL_RHO = NONSM / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"

OUT_CERT = ROOT / "certificates" / "target_independent_dimensional_anchor_candidates_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    scale_gate = load_json(SCALE_GATE)
    candidate_gate = load_json(ABS_CANDIDATES)
    physical_action = load_json(PHYSICAL_ACTION)
    final_rho = load_json(FINAL_RHO)

    imported = scale_gate["imported_internal_scale_lift"]
    candidates = candidate_gate["candidates"]

    # Promote the generic non-SM candidate taxonomy into a GR-specific anchor
    # table. The selected internal rho branch improves the state of E, but does
    # not by itself add dimensions.
    gr_candidates = [
        {
            "id": "E_topological_flux_integer_minimization_plus_rhoUV",
            "base_candidate": "E_topological_flux_integer_minimization",
            "classification": "BEST_OPEN_ROUTE_DIMENSIONLESS_MINIMIZER_CLOSED_DIMENSIONAL_ANCHOR_MISSING",
            "closed_inputs": {
                "internal_rho_UV": imported["rho_UV"],
                "internal_R_star": imported["R_star"],
                "internal_s_star": imported["s_star_from_rho"],
                "canonical_G10_int": physical_action["canonical_internal_normalization"]["G10_int"],
            },
            "why_not_physical_closure": (
                "The minimizer is an internal normalized scale. No selected map from "
                "internal action units to SI length/mass/action units is supplied."
            ),
            "next_needed": "a source-certified dimensional value for the fundamental action/length unit, not derived from G_N or M_Pl",
        },
        {
            "id": "C_theta_coherence_scale",
            "base_candidate": "C_theta_coherence_scale",
            "classification": "PROMISING_OPEN_ROUTE_NO_EXECUTABLE_DIMENSIONAL_VALUE",
            "why_not_physical_closure": (
                "The corpus supports a coherence-scale role, but current certificates "
                "do not derive a dimensionful Lambda_Theta independently of target observables."
            ),
            "next_needed": "derive Lambda_Theta as a physical dimensionful scale before comparing to tensors, G_N, H0, or masses",
        },
        {
            "id": "D_flux_bianchi_alpha_prime",
            "base_candidate": "D_flux_bianchi_alpha_prime",
            "classification": "OPEN_REQUIRES_ALPHA_PRIME_OR_STRING_LENGTH_ANCHOR",
            "why_not_physical_closure": (
                "Flux/Bianchi data select ratios and internal branch values; alpha-prime/string length "
                "is still an external physical scale unless selected by another theorem."
            ),
            "next_needed": "source-certified alpha-prime/string-length selection independent of Newton/Planck data",
        },
        {
            "id": "F_central_circle_spectral_gap",
            "base_candidate": "F_central_circle_spectral_gap",
            "classification": "BOUNDS_AND_INTERNAL_UNITS_NOT_ABSOLUTE_DIMENSIONAL_SELECTION",
            "why_not_physical_closure": (
                "The central-circle branch closes internal alpha=1 and lambda_star=15, "
                "but physical alpha remains a unit/scale conversion."
            ),
            "next_needed": "independent equality fixing physical alpha, not merely an admissible bound",
        },
        {
            "id": "H_coherence_capacity_to_Geff",
            "base_candidate": "corpus_parameter_paper",
            "classification": "STRUCTURAL_RELATION_OPEN_CANONICAL_REPRESENTATIVE_MISSING",
            "why_not_physical_closure": (
                "Corpus says G_eff is proportional to inverse coherence capacity in the Einstein limit, "
                "but does not provide a canonical physical normalization of C_MTT."
            ),
            "next_needed": "canonical representative of C_MTT with physical dimensions and a no-backsolve value",
        },
        {
            "id": "B_newton_backsolve",
            "base_candidate": "B_newton_backsolve",
            "classification": "FORBIDDEN_FOR_PREDICTION",
            "why_not_physical_closure": "Uses the target value G_N to set the claimed prediction.",
            "next_needed": "none; allowed only as phenomenological calibration",
        },
        {
            "id": "unit_conventions_c_hbar_kB",
            "base_candidate": "unit conventions",
            "classification": "FORBIDDEN_AS_PREDICTION_TARGETS",
            "why_not_physical_closure": "Changing units cannot predict a physical dimensionful observable.",
            "next_needed": "none",
        },
    ]

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "target_independent_dimensional_anchor_candidates",
        "status": "DIMENSIONAL_ANCHOR_CANDIDATES_CLASSIFIED_NO_PHYSICAL_CLOSURE",
        "input_certificates": {
            "physical_scale_lifting_anchor_gate": str(SCALE_GATE),
            "absolute_normalization_candidate_gate": str(ABS_CANDIDATES),
            "physical_action_normalization": str(PHYSICAL_ACTION),
            "final_internal_rho_uv": str(FINAL_RHO),
        },
        "gate_rules": candidate_gate["gate_rules"],
        "candidate_table": gr_candidates,
        "best_next_route": {
            "id": "E_topological_flux_integer_minimization_plus_rhoUV",
            "why": (
                "It uses the newly closed internal rho_UV/scale-lift data and preserves "
                "the no-backsolve discipline. It is the only route in the current table "
                "that improves from existing selected internal data rather than adding an observed scale."
            ),
            "specific_next_artifact": "Target_Independent_Dimensional_Anchor_Candidate_v1",
            "must_output": [
                "which quantity is dimensionful",
                "its physical units",
                "the selected MTT source of its value",
                "proof that no observed target constant is used",
                "the induced physical G_eff and kappa_STF only after the anchor is fixed",
            ],
        },
        "verdict": {
            "internal_scale_lift_available": scale_gate["guardrails"]["claims_internal_scale_lift_closed"],
            "physical_dimensionful_anchor_available": False,
            "newton_or_planck_prediction_allowed_now": False,
            "most_honest_current_claim": (
                "MTT GR normalization is closed in canonical internal units and reduced to "
                "one target-independent dimensional-anchor problem."
            ),
        },
        "guardrails": {
            "claims_physical_GN": False,
            "claims_physical_MPl": False,
            "claims_dimensional_anchor_closed": False,
            "forbids_target_backsolve": True,
            "forbids_unit_convention_as_prediction": True,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
