"""Audit const_em_01_alpha1_universal_primitive_or_nogo."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_universal_primitive_or_nogo"
CANDIDATE = DATA / "const_em_01_alpha1_universal_primitive_or_nogo.candidate.json"
PRIMITIVE = BASE / "one_universal_primitive.packet.json"
NOGO = BASE / "strict_internal_nogo.packet.json"
VERDICT = BASE / "two_path_verdict.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_universal_primitive_or_nogo_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_UniversalPrimitiveOrNoGo_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_universal_primitive_or_nogo.py"
STATUS = "MTT_CONST_EM_01_A10_PRIMITIVE_EXTENSION_READY_STRICT_NOGO_CERTIFIED"


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
    primitive = load(PRIMITIVE)
    nogo = load(NOGO)
    verdict = load(VERDICT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["what_closes_now"]["strict_current_corpus_nogo"] is True, "strict no-go not closed")
    require(candidate["what_closes_now"]["one_universal_primitive_extension"] is True, "primitive extension not closed")
    require(candidate["what_closes_now"]["policy_separation"] is True, "policy separation missing")
    require(candidate["what_remains_open"]["strict_no_knob_alpha_phys"] is True, "strict alpha closed too early")

    require(primitive["status"] == "ONE_UNIVERSAL_PRIMITIVE_EXTENSION_READY", "primitive status mismatch")
    require(primitive["status_relative_to_no_knob"] == "NOT_STRICT_NO_KNOB_CLOSURE", "primitive no-knob guard missing")
    require("declared exactly once as a universal primitive" in primitive["acceptance_policy"]["allowed_if"], "primitive declaration rule missing")
    require(any("alpha_EM" in item for item in primitive["acceptance_policy"]["forbidden_if"]), "observed alpha guard missing")
    require(close(primitive["numeric_internal_coefficients"]["tau_int"], math.log(448) / 15), "primitive tau mismatch")

    require(nogo["status"] == "STRICT_INTERNAL_ABSOLUTE_ALPHA_PHYS_NOGO_CERTIFIED_FOR_CURRENT_CORPUS", "nogo status mismatch")
    require(nogo["premises"]["absolute_L0_E0_value_absent"] is True, "nogo missing value premise")
    require(nogo["logical_boundary"]["proves_current_corpus_no_go"] is True, "current no-go not certified")
    require(nogo["logical_boundary"]["does_not_prove_future_impossibility"] is True, "future impossibility overclaimed")
    require(any("internal alpha_int=1" in item for item in nogo["forbidden_shortcuts"]), "internal alpha shortcut guard missing")

    require(all(verdict["source_checks"].values()), "source check failed")
    require(verdict["path_A_strict_no_knob"]["verdict"] == "NO_GO_FOR_CURRENT_CORPUS", "path A verdict mismatch")
    require(verdict["path_B_one_universal_primitive"]["verdict"] == "READY_AS_EXTENSION", "path B verdict mismatch")
    require("not as no-knob proof" in verdict["path_B_one_universal_primitive"]["credibility"], "path B credibility guard missing")

    require(cert["strict_current_corpus_nogo"] is True, "cert no-go missing")
    require(cert["one_universal_primitive_extension_ready"] is True, "cert primitive missing")
    require(cert["strict_no_knob_alpha_phys_claimed"] is False, "cert strict alpha overclaim")
    require("It is not strict no-knob closure." in note, "note guard missing")

    for packet in [candidate, primitive, nogo, verdict, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
