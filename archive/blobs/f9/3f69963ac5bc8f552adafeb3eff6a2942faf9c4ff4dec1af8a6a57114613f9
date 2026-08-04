"""Audit const_em_01_alpha1_normalization_frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_normalization_frontier"
CANDIDATE = DATA / "const_em_01_alpha1_normalization_frontier.candidate.json"
IMPORTS = BASE / "cy_candidate_imports.packet.json"
SUPERSET = BASE / "superset_path_decision.packet.json"
NO_GO = BASE / "physical_cy_nogo.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_normalization_frontier_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_NormalizationFrontier_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_normalization_frontier.py"
STATUS = "MTT_CONST_EM_01_ALPHA1_NORMALIZATION_FRONTIER_BUILT_INTERNAL_INDEX_SUPPORT_PHYSICAL_CY_OPEN"


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
    imports = load(IMPORTS)
    superset = load(SUPERSET)
    no_go = load(NO_GO)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["what_closes_now"]["internal_K_gauge_int_unit_imported"] is True, "K_gauge internal unit not imported")
    require(candidate["what_closes_now"]["internal_U1_index_two_thirds_imported"] is True, "U1 index not imported")
    require(candidate["what_closes_now"]["physical_CY_no_go_proved_for_current_sources"] is True, "physical CY no-go missing")
    require(candidate["what_remains_open"]["physical_C_Y_source_to_hypercharge_multiplier"] is True, "physical CY closed too early")
    require(candidate["current_best_candidate"]["value"] == "2/3", "best candidate value mismatch")
    require(candidate["current_best_candidate"]["not_a_physical_CY"] is True, "best candidate overpromoted")

    imported = {item["id"]: item for item in imports["imports"]}
    require(imported["QA-K-GAUGE-INTERNAL-ANCHOR"]["verdict"] == "INTERNAL_INVERSE_KERNEL_NORMALIZATION_SUPPORT_NOT_PHYSICAL_CY", "K_gauge verdict mismatch")
    require(imported["QA-U1-PERP-PROJECTOR"]["verdict"] == "INTERNAL_U1_INDEX_SUPPORT", "U1 projector verdict mismatch")
    require(imported["NONSM-ELECTROWEAK-SOURCE-EXHAUSTION"]["verdict"] == "NEGATIVE_CLOSURE_GUARDRAIL", "nonSM exhaustion verdict mismatch")

    kernel = superset["combined_paths"]["internal_index_kernel"]
    require(kernel["K_gauge_int"] == "1", "K_gauge internal mismatch")
    require(kernel["I_U1"] == "2/3", "I_U1 mismatch")
    require(kernel["I_SU2"] == "1", "I_SU2 mismatch")
    require(kernel["I_Qa_or_SU3"] == "log(2008)", "I_Qa mismatch")
    require(superset["promotable_now"]["internal_inverse_kernel_U1_index"] is True, "internal U1 index not promotable")
    require(superset["promotable_now"]["physical_C_Y_coupling_multiplier"] is False, "physical CY promoted")
    require(superset["promotable_now"]["alpha_em_numeric"] is False, "alpha_em promoted")

    require(no_go["theorem"]["proved"] is True, "no-go theorem not proved")
    require("Set C_Y=2/3 directly as alpha_Y multiplier." in no_go["forbidden_shortcuts"], "2/3 shortcut not forbidden")
    require("Selected_Electroweak_U1Y_FactorizedThresholdOperator_SourceEmission_v1" == no_go["minimal_repair_objects"]["dimensionless_first"], "dimensionless repair mismatch")
    require(next_work["primary"]["label"] == "CONST-EM-01 / ALPHA1-NORMALIZATION / A4-TYPED-CY-CONVENTION", "next primary mismatch")

    require(cert["internal_U1_index_support_value"] == "2/3", "cert U1 index mismatch")
    require(cert["physical_CY_claimed"] is False, "cert physical CY overclaim")
    require(cert["selected_universal_parameters_now"] == 0, "universal parameter selected")
    require("Do not set `C_Y=2/3`" in note, "note missing 2/3 shortcut guard")
    require("A4-TYPED-CY-CONVENTION" in note, "note next label missing")

    for packet in [candidate, imports, superset, no_go, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
