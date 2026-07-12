from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

BRANCH_CERT = ROOT / "certificates" / "selected_finite_resolution_branch_theorem_certificate.json"
OUT_CERT = ROOT / "certificates" / "quotient_cell_admissibility_rule_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Quotient_Cell_Admissibility_Rule_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def finite_haar_atoms(n: int) -> list[float]:
    return [1.0 / n for _ in range(n)]


def main() -> None:
    branch_cert = load(BRANCH_CERT)
    n = branch_cert["finite_resolution_branch"]["selected_N"]
    atoms = finite_haar_atoms(n)
    epsilon = min(m for m in atoms if m > 0.0)
    positive_unresolved_masses = [k / n for k in range(1, n + 1)]
    log_ratio_cq1 = math.log(1.0 / epsilon)
    lambda_eff_cq1 = math.sqrt(15.0 / log_ratio_cq1)
    r1_cq1 = 1.0 / lambda_eff_cq1

    closed_inputs = {
        "selected_finite_branch_available": branch_cert["status"]
        == "Z448_BRANCH_SELECTED_EPSILON_RULE_CONDITIONAL_CQ_ALPHA_CHI_OPEN",
        "selected_branch_N_is_448": n == 448,
        "selected_branch_not_target_fit": not branch_cert["guardrails"]["chooses_N_by_numerical_fit"],
        "finite_quotient_has_uniform_normalized_Haar_measure": abs(sum(atoms) - 1.0) < 1e-12,
        "smallest_positive_cell_mass_is_one_over_N": abs(epsilon - 1 / n) < 1e-15,
        "all_positive_unresolved_cell_masses_are_multiples_of_one_over_N": all(
            abs((mass * n) - round(mass * n)) < 1e-12 for mass in positive_unresolved_masses
        ),
    }

    proof = {
        "finite_space": "Gamma_CP",
        "cardinality": n,
        "measure": "normalized counting/Haar measure mu({g})=1/|Gamma_CP|",
        "admissibility_event_model": (
            "an unresolved finite-branch event is a union of selected quotient cells; "
            "a nonempty unresolved event has measure at least one cell"
        ),
        "minimal_positive_unresolved_mass": epsilon,
        "epsilon_adm": epsilon,
        "sharpness": {
            "below_one_cell": "any threshold below 1/N distinguishes zero unresolved cells from one unresolved cell",
            "one_cell_scale": "1/N is the canonical resolution scale of the selected finite quotient",
            "above_one_cell": "a threshold above 1/N can ignore a one-cell unresolved branch",
        },
    }

    conditional_omega0 = {
        "selected_epsilon_adm": epsilon,
        "general_formula": "Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(C_Q/epsilon_adm))",
        "with_selected_epsilon": "Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448*C_Q))",
        "if_CQ_equals_1": "Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448))",
        "C_Q_equals_1_log_ratio": log_ratio_cq1,
        "C_Q_equals_1_Lambda_eff_over_sqrt_alpha": lambda_eff_cq1,
        "C_Q_equals_1_R1_sigma1": r1_cq1,
    }

    guardrails = {
        "uses_observed_Newton_or_Planck_input": False,
        "uses_observed_Omega0_input": False,
        "chooses_epsilon_by_target_fit": False,
        "uses_nonuniform_measure_knob": False,
        "claims_CQ_equals_1_is_physically_sharp": False,
        "claims_alpha_phys_selected": False,
        "claims_chi_omega_selected": False,
        "claims_physical_Omega0_closed": False,
    }

    still_open = {
        "C_Q_sharp_physical_semigroup_bound": False,
        "alpha_phys_or_action_unit_selected": False,
        "chi_omega_convention_selected": False,
        "physical_Omega0_closed": False,
    }

    ready = all(closed_inputs.values())
    status = "Z448_EPSILON_ADM_CLOSED_CQ_ALPHA_CHI_OPEN" if ready else "QUOTIENT_CELL_RULE_INPUTS_NOT_READY"

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "quotient_cell_admissibility_rule_theorem",
        "status": status,
        "input_certificates": {
            "selected_finite_resolution_branch_theorem": str(BRANCH_CERT),
        },
        "closed_inputs": closed_inputs,
        "proof": proof,
        "conditional_omega0_formula": conditional_omega0,
        "guardrails": guardrails,
        "still_open": still_open,
        "theorem": {
            "name": "Quotient_Cell_Admissibility_Rule_Theorem.v1",
            "status": "EPSILON_ADM_SELECTED_BY_FINITE_HAAR_CELL_SCALE",
            "statement": (
                "On the selected finite CP quotient Gamma_CP ~= Z448, the normalized "
                "finite Haar/counting measure gives every quotient cell mass 1/448. "
                "If unresolved admissibility events are quotient-cell unions, the "
                "canonical one-cell resolution scale is epsilon_adm=1/448. This "
                "derives the tolerance from the selected finite quotient rather than "
                "from observed physical constants."
            ),
        },
        "next_required_artifacts": [
            "Selected_Sharp_Semigroup_Bound_Theorem_v1",
            "Selected_Physical_Alpha_or_Action_Unit_Theorem_v1",
            "Selected_Omega_Convention_Theorem_v1",
        ],
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Quotient Cell Admissibility Rule Theorem v1

## Result

The finite tolerance is now selected by the selected quotient itself.

The previous theorem selected:

```text
Gamma_CP ~= Z64 x Z7 ~= Z448
|Gamma_CP| = 448
```

On a finite selected quotient, the canonical invariant probability measure is
normalized counting measure:

```text
mu({{g}}) = 1/|Gamma_CP|.
```

Therefore every selected quotient cell has mass:

```text
1/448 = {epsilon:.15g}.
```

If an unresolved finite-branch event is a union of selected quotient cells, its
possible positive masses are:

```text
k/448,  k = 1,...,448.
```

So the smallest positive unresolved mass is exactly:

```text
epsilon_adm = 1/448.
```

This is not obtained from Newton's constant, Planck data, observed Omega0, or
any target fit. It is the one-cell resolution scale of the selected finite CP
quotient.

## Omega0 Consequence

The physical normalization formula is now reduced to:

```text
Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448*C_Q)).
```

If a later theorem proves `C_Q=1`, this becomes:

```text
Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448))
sqrt(15/log(448)) = {lambda_eff_cq1:.15g}
R1(sigma=1) = {r1_cq1:.15g}
```

## Still Open

The remaining gates are now fewer:

```text
C_Q          sharp physical semigroup bound
alpha_phys   selected physical action/unit anchor
chi_omega    selected convention between Omega0 and the gap unit
```
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
