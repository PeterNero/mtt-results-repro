"""Audit PSM-C1-02 RA-2 boundary/source or RB-4 independent-source gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

BASE = DATA / "selected_psm_c1_02_ra2_boundarysource_or_rb4_independentsource"
CANDIDATE = DATA / "selected_psm_c1_02_ra2_boundarysource_or_rb4_independentsource.candidate.json"
RA2 = BASE / "route_a_ra2_boundary_source_gate.packet.json"
RB4 = BASE / "route_b_rb4_independent_source_gate.packet.json"
MATRIX = BASE / "psm_c1_02_source_promotion_matrix.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / "selected_psm_c1_02_ra2_boundarysource_or_rb4_independentsource_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_RouteA_RA2_BoundarySource_or_RouteB_RB4_IndependentSource_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_RA2_BOUNDARYSOURCE_OR_RB4_INDEPENDENTSOURCE_BUILT_STATIC_PROVENANCE_CLOSED_DYNAMIC_SOURCE_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_RouteA_RA3_SameSourceEmission_or_RouteB_RB5_DynamicValueSourceOwnerFill_v1"
OPEN_FIELDS = ["b_selected_source", "phase_R_Z_source", "sector_row_assembly", "shift_R_X_source"]
CLOSED_FIELDS = ["admissible_c1_variation_space", "independence_guard", "source_owner_id"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    ra2 = load(RA2)
    rb4 = load(RB4)
    matrix = load(MATRIX)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["ROUTE-A/RA-2", "ROUTE-B/RB-4"], "active routes mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(candidate["target_fitting_used"] is False, "candidate target fitting")
    require(candidate["what_closes_now"]["ROUTE_A_RA2_static_finite_boundary_gate"] is True, "RA2 static gate not closed")
    require(candidate["what_closes_now"]["ROUTE_B_RB4_strict_independent_payload_schema_ready"] is True, "RB4 schema not ready")
    require(candidate["what_closes_now"]["source_owner_static_fields_closed_count"] == 3, "closed field count mismatch")
    require(sorted(candidate["what_closes_now"]["dynamic_source_open_fields_identified"]) == OPEN_FIELDS, "open fields mismatch")
    require(candidate["what_remains_open"]["selected_source_promotion"] is True, "selected promotion should remain open")

    require(ra2["route_label"] == "ROUTE-A", "RA2 route mismatch")
    require(ra2["clause_id"] == "RA-2", "RA2 clause mismatch")
    require(ra2["finite_trace_boundary_cancellation"]["algebraic_boundary_closed_now"] is True, "algebraic boundary not closed")
    require(ra2["finite_trace_boundary_cancellation"]["physical_boundary_promoted_now"] is False, "physical boundary overpromoted")
    require(ra2["ra2_static_gate_closed"] is True, "RA2 static gate mismatch")
    require(ra2["ra2_physical_boundary_source_closed"] is False, "RA2 physical gate overclosed")
    require(sorted(ra2["static_source_owner_fields_closed"]) == CLOSED_FIELDS, "RA2 closed fields mismatch")
    require(ra2["free_axiom_patch_used"] is False, "RA2 free axiom used")

    require(rb4["route_label"] == "ROUTE-B", "RB4 route mismatch")
    require(rb4["input_id"] == "RB-4", "RB4 input mismatch")
    require(rb4["strict_payload_schema_ready"] is True, "RB4 schema not ready")
    require(rb4["strict_payload_counts"]["strict_payload_rows"] == 110, "strict row count mismatch")
    require(rb4["strict_payload_counts"]["primitive_contractions"] == 72, "primitive row count mismatch")
    require(rb4["strict_payload_counts"]["hessian_source"] == 2, "hessian row count mismatch")
    require(rb4["strict_payload_counts"]["sector_matrices"] == 36, "sector row count mismatch")
    require(rb4["formal_replay_closed"] is True, "formal replay not closed")
    require(rb4["rb3_hessian_support"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "RB3 Hessian mismatch")
    require(rb4["independent_source_promoted_now"] is False, "RB4 independent source overpromoted")
    require(rb4["selected_dynamic_values_promoted_now"] is False, "RB4 dynamic values overpromoted")
    require(sorted(rb4["closed_source_owner_fields"]) == CLOSED_FIELDS, "RB4 closed fields mismatch")
    require(sorted(rb4["open_source_owner_fields"]) == OPEN_FIELDS, "RB4 open fields mismatch")

    require(matrix["closed_boundary"] == "DONE-PARITY-00", "matrix boundary mismatch")
    require(matrix["source_owner_field_counts"]["closed"] == 3, "matrix closed count mismatch")
    require(matrix["source_owner_field_counts"]["open"] == 4, "matrix open count mismatch")
    require(matrix["closed_now"]["finite_trace_algebraic_boundary_cancellation"] is True, "matrix boundary missing")
    require(matrix["closed_now"]["strict_110_row_payload_schema_ready"] is True, "matrix schema missing")
    require(matrix["still_open"]["selected_source_promotion"] is True, "matrix promotion should remain open")
    require(matrix["superset_strategy"]["paths_used_as_knobs"] is False, "paths used as knobs")
    require(matrix["superset_strategy"]["observed_values_used_as_knobs"] is False, "observed values used as knobs")

    require(next_work["primary"]["label"] == "PSM-C1-02 / ROUTE-A / RA-3", "next primary mismatch")
    require(next_work["secondary"]["label"] == "PSM-C1-02 / ROUTE-B / RB-5", "next secondary mismatch")
    require(next_work["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["route_A_RA2_static_gate_closed"] is True, "cert RA2 static mismatch")
    require(cert["route_A_RA2_physical_boundary_source_closed"] is False, "cert RA2 overclosed")
    require(cert["route_B_RB4_schema_ready"] is True, "cert RB4 schema mismatch")
    require(cert["route_B_RB4_selected_source_promoted"] is False, "cert RB4 overpromoted")
    require(sorted(cert["closed_source_owner_fields"]) == CLOSED_FIELDS, "cert closed fields mismatch")
    require(sorted(cert["open_source_owner_fields"]) == OPEN_FIELDS, "cert open fields mismatch")
    require(cert["closure_claimed"] is False, "cert closure overclaimed")

    require("Status label: `PSM-C1-02 / ROUTE-A / RA-2`" in note, "note RA2 label missing")
    require("`PSM-C1-02 / ROUTE-B / RB-4`" in note, "note RB4 label missing")
    require("They are not knobs" in note, "note superset guardrail missing")

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
