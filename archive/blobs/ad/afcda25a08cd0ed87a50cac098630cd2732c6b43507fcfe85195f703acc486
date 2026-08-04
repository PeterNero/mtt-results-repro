"""Audit PSM-C1-02 RA-1 physical equality / RB-3 Hessian source fill."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

BASE = DATA / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill"
CANDIDATE = DATA / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill.candidate.json"
ROUTE_A = BASE / "route_a_ra1_physical_action_equality_status.packet.json"
ROUTE_B = BASE / "route_b_rb3_hessian_source_fill.packet.json"
SUPERSET = BASE / "psm_c1_02_superset_alignment_after_rb3.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_RouteA_RA1_PhysicalActionEquality_or_RouteB_RB3_HessianSourceFill_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_RA1_PHYSICALACTIONEQUALITY_OR_RB3_HESSIANSOURCEFILL_BUILT_RB3_NORMAL_EQUATIONS_FILLED_SELECTION_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_RouteA_RA2_BoundarySourceCancellation_or_RouteB_RB4_IndependentQuadratureSource_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    superset = load(SUPERSET)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["ROUTE-A/RA-1", "ROUTE-B/RB-3"], "active routes mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["observed_data_used_as_selector"] is False, "candidate uses observed selector")
    require(candidate["target_fitting_used"] is False, "candidate target fitting")
    require(candidate["what_closes_now"]["ROUTE_A_RA1_reduced_to_RA2_boundary_source_cancellation"] is True, "RA1 reduction missing")
    require(candidate["what_closes_now"]["ROUTE_B_RB3_hessian_source_normal_equations_filled"] is True, "RB3 fill missing")
    require(candidate["what_closes_now"]["RB3_matches_prior_conditional_source_map"] is True, "conditional map mismatch")
    require(candidate["what_closes_now"]["support_hessian_positive_definite"] is True, "support Hessian not positive")
    require(candidate["what_remains_open"]["selected_source_promotion"] is True, "selected source promotion should remain open")

    require(route_a["route_label"] == "ROUTE-A", "route A label mismatch")
    require(route_a["clause_id"] == "RA-1", "route A clause mismatch")
    require(route_a["physical_action_equality_claimed"] is False, "RA1 physical equality overclaimed")
    require(route_a["free_axiom_patch_used"] is False, "RA1 free axiom patch used")
    require(route_a["current_RA1_result"]["RA1d_boundary_source_terms_split_to_RA2"] is True, "RA2 split missing")
    require(all(item["used_as_source_proof"] is False for item in route_a["corpus_support"]), "corpus source proof overclaimed")

    hessian = route_b["hessian_source_support"]
    require(route_b["route_label"] == "ROUTE-B", "route B label mismatch")
    require(route_b["input_id"] == "RB-3", "route B input mismatch")
    require(route_b["primitive_row_count"] == 72, "primitive row count mismatch")
    require(route_b["matches_prior_conditional_source_map"] is True, "route B conditional mismatch")
    require(hessian["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(hessian["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(hessian["deltaTheta_C1_support_solution"] == [1.0, 1.0], "delta mismatch")
    require(hessian["determinant"] == 144.0, "determinant mismatch")
    require(hessian["positive_definite_support_hessian"] is True, "support Hessian positivity mismatch")
    require(route_b["computed_from_independent_galerkin_quadrature"] is False, "RB3 independent quadrature overclaimed")
    require(route_b["selected_hessian_source_emitted"] is False, "RB3 selected source overclaimed")
    require(route_b["theorem_derived"] is False, "RB3 theorem-derived overclaimed")
    require(route_b["source_owner_verified"] is False, "RB3 source owner overclaimed")
    require(route_b["residual_replay_dependency"] is True, "RB3 residual dependency should be recorded")

    require(superset["closed_boundary"] == "DONE-PARITY-00", "superset boundary mismatch")
    require(superset["paths_used_as_knobs"] is False, "superset paths used as knobs")
    require(superset["observed_values_used_as_knobs"] is False, "observed values used as knobs")
    require("same PSM-C1-02 C1 source-promotion packet" in superset["locked_target"], "locked target mismatch")
    require(all(ref["used_as_source_proof"] is False for ref in superset["external_references"]), "external proof overclaimed")

    require(next_work["primary"]["label"] == "PSM-C1-02 / ROUTE-A / RA-2", "next primary mismatch")
    require(next_work["secondary"]["label"] == "PSM-C1-02 / ROUTE-B / RB-4", "next secondary mismatch")
    require(next_work["next_required_artifact"] == NEXT, "next work artifact mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["route_A_RA1_reduced_to_RA2"] is True, "cert RA1 reduction mismatch")
    require(cert["route_A_RA1_closed"] is False, "cert RA1 overclosed")
    require(cert["route_B_RB3_hessian_filled"] is True, "cert RB3 fill mismatch")
    require(cert["route_B_RB3_selected_promoted"] is False, "cert RB3 overpromoted")
    require(cert["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "cert Hessian mismatch")
    require(cert["A_transpose_b"] == [12.0, 12.0], "cert source mismatch")
    require(cert["deltaTheta_C1_support_solution"] == [1.0, 1.0], "cert delta mismatch")
    require(cert["closure_claimed"] is False, "cert closure overclaimed")

    require("Status label: `PSM-C1-02 / ROUTE-A / RA-1`" in note, "note label missing")
    require("`PSM-C1-02 / ROUTE-B / RB-3`" in note, "note RB3 label missing")
    require("They are not free knobs" in note, "note superset guardrail missing")

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
