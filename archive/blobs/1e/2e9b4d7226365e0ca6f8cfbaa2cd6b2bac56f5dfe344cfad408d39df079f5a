"""Audit const_ew_02_weak_mixing_b5_a0_or_ratio_kernel_import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_ew_02_weak_mixing_b5_a0_or_ratio_kernel_import"
CANDIDATE = DATA / "const_ew_02_weak_mixing_b5_a0_or_ratio_kernel_import.candidate.json"
SEARCH = BASE / "cross_repo_source_search.packet.json"
RATIO = BASE / "theta_ratio_high_scale_packet.packet.json"
REPLAY = BASE / "sm_parity_replay_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_ew_02_weak_mixing_b5_a0_or_ratio_kernel_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B5_A0_or_RatioKernelImport_v1.md"
BUILD = ROOT / "scripts" / "build_const_ew_02_weak_mixing_b5_a0_or_ratio_kernel_import.py"
STATUS = "MTT_CONST_EW_02_B5_RATIO_EDGE_IMPORTED_HIGH_SCALE_TREE_VALUE_LOW_SCALE_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def approx(a: float, b: float, eps: float = 1e-12) -> bool:
    return abs(a - b) < eps


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    search = load(SEARCH)
    ratio = load(RATIO)
    replay = load(REPLAY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["what_closes_now"]["B4_difference_obstruction_preserved"] is True, "B4 not preserved")
    require(candidate["what_closes_now"]["Theta_ratio_edge_imported"] is True, "ratio edge not imported")
    require(candidate["what_closes_now"]["high_scale_tree_sin2_evaluated"] is True, "tree value not evaluated")
    require(candidate["what_closes_now"]["direct_threshold_import_rejected"] is True, "direct threshold not rejected")
    require(candidate["what_remains_open"]["strict_no_knob_low_scale_sin2thetaW"] is True, "low scale closed too early")
    require(candidate["what_remains_open"]["K_EW_threshold_kernel"] is True, "kernel closed too early")

    require(search["status"] == "RATIO_EDGE_FOUND_A0_STILL_OPEN", "search status mismatch")
    require(all(search["search_checks"].values()), "one or more search checks failed")
    require(search["classification"]["A0_path"] == "still open in strict no-knob lane", "A0 lane mismatch")
    require("high-scale ratio" in search["classification"]["Theta_ratio_path"], "ratio classification missing")

    require(ratio["status"] == "HIGH_SCALE_TREE_RATIO_EVALUATED_LOW_SCALE_OPEN", "ratio status mismatch")
    require(approx(ratio["ratio_source"]["value"], 0.56027), "r12 mismatch")
    require(approx(ratio["formula"]["computed_value"], 0.2515877565744274), "high-scale tree sin2 mismatch")
    require(any("B4 blocks ratio extraction" in item for item in ratio["why_this_bypasses_B4"]), "B4 explanation missing")
    require("T1 and T2 are not selected." in ratio["why_this_is_not_final_physical_closure"], "threshold boundary missing")

    require(replay["status"] == "PARITY_REPLAY_AVAILABLE_NOT_SOURCE_SELECTOR", "replay status mismatch")
    require("choose r_12 from observed sin^2(theta_W)" in replay["forbidden_use"], "selector guard missing")
    require(replay["available_replay_values"]["sm_parity_replay_present"] is True, "SM parity replay missing")

    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B6-K_EW-KERNEL", "next primary mismatch")
    require("exceptional/local/representation-sensitive" in next_work["most_promising_clue"], "clue missing")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(approx(cert["r_12"], 0.56027), "cert r12 mismatch")
    require(cert["physical_sin2thetaW_value_claimed"] is False, "cert physical overclaim")
    require(cert["low_scale_electroweak_closure"] is False, "cert low-scale overclaim")
    require("Theta ratio" in note, "note ratio lane missing")
    require("B6-K_EW-KERNEL" in note, "note next label missing")

    for packet in [candidate, search, ratio, replay, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
