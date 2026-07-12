"""Audit CONST-EW-02 B44 conditional weak-mixing profile execution packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b44_conditional_profile_execution"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
ASSUMPTIONS = BASE / "conditional_profile_assumption_lock.packet.json"
EXECUTION = BASE / "conditional_profile_execution.packet.json"
COMPARISON = BASE / "profile_status_and_comparison_boundaries.packet.json"
BOUNDARY = BASE / "weak_mixing_b44_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B44_ConditionalProfileExecution_v1.md"

STATUS = "MTT_CONST_EW_02_B44_CONDITIONAL_PROFILE_EXECUTION_BUILT_REPLAY_ONLY"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    assumptions = load(ASSUMPTIONS)
    execution = load(EXECUTION)
    comparison = load(COMPARISON)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("assumptions", assumptions),
        ("execution", execution),
        ("comparison", comparison),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["conditional_profile_execution_closed"] is True, "profile execution")
    require(abs(candidate["conditional_minimal_threshold_sin2"] - 0.2315309482915084) < 1e-15, "candidate sin2")
    require(candidate["comparison_boundaries_declared"] is True, "comparison boundaries")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")
    require(candidate["strict_full_no_knob_closure"] is False, "strict overclosed")

    assumption_map = assumptions["assumptions"]
    require(assumption_map["local_source_kernel_tier"]["accepted"] is True, "local tier")
    require(assumption_map["local_source_kernel_tier"]["strict_unpatched"] is False, "strict local tier")
    require(assumption_map["one_primitive_tier"]["contract_closed"] is True, "one primitive contract")
    require(assumption_map["one_primitive_tier"]["value_selected"] is False, "primitive value")
    require(assumption_map["minimal_threshold_policy"]["closed"] is True, "minimal threshold")
    require(assumption_map["minimal_threshold_policy"]["strict_vector_emitted"] is False, "strict vector")
    require(assumption_map["source_strength_prefix"]["u_dyn_source_derived"] is True, "u_dyn source")
    require("calling this strict no-knob closure" in assumptions["forbidden_uses"], "forbidden strict")

    values = execution["values"]
    require(abs(values["sin2_conditional_minimal_threshold"] - 0.2315309482915084) < 1e-15, "execution sin2")
    require(abs(values["sin2_high_scale_y0"] - 0.2515877565744274) < 1e-15, "high-scale value")
    require(execution["checks"]["matches_B43_conditional_value"] is True, "B43 check")
    require(execution["checks"]["matches_B22_conditional_value"] is True, "B22 check")
    require(execution["checks"]["finite_value"] is True, "finite check")
    require(execution["checks"]["inside_positive_A2_interval"] is True, "interval check")

    require(comparison["emitted_value"]["classification"] == "conditional replay value", "classification")
    require("strict no-knob source prediction claim" in comparison["blocked_comparisons"], "blocked strict comparison")
    require(comparison["open_promotions"]["strict_QaStack_threshold_vector"] is True, "strict threshold open")
    require(comparison["open_promotions"]["primitive_E0_or_L0_value"] is True, "primitive open")
    require(comparison["open_promotions"]["physical_effective_weak_angle"] is True, "physical angle open")

    closed = boundary["closed_or_decided_now"]
    require(closed["conditional_assumption_lock"] is True, "boundary assumptions")
    require(closed["conditional_profile_execution"] is True, "boundary execution")
    require(closed["profile_value_regression_test"] is True, "boundary regression")
    require(boundary["still_open"]["strict_QaStack_threshold_vector"] is True, "boundary strict threshold")
    require(boundary["still_open"]["primitive_value_or_source_unit"] is True, "boundary primitive")
    require(boundary["still_open"]["physical_weak_angle_numerical_closure"] is True, "boundary physical")
    require("not promoting the replay value to a physical weak-angle closure" in boundary["anti_cycle_delta_from_B43"]["not_repeated"], "anti-cycle")

    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B45-QASTACK-QUOTIENTFUNCTOR-ABASE-IDENTITY-ATTEMPT", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B45-PRIMITIVE-VALUE-SOURCE-SEARCH", "next parallel")

    require(cert["status"] == STATUS, "cert status")
    require(cert["conditional_profile_execution_closed"] is True, "cert execution")
    require(cert["physical_weak_angle_closure"] is False, "cert weak angle")
    require(cert["strict_full_no_knob_closure"] is False, "cert strict")
    require("B44" in note and "conditional replay sin2" in note and "machine-checked" in note, "note")

    print("CONST-EW-02 B44 conditional profile execution audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
