"""Audit current execution for precision profile values or Qa/SU3 operator payload."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_precisionprofileloopvalues_or_actualqasu3operatorpayload_currentexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_precision_profile_loop_execution.packet.json"
ROUTE_B = PACKET_DIR / "route_b_qasu3_hym_operator_execution.packet.json"
DECISION = PACKET_DIR / "current_execution_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrecisionProfileLoopValues_or_ActualQaSU3OperatorPayload_CurrentExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PRECISIONPROFILELOOPVALUES_OR_ACTUALQASU3OPERATORPAYLOAD_CURRENTEXECUTION_BUILT_BOTH_ROUTES_OPEN"
NEXT = "MTT_Selected_LocalQFTPrecisionObservableTable_or_QaSU3HYMOperatorPacket_ValueAttempt_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


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
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(route_a["available_now"]["external_literature_RG_values"] is True, "Route A missing external RG rows")
    require(route_a["available_now"]["hypercharge_basis_reduction"] is True, "Route A missing basis reduction")
    require(route_a["available_now"]["correlation_robust_profile_envelope"] is True, "Route A missing profile envelope")
    require(route_a["available_now"]["representative_tree_level_decay_rows"] is True, "Route A missing tree QFT rows")
    require(route_a["available_now"]["finite_nonnegative_decay_widths"] is True, "Route A missing finite widths")
    for key in [
        "published_or_reconstructed_correlated_profile_values",
        "local_QFT_observable_value_rows",
        "loop_corrected_local_QFT_correlator_smatrix_decay_rows",
        "multi_loop_threshold_convention_values",
    ]:
        require(route_a["missing_for_true_equivalence"][key] is True, f"Route A missing open gate: {key}")
    require(route_a["execution_result"]["route_attempted"] is True, "Route A not attempted")
    require(route_a["execution_result"]["precision_value_table_emitted_now"] is False, "Route A overemitted value table")
    require(route_a["execution_result"]["full_profile_likelihood_emitted_now"] is False, "Route A overemitted profile")
    require(route_a["execution_result"]["accepted_for_true_SM_equivalence"] is False, "Route A overaccepted")

    require(route_b["available_now"]["partial_same_source_payload_emitted"] is True, "Route B missing partial payload")
    require(route_b["available_now"]["best_qasu3_payload_lane_selected"] is True, "Route B missing best lane")
    require(route_b["available_now"]["selected_diagonal_HYM_first_solve"] is True, "Route B missing HYM solve")
    require(route_b["available_now"]["diagonal_End0_DE_formula"] is True, "Route B missing D_E formula")
    require(route_b["available_now"]["stationary_projector_rho_s_reconciled"] is True, "Route B missing stationary reconciliation")
    require(
        route_b["available_now"]["crossrepo_promotable_qasu3_packet_found"] is False,
        "Route B found an unexpected promotable cross-repo packet",
    )
    for key in [
        "actual_QaSU3_operator_payload",
        "Pic0_selection_or_quotient",
        "selected_HYM_Riesz_Green_dotD",
        "dynamic_sector_ready_operator_payload",
        "selected_dynamic_PhiFin_C1_payload",
    ]:
        require(route_b["missing_for_true_equivalence"][key] is True, f"Route B missing open gate: {key}")
    require(route_b["execution_result"]["route_attempted"] is True, "Route B not attempted")
    require(route_b["execution_result"]["actual_operator_payload_emitted_now"] is False, "Route B overemitted payload")
    require(route_b["execution_result"]["promotable_crossrepo_packet_found"] is False, "Route B overpromoted cross-repo packet")
    require(route_b["execution_result"]["accepted_for_true_SM_equivalence"] is False, "Route B overaccepted")

    require(decision["SM_parity_closed"] is True, "decision reopened SM parity")
    require(decision["route_A"]["closed_now"] is False, "decision overclosed Route A")
    require(decision["route_B"]["closed_now"] is False, "decision overclosed Route B")
    require(decision["true_SM_equivalence_closed"] is False, "decision overclosed true equivalence")
    require(decision["no_knob_closed"] is False, "decision overclosed no-knob")
    require("full precision observable value table" in decision["route_A"]["next_fill"], "decision missing Route A next fill")
    require("actual selected Qa/SU3 operator packet" in decision["route_B"]["next_fill"], "decision missing Route B next fill")

    require(data["closure_decision"]["SM_parity_closed"] is True, "candidate SM parity not closed")
    require(
        data["closure_decision"]["route_A_precision_profile_loop_values_closed"] is False,
        "candidate overclosed Route A",
    )
    require(
        data["closure_decision"]["route_B_actual_QaSU3_operator_payload_closed"] is False,
        "candidate overclosed Route B",
    )
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(data["closure_decision"]["no_knob_closed"] is False, "candidate no-knob overclosed")
    require(data["closure_claimed"] is False, "candidate incorrectly claims closure")
    require(data["what_closes_now"]["both_routes_kept_as_superset_paths"] is True, "superset path flag missing")
    require(data["what_closes_now"]["next_value_attempt_target_selected"] is True, "next target flag missing")
    require(data["what_remains_open"]["full_precision_observable_value_table"] is True, "precision table gate missing")
    require(data["what_remains_open"]["actual_QaSU3_operator_packet"] is True, "Qa/SU3 gate missing")
    require("not a closure claim" in note, "note missing non-closure guard")
    require("not a target" in note, "note missing no-target-fit guard")

    for packet in [data, route_a, route_b, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
