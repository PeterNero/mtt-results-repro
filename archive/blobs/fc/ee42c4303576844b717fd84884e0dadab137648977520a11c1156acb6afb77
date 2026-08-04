"""Audit const_em_01_alpha1_rod_clock_source_discriminator."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_rod_clock_source_discriminator"
CANDIDATE = DATA / "const_em_01_alpha1_rod_clock_source_discriminator.candidate.json"
ROUTES = BASE / "rod_clock_route_table.packet.json"
DECISION = BASE / "decision.packet.json"
NEXT = BASE / "next_attack.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_rod_clock_source_discriminator_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_RodClockSourceDiscriminator_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_rod_clock_source_discriminator.py"
STATUS = "MTT_CONST_EM_01_ROD_CLOCK_SOURCE_DISCRIMINATOR_BUILT_STRICT_SOURCE_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def close(a: float, b: float, tol: float = 1e-14) -> bool:
    return abs(a - b) < tol


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
    routes = load(ROUTES)
    decision = load(DECISION)
    next_attack = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem did not prove source checks")
    require(candidate["what_closes_now"]["candidate_source_table"] is True, "source table not closed")
    require(candidate["what_closes_now"]["strict_no_knob_L0_E0_found"] is False, "strict L0/E0 overclaimed")
    require(candidate["what_closes_now"]["one_universal_primitive_extension_ready"] is True, "one primitive extension missing")
    require(candidate["what_remains_open"]["source_selected_L0_or_E0"] is True, "L0/E0 not open")

    require(all(routes["source_checks"].values()), "source check failed")
    require(routes["routes"]["finite_coherent_projection_tau"]["classification"] == "RELATIVE_ROLE_CLOSED_ABSOLUTE_VALUE_OPEN", "FCP route classification mismatch")
    require(routes["routes"]["central_circle_time_bookkeeping"]["classification"] == "PROMISING_SHARED_SOURCE_NOT_NUMERIC_ANCHOR", "central circle classification mismatch")
    require(routes["routes"]["m_theory_modal_gap_planck_anchor"]["classification"] == "BEST_STRUCTURAL_ROUTE_VALUE_OPEN", "M-theory classification mismatch")
    require(routes["routes"]["declared_universal_primitive"]["classification"] == "ONE_PRIMITIVE_EXTENSION_CREDIBLE_NOT_NO_KNOB", "primitive classification mismatch")
    require(routes["routes"]["observed_constant_backsolve"]["classification"] == "FORBIDDEN", "backsolve classification mismatch")

    strict = decision["strict_no_knob_result"]
    require(strict["L0_or_E0_source_selected_now"] is False, "decision overclaimed L0/E0")
    require(decision["source_promotion_now"] is False, "source promotion overclaimed")
    primitive = decision["one_universal_primitive_result"]
    require(primitive["extension_ready"] is True, "primitive extension not ready")
    require(primitive["primitive"] == "L0 or E0", "primitive mismatch")
    require("before target comparison" in primitive["credibility_condition"], "primitive guard missing")
    require(close(primitive["numeric_internal_coefficients"]["tau_int"], math.log(448) / 15), "tau mismatch")

    require(next_attack["active_label"] == "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A9-CENTRAL-CIRCLE-ROD-CLOCK-THEOREM", "next label mismatch")
    require("proof computed before comparison" in " ".join(next_attack["must_emit"]), "next no-backsolve condition missing")
    require(cert["strict_no_knob_L0_E0_found"] is False, "cert strict overclaim")
    require(cert["one_universal_primitive_extension_ready"] is True, "cert primitive missing")
    require("It is not strict no-knob closure." in note, "note no-knob guard missing")

    for packet in [candidate, routes, decision, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
