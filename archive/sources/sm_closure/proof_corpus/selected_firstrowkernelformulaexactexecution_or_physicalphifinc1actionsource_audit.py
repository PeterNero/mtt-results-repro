"""Audit selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource.candidate.json"
CERT = ROOT / "certificates" / "selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource_certificate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource"
EXEC = PACKET_DIR / "first_row_exact_weyl_execution.packet.json"
ACTION = PACKET_DIR / "physical_action_source_gate_after_first_row.packet.json"
DECISION = PACKET_DIR / "first_row_execution_decision.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FirstRowKernelFormulaExactExecution_or_PhysicalPhiFinC1ActionSource_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    execution = load(EXEC)
    action = load(ACTION)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_FIRSTROWKERNELFORMULAEXACTEXECUTION_OR_PHYSICALPHIFINC1ACTIONSOURCE_BUILT_FIRST_ROW_VALUE_EXACT_PROVENANCE_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(execution["row_id"] == "u:phase:r0c0", "row mismatch")
    require(execution["computed_complex_entry_value"]["exact"] == "4/3", "exact value mismatch")
    require(abs(execution["computed_complex_entry_value"]["real"] - 4.0 / 3.0) < 1e-12, "float value mismatch")
    require(execution["matches_algebraic_support_value"] is True, "support mismatch")
    require(execution["matches_weyl_packet_matrix_entry"] is True, "Weyl packet mismatch")
    require(execution["exactness_or_error_bound_certificate"]["roundoff_bound"] == 0.0, "not exact")
    require(execution["computed_independent_complex_entry_value"] is True, "computed clause not closed")
    require(execution["exactness_certificate_emitted"] is True, "exactness clause not closed")
    require(execution["provenance_independent_of_residual_projector_replay"] is False, "provenance overclaimed")
    require(execution["first_row_independently_executed_now"] is False, "independence overclaimed")
    require(action["already_closed"]["first_row_exact_value"] is True, "action gate missing row value")
    require(action["still_required_for_independent_route_B"]["first_row_provenance_independent_of_residual_projector_replay"] is True, "route B gap missing")
    require(decision["closed_kernel_clauses_for_first_row"]["computed_independent_complex_entries"] is True, "computed clause false")
    require(decision["closed_kernel_clauses_for_first_row"]["exactness_or_error_bound_certificate"] is True, "exactness clause false")
    require(decision["closed_kernel_clauses_for_first_row"]["provenance_independent_of_residual_projector_replay"] is False, "provenance overclosed")
    require(decision["first_row_value_exact"] == "4/3", "decision exact value mismatch")
    require(decision["full_72_row_execution_closed"] is False, "72 row overclaimed")
    require(decision["true_SM_equivalence_closed"] is False, "SM equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob overclaimed")
    require(cert["first_row_value_exact"] == "4/3", "certificate exact value mismatch")
    require(cert["first_row_independently_executed_now"] is False, "certificate independence overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("R_Z(0,0) = 2/3 + 2/3 = 4/3" in note, "note missing exact calculation")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
