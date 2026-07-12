"""Audit selected_firstrowprovenancepromotion_or_allrowsweylexecution."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_firstrowprovenancepromotion_or_allrowsweylexecution.candidate.json"
CERT = ROOT / "certificates" / "selected_firstrowprovenancepromotion_or_allrowsweylexecution_certificate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
ROWS = PACKET_DIR / "all_72_exact_weyl_row_execution.packet.json"
PROVENANCE = PACKET_DIR / "provenance_promotion_gate_after_all_rows.packet.json"
DECISION = PACKET_DIR / "all_rows_execution_decision.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FirstRowProvenancePromotion_or_AllRowsWeylExecution_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    rows = load(ROWS)
    provenance = load(PROVENANCE)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_FIRSTROWPROVENANCEPROMOTION_OR_ALLROWSWEYLEXECUTION_BUILT_72_ROW_VALUES_EXACT_PROVENANCE_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(rows["row_count"] == 72, "row count mismatch")
    require(rows["source_counts"]["R_Z"] == 18, "R_Z count mismatch")
    require(rows["source_counts"]["R_X"] == 18, "R_X count mismatch")
    require(rows["source_counts"]["zero_route"] == 36, "zero-route count mismatch")
    require(rows["all_rows_match_formal_packet"] is True, "formal packet mismatch")
    require(rows["max_abs_error_against_formal_packet"] <= 1e-12, "row error too large")
    require(rows["computed_value_clause_closed_for_all_rows"] is True, "computed values not closed")
    require(rows["exactness_clause_closed_for_all_rows"] is True, "exactness not closed")
    require(rows["physical_source_promoted_for_any_row"] is False, "physical source overpromoted")
    require(rows["provenance_independent_of_residual_projector_replay_for_all_rows"] is False, "provenance overclaimed")
    first = rows["rows"][0]
    require(first["row_id"] == "u:phase:r0c0", "first row mismatch")
    require(first["exact_value"] == "4/3", "first exact value mismatch")
    require(provenance["route_B_independence_gate"]["all_72_values_exact"] is True, "route B values missing")
    require(provenance["route_B_independence_gate"]["residual_projector_independent_source"] is False, "route B overclosed")
    require(decision["closed_kernel_clauses_for_all_rows"]["computed_independent_complex_entries"] is True, "computed clause false")
    require(decision["closed_kernel_clauses_for_all_rows"]["exactness_or_error_bound_certificate"] is True, "exactness clause false")
    require(decision["closed_kernel_clauses_for_all_rows"]["provenance_independent_of_residual_projector_replay"] is False, "provenance clause overclosed")
    require(decision["all_72_row_execution_closed_under_independent_route_B"] is False, "independent route overclosed")
    require(decision["physical_PhiFinC1_action_source_closed"] is False, "physical action overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "SM equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob overclaimed")
    require(cert["row_count"] == 72, "cert row count mismatch")
    require(cert["all_72_row_values_exact"] is True, "cert row values missing")
    require(cert["provenance_independent_of_residual_projector_replay"] is False, "cert provenance overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("R_Z rows: 18" in note, "note missing R_Z count")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
