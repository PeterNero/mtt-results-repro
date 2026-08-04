"""Audit CONST-EW-02 B31 clause-proof and row-packet frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b31_clauseproof_and_rowpacket_frontier"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
TRACE = BASE / "trace_assembly_subclause_import.packet.json"
PROMOTION = BASE / "strict_promotion_rejection_import.packet.json"
ROWPACKET = BASE / "honest_rowpacket_template_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b31_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B31_ClauseProofAndRowPacketFrontier_v1.md"

STATUS = "MTT_CONST_EW_02_B31_CLAUSEPROOF_AND_ROWPACKET_FRONTIER_BUILT"


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
    trace = load(TRACE)
    promotion = load(PROMOTION)
    rowpacket = load(ROWPACKET)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("trace", trace),
        ("promotion", promotion),
        ("rowpacket", rowpacket),
        ("boundary", boundary),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["trace_assembly_subclause_closed"] is True, "trace subclause")
    require(candidate["strict_promotion_validator_ok"] is False, "validator overaccepted")
    require(candidate["source_identity_theorem_proved_now"] is False, "source identity overproved")
    require(candidate["new_independent_row_packet_emitted_now"] is False, "row packet overemitted")
    require(candidate["minimal_remaining_payload_locked"] is True, "minimal payload not locked")
    require(candidate["anti_cycle_confirmed"] is True, "anti-cycle")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    closed = trace["closed_subclaim"]
    require(closed["finite_measure_equals_normalized_trace"] is True, "finite measure")
    require(closed["formal_110_rows_executed"] is True, "formal 110")
    require(closed["sector_rows_assembled_formally"] is True, "sector assembly")
    require(closed["hessian_source_rows_assembled_formally"] is True, "hessian assembly")
    require(trace["not_closed_subclaim"]["sector_rows_physical_source_promoted"] is False, "sector source overpromoted")
    require(trace["not_closed_subclaim"]["hessian_source_rows_physical_source_promoted"] is False, "hessian source overpromoted")
    require(trace["source_identity_theorem_proved"] is False, "trace packet source identity")

    require(promotion["strict_validator_ok"] is False, "promotion validator")
    require(promotion["source_identity_theorem_proved"] is False, "promotion source identity")
    require(promotion["new_independent_row_packet_emitted"] is False, "promotion row packet")
    require(promotion["route_A_current"]["physical_phifin_c1_action_emitted"] is False, "Route A overemitted")
    require(promotion["route_A_current"]["same_source_b_selected_emitted"] is False, "b overemitted")
    require(promotion["route_B_current"]["all_72_primitive_rows_executed"] is True, "Route B rows missing")
    require(promotion["route_B_current"]["source_independent_of_residual_projector_replay"] is False, "Route B source overclosed")

    support = rowpacket["current_postcheck_support"]
    require(support["primitive_rows_available"] == 72, "primitive count")
    require(support["sector_rows_available_formally"] == 36, "sector count")
    require(support["hessian_rows_available_formally"] == 2, "hessian count")
    missing = rowpacket["missing_for_export"]
    require(missing["primitive_source_integral_or_formula_independent"] is True, "primitive source gap")
    require(missing["same_source_b_selected_derivation"] is True, "b source gap")
    require(missing["residual_projector_replay_excluded_as_source"] is False, "residual exclusion overclosed")
    require(missing["selected_source_identity_emitted"] is False, "source identity emitted")

    require(boundary["closed_or_sharpened_now"]["finite_trace_measure_equals_normalized_trace"] is True, "boundary measure")
    require(boundary["still_open"]["same_branch_phifin_c1_source_emission"] is True, "boundary Route A")
    require(boundary["still_open"]["new_independent_selected_row_packet"] is True, "boundary row packet")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "boundary weak angle")
    require("not another B27-B29 row replay" in boundary["anti_cycle_delta_from_B30"]["not_repeated"], "anti-cycle repeat guard")

    require(cert["status"] == STATUS, "cert status")
    require(cert["trace_assembly_subclause_closed"] is True, "cert trace")
    require(cert["strict_promotion_validator_ok"] is False, "cert validator")
    require(cert["source_identity_theorem_proved_now"] is False, "cert source identity")
    require(cert["new_independent_row_packet_emitted_now"] is False, "cert row packet")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B32-SAMESOURCE-PHIFIN-B-EMISSION", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B32-ACTUAL-INDEPENDENT-ROWPACKET", "next parallel")
    require("Not A Cycle" in note, "note missing anti-cycle")
    require("Closed Now" in note, "note missing closed section")

    print("CONST-EW-02 B31 clause-proof and row-packet frontier audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
