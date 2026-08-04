"""Audit strict PEW/direct-K row emission attempt or gauge-action source packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_strictpewdirectkrowemissionattempt_or_gaugeactionnormalizationsource"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ACCEPTANCE = PACKET_DIR / "strict_pew_directk_acceptance_predicate.packet.json"
ROW_ATTEMPT = PACKET_DIR / "strict_pew_source_row_emission_attempt.packet.json"
DIRECT_K_GATE = PACKET_DIR / "direct_kthreshold_certificate_gate.packet.json"
NEXT_PAYLOAD = PACKET_DIR / "next_gauge_action_normalization_source_payload.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StrictPEWDirectKRowEmissionAttempt_or_GaugeActionNormalizationSource_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_STRICTPEWDIRECTKROWEMISSIONATTEMPT_OR_GAUGEACTIONNORMALIZATIONSOURCE_"
    "ATTEMPT_EXECUTED_ZERO_STRICT_ROWS_SOURCE_PAYLOAD_OPEN"
)
NEXT = "MTT_Selected_PEWGaugeActionNormalizationSourcePacket_or_DirectKCertificatePayload_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    acceptance = load(ACCEPTANCE)
    row_attempt = load(ROW_ATTEMPT)
    direct_k = load(DIRECT_K_GATE)
    next_payload = load(NEXT_PAYLOAD)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("acceptance", acceptance),
        ("row_attempt", row_attempt),
        ("direct_k", direct_k),
        ("next_payload", next_payload),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(next_payload["next_required_artifact"] == NEXT, "next payload")
    require(data["theorem"]["proved"] is True, "theorem proved")
    require(data["theorem"]["name"] == "StrictPEWDirectKRowEmissionAttemptTheorem", "theorem name")

    require(data["strict_row_emission_attempt_closed"] is True, "attempt not closed")
    require(data["strict_P_EW_source_theorem_closed"] is False, "strict PEW overclaim")
    require(data["direct_K_threshold_Omega_H_lambda_closed"] is False, "direct K overclaim")
    require(data["minimal_one_primitive_lane_preserved"] is True, "primitive lane")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    rejects = acceptance["rejects"]
    require("counted P_EW primitive without source theorem" in rejects, "primitive rejection")
    require("near-miss internal expressions without correction source" in rejects, "near-miss rejection")
    require("diagnostic lambda_H replay" in rejects, "lambda replay rejection")

    closed_inputs = row_attempt["closed_inputs"]
    require(closed_inputs["finite_H_radial_source_closed"] is True, "finite H")
    require(closed_inputs["selected_R_H_RG_source_emitted"] is True, "R_H_RG")
    require(closed_inputs["H_specific_parameter_count_after_finite_H"] == 0, "H count")
    require(closed_inputs["internal_lambda_12_available"] is True, "lambda12")
    require(closed_inputs["minimal_one_prefactor_lane_closed"] is True, "minimal primitive")

    require(row_attempt["accepted_strict_P_EW_source_rows"] == 0, "strict PEW rows")
    require(row_attempt["exact_expression_hits_found"] == 0, "exact hits")
    require(row_attempt["strict_P_EW_source_emitted"] is False, "PEW overemitted")
    require(len(row_attempt["candidate_rows_tested"]) >= 3, "candidate rows")
    best = row_attempt["best_near_miss"]
    require(best["formula"] == "8*Delta_G12/pi^2", "best formula")
    require(0 < best["relative_residual"] < 1e-3, "best residual")
    require(best["correction_factor_required"] != 1.0, "correction factor")

    primitive = row_attempt["one_primitive_replay"]
    require(primitive["accepted_as_strict_source"] is False, "primitive promoted")
    require(primitive["P_EW_action_prefactor"] == 0.0685013467625, "primitive value")
    require(primitive["relative_residual"] < 1e-12, "replay residual")

    require(direct_k["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K rows")
    require(direct_k["strict_K_threshold_Omega_H_lambda_emitted"] is False, "direct K emitted")
    require(direct_k["closed_prerequisites"]["selected_R_H_RG"] is True, "direct K R_H")
    require(direct_k["missing_for_strict_direct_K"]["selected_A_EW_or_equivalent_prefactor"] is False, "A_EW missing")
    require(
        direct_k["missing_for_strict_direct_K"]["row_level_K_threshold_Omega_H_lambda_certificate"] is False,
        "row cert missing",
    )

    required = next_payload["required_new_payload"]
    for route in [
        "route_A_same_branch_gauge_action",
        "route_B_direct_K_certificate",
        "route_C_nonHiggs_crossuse",
    ]:
        require(route in required, f"missing {route}")

    decision = data["closure_decision"]
    require(decision["strict_row_emission_attempt_closed"] is True, "decision attempt")
    require(decision["finite_H_radial_source_closed"] is True, "decision finite H")
    require(decision["H_specific_parameter_count_after_finite_H"] == 0, "decision H count")
    require(decision["minimal_one_primitive_lane_closed"] is True, "decision primitive")
    require(decision["accepted_strict_P_EW_source_rows"] == 0, "decision PEW rows")
    require(decision["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "decision K rows")
    require(decision["exact_A_EW_expression_hits_found"] == 0, "decision exact hits")
    require(decision["best_A_EW_expression_formula"] == "8*Delta_G12/pi^2", "decision formula")
    require(decision["P_EW_counted_as_shared_physical_primitive"] is True, "decision counted")
    require(decision["P_EW_parameter_count"] == 1, "decision P_EW count")
    require(decision["strict_P_EW_source_promoted"] is False, "decision PEW promoted")
    require(decision["direct_K_threshold_Omega_H_lambda_emitted"] is False, "decision direct K")
    require(decision["full_no_knob_closed"] is False, "decision no-knob")
    require(decision["true_SM_equivalence_closed"] is False, "decision true SM")

    require(cert["theorem_proved"] is True, "cert theorem")
    require(cert["accepted_strict_P_EW_source_rows"] == 0, "cert PEW")
    require(cert["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "cert K")
    require(cert["minimal_one_primitive_lane_preserved"] is True, "cert primitive")

    for phrase in [
        "StrictPEWDirectKRowEmissionAttemptTheorem",
        "accepted strict `P_EW` source rows: `0`",
        "accepted direct `K_threshold.Omega_H.lambda` rows: `0`",
        "exact `A_EW` expression hits found: `0`",
        "best current expression: `8*Delta_G12/pi^2`",
        "not promoted as strict selected source data",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: strict PEW/direct-K row emission attempt executed with zero "
        "accepted strict rows; next payload is gauge/action normalization, direct-K "
        "certificate, or non-Higgs HRG cross-use."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
