from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "quotient_cell_admissibility_rule_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    closed = cert["closed_inputs"]
    proof = cert["proof"]
    formula = cert["conditional_omega0_formula"]
    guards = cert["guardrails"]
    still_open = cert["still_open"]

    require(
        cert["status"] == "Z448_EPSILON_ADM_CLOSED_CQ_ALPHA_CHI_OPEN",
        "unexpected quotient-cell theorem status",
    )
    require(all(closed.values()), "all quotient-cell inputs must close")
    require(proof["cardinality"] == 448, "selected quotient cardinality changed")
    require(abs(proof["minimal_positive_unresolved_mass"] - 1 / 448) < 1e-15, "epsilon_adm changed")
    require(abs(formula["selected_epsilon_adm"] - 1 / 448) < 1e-15, "formula epsilon changed")
    require("log(448*C_Q)" in formula["with_selected_epsilon"], "selected epsilon formula changed")
    require(abs(formula["C_Q_equals_1_Lambda_eff_over_sqrt_alpha"] - 1.5675093859261626) < 1e-15, "Lambda_eff changed")
    require(abs(formula["C_Q_equals_1_R1_sigma1"] - 0.6379547127299338) < 1e-15, "R1 changed")

    require(guards["uses_observed_Newton_or_Planck_input"] is False, "must not use Newton/Planck input")
    require(guards["uses_observed_Omega0_input"] is False, "must not use observed Omega0")
    require(guards["chooses_epsilon_by_target_fit"] is False, "must not fit epsilon")
    require(guards["uses_nonuniform_measure_knob"] is False, "must not introduce measure knob")
    require(guards["claims_CQ_equals_1_is_physically_sharp"] is False, "must not close C_Q")
    require(guards["claims_alpha_phys_selected"] is False, "must not close alpha")
    require(guards["claims_chi_omega_selected"] is False, "must not close chi")
    require(guards["claims_physical_Omega0_closed"] is False, "must not claim physical Omega0")

    require(still_open["C_Q_sharp_physical_semigroup_bound"] is False, "C_Q gate should remain open")
    require(still_open["alpha_phys_or_action_unit_selected"] is False, "alpha gate should remain open")
    require(still_open["chi_omega_convention_selected"] is False, "chi gate should remain open")
    require(still_open["physical_Omega0_closed"] is False, "Omega0 should remain open")

    require("epsilon_adm = 1/448" in note, "note must state epsilon")
    require("not obtained from Newton's constant" in note, "note must include no-target-fit guardrail")
    print("AUDIT_PASS: epsilon_adm=1/448 follows from selected finite Haar cell scale; C_Q, alpha, chi remain open")


if __name__ == "__main__":
    main()
