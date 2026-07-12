"""Audit local Weyl-variation action-principle application."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ACCEPTED = PACKET_DIR / "accepted_local_weylvariation_actionprinciple.packet.json"
APPLIED_KERNEL = PACKET_DIR / "applied_principle_kernel_closure.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "applied_kernel_validator_result.packet.json"
UNPATCHED_EXIT = PACKET_DIR / "unpatched_or_independent_kernel_execution_exit.packet.json"
DECISION = PACKET_DIR / "apply_or_independent_execution_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_WeylVariationActionPrinciple_Apply_or_IndependentKernelExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_WEYLVARIATION_ACTIONPRINCIPLE_APPLIED_LOCAL_KERNEL_CLOSED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_LocalPrincipleDynamicC1Closure_Integration_or_UnpatchedKernelExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    accepted = load(ACCEPTED)
    applied = load(APPLIED_KERNEL)
    validator = load(VALIDATOR_RESULT)
    unpatched = load(UNPATCHED_EXIT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")

    require(
        accepted["status"] == "LOCAL_WEYLVARIATION_ACTION_PRINCIPLE_ACCEPTED_IN_THIS_PROOF_SPINE",
        "accepted status mismatch",
    )
    require(accepted["accepted_as"] == "explicit local premise, not unpatched theorem", "accepted_as guard missing")
    require(accepted["external_papers_modified"] is False, "external papers modified")
    for key, value in accepted["guardrails"].items():
        require(value is False, f"accepted guardrail overclosed: {key}")

    require(applied["status"] == "STRICT_PRE_RESIDUAL_KERNEL_CLOSED_BY_ACCEPTED_LOCAL_PRINCIPLE", "applied status mismatch")
    for key in ["same_branch", "selected_variation_functional", "same_source_hessian", "sector_functor", "independence_certificate"]:
        require(applied[key] is True, f"applied kernel field missing: {key}")
    require(applied["locked_target_values_used_as_source"] is False, "locked target used as source")
    require(applied["residual_projector_replay_used_as_source"] is False, "residual replay used as source")
    for key, value in applied["promoted_inside_local_spine"].items():
        require(value is True, f"local promotion missing: {key}")
    for key, value in applied["does_not_close"].items():
        require(value is True, f"does-not-close guard missing: {key}")

    require(validator["ok"] is True, "applied kernel validator should pass")
    require(validator["exit_code"] == 0, "validator exit mismatch")

    require(unpatched["status"] == "UNPATCHED_AND_INDEPENDENT_EXECUTION_EXITS_REMAIN_OPEN", "unpatched status mismatch")
    require(unpatched["unpatched_principle_derived_now"] is False, "unpatched principle overderived")
    require(unpatched["route_A_accepts_without_local_principle"] is False, "Route A overaccepted")
    require(unpatched["route_B_accepts_without_local_principle"] is False, "Route B overaccepted")
    require(unpatched["independent_kernel_execution_supplied"] is False, "independent execution overclaimed")
    require(unpatched["local_principle_replaces_neither_exit"] is True, "exit preservation missing")
    require(len(unpatched["remaining_unpatched_exits"]) == 2, "remaining exit count mismatch")

    require(
        decision["status"] == "LOCAL_PRINCIPLE_APPLIED_KERNEL_VALIDATES_UNPATCHED_EXITS_RETAINED",
        "decision status mismatch",
    )
    require(decision["local_principle_accepted"] is True, "local principle not accepted")
    require(decision["applied_kernel_validator_ok"] is True, "decision validator not ok")
    require(decision["local_pre_residual_kernel_closed"] is True, "local kernel not closed")
    require(decision["unpatched_principle_derived_now"] is False, "decision overderived principle")
    require(decision["independent_kernel_execution_supplied"] is False, "decision overclaimed independent execution")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")
    require(decision["superset_strategy"]["locked_target_used_only_as_postcheck"] is True, "locked target misuse")
    require(decision["superset_strategy"]["paths_used_as_free_parameters"] is False, "paths treated as knobs")

    require(data["theorem"]["proved"] is True, "local theorem not proved")
    closure = data["closure_decision"]
    require(closure["local_principle_accepted"] is True, "candidate local principle not accepted")
    require(closure["local_pre_residual_kernel_closed"] is True, "candidate local kernel not closed")
    require(closure["unpatched_principle_derived_now"] is False, "candidate overderived principle")
    require(closure["independent_kernel_execution_supplied"] is False, "candidate overclaimed independent execution")
    require(closure["unpatched_dynamic_C1_closed"] is False, "candidate unpatched dynamic overclosed")
    require(closure["global_closure_claimed"] is False, "global closure overclaimed")
    for key in [
        "local_weylvariation_principle_accepted",
        "strict_pre_residual_kernel_closed_under_local_principle",
        "unpatched_exits_preserved",
        "local_dynamic_C1_spine_has_stronger_source_kernel_basis",
    ]:
        require(data["what_closes_now"][key] is True, f"achievement missing: {key}")

    require("explicit local premise" in note, "note missing local premise guard")
    require("does not derive the principle" in note, "note missing unpatched guard")

    for packet in [data, accepted, applied, unpatched, decision, cert]:
        guard(packet)

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
