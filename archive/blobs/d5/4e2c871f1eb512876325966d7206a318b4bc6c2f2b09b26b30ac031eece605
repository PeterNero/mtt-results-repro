from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from flint import acb


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_side_beta_defect_transport as validated
from build_selected_q79_E32_weighted_71_and_carrier_decision import coordinate_zero_exclusion


CANDIDATE = ROOT / "candidate_data" / "selected_q79heightfoursurvivore32decisions.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79heightfoursurvivore32decisions.certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    packet_path = ROOT / candidate["packet"]
    packet = load(packet_path)
    if candidate["artifact"] != "A210" or packet["artifact"] != "A210":
        raise AssertionError("A210 artifact label changed")
    if sha256(packet_path) != candidate["packet_sha256"]:
        raise AssertionError("A210 packet hash mismatch")
    if sha256(ROOT / candidate["note"]) != candidate["note_sha256"]:
        raise AssertionError("A210 proof-note hash mismatch")
    if sha256(CANDIDATE) != certificate["candidate_sha256"]:
        raise AssertionError("A210 candidate hash mismatch")
    if candidate["closure_claimed"] or certificate["closure_claimed"]:
        raise AssertionError("A210 overclaims covariant closure")

    for path_key, hash_key in (
        ("A208_survivor_queue", "A208_survivor_queue_sha256"),
        ("A209_handle_basis", "A209_handle_basis_sha256"),
        ("A207_direct_decision", "A207_direct_decision_sha256"),
        ("orientation_packet", "orientation_packet_sha256"),
        ("period_table", "period_table_sha256"),
        ("refined_beta_packet", "refined_beta_packet_sha256"),
        ("builder_source", "builder_source_sha256"),
    ):
        path = ROOT / packet["authority"][path_key]
        if sha256(path) != packet["authority"][hash_key]:
            raise AssertionError(f"A210 authority hash mismatch: {path_key}")
    for relative, digest in packet["authority"]["all_interval_authority_sha256"].items():
        if sha256(ROOT / relative) != digest:
            raise AssertionError(f"A210 interval authority hash mismatch: {relative}")

    rows = packet["candidate_decisions"]
    if len(rows) != 5 or [row["A132_objective_rank"] for row in rows] != [1, 2, 3, 4, 5]:
        raise AssertionError("A210 candidate decision order changed")
    rejected = 0
    nonseparated = 0
    for row in rows:
        residual = validated.interval_from_bounds(row["residual_interval"])
        replay = coordinate_zero_exclusion(residual)
        stored = row["coordinate_zero_exclusion"]
        if (
            replay["separating_component"] != stored["separating_component"]
            or replay["zero_excluded"] != stored["zero_excluded"]
        ):
            raise AssertionError("A210 coordinate zero-exclusion classification changed")
        for stored_bound, replay_bound in zip(
            stored["coordinate_bounds"], replay["coordinate_bounds"]
        ):
            if stored_bound["component"] != replay_bound["component"]:
                raise AssertionError("A210 coordinate bound order changed")
            if max(
                abs(float(stored_bound[key]) - float(replay_bound[key]))
                for key in ("lower", "upper")
            ) > 1.0e-9:
                raise AssertionError("A210 coordinate bound replay mismatch")
        zero_excluded = not residual.contains(acb(0)) and replay["zero_excluded"]
        if zero_excluded != row["current_aggregate_zero_excluded"]:
            raise AssertionError("A210 aggregate decision replay mismatch")
        if row["A132_objective_rank"] == 1:
            if row["rigorous_decision"] != "REJECTED_BY_A207_SHARPER_DIRECT_HANDLE_INTERVAL":
                raise AssertionError("A210 lost the A207 rejection")
        elif zero_excluded:
            if row["rigorous_decision"] != "REJECTED_BY_E32_ZERO_EXCLUSION":
                raise AssertionError("A210 survivor rejection mismatch")
            rejected += 1
        else:
            if row["rigorous_decision"] != "NOT_SEPARATED_BY_CURRENT_E32_INTERVAL":
                raise AssertionError("A210 survivor nonseparation mismatch")
            nonseparated += 1

    ledger = packet["decision_ledger"]
    if ledger["newly_rejected_survivors"] != rejected:
        raise AssertionError("A210 rejected-survivor ledger mismatch")
    if ledger["current_E32_nonseparated_survivors"] != nonseparated:
        raise AssertionError("A210 nonseparated-survivor ledger mismatch")
    if packet["scope"]["global_height_four_completeness_over_Z90_proved"]:
        raise AssertionError("A210 promotes finite-grid decisions to Z90 completeness")
    if packet["scope"]["covariant_PGL3_zero_and_Jacobian_solved"]:
        raise AssertionError("A210 promotes an E32 gate to covariant closure")

    print("q79 A210 height-four survivor E32 decision audit: PASS")
    print(f"closed: five fixed-grid aggregates, including {rejected} new survivor rejection(s)")
    print(f"open: {nonseparated} E32-nonseparated survivor(s), full eight-row covariant gate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
