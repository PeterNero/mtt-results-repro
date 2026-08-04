"""Audit the finitepart/kernel policy closure on A_N."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_finitepartkernelpolicy_on_an_or_sourcebranchidentity.py"

SLUG = "selected_finitepartkernelpolicy_on_an_or_sourcebranchidentity"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FinitepartKernelPolicy_on_AN_or_SourceBranchIdentity_v1.md"
POLICY_PACKET = PACKET_DIR / "an_finitepart_kernel_policy.packet.json"
LOGDET_GATE_PACKET = PACKET_DIR / "strict_logdet_gate_after_an_policy.packet.json"
FRONTIER_PACKET = PACKET_DIR / "next_sourcebranch_or_cechhym_after_policy.packet.json"

STATUS = (
    "MTT_SELECTED_FINITEPARTKERNELPOLICY_ON_AN_OR_SOURCEBRANCHIDENTITY_"
    "FINITE_POLICY_CLOSED_LOGDET_ROW_STILL_SOURCEBRANCH_OPEN"
)
NEXT = "MTT_Selected_SourceBranchIdentity_or_CechHYMConnectionValues_AfterFinitepartPolicy_v1"
ACCEPTED = [
    "typed_f_sections",
    "typed_g_sections",
    "g_after_f_zero_exactness_certificate",
    "BN27_DE_Riesz_Green_kernel_trace_export",
]
REMAINING = [
    "cech_transition_cocycles",
    "selected_HYM_or_projective_connection_coefficients",
    "finitepart_log92160000_identity_from_values",
    "no_lifted_flags_connection_replay",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    policy = load(POLICY_PACKET)
    logdet_gate = load(LOGDET_GATE_PACKET)
    frontier = load(FRONTIER_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(frontier["next_required_artifact"] == NEXT, "frontier next mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, policy, logdet_gate, frontier]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    require(policy["status"] == "FINITEPART_KERNEL_POLICY_CLOSED_ON_SELECTED_A_N_SOURCE", "policy status")
    require(policy["finite_source_exactness_theorem"]["proved"] is True, "finite exactness missing")
    require(policy["finite_source_exactness_theorem"]["finite_trace"] is True, "finite trace missing")
    require(policy["finite_source_exactness_theorem"]["unprojected_continuum_HYM"] is False, "continuum overclaim")
    require(policy["kernel_policy"]["kernel_trace_policy_source_owned_on_A_N"] is True, "kernel policy not source-owned")
    require(policy["finitepart_functional"]["source_owned_finitepart_functional_closed_on_A_N"] is True, "finitepart not closed")
    require(policy["finitepart_functional"]["ordinary_continuum_zeta_claimed"] is False, "zeta overclaim")
    values = policy["exact_oriented_values_retained"]
    require(values["plus_sector_product"] * values["minus_sector_product"] == values["oriented_abs_sector_product"], "sector product")
    require(values["oriented_abs_sector_product"] == 92160000, "oriented product")
    require(values["oriented_abs_sector_logdet_exact"] == "log(92160000)", "oriented log")
    require(policy["policy_does_not_yet_promote"]["finitepart_log92160000_identity_from_values"] is True, "logdet guard")
    require(policy["policy_does_not_yet_promote"]["no_lifted_flags_connection_replay"] is True, "no-lift guard")

    require(logdet_gate["accepted_final_same_source_connection_tables"] == 4, "accepted count")
    require(logdet_gate["accepted_rows"] == ACCEPTED, "accepted rows")
    require(logdet_gate["remaining_rows"] == REMAINING, "remaining rows")
    finite_policy = logdet_gate["finite_policy_closure"]
    require(finite_policy["kernel_trace_policy_source_owned_on_A_N"] is True, "gate kernel policy")
    require(finite_policy["source_owned_finitepart_functional_closed_on_A_N"] is True, "gate finitepart policy")
    require(finite_policy["exact_log92160000_arithmetic_available"] is True, "gate exact log")
    require(finite_policy["conditional_no_lift_replay_available"] is True, "gate conditional replay")
    for key, value in logdet_gate["strict_promotion_blockers_remaining"].items():
        require(value is False, f"strict blocker unexpectedly closed: {key}")
    require(logdet_gate["new_final_rows_promoted"] == [], "new rows promoted unexpectedly")

    decision = candidate["closure_decision"]
    require(decision["accepted_final_same_source_connection_tables"] == 4, "decision accepted count")
    require(decision["accepted_rows"] == ACCEPTED, "decision accepted rows")
    require(decision["remaining_rows"] == REMAINING, "decision remaining rows")
    require(decision["kernel_trace_policy_source_owned_on_A_N"] is True, "decision kernel policy")
    require(decision["source_owned_finitepart_functional_closed_on_A_N"] is True, "decision finitepart policy")
    require(decision["new_final_rows_promoted"] == 0, "decision new rows")
    for key in [
        "finitepart_log92160000_identity_from_values_promoted",
        "no_lifted_flags_connection_replay_promoted",
        "source_branch_identity_closed",
        "selected_connection_witness_values_closed",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")
        require(cert[key] is False, f"cert overclaim: {key}")

    require(frontier["current_count"] == "4/8", "frontier count")
    require(frontier["remaining_rows"] == REMAINING, "frontier remaining")
    require("count remains `4/8`" in note, "note missing count")
    require(NEXT in note, "note missing next")

    print("Finitepart/kernel policy on A_N audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
