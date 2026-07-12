"""Audit const_em_01_alpha1_qa_replay."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_qa_replay"
CANDIDATE = DATA / "const_em_01_alpha1_qa_replay.candidate.json"
QA_REPLAY = BASE / "qa_dependency_replay.packet.json"
SOURCE_DECISION = BASE / "alpha1_source_side_closure_decision.packet.json"
CONVENTION = BASE / "alpha_convention_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_qa_replay_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_QAReplay_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_qa_replay.py"
STATUS = "MTT_CONST_EM_01_ALPHA1_QA_REPLAY_ACCEPTED_SOURCE_SIDE_DRIVER_CLOSED_CONVENTION_MAP_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def global_guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "physical/global closure overclaim")


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
    qa_replay = load(QA_REPLAY)
    source = load(SOURCE_DECISION)
    convention = load(CONVENTION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["what_closes_now"]["qa_su3_alpha1_driver_theorem_replayed"] is True, "QA theorem not replayed")
    require(candidate["what_closes_now"]["source_side_alpha1_driver_accepted_here"] is True, "source-side driver not accepted")
    require(candidate["what_closes_now"]["selected_N_alpha1_h_ext_value"] is True, "unit source value not accepted")
    require(candidate["what_closes_now"]["du_dalpha1_equals_h_ext"] is True, "du/dalpha1 not accepted")
    require(candidate["what_remains_open"]["physical_alpha_zero_or_MZ_value"] is True, "physical alpha closed too early")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["source_side_closure_claimed"] is True, "source-side closure flag missing")

    require(qa_replay["status"] == "QA_REPLAY_DEPENDENCIES_PASS", "QA dependency replay did not pass")
    require(all(item["passed"] for item in qa_replay["audit_results"]), "at least one QA audit failed")
    require(all(qa_replay["dependency_checks"].values()), "at least one dependency check failed")
    require(all(item["guardrail_ok"] for item in qa_replay["qa_candidates"].values()), "QA guardrail failure")

    decision = source["decision"]
    require(decision["source_side_alpha1_driver_accepted_here"] is True, "source decision not accepted")
    require(decision["N_alpha1_h_ext"] == 1.0, "N alpha1 value mismatch")
    require(decision["lambda_alpha1"] == 1.0, "lambda alpha1 value mismatch")
    require(decision["physical_alpha_value_claimed"] is False, "physical alpha overclaim")
    require(decision["alpha_zero_or_MZ_claimed"] is False, "alpha0/MZ overclaim")
    require(decision["GUT_normalized_alpha1_claimed"] is False, "GUT alpha1 overclaim")
    require(decision["universal_parameter_selected"] is False, "universal parameter selected too early")
    require(source["residual_open"]["alpha_convention_map"] is True, "convention map closed too early")

    require(convention["status"] == "ALPHA_CONVENTION_MAP_STILL_OPEN", "convention status mismatch")
    require("alpha(0)" in convention["not_yet_identified_with"], "alpha(0) boundary missing")
    require("alpha(M_Z)" in convention["not_yet_identified_with"], "alpha(MZ) boundary missing")
    require("GUT-normalized alpha_1=(5/3)alpha_Y" in convention["not_yet_identified_with"], "GUT boundary missing")
    require(next_work["primary"]["label"] == "CONST-EM-01 / ALPHA1-CONVENTION / A2-MAP", "next label mismatch")

    require(cert["source_side_alpha1_driver_accepted_here"] is True, "certificate source-side flag mismatch")
    require(cert["physical_alpha_value_claimed"] is False, "certificate physical alpha overclaim")
    require(cert["universal_parameter_selected"] is False, "certificate universal parameter overclaim")
    require("source-side" in note, "note lacks source-side scope")
    require("not yet" in note, "note lacks open-boundary language")
    require("CONVENTION / A2-MAP" in note, "note lacks next label")

    for packet in [candidate, qa_replay, source, convention, cert]:
        global_guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
