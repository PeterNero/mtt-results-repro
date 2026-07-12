"""Audit const_ew_02_weak_mixing_b6_kew_kernel_gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_ew_02_weak_mixing_b6_kew_kernel_gate"
CANDIDATE = DATA / "const_ew_02_weak_mixing_b6_kew_kernel_gate.candidate.json"
IMPORTS = BASE / "kernel_imports.packet.json"
KERNEL = BASE / "kew_kernel_contract.packet.json"
PROJECTION = BASE / "exceptional_projection_gate.packet.json"
SOURCE_GAP = BASE / "source_gap_and_next_work.packet.json"
CERT = ROOT / "certificates" / "const_ew_02_weak_mixing_b6_kew_kernel_gate_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B6_KEWKernelGate_v1.md"
BUILD = ROOT / "scripts" / "build_const_ew_02_weak_mixing_b6_kew_kernel_gate.py"
STATUS = "MTT_CONST_EW_02_B6_KEW_KERNEL_GATE_BUILT_PROJECTION_CLOSED_VALUES_OPEN"


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
    kernel = load(KERNEL)
    projection = load(PROJECTION)
    source_gap = load(SOURCE_GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["what_closes_now"]["K_EW_interface"] is True, "K_EW interface not closed")
    require(candidate["what_closes_now"]["exceptional_projection_basis_and_formula"] is True, "projection not closed")
    require(candidate["what_remains_open"]["T1_T2_or_c1_c2_source_coefficients"] is True, "coefficients closed too early")
    require(candidate["what_remains_open"]["effective_kappa_l_profile"] is True, "effective profile closed too early")

    require(imports["status"] == "KERNEL_IMPORTS_ACCEPTED_WITH_VALUE_BOUNDARY", "imports status mismatch")
    require(all(imports["import_checks"].values()), "one or more import checks failed")

    require(kernel["status"] == "K_EW_CONTRACT_BUILT_VALUES_OPEN", "kernel status mismatch")
    require(kernel["kernel_shape"]["required_map"] == "K_EW(selected MTT branch) -> (mu_Theta, x, T1, T2, scheme)", "kernel map mismatch")
    require(approx(kernel["kernel_shape"]["ratio_edge"]["high_scale_tree_sin2"], 0.2515877565744274), "tree sin2 mismatch")
    require(kernel["not_source_selected_yet"]["kappa_EW"] is True, "kappa closed too early")
    require("choosing Delta_sel to match sin^2(theta_W)" in kernel["forbidden"], "forbidden Delta fit missing")

    require(projection["status"] == "EXCEPTIONAL_PROJECTION_ALGEBRA_CLOSED_COEFFICIENTS_OPEN", "projection status mismatch")
    require(projection["promotion_tests"]["trace_free_exceptional_plane_closed"] is True, "trace-free plane not closed")
    require(projection["promotion_tests"]["basis_projection_formula_closed"] is True, "basis formula not closed")
    require(projection["promotion_tests"]["execution_i_coefficients_source_selected"] is False, "diagnostic coefficients overpromoted")
    require(projection["verdict"]["projection_algebra_promoted"] is True, "projection algebra not promoted")
    require(projection["verdict"]["numeric_coefficients_promoted"] is False, "numeric coefficients overpromoted")
    require(approx(projection["diagnostic_execution_i_coefficients"]["Delta_G_12_split_recomputed"], projection["diagnostic_execution_i_coefficients"]["Delta_G_12_split"]), "Delta_G recompute mismatch")

    require(source_gap["status"] == "EXACT_SOURCE_GAP_IDENTIFIED", "source gap status mismatch")
    require(source_gap["next_primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B7-LOCAL-COEFFICIENT-SOURCE", "next primary mismatch")
    require("2*c1-c2" in source_gap["best_current_clue"], "best clue missing")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["projection_algebra_closed"] is True, "cert projection missing")
    require(cert["execution_i_c1_c2_promoted"] is False, "cert c1/c2 overclaim")
    require(cert["low_scale_electroweak_closure"] is False, "cert low-scale overclaim")
    require(cert["physical_sin2thetaW_value_claimed"] is False, "cert physical angle overclaim")
    require("B7-LOCAL-COEFFICIENT-SOURCE" in note, "note next label missing")
    require("not promoted as a no-knob prediction" in note, "note boundary missing")

    for packet in [candidate, imports, kernel, projection, source_gap, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
