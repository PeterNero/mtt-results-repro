from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SHARP_CERT = ROOT / "certificates" / "selected_sharp_semigroup_bound_theorem_certificate.json"
OMEGA0_CERT = ROOT / "certificates" / "selected_physical_omega0_source_theorem_certificate.json"
OMEGA_GAP_CERT = ROOT / "certificates" / "selected_physical_omega_gap_theorem_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_omega_convention_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Omega_Convention_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    sharp = load(SHARP_CERT)
    omega0 = load(OMEGA0_CERT)
    omega_gap = load(OMEGA_GAP_CERT)

    factor = sharp["omega0_formula"]["Omega0_over_chi_sqrt_alpha"]
    s_star = omega_gap["internal_formulae"]["s_star"]
    chi_omega = 1.0
    omega0_over_sqrt_alpha = chi_omega * factor
    omega_gap_over_sqrt_alpha = omega0_over_sqrt_alpha / s_star
    lambda_gap_over_sqrt_alpha = math.sqrt(15.0) * omega_gap_over_sqrt_alpha

    closed_inputs = {
        "sharp_semigroup_reduction_available": sharp["status"]
        == "CQ1_SHARP_SEMIGROUP_BOUND_CLOSED_ALPHA_CHI_OPEN",
        "omega0_source_schema_available": omega0["status"] == "OMEGA0_REDUCED_TO_PHYSICAL_ALPHA_CQ_EPSILON_AND_CHI",
        "omega_gap_relation_available": omega_gap["internal_formulae"]["conditional_omega_relation"]
        == "Lambda_gap_phys = sqrt(15) * omega_gap_phys",
        "s_star_imported": abs(s_star - 1.464646774701829) < 1e-15,
        "factor_after_CQ_epsilon_closure_matches": abs(factor - math.sqrt(15.0 / math.log(448.0))) < 1e-15,
    }

    convention_selection = {
        "selected_symbol": "Omega0",
        "selected_convention": "Omega0 names the physical damping/admissibility scale Lambda_eff itself",
        "chi_omega": chi_omega,
        "alternative_not_selected": {
            "convention": "omega_gap_phys names Lambda_eff and Omega0=s_star*omega_gap_phys",
            "chi_omega": s_star,
            "reason_rejected_as_default": (
                "It is an equally valid reparameterization, but it makes Omega0 a derived "
                "post-radius symbol rather than the primitive source scale named in the "
                "Omega0 gate."
            ),
        },
        "why_not_physical_parameter": (
            "chi_omega is not a physical parameter. Changing chi_omega here only renames "
            "which physical inverse-length symbol is called Omega0. It does not alter the "
            "dimensionless internal branch, the finite quotient, epsilon_adm, C_Q, s_star, "
            "or the remaining physical action unit."
        ),
    }

    reduced_formula = {
        "Omega0": "sqrt(alpha_phys) * sqrt(15/log(448))",
        "Omega0_over_sqrt_alpha_phys": omega0_over_sqrt_alpha,
        "omega_gap_phys": "Omega0 / s_star",
        "omega_gap_phys_over_sqrt_alpha_phys": omega_gap_over_sqrt_alpha,
        "Lambda_gap_phys": "sqrt(15) * Omega0 / s_star",
        "Lambda_gap_phys_over_sqrt_alpha_phys": lambda_gap_over_sqrt_alpha,
        "s_star": s_star,
    }

    guardrails = {
        "uses_observed_Newton_or_Planck_input": False,
        "uses_observed_Omega0_input": False,
        "fits_chi_omega_to_target": False,
        "adds_dimensionless_physical_parameter": False,
        "claims_alpha_phys_selected": False,
        "claims_physical_Omega0_numeric_closed": False,
        "claims_Newton_or_Planck_prediction": False,
    }

    still_open = {
        "alpha_phys_or_action_unit_selected": False,
        "physical_Omega0_numeric_closed": False,
        "physical_Newton_or_Planck_predicted": False,
    }

    ready = all(closed_inputs.values())
    status = "CHI_OMEGA_CONVENTION_CLOSED_ALPHA_OPEN" if ready else "OMEGA_CONVENTION_INPUTS_NOT_READY"

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_omega_convention_theorem",
        "status": status,
        "input_certificates": {
            "selected_sharp_semigroup_bound": str(SHARP_CERT),
            "selected_physical_omega0_source": str(OMEGA0_CERT),
            "selected_physical_omega_gap": str(OMEGA_GAP_CERT),
        },
        "closed_inputs": closed_inputs,
        "convention_selection": convention_selection,
        "reduced_formula": reduced_formula,
        "guardrails": guardrails,
        "still_open": still_open,
        "theorem": {
            "name": "Selected_Omega_Convention_Theorem.v1",
            "status": "CHI_OMEGA_EQUALS_1_BY_SYMBOL_CONVENTION",
            "statement": (
                "The symbol Omega0 is selected to denote the physical damping/"
                "admissibility scale Lambda_eff itself. Therefore chi_omega=1 by "
                "definition of the Omega0 slot. The post-radius gap unit remains "
                "omega_gap_phys=Omega0/s_star. This closes only a naming convention; "
                "the physical action/unit anchor alpha_phys remains open."
            ),
        },
        "next_required_artifacts": [
            "Selected_Physical_Alpha_or_Action_Unit_Theorem_v1",
        ],
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected Omega Convention Theorem v1

## Result

The dimensionless convention factor is closed:

```text
chi_omega = 1.
```

This is not a new physical parameter. It fixes the symbol convention:

```text
Omega0 := Lambda_eff,phys
```

while the post-radius physical gap unit remains:

```text
omega_gap_phys = Omega0 / s_star
s_star = {s_star:.15g}
```

The alternative convention,

```text
omega_gap_phys := Lambda_eff,phys
Omega0 = s_star * omega_gap_phys
```

is mathematically equivalent, but it makes `Omega0` a derived post-radius
symbol. The repository's Omega0 gate uses `Omega0` as the primitive source scale,
so the selected convention is `chi_omega=1`.

## Reduced Formula

Using the already closed facts:

```text
N = 448
epsilon_adm = 1/448
C_Q = 1
lambda_star = 15
```

the physical scale is reduced to:

```text
Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))
Omega0/sqrt(alpha_phys) = {omega0_over_sqrt_alpha:.15g}
```

and:

```text
omega_gap_phys/sqrt(alpha_phys) = {omega_gap_over_sqrt_alpha:.15g}
Lambda_gap_phys/sqrt(alpha_phys) = {lambda_gap_over_sqrt_alpha:.15g}
```

## Still Open

Only the actual physical action/unit anchor remains:

```text
alpha_phys
```

No observed Newton, Planck, cosmological, mass, or TeV value is used.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
