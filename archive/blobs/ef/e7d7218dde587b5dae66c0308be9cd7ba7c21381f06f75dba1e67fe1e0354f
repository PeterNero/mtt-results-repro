"""Audit const_em_01_alpha1_internal_weaksplit_import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_internal_weaksplit_import"
CANDIDATE = DATA / "const_em_01_alpha1_internal_weaksplit_import.candidate.json"
IMPORT = BASE / "qa_internal_weaksplit_import.packet.json"
PROMOTION = BASE / "internal_threshold_promotion.packet.json"
BOUNDARY = BASE / "physical_alpha_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_internal_weaksplit_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_InternalWeakSplitImport_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_internal_weaksplit_import.py"
STATUS = "MTT_CONST_EM_01_INTERNAL_WEAKSPLIT_IMPORTED_PHYSICAL_ALPHA_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "physical/global closure overclaim")


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
    imported = load(IMPORT)
    promotion = load(PROMOTION)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["what_closes_now"]["selected_p_a_internal"] is True, "p_a internal not closed")
    require(candidate["what_closes_now"]["selected_p_Y_internal"] is True, "p_Y internal not closed")
    require(candidate["what_closes_now"]["selected_lambda_12_internal"] is True, "lambda12 internal not closed")
    require(candidate["what_closes_now"]["selected_Delta_G12_internal"] is True, "DeltaG12 internal not closed")
    require(candidate["what_remains_open"]["physical_K_gauge_or_action_unit"] is True, "physical K closed too early")
    require(candidate["what_remains_open"]["alpha_zero_or_MZ_value"] is True, "physical alpha closed too early")
    require(candidate["internal_closure_claimed"] is True, "internal closure not claimed")

    require(imported["status"] == "QA_INTERNAL_WEAKSPLIT_IMPORT_PASS", "QA import did not pass")
    require(all(imported["import_checks"].values()), "one or more QA import checks failed")
    require(imported["supersedes_prior_open_item"]["scope"] == "internal dimensionless weak-split only", "supersession scope mismatch")

    values = promotion["promoted_internal_values"]
    require(approx(values["p_a_internal"], 29.201650332199108), "p_a mismatch")
    require(approx(values["p_Y_internal"], 1.4217420994950278), "p_Y mismatch")
    require(approx(values["lambda_12_internal"], 2.6179362173268497), "lambda12 mismatch")
    require(approx(values["Delta_G12_internal"], 0.08450302790361214), "DeltaG12 mismatch")
    require(promotion["internal_closure_claimed"] is True, "promotion internal closure missing")
    require(promotion["closure_claimed"] is False, "promotion physical overclaim")

    require(boundary["closed_internal"]["lambda_12_internal"] is True, "boundary internal lambda missing")
    require(boundary["open_physical"]["physical_K_gauge_or_action_unit"] is True, "boundary physical K not open")
    require(boundary["open_physical"]["measured_electroweak_closure"] is True, "boundary measured closure not open")
    require(next_work["primary"]["label"] == "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A5-KPHYS", "next primary mismatch")

    require(approx(cert["lambda_12_internal"], 2.6179362173268497), "cert lambda mismatch")
    require(cert["physical_alpha_value_claimed"] is False, "cert alpha overclaim")
    require(cert["physical_K_gauge_anchor_closed"] is False, "cert K overclaim")
    require("lambda_12_internal = 2.6179362173268497" in note, "note lambda missing")
    require("A5-KPHYS" in note, "note next label missing")

    for packet in [candidate, imported, promotion, boundary, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
