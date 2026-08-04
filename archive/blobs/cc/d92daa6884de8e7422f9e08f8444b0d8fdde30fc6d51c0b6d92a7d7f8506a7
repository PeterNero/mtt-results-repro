from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"

PREV_CERT = ROOT / "certificates" / "selected_admissibility_tolerance_and_semigroup_bound_theorem_certificate.json"
SHARED_LEDGER = Q79 / "certificates" / "shared_knob_cross_encoding_ledger_certificate.json"
Z64_CERT = Q79 / "certificates" / "z64_exact_branch_certificate.json"
Z7_CERT = Q79 / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json"
QUOTIENT_NOTE = Q79 / "proof_corpus" / "Ambient_to_Selected_Z448_CP_Quotient_Map_v1.md"
TERMINAL_NOTE = Q79 / "proof_corpus" / "Terminal_Closure_Certificate_and_Remaining_Proof_Obligations_v1.md"

OUT_CERT = ROOT / "certificates" / "selected_finite_resolution_branch_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Finite_Resolution_Branch_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def get_shared_knob(ledger: dict, knob_id: str) -> dict:
    for knob in ledger["shared_knobs"]:
        if knob["id"] == knob_id:
            return knob
    raise KeyError(knob_id)


def main() -> None:
    prev = load(PREV_CERT)
    ledger = load(SHARED_LEDGER)
    z64 = load(Z64_CERT)
    z7 = load(Z7_CERT)

    q79_knob = get_shared_knob(ledger, "q79_cp_character")
    z64_knob = get_shared_knob(ledger, "z64_exact_central_circle_carrier")
    z7_knob = get_shared_knob(ledger, "z7_mukai_fuyau_charge_block")

    selected_n = 448
    epsilon = 1.0 / selected_n
    log_ratio_cq1 = math.log(selected_n)
    lambda_eff_cq1 = math.sqrt(15.0 / log_ratio_cq1)
    r1_cq1 = 1.0 / lambda_eff_cq1
    s_star = 1.464646774701829
    omega_gap_factor_cq1 = lambda_eff_cq1 / s_star
    lambda_gap_factor_cq1 = math.sqrt(15.0) * omega_gap_factor_cq1

    closed_inputs = {
        "previous_CQ_epsilon_gate_reduced_to_finite_candidates": prev["status"]
        == "CQ_EPSILON_REDUCED_TO_FINITE_RESOLUTION_CANDIDATES_UNIQUE_SELECTION_OPEN",
        "q79_shared_character_closed": q79_knob["status"] == "CLOSED",
        "q79_quotient_is_Z64_x_Z7_equiv_Z448": q79_knob["selected_data"]["quotient"] == "Z64 x Z7 ~= Z448",
        "z64_exact_branch_closed": z64["status"] == "CLOSED_EXACT_CENTRAL_CIRCLE_BRANCH",
        "z7_charge_sector_closed": z7["status"] == "CLOSED_CHARGE_SECTOR",
        "z64_q64_matches": z64["conclusion"]["q_64"] == 15,
        "z7_q7_matches": z7["conclusion"]["q_7"] == 2,
        "crt_q_mod_448_matches": z64["conclusion"]["q_mod_448"] == z7["conclusion"]["q_mod_448"] == 79,
        "ambient_to_selected_quotient_note_exists": QUOTIENT_NOTE.exists(),
        "terminal_exact_charge_note_exists": TERMINAL_NOTE.exists(),
    }

    branch_comparison = {
        "N64": {
            "status": "REJECTED_AS_FULL_SELECTED_FINITE_RESOLUTION_BRANCH",
            "reason": "closed exact dyadic carrier but omits the selected Z7 Fu-Yau/Mukai charge factor",
        },
        "N79": {
            "status": "REJECTED_AS_QUOTIENT_SIZE",
            "reason": "79 is the selected CP character label q mod 448, not the order of the selected quotient",
        },
        "N448": {
            "status": "SELECTED_AS_CP_QUOTIENT_BRANCH",
            "reason": "closed q79 shared knob selects Gamma_CP ~= Z64 x Z7 ~= Z448 from q64=15 and q7=2",
        },
    }

    finite_resolution_branch = {
        "selected_N": selected_n,
        "selected_finite_quotient": "Gamma_CP ~= Z64 x Z7 ~= Z448",
        "q64": 15,
        "q7": 2,
        "q_mod_448": 79,
        "ambient_family_topology_allowed": "Z1344 with Z3 family kernel",
        "selected_observable_quotient_map": "pi: Z1344 -> Z448, pi(x)=x mod 448",
        "not_claimed": [
            "the full flavor topology is exactly Z448",
            "448 is a fundamental universe cardinality",
            "physical Omega0 is predicted",
        ],
    }

    quotient_cell_tolerance = {
        "rule": "epsilon_adm = 1 / |Gamma_CP|",
        "status": "CONDITIONAL_SELECTION_RULE_APPLIED_TO_SELECTED_CP_QUOTIENT",
        "epsilon_adm_if_rule_accepted": epsilon,
        "source": "selected finite CP quotient from q79 exact-charge branch",
        "remaining_rigor_gate": (
            "derive or axiomatize the quotient-cell admissibility rule from the "
            "retarded overlap/basin-separation functional rather than using it as a policy"
        ),
    }

    conditional_omega0 = {
        "general_with_selected_epsilon": "Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448*C_Q))",
        "if_CQ_equals_1": "Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448))",
        "C_Q_equals_1_internal_log_ratio": log_ratio_cq1,
        "C_Q_equals_1_Lambda_eff_over_sqrt_alpha": lambda_eff_cq1,
        "C_Q_equals_1_R1_sigma1": r1_cq1,
        "omega_gap_phys_factor_if_alpha_chi_one": omega_gap_factor_cq1,
        "Lambda_gap_phys_factor_if_alpha_chi_one": lambda_gap_factor_cq1,
    }

    guardrails = {
        "uses_observed_Newton_or_Planck_input": False,
        "uses_observed_Omega0_input": False,
        "chooses_N_by_numerical_fit": False,
        "claims_Z448_is_full_topology": False,
        "claims_Z448_is_fundamental_cardinality": False,
        "claims_CQ_equals_1_is_physically_sharp": False,
        "claims_quotient_cell_rule_derived": False,
        "claims_physical_Omega0_closed": False,
    }

    still_open = {
        "quotient_cell_tolerance_rule_derived_from_selected_functional": False,
        "C_Q_sharp_physical_semigroup_bound": False,
        "alpha_phys_or_action_unit_selected": False,
        "chi_omega_convention_selected": False,
        "physical_Omega0_closed": False,
    }

    ready = all(closed_inputs.values())
    status = (
        "Z448_BRANCH_SELECTED_EPSILON_RULE_CONDITIONAL_CQ_ALPHA_CHI_OPEN"
        if ready
        else "SELECTED_FINITE_RESOLUTION_BRANCH_INPUTS_NOT_READY"
    )

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_finite_resolution_branch_theorem",
        "status": status,
        "input_certificates": {
            "previous_CQ_epsilon_gate": str(PREV_CERT),
            "shared_knob_cross_encoding_ledger": str(SHARED_LEDGER),
            "z64_exact_branch": str(Z64_CERT),
            "z7_fuyau_mukai_charge_sector": str(Z7_CERT),
        },
        "source_notes": {
            "ambient_to_selected_z448_cp_quotient_map": str(QUOTIENT_NOTE),
            "terminal_closure_exact_charge_branch": str(TERMINAL_NOTE),
        },
        "closed_inputs": closed_inputs,
        "imported_shared_knobs": {
            "q79_cp_character": q79_knob["selected_data"],
            "z64_exact_central_circle_carrier": z64_knob["selected_data"],
            "z7_mukai_fuyau_charge_block": z7_knob["selected_data"],
        },
        "branch_comparison": branch_comparison,
        "finite_resolution_branch": finite_resolution_branch,
        "quotient_cell_tolerance": quotient_cell_tolerance,
        "conditional_omega0_formula": conditional_omega0,
        "guardrails": guardrails,
        "still_open": still_open,
        "theorem": {
            "name": "Selected_Finite_Resolution_Branch_Theorem.v1",
            "status": "FINITE_BRANCH_SELECTED_TOLERANCE_RULE_CONDITIONAL",
            "statement": (
                "For any Omega0 route that uses the selected CP quotient as the finite "
                "admissibility resolution, the source-certified branch is N=448 because "
                "the q79 exact-charge proof selects Gamma_CP ~= Z64 x Z7 ~= Z448. "
                "This closes the N-selection part of the finite-resolution candidate "
                "family. It does not claim that the full topology is Z448, that 448 is "
                "fundamental, that C_Q=1 is physically sharp, or that Omega0 is already "
                "predicted."
            ),
        },
        "next_required_artifacts": [
            "Quotient_Cell_Admissibility_Rule_Theorem_v1",
            "Selected_Sharp_Semigroup_Bound_Theorem_v1",
            "Selected_Physical_Alpha_or_Action_Unit_Theorem_v1",
            "Selected_Omega_Convention_Theorem_v1",
        ],
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected Finite Resolution Branch Theorem v1

## Result

The finite-resolution branch is no longer symmetric among `N=64`, `N=79`, and
`N=448` once the q79 exact-charge proof is imported.

The selected finite CP quotient is:

```text
Gamma_CP ~= Z64 x Z7 ~= Z448
q64 = 15
q7 = 2
q = 79 mod 448
```

Therefore the finite quotient branch selected by the existing MTT/q79 corpus is:

```text
N = |Gamma_CP| = 448
```

## Why the other candidates no longer serve as the selected branch

```text
N=64   closed dyadic carrier, but it omits the selected Z7 charge factor
N=79   selected CP label q mod 448, not a quotient size
N=448  selected CP quotient Z64 x Z7 ~= Z448
```

## Guardrail

This does not say that the full topology is exactly `Z448`. The q79 corpus
already separates the ambient family carrier from the selected observable
quotient:

```text
pi: Z1344 -> Z448
ker(pi) = Z3-family
```

So the rigorous statement is:

```text
MTT selects a family-trivial CP character factoring through Z448.
```

## Consequence for Omega0

If the one-cell quotient tolerance rule is accepted,

```text
epsilon_adm = 1/|Gamma_CP|,
```

then the selected tolerance is:

```text
epsilon_adm = 1/448 = {epsilon:.15g}.
```

The remaining formula becomes:

```text
Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448*C_Q)).
```

If the later sharp-semigroup theorem proves `C_Q=1`, this specializes to:

```text
Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448))
sqrt(15/log(448)) = {lambda_eff_cq1:.15g}
R1(sigma=1) = {r1_cq1:.15g}
```

## Still Open

This theorem closes the source-certified finite branch, not the whole physical
normalization. Remaining gates:

```text
derive the quotient-cell admissibility rule from the selected functional
prove whether C_Q=1 is the sharp physical semigroup bound
select alpha_phys or an equivalent action/unit anchor
select chi_omega
```
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
