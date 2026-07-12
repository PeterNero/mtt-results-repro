from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_character_channel_covariance_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    imported = cert["imported_closures"]
    data = cert["internal_selected_data"]
    still_open = cert["still_open"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "INTERNAL_CHARACTER_CHANNEL_QTAU_AND_CUV_IMPORTED_OMEGA0_OPEN",
        "unexpected character-channel import status",
    )
    require(all(imported.values()), "all selected character-channel imports must be closed")
    require(data["selected_character"] == "q_64=15", "wrong selected character")
    require(data["D_raw_norm_squared_d_Q"] == 1.0, "d_Q must be one on selected character channel")
    require(data["G_11"] == 1.0, "G_11 must be one")
    require(abs(data["R_star"] - 4.440528182269818) < 1e-15, "R_star changed")
    require(abs(data["C_UV_norm_internal"] - 0.405623467693425) < 1e-15, "C_UV internal norm changed")
    require(abs(data["rho_UV"] - 0.164530397543639) < 1e-15, "rho_UV changed")
    require(abs(data["s_star"] - 1.464646774701829) < 1e-15, "s_star changed")

    require(still_open["physical_Omega_0_selected"] is False, "Omega_0 should remain open")
    require(still_open["physical_omega_gap_selected"] is False, "physical omega should remain open")
    require(still_open["physical_Newton_or_Planck_predicted"] is False, "Newton/Planck should remain open")
    require(still_open["unconditional_all_covariance_models_closed"] is False, "must not claim all covariance models")
    require(
        still_open["independent_higher_order_functional_evaluation_supplied_here"] is False,
        "must not claim independent functional evaluation",
    )

    require(guards["uses_unit_covariance_shortcut"] is False, "must not use shortcut")
    require(guards["uses_rank_one_selected_character_projector"] is True, "must use character projector")
    require(guards["imports_threshold_delta_as_covariance"] is False, "must not import threshold delta")
    require(guards["uses_observed_target_constant"] is False, "must not use observed target")
    require(guards["claims_unconditional_covariance_model"] is False, "must not overclaim covariance")
    require(guards["claims_physical_units"] is False, "must not claim physical units")

    require("Omega_0" in note, "note must identify Omega_0")
    require("conditional" in note.lower(), "note must retain conditional caveat")
    print("AUDIT_PASS: selected character-channel covariance import closes internal Q_tau/C_UV and leaves Omega_0 open")


if __name__ == "__main__":
    main()
