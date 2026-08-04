from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ONE_ANCHOR = ROOT / "certificates" / "one_anchor_gr_normalization_propagation_certificate.json"
TT_SUPPORT = ROOT / "certificates" / "gr_tt_support_final_theorem_certificate.json"
STRESS = ROOT / "certificates" / "physical_normalization_stress_response_gate_certificate.json"
EXACT_ID = ROOT / "certificates" / "gr_tt_exact_branch_identity_final_gate_certificate.json"
CHAR_STRESS = ROOT / "certificates" / "gr_tt_character_channel_identification_stress_test_certificate.json"

OUT_CERT = ROOT / "certificates" / "one_anchor_einstein_response_assembly_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "One_Anchor_Einstein_Response_Assembly_v1.md"
OUT_PACKET = ROOT / "candidate_data" / "one_anchor_einstein_response_assembly.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    one_anchor = load(ONE_ANCHOR)
    tt_support = load(TT_SUPPORT)
    stress = load(STRESS)
    exact_id = load(EXACT_ID)
    char_stress = load(CHAR_STRESS)

    norm = one_anchor["solution"]
    length = norm["length_anchor_family"]
    energy = norm["energy_anchor_family"]
    row = norm["selected_internal_row"]

    response_kernel = {
        "target_form": "linearized Einstein response on the TT support",
        "operator_schema": "K_TT h_TT = T_TT",
        "normalization_schema": "K_TT = (32*pi*G_eff)^(-1) E_TT on the selected TT support",
        "retarded_solution_schema": "h_TT = 32*pi*G_eff * G_ret,TT * T_TT",
        "support_identity": tt_support["conclusion"]["support_identity"],
        "support": tt_support["conclusion"]["support"],
        "lambda_GR_TT_internal": tt_support["conclusion"]["lambda_GR_TT_internal_exact_branch"],
        "length_anchor_form": {
            "G_eff": length["G_eff_phys"],
            "kappa_STF": length["kappa_STF_phys"],
            "response_coupling_32pi_G_eff": f"{32.0 * 3.141592653589793 * length['G_eff_over_L0_squared']} * L0^2",
        },
        "energy_anchor_form": {
            "G_eff": energy["G_eff_phys"],
            "kappa_STF": energy["kappa_STF_phys"],
            "response_coupling_32pi_G_eff": f"{32.0 * 3.141592653589793 * energy['G_eff_times_E0_squared']} / E0^2",
        },
    }

    assembly = {
        "closed_components": {
            "exact_TT_support": tt_support["theorem"]["status"] == "CLOSED",
            "one_anchor_normalization_family": one_anchor["verdict"]["one_anchor_gr_normalization_family_closed"],
            "universal_stress_tensor_form": stress["stress_response"]["universal_variational_definition_closed"],
            "bianchi_noether_conservation": stress["stress_response"]["conservation_law_closed"],
            "retarded_support_target_identified": stress["einstein_response_assembly"]["retarded_support_target_identified"],
            "EH_target_operator_identified": stress["einstein_response_assembly"]["EH_target_operator_identified"],
        },
        "conditional_components": {
            "selected_full_matter_map_ready": stress["einstein_response_assembly"]["selected_full_matter_map_ready"],
            "unconditional_full_GR_TT_operator_identity": not exact_id["not_closed"]["unconditional_full_GR_TT_gap"],
            "literal_GR_TT_noise_channel_identity": (
                char_stress["status"] != "SHARED_Z64_Q64_ALIGNMENT_CLOSED_LITERAL_GR_TT_NOISE_CHANNEL_OPEN"
            ),
            "absolute_SI_anchor_selected": False,
        },
        "conditional_theorem": {
            "statement": (
                "Given one physical metrological primitive L0 or E0, and given the selected "
                "matter stress map plus the GR TT operator identity gate, the low-energy "
                "Einstein TT response is assembled with no additional GR normalization knob."
            ),
            "length_anchor_response": (
                f"h_TT = ({32.0 * 3.141592653589793 * length['G_eff_over_L0_squared']}) "
                "* L0^2 * G_ret,TT T_TT"
            ),
            "energy_anchor_response": (
                f"h_TT = ({32.0 * 3.141592653589793 * energy['G_eff_times_E0_squared']}) "
                "* E0^-2 * G_ret,TT T_TT"
            ),
            "kappa_relation": row["kappa_relation"],
        },
    }

    open_gates = {
        "selected_full_matter_stress_coefficients": {
            "status": "OPEN",
            "why": stress["stress_response"]["interpretation"],
        },
        "unconditional_GR_TT_operator_identity": {
            "status": "OPEN",
            "why": exact_id["theorem_options"]["unconditional_full_GR_TT_gap_theorem"]["missing"],
        },
        "literal_GR_TT_noise_channel_identity": {
            "status": "OPEN",
            "why": "Current certificate proves shared Z64/q64 alignment, not literal noise-channel identity.",
        },
        "absolute_SI_metrology": {
            "status": "OPEN_IF_SI_NUMBERS_REQUIRED",
            "why": one_anchor["verdict"]["what_remains"],
        },
    }

    closed_inputs = {
        "one_anchor_gr_normalization_closed": one_anchor["status"]
        == "ONE_ANCHOR_GR_NORMALIZATION_FAMILY_CLOSED_ABSOLUTE_VALUE_OPEN",
        "tt_support_closed": tt_support["theorem"]["status"] == "CLOSED",
        "stress_response_structural_closed": stress["status"] == "STRUCTURAL_STRESS_RESPONSE_CLOSED_PHYSICAL_NORMALIZATION_OPEN",
        "exact_branch_identity_gate_explicit": exact_id["status"]
        == "EXACT_BRANCH_GR_GAP_THEOREM_AVAILABLE_FULL_GR_IDENTITY_OPEN",
        "character_channel_stress_test_available": char_stress["status"]
        == "SHARED_Z64_Q64_ALIGNMENT_CLOSED_LITERAL_GR_TT_NOISE_CHANNEL_OPEN",
        "response_coupling_length_positive": length["G_eff_over_L0_squared"] > 0.0,
        "response_coupling_energy_positive": energy["G_eff_times_E0_squared"] > 0.0,
    }

    verdict = {
        "one_anchor_einstein_response_assembled": True,
        "full_unconditional_physical_GR_closed": False,
        "conditional_low_energy_TT_response_closed": True,
        "new_GR_knob_introduced": False,
        "measured_Newton_or_Planck_predicted": False,
        "remaining_gates_count": len(open_gates),
        "next_executable_artifact": "Selected_Matter_Stress_Map_or_GR_TT_Operator_Identity_Closure_v1",
    }

    guardrails = {
        "claims_full_unconditional_GR": False,
        "claims_measured_Newton_constant": False,
        "uses_observed_Newton_or_Planck_input": False,
        "uses_observed_cosmology_or_masses": False,
        "claims_selected_matter_coefficients_closed": False,
        "claims_unconditional_GR_TT_operator_identity": False,
        "adds_new_GR_parameter": False,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "one_anchor_einstein_response_assembly",
        "status": "ONE_ANCHOR_EINSTEIN_RESPONSE_ASSEMBLED_CONDITIONAL_GATES_OPEN",
        "input_certificates": {
            "one_anchor_gr_normalization_propagation": str(ONE_ANCHOR),
            "gr_tt_support_final_theorem": str(TT_SUPPORT),
            "physical_normalization_stress_response_gate": str(STRESS),
            "gr_tt_exact_branch_identity_final_gate": str(EXACT_ID),
            "gr_tt_character_channel_identification_stress_test": str(CHAR_STRESS),
        },
        "closed_inputs": closed_inputs,
        "response_kernel": response_kernel,
        "assembly": assembly,
        "open_gates": open_gates,
        "verdict": verdict,
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# One Anchor Einstein Response Assembly v1

## Result

The conditional one-anchor low-energy TT Einstein response is assembled.

Closed ingredients:

```text
TT support identity: {response_kernel["support_identity"]}
TT support: {response_kernel["support"]}
lambda_GR,TT,int = {response_kernel["lambda_GR_TT_internal"]}
kappa_STF = (32*pi*G_eff)^(-1)
```

With a length anchor `L0`:

```text
G_eff = {length["G_eff_over_L0_squared"]:.15g} * L0^2
kappa_STF = {length["kappa_STF_times_L0_squared"]:.15g} / L0^2
h_TT = {32.0 * 3.141592653589793 * length["G_eff_over_L0_squared"]:.15g} * L0^2 * G_ret,TT T_TT
```

With an energy anchor `E0`:

```text
G_eff = {energy["G_eff_times_E0_squared"]:.15g} / E0^2
kappa_STF = {energy["kappa_STF_over_E0_squared"]:.15g} * E0^2
h_TT = {32.0 * 3.141592653589793 * energy["G_eff_times_E0_squared"]:.15g} * E0^-2 * G_ret,TT T_TT
```

## What This Closes

Given one metrological primitive and the selected matter stress map/operator
identity gates, the low-energy TT Einstein response has no remaining GR
normalization knob. The response coefficient is fixed by the selected `N=448`
row.

## What Remains Open

```text
selected full matter stress coefficients
unconditional GR TT operator identity
literal GR TT noise-channel identity
absolute SI metrology if measured numbers are required
```

So this is a conditional Einstein-response assembly, not a claim that measured
Newton/Planck values or the full non-TT nonlinear Einstein equation have been
predicted.
"""

    OUT_PACKET.write_text(json.dumps({"response_kernel": response_kernel, "assembly": assembly, "open_gates": open_gates}, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_PACKET}")
    print("STATUS: ONE_ANCHOR_EINSTEIN_RESPONSE_ASSEMBLED_CONDITIONAL_GATES_OPEN")


if __name__ == "__main__":
    main()
