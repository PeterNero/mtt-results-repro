from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_finite_resolution_branch_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    closed = cert["closed_inputs"]
    branch = cert["finite_resolution_branch"]
    tolerance = cert["quotient_cell_tolerance"]
    formula = cert["conditional_omega0_formula"]
    comparisons = cert["branch_comparison"]
    guards = cert["guardrails"]
    still_open = cert["still_open"]

    require(
        cert["status"] == "Z448_BRANCH_SELECTED_EPSILON_RULE_CONDITIONAL_CQ_ALPHA_CHI_OPEN",
        "unexpected finite-resolution branch status",
    )
    require(all(closed.values()), "all imported q79 branch inputs must be closed/available")
    require(branch["selected_N"] == 448, "selected finite branch must be N=448")
    require(branch["q64"] == 15 and branch["q7"] == 2, "q64/q7 imports changed")
    require(branch["q_mod_448"] == 79, "q mod 448 import changed")
    require("Z64 x Z7 ~= Z448" in branch["selected_finite_quotient"], "selected quotient changed")

    require(comparisons["N64"]["status"].startswith("REJECTED"), "N64 should not be full branch")
    require(comparisons["N79"]["status"] == "REJECTED_AS_QUOTIENT_SIZE", "N79 role changed")
    require(comparisons["N448"]["status"] == "SELECTED_AS_CP_QUOTIENT_BRANCH", "N448 should be selected")

    require(abs(tolerance["epsilon_adm_if_rule_accepted"] - 1 / 448) < 1e-15, "epsilon changed")
    require(
        tolerance["status"] == "CONDITIONAL_SELECTION_RULE_APPLIED_TO_SELECTED_CP_QUOTIENT",
        "tolerance rule should remain conditional",
    )
    require("log(448*C_Q)" in formula["general_with_selected_epsilon"], "general Omega0 formula changed")
    require(abs(formula["C_Q_equals_1_Lambda_eff_over_sqrt_alpha"] - 1.5675093859261626) < 1e-15, "Lambda_eff changed")
    require(abs(formula["C_Q_equals_1_R1_sigma1"] - 0.6379547127299338) < 1e-15, "R1 changed")

    require(guards["uses_observed_Newton_or_Planck_input"] is False, "must not use observed G/Planck input")
    require(guards["uses_observed_Omega0_input"] is False, "must not use observed Omega0")
    require(guards["chooses_N_by_numerical_fit"] is False, "must not fit N")
    require(guards["claims_Z448_is_full_topology"] is False, "must not claim full topology is Z448")
    require(guards["claims_Z448_is_fundamental_cardinality"] is False, "must not claim fundamental cardinality")
    require(guards["claims_CQ_equals_1_is_physically_sharp"] is False, "must not close C_Q")
    require(guards["claims_quotient_cell_rule_derived"] is False, "must not overclaim tolerance rule")
    require(guards["claims_physical_Omega0_closed"] is False, "must not claim Omega0 closure")

    require(still_open["quotient_cell_tolerance_rule_derived_from_selected_functional"] is False, "tolerance rule gate should remain open")
    require(still_open["C_Q_sharp_physical_semigroup_bound"] is False, "C_Q gate should remain open")
    require(still_open["alpha_phys_or_action_unit_selected"] is False, "alpha gate should remain open")
    require(still_open["chi_omega_convention_selected"] is False, "chi gate should remain open")

    require("N = |Gamma_CP| = 448" in note, "note must state selected branch")
    require("does not say that the full topology is exactly `Z448`" in note, "note must include topology guardrail")
    print("AUDIT_PASS: selected finite resolution branch is Z448; tolerance rule, C_Q, alpha, and chi remain open")


if __name__ == "__main__":
    main()
