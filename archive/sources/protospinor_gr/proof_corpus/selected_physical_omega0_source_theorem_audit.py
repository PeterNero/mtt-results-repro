from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_physical_omega0_source_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    closed = cert["closed_inputs"]
    reduction = cert["source_reduction"]
    rows = cert["finite_resolution_candidates_internal_only"]
    still_open = cert["still_open"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "OMEGA0_REDUCED_TO_PHYSICAL_ALPHA_CQ_EPSILON_AND_CHI",
        "unexpected Omega0 theorem status",
    )
    require(all(closed.values()), "all source inputs should be closed/reduced")
    require(reduction["exact_branch_lambda_star"] == 15.0, "lambda star must be 15")
    require("sqrt(alpha_phys)" in reduction["Omega0_schema"], "Omega0 schema must expose physical alpha")
    require("chi_omega" in reduction["Omega0_schema"], "Omega0 schema must expose convention factor")
    require(len(rows) == 3, "expected three internal finite-resolution candidates")
    require([row["N"] for row in rows] == [64, 79, 448], "unexpected N candidates")
    require(abs(rows[1]["R1_internal_if_sigma_1"] - 0.5397189300902845) < 1e-15, "N=79 R1 changed")

    require(
        still_open["physical_alpha_or_equivalent_inverse_length_unit_selected"] is False,
        "physical alpha should remain open",
    )
    require(still_open["C_Q_source_certified_physical_branch_value"] is False, "C_Q should remain open")
    require(still_open["epsilon_adm_source_certified_physical_branch_value"] is False, "epsilon should remain open")
    require(still_open["chi_omega_convention_source_certified"] is False, "chi should remain open")
    require(still_open["unique_finite_resolution_N_selected_for_physical_omega0"] is False, "N selection should remain open")
    require(still_open["Omega0_physical_numeric_closed"] is False, "Omega0 should remain open")
    require(still_open["physical_Newton_or_Planck_predicted"] is False, "Newton/Planck should remain open")

    require(guards["uses_theta_5TeV_as_prediction"] is False, "must not use TeV calibration")
    require(guards["uses_observed_Newton_or_Planck"] is False, "must not use Newton/Planck")
    require(guards["treats_internal_alpha_1_as_physical_unit"] is False, "must not promote alpha=1")
    require(guards["claims_physical_Omega0"] is False, "must not claim physical Omega0")

    require("Omega_0 = chi_omega" in note, "note must include Omega0 schema")
    require("not physical predictions" in note, "note must label table internal-only")
    print("AUDIT_PASS: Omega0 reduced to physical alpha, C_Q, epsilon_adm, chi_omega, and branch selection")


if __name__ == "__main__":
    main()
