from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "one_anchor_gr_normalization_propagation_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    solution = cert["solution"]
    length = solution["length_anchor_family"]
    energy = solution["energy_anchor_family"]
    inv = solution["dimensionless_invariants"]
    verdict = cert["verdict"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "ONE_ANCHOR_GR_NORMALIZATION_FAMILY_CLOSED_ABSOLUTE_VALUE_OPEN",
        "unexpected one-anchor GR status",
    )
    require(all(cert["closed_inputs"].values()), "all one-anchor inputs must be closed")
    require(packet["selected_internal_row"]["N"] == 448, "must use selected Z448 row")
    require(verdict["one_anchor_gr_normalization_family_closed"] is True, "one-anchor family must close")
    require(verdict["absolute_newton_value_predicted_without_anchor"] is False, "must not predict Newton without anchor")
    require(verdict["new_gr_knob_introduced"] is False, "must not add GR knob")

    require(abs(packet["selected_internal_row"]["tau_int"] - 0.40698621549433234) < 1e-15, "tau changed")
    require(abs(packet["selected_internal_row"]["G_eff_int"] - 0.12111650495392737) < 1e-15, "G int changed")
    require(abs(packet["selected_internal_row"]["kappa_STF_int"] - 0.08212905373241541) < 1e-15, "kappa int changed")
    require(abs(length["G_eff_over_L0_squared"] - 0.29759362932431804) < 1e-15, "length G coefficient changed")
    require(abs(length["kappa_STF_times_L0_squared"] - 0.03342539276068642) < 1e-15, "length kappa coefficient changed")
    require(abs(energy["G_eff_times_E0_squared"] - 0.29759362932431804) < 1e-15, "energy G coefficient changed")
    require(abs(energy["kappa_STF_over_E0_squared"] - 0.03342539276068642) < 1e-15, "energy kappa coefficient changed")
    require(abs(inv["G_eff_phys_times_kappa_STF_phys"] - inv["G_eff_phys_times_kappa_STF_phys_target"]) < 1e-15, "G*kappa invariant mismatch")

    require("G_eff = 0.297593629324318 * L0^2" in note, "note must include length-anchor G formula")
    require("kappa_STF = 0.0334253927606864 / L0^2" in note, "note must include length-anchor kappa formula")
    require("G_eff = 0.297593629324318 / E0^2" in note, "note must include energy-anchor G formula")
    require("kappa_STF = 0.0334253927606864 * E0^2" in note, "note must include energy-anchor kappa formula")

    require(guards["claims_measured_Newton_constant"] is False, "must not claim measured Newton")
    require(guards["claims_measured_Planck_scale"] is False, "must not claim Planck")
    require(guards["uses_observed_Newton_or_Planck_input"] is False, "must not use Newton/Planck input")
    require(guards["uses_observed_cosmology_or_masses"] is False, "must not use observed targets")
    require(guards["uses_Theta_5TeV_as_prediction"] is False, "must not use 5 TeV")
    require(guards["adds_new_GR_parameter"] is False, "must not add GR parameter")

    print("AUDIT_PASS: one-anchor GR normalization family closed; absolute Newton value remains anchor-open")


if __name__ == "__main__":
    main()
