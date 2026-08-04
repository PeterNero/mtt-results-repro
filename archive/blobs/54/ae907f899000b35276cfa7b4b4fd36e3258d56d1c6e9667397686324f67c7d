"""Audit dynamic transfer/Hessian/b_selected or honest Galerkin C1 value-fill gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"
CERT = ROOT / "certificates" / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicTransferHessian_bSelected_or_HonestGalerkinC1_ValueFill_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.py"

STATUS = (
    "MTT_SELECTED_DYNAMICTRANSFERHESSIAN_BSELECTED_OR_HONESTGALERKINC1_"
    "VALUEFILL_BUILT_CONDITIONAL_GRAM_EXACT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_SameSourceDynamicTransferIdentity_or_GalerkinC1Contractions_Emission_v1"
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

    packet = data["conditional_dynamic_transfer_coordinate_packet"]
    coord = packet["coordinate_system"]
    require(coord["codomain_real_dimension"] == 72, "codomain dimension mismatch")
    require(coord["sector_order"] == ["u", "d", "e", "nuD"], "sector order mismatch")
    require(coord["coordinates_per_sector"] == 18, "sector block size mismatch")
    require(packet["A_conditional_shape"] == [72, 2], "A shape mismatch")
    require(abs(packet["phase_column_norm_sq"] - 12.0) <= TOL, "phase norm mismatch")
    require(abs(packet["shift_column_norm_sq"] - 12.0) <= TOL, "shift norm mismatch")
    require(abs(packet["cross_inner_product"]) <= TOL, "columns not orthogonal")
    require(packet["Gram_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "Gram mismatch")
    require(packet["A_transpose_b_conditional"] == [12.0, 12.0], "dual coefficients mismatch")
    require(abs(packet["b_conditional_norm_sq"] - 24.0) <= TOL, "b norm mismatch")
    require(packet["b_conditional_sector_norm_sq"] == {"u": 6.0, "d": 6.0, "e": 6.0, "nuD": 6.0}, "sector norm mismatch")
    require(packet["rank"] == 2, "rank mismatch")
    require(packet["condition_number"] == 1.0, "condition number mismatch")
    require(all(abs(value - 1.0) <= TOL for value in packet["deltaTheta_conditional_from_Gram_solve"]), "deltaTheta mismatch")
    require(packet["residual_norm"] <= TOL, "residual nonzero")
    require(packet["matches_splitter_target_norm_sq"] is True, "splitter target mismatch")
    require(packet["matches_prior_weylpair_assembly"] is True, "prior assembly mismatch")

    hessian = data["hessian_bselected_fill_attempt"]
    require(hessian["attempted"] is True, "Hessian fill not attempted")
    require(hessian["conditional_Hessian_Gram_candidate"]["orthogonal_equal_norm_columns"] is True, "Gram candidate not exact")
    require(hessian["conditional_Hessian_Gram_candidate"]["selected_by_MTT"] is False, "Hessian overselected")
    require(hessian["conditional_b_candidate"]["selected_b_selected"] is False, "b_selected overselected")
    require(hessian["conditional_b_candidate"]["dual_source_coefficients_A_transpose_b"] == [12.0, 12.0], "dual source mismatch")
    for key, value in hessian["selected_value_slots_from_C1_response_audit"].items():
        require(value is False, f"selected value slot overclaimed: {key}")
    require(hessian["promoted"] is False, "Hessian/b promotion overclaimed")

    galerkin = data["honest_Galerkin_C1_value_fill_attempt"]
    require(galerkin["attempted"] is True, "Galerkin fill not attempted")
    require(galerkin["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING", "Galerkin status mismatch")
    require(galerkin["selected_source_verified"] is False, "Galerkin source oververified")
    require(galerkin["required_outputs"] == [
        "zero_mode_bases",
        "primitive_three_by_three_contraction_terms",
        "linear_response_matrices",
        "C33/nonzero-family-rank tests",
    ], "Galerkin outputs mismatch")
    require(galerkin["required_coordinate_compatibility"]["codomain_real_dimension"] == 72, "Galerkin codomain mismatch")
    require(galerkin["promoted"] is False, "Galerkin overpromoted")

    gate = data["promotion_gate"]
    require(gate["conditional_dynamic_value_packet_built"] is True, "conditional packet not built")
    require(gate["no_linear_algebra_obstruction"] is True, "linear algebra obstruction remains")
    for key in ["mass_split", "ckm_commutator", "pmns_commutator", "cp_odd"]:
        require(gate["qualitative_flavor_tests_pass_conditionally"][key] is True, f"conditional flavor test failed: {key}")
    for key in [
        "selected_dynamic_transfer_identity_emitted",
        "selected_Hessian_bselected_emitted",
        "honest_Galerkin_C1_contractions_emitted",
        "promote_to_selected_A_selected",
        "promote_to_selected_b_selected",
        "promote_to_selected_deltaTheta_C1",
    ]:
        require(gate[key] is False, f"promotion overclaimed: {key}")

    closes = data["what_closes_now"]
    for key in [
        "exact_72_real_coordinate_system_fixed",
        "conditional_A_transpose_A_Gram_computed",
        "conditional_b_conditional_computed",
        "conditional_deltaTheta_Gram_solve_exact",
        "linear_algebra_obstruction_removed",
        "selected_value_source_gap_reduced_to_same_source_dynamic_transfer_or_honest_Galerkin",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_same_source_dynamic_transfer_identity",
        "selected_Hessian_blocks",
        "selected_grad_source_vector_or_b_selected",
        "selected_A_selected",
        "selected_b_selected",
        "honest_Galerkin_C1_contractions",
        "full_SM_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    for key in [
        "closure_claimed",
        "observed_data_used",
        "target_fitting_used",
        "selected_dynamic_transfer_identity_claimed",
        "selected_Hessian_blocks_claimed",
        "A_selected_claimed",
        "b_selected_claimed",
        "deltaTheta_C1_claimed",
        "Galerkin_C1_contractions_claimed",
    ]:
        require(data[key] is False, f"guardrail overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
