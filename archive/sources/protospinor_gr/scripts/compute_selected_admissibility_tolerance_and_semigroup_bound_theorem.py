from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"
Q79 = ROOT.parent / "mtt-q79-proof-repro"

OMEGA0 = ROOT / "certificates" / "selected_physical_omega0_source_theorem_certificate.json"
DAMPING_BRANCH = NONSM / "certificates" / "selected_damping_normalization_branch_certificate.json"
CENTRAL_LEMMA = NONSM / "certificates" / "selected_central_circle_damping_identification_lemma_certificate.json"
DAMPING_HESSIAN = NONSM / "certificates" / "damping_hessian_z64_block_identification_certificate.json"
PRIMITIVE_POLICY = NONSM / "certificates" / "primitive_constant_discipline_certificate.json"
EXPLORATORY = NONSM / "certificates" / "exploratory_absolute_normalization_solution_certificate.json"
SHARED_LEDGER = Q79 / "certificates" / "shared_knob_cross_encoding_ledger_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_admissibility_tolerance_and_semigroup_bound_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Admissibility_Tolerance_and_Semigroup_Bound_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def finite_row(n: int) -> dict:
    eps = 1.0 / n
    log_ratio = math.log(n)
    lambda_eff = math.sqrt(15.0 / log_ratio)
    return {
        "N": n,
        "C_Q_candidate": 1.0,
        "epsilon_adm_candidate": eps,
        "log_CQ_over_epsilon": log_ratio,
        "Lambda_eff_internal_alpha_1": lambda_eff,
        "R1_internal_sigma_1": 1.0 / lambda_eff,
        "passes_R1_le_2": (1.0 / lambda_eff) <= 2.0,
    }


def main() -> None:
    omega0 = load(OMEGA0)
    damping_branch = load(DAMPING_BRANCH)
    central_lemma = load(CENTRAL_LEMMA)
    damping_hessian = load(DAMPING_HESSIAN)
    primitive_policy = load(PRIMITIVE_POLICY)
    exploratory = load(EXPLORATORY)
    shared_ledger = load(SHARED_LEDGER)

    closed_inputs = {
        "omega0_reduced_to_CQ_epsilon_gate": omega0["status"]
        == "OMEGA0_REDUCED_TO_PHYSICAL_ALPHA_CQ_EPSILON_AND_CHI",
        "damping_branch_schema_available": damping_branch["verdict"]["branch_finished_as_reduction"],
        "central_circle_lemma_passes_with_finite_candidates": central_lemma["verdict"][
            "lemma_closed_under_z64_tower_identification"
        ],
        "damping_hessian_exact_branch_identified": damping_hessian["verdict"][
            "exact_branch_hessian_kernel_identified"
        ],
        "primitive_policy_allows_coherence_data_in_principle": primitive_policy["verdict"][
            "primitive_constants_allowed_in_principle"
        ],
        "exploratory_schema_found": exploratory["verdict"]["solution_schema_found"],
        "shared_q79_ledger_available": shared_ledger["verdict"]["closes_cross_encoding_dictionary"],
    }

    finite_candidates = [finite_row(64), finite_row(79), finite_row(448)]

    source_classification = {
        "C_Q_equals_1": {
            "classification": "NORMALIZED_CONTRACTION_CANDIDATE_NOT_PHYSICAL_SOURCE_CERTIFIED",
            "role": "unit semigroup constant in the exact branch damping sanity model",
            "current_status": (
                "used in existing finite-resolution examples; not proven as the unique "
                "physical-branch semigroup bound"
            ),
        },
        "epsilon_adm_equals_1_over_N": {
            "classification": "FINITE_RESOLUTION_CANDIDATE_NOT_UNIQUE_PHYSICAL_SELECTION",
            "role": "one-cell tolerance for an N-state/effective finite quotient resolution",
            "current_status": (
                "executable for N=64,79,448; current sources do not prove which N is the "
                "physical Omega0 branch"
            ),
        },
        "N_64": {
            "classification": "EXACT_DYADIC_Z64_BRANCH",
            "current_status": "closed exact central-circle carrier, but omits the Z7/q79 companion",
        },
        "N_79": {
            "classification": "SELECTED_Q79_LABEL_SCAFFOLD",
            "current_status": "appears in selected q79/no-knob scaffolds; not a finite quotient size proof for Omega0",
        },
        "N_448": {
            "classification": "Z64_X_Z7_COMBINED_QUOTIENT_CANDIDATE",
            "current_status": "natural combined quotient Z448; q79 corpus warns compact finite N=448 is not asserted fundamental",
        },
    }

    branch_selection_tests = {
        "all_candidates_pass_R1_le_2_internal": all(row["passes_R1_le_2"] for row in finite_candidates),
        "N64_is_exact_dyadic_carrier": True,
        "N79_is_selected_label_not_quotient_size": True,
        "N448_is_combined_quotient_candidate": True,
        "unique_N_for_physical_Omega0_selected": False,
    }

    still_open = {
        "C_Q_unique_physical_branch_value_sourced": False,
        "epsilon_adm_unique_physical_branch_value_sourced": False,
        "finite_resolution_N_for_Omega0_selected": False,
        "basin_separation_derivation_of_epsilon_adm": False,
        "sharp_semigroup_bound_derivation_of_C_Q": False,
        "physical_Omega0_closed": False,
    }

    guardrails = {
        "chooses_N_by_target_fit": False,
        "chooses_epsilon_from_Newton_or_Planck": False,
        "treats_internal_candidates_as_physical_prediction": False,
        "claims_C_Q_equals_1_physical": False,
        "claims_unique_N_selected": False,
        "claims_physical_Omega0": False,
    }

    ready = all(closed_inputs.values())
    status = (
        "CQ_EPSILON_REDUCED_TO_FINITE_RESOLUTION_CANDIDATES_UNIQUE_SELECTION_OPEN"
        if ready
        else "CQ_EPSILON_THEOREM_INPUTS_NOT_READY"
    )

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_admissibility_tolerance_and_semigroup_bound_theorem",
        "status": status,
        "input_certificates": {
            "selected_physical_omega0_source_theorem": str(OMEGA0),
            "selected_damping_normalization_branch": str(DAMPING_BRANCH),
            "selected_central_circle_damping_identification_lemma": str(CENTRAL_LEMMA),
            "damping_hessian_z64_block_identification": str(DAMPING_HESSIAN),
            "primitive_constant_discipline": str(PRIMITIVE_POLICY),
            "exploratory_absolute_normalization_solution": str(EXPLORATORY),
            "shared_knob_cross_encoding_ledger": str(SHARED_LEDGER),
        },
        "closed_inputs": closed_inputs,
        "source_classification": source_classification,
        "finite_resolution_candidates_internal_only": finite_candidates,
        "branch_selection_tests": branch_selection_tests,
        "still_open": still_open,
        "guardrails": guardrails,
        "theorem": {
            "name": "Selected_Admissibility_Tolerance_and_Semigroup_Bound_Theorem.v1",
            "status": "FINITE_CANDIDATES_COMPUTED_UNIQUE_PHYSICAL_SELECTION_OPEN",
            "statement": (
                "The admissibility/semigroup part of Omega_0 is reduced to finite "
                "candidate data. The current verified corpus supports the internal "
                "candidate family C_Q=1 and epsilon_adm=1/N for N in {64,79,448}; "
                "all three pass the central-circle R1<=2 test when lambda_star=15. "
                "However, the corpus does not yet source C_Q=1 as the unique physical "
                "semigroup bound, epsilon_adm=1/N as the unique physical tolerance, "
                "or a unique N for the Omega_0 branch."
            ),
            "conditional_closure": (
                "If a source theorem selects C_Q and epsilon_adm, or selects one N with "
                "C_Q=1 and epsilon_adm=1/N, then the remaining Omega_0 formula loses "
                "the C_Q/epsilon gate and depends only on alpha_phys and chi_omega."
            ),
        },
        "next_required_artifacts": [
            "Selected_Finite_Resolution_Branch_Theorem_v1",
            "Selected_Sharp_Semigroup_Bound_Theorem_v1",
            "Selected_Basin_Separation_Tolerance_Theorem_v1",
        ],
        "note_written": str(OUT_NOTE),
    }

    rows = "\n".join(
        f"| {row['N']} | {row['epsilon_adm_candidate']:.15g} | "
        f"{row['log_CQ_over_epsilon']:.15g} | "
        f"{row['Lambda_eff_internal_alpha_1']:.15g} | "
        f"{row['R1_internal_sigma_1']:.15g} |"
        for row in finite_candidates
    )

    note = f"""# Selected Admissibility Tolerance and Semigroup Bound Theorem v1

## Result

The `C_Q` and `epsilon_adm` gate is reduced to finite internal candidates, but
not yet to a unique physical branch.

Current executable candidate family:

```text
C_Q = 1
epsilon_adm = 1/N
N in {{64, 79, 448}}
```

With `lambda_star=15` and normalized internal alpha:

| N | epsilon_adm | log(C_Q/epsilon_adm) | Lambda_eff internal | R1 internal |
|---:|---:|---:|---:|---:|
{rows}

All three candidates pass the internal `R1 <= 2` central-circle admissibility
test.

## Interpretation

This is progress, but not physical closure. The current sources support these
as finite-resolution candidates:

```text
N=64   exact dyadic Z64 carrier
N=79   selected q79 label scaffold
N=448  combined Z64 x Z7 quotient candidate
```

The corpus does not yet prove that one of these is the unique physical
`Omega_0` branch, nor that `C_Q=1` is the sharp physical semigroup bound.

## Remaining Gate

To close this part, we need one of:

```text
Selected_Finite_Resolution_Branch_Theorem
Selected_Sharp_Semigroup_Bound_Theorem
Selected_Basin_Separation_Tolerance_Theorem
```

No observed Newton, Planck, cosmological, TeV, or particle-mass value is used.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
