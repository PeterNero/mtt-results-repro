from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "one_anchor_einstein_response_assembly_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    kernel = cert["response_kernel"]
    assembly = cert["assembly"]
    open_gates = cert["open_gates"]
    verdict = cert["verdict"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "ONE_ANCHOR_EINSTEIN_RESPONSE_ASSEMBLED_CONDITIONAL_GATES_OPEN",
        "unexpected Einstein assembly status",
    )
    require(all(cert["closed_inputs"].values()), "all assembly inputs must be ready")
    require(verdict["one_anchor_einstein_response_assembled"] is True, "assembly should be true")
    require(verdict["conditional_low_energy_TT_response_closed"] is True, "conditional TT response should close")
    require(verdict["full_unconditional_physical_GR_closed"] is False, "full GR must remain open")
    require(verdict["new_GR_knob_introduced"] is False, "must not introduce GR knob")
    require(verdict["measured_Newton_or_Planck_predicted"] is False, "must not predict measured Newton/Planck")
    require(verdict["remaining_gates_count"] == 4, "remaining gate count changed")

    require(kernel["support_identity"] == "Pi_exact64 B^*P_TT = B^*P_TT", "support identity changed")
    require(kernel["lambda_GR_TT_internal"] == 15, "lambda must be 15")
    require("32*pi*G_eff" in kernel["retarded_solution_schema"], "retarded response schema missing normalization")

    length = kernel["length_anchor_form"]
    energy = kernel["energy_anchor_form"]
    require(length["G_eff"] == "0.29759362932431804 * L0^2", "length G formula changed")
    require(length["kappa_STF"] == "0.03342539276068642 / L0^2", "length kappa formula changed")
    require(energy["G_eff"] == "0.29759362932431804 / E0^2", "energy G formula changed")
    require(energy["kappa_STF"] == "0.03342539276068642 * E0^2", "energy kappa formula changed")

    require(assembly["closed_components"]["exact_TT_support"] is True, "TT support should close")
    require(assembly["closed_components"]["one_anchor_normalization_family"] is True, "normalization family should close")
    require(assembly["closed_components"]["universal_stress_tensor_form"] is True, "stress form should close")
    require(assembly["conditional_components"]["selected_full_matter_map_ready"] is False, "matter map must remain open")
    require(assembly["conditional_components"]["unconditional_full_GR_TT_operator_identity"] is False, "operator identity must remain open")
    require(assembly["conditional_components"]["literal_GR_TT_noise_channel_identity"] is False, "literal noise identity must remain open")

    require(set(open_gates.keys()) == {
        "selected_full_matter_stress_coefficients",
        "unconditional_GR_TT_operator_identity",
        "literal_GR_TT_noise_channel_identity",
        "absolute_SI_metrology",
    }, "open gates changed")
    require("conditional Einstein-response assembly" in note, "note must state conditional status")
    require(packet["assembly"]["conditional_theorem"]["kappa_relation"] == "kappa_STF = (32*pi*G_eff)^(-1)", "packet kappa relation changed")

    require(guards["claims_full_unconditional_GR"] is False, "must not claim full GR")
    require(guards["claims_measured_Newton_constant"] is False, "must not claim Newton")
    require(guards["uses_observed_Newton_or_Planck_input"] is False, "must not use Newton/Planck")
    require(guards["claims_selected_matter_coefficients_closed"] is False, "must not claim matter coefficients")
    require(guards["claims_unconditional_GR_TT_operator_identity"] is False, "must not claim unconditional identity")
    require(guards["adds_new_GR_parameter"] is False, "must not add GR parameter")

    print("AUDIT_PASS: one-anchor Einstein TT response assembled conditionally; full GR gates remain explicit")


if __name__ == "__main__":
    main()
