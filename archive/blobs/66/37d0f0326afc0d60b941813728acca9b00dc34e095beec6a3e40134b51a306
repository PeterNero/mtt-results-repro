"""Audit const_ew_02_weak_mixing_angle_source_frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_ew_02_weak_mixing_angle_source_frontier"
CANDIDATE = DATA / "const_ew_02_weak_mixing_angle_source_frontier.candidate.json"
IMPORTS = BASE / "alpha1_imports.packet.json"
FORMULAE = BASE / "weak_angle_formulae.packet.json"
FRONTIER = BASE / "source_frontier.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_ew_02_weak_mixing_angle_source_frontier_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixingAngle_SourceFrontier_v1.md"
BUILD = ROOT / "scripts" / "build_const_ew_02_weak_mixing_angle_source_frontier.py"
STATUS = "MTT_CONST_EW_02_WEAK_MIXING_SOURCE_FRONTIER_BUILT_VALUE_OPEN"


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
    imports = load(IMPORTS)
    formulae = load(FORMULAE)
    frontier = load(FRONTIER)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "frontier theorem not proved")
    require(candidate["what_closes_now"]["weak_angle_selected_as_next_target"] is True, "target not selected")
    require(candidate["what_closes_now"]["internal_pY_pSU2_lambda12_imported"] is True, "internal split not imported")
    require(candidate["what_remains_open"]["numerical_sin2thetaW_prediction"] is True, "numerical angle closed too early")

    require(imports["status"] == "ALPHA1_IMPORTS_ACCEPTED_FOR_WEAK_ANGLE", "alpha1 imports not accepted")
    require(all(imports["import_checks"].values()), "one or more import checks failed")
    require(imports["scope"] == "internal weak-split and electroweak convention support only", "import scope mismatch")

    values = formulae["selected_internal_split"]
    require(approx(values["p_Y_internal"], 1.4217420994950278), "pY mismatch")
    require(approx(values["p_SU2_weaksplit"], -1.1961941178318218), "pSU2 mismatch")
    require(approx(values["lambda_12_internal"], 2.6179362173268497), "lambda mismatch")
    require(approx(values["Delta_G12_internal"], 0.08450302790361214), "Delta mismatch")
    require("tree_angle" in formulae["standard_formulae"], "tree angle missing")
    require("effective_angle" in formulae["standard_formulae"], "effective angle missing")
    require(any("not a physical coupling ratio" in item for item in formulae["why_internal_split_is_not_the_angle"]), "boundary warning missing")

    require(frontier["what_is_closed"]["no_observed_angle_selector"] is True, "selector guard missing")
    require(frontier["what_remains_open"]["same_branch_SU2_physical_normalization"] is True, "SU2 packet closed too early")
    require(frontier["what_remains_open"]["effective_angle_kappa_factor"] is True, "kappa factor closed too early")
    require(frontier["superset_strategy"]["locked_target"].startswith("sin^2"), "locked target missing")

    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B4-SU2-PHYSICAL-PACKET", "next label mismatch")
    require("backsolve A0 from measured sin^2(theta_W)" in next_work["forbidden_shortcuts"], "backsolve guard missing")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["physical_sin2thetaW_value_claimed"] is False, "cert numerical overclaim")
    require(cert["same_branch_SU2_physical_packet_closed"] is False, "cert SU2 overclaim")
    require("WEAK-MIXING / B4-SU2-PHYSICAL-PACKET" in note, "note next label missing")
    require("It does not derive a" in note, "note boundary missing")

    for packet in [candidate, imports, formulae, frontier, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
