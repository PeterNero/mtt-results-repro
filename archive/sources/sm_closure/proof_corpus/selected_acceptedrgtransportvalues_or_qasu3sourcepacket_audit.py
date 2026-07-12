"""Audit accepted first-pass RG transport values / QaSU3 source packet gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_acceptedrgtransportvalues_or_qasu3sourcepacket"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
VALUES = PACKET_DIR / "accepted_firstpass_common_scale_yukawa_higgs_values.packet.json"
BLOCKERS = PACKET_DIR / "remaining_one_gate_sm_parity_matrix.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AcceptedRGTransportValues_or_QaSU3SourcePacket_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_ACCEPTEDRGTRANSPORTVALUES_OR_QASU3SOURCEPACKET_BUILT_FIRSTPASS_RG_ACCEPTED_QASU3_OPEN"
NEXT_ARTIFACT = "MTT_Selected_QaSU3SourcePacket_or_FinalSMParityClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def finite_matrix(matrix: list) -> bool:
    for row in matrix:
        for pair in row:
            if not (math.isfinite(pair[0]) and math.isfinite(pair[1])):
                return False
    return True


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    values = load(VALUES)
    blockers = load(BLOCKERS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")
    require(NEXT_ARTIFACT in note, "note missing next artifact")

    require(values["status"] == "FIRSTPASS_COMMON_SCALE_VALUES_ACCEPTED_FOR_SM_PARITY_ONLY", "values status mismatch")
    require(values["accepted_for_SM_parity"] is True, "SM parity values not accepted")
    require(values["accepted_for_true_precision_equivalence"] is False, "precision overclaimed")
    require(values["acceptance_evidence"]["finite_values_emitted"] is True, "finite evidence missing")
    require(values["acceptance_evidence"]["internal_RK_convergence_closed"] is True, "convergence evidence missing")
    require(values["acceptance_evidence"]["central_value_tolerance_policy_executed"] is True, "tolerance evidence missing")
    accepted = values["accepted_values"]
    for key in ["Y_u_MZ_firstpass", "Y_d_MZ_firstpass", "Y_e_MZ_firstpass"]:
        require(finite_matrix(accepted[key]), f"nonfinite accepted matrix: {key}")
    require(math.isfinite(accepted["lambda_H_MZ_firstpass"]), "nonfinite lambda")
    for not_claimed in ["full threshold matching", "pole-to-running mass conversion", "no-knob derivation of Yukawa or Higgs values"]:
        require(not_claimed in values["not_claimed"], f"guardrail missing: {not_claimed}")
    require(values["observed_data_used_as_selector"] is False, "observed selector violation")
    require(values["target_fitting_used"] is False, "target fitting violation")

    require(blockers["status"] == "SM_PARITY_REDUCED_TO_ONE_SOURCE_GATE", "blocker matrix status mismatch")
    require("common_scale_Yukawa_and_Higgs_transport" in blockers["previous_SM_parity_blockers"], "previous RG blocker missing")
    require(blockers["closed_now"] == ["common_scale_Yukawa_and_Higgs_transport"], "closed gate mismatch")
    require(blockers["current_SM_parity_blockers"] == ["selected_SM_packet_certificate_integration"], "current blocker mismatch")
    require(blockers["remaining_gate_details"]["selected_SM_packet_certificate_integration"]["critical_open_row"]["id"] == "qa_su3_color_operator_packet", "QaSU3 critical row missing")
    require("full threshold matching" in blockers["precision_true_equivalence_still_open"], "precision threshold guard missing")
    require("no-knob Yukawa/Higgs/gauge constants" in blockers["no_knob_still_open"], "no-knob guard missing")

    for key in [
        "firstpass_RG_acceptance_convention_declared",
        "Y_u_Y_d_Y_e_lambda_H_firstpass_MZ_values_accepted_for_SM_parity",
        "common_scale_Yukawa_and_Higgs_transport_closed_for_SM_parity",
        "SM_parity_blocker_matrix_reduced_to_one_gate",
        "precision_RG_and_no_knob_guardrails_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_SM_packet_certificate_integration",
        "QaSU3_color_operator_packet",
        "SM_parity_closure",
        "precision_threshold_mass_scheme_RG",
        "true_SM_equivalence_closure",
        "full_no_knob_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key in ["SM_parity_closed", "true_SM_equivalence_closed", "no_knob_closed"]:
        require(data["closure_decision"][key] is False, f"closure overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "candidate guardrail violated")
    require("Current SM-parity blocker" in note, "note missing one-gate statement")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
