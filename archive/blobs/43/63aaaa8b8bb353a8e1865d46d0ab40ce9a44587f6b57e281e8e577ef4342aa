"""Audit dynamic overlap-kernel or C1-primitive source-emission reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_dynamic_overlapkernel_or_c1primitive_source_emission.candidate.json"
CERT = ROOT / "certificates" / "selected_dynamic_overlapkernel_or_c1primitive_source_emission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_dynamic_overlapkernel_or_c1primitive_source_emission.py"

STATUS = (
    "MTT_SELECTED_DYNAMIC_OVERLAPKERNEL_OR_C1PRIMITIVE_SOURCE_EMISSION_"
    "REDUCED_TYPED_DERIVATIVE_PRIMITIVE_VALUES_OPEN"
)
NEXT = "MTT_Selected_TypedBN_RetardedDerivative_or_PrimitiveResponse_ValueEmission_v1"


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
    require(NEXT in note, "note does not record next artifact")

    static_import = data["static_import"]
    require(static_import["sector_pair_partition_closed_static"] is True, "static sector partition not imported")
    require(static_import["oneM_Dirac_rule_closed_static"] is True, "static 1M rule not imported")
    require(static_import["finite_trace_transfer_closed_static"] is True, "static transfer not imported")
    require(static_import["dynamic_C1_operator_values_closed"] is False, "dynamic operator values overclosed")

    lanes = data["lanes"]
    lane_a = lanes["A_same_source_alpha1_strength"]
    require(lane_a["closed"] is False, "lane A overclosed")
    require(lane_a["source_identity_selected"] is True, "source identity support not imported")
    require(lane_a["lambda_alpha1_candidate"] == 1.0, "lambda candidate changed")
    require(lane_a["h_ext_residual_l2"] < 1e-10, "h_ext residual too large")

    lane_b = lanes["B_typed_retarded_derivative"]
    require(lane_b["closed"] is False, "lane B overclosed")
    require(lane_b["dotD_source_algebra_closed"] is True, "dotD source algebra not closed")
    require(
        lane_b["validator_math_passes_if_driver_is_theorem_derived"] is True,
        "dotD validator math readiness missing",
    )
    require(lane_b["static_sector_route_available"] is True, "static sector route missing")
    require(lane_b["static_finite_transfer_available"] is True, "static finite transfer missing")
    require(
        lane_b["dynamic_End0_to_sector_functor_values_extracted"] is False,
        "End0-to-sector values overclaimed",
    )
    require(
        lane_b["typed_BN_tangent_or_retarded_kernel_emitted"] is False,
        "typed retarded derivative overclaimed",
    )
    require(lane_b["honest_dotD_replay_from_kernel"] is False, "honest replay overclaimed")

    lane_c = lanes["C_selected_C1_primitive_or_vertex"]
    require(lane_c["closed"] is False, "lane C overclosed")
    require(lane_c["canonical_mode_conserving_C1_zero"] is True, "canonical zero no-go missing")
    require(lane_c["noninvariant_active_shift_forced"] is True, "active shift not localized")
    require(lane_c["noninvariant_candidates_nonzero"] is True, "noninvariant candidates missing")
    require(lane_c["fixed_fiber_candidate_count"] == 3, "fixed fiber candidate count mismatch")
    require(lane_c["fixed_fiber_ranks_all_three"] is True, "fixed fiber ranks not all 3")
    require(lane_c["conditional_weylpair_A_exact"] is True, "conditional Weylpair A not exact")
    require(lane_c["promote_to_A_selected"] is False, "A_selected overclaimed")

    cutset = data["dynamic_cutset"]
    for key, value in cutset["already_closed_or_reduced"].items():
        require(value is True, f"closed/reduced cutset item false: {key}")
    require(
        "typed dynamic B_N retarded derivative or alpha1 source-strength theorem"
        in cutset["remaining_minimal_objects"],
        "typed derivative not listed as remaining minimal object",
    )

    require(data["closure_claimed"] is False, "full closure overclaimed")
    require(data["dynamic_kernel_emitted"] is False, "dynamic kernel overclaimed")
    require(data["selected_C1_primitive_emitted"] is False, "C1 primitive overclaimed")
    require(data["A_selected_claimed"] is False, "A_selected overclaimed")
    require(data["b_selected_claimed"] is False, "b_selected overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not marked proved")
    require(cert["theorem_proved"] is True, "certificate theorem not marked proved")

    remains = data["what_remains_open"]
    for key in [
        "typed_BN_retarded_derivative_or_alpha1_source_strength",
        "selected_End0_to_sector_functor_values",
        "selected_dynamic_overlap_Hessian_normalization",
        "selected_primitive_or_vertex_response_values",
        "selected_b_selected",
        "honest_selected_deltaTheta_C1_solve",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
