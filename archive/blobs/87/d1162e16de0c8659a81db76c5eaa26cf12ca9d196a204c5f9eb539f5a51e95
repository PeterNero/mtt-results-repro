"""Audit CONST-EW-02 B29 Route-B final source-theorem frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b29_routeb_final_source_theorem_frontier"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
VALIDATOR = BASE / "strict_validator_import.packet.json"
ROUTEB = BASE / "routeb_final_source_theorem_frontier.packet.json"
ANTICYCLE = BASE / "anti_cycle_progress_ledger.packet.json"
BOUNDARY = BASE / "weak_mixing_b29_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B29_RouteBFinalSourceTheoremFrontier_v1.md"

STATUS = "MTT_CONST_EW_02_B29_ROUTEB_FINAL_SOURCE_THEOREM_FRONTIER_BUILT"


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
    validator = load(VALIDATOR)
    routeb = load(ROUTEB)
    anti = load(ANTICYCLE)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("validator", validator),
        ("routeb", routeb),
        ("anti", anti),
        ("boundary", boundary),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["strict_validator_built"] is True, "strict validator")
    require(candidate["selected_basis_independence_closed"] is True, "basis independence")
    require(candidate["route_B_all_other_strict_fields_closed"] is True, "route B field reduction")
    require(candidate["primitive_source_theorem_template_emitted"] is True, "primitive template")
    require(candidate["route_B_promoted_now"] is False, "Route B overpromoted")
    require(candidate["source_independence_closed"] is False, "source independence overclosed")
    require(candidate["anti_cycle_confirmed"] is True, "anti-cycle missing")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    require(validator["current_attempt_rejected_as_expected"] is True, "current rejection missing")
    require(validator["decision"]["strict_validator_built"] is True, "validator not built")
    require(validator["decision"]["route_A_filled_now"] is False, "Route A overfilled")
    require(validator["decision"]["route_B_executed_now"] is False, "Route B overexecuted")

    closed = routeb["closed_support"]
    require(closed["selected_basis_independence_closed"] is True, "closed support basis")
    require(closed["route_B_all_other_strict_fields_closed"] is True, "closed support routeB")
    require(closed["primitive_source_theorem_template_emitted"] is True, "closed support template")
    remaining = routeb["remaining_routeB_theorem"]
    require(remaining["name"] == "SelectedPrimitiveKernelSourceTheorem", "remaining theorem name")
    require(remaining["status"] == "STRICT_TEMPLATE_READY_NOT_PROVED", "remaining theorem status")
    must = remaining["must_prove"]
    require(must["selected_basis_feeds_row_functions"] is False, "basis rows overproved")
    require(must["selected_phase_shift_variation_operators_pre_residual"] is False, "variation ops overproved")
    require(must["selected_hessian_counterterm_source"] is False, "hessian source overproved")
    require(must["no_residual_projector_replay_used_as_source"] is False, "residual source overproved")
    require(routeb["route_B_promoted_now"] is False, "routeb packet promoted")
    require(routeb["source_independence_closed"] is False, "routeb packet source independence")

    require(anti["is_cycle"] is False, "cycle detected")
    require(anti["newly_closed_or_sharpened"]["broad_RouteB_run_replaced_by_named_primitive_kernel_source_theorem"] is True, "frontier not sharpened")
    require("B29 imports a strict validator" in anti["why_not_cycle"][1], "anti-cycle explanation")

    require(boundary["advanced_now"]["RouteB_selected_basis_independence_closed"] is True, "boundary basis")
    require(boundary["advanced_now"]["RouteB_all_other_strict_fields_closed"] is True, "boundary routeB")
    require(boundary["still_open"]["primitive_kernel_source_theorem"] is True, "boundary primitive theorem open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "boundary weak angle open")

    require(cert["status"] == STATUS, "cert status")
    require(cert["anti_cycle_confirmed"] is True, "cert anti-cycle")
    require(cert["route_B_promoted_now"] is False, "cert Route B")
    require(cert["source_independence_closed"] is False, "cert source independence")
    require(cert["physical_weak_angle_closure"] is False, "cert weak angle")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B30-PRIMITIVE-KERNEL-SOURCE-THEOREM", "next primary")
    require("Not A Cycle" in note, "note missing anti-cycle")

    print("CONST-EW-02 B29 Route-B final source-theorem frontier audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
