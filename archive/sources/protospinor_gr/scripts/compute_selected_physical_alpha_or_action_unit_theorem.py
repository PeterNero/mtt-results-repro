from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

OMEGA_CONVENTION = ROOT / "certificates" / "selected_omega_convention_theorem_certificate.json"
ANCHOR_HUNT = ROOT / "certificates" / "selected_physical_anchor_source_hunt_certificate.json"
SCALE_GATE = ROOT / "certificates" / "physical_scale_lifting_anchor_gate_certificate.json"
PHYSICAL_ACTION = NONSM / "certificates" / "physical_action_normalization_gate_certificate.json"
DIMENSIONFUL_OBSTRUCTION = NONSM / "certificates" / "dimensionful_constant_obstruction_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Physical_Alpha_or_Action_Unit_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    omega = load(OMEGA_CONVENTION)
    anchor = load(ANCHOR_HUNT)
    scale_gate = load(SCALE_GATE)
    physical_action = load(PHYSICAL_ACTION)
    obstruction = load(DIMENSIONFUL_OBSTRUCTION)

    omega_factor = omega["reduced_formula"]["Omega0_over_sqrt_alpha_phys"]
    alpha_int = physical_action["canonical_internal_normalization"]["alpha_int"]
    g10_int = physical_action["canonical_internal_normalization"]["G10_int"]

    closed_inputs = {
        "omega_convention_closed": omega["status"] == "CHI_OMEGA_CONVENTION_CLOSED_ALPHA_OPEN",
        "physical_anchor_hunt_complete": anchor["status"] == "PHYSICAL_ANCHOR_SOURCE_HUNT_COMPLETE_DIRECT_ANCHOR_NOT_FOUND",
        "direct_anchor_not_found": anchor["hard_negative"]["direct_physical_anchor_found_in_current_sources"] is False,
        "theta_5TeV_forbidden": anchor["hard_negative"]["theta_5TeV_promotable_to_prediction"] is False,
        "internal_action_normalization_closed": physical_action["verdict"]["canonical_internal_action_normalization_closed"],
        "internal_alpha_equals_one": alpha_int == 1.0,
        "internal_G10_equals_one": g10_int == 1.0,
        "physical_absolute_no_go_active": physical_action["verdict"]["no_go_without_external_dimensional_anchor"],
        "dimensionful_obstruction_certified": obstruction["status"] == "OBSTRUCTION_CERTIFIED",
        "physical_scale_lift_still_open": scale_gate["open_tests"]["physical_absolute_dimensionful_anchor_closed"] is False,
    }

    theorem_result = {
        "alpha_int": alpha_int,
        "G10_int": g10_int,
        "alpha_phys_status": "SOLE_REMAINING_EXTERNAL_DIMENSIONFUL_ANCHOR",
        "physical_numeric_alpha_selected": False,
        "reason": (
            "All preceding dimensionless branch data are closed, but the corpus contains "
            "an explicit dimensionful obstruction: an absolute physical unit cannot be "
            "predicted from dimensionless internal data without an independently selected "
            "dimensional anchor."
        ),
        "allowed_outputs_without_new_anchor": [
            "internal-unit Omega0 coefficient",
            "dimensionless ratios",
            "conditional physical formulae parameterized by alpha_phys",
            "no-backsolve structural constraints",
        ],
        "forbidden_outputs_without_new_anchor": [
            "numeric Newton constant",
            "numeric reduced Planck mass",
            "numeric physical Omega0",
            "numeric SI length/action scale",
        ],
    }

    final_reduction = {
        "Omega0": "sqrt(alpha_phys) * sqrt(15/log(448))",
        "Omega0_over_sqrt_alpha_phys": omega_factor,
        "alpha_phys_if_Omega0_were_independently_measured": "Omega0^2 * log(448) / 15",
        "alpha_phys_backsolve_forbidden_as_prediction": True,
        "canonical_internal_units": {
            "alpha_int": alpha_int,
            "Omega0_internal": omega_factor,
            "interpretation": "internal exact-branch action units only, not SI units",
        },
    }

    route_forward = {
        "strict_no_knob_completion_requires": (
            "a new target-independent dimensional anchor from another selected sector, "
            "for example a physical modal-gap unit, string/M-theory length/action unit, "
            "or externally fixed unit not among the constants being predicted"
        ),
        "credible_current_claim": (
            "The GR/protospinor exact branch is closed up to the single unavoidable "
            "absolute action/unit anchor alpha_phys."
        ),
        "full_physical_GR_claim_status": "CONDITIONAL_ON_ALPHA_PHYS_OR_EQUIVALENT_DIMENSIONFUL_ANCHOR",
    }

    guardrails = {
        "uses_observed_Newton_or_Planck_input": False,
        "uses_observed_Omega0_input": False,
        "uses_theta_5TeV_as_prediction": False,
        "sets_alpha_phys_to_internal_one_as_SI_prediction": False,
        "backsolves_alpha_phys_from_target": False,
        "claims_physical_Omega0_numeric_closed": False,
        "claims_Newton_or_Planck_prediction": False,
        "claims_full_physical_GR_closed": False,
    }

    ready = all(closed_inputs.values())
    status = "ALPHA_PHYS_REDUCED_TO_SINGLE_EXTERNAL_DIMENSIONFUL_ANCHOR" if ready else "ALPHA_THEOREM_INPUTS_NOT_READY"

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_physical_alpha_or_action_unit_theorem",
        "status": status,
        "input_certificates": {
            "selected_omega_convention": str(OMEGA_CONVENTION),
            "selected_physical_anchor_source_hunt": str(ANCHOR_HUNT),
            "physical_scale_lifting_anchor_gate": str(SCALE_GATE),
            "physical_action_normalization": str(PHYSICAL_ACTION),
            "dimensionful_constant_obstruction": str(DIMENSIONFUL_OBSTRUCTION),
        },
        "closed_inputs": closed_inputs,
        "theorem_result": theorem_result,
        "final_reduction": final_reduction,
        "route_forward": route_forward,
        "guardrails": guardrails,
        "theorem": {
            "name": "Selected_Physical_Alpha_or_Action_Unit_Theorem.v1",
            "status": "INTERNAL_ALPHA_CLOSED_PHYSICAL_ALPHA_IS_SINGLE_EXTERNAL_ANCHOR",
            "statement": (
                "The selected branch closes alpha in canonical internal action units "
                "(alpha_int=1, G10_int=1), but the physical alpha_phys is not selected "
                "by the current dimensionless corpus. The entire Omega0/GR normalization "
                "chain is therefore reduced to one external absolute action/unit anchor: "
                "Omega0=sqrt(alpha_phys)*sqrt(15/log(448)). A numeric physical prediction "
                "requires a new target-independent dimensional anchor; backsolving from "
                "Newton, Planck, cosmological, mass, or TeV targets is forbidden."
            ),
        },
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected Physical Alpha or Action Unit Theorem v1

## Result

The remaining physical normalization gate is reduced as far as the current
corpus allows.

Closed internally:

```text
alpha_int = {alpha_int:.15g}
G10_int = {g10_int:.15g}
```

These are canonical exact-branch action units. They are not SI predictions.

The physical formula is:

```text
Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))
Omega0/sqrt(alpha_phys) = {omega_factor:.15g}
```

Thus `alpha_phys` is the only remaining absolute normalization object in this
chain.

Equivalently: alpha_phys is the only remaining absolute normalization object.

## No-Go

The current corpus does not select a physical numeric value for `alpha_phys`.
This is not a missing arithmetic step. It is the standard dimensionful
normalization obstruction already certified by the non-SM constants repo:
dimensionless internal data cannot predict an absolute SI scale unless one
independent dimensional anchor is selected first.

Forbidden moves:

```text
set alpha_phys=1 and call it SI physics
backsolve alpha_phys from observed Newton or Planck data
promote Theta 5 TeV calibration into a prediction
fit Omega0 to cosmology or masses
```

## What Is Achieved

The branch is closed up to exactly one external action/unit anchor:

```text
N = 448
epsilon_adm = 1/448
C_Q = 1
chi_omega = 1
Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))
```

A future strict no-knob physical closure must add a target-independent
dimensional anchor from another selected sector, such as a physical modal-gap
unit, an M/string length-action unit, or an externally fixed unit not among the
constants being predicted.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
