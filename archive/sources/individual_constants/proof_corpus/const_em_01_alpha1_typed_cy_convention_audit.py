"""Audit const_em_01_alpha1_typed_cy_convention."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_typed_cy_convention"
CANDIDATE = DATA / "const_em_01_alpha1_typed_cy_convention.candidate.json"
TYPED_MAP = BASE / "typed_hypercharge_map.packet.json"
CY_DECISION = BASE / "cy_promotion_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_typed_cy_convention_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_TypedCYConvention_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_typed_cy_convention.py"
STATUS = "MTT_CONST_EM_01_TYPED_CY_CONVENTION_STRUCTURAL_MAP_CLOSED_CY_VALUE_OPEN"


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
    typed = load(TYPED_MAP)
    decision = load(CY_DECISION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["what_closes_now"]["typed_hypercharge_structural_map"] is True, "typed map not closed")
    require(candidate["what_closes_now"]["pY_equals_pa_over_36_plus_pc_over_4"] is True, "pY map not closed")
    require(candidate["what_closes_now"]["internal_index_direct_CY_shortcut_rejected"] is True, "index shortcut not rejected")
    require(candidate["what_closes_now"]["quotient_logdet_direct_pY_shortcut_rejected"] is True, "logdet shortcut not rejected")
    require(candidate["what_remains_open"]["C_Y_value"] is True, "C_Y closed too early")
    require(candidate["what_remains_open"]["factorized_operator_source_emission"] is True, "factorized operator source closed too early")

    closed_map = typed["closed_structural_map"]
    require(closed_map["hypercharge_embedding"] == "Y = (1/6) Q_a - (1/2) Q_c", "hypercharge embedding mismatch")
    require(closed_map["threshold_combination"] == "p_Y = (1/36) p_a + (1/4) p_c", "threshold combination mismatch")
    require(closed_map["weak_split"] == "lambda_12 = p_Y - p_SU2", "weak split mismatch")
    require(typed["imports"]["qa_typed_hypercharge_gate"]["lambda_12_closed"] is False, "lambda12 closed too early")
    require(typed["route_tests"]["direct_U1Y_row_shortcut"]["accepted"] is False, "direct U1Y shortcut accepted")
    require(typed["route_tests"]["Qa_stack_interpretation_of_quotient_operator"]["accepted"] is False, "quotient p_a accepted too early")

    closed_now = decision["closed_now"]
    open_now = decision["open_now"]
    require(closed_now["typed_hypercharge_structural_map"] is True, "decision typed map not closed")
    require(closed_now["reject_internal_index_as_direct_CY"] is True, "decision index rejection missing")
    require(open_now["physical_CY"] is True, "decision physical CY not open")
    require(open_now["lambda_12"] is True, "decision lambda12 not open")
    require(decision["typed_CY_options"]["internal_index_option"]["decision"] == "REJECT_AS_DIRECT_COUPLING_MULTIPLIER", "internal option verdict mismatch")
    require(decision["typed_CY_options"]["quotient_logdet_option"]["decision"] == "CONDITIONAL_AS_QA_STACK_P_A_ONLY", "logdet option verdict mismatch")

    require(next_work["primary"]["label"] == "CONST-EM-01 / ALPHA1-U1Y-ROW / A5-FACTORIZED-OPERATOR-SOURCE", "next primary mismatch")
    require(cert["typed_hypercharge_structural_map_closed"] is True, "cert typed map mismatch")
    require(cert["C_Y_value_claimed"] is False, "cert CY overclaim")
    require(cert["physical_alpha_value_claimed"] is False, "cert alpha overclaim")
    require("p_Y = p_a/36 + p_c/4" in note, "note missing pY formula")
    require("A5-FACTORIZED-OPERATOR-SOURCE" in note, "note next label missing")

    for packet in [candidate, typed, decision, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
