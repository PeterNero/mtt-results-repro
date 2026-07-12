"""Audit diagonal profile execution and multi-loop convention gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fullcovarianceprofile_or_multiloopconventionaudit"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROFILE = PACKET_DIR / "diagonal_profile_likelihood_execution.packet.json"
CONVENTION = PACKET_DIR / "multiloop_convention_audit_requirements.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_diagonal_profile.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FullCovarianceProfile_or_MultiLoopConventionAudit_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_FULLCOVARIANCEPROFILE_OR_MULTILOOPCONVENTIONAUDIT_BUILT_DIAGONAL_PROFILE_FULL_PROFILE_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    profile = load(PROFILE)
    convention = load(CONVENTION)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    rows = profile["profile_rows"]
    require(len(rows) == 6, "profile row count mismatch")
    chi2_sum = sum(row["chi2_contribution"] for row in rows)
    require(abs(chi2_sum - profile["chi2_diagonal"]) < 1e-12, "chi2 sum mismatch")
    require(profile["degrees_of_freedom"] == 6, "dof mismatch")
    require(abs(profile["reduced_chi2_diagonal"] - profile["chi2_diagonal"] / 6.0) < 1e-15, "reduced chi2 mismatch")
    require(profile["passes_coarse_diagonal_profile"] is True, "coarse profile should pass")
    require(profile["max_abs_pull"] < 3.0, "max pull too large")
    require(profile["accepted_as_full_covariance_profile"] is False, "full covariance profile overclaimed")
    for row in rows:
        require(row["total_diagonal_sigma"] > 0.0, f"missing sigma: {row['id']}")
        require(math.isfinite(row["pull"]), f"nonfinite pull: {row['id']}")
    yt = next(row for row in rows if row["id"] == "y_t_Mt")
    require(abs(yt["pull"]) > 2.0, "yt pull should remain the leading tension marker")

    reqs = convention["required_for_full_true_equivalence"]
    require(len(reqs) == 4, "convention requirement count mismatch")
    require(any(req["id"] == "correlated_input_profile" and req["closed"] is False for req in reqs), "correlated profile gate missing")
    require(any(req["id"] == "multi_loop_threshold_policy" and req["closed"] is False for req in reqs), "multi-loop gate missing")
    require(convention["source_independence_guardrails"]["profile_values_used_to_select_MTT_source"] is False, "source guard mismatch")
    require(convention["source_independence_guardrails"]["profile_values_allowed_as_SM_parity_replay"] is True, "parity replay guard mismatch")

    require("diagonal profile likelihood execution" in updated["closed_now"], "profile execution not closed")
    require("full correlated covariance/profile likelihood values" in updated["remaining_true_equivalence_blockers"], "correlated blocker missing")
    require("multi-loop threshold convention values" in updated["remaining_true_equivalence_blockers"], "multi-loop blocker missing")
    require(updated["guardrails"]["diagonal_profile_is_not_full_covariance_profile"] is True, "diagonal guard missing")
    require(updated["guardrails"]["coarse_profile_pass_is_not_true_SM_equivalence"] is True, "true-equivalence guard missing")

    for key in [
        "diagonal_profile_likelihood_executed",
        "coarse_diagonal_profile_passes",
        "multiloop_convention_audit_requirements_built",
        "superset_strategy_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"missing close flag: {key}")
    require(data["closure_decision"]["full_covariance_profile_closed"] is False, "full profile overclaimed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(cert["next_required_artifact"] == "MTT_Selected_CorrelatedProfileValues_or_LocalQFTObservableValues_v1", "next artifact mismatch")

    for packet in [profile, convention, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("diagonal chi-square" in note, "note missing diagonal chi-square")
    require("not a full covariance/profile" in note, "note missing guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
