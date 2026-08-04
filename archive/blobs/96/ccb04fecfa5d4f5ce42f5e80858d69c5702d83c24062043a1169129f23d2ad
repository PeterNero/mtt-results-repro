"""Audit CONST-EW-02 B39 source-kernel/local-principle decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b39_source_kernel_or_local_principle"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
LOCAL_KERNEL = BASE / "local_principle_preresidual_source_kernel.packet.json"
UNPATCHED = BASE / "strict_unpatched_source_kernel_status.packet.json"
DECISION = BASE / "b39_decision_boundary.packet.json"
BOUNDARY = BASE / "weak_mixing_b39_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B39_SourceKernel_or_LocalPrinciple_v1.md"

STATUS = "MTT_CONST_EW_02_B39_SOURCE_KERNEL_LOCAL_PRINCIPLE_TIER_BUILT"


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
    local = load(LOCAL_KERNEL)
    unpatched = load(UNPATCHED)
    decision = load(DECISION)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("local", local),
        ("unpatched", unpatched),
        ("decision", decision),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["local_tier_source_kernel_closed"] is True, "local kernel not closed")
    require(candidate["strict_unpatched_source_kernel_closed"] is False, "unpatched kernel overclosed")
    require(candidate["one_universal_principle_tier_used"] is True, "principle tier missing")
    require(candidate["free_numeric_parameter_used"] is False, "numeric parameter introduced")
    require(candidate["source_promotion_closed_in_local_tier"] is True, "local source promotion missing")
    require(candidate["source_promotion_closed_strict_no_knob"] is False, "strict source promotion overclosed")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    clauses = local["kernel_clauses_under_local_principle"]
    for key in [
        "selected_variation_functional",
        "same_source_hessian",
        "same_source_hessian_b_selected_rows",
        "pre_residual_phase_shift_operator_source",
        "sector_functor",
        "sector_rows_physical_source_promotion",
        "independence_certificate",
        "independence_from_residual_projector_replay",
    ]:
        require(clauses[key] is True, f"local clause not closed: {key}")
    require(local["strict_pre_residual_kernel_closed_under_local_principle"] is True, "strict local kernel")
    require(local["residual_projector_replay_used_as_source"] is False, "residual replay source")
    require(local["locked_target_values_used_as_source"] is False, "locked target source")
    require("Do not call this an unpatched derivation" in local["forbidden_use"], "local forbidden boundary")

    require(unpatched["current_pre_residual_validator_rejects"] is True, "unpatched validator should reject")
    require(unpatched["source_identity_unpatched_derived"] is False, "source identity overderived")
    require(unpatched["honest_kernel_export_emitted"] is False, "honest export overemitted")
    require(unpatched["route_A_accepts_without_local_principle"] is False, "Route A overaccepted")
    require(unpatched["route_B_accepts_without_local_principle"] is False, "Route B overaccepted")
    require(unpatched["strict_manifest_available"]["row_counts"]["total_rows"] == 110, "manifest row count")

    require(decision["local_tier_source_kernel_closed"] is True, "decision local close")
    require(decision["strict_unpatched_source_kernel_closed"] is False, "decision unpatched overclose")
    require(decision["one_universal_principle_tier_used"] is True, "decision principle")
    require(decision["free_numeric_parameter_used"] is False, "decision numeric parameter")
    require(decision["observed_weak_angle_used"] is False, "decision observed weak angle")

    closed = boundary["closed_or_decided_now"]
    require(closed["local_pre_residual_variation_hessian_source_kernel_emitted"] is True, "boundary local kernel")
    require(closed["same_source_b_selected_closed_in_local_tier"] is True, "boundary b")
    require(closed["strict_unpatched_kernel_closed"] is False, "boundary unpatched")
    require(closed["free_numeric_parameter_introduced"] is False, "boundary parameter")
    require(boundary["still_open"]["strict_unpatched_SelectedWeylVariationActionPrinciple_derivation"] is True, "strict derivation should remain open")
    require(boundary["still_open"]["physical_weak_angle_numerical_closure"] is True, "weak angle should remain open")
    require("not claiming local premise as unpatched no-knob proof" in boundary["anti_cycle_delta_from_B38"]["not_repeated"], "anti-cycle guard")

    require(cert["status"] == STATUS, "cert status")
    require(cert["local_tier_source_kernel_closed"] is True, "cert local")
    require(cert["strict_unpatched_source_kernel_closed"] is False, "cert unpatched")
    require(cert["one_universal_principle_tier_used"] is True, "cert principle")
    require(cert["physical_weak_angle_closure"] is False, "cert weak angle")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B40-LOCAL-C1-SOURCE-KERNEL-PROPAGATION", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B40-STRICT-NO-KNOB-UPGRADE-LEDGER", "next parallel")
    require("B40" in note and "not pretend" in note, "note")

    print("CONST-EW-02 B39 source-kernel/local-principle audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
