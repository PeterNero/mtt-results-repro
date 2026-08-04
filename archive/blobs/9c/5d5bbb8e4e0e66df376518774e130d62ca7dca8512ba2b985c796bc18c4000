from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_physical_omega_gap_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    structural = cert["structural_inputs"]
    open_inputs = cert["open_inputs"]
    formulae = cert["internal_formulae"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "OMEGA_GAP_THEOREM_REDUCED_TO_CUV_DELTA_AND_OMEGA0_SOURCE_DATA",
        "unexpected omega theorem status",
    )
    require(all(structural.values()), "all structural inputs must be ready")
    require(open_inputs["C_UV_source_certified"] is False, "C_UV should remain open")
    require(open_inputs["delta_source_certified"] is False, "delta should remain open")
    require(open_inputs["omega_gap_phys_selected"] is False, "omega_gap_phys should remain open")
    require(
        open_inputs["C_UV_squared_over_delta_physical_scale_certified"] is False,
        "C_UV^2/delta physical scale should remain open",
    )

    require(abs(formulae["rho_UV"] - 0.164530397543639) < 1e-15, "rho_UV changed")
    require(abs(formulae["lambda_internal_exact"] - 15.0) < 1e-15, "lambda changed")
    require(formulae["conditional_omega_relation"] == "Lambda_gap_phys = sqrt(15) * omega_gap_phys", "omega relation wrong")

    require(guards["claims_omega_gap_phys"] is False, "must not claim omega")
    require(guards["claims_physical_Newton_or_Planck"] is False, "must not claim Newton/Planck")
    require(guards["uses_theta_5TeV_as_prediction"] is False, "must not use 5 TeV")
    require(guards["uses_observed_target_backsolve"] is False, "must not backsolve")
    require(guards["treats_dimensionless_rho_as_physical_unit"] is False, "must not treat rho as physical unit")
    require(guards["adds_new_GR_parameter"] is False, "must not add GR parameter")

    require("Omega_0" in note, "note must identify Omega_0")
    require("C_UV" in note and "delta" in note, "note must identify coefficient gap")
    print("AUDIT_PASS: omega gap reduced to C_UV, delta, and Omega_0 source data")


if __name__ == "__main__":
    main()
