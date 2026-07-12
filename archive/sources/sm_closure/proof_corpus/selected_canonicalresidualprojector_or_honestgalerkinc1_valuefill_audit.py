"""Audit canonical residual projector or honest Galerkin C1 value-fill gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill"
PROJECTOR = PACKET_DIR / "canonical_fixedfiber_residual_projector.packet.json"
REPLAY = PACKET_DIR / "projector_application_value_replay.packet.json"
CUTSET = PACKET_DIR / "projector_or_galerkin_cutset_decision.packet.json"
CERT = ROOT / "certificates" / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill.py"

STATUS = (
    "MTT_SELECTED_CANONICALRESIDUALPROJECTOR_OR_HONESTGALERKINC1_VALUEFILL_"
    "BUILT_PROJECTOR_CLOSED_APPLICATION_OPEN"
)
NEXT = "MTT_Selected_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_v1"
TOL = 1e-9


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    projector = load(PROJECTOR)
    replay = load(REPLAY)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(projector["status"] == "CANONICAL_PROJECTOR_COMPUTED_FROM_SELECTED_FIXED_FIBER_CLASS", "projector status mismatch")
    selected = projector["selected_inputs"]
    for key in [
        "source_level_weyl_carrier_selected",
        "active_shift_selected",
        "fixed_fiber_class_selected_for_current_observables",
        "trace_frobenius_transfer_normalization_selected",
    ]:
        require(selected[key] is True, f"selected input missing: {key}")

    checks = projector["operator_checks"]
    require(checks["fixed_projector_rank"] == 3, "fixed projector rank mismatch")
    require(checks["residual_projector_rank"] == 6, "residual projector rank mismatch")
    for key in [
        "fixed_projector_idempotence_norm_sq",
        "residual_projector_idempotence_norm_sq",
        "fixed_projector_self_adjoint_norm_sq",
        "residual_projector_self_adjoint_norm_sq",
        "orthogonal_complement_product_norm_sq",
        "partition_sum_identity_norm_sq",
    ]:
        require(abs(checks[key]) <= TOL, f"projector check nonzero: {key}")
    require(projector["selected_as_canonical_mathematical_projector"] is True, "canonical projector not selected")
    require(projector["selected_as_physical_C1_transfer_application"] is False, "physical application overclaimed")
    require(projector["observed_data_used"] is False, "observed data used in projector")
    require(projector["target_fitting_used"] is False, "target fitting used in projector")

    require(replay["status"] == "PROJECTOR_REPLAY_MATCHES_RESIDUAL_PACKET_APPLICATION_OPEN", "replay status mismatch")
    require(replay["matches_stored_residual_packet"] is True, "replay does not match residual packet")
    for section in ["phase_replay", "shift_replay"]:
        packet = replay[section]
        for key in [
            "projection_matches_stored_norm_sq",
            "residual_matches_stored_norm_sq",
            "target_minus_projection_minus_residual_norm_sq",
        ]:
            require(abs(packet[key]) <= TOL, f"{section} mismatch: {key}")
    require(replay["physical_application_claimed"] is False, "physical application overclaimed in replay")
    require(replay["honest_galerkin_selected_source_verified"] is False, "Galerkin source overclaimed")

    require(cutset["status"] == "TWO_LANE_CUTSET_SHARP_SM_PARITY_DYNAMIC_PACKET_OPEN", "cutset status mismatch")
    require("Lane A" in cutset["straight_path"], "straight path missing Lane A")
    require("Lane B" in cutset["superset_path"], "superset path missing Lane B")
    lane_a = cutset["if_lane_A_application_theorem_is_supplied"]
    require(lane_a["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "Lane A ATA mismatch")
    require(lane_a["A_transpose_b"] == [12.0, 12.0], "Lane A ATb mismatch")
    require(lane_a["deltaTheta_C1"] == [1.0, 1.0], "Lane A delta mismatch")
    require(lane_a["SM_parity_dynamic_packet_would_close"] is True, "Lane A SM parity implication missing")
    require(lane_a["no_knob_flavor_constants_would_close"] is False, "Lane A no-knob overclaim")
    require(cutset["if_lane_B_values_are_emitted"]["selected_source_verified_now"] is False, "Lane B overclaimed")
    for key in [
        "PhiFinC1_projector_application_promoted",
        "honest_Galerkin_C1_value_run_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
        "observed_data_used",
        "target_fitting_used",
    ]:
        require(cutset[key] is False, f"cutset overclaimed: {key}")

    closes = data["what_closes_now"]
    for key in [
        "canonical_fixed_fiber_projector_constructed",
        "projector_rank_idempotence_selfadjointness_verified",
        "residual_projector_replays_R_Z_R_X_exactly",
        "Lane_A_reduced_to_PhiFinC1_projector_application_theorem",
        "Lane_B_honest_galerkin_value_requirements_reemitted",
        "SM_parity_dynamic_packet_cutset_reduced_to_two_named_routes",
        "superset_strategy_made_explicit",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_PhiFinC1_applies_canonical_residual_projector",
        "selected_Hessian_or_vertex_operator_implements_projector",
        "honest_selected_Galerkin_C1_value_run",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(remains[key] is True, f"remaining gate missing: {key}")

    decision = data["promotion_decision"]
    require(decision["canonical_residual_projector_promoted_as_unique_mathematical_projector"] is True, "projector not promoted mathematically")
    for key in [
        "PhiFinC1_projector_application_promoted",
        "honest_Galerkin_C1_value_run_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
        "full_no_knob_flavor_closure_promoted",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")
    for key in [
        "closure_claimed",
        "SM_parity_dynamic_packet_closure_claimed",
        "true_SM_equivalence_claimed",
        "no_knob_closure_claimed",
        "observed_data_used",
        "target_fitting_used",
        "A_selected_claimed",
        "b_selected_claimed",
        "deltaTheta_C1_claimed",
        "Galerkin_C1_contractions_claimed",
    ]:
        require(data[key] is False, f"candidate overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("Lane A" in note, "note missing Lane A")
    require("Lane B" in note, "note missing Lane B")
    require("SM-parity" in note, "note missing SM-parity target")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
