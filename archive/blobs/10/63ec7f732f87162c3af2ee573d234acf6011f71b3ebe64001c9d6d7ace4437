"""Audit final integrated SM-parity replay after source-identity patch."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finalintegratedsmparityreplayaftersourceidentitypatch"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RECONCILIATION = PACKET_DIR / "post_source_identity_final_replay_reconciliation.packet.json"
FINAL_REPLAY = PACKET_DIR / "final_integrated_sm_parity_replay_after_source_identity_patch.packet.json"
FRONTIER = PACKET_DIR / "true_equivalence_and_noknob_frontier_after_final_replay.packet.json"
NEXTSTEPS = PACKET_DIR / "post_final_sm_parity_next_steps.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FinalIntegratedSMParityReplayAfterSourceIdentityPatch_v1.md"

STATUS = "MTT_SELECTED_FINALINTEGRATEDSMPARITYREPLAY_AFTER_SOURCEIDENTITYPATCH_BUILT_SMPARITY_CLOSED_TRUE_EQ_OPEN"
NEXT = "MTT_Selected_ExternalRGBenchmarkValues_or_LocalQFTObservableFunctor_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    reconciliation = load(RECONCILIATION)
    final_replay = load(FINAL_REPLAY)
    frontier = load(FRONTIER)
    nextsteps = load(NEXTSTEPS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(candidate["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(
        reconciliation["status"]
        == "OLDER_TWO_GATE_AUDIT_SUPERSEDED_BY_ACCEPTED_RG_QASU3_AND_SOURCE_IDENTITY_PATCH",
        "reconciliation status mismatch",
    )
    result = reconciliation["reconciliation_result"]
    for key in [
        "common_scale_Yukawa_and_Higgs_transport_closed_for_SM_parity",
        "selected_SM_packet_certificate_integration_closed_for_SM_parity",
        "patched_dynamic_C1_source_and_value_interface_closed",
        "bridge_imported_as_latest_dynamic_C1_parity_close",
        "older_two_gate_matrix_superseded_at_parity_tier",
    ]:
        require(result[key] is True, f"reconciliation missing: {key}")
    require(reconciliation["guardrail"]["full_no_knob_closure"] is True, "no-knob guardrail missing")

    require(final_replay["status"] == "FINAL_INTEGRATED_SM_PARITY_REPLAY_PASSES_DECLARED_STANDARD", "final replay status mismatch")
    require(final_replay["all_replay_rows_pass"] is True, "replay rows did not pass")
    require(final_replay["SM_parity_closed_under_declared_standard"] is True, "SM parity not closed")
    require(final_replay["patched_dynamic_C1_source_identity_retained"] is True, "source identity not retained")
    require(final_replay["patched_dynamic_C1_value_interface_retained"] is True, "value interface not retained")
    require(final_replay["samebranch_or_independent_hessian_bridge_retained"] is True, "bridge not retained")
    require(
        any(row["id"] == "samebranch_or_independent_hessian_bridge" for row in final_replay["replay_rows"]),
        "bridge replay row missing",
    )
    require(final_replay["accepted_RG_transport_for_SM_parity"] is True, "RG not retained")
    require(final_replay["selected_SM_packet_certificate_integrated_for_SM_parity"] is True, "SM packet not retained")
    require(final_replay["closure_limits"]["true_precision_SM_equivalence"] is True, "precision guardrail missing")
    require(final_replay["closure_claimed"] is False, "global closure flag overclaimed")

    require(frontier["status"] == "SM_PARITY_CLOSED_TRUE_EQUIVALENCE_AND_NOKNOB_OPEN", "frontier status mismatch")
    require(frontier["SM_parity_closed"] is True, "frontier parity closed missing")
    require(frontier["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(frontier["no_knob_closed"] is False, "no-knob overclaimed")
    for key, value in frontier["source_identity_specific_no_knob_upgrade"].items():
        require(value is True, f"source identity upgrade missing: {key}")

    require(nextsteps["status"] == "NEXT_WORK_MOVES_TO_TRUE_EQUIVALENCE_PRECISION_AND_NOKNOB_UPGRADES", "nextsteps status mismatch")
    require(NEXT == nextsteps["recommended_next_artifact"], "nextsteps next mismatch")
    require("older two-gate final audit" in nextsteps["do_not_reopen_as_SM_parity_blockers"], "old audit not retired")
    require("dynamic C1 source identity under local parity principle" in nextsteps["do_not_reopen_as_SM_parity_blockers"], "C1 not retired as blocker")

    require(candidate["closure_decision"]["SM_parity_closed_under_declared_standard"] is True, "candidate parity closure missing")
    require(candidate["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclaimed")
    require(candidate["closure_decision"]["no_knob_closed"] is False, "candidate no-knob overclaimed")
    require(
        candidate["what_closes_now"]["samebranch_or_independent_hessian_bridge_retained"] is True,
        "candidate bridge flag missing",
    )
    require(candidate["closure_claimed"] is False and cert["closure_claimed"] is False, "closure_claimed guard violated")
    require(cert["SM_parity_closed_under_declared_standard"] is True, "cert parity missing")
    require(cert["true_SM_equivalence_closed"] is False, "cert true equivalence overclaimed")
    require(cert["no_knob_closed"] is False, "cert no-knob overclaimed")
    require("same-branch/independent-Hessian" in note, "note missing bridge import")
    require("older two-gate audit superseded         = True" in note, "note missing superseded audit")
    require("true SM equivalence closed              = False" in note, "note missing true-eq guardrail")
    require("no-knob closure                         = False" in note, "note missing no-knob guardrail")

    for packet in [candidate, reconciliation, final_replay, frontier, nextsteps, cert]:
        guard(packet)

    print(proc.stdout.strip())
    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
