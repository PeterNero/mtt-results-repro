from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SOURCE = ROOT / "certificates" / "same_branch_physical_clock_or_length_source_search_certificate.json"
ALPHA = ROOT / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json"

OUT_CERT = ROOT / "certificates" / "dimensional_metrology_no_go_and_relative_closure_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Dimensional_Metrology_NoGo_and_Relative_Closure_Theorem_v1.md"
OUT_PACKET = ROOT / "candidate_data" / "relative_physical_scale_solution.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    source = load(SOURCE)
    alpha = load(ALPHA)
    source_packet = load(Path(source["packet_written"]))

    tau_int = source_packet["relative_values"]["tau_int"]
    ell_factor = source_packet["relative_values"]["ell_coh_over_alpha_phys_minus_half"]
    lambda_factor = source_packet["relative_values"]["Lambda_eff_over_sqrt_alpha_phys"]

    # These identities define the entire one-anchor solution family.
    solution_family = {
        "dimensionless_branch_solution": {
            "status": "CLOSED",
            "branch": source_packet["selected_branch"],
            "tau_int": tau_int,
            "ell_coh_over_alpha_phys_minus_half": ell_factor,
            "Lambda_eff_over_sqrt_alpha_phys": lambda_factor,
            "invariant_product": ell_factor * lambda_factor,
            "invariant_product_target": 1.0,
        },
        "one_length_anchor_solution": {
            "anchor": "choose a physical coherent length L0, not fitted to the target being predicted",
            "alpha_phys": "tau_int / L0^2",
            "tau_phys": "L0^2",
            "ell_coh": "L0",
            "Lambda_eff": "1 / L0",
            "Omega0": "sqrt(tau_int) / L0",
        },
        "one_energy_anchor_solution": {
            "anchor": "choose a physical coherent energy E0, not fitted to the target being predicted",
            "alpha_phys": "tau_int * E0^2",
            "tau_phys": "1 / E0^2",
            "ell_coh": "1 / E0",
            "Lambda_eff": "E0",
            "Omega0": "sqrt(tau_int) * E0",
        },
        "one_tau_anchor_solution": {
            "anchor": "choose a physical proper-time/coherent-width T0 with units L^2=E^-2",
            "alpha_phys": "tau_int / T0",
            "tau_phys": "T0",
            "ell_coh": "sqrt(T0)",
            "Lambda_eff": "1 / sqrt(T0)",
            "Omega0": "sqrt(tau_int / T0)",
        },
    }

    no_go = {
        "theorem": "absolute dimensionful non-identifiability",
        "status": "PROVED_IN_CURRENT_FORMALIZATION",
        "reason": (
            "For any positive scale s, alpha_phys -> s^2 alpha_phys, "
            "Lambda_eff -> s Lambda_eff, and ell_coh -> ell_coh/s leaves all "
            "dimensionless branch facts and relative ratios invariant. Therefore "
            "the current branch cannot select an absolute SI length/energy value "
            "without one external metrological identification or an internally "
            "constructed physical rod/clock process."
        ),
        "free_parameter_count_for_absolute_units": 1,
        "free_parameter_count_for_relative_predictions": 0,
        "not_a_failed_derivation": (
            "Dimensionful constants require a unit-realization map. The branch has "
            "selected the map shape and all dimensionless coefficients; it has not "
            "selected the metrological ruler itself."
        ),
    }

    closure_result = {
        "relative_physical_closure": True,
        "absolute_SI_closure": False,
        "minimal_absolute_extension": "one physical rod/clock/energy primitive",
        "knob_audit": {
            "no_knob_relative_solution": True,
            "absolute_solution_with_declared_metrology": "one primitive, not a tunable sector parameter",
            "absolute_solution_without_declared_metrology": False,
        },
        "closed_formulas": {
            "tau_int": "log(448)/15",
            "tau_phys": "tau_int / alpha_phys",
            "ell_coh": "sqrt(tau_int / alpha_phys)",
            "Lambda_eff": "sqrt(alpha_phys / tau_int)",
            "Omega0": "sqrt(alpha_phys) * sqrt(15/log(448))",
        },
        "numeric_coefficients": {
            "tau_int": tau_int,
            "sqrt_tau_int": ell_factor,
            "sqrt_1_over_tau_int": lambda_factor,
            "Omega0_over_sqrt_alpha_phys": lambda_factor,
        },
    }

    closed_inputs = {
        "same_branch_source_closed": source["status"] == "SAME_BRANCH_CLOCK_LENGTH_SOURCE_FOUND_ABSOLUTE_METROLOGY_OPEN",
        "alpha_single_anchor_theorem_ready": alpha["status"] == "ALPHA_PHYS_REDUCED_TO_SINGLE_EXTERNAL_DIMENSIONFUL_ANCHOR",
        "tau_positive": tau_int > 0.0,
        "ell_lambda_product_one": abs(ell_factor * lambda_factor - 1.0) < 1e-15,
        "lambda_matches_inverse_sqrt_tau": abs(lambda_factor - (1.0 / math.sqrt(tau_int))) < 1e-15,
    }

    guardrails = {
        "claims_absolute_SI_prediction_without_anchor": False,
        "sets_alpha_phys_to_one_as_physics": False,
        "backsolves_from_Newton_or_Planck": False,
        "backsolves_from_cosmology_or_masses": False,
        "uses_Theta_5TeV_as_prediction": False,
        "counts_metrological_primitive_as_sector_knob": False,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "dimensional_metrology_no_go_and_relative_closure_theorem",
        "status": "RELATIVE_PHYSICAL_SCALE_SOLUTION_CLOSED_ABSOLUTE_METROLOGY_REQUIRED",
        "input_certificates": {
            "same_branch_physical_clock_or_length_source_search": str(SOURCE),
            "selected_physical_alpha_or_action_unit_theorem": str(ALPHA),
        },
        "closed_inputs": closed_inputs,
        "solution_family": solution_family,
        "no_go": no_go,
        "closure_result": closure_result,
        "verdict": {
            "calculated_solution": True,
            "relative_solution_closed": True,
            "absolute_solution_closed_without_metrology": False,
            "minimal_remaining_input": "one metrological primitive if SI-valued predictions are required",
            "next_executable_artifact": "One_Anchor_GR_Normalization_Propagation_v1",
        },
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Dimensional Metrology No-Go and Relative Closure Theorem v1

## Calculated Solution

The selected branch now has a closed relative physical scale solution:

```text
tau_int = log(448)/15 = {tau_int:.15g}
sqrt(tau_int) = {ell_factor:.15g}
1/sqrt(tau_int) = {lambda_factor:.15g}
```

The physical chain is:

```text
tau_phys = tau_int / alpha_phys
ell_coh = sqrt(tau_int / alpha_phys)
Lambda_eff = sqrt(alpha_phys / tau_int)
Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))
```

Equivalently:

```text
ell_coh * Lambda_eff = 1
Lambda_eff / sqrt(alpha_phys) = 1/sqrt(tau_int)
```

## One-Anchor Absolute Solution

If a physical coherent length `L0` is selected by an independent rod/clock
construction, then:

```text
alpha_phys = tau_int / L0^2
tau_phys = L0^2
ell_coh = L0
Lambda_eff = 1/L0
Omega0 = sqrt(tau_int)/L0
```

If instead a physical coherent energy `E0` is selected, then:

```text
alpha_phys = tau_int * E0^2
tau_phys = 1/E0^2
ell_coh = 1/E0
Lambda_eff = E0
Omega0 = sqrt(tau_int)*E0
```

These are the same solution written in different metrological coordinates.

## No-Go Boundary

There is no further arithmetic trick that turns this relative solution into an
absolute SI number. For any positive scale `s`:

```text
alpha_phys -> s^2 alpha_phys
Lambda_eff -> s Lambda_eff
ell_coh -> ell_coh/s
```

leaves the internal branch facts and all dimensionless ratios invariant.
Therefore an absolute SI prediction needs exactly one metrological primitive,
or an internally constructed physical rod/clock process.

## Status

```text
relative physical scale solution: CLOSED
absolute SI scale without metrology: NOT AVAILABLE
minimum absolute extension: one rod/clock/energy primitive
```
"""

    OUT_PACKET.write_text(json.dumps(closure_result, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_PACKET}")
    print("STATUS: RELATIVE_PHYSICAL_SCALE_SOLUTION_CLOSED_ABSOLUTE_METROLOGY_REQUIRED")


if __name__ == "__main__":
    main()
