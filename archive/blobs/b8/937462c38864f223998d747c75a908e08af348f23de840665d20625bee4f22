from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

STRESS = ROOT / "certificates" / "gr_tt_character_channel_identification_stress_test_certificate.json"
OMEGA_GAP = ROOT / "certificates" / "selected_physical_omega_gap_theorem_certificate.json"
MODAL_UNIT = ROOT / "certificates" / "selected_modal_gap_to_physical_unit_theorem_certificate.json"
ANCHOR_HUNT = ROOT / "certificates" / "selected_physical_anchor_source_hunt_certificate.json"
DAMPING_BRANCH = NONSM / "certificates" / "selected_damping_normalization_branch_certificate.json"
CENTRAL_LEMMA = NONSM / "certificates" / "selected_central_circle_damping_identification_lemma_certificate.json"
DAMPING_HESSIAN = NONSM / "certificates" / "damping_hessian_z64_block_identification_certificate.json"
ACTION_NORM = NONSM / "certificates" / "physical_action_normalization_gate_certificate.json"
DIM_OBSTRUCTION = NONSM / "certificates" / "dimensionful_constant_obstruction_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_physical_omega0_source_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Physical_Omega0_Source_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def finite_resolution_row(n: int, s_star: float) -> dict:
    lambda_eff_internal = math.sqrt(15.0 / math.log(n))
    r1_internal = 1.0 / lambda_eff_internal
    return {
        "N": n,
        "epsilon_adm_if_1_over_N": 1.0 / n,
        "Lambda_eff_internal_if_CQ_sigma_alpha_1": lambda_eff_internal,
        "R1_internal_if_sigma_1": r1_internal,
        "Omega0_internal_if_Omega0_equals_Lambda_eff": lambda_eff_internal,
        "Omega0_internal_if_omega_gap_equals_Lambda_eff": s_star * lambda_eff_internal,
    }


def main() -> None:
    stress = load(STRESS)
    omega_gap = load(OMEGA_GAP)
    modal_unit = load(MODAL_UNIT)
    anchor_hunt = load(ANCHOR_HUNT)
    damping_branch = load(DAMPING_BRANCH)
    central_lemma = load(CENTRAL_LEMMA)
    damping_hessian = load(DAMPING_HESSIAN)
    action_norm = load(ACTION_NORM)
    dim_obstruction = load(DIM_OBSTRUCTION)

    s_star = float(omega_gap["internal_formulae"]["s_star"])

    closed_inputs = {
        "shared_z64_q64_alignment_closed": stress["status"]
        == "SHARED_Z64_Q64_ALIGNMENT_CLOSED_LITERAL_GR_TT_NOISE_CHANNEL_OPEN",
        "omega_gap_reduced_to_Omega0": omega_gap["status"]
        == "OMEGA_GAP_THEOREM_REDUCED_TO_CUV_DELTA_AND_OMEGA0_SOURCE_DATA",
        "modal_to_unit_conditional_map_closed": modal_unit["status"]
        == "CONDITIONAL_MAP_CLOSED_PHYSICAL_UNIT_COEFFICIENT_OPEN",
        "physical_anchor_hunt_complete": anchor_hunt["status"]
        == "PHYSICAL_ANCHOR_SOURCE_HUNT_COMPLETE_DIRECT_ANCHOR_NOT_FOUND",
        "damping_branch_reduced": damping_branch["verdict"]["branch_finished_as_reduction"],
        "central_circle_lemma_closed_under_z64": central_lemma["verdict"][
            "lemma_closed_under_z64_tower_identification"
        ],
        "damping_hessian_exact_branch_identified": damping_hessian["verdict"][
            "exact_branch_hessian_kernel_identified"
        ],
        "canonical_internal_action_normalization_closed": action_norm["verdict"][
            "canonical_internal_action_normalization_closed"
        ],
        "dimensionful_obstruction_certified": dim_obstruction["status"] == "OBSTRUCTION_CERTIFIED",
    }

    source_reduction = {
        "damping_scale_internal_schema": damping_branch["selected_branch"]["damping_scale"],
        "central_circle_identification_schema": damping_branch["selected_branch"][
            "central_circle_identification"
        ],
        "exact_branch_lambda_star": damping_hessian["damping_consequence"]["normalized_lambda_star"],
        "physical_alpha_status": "open; internal alpha=1 is a normalized exact-branch convention",
        "Omega0_schema": (
            "Omega_0 = chi_omega * sqrt(alpha_phys) * "
            "sqrt(lambda_star_norm / log(C_Q/epsilon_adm))"
        ),
        "chi_omega_role": (
            "dimensionless convention selecting whether the damping scale is identified "
            "with Omega_0 directly or with omega_gap_phys=Omega_0/s_star"
        ),
        "if_Omega0_equals_Lambda_eff": "chi_omega = 1",
        "if_omega_gap_phys_equals_Lambda_eff": f"chi_omega = s_star = {s_star:.15g}",
    }

    finite_resolution_candidates = [
        finite_resolution_row(64, s_star),
        finite_resolution_row(79, s_star),
        finite_resolution_row(448, s_star),
    ]

    still_open = {
        "physical_alpha_or_equivalent_inverse_length_unit_selected": False,
        "C_Q_source_certified_physical_branch_value": False,
        "epsilon_adm_source_certified_physical_branch_value": False,
        "chi_omega_convention_source_certified": False,
        "unique_finite_resolution_N_selected_for_physical_omega0": False,
        "Omega0_physical_numeric_closed": False,
        "physical_Newton_or_Planck_predicted": False,
    }

    guardrails = {
        "uses_theta_5TeV_as_prediction": False,
        "uses_observed_Newton_or_Planck": False,
        "uses_observed_mass_or_cosmology": False,
        "treats_internal_alpha_1_as_physical_unit": False,
        "chooses_N_after_target_comparison": False,
        "claims_physical_Omega0": False,
        "claims_full_physical_GR": False,
    }

    ready = all(closed_inputs.values())
    physical_closed = ready and all(still_open.values())
    status = (
        "OMEGA0_REDUCED_TO_PHYSICAL_ALPHA_CQ_EPSILON_AND_CHI"
        if ready and not physical_closed
        else "PHYSICAL_OMEGA0_CLOSED"
        if physical_closed
        else "OMEGA0_SOURCE_THEOREM_INPUTS_NOT_READY"
    )

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_physical_omega0_source_theorem",
        "status": status,
        "input_certificates": {
            "gr_tt_character_channel_identification_stress_test": str(STRESS),
            "selected_physical_omega_gap_theorem": str(OMEGA_GAP),
            "selected_modal_gap_to_physical_unit_theorem": str(MODAL_UNIT),
            "selected_physical_anchor_source_hunt": str(ANCHOR_HUNT),
            "selected_damping_normalization_branch": str(DAMPING_BRANCH),
            "selected_central_circle_damping_identification_lemma": str(CENTRAL_LEMMA),
            "damping_hessian_z64_block_identification": str(DAMPING_HESSIAN),
            "physical_action_normalization": str(ACTION_NORM),
            "dimensionful_constant_obstruction": str(DIM_OBSTRUCTION),
        },
        "closed_inputs": closed_inputs,
        "source_reduction": source_reduction,
        "finite_resolution_candidates_internal_only": finite_resolution_candidates,
        "still_open": still_open,
        "guardrails": guardrails,
        "theorem": {
            "name": "Selected_Physical_Omega0_Source_Theorem.v1",
            "status": "REDUCED_NOT_PHYSICALLY_CLOSED",
            "statement": (
                "The remaining physical unit Omega_0 is reduced to a precise damping "
                "normalization problem. The selected exact Z64 damping Hessian supplies "
                "lambda_star_norm=15 and closes the internal central-circle damping "
                "branch. A physical Omega_0 still requires a source-certified physical "
                "alpha or equivalent inverse-length/action unit, source-certified C_Q "
                "and epsilon_adm for the physical branch, a dimensionless convention "
                "chi_omega tying Lambda_eff to Omega_0 or omega_gap_phys, and a selected "
                "finite resolution branch if N is used."
            ),
            "conditional_closure": (
                "Given alpha_phys>0, C_Q>epsilon_adm>0, chi_omega>0, and selected N "
                "or equivalent epsilon_adm, Omega_0 = chi_omega sqrt(alpha_phys) "
                "sqrt(15/log(C_Q/epsilon_adm)); then omega_gap_phys=Omega_0/s_star "
                "and Lambda_gap_phys=sqrt(15) Omega_0/s_star."
            ),
        },
        "next_required_artifacts": [
            "Selected_Physical_Alpha_or_Action_Unit_Theorem_v1",
            "Selected_Admissibility_Tolerance_and_Semigroup_Bound_Theorem_v1",
            "Selected_Omega_Convention_Theorem_v1",
        ],
        "note_written": str(OUT_NOTE),
    }

    rows = "\n".join(
        f"| {row['N']} | {row['Lambda_eff_internal_if_CQ_sigma_alpha_1']:.15g} | "
        f"{row['R1_internal_if_sigma_1']:.15g} | "
        f"{row['Omega0_internal_if_Omega0_equals_Lambda_eff']:.15g} | "
        f"{row['Omega0_internal_if_omega_gap_equals_Lambda_eff']:.15g} |"
        for row in finite_resolution_candidates
    )

    note = f"""# Selected Physical Omega0 Source Theorem v1

## Result

`Omega_0` is not physically closed, but the remaining source problem is now
precise.

Closed internal inputs:

```text
lambda_star_norm = 15
s_star = {s_star:.15g}
internal alpha = 1 as normalized exact-branch convention
```

The legal damping-scale schema is:

```text
tau_adm = log(C_Q/epsilon_adm) / lambda_star
Lambda_eff = sqrt(lambda_star / log(C_Q/epsilon_adm))
Omega_0 = chi_omega * sqrt(alpha_phys) * sqrt(15 / log(C_Q/epsilon_adm))
omega_gap_phys = Omega_0 / s_star
Lambda_gap_phys = sqrt(15) * Omega_0 / s_star
```

`chi_omega` records the remaining convention:

```text
chi_omega = 1       if Omega_0 is identified directly with Lambda_eff
chi_omega = s_star  if omega_gap_phys is identified with Lambda_eff
```

## Internal Candidate Table

These are internal-only values under `C_Q=1`, `epsilon_adm=1/N`,
`alpha=1`, and `chi_omega` as shown. They are not physical predictions.

| N | Lambda_eff internal | R1 internal | Omega0 if direct | Omega0 if omega_gap=Lambda_eff |
|---:|---:|---:|---:|---:|
{rows}

## What Remains

The open physical source objects are:

```text
alpha_phys or equivalent physical inverse-length/action unit
C_Q
epsilon_adm
chi_omega
selected finite-resolution branch N, if N is used
```

Theta `5 TeV`, observed Newton/Planck values, cosmological scales, and particle
masses are still forbidden as no-knob inputs.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
