"""Audit non-scalar dynamic-overlap / full-response correction value emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json"
CERT = ROOT / "certificates" / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NonScalarDynamicOverlap_or_FullResponseCorrection_ValueEmission_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.py"

STATUS = (
    "MTT_SELECTED_NONSCALARDYNAMICOVERLAP_OR_FULLRESPONSECORRECTION_VALUEEMISSION_"
    "BUILT_CONDITIONAL_VALUES_SOURCE_OPEN"
)
NEXT = "MTT_Selected_WeylPairDynamicOverlap_SourcePromotion_or_HonestGalerkinC1_ValueFill_v1"
SECTORS = ["u", "d", "e", "nuD"]
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

    closed = data["closed_inputs"]
    for key in [
        "current_scalar_layer_no_go_proved",
        "current_C1_observable_class_emitted",
        "static_sector_routing_selected",
        "static_trace_normalization_selected",
        "source_level_weyl_carrier_closed",
        "active_shift_1_1_provenance_closed",
        "conditional_weylpair_A_rank_exact",
        "conditional_weylpair_solve_exact",
    ]:
        require(closed[key] is True, f"closed input missing: {key}")

    packet = data["conditional_non_scalar_value_packet"]
    require(packet["constructed"] is True, "packet not constructed")
    require(packet["selected_by_MTT"] is False, "conditional packet overselected")
    require(packet["observed_flavor_data_used"] is False, "observed data used")
    require(packet["baseline_layer"]["fiber_representative"] == 0, "baseline representative mismatch")

    responses = packet["sector_first_responses"]
    for sector in SECTORS:
        inv = responses[sector]["invariants"]
        require(inv["non_scalar"] is True, f"sector response scalar: {sector}")
        require(inv["traceless_norm_sq"] > TOL, f"traceless norm not positive: {sector}")
        require(inv["hermitian_residual_norm_sq"] <= TOL, f"H1 not Hermitian: {sector}")
    require(responses["u"]["source_direction"] == "phase_packet_I_plus_Z", "u route mismatch")
    require(responses["e"]["source_direction"] == "phase_packet_I_plus_Z", "e route mismatch")
    require(responses["d"]["source_direction"] == "shift_packet_I_plus_X", "d route mismatch")
    require(responses["nuD"]["source_direction"] == "shift_packet_I_plus_X", "nuD route mismatch")

    tests = packet["acceptance_tests"]
    require(tests["all_mass_split_positive"] is True, "mass split test failed")
    require(tests["ckm_commutator_positive"] is True, "CKM commutator test failed")
    require(tests["pmns_commutator_positive"] is True, "PMNS commutator test failed")
    require(tests["cp_odd_invariant_nonzero"] is True, "CP invariant test failed")
    require(tests["current_layer_flavor_tests_pass_conditionally"] is True, "conditional tests missing")
    require(tests["ckm_commutator_norm_sq"] > TOL, "CKM norm not positive")
    require(tests["pmns_commutator_norm_sq"] > TOL, "PMNS norm not positive")
    require(abs(tests["cp_odd_trace_commutator_cubed_imag"]) > TOL, "CP imag not positive")

    diagnostic = packet["matches_existing_diagnostic_metrics"]
    require(
        abs(tests["ckm_commutator_norm_sq"] - diagnostic["ckm_commutator_norm_sq"]) <= TOL,
        "CKM diagnostic mismatch",
    )
    require(
        abs(tests["pmns_commutator_norm_sq"] - diagnostic["pmns_commutator_norm_sq"]) <= TOL,
        "PMNS diagnostic mismatch",
    )
    require(
        abs(
            tests["cp_odd_trace_commutator_cubed_imag"]
            - diagnostic["cp_odd_trace_commutator_cubed_imag"]
        )
        <= TOL,
        "CP diagnostic mismatch",
    )

    gate = data["promotion_gate"]
    require(gate["conditional_non_scalar_packet_available"] is True, "non-scalar packet unavailable")
    for key in [
        "promote_to_selected_dynamic_overlap_allowed",
        "promote_to_selected_full_response_allowed",
        "promote_to_A_selected_allowed",
        "promote_to_b_selected_allowed",
        "selected_source_to_C1_transfer_map_emitted",
        "selected_sector_routing_dynamic_map_emitted",
        "selected_Hessian_blocks_emitted",
        "selected_b_selected_emitted",
        "honest_Galerkin_C1_contractions_emitted",
    ]:
        require(gate[key] is False, f"promotion overclaimed: {key}")

    source_gap = data["selected_source_gap"]
    for key in [
        "Z_and_X_source_carrier",
        "active_shift_1_1",
        "static_sector_route",
        "static_trace_normalization",
    ]:
        require(source_gap["source_level_closed"][key] is True, f"source closed flag missing: {key}")
    for key in [
        "phase_Z_to_u_e_I_plus_Z_as_dynamic_overlap_column",
        "shift_X_to_d_nuD_I_plus_X_as_dynamic_overlap_column",
        "same_source_Hessian_or_b_selected_normalization",
        "A_selected_from_theorem_derived_packet",
        "honest_deltaTheta_C1_solve",
        "honest_Galerkin_C1_value_fill",
    ]:
        require(source_gap["dynamic_level_open"][key] is True, f"dynamic gap missing: {key}")

    closes = data["what_closes_now"]
    for key in [
        "non_scalar_full_response_candidate_values_constructed",
        "mass_split_mixing_CP_acceptance_tests_pass_conditionally",
        "current_scalar_layer_no_go_repaired_conditionally",
        "promotion_gate_to_selected_dynamic_overlap_built",
        "same_source_gap_sharpened_to_dynamic_transfer_or_honest_Galerkin",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["selected_dynamic_overlap_tensor_claimed"] is False, "dynamic overlap overclaimed")
    require(data["selected_full_response_claimed"] is False, "full response overclaimed")
    require(data["A_selected_claimed"] is False, "A_selected claimed")
    require(data["b_selected_claimed"] is False, "b_selected claimed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("without observed flavor targets" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
