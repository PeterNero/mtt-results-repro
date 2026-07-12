"""Audit CONST-EW-02 B38 actual proof/fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b38_actual_proof_fill_attempt"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
ROUTE_A = BASE / "route_a_physical_action_identity_actual_attempt.packet.json"
ROUTE_B = BASE / "route_b_independent_payload_actual_fill_attempt.packet.json"
LOCAL = BASE / "local_principle_conditional_closure_boundary.packet.json"
NOGO = BASE / "unpatched_current_material_no_go.packet.json"
BOUNDARY = BASE / "weak_mixing_b38_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B38_ActualProofFillAttempt_v1.md"

STATUS = "MTT_CONST_EW_02_B38_ACTUAL_PROOF_FILL_ATTEMPT_BUILT_DECISIVE_NOGO"


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
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    local = load(LOCAL)
    nogo = load(NOGO)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("route_a", route_a),
        ("route_b", route_b),
        ("local", local),
        ("nogo", nogo),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["Route_A_actual_unpatched_proof_closed"] is False, "Route A overclosed")
    require(candidate["Route_A_local_principle_conditional_kernel_closed"] is True, "local close missing")
    require(candidate["Route_B_actual_independent_payload_fill_closed"] is False, "Route B overclosed")
    require(candidate["typed_row_functor_sublemma_proved"] is True, "typed functor missing")
    require(candidate["closed_support_not_enough_countermodel"] is True, "countermodel missing")
    require(candidate["current_material_no_go_for_unpatched_B38"] is True, "no-go missing")
    require(candidate["source_promotion_closed_now"] is False, "source promotion overclosed")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    require(route_a["actual_unpatched_route_A_accepts"] is False, "Route A should not accept")
    require(route_a["local_principle_accepted"] is True, "local principle should be accepted conditionally")
    require(route_a["unpatched_principle_derived_now"] is False, "unpatched principle overderived")
    require("same_source_b_selected_emission" in route_a["missing_unpatched_fields"], "missing b_selected guard")

    require(route_b["actual_current_validator_returncode"] != 0, "validator should reject")
    require(route_b["actual_route_B_accepts_now"] is False, "Route B should not accept")
    require(route_b["full_minimal_lemma_proved"] is False, "minimal lemma overproved")
    require(route_b["typed_row_functor_sublemma_proved"] is True, "typed functor")
    require(route_b["typed_row_counts"]["total_rows"] == 110, "row count")
    require(route_b["countermodel_to_support_only"]["status"] == "COUNTERMODEL_TO_DERIVING_SOURCE_PROMOTION_FROM_CLOSED_SUPPORT_ONLY", "countermodel status")
    require("independent_hessian_counterterm_source_rows" in route_b["missing_actual_independent_fields"], "hessian source guard")

    require(local["conditional_kernel_closed"] is True, "local conditional close")
    require(local["does_not_close"]["unpatched_principle_derivation"] is True, "local should not close unpatched")
    require("not as strict unpatched no-knob derivation" in local["allowed_use"], "local boundary text")

    basis = nogo["proof_basis"]
    require(basis["strict_validator_rejects_current_two_exit_packet"] is True, "no-go validator")
    require(basis["closed_support_not_enough_countermodel"] is True, "no-go countermodel")
    require(basis["full_minimal_source_promotion_lemma_proved"] is False, "no-go lemma")
    require(basis["local_principle_is_not_unpatched"] is True, "no-go local")
    require(nogo["next_kernel_required"]["kernel_name"] == "PreResidualVariationAndHessianSourceKernel", "next kernel")

    decided = boundary["closed_or_decided_now"]
    require(decided["Route_A_actual_unpatched_proof_closed"] is False, "boundary Route A")
    require(decided["Route_A_local_principle_conditional_kernel_closed"] is True, "boundary local")
    require(decided["Route_B_actual_independent_payload_fill_closed"] is False, "boundary Route B")
    require(decided["current_material_no_go_for_unpatched_B38"] is True, "boundary no-go")
    require(boundary["still_open"]["emit_PreResidualVariationAndHessianSourceKernel"] is True, "kernel should remain open")
    require("not treating local principle as unpatched proof" in boundary["anti_cycle_delta_from_B37"]["not_repeated"], "anti-cycle guard")

    require(cert["status"] == STATUS, "cert status")
    require(cert["Route_A_actual_unpatched_proof_closed"] is False, "cert Route A")
    require(cert["Route_A_local_principle_conditional_kernel_closed"] is True, "cert local")
    require(cert["Route_B_actual_independent_payload_fill_closed"] is False, "cert Route B")
    require(cert["current_material_no_go_for_unpatched_B38"] is True, "cert no-go")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B39-PRERESIDUAL-VARIATION-HESSIAN-SOURCE-KERNEL", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B39-LOCAL-WEYLVARIATION-PRINCIPLE-TIER", "next parallel")
    require("not a cycle" in note and "B39" in note, "note")

    print("CONST-EW-02 B38 actual proof/fill attempt audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
