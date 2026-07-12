"""Audit non-split/Route-C visible lane and minimal Hsel/Gret QA import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "nonsplit_routec_and_minimal_hsel_gret_import.candidate.json"
CERT = ROOT / "certificates" / "nonsplit_routec_and_minimal_hsel_gret_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "NonSplitRouteC_and_MinimalHselGret_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_nonsplit_routec_and_minimal_hsel_gret.py"

STATUS = "NONSPLIT_ROUTEC_AND_MINIMAL_HSEL_GRET_IMPORTED_PROMOTION_OPEN"
NEXT = "MTT_SameSource_SymmetryBreaking_Source_v1"
PARALLEL_NEXT = "Selected_Qa_SU3_Finite_Galerkin_to_Smooth_Operator_Promotion_or_NoGo_v1"


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
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["parallel_next_required_artifact"] == PARALLEL_NEXT, "candidate parallel next mismatch")
    require(cert["parallel_next_required_artifact"] == PARALLEL_NEXT, "certificate parallel next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    visible = data["visible_same_source_lane"]
    require(visible["next_required_artifact"] == NEXT, "visible next mismatch")
    require(visible["rank2_lane"]["classification"] == "SUPERSET_CONVERGENCE_PRIMARY_FILL_LANE", "rank2 lane not primary")
    require(visible["rank2_lane"]["target"]["l_vector_abc"] == [1, -2, 0], "wrong rank2 L vector")
    require(visible["rank2_lane"]["target"]["c2_extension_alpha_coeffs"] == [4, 0, 0], "wrong c2 target")
    for key in [
        "selected_l2_cochain_packet_absent",
        "branch_orientation_not_selected",
        "base_swap_pic0_selector_obstruction",
        "nonzero_ext_not_selected",
        "stability_not_proved",
    ]:
        require(visible["rank2_lane"]["blocked_by"][key] is True, f"rank2 blocker missing: {key}")
    for key in [
        "actual_selected_branch_packet",
        "actual_selected_rho_E_values",
        "actual_selected_Hermitian_metric",
        "actual_selected_A01_or_DE_action",
        "actual_source_residual_certificate",
        "actual_Riesz_Green_dotD_data",
    ]:
        require(visible["route_c_lane"]["blocked_by"][key] is True, f"Route-C blocker missing: {key}")

    qa = data["qa_minimal_hsel_gret"]
    require(qa["hessian"]["matrix"] == [[26, -3, 0], [-3, 10, 0], [0, 0, 8]], "wrong H_sel")
    require(qa["hessian"]["determinant"] == 2008, "wrong Hessian determinant")
    require(qa["hessian"]["positive_definite"] is True, "H_sel not positive definite")
    require(qa["green"]["inverse_verified"] is True, "G_ret inverse not verified")
    require(qa["green"]["identity_check"] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]], "wrong inverse identity")
    require(qa["selection_proof"]["selected_covector"] == [0, 0, 1], "wrong selected covector")
    require(qa["selection_proof"]["selected_covector_retarded_norm"] == "1/8", "wrong selected norm")
    require(qa["tau"]["all_products_cancel"] is True, "tau cancellation failed")
    require(qa["validator_result"]["exit_code"] == 0, "QA validator failed")
    require(qa["closure_claimed"] is False, "QA closure overclaimed")

    closes = data["what_closes_now"]
    for key in [
        "visible_two_lane_reduction_imported",
        "rank2_valpha_preferred_fill_lane_identified",
        "routec_repair_lane_preserved",
        "same_source_symmetry_breaking_source_named_as_common_blocker",
        "qa_actual_finite_H_sel_matrix_imported",
        "qa_actual_exact_rational_G_ret_imported",
        "qa_H_sel_G_ret_identity_verified",
        "qa_finite_Pi_tw_plus_e3_selection_imported",
        "qa_tau_values_derived_in_finite_model",
        "no_target_fitting_reaffirmed",
    ]:
        require(closes[key] is True, f"closed flag missing: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_same_source_symmetry_breaking_source",
        "claims_selected_visible_operator_source",
        "claims_selected_L2_cochain_or_Ext",
        "claims_selected_RouteC_residual",
        "claims_selected_DE_dotD_Riesz_Green",
        "claims_smooth_Qa_SU3_operator_promotion",
        "claims_qa_threshold_determinant",
        "claims_A_selected_or_b_selected",
        "claims_Yukawa_or_full_SM_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("SameSourceSymmetryBreakingSource.v1" in note, "note missing common blocker")
    require("det(H_sel) = 2008" in note, "note missing finite Hessian determinant")
    require("full SM closure remain open" in note, "note missing open closure guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
