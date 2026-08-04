"""Audit CONST-EW-02 B40 local-kernel to weak-mixing profile handoff."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b40_local_kernel_to_profile"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
PROPAGATION = BASE / "local_c1_source_kernel_propagation.packet.json"
PHYSICAL_GATE = BASE / "physical_weak_angle_gate_after_local_kernel.packet.json"
BOUNDARY = BASE / "weak_mixing_b40_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B40_LocalKernel_to_Profile_v1.md"

STATUS = "MTT_CONST_EW_02_B40_LOCAL_KERNEL_TO_PROFILE_HANDOFF_BUILT"


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
    propagation = load(PROPAGATION)
    physical_gate = load(PHYSICAL_GATE)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("propagation", propagation),
        ("physical_gate", physical_gate),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["local_dynamic_C1_source_kernel_propagated"] is True, "local kernel propagation")
    require(candidate["u_dyn_source_derived_preserved"] is True, "u_dyn")
    require(candidate["internal_lambda_12_closed_preserved"] is True, "lambda")
    require(candidate["physical_gate_reduced_to_gauge_action_RG_matching"] is True, "physical gate reduction")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    local = propagation["local_principle_tier"]
    require(local["source_kernel_closed"] is True, "local source kernel")
    require(local["strict_unpatched_kernel_closed"] is False, "unpatched overclosed")
    prefix = propagation["weak_mixing_profile_prefix"]
    require(prefix["u_dyn_source_derived"] is True and prefix["u_dyn_value"] == 1.0, "u_dyn prefix")
    require(prefix["internal_lambda_12_closed"] is True, "lambda prefix")
    disposition = propagation["local_tier_C1_source_promotion_disposition"]
    require(disposition["dynamic_C1_source_kernel_active_blocker_retired_in_local_tier"] is True, "C1 blocker")
    require(disposition["strict_no_knob_upgrade_still_tracks_unpatched_kernel"] is True, "strict ledger")

    remaining = physical_gate["remaining_physical_gates"]
    require(remaining["K_phys_or_f_ab_closed"] is False, "K phys overclosed")
    require(remaining["mu_match_closed"] is False, "mu match overclosed")
    require(remaining["RG_scheme_closed"] is False, "RG overclosed")
    require(physical_gate["physical_weak_angle_closure"] is False, "physical gate weak angle")

    closed = boundary["closed_or_decided_now"]
    require(closed["local_dynamic_C1_source_kernel_propagated"] is True, "boundary local")
    require(closed["physical_gate_reduced_to_gauge_action_RG_matching"] is True, "boundary physical gate")
    require(closed["physical_weak_angle_numerical_closure"] is False, "boundary weak angle")
    require(boundary["still_open"]["K_phys_or_gauge_kinetic_normalization"] is True, "K phys open")
    require(boundary["still_open"]["RG_threshold_scheme"] is True, "RG open")
    require("not re-opening the C1 source-kernel blocker in the local tier" in boundary["anti_cycle_delta_from_B39"]["not_repeated"], "anti-cycle")

    require(cert["status"] == STATUS, "cert status")
    require(cert["local_dynamic_C1_source_kernel_propagated"] is True, "cert local")
    require(cert["physical_gate_reduced_to_gauge_action_RG_matching"] is True, "cert physical gate")
    require(cert["physical_weak_angle_closure"] is False, "cert weak angle")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B41-GAUGE-ACTION-NORMALIZATION-ANCHOR", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B41-RG-MATCHING-THRESHOLD-SCHEME", "next parallel")
    require("B41" in note and "active blocker has moved" in note, "note")

    print("CONST-EW-02 B40 local-kernel to profile audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
