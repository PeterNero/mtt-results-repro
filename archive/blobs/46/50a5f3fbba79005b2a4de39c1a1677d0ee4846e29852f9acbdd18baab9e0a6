"""Audit enriched Weyl-pair source provenance / Galerkin C1 values gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
STATIC = PACKET_DIR / "static_enriched_weylpair_source_provenance.packet.json"
DYNAMIC = PACKET_DIR / "dynamic_c1_value_boundary.packet.json"
GALERKIN = PACKET_DIR / "galerkin_c1_values_fallback.packet.json"
CERT = ROOT / "certificates" / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_enrichedweylpairsourceprovenance_or_galerkinc1values.py"

STATUS = (
    "MTT_SELECTED_ENRICHEDWEYLPAIRSOURCEPROVENANCE_OR_GALERKINC1VALUES_"
    "BUILT_STATIC_PROVENANCE_CLOSED_DYNAMIC_VALUES_OPEN"
)
NEXT = "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    static = load(STATIC)
    dynamic = load(DYNAMIC)
    galerkin = load(GALERKIN)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(static["status"] == "STATIC_ENRICHED_WEYLPAIR_SOURCE_PROVENANCE_CLOSED", "static status mismatch")
    require(static["provenance_closed"] is True, "static provenance not closed")
    carrier = static["source_level_carrier"]
    for key in ["phase_Z_source_proved", "shift_X_source_proved", "active_shift_1_1_proved"]:
        require(carrier[key] is True, f"carrier flag missing: {key}")
    route = static["static_sector_route"]
    require(route["phase_Z_to"] == ["u", "e"], "phase route mismatch")
    require(route["shift_X_to"] == ["d", "nuD"], "shift route mismatch")
    require(route["selected_static_sector_route_now_closed"] is True, "static route not closed")
    require(route["same_route_in_primitive_selector"] is True, "primitive selector route mismatch")
    require(route["clock_phase_side"]["matter_slot"] == "10_M", "clock matter slot mismatch")
    require(route["shift_non10_side"]["matter_slots"] == ["bar5_M", "1_M=N^c"], "shift matter slots mismatch")
    norm = static["static_normalization"]
    require(norm["selected_overlap_transfer_normalization"] is True, "overlap normalization not selected")
    require(norm["static_trace_innerproduct_normalization_selected"] is True, "trace normalization not selected")
    require("rho_s(T_i)/sqrt(2)" in norm["unit_trace_transfer"], "unit trace transfer mismatch")
    require(static["observed_data_used"] is False, "static observed data used")
    require(static["target_fitting_used"] is False, "static target fitting used")

    require(dynamic["status"] == "DYNAMIC_C1_VALUES_OPEN_AFTER_STATIC_PROVENANCE", "dynamic status mismatch")
    require(dynamic["conditional_value_run_ready"] is True, "conditional value run not ready")
    require(dynamic["conditional_rank"] == 2, "conditional rank mismatch")
    require(abs(dynamic["conditional_condition_number"] - 1.0) < 1e-9, "condition number mismatch")
    require(abs(dynamic["conditional_deltaTheta"][0] - 1.0) < 1e-9, "delta 0 mismatch")
    require(abs(dynamic["conditional_deltaTheta"][1] - 1.0) < 1e-9, "delta 1 mismatch")
    require(dynamic["A_transpose_A_if_promoted"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(dynamic["A_transpose_b_if_promoted"] == [12.0, 12.0], "ATb mismatch")
    after = dynamic["after_static_provenance_closure"]
    for key in [
        "source_level_weylpair_provenance_open",
        "static_sector_routing_open",
        "static_transfer_normalization_open",
        "A_selected_currently_emitted",
        "b_selected_currently_emitted",
        "deltaTheta_C1_currently_promoted",
    ]:
        require(after[key] is False, f"post-static false flag mismatch: {key}")
    for key in [
        "selected_dynamic_source_to_C1_transfer_tensor_open",
        "selected_primitive_C1_overlap_contractions_open",
        "selected_Hessian_or_b_source_vector_open",
    ]:
        require(after[key] is True, f"post-static dynamic blocker missing: {key}")
    for key in [
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
    ]:
        require(dynamic["dynamic_value_promotion"][key] is False, f"dynamic overclaimed: {key}")
    require(dynamic["observed_data_used"] is False, "dynamic observed data used")
    require(dynamic["target_fitting_used"] is False, "dynamic target fitting used")

    require(galerkin["status"] == "HONEST_GALERKIN_C1_VALUES_STILL_OPEN", "Galerkin status mismatch")
    require(galerkin["selected_source_verified"] is False, "Galerkin oververified")
    require(galerkin["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True, "Galerkin SM implication missing")
    require(galerkin["would_close_no_knob_flavor_constants_if_values_emitted"] is False, "Galerkin no-knob overclaim")
    require(galerkin["observed_flavor_data_forbidden"] is True, "observed flavor data not forbidden")
    require(galerkin["target_fitting_forbidden"] is True, "target fitting not forbidden")

    closes = data["what_closes_now"]
    for key in [
        "static_enriched_weylpair_source_provenance",
        "static_Z_to_u_e_X_to_d_nuD_route",
        "static_1M_Dirac_neutrino_shift_rule",
        "static_finite_trace_transfer_normalization",
        "dynamic_value_boundary_after_static_provenance",
        "observed_constants_excluded_as_selectors",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")
    remains = data["what_remains_open"]
    for key in [
        "selected_dynamic_source_to_C1_transfer_tensor",
        "selected_primitive_C1_overlap_contractions",
        "selected_D_E_Riesz_Green_dotD",
        "physical_alpha1_driver_at_dynamic_C1_tier",
        "theorem_derived_A_selected",
        "theorem_derived_b_selected",
        "selected_deltaTheta_C1",
        "honest_selected_Galerkin_C1_execution_values",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(remains[key] is True, f"remaining gate missing: {key}")
    decision = data["promotion_decision"]
    require(decision["static_enriched_weylpair_source_provenance_promoted"] is True, "static provenance not promoted")
    for key in [
        "dynamic_C1_transfer_tensor_promoted",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "honest_Galerkin_C1_execution_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(decision[key] is False, f"candidate overclaimed: {key}")
    for key in [
        "observed_data_used",
        "target_fitting_used",
        "closure_claimed",
        "SM_parity_dynamic_packet_closure_claimed",
        "true_SM_equivalence_claimed",
        "no_knob_closure_claimed",
    ]:
        require(data[key] is False, f"candidate flag overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("static enriched Weyl-pair provenance" in note, "note missing static provenance")
    require("dynamic C1 value tier remains open" in note, "note missing dynamic boundary")
    require("No observed masses" in note, "note missing no-observed-data guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
