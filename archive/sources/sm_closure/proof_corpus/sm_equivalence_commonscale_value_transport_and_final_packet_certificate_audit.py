"""Audit common-scale value transport and final packet certificate gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"
CERT = ROOT / "certificates" / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SM_Equivalence_CommonScale_ValueTransport_and_FinalPacketCertificate_v1.md"
BUILDER = ROOT / "scripts" / "build_sm_equivalence_commonscale_value_transport_and_final_packet_certificate.py"

STATUS = "MTT_SM_EQUIVALENCE_COMMONSCALE_VALUE_TRANSPORT_AND_FINALPACKETCERT_BUILT_PARTIAL_GAUGE_CLOSED"
NEXT = "MTT_SM_Equivalence_SelectedSMPacket_or_RGTransport_ValueFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    packet = data["common_scale_packet"]
    require(packet["status"] == "PARTIAL_COMMON_SCALE_PACKET_GAUGE_ONLY", "common-scale packet status mismatch")
    require(packet["reference_scale"] == "M_Z", "reference scale mismatch")
    require(packet["scheme"] == "MSbar", "scheme mismatch")
    for key in ["alpha_1_GUT_MZ", "alpha_2_MZ", "alpha_3_MZ", "g_1_GUT_MZ", "g_2_MZ", "g_3_MZ"]:
        require(packet["closed_values"][key]["central_value"] > 0.0, f"closed gauge value missing: {key}")
    for key in ["Y_u_MZ", "Y_d_MZ", "Y_e_MZ", "lambda_H_MZ", "pole_to_running_mass_maps", "threshold_matching_values"]:
        require(packet["transport_values_open"][key] is True, f"transport value not open: {key}")
    for key in ["Y_u_native", "Y_d_native_complex_up_diagonal_convention", "Y_e_native", "lambda_H_tree_native", "CKM_native", "PMNS_native"]:
        require(key in packet["native_values_carried_but_not_common_scale"], f"native carried value missing: {key}")

    final_packet = data["final_packet_certificate"]
    require(final_packet["status"] == "SM_PARITY_INTERFACE_PARTIAL_CERTIFICATE_BUILT_QA_SU3_OPEN", "final packet status mismatch")
    require(final_packet["interface_components_supported_except_QaSU3"] is True, "interface support missing")
    require(final_packet["can_close_true_SM_equivalence_now"] is False, "true equivalence overclosed")
    require(final_packet["can_close_SM_parity_interface_without_QaSU3"] is False, "SM interface overclosed")
    require(final_packet["critical_open_row"]["id"] == "qa_su3_color_operator_packet", "critical row mismatch")
    require(final_packet["critical_open_row"]["closed_for_sm_parity_interface"] is False, "Qa/SU3 incorrectly closed")
    require(len(final_packet["source_rows"]) == 6, "source row count mismatch")
    for row in final_packet["source_rows"]:
        require("required_selected_data" in row, f"source row incomplete: {row.get('id')}")
    require(any("observed SM couplings" in item for item in final_packet["unsafe_shortcuts_rejected"]), "unsafe shortcut guard missing")

    status = data["observable_status"]
    require(status["gauge_MZ"] == "CLOSED_AT_DECLARED_REFERENCE_SCALE", "gauge status mismatch")
    require(status["source_packet"] == "PARTIAL_CERTIFICATE_QA_SU3_OPEN", "source packet status mismatch")
    require(status["local_QFT_observables"] == "OPEN", "local QFT status mismatch")

    decision = data["closure_decision"]
    require(decision["common_scale_gauge_values"] == "CLOSED", "gauge closure decision mismatch")
    require(decision["common_scale_yukawa_higgs_values"] == "OPEN", "Yukawa/Higgs should remain open")
    require(decision["selected_SM_packet_final_certificate"] == "OPEN_QA_SU3_COLOR_OPERATOR_PACKET", "packet certificate decision mismatch")
    require(decision["true_SM_equivalence"] == "OPEN", "true equivalence overclosed")
    require(decision["no_knob_SM_derivation"] == "OPEN", "no-knob overclosed")

    closes = data["what_closes_now"]
    for key in [
        "common_scale_gauge_values_at_MZ",
        "partial_common_scale_packet_built",
        "final_packet_certificate_rows_instantiated",
        "QaSU3_identified_as_source_interface_blocker",
        "value_transport_blockers_separated_from_source_certificate_blockers",
        "source_selection_guardrails_preserved",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "Yukawa_common_scale_transport",
        "Higgs_lambda_common_scale_transport",
        "loop_threshold_beta_function_values",
        "full_covariance_profile_likelihood",
        "absolute_neutrino_mass_or_policy_upgrade",
        "local_QFT_observable_functor_values",
        "QaSU3_color_operator_packet",
        "selected_SM_packet_final_certificate",
        "true_SM_equivalence_closure",
        "full_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining gate missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["native_replay_closure_claimed"] is True, "native replay closure lost")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["source_boundary_preserved"] is True, "source boundary not preserved")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("Gate A: common-scale Yukawa/Higgs/threshold transport values" in note, "note missing gate A")
    require("Gate B: final selected SM packet certificate" in note, "note missing gate B")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
