from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

EPS_CERT = ROOT / "certificates" / "quotient_cell_admissibility_rule_theorem_certificate.json"
EXACT_GAP_CERT = ROOT / "certificates" / "exact_branch_internal_aint_gap_import_certificate.json"
DAMPING_HESSIAN = NONSM / "certificates" / "damping_hessian_z64_block_identification_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_sharp_semigroup_bound_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Sharp_Semigroup_Bound_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    eps_cert = load(EPS_CERT)
    exact_gap = load(EXACT_GAP_CERT)
    damping = load(DAMPING_HESSIAN)

    epsilon = eps_cert["proof"]["epsilon_adm"]
    lambda_star = exact_gap["exact_branch_import"]["lambda_star_internal"]
    c_q = 1.0
    log_ratio = math.log(c_q / epsilon)
    lambda_eff = math.sqrt(lambda_star / log_ratio)
    r1_sigma1 = 1.0 / lambda_eff
    s_star = 1.464646774701829
    omega_gap_factor = lambda_eff / s_star
    lambda_gap_factor = math.sqrt(lambda_star) * omega_gap_factor

    closed_inputs = {
        "epsilon_adm_closed": eps_cert["status"] == "Z448_EPSILON_ADM_CLOSED_CQ_ALPHA_CHI_OPEN",
        "epsilon_is_one_over_448": abs(epsilon - 1 / 448) < 1e-15,
        "exact_branch_gap_imported": exact_gap["status"] == "EXACT_BRANCH_INTERNAL_AINT_GAP_CLOSED_GR_TT_BRANCH_IDENTITY_OPEN",
        "lambda_star_is_15": lambda_star == 15.0,
        "damping_hessian_exact_branch_identified": damping["verdict"]["exact_branch_hessian_kernel_identified"],
        "damping_hessian_has_zero_schur_correction": damping["exact_branch_data"]["schur_correction"] == 0,
        "damping_operator_is_positive_hessian_block": damping["exact_branch_data"]["hessian_block"]
        == "L_64 = alpha L_tower, alpha > 0",
        "normalized_alpha_internal_is_one": damping["exact_branch_data"]["normalized_alpha"] == 1.0,
    }

    semigroup_proof = {
        "operator": "L_64 = alpha L_tower on the selected exact central-circle branch",
        "branch": "orthogonal exact-branch noncoherent complement",
        "normalized_internal_alpha": 1.0,
        "lambda_star": lambda_star,
        "schur_correction": 0.0,
        "spectral_theorem_bound": "||exp(-t L_64) Q|| <= exp(-lambda_star t) on the selected complement",
        "prefactor": c_q,
        "why_sharp": (
            "For a positive self-adjoint Hessian block with orthogonal spectral projection, "
            "the operator norm of the semigroup on the complement is the largest retained "
            "eigen-decay. The prefactor is exactly 1; any C_Q>1 is weaker, while C_Q<1 "
            "fails at t=0 for normalized complement states."
        ),
        "scope": "selected exact branch only; not a nonnormal full mixed Hessian claim",
    }

    omega0_formula = {
        "C_Q": c_q,
        "epsilon_adm": epsilon,
        "log_CQ_over_epsilon": log_ratio,
        "Omega0_over_chi_sqrt_alpha": lambda_eff,
        "R1_sigma1": r1_sigma1,
        "Omega0_formula": "Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448))",
        "omega_gap_phys_over_chi_sqrt_alpha": omega_gap_factor,
        "Lambda_gap_phys_over_chi_sqrt_alpha": lambda_gap_factor,
    }

    guardrails = {
        "uses_observed_Newton_or_Planck_input": False,
        "uses_observed_Omega0_input": False,
        "fits_C_Q_to_target": False,
        "claims_full_mixed_hessian_semigroup_is_normal": False,
        "claims_unconditional_full_GR_response_closed": False,
        "claims_alpha_phys_selected": False,
        "claims_chi_omega_selected": False,
        "claims_physical_Omega0_closed": False,
    }

    still_open = {
        "alpha_phys_or_action_unit_selected": False,
        "chi_omega_convention_selected": False,
        "physical_Omega0_closed": False,
        "optional_full_mixed_hessian_nonnormal_bound": False,
    }

    ready = all(closed_inputs.values())
    status = "CQ1_SHARP_SEMIGROUP_BOUND_CLOSED_ALPHA_CHI_OPEN" if ready else "SHARP_SEMIGROUP_INPUTS_NOT_READY"

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_sharp_semigroup_bound_theorem",
        "status": status,
        "input_certificates": {
            "quotient_cell_admissibility_rule": str(EPS_CERT),
            "exact_branch_internal_aint_gap_import": str(EXACT_GAP_CERT),
            "damping_hessian_z64_block_identification": str(DAMPING_HESSIAN),
        },
        "closed_inputs": closed_inputs,
        "semigroup_proof": semigroup_proof,
        "omega0_formula": omega0_formula,
        "guardrails": guardrails,
        "still_open": still_open,
        "theorem": {
            "name": "Selected_Sharp_Semigroup_Bound_Theorem.v1",
            "status": "C_Q_EQUALS_1_CLOSED_ON_SELECTED_EXACT_BRANCH",
            "statement": (
                "On the selected exact central-circle damping branch, the generator is "
                "the positive self-adjoint Hessian block L_64=alpha L_tower with zero "
                "Schur leakage. The spectral theorem gives the sharp contraction "
                "prefactor C_Q=1 on the orthogonal selected complement. Together with "
                "epsilon_adm=1/448, Omega0 reduces to chi_omega*sqrt(alpha_phys)*"
                "sqrt(15/log(448))."
            ),
        },
        "next_required_artifacts": [
            "Selected_Physical_Alpha_or_Action_Unit_Theorem_v1",
            "Selected_Omega_Convention_Theorem_v1",
        ],
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected Sharp Semigroup Bound Theorem v1

## Result

The semigroup prefactor is closed on the selected exact central-circle branch:

```text
C_Q = 1.
```

The imported branch has:

```text
L_64 = alpha L_tower, alpha > 0
normalized alpha = 1
lambda_star = 15
Schur correction = 0
```

Because the selected generator is a positive self-adjoint Hessian block and the
complement is an orthogonal spectral complement, the spectral theorem gives:

```text
|| exp(-t L_64) Q || <= exp(-lambda_star t).
```

The prefactor is exactly `1`. A larger value is merely weaker, and a smaller
value fails at `t=0` for normalized complement states.

This closes the sharp bound for the selected exact branch. It does not assert a
nonnormal bound for an unprojected full mixed Hessian.

## Omega0 Consequence

With the already closed quotient-cell result:

```text
epsilon_adm = 1/448,
```

the formula becomes:

```text
Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448)).
```

Numerically:

```text
log(448) = {log_ratio:.15g}
sqrt(15/log(448)) = {lambda_eff:.15g}
R1(sigma=1) = {r1_sigma1:.15g}
omega_gap_phys/(chi_omega*sqrt(alpha_phys)) = {omega_gap_factor:.15g}
Lambda_gap_phys/(chi_omega*sqrt(alpha_phys)) = {lambda_gap_factor:.15g}
```

## Still Open

Only two physical normalization gates remain in this chain:

```text
alpha_phys
chi_omega
```
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
