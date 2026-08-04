"""Audit Weyl-pair dynamic-overlap source-promotion / honest Galerkin C1 gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill.candidate.json"
CERT = ROOT / "certificates" / "selected_weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_WeylPairDynamicOverlap_SourcePromotion_or_HonestGalerkinC1_ValueFill_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill.py"

STATUS = (
    "MTT_SELECTED_WEYLPAIRDYNAMICOVERLAP_SOURCEPROMOTION_OR_HONESTGALERKINC1_"
    "VALUEFILL_BUILT_PROMOTION_CUTSET_OPEN"
)
NEXT = "MTT_Selected_DynamicTransferHessian_bSelected_or_HonestGalerkinC1_ValueFill_v1"
TOL = 1e-12


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    closed = data["closed_static_source_tier"]
    for key in [
        "source_level_Z_and_X_carrier",
        "active_shift_1_1",
        "static_Z_clock_to_u_e",
        "static_X_shift_to_d_nuD",
        "static_1M_Nc_shift_rule",
        "static_trace_transfer_normalization",
        "conditional_non_scalar_packet",
        "conditional_weylpair_rank_and_solve",
    ]:
        require(closed[key] is True, f"closed static/source field missing: {key}")

    lane_a = data["lane_A_dynamic_source_promotion"]
    require(lane_a["conditional_transfer_exact"] is True, "conditional transfer not exact")
    require(lane_a["conditional_transfer_formula"]["phase_column"] == "T(Z) = sector_route(u,e; I + Z)", "phase formula mismatch")
    require(lane_a["conditional_transfer_formula"]["shift_column"] == "T(X) = sector_route(d,nuD; I + X)", "shift formula mismatch")
    require(abs(lane_a["conditional_transfer_residuals"]["phase_residual"]) <= TOL, "phase residual nonzero")
    require(abs(lane_a["conditional_transfer_residuals"]["shift_residual"]) <= TOL, "shift residual nonzero")
    require(lane_a["static_source_route_reclassified_closed"] is True, "static route not reclassified")
    for key in ["mass_split", "ckm_commutator", "pmns_commutator", "cp_odd"]:
        require(lane_a["conditional_packet_tests_pass"][key] is True, f"conditional test failed: {key}")
    for key, value in lane_a["selected_promotion_fields"].items():
        require(value is False, f"dynamic promotion overclaimed: {key}")
    require(lane_a["promoted"] is False, "Lane A overpromoted")

    lane_b = data["lane_B_honest_Galerkin_C1_value_fill"]
    require(lane_b["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING", "Galerkin manifest status mismatch")
    require(lane_b["selected_source_verified"] is False, "Galerkin source oververified")
    require(lane_b["required_outputs"] == [
        "zero_mode_bases",
        "primitive_three_by_three_contraction_terms",
        "linear_response_matrices",
        "C33/nonzero-family-rank tests",
    ], "Galerkin required outputs mismatch")
    for key, value in lane_b["required_outputs_present"].items():
        require(value is False, f"Galerkin output overclaimed: {key}")
    require(lane_b["promoted"] is False, "Lane B overpromoted")

    cutset = data["minimum_cutset"]
    require(cutset["static_routing_no_longer_in_cutset"] is True, "static routing still in cutset")
    require(cutset["observed_flavor_data_forbidden_as_selector"] is True, "observed selector guard missing")
    require("selected_b_selected" in cutset["lane_A_fill_all"], "Lane A missing b_selected")
    require("linear_response_matrices" in cutset["lane_B_fill_all"], "Lane B missing response matrices")

    decision = data["promotion_decision"]
    require(decision["static_source_route_retired_as_blocker"] is True, "static blocker not retired")
    require(decision["conditional_non_scalar_packet_available"] is True, "conditional packet unavailable")
    require(decision["dynamic_promotion_cutset_open"] is True, "cutset not open")
    for key in [
        "selected_dynamic_overlap_promoted",
        "selected_full_response_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_Galerkin_C1_contractions_promoted",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    closes = data["what_closes_now"]
    for key in [
        "promotion_cutset_built",
        "stale_static_sector_routing_blocker_superseded",
        "conditional_transfer_tied_to_static_selected_routing",
        "honest_Galerkin_value_fill_requirements_extracted",
        "no_target_fitting_guard_preserved",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_dynamic_source_to_C1_transfer",
        "selected_Hessian_blocks",
        "selected_b_selected",
        "selected_A_selected",
        "honest_Galerkin_C1_contractions",
        "full_SM_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["selected_dynamic_overlap_tensor_claimed"] is False, "dynamic overlap claimed")
    require(data["selected_full_response_claimed"] is False, "full response claimed")
    require(data["A_selected_claimed"] is False, "A_selected claimed")
    require(data["b_selected_claimed"] is False, "b_selected claimed")
    require(data["Galerkin_C1_contractions_claimed"] is False, "Galerkin contractions claimed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
