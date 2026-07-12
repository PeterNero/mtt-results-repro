from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

MODAL_TO_UNIT = ROOT / "certificates" / "selected_modal_gap_to_physical_unit_theorem_certificate.json"
ANCHOR_HUNT = ROOT / "certificates" / "selected_physical_anchor_source_hunt_certificate.json"
SCALE_COEFF = NONSM / "certificates" / "selected_scale_coefficient_extraction_certificate.json"
FINAL_RHO = NONSM / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"
RHO_UNIT_NO_GO = NONSM / "certificates" / "selected_rho_uv_unit_covariance_no_go_certificate.json"
RHO_RESPONSE_ATTEMPT = NONSM / "certificates" / "selected_rho_uv_response_ratio_computation_attempt_certificate.json"
ACTION_NORM = NONSM / "certificates" / "physical_action_normalization_gate_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_physical_omega_gap_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Physical_Omega_Gap_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    modal_to_unit = load(MODAL_TO_UNIT)
    anchor_hunt = load(ANCHOR_HUNT)
    scale_coeff = load(SCALE_COEFF)
    final_rho = load(FINAL_RHO)
    rho_unit_no_go = load(RHO_UNIT_NO_GO)
    rho_response_attempt = load(RHO_RESPONSE_ATTEMPT)
    action_norm = load(ACTION_NORM)

    rho_uv = float(final_rho["selected_values"]["rho_UV"])
    s_star = float(final_rho["selected_values"]["s_star_from_rho"])
    lambda_internal = float(
        modal_to_unit["conditional_theorem"]["conditional_map"]["exact_branch"]["lambda_internal"]
    )
    sqrt_lambda = math.sqrt(lambda_internal)

    structural_inputs = {
        "conditional_modal_to_unit_map_closed": modal_to_unit["status"]
        == "CONDITIONAL_MAP_CLOSED_PHYSICAL_UNIT_COEFFICIENT_OPEN",
        "physical_anchor_hunt_complete": anchor_hunt["status"]
        == "PHYSICAL_ANCHOR_SOURCE_HUNT_COMPLETE_DIRECT_ANCHOR_NOT_FOUND",
        "kappa_extracted": scale_coeff["verdict"]["kappa_extracted"],
        "formula_level_coefficient_gap_fixed": scale_coeff["verdict"]["formula_level_coefficient_gap_fixed"],
        "internal_rho_uv_closed": final_rho["closed"]["selected_internal_rho_uv"],
        "internal_action_units_closed": action_norm["verdict"]["canonical_internal_action_normalization_closed"],
    }

    open_inputs = {
        "C_UV_source_certified": False,
        "delta_source_certified": False,
        "C_UV_squared_over_delta_physical_scale_certified": scale_coeff["verdict"][
            "numeric_coefficients_extracted"
        ],
        "finite_memory_disturbance_covariance_certified": False,
        "O_alpha_prime_squared_correction_functional_certified": False,
        "fluctuation_dissipation_bridge_certified": False,
        "omega_gap_phys_selected": False,
    }

    # rho_UV is dimensionless and selected. It can normalize internal scale s_*,
    # but cannot by itself create a physical unit.
    internal_formulae = {
        "rho_UV": rho_uv,
        "s_star": s_star,
        "rho_UV_definition": "C_UV^2 / delta",
        "s_star_formula": "(60 rho_UV)^(1/6)",
        "lambda_internal_exact": lambda_internal,
        "sqrt_lambda_internal_exact": sqrt_lambda,
        "conditional_omega_relation": "Lambda_gap_phys = sqrt(15) * omega_gap_phys",
    }

    admissible_closure_formula = {
        "if_CUV_and_delta_physical_units_are_selected": {
            "rho_UV": "C_UV^2 / delta",
            "s_star": "(60 rho_UV)^(1/6)",
            "omega_gap_phys_candidate": "Omega_0 / s_star",
            "meaning_of_Omega_0": (
                "the one still-needed physical inverse-length/action unit supplied by the "
                "selected higher-order correction and finite-memory covariance theorem"
            ),
        },
        "why_rho_UV_alone_is_not_enough": (
            "rho_UV and s_star are dimensionless selected ratios. Multiplying the exact "
            "internal gap by them still leaves one physical unit Omega_0."
        ),
    }

    no_go_inputs = {
        "rho_unit_covariance_no_go_status": rho_unit_no_go["status"],
        "rho_response_attempt_status": rho_response_attempt["status"],
        "theta_5TeV_forbidden": anchor_hunt["hard_negative"]["theta_5TeV_promotable_to_prediction"] is False,
        "target_backsolve_forbidden": anchor_hunt["guardrails"]["uses_observed_target_backsolve"] is False,
    }

    theorem_ready = all(structural_inputs.values())
    physical_closed = theorem_ready and all(open_inputs.values())
    status = (
        "OMEGA_GAP_THEOREM_REDUCED_TO_CUV_DELTA_AND_OMEGA0_SOURCE_DATA"
        if theorem_ready and not physical_closed
        else "PHYSICAL_OMEGA_GAP_CLOSED"
        if physical_closed
        else "OMEGA_GAP_THEOREM_NOT_READY"
    )

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_physical_omega_gap_theorem",
        "status": status,
        "input_certificates": {
            "selected_modal_gap_to_physical_unit_theorem": str(MODAL_TO_UNIT),
            "selected_physical_anchor_source_hunt": str(ANCHOR_HUNT),
            "selected_scale_coefficient_extraction": str(SCALE_COEFF),
            "final_internal_rho_uv_selected_radius_theorem": str(FINAL_RHO),
            "selected_rho_uv_unit_covariance_no_go": str(RHO_UNIT_NO_GO),
            "selected_rho_uv_response_ratio_computation_attempt": str(RHO_RESPONSE_ATTEMPT),
            "physical_action_normalization": str(ACTION_NORM),
        },
        "structural_inputs": structural_inputs,
        "open_inputs": open_inputs,
        "internal_formulae": internal_formulae,
        "admissible_closure_formula": admissible_closure_formula,
        "no_go_inputs": no_go_inputs,
        "theorem": {
            "name": "Selected_Physical_Omega_Gap_Theorem.v1",
            "status": "REDUCED_NOT_CLOSED",
            "statement": (
                "The selected physical omega-gap is reduced to one source-certified physical "
                "scale theorem: compute the selected O(alpha'^2) UV correction coefficient "
                "C_UV, the finite-memory disturbance covariance delta, and the remaining "
                "physical unit Omega_0 from the same branch. The current corpus closes "
                "kappa=1, rho_UV, and the internal exact gap, but not Omega_0."
            ),
            "what_would_close": [
                "selected O(alpha'^2) correction functional evaluated on the branch",
                "selected finite-memory disturbance covariance delta",
                "fluctuation-dissipation/projection theorem tying delta to the same Hessian normalization",
                "physical unit Omega_0, independent of observed target constants",
            ],
        },
        "guardrails": {
            "claims_omega_gap_phys": False,
            "claims_physical_Newton_or_Planck": False,
            "uses_theta_5TeV_as_prediction": False,
            "uses_observed_target_backsolve": False,
            "treats_dimensionless_rho_as_physical_unit": False,
            "adds_new_GR_parameter": False,
        },
        "next_required_artifact": {
            "name": "Selected_Higher_Order_Correction_and_Disturbance_Covariance_Theorem",
            "must_supply": [
                "C_UV from the selected higher-alpha-prime/curvature correction functional",
                "delta from the selected finite-memory disturbance covariance",
                "Omega_0 or equivalent physical inverse-length unit",
                "same-branch proof tying these to the exact damping Hessian normalization",
            ],
        },
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected Physical Omega Gap Theorem v1

## Result

The physical omega-gap is not yet closed, but it is reduced to a single
source-data problem.

Closed internal data:

```text
lambda_internal = 15
rho_UV = {rho_uv:.15g}
s_star = {s_star:.15g}
kappa = 1
```

The admissible physical form is:

```text
Lambda_gap_phys = sqrt(15) * omega_gap_phys
omega_gap_phys = Omega_0 / s_star
```

where `Omega_0` is the remaining physical inverse-length/action unit. The
dimensionless selected ratio `rho_UV=C_UV^2/delta` fixes internal scale
placement, but it does not by itself supply physical units.

## What Would Close It

The next source theorem must compute:

```text
C_UV
delta
Omega_0
```

from the selected higher-order correction functional, the finite-memory
disturbance covariance, and a same-branch fluctuation-dissipation/projection
normalization.

## Guardrail

Theta `5 TeV`, observed `G_N`, observed `M_Pl`, cosmological scales, and
absolute particle masses cannot be used to select `Omega_0`.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
