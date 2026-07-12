"""Audit common-scale Yukawa/Higgs transport kernel scaffold / final replay audit gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
KERNEL = PACKET_DIR / "yukawa_higgs_common_scale_transport_kernel.packet.json"
AUDIT_PLAN = PACKET_DIR / "final_empirical_replay_audit_plan.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CommonScaleYukawaHiggsTransport_or_FinalReplayAudit_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_COMMONSCALEYUKAWAHIGGSTRANSPORT_OR_FINALREPLAYAUDIT_BUILT_TRANSPORT_KERNEL_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RGEngineExecution_or_SelectedSMPacketCertificateIntegration_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    kernel = load(KERNEL)
    audit_plan = load(AUDIT_PLAN)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")
    require(NEXT_ARTIFACT in note, "note missing next artifact")

    require(kernel["status"] == "TRANSPORT_KERNEL_SPEC_BUILT_VALUES_NOT_EMITTED", "kernel status mismatch")
    require(kernel["target_scale"] == "M_Z", "target scale mismatch")
    require(kernel["target_scheme"] == "MSbar", "target scheme mismatch")
    for key in ["Y_u_native", "Y_d_native_complex_up_diagonal_convention", "Y_e_native", "lambda_H_tree_native"]:
        require(key in kernel["native_values_to_transport"], f"missing native transport key: {key}")
    for key in ["Y_u_MZ", "Y_d_MZ", "Y_e_MZ", "lambda_H_MZ"]:
        require(kernel["emitted_values"][key] is None, f"transport value over-emitted: {key}")
    require("beta functions" in " ".join(kernel["required_engine_inputs"]["beta_functions_required"]), "beta functions not required")
    require(kernel["observed_data_used_as_selector"] is False, "observed data selector violation")
    require(kernel["target_fitting_used"] is False, "target fitting violation")

    require(audit_plan["status"] == "FINAL_REPLAY_AUDIT_PLAN_BUILT_WAITING_FOR_TRANSPORT_VALUES_AND_PACKET_CERT", "audit plan status mismatch")
    blocks = {row["block"]: row for row in audit_plan["audit_blocks"]}
    require(blocks["gauge_MZ"]["can_run_now"] is True, "gauge block should be runnable")
    for key in ["charged_yukawa_MZ", "higgs_lambda_MZ", "selected_SM_packet_certificate"]:
        require(blocks[key]["can_run_now"] is False, f"audit block overclaimed: {key}")
    require(audit_plan["closure_claimed"] is False, "audit plan closure overclaimed")

    for key in [
        "common_scale_yukawa_higgs_transport_kernel_specified",
        "native_values_to_transport_bound_into_one_packet",
        "final_empirical_replay_audit_plan_built",
        "transport_shortcut_rejected",
        "superset_strategy_remains_locked_to_downstream_replay",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "RG_engine_execution",
        "Y_u_MZ_Y_d_MZ_Y_e_MZ_values",
        "lambda_H_MZ_value",
        "selected_SM_packet_certificate_integration",
        "final_integrated_empirical_replay_audit",
        "SM_parity_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key in ["patched_SM_parity_closed", "true_SM_equivalence_closed", "no_knob_closed"]:
        require(data["closure_decision"][key] is False, f"closure overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require("Y_u(M_Z), Y_d(M_Z), Y_e(M_Z) = OPEN" in note, "note missing transport guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
