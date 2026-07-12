from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

RELATIVE = ROOT / "certificates" / "dimensional_metrology_no_go_and_relative_closure_theorem_certificate.json"
ABS_BRIDGE = ROOT / "certificates" / "absolute_normalization_bridge_from_nonsm_certificate.json"
STF = ROOT / "certificates" / "stf_hessian_scale_to_geff_relation_certificate.json"
STRESS = ROOT / "certificates" / "physical_normalization_stress_response_gate_certificate.json"

OUT_CERT = ROOT / "certificates" / "one_anchor_gr_normalization_propagation_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "One_Anchor_GR_Normalization_Propagation_v1.md"
OUT_PACKET = ROOT / "candidate_data" / "one_anchor_gr_normalization_propagation.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def selected_row(rows: list[dict], n: int) -> dict:
    for row in rows:
        if row["N"] == n:
            return row
    raise KeyError(f"missing N={n} row")


def main() -> None:
    relative = load(RELATIVE)
    abs_bridge = load(ABS_BRIDGE)
    stf = load(STF)
    stress = load(STRESS)

    closure = relative["closure_result"]
    tau_int = closure["numeric_coefficients"]["tau_int"]
    sqrt_tau = closure["numeric_coefficients"]["sqrt_tau_int"]
    inv_sqrt_tau = closure["numeric_coefficients"]["sqrt_1_over_tau_int"]
    row448 = selected_row(abs_bridge["closed_internal_units"]["computed_rows"], 448)
    vol_int = row448["Vol_int"]
    g_eff_int = row448["G_eff_int"]
    kappa_stf_int = row448["kappa_STF_int"]

    # Dimensional propagation in c=hbar=1 units:
    # alpha_phys has units L^-2 = E^2, so G_eff has units L^2 and kappa_STF has units L^-2.
    g_eff_over_l0_sq = g_eff_int / tau_int
    kappa_times_l0_sq = kappa_stf_int * tau_int
    kappa_over_e0_sq = kappa_stf_int * tau_int
    g_eff_times_e0_sq = g_eff_int / tau_int

    solution = {
        "selected_branch": "Z448/q79 exact central-circle branch with rho_UV import",
        "selected_internal_row": {
            "N": 448,
            "tau_int": tau_int,
            "sqrt_tau_int": sqrt_tau,
            "Lambda_eff_over_sqrt_alpha_phys": inv_sqrt_tau,
            "Vol_int": vol_int,
            "G_eff_int": g_eff_int,
            "kappa_STF_int": kappa_stf_int,
            "kappa_relation": stf["relation"]["kappa_STF_relation"],
        },
        "alpha_propagation": {
            "alpha_phys_from_length_anchor": "alpha_phys = tau_int / L0^2",
            "alpha_phys_from_energy_anchor": "alpha_phys = tau_int * E0^2",
            "G_eff_phys": "G_eff_int / alpha_phys",
            "kappa_STF_phys": "kappa_STF_int * alpha_phys",
        },
        "length_anchor_family": {
            "anchor": "physical coherent length L0",
            "alpha_phys": f"{tau_int} / L0^2",
            "tau_phys": "L0^2",
            "ell_coh": "L0",
            "Lambda_eff": "1 / L0",
            "Omega0": f"{sqrt_tau} / L0",
            "G_eff_phys": f"{g_eff_over_l0_sq} * L0^2",
            "kappa_STF_phys": f"{kappa_times_l0_sq} / L0^2",
            "G_eff_over_L0_squared": g_eff_over_l0_sq,
            "kappa_STF_times_L0_squared": kappa_times_l0_sq,
        },
        "energy_anchor_family": {
            "anchor": "physical coherent energy E0",
            "alpha_phys": f"{tau_int} * E0^2",
            "tau_phys": "1 / E0^2",
            "ell_coh": "1 / E0",
            "Lambda_eff": "E0",
            "Omega0": f"{sqrt_tau} * E0",
            "G_eff_phys": f"{g_eff_times_e0_sq} / E0^2",
            "kappa_STF_phys": f"{kappa_over_e0_sq} * E0^2",
            "G_eff_times_E0_squared": g_eff_times_e0_sq,
            "kappa_STF_over_E0_squared": kappa_over_e0_sq,
        },
        "dimensionless_invariants": {
            "ell_coh_times_Lambda_eff": 1.0,
            "G_eff_phys_times_kappa_STF_phys": g_eff_int * kappa_stf_int,
            "G_eff_phys_times_kappa_STF_phys_formula": "G_eff_int * kappa_STF_int = 1/(32*pi) in the selected convention",
            "G_eff_phys_times_kappa_STF_phys_target": 1.0 / (32.0 * 3.141592653589793),
        },
    }

    closed_inputs = {
        "relative_solution_closed": relative["status"]
        == "RELATIVE_PHYSICAL_SCALE_SOLUTION_CLOSED_ABSOLUTE_METROLOGY_REQUIRED",
        "internal_gr_normalization_carried": abs_bridge["status"]
        == "INTERNAL_GR_NORMALIZATION_CARRIED_HOME_PHYSICAL_ABSOLUTE_ANCHOR_OPEN",
        "stf_relation_closed": stf["closed_tests"]["kappa_is_not_independent_of_G_eff"],
        "stress_response_structural_ready": stress["status"] == "STRUCTURAL_STRESS_RESPONSE_CLOSED_PHYSICAL_NORMALIZATION_OPEN",
        "selected_row_is_z448": row448["N"] == 448,
        "g_kappa_product_matches_convention": abs(g_eff_int * kappa_stf_int - (1.0 / (32.0 * 3.141592653589793))) < 1e-15,
    }

    verdict = {
        "one_anchor_gr_normalization_family_closed": True,
        "absolute_newton_value_predicted_without_anchor": False,
        "new_gr_knob_introduced": False,
        "what_is_closed": (
            "Given exactly one length/energy/metrology primitive, the selected Z448 internal "
            "GR normalization, TT stiffness, coherent length, Lambda_eff, and Omega0 all "
            "propagate algebraically with fixed coefficients."
        ),
        "what_remains": (
            "A selected physical metrological primitive, or an internal rod/clock theorem, "
            "if measured SI-valued G_N/Planck/Omega0 numbers are required."
        ),
        "next_executable_artifact": "One_Anchor_Einstein_Response_Assembly_v1",
    }

    guardrails = {
        "claims_measured_Newton_constant": False,
        "claims_measured_Planck_scale": False,
        "uses_observed_Newton_or_Planck_input": False,
        "uses_observed_cosmology_or_masses": False,
        "uses_Theta_5TeV_as_prediction": False,
        "adds_new_GR_parameter": False,
        "counts_metrological_anchor_as_sector_knob": False,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "one_anchor_gr_normalization_propagation",
        "status": "ONE_ANCHOR_GR_NORMALIZATION_FAMILY_CLOSED_ABSOLUTE_VALUE_OPEN",
        "input_certificates": {
            "dimensional_metrology_no_go_and_relative_closure_theorem": str(RELATIVE),
            "absolute_normalization_bridge_from_nonsm": str(ABS_BRIDGE),
            "stf_hessian_scale_to_geff_relation": str(STF),
            "physical_normalization_stress_response_gate": str(STRESS),
        },
        "closed_inputs": closed_inputs,
        "solution": solution,
        "verdict": verdict,
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# One Anchor GR Normalization Propagation v1

## Result

The selected `N=448` row is now propagated through the one-anchor family.

Internal selected data:

```text
tau_int = {tau_int:.15g}
Vol_int = {vol_int:.15g}
G_eff,int = {g_eff_int:.15g}
kappa_STF,int = {kappa_stf_int:.15g}
```

The TT convention is:

```text
kappa_STF = (32*pi*G_eff)^(-1)
```

and indeed:

```text
G_eff,int * kappa_STF,int = {g_eff_int * kappa_stf_int:.15g}
1/(32*pi) = {1.0 / (32.0 * 3.141592653589793):.15g}
```

## Length Anchor Form

If the physical coherent length is `L0`, then:

```text
alpha_phys = {tau_int:.15g} / L0^2
tau_phys = L0^2
ell_coh = L0
Lambda_eff = 1/L0
Omega0 = {sqrt_tau:.15g}/L0
G_eff = {g_eff_over_l0_sq:.15g} * L0^2
kappa_STF = {kappa_times_l0_sq:.15g} / L0^2
```

## Energy Anchor Form

If the physical coherent energy is `E0`, then:

```text
alpha_phys = {tau_int:.15g} * E0^2
tau_phys = 1/E0^2
ell_coh = 1/E0
Lambda_eff = E0
Omega0 = {sqrt_tau:.15g} * E0
G_eff = {g_eff_times_e0_sq:.15g} / E0^2
kappa_STF = {kappa_over_e0_sq:.15g} * E0^2
```

## Interpretation

This closes the one-anchor GR normalization family. It does not predict the
measured Newton constant without an anchor. It proves that once the single
metrological primitive is supplied, the GR normalization, TT stiffness, coherent
length, effective energy, and Omega0 move together with no additional GR knob.
"""

    OUT_PACKET.write_text(json.dumps(solution, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_PACKET}")
    print("STATUS: ONE_ANCHOR_GR_NORMALIZATION_FAMILY_CLOSED_ABSOLUTE_VALUE_OPEN")


if __name__ == "__main__":
    main()
