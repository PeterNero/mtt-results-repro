"""Audit const_em_01_alpha1_import_evaluation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_import_evaluation"
CANDIDATE = DATA / "const_em_01_alpha1_import_evaluation.candidate.json"
REPO_IMPORTS = BASE / "repo_imports_critical_evaluation.packet.json"
EXTERNAL = BASE / "external_sources_critical_evaluation.packet.json"
CONVENTIONS = BASE / "alpha1_convention_guardrail.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_import_evaluation_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_ImportEvaluation_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_import_evaluation.py"
STATUS = "MTT_CONST_EM_01_ALPHA1_IMPORT_EVALUATION_BUILT_VALUE_OPEN"


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
    repo_imports = load(REPO_IMPORTS)
    external = load(EXTERNAL)
    conventions = load(CONVENTIONS)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["what_closes_now"]["qa_su3_oriented_overlap_identified_as_primary_dependency"] is True, "QA dependency not identified")
    require(candidate["what_remains_open"]["replay_qa_su3_alpha1_driver_theorem"] is True, "QA replay should remain open")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")

    imports = {item["id"]: item for item in repo_imports["imports"]}
    require(imports["SM-PARITY-ALPHA1-STRENGTH-CRITERION"]["critical_verdict"] == "USABLE_AS_ACCEPTANCE_CRITERION_NOT_VALUE", "SM criterion verdict mismatch")
    require(imports["NONSM-ALPHA1-DRIVER-CLOSURE-IMPORT"]["critical_verdict"] == "POTENTIAL_SOURCE_PROOF_IMPORT_REQUIRES_QA_DEPENDENCY_REPLAY", "nonSM closure verdict mismatch")
    require(imports["QA-SU3-U1Y-ORIENTED-OVERLAP"]["critical_verdict"] == "PRIMARY_DEPENDENCY_TO_REPLAY_NEXT", "QA verdict mismatch")
    require(all(item["import_as_source_proof_now"] is False for item in repo_imports["imports"]), "source proof imported too early")

    require(len(external["sources"]) == 4, "external source count mismatch")
    require(external["sources"][0]["critical_verdict"] == "NECESSARY_CONVENTION_GUARDRAIL_NOT_SOURCE_PROOF", "PDG verdict mismatch")
    require(external["external_level_conclusion"].endswith("none can select the MTT source value."), "external conclusion mismatch")

    required = set(conventions["do_not_identify_without_map"])
    require("alpha(0) Thomson-limit fine-structure constant" in required, "alpha0 guard missing")
    require("alpha(M_Z) running electromagnetic coupling" in required, "alphaMZ guard missing")
    require("MTT source-strength coordinate alpha1" in required, "MTT alpha1 guard missing")
    require(conventions["universal_parameter_status"]["may_use_now"] is False, "universal parameter allowed too early")

    require(next_work["primary"]["label"] == "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH / A1-REPLAY-QA", "next primary mismatch")
    require(cert["value_claimed_now"] is False, "cert value overclaim")
    require("Do not identify" in note, "note convention guard missing")
    require("must replay the QA dependency" in note, "note QA replay guard missing")

    for packet in [candidate, repo_imports, external, conventions, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
