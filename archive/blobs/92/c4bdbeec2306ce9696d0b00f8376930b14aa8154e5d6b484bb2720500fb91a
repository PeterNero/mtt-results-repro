"""Audit CONST-EW-02 B30 source-identity two-exit reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b30_source_identity_two_exit_reduction"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
CONDITIONAL = BASE / "conditional_superset_validator_import.packet.json"
GATE = BASE / "finite_c1_source_identity_gate_import.packet.json"
TWO_EXIT = BASE / "two_exit_noncycle_frontier.packet.json"
BOUNDARY = BASE / "weak_mixing_b30_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B30_SourceIdentityTwoExitReduction_v1.md"

STATUS = "MTT_CONST_EW_02_B30_SOURCE_IDENTITY_TWO_EXIT_REDUCTION_BUILT"


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
    conditional = load(CONDITIONAL)
    gate = load(GATE)
    two_exit = load(TWO_EXIT)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("conditional", conditional),
        ("gate", gate),
        ("two_exit", two_exit),
        ("boundary", boundary),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["conditional_superset_RouteB_validator_passes"] is True, "conditional validator should pass")
    require(candidate["unpatched_RouteB_validator_passes"] is False, "unpatched Route B overclosed")
    require(candidate["finite_C1_source_identity_gate_imported"] is True, "source identity gate missing")
    require(candidate["two_legal_finishing_routes_locked"] is True, "two exits not locked")
    require(candidate["anti_cycle_confirmed"] is True, "anti-cycle not confirmed")
    require(candidate["source_identity_proved_now"] is False, "source identity overproved")
    require(candidate["honest_kernel_export_emitted_now"] is False, "kernel export overemitted")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    superset = conditional["conditional_superset_path"]
    require(superset["validator_passes_conditionally"] is True, "conditional pass missing")
    require(superset["unpatched_routeB_validates"] is False, "unpatched condition mismatch")
    require("strict Route-B row-source validator" in superset["locked_target"], "locked target mismatch")
    require("weak-angle" in superset["locked_target"] or "observed weak" not in superset["locked_target"], "bad target")

    require(gate["theorem_name"] == "SelectedFiniteC1SourceIdentityTheorem", "gate theorem name")
    require(gate["current_route_A_accepts"] is False, "Route A overaccepted")
    require(gate["current_route_B_accepts"] is False, "Route B overaccepted")
    clauses = gate["clause_status"]
    require(clauses["selected_transported_bases_feed_all_72_primitive_row_kernels"]["status"] == "PARTIAL", "basis clause status")
    require(clauses["no_residual_projector_replay_as_source_provenance"]["status"] == "OPEN", "residual provenance status")
    require(clauses["same_source_R_Z_R_X_b_selected_emission"]["status"] == "OPEN", "same-source status")

    exits = two_exit["new_B30_frontier"]
    require(exits["exit_1"]["artifact"] == "SelectedFiniteC1SourceIdentityTheorem", "exit 1 artifact")
    require("R_Z/R_X" in " ".join(exits["exit_1"]["must_prove"]), "exit 1 missing RZ/RX")
    require(exits["exit_2"]["artifact"] == "Independent selected finite C1 kernel/quadrature export", "exit 2 artifact")
    require("72 primitive row values with source ids" in exits["exit_2"]["must_emit"], "exit 2 rows")
    require("not another 72-row value replay" in two_exit["anti_cycle_delta_from_B29"]["not_repeated"], "anti-cycle not specific")
    require("repeat B27-B29 row replay without new source identity or independent row provenance" in two_exit["forbidden_next_moves"], "forbidden loop missing")

    require(boundary["closed_or_sharpened_now"]["conditional_superset_RouteB_validator_pass_imported"] is True, "boundary conditional")
    require(boundary["still_open"]["SelectedFiniteC1SourceIdentityTheorem_unpatched"] is True, "source identity should remain open")
    require(boundary["still_open"]["honest_independent_finite_C1_kernel_export"] is True, "kernel export should remain open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "weak angle should remain open")

    require(cert["status"] == STATUS, "cert status")
    require(cert["conditional_superset_RouteB_validator_passes"] is True, "cert conditional")
    require(cert["unpatched_RouteB_validator_passes"] is False, "cert unpatched")
    require(cert["source_identity_proved_now"] is False, "cert source identity")
    require(cert["honest_kernel_export_emitted_now"] is False, "cert kernel export")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B31-SOURCE-IDENTITY-CLAUSE-PROOF", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B31-HONEST-KERNEL-EXPORT", "next parallel")
    require("Not A Cycle" in note, "note missing anti-cycle")
    require("Two Legal Exits" in note, "note missing exits")

    print("CONST-EW-02 B30 source-identity two-exit reduction audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
