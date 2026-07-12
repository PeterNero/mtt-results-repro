from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

PHYS_ANCHOR_HUNT = ROOT / "certificates" / "selected_physical_anchor_source_hunt_certificate.json"
DIMLESS_GAP = ROOT / "certificates" / "dimensionless_modal_gap_operator_reduction_certificate.json"
EXACT_GAP = ROOT / "certificates" / "exact_branch_internal_aint_gap_import_certificate.json"
M_THEORY = ROOT / "certificates" / "m_theory_modal_gap_dimensional_anchor_candidate_certificate.json"
PHYS_STRESS = ROOT / "certificates" / "physical_normalization_stress_response_gate_certificate.json"
SCALE_COEFF = NONSM / "certificates" / "selected_scale_coefficient_extraction_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_modal_gap_to_physical_unit_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Modal_Gap_to_Physical_Unit_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    anchor_hunt = load(PHYS_ANCHOR_HUNT)
    dimless_gap = load(DIMLESS_GAP)
    exact_gap = load(EXACT_GAP)
    m_theory = load(M_THEORY)
    phys_stress = load(PHYS_STRESS)
    scale_coeff = load(SCALE_COEFF)

    lambda_exact = float(exact_gap["exact_branch_import"]["lambda_star_internal"])
    sqrt_lambda_exact = math.sqrt(lambda_exact)
    lambda_bound = float(dimless_gap["reduction"]["known_internal_gap_bound"])
    sqrt_lambda_bound = math.sqrt(lambda_bound)

    # Algebraic map. omega_phys is the missing physical unit with dimensions of
    # inverse length/energy/action-normalized modal frequency.
    conditional_map = {
        "missing_physical_unit": "omega_gap_phys",
        "unit_role": "physical inverse-length or energy unit multiplying the internal dimensionless modal frequency",
        "exact_branch": {
            "lambda_internal": lambda_exact,
            "sqrt_lambda_internal": sqrt_lambda_exact,
            "Lambda_gap_phys": "sqrt(15) * omega_gap_phys",
            "ell_p_if_identified_with_gap_length": "1 / (sqrt(15) * omega_gap_phys)",
            "kappa_11_squared_if_ellp_gap_identified": "(2*pi)^8 * ell_p^9 / 2",
        },
        "bound_branch": {
            "lambda_internal_bound": lambda_bound,
            "sqrt_lambda_internal_bound": sqrt_lambda_bound,
            "Lambda_gap_phys_if_saturated": "0.5 * omega_gap_phys",
            "ell_p_if_saturated_and_identified": "2 / omega_gap_phys",
        },
        "four_dimensional_reduction_after_anchor": {
            "kappa_4_inverse_squared": "kappa_11_inverse_squared * Vol(X_7)",
            "G_eff": "G_10 / Vol_int",
            "kappa_STF": "(32*pi*G_eff)^-1",
        },
    }

    closure_checks = {
        "physical_anchor_source_hunt_complete": anchor_hunt["status"]
        == "PHYSICAL_ANCHOR_SOURCE_HUNT_COMPLETE_DIRECT_ANCHOR_NOT_FOUND",
        "m_theory_modal_gap_route_is_best": anchor_hunt["synthesis"]["best_route"]
        == "route_A_m_theory_modal_gap_to_ellp",
        "m_theory_planck_slot_identified": m_theory["closed_tests"]["m_theory_planck_slot_identified"],
        "exact_internal_gap_closed": exact_gap["closed_now"]["exact_branch_internal_gap_value_closed"],
        "dimensionless_operator_shape_closed": dimless_gap["verdict"]["dimensionless_operator_shape_closed"],
        "structural_stress_response_closed": phys_stress["stress_response"][
            "universal_variational_definition_closed"
        ],
        "scale_formula_level_reduced": scale_coeff["verdict"]["formula_level_coefficient_gap_fixed"],
    }

    open_checks = {
        "omega_gap_phys_selected": False,
        "modal_gap_to_ellp_coefficient_selected": False,
        "physical_ellp_or_kappa11_selected": False,
        "physical_G10_selected": False,
        "physical_Newton_or_Planck_prediction_allowed": False,
        "numeric_CUV_delta_ratio_source_certified": scale_coeff["verdict"]["numeric_coefficients_extracted"],
    }

    theorem_status = (
        "CONDITIONAL_MAP_CLOSED_PHYSICAL_UNIT_COEFFICIENT_OPEN"
        if all(closure_checks.values()) and not any(open_checks.values())
        else "MODAL_GAP_TO_PHYSICAL_UNIT_NOT_READY"
    )

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_modal_gap_to_physical_unit_theorem",
        "status": theorem_status,
        "input_certificates": {
            "selected_physical_anchor_source_hunt": str(PHYS_ANCHOR_HUNT),
            "dimensionless_modal_gap_operator_reduction": str(DIMLESS_GAP),
            "exact_branch_internal_aint_gap_import": str(EXACT_GAP),
            "m_theory_modal_gap_dimensional_anchor_candidate": str(M_THEORY),
            "physical_normalization_stress_response_gate": str(PHYS_STRESS),
            "selected_scale_coefficient_extraction": str(SCALE_COEFF),
        },
        "closure_checks": closure_checks,
        "open_checks": open_checks,
        "conditional_theorem": {
            "name": "Selected_Modal_Gap_to_Physical_Unit_Theorem.v1",
            "status": "CONDITIONAL_ALGEBRA_CLOSED_ONLY",
            "statement": (
                "If the selected coherent fixed point supplies a physical inverse-length unit "
                "omega_gap_phys and a convention identifying the selected modal gap with the "
                "M-theory fundamental length/action scale, then the exact branch maps "
                "lambda_internal=15 to Lambda_gap_phys=sqrt(15) omega_gap_phys and hence "
                "to ell_p, kappa_11, G_eff, and kappa_STF through the sourced M-theory and "
                "GR reduction formulae."
            ),
            "conditional_map": conditional_map,
        },
        "why_not_full_closure": [
            "The exact branch supplies a dimensionless internal eigenvalue, not a physical inverse length.",
            "M-theory supplies the ell_p/kappa_11 slot once modal gap scales are physically chosen.",
            "Theta 5 TeV is explicitly calibration, not a no-knob physical unit.",
            "The scale-coefficient program still lacks source-certified numeric C_UV^2/delta for a physical scale.",
        ],
        "next_required_object": {
            "name": "Selected_Physical_Omega_Gap_Theorem",
            "must_supply": [
                "omega_gap_phys in physical units, or an equivalent selected length/action unit",
                "the convention mapping the selected modal gap to ell_p/kappa_11/alpha_prime/G10",
                "source-certified C_UV^2/delta or equivalent physical scale coefficient",
                "proof that no observed G_N, M_Pl, H0, rho_DE, absolute mass, or TeV calibration is used",
            ],
        },
        "guardrails": {
            "claims_physical_omega_gap": False,
            "claims_physical_ellp": False,
            "claims_physical_kappa11": False,
            "claims_physical_G10": False,
            "claims_Newton_or_Planck_prediction": False,
            "uses_observed_target_backsolve": False,
            "uses_Theta_5TeV_as_prediction": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# Selected Modal Gap to Physical Unit Theorem v1

## Conditional Closure

The exact branch supplies the dimensionless internal value:

```text
lambda_internal = 15
sqrt(lambda_internal) = sqrt(15)
```

If a selected physical inverse-length unit `omega_gap_phys` is supplied, then:

```text
Lambda_gap_phys = sqrt(15) * omega_gap_phys
ell_p = 1 / Lambda_gap_phys
2 kappa_11^2 = (2 pi)^8 ell_p^9
kappa_4^-2 = kappa_11^-2 Vol(X_7)
G_eff = G_10 / Vol_int
kappa_STF = (32 pi G_eff)^-1
```

So the algebraic bridge from an MTT physical modal-gap unit to the GR/M-theory
normalization is closed.

## What Is Still Open

The missing datum is not another internal eigenvalue. It is:

```text
omega_gap_phys
```

or an equivalent selected physical length/action unit. Current sources do not
select this value. Theta `5 TeV` remains calibration, and the exact branch
`lambda=15` remains internal until a physical unit theorem is supplied.

## Next Object

```text
Selected_Physical_Omega_Gap_Theorem
```

This theorem must derive the physical modal-gap unit from selected fixed-point
data, topological integers, or source-certified scale coefficients, without
observed Newton, Planck, cosmological, absolute mass, or TeV calibration input.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {theorem_status}")


if __name__ == "__main__":
    main()
