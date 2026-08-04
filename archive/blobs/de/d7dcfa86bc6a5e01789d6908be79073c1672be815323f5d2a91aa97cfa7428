"""Audit const_em_01_alpha1_kphys_source_hunt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_kphys_source_hunt"
CANDIDATE = DATA / "const_em_01_alpha1_kphys_source_hunt.candidate.json"
ANCHORS = BASE / "physical_anchor_imports.packet.json"
REDUCTION = BASE / "kphys_reduction.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_kphys_source_hunt_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_KPhysSourceHunt_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_kphys_source_hunt.py"
STATUS = "MTT_CONST_EM_01_KPHYS_SOURCE_HUNT_REDUCED_TO_ALPHA_PHYS_ANCHOR_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


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
    anchors = load(ANCHORS)
    reduction = load(REDUCTION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["what_closes_now"]["physical_anchor_search_executed"] is True, "search not executed")
    require(candidate["what_closes_now"]["K_phys_reduced_to_alpha_phys_or_action_unit"] is True, "K reduction missing")
    require(candidate["what_remains_open"]["K_phys_value"] is True, "K_phys closed too early")
    require(candidate["what_remains_open"]["alpha_phys_value"] is True, "alpha_phys closed too early")
    require(all(anchors["import_checks"].values()), "anchor import check failed")

    phys = reduction["physical_anchor_reduction"]
    require(phys["best_structural_route"] == "m_theory_modal_gap_planck_anchor", "best route mismatch")
    require(phys["single_remaining_anchor"] == "alpha_phys or equivalent physical inverse-length/action unit", "anchor reduction mismatch")
    require(abs(phys["Omega0_over_sqrt_alpha_phys"] - 1.5675093859261626) < 1e-15, "Omega0 coefficient mismatch")
    require(reduction["open"]["K_phys"] is True, "K_phys not open")
    require(reduction["open"]["alpha_phys"] is True, "alpha_phys not open")
    require(next_work["primary"]["label"] == "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A6-DIMENSIONAL-ANCHOR-PACKET", "next primary mismatch")

    require(cert["K_phys_value_claimed"] is False, "cert K overclaim")
    require(cert["alpha_phys_value_claimed"] is False, "cert alpha_phys overclaim")
    require(cert["physical_alpha_value_claimed"] is False, "cert physical alpha overclaim")
    require("Omega0/sqrt(alpha_phys) = 1.5675093859261626" in note, "note Omega coefficient missing")
    require("A6-DIMENSIONAL-ANCHOR-PACKET" in note, "note next label missing")

    for packet in [candidate, anchors, reduction, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
