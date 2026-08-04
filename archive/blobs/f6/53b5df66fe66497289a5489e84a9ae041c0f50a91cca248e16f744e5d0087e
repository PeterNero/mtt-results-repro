"""Audit RG engine smoke execution / selected SM packet certificate gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rgengineexecution_or_selectedsmpacketcertificateintegration"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ENGINE = PACKET_DIR / "one_loop_sm_rg_engine_contract.packet.json"
SMOKE = PACKET_DIR / "diagnostic_one_loop_transport_smoke_run.packet.json"
CERT_GATE = PACKET_DIR / "selected_sm_packet_certificate_integration_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RGEngineExecution_or_SelectedSMPacketCertificateIntegration_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_RGENGINEEXECUTION_OR_SELECTEDSMPACKETCERTIFICATEINTEGRATION_BUILT_DIAGNOSTIC_RUN_ONLY"
NEXT_ARTIFACT = "MTT_Selected_ThresholdMassSchemeCovarianceFill_or_QaSU3PacketIntegration_v1"


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
    engine = load(ENGINE)
    smoke = load(SMOKE)
    cert_gate = load(CERT_GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")
    require(NEXT_ARTIFACT in note, "note missing next artifact")

    require(engine["status"] == "ONE_LOOP_RG_ENGINE_CONTRACT_AND_SMOKE_EXECUTION_BUILT", "engine status mismatch")
    require("Y_u" in engine["equations"] and "lambda_H" in engine["equations"], "equations incomplete")
    require(engine["accepted_for_SM_parity"] is False, "engine acceptance overclaimed")
    require(len(engine["acceptance_requirements_before_value_promotion"]) >= 5, "acceptance requirements incomplete")

    require(smoke["status"] == "DIAGNOSTIC_ONE_LOOP_SMOKE_RUN_FINITE_NOT_ACCEPTANCE_VALUES", "smoke status mismatch")
    require(smoke["accepted_for_SM_parity"] is False, "smoke acceptance overclaimed")
    require(smoke["finite_values_emitted"] is True, "finite flag missing")
    for key in ["Y_u_MZ", "Y_d_MZ", "Y_e_MZ", "lambda_H_MZ"]:
        require(smoke["acceptance_value_status"][key] == "NOT_EMITTED_ACCEPTANCE_VALUE", f"accepted value over-emitted: {key}")
    run = smoke["diagnostic_run"]
    require(run["steps"] == 256, "RK step count mismatch")
    require(run["from_scale_GeV"] > run["to_scale_GeV"] > 0, "scale direction mismatch")
    require(finite_matrix(run["diagnostic_Y_u_MZ_like"]), "nonfinite Yu diagnostic")
    require(finite_matrix(run["diagnostic_Y_d_MZ_like"]), "nonfinite Yd diagnostic")
    require(finite_matrix(run["diagnostic_Y_e_MZ_like"]), "nonfinite Ye diagnostic")
    require(math.isfinite(run["diagnostic_lambda_H_MZ_like"]), "nonfinite lambda diagnostic")
    for value in run["end_norms"].values():
        require(math.isfinite(value), "nonfinite end norm")
    require("no threshold matching" in smoke["known_limitations"], "threshold limitation missing")

    require(cert_gate["status"] == "CERTIFICATE_GATE_RECHECKED_QA_SU3_STILL_OPEN", "cert gate status mismatch")
    require(cert_gate["can_attach_final_packet_certificate_now"] is False, "packet certificate overclaimed")
    require(cert_gate["critical_open_row"]["id"] == "qa_su3_color_operator_packet", "Qa/SU3 blocker missing")

    for key in [
        "one_loop_RG_engine_contract_built",
        "diagnostic_RG_smoke_run_executed",
        "finite_RG_outputs_verified_diagnostic_only",
        "SM_packet_certificate_gate_rechecked",
        "RG_value_gate_separated_from_QaSU3_source_gate",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "accepted_Y_u_MZ_Y_d_MZ_Y_e_MZ_values",
        "accepted_lambda_H_MZ_value",
        "threshold_matching_values",
        "mass_scheme_conversion",
        "QaSU3_color_operator_packet",
        "SM_parity_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key in ["patched_SM_parity_closed", "true_SM_equivalence_closed", "no_knob_closed"]:
        require(data["closure_decision"][key] is False, f"closure overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "guardrail violated")
    require("diagnostic engine" in note and "Qa/SU3 color/operator packet" in note, "note missing core result")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
