"""Audit Route A RZ/RX/b emission or Route B first-row execution attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_rzrxb_source_emission_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_first_primitive_row_execution_attempt.packet.json"
DECISION = PACKET_DIR / "source_gap_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalRZRXBSourceEmission_or_PrimitiveRowFirstExecution_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution.py"

STATUS = "MTT_SELECTED_PHYSICALRZRXBSOURCEEMISSION_OR_PRIMITIVEROWFIRSTEXECUTION_ATTEMPTED_SUPPORT_ONLY"
NEXT = "MTT_Selected_PhysicalActionSourceRule_or_IndependentPrimitiveKernelFormula_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require("source promotion, not value search" in note, "note misses source-gap conclusion")

    require(route_a["status"] == "RZ_RX_B_VALUES_READY_PHYSICAL_SOURCE_EMISSION_NOT_PROVED", "Route A status mismatch")
    require(route_a["canonical_R_Z_support"]["available"] is True, "R_Z support missing")
    require(route_a["canonical_R_X_support"]["available"] is True, "R_X support missing")
    require(route_a["canonical_R_Z_support"]["norm_sq"] == 4.0, "R_Z norm mismatch")
    require(route_a["canonical_R_X_support"]["norm_sq"] == 2.0, "R_X norm mismatch")
    require(route_a["b_selected_support"]["A_transpose_b"] == [12.0, 12.0], "b support mismatch")
    require(route_a["b_selected_support"]["same_source_emitted"] is False, "b overemitted")
    require(route_a["same_source_physical_R_Z_emitted"] is False, "R_Z overemitted")
    require(route_a["same_source_physical_R_X_emitted"] is False, "R_X overemitted")
    require(route_a["same_source_physical_b_selected_emitted"] is False, "b_selected overemitted")
    require(route_a["physical_action_restriction_emitted"] is False, "action restriction overemitted")
    require(route_a["no_extra_boundary_or_source_emitted"] is False, "boundary overemitted")
    require(route_a["route_a_closed_now"] is False, "Route A overclosed")

    require(route_b["status"] == "FIRST_PRIMITIVE_ROW_REHEARSED_FROM_ALGEBRAIC_SUPPORT_NOT_INDEPENDENTLY_EXECUTED", "Route B status mismatch")
    require(route_b["row_id"] == "u:phase:r0c0", "first row mismatch")
    require(route_b["sector"] == "u", "first row sector mismatch")
    require(route_b["response"] == "phase", "first row response mismatch")
    require(route_b["matrix_coordinate"] == {"row": 0, "column": 0}, "first row coordinate mismatch")
    require(abs(route_b["algebraic_support_value"] - (4.0 / 3.0)) < 1e-12, "first row value mismatch")
    require(route_b["value_source"] == "R_Z", "first row source mismatch")
    require(route_b["filled_as_algebraic_candidate"] is True, "first row algebraic support missing")
    require(route_b["independent_quadrature_emitted"] is False, "first row independent quadrature overemitted")
    require(route_b["physical_source_promoted"] is False, "first row physical source overpromoted")
    require(route_b["selected_primitive_kernel_formula"] is None, "primitive formula overfilled")
    require(route_b["selected_trace_or_pairing_source"] is None, "pairing source overfilled")
    require(route_b["exactness_or_error_bound_certificate"] is None, "exactness cert overfilled")
    require(route_b["provenance_independent_of_residual_projector_replay"] is False, "provenance overfilled")
    require(route_b["first_row_independently_executed_now"] is False, "first row overexecuted")

    require(decision["status"] == "FIRST_ATTACK_FINDS_SOURCE_PROMOTION_GAP_NOT_NUMERIC_GAP", "decision status mismatch")
    require(decision["route_a_values_numerically_ready"] is True, "Route A values not ready")
    require(decision["route_a_same_source_physical_emission_closed"] is False, "Route A overclosed")
    require(decision["route_b_first_row_value_numerically_ready"] is True, "Route B value not ready")
    require(decision["route_b_first_row_independent_execution_closed"] is False, "Route B overclosed")
    require(decision["source_gap_not_numeric_gap"] is True, "source-gap conclusion missing")
    require(decision["unpatched_dynamic_C1_packet_closed"] is False, "dynamic C1 overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    for label, payload in [
        ("candidate", data),
        ("route_a", route_a),
        ("route_b", route_b),
        ("decision", decision),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
