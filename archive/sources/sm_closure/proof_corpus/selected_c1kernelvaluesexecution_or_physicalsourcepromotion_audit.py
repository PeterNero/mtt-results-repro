"""Audit selected C1 kernel-values execution / physical-source promotion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_c1kernelvaluesexecution_or_physicalsourcepromotion"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_physical_source_promotion_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_algebraic_kernel_value_execution_attempt.packet.json"
BARRIER = PACKET_DIR / "promotion_barrier_and_next_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_C1KernelValuesExecution_or_PhysicalSourcePromotion_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_C1KERNELVALUESEXECUTION_OR_PHYSICALSOURCEPROMOTION_ALGEBRAIC_VALUES_FILLED_PROMOTION_OPEN"
NEXT = "MTT_Selected_C1MeasurePairing_or_PhysicalActionIdentity_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    barrier = load(BARRIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(route_a["status"] == "PHYSICAL_SOURCE_PROMOTION_ATTEMPT_STILL_OPEN", "route A status mismatch")
    require(route_a["available_now"]["formal_euler_projection"] is True, "Euler support missing")
    require(route_a["available_now"]["least_norm_Q_residual_selection"] is True, "Q residual support missing")
    require(route_a["available_now"]["algebraic_RZ_RX_values_filled"] is True, "RZ/RX fill missing")
    require(route_a["available_now"]["algebraic_b_selected_filled"] is True, "b fill missing")
    require(route_a["available_now"]["algebraic_sector_response_values_filled"] is True, "sector fill missing")
    for key in [
        "physical_action_identity",
        "selected_measure_or_pairing_from_PhiFinC1_trace",
        "admissible_variation_class",
        "boundary_cancellation",
        "same_source_emits_b_selected",
    ]:
        require(route_a["still_missing_for_promotion"][key] is True, f"route A gap missing: {key}")
    require(route_a["route_A_promoted_now"] is False, "route A overclaimed")

    require(route_b["status"] == "ALGEBRAIC_VALUES_FILLED_NOT_INDEPENDENT_QUADRATURE", "route B status mismatch")
    counts = route_b["counts"]
    require(counts["primitive_values_filled"] == 72, "primitive value count mismatch")
    require(counts["hessian_values_filled"] == 2, "hessian value count mismatch")
    require(counts["sector_values_filled"] == 36, "sector value count mismatch")
    require(counts["total_algebraic_values_filled"] == 110, "total value count mismatch")
    require(counts["independent_quadrature_values"] == 0, "independent values overclaimed")
    require(counts["physical_source_promoted_values"] == 0, "physical values overclaimed")
    require(len(route_b["primitive_kernel_values"]) == 72, "primitive values list mismatch")
    require(len(route_b["hessian_source_values"]) == 2, "hessian values list mismatch")
    require(len(route_b["sector_matrix_values"]) == 36, "sector values list mismatch")
    require(all(row["filled_as_algebraic_candidate"] is True for row in route_b["primitive_kernel_values"]), "primitive fill flag missing")
    require(all(row["independent_quadrature_emitted"] is False for row in route_b["primitive_kernel_values"]), "primitive independent overclaim")
    require(route_b["algebraic_consistency_certificate"]["R_Z_norm_sq"] == 4.0, "R_Z norm mismatch")
    require(route_b["algebraic_consistency_certificate"]["R_X_norm_sq"] == 2.0, "R_X norm mismatch")
    require(route_b["algebraic_consistency_certificate"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(route_b["algebraic_consistency_certificate"]["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(route_b["algebraic_consistency_certificate"]["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(route_b["algebraic_consistency_certificate"]["passes_locked_target_by_algebraic_replay"] is True, "locked target failed")
    require(route_b["route_B_accepts_now"] is False, "route B overclaimed")

    require(barrier["status"] == "VALUES_FILLED_PROMOTION_REQUIRES_MEASURE_OR_ACTION_IDENTITY", "barrier status mismatch")
    require(barrier["acceptance_contract_result"]["route_A_accepts_now"] is False, "barrier route A overclaim")
    require(barrier["acceptance_contract_result"]["route_B_accepts_now"] is False, "barrier route B overclaim")
    require(barrier["acceptance_contract_result"]["closure_claimed"] is False, "barrier closure overclaim")
    require(barrier["minimal_next_gate"]["derive_selected_physical_action_identity"] is True, "next gate action identity missing")
    require(barrier["minimal_next_gate"]["or_define_selected_C1_measure_pairing_and_exact_kernel_quadrature"] is True, "next gate measure missing")

    for key in [
        "all_110_value_slots_have_algebraic_candidate_values",
        "primitive_RZ_RX_values_filled",
        "hessian_b_delta_values_filled",
        "sector_response_values_filled",
        "promotion_barrier_identified",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_physical_action_identity",
        "selected_C1_measure_pairing",
        "independent_quadrature_exactness_certificate",
        "same_source_b_selected_emission",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key, value in data["promotion_decision"].items():
        require(value is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("primitive C1 values filled     = 72" in note, "note missing primitive count")
    require("independent quadrature values  = 0" in note, "note missing independent guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
