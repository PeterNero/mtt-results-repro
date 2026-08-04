"""Audit zero-mode/Hessian/primitive-row execution or pure-Weyl rows gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_zeromodehessianprimitiverowexecution_or_pureweylrows"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PURE_ROWS = PACKET_DIR / "identity_free_pure_weyl_rows.packet.json"
HESSIAN_GATE = PACKET_DIR / "zeromode_hessian_payload_reconciliation.packet.json"
PROMOTION = PACKET_DIR / "pure_weyl_promotion_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_identity_free_pure_weyl_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ZeroModeHessianPrimitiveRowExecution_or_PureWeylRows_v1.md"

STATUS = (
    "MTT_SELECTED_ZEROMODEHESSIANPRIMITIVEROWEXECUTION_OR_PUREWEYLROWS_"
    "BUILT_IDENTITY_FREE_PURE_WEYL_ROWS_CLOSED_LAMBDA_OPEN"
)
NEXT = "MTT_Selected_PureWeylLambdaRepresentative_or_HigherResponseScalarRows_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], errors: list[str], label: str, *, closure: bool = False) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is closure, f"{label} closure flag mismatch", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    pure_rows = load(PURE_ROWS)
    hessian = load(HESSIAN_GATE)
    promotion = load(PROMOTION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")
    errors: list[str] = []

    expect(data.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(data.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(data.get("theorem", {}).get("proved") is True, "theorem should be proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem should be proved", errors)

    guard(data, errors, "candidate", closure=False)
    guard(cert, errors, "certificate", closure=False)
    guard(pure_rows, errors, "pure_rows", closure=True)
    guard(hessian, errors, "hessian_gate", closure=False)
    guard(promotion, errors, "promotion", closure=False)
    guard(cutset, errors, "cutset", closure=False)

    expect(
        pure_rows.get("status") == "IDENTITY_FREE_PURE_RZ_RX_PRIMITIVE_ROWS_CLOSED",
        "pure rows status mismatch",
        errors,
    )
    expect(pure_rows.get("identity_subtraction_used") is False, "identity subtraction was used", errors)
    expect(pure_rows.get("dynamic_C1_identity_row_emitted") is False, "dynamic identity overemitted", errors)
    expect(pure_rows.get("row_counts", {}).get("R_Z") == 18, "R_Z row count mismatch", errors)
    expect(pure_rows.get("row_counts", {}).get("R_X") == 18, "R_X row count mismatch", errors)
    expect(pure_rows.get("row_counts", {}).get("zero_route") == 36, "zero route row count mismatch", errors)
    expect(pure_rows.get("row_counts", {}).get("total") == 72, "total row count mismatch", errors)
    expect(pure_rows.get("sector_coverage", {}).get("R_Z_sectors") == ["e", "u"], "R_Z sector coverage mismatch", errors)
    expect(pure_rows.get("sector_coverage", {}).get("R_X_sectors") == ["d", "nuD"], "R_X sector coverage mismatch", errors)
    exactness = pure_rows.get("exactness", {})
    for key in ["R_Z_rows_exact", "R_X_rows_exact", "all_72_exact", "all_72_match_formal_packet"]:
        expect(exactness.get(key) is True, f"exactness missing: {key}", errors)
    expect(exactness.get("max_abs_error_against_formal_packet", 1.0) < 1e-12, "formal packet error too high", errors)
    source = pure_rows.get("source_promotion", {})
    for key in [
        "VSD01_source_assembly_subgate_closed",
        "PhysicalPhiFinC1ActionSource_promoted",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
    ]:
        expect(source.get(key) is True, f"source promotion missing: {key}", errors)
    expect(pure_rows.get("accepted_as_unscaled_selected_pure_weyl_primitive_rows") is True, "pure rows not accepted", errors)

    hym = hessian.get("hym_projector_values", {})
    expect(hym.get("finite_model_active_projector_values_emitted") is True, "HYM finite values missing", errors)
    expect(hym.get("ordered_zero_mode_basis_ids_emitted") is True, "zero-mode ids missing", errors)
    expect(hym.get("positive_model_complement_gap_emitted") is True, "positive gap missing", errors)
    expect(hym.get("selected_HYM_projector_values_promoted") is False, "HYM source overpromoted", errors)
    expect(hym.get("selected_rho_s_promoted") is False, "rho_s overpromoted", errors)
    formal = hessian.get("formal_hessian_source_rows", {})
    expect(formal.get("formal_110_rows_executed") is True, "formal 110 not executed", errors)
    expect(formal.get("hessian_source_row_count") == 2, "hessian row count mismatch", errors)
    expect(formal.get("same_branch_source_stack_promotes_A_b_deltaTheta") is True, "A/b/delta not promoted", errors)
    dynamic = hessian.get("dynamic_payload_inventory", {})
    expect(dynamic.get("accepted_dynamic_payload_row_count") == 0, "dynamic payload rows overaccepted", errors)
    expect(dynamic.get("higher_response_execution_inputs_available") is False, "higher response inputs overclaimed", errors)

    closes = promotion.get("what_closes_now", {})
    for key in [
        "unscaled_selected_pure_R_Z_rows",
        "unscaled_selected_pure_R_X_rows",
        "identity_subtraction_no_longer_needed_for_unscaled_pure_rows",
        "VSD01_primitive_source_reconciled_with_pure_rows",
        "first_response_dynamic_tensor_subgate_preserved",
        "same_source_dynamic_matter_overlap_packet_preserved",
    ]:
        expect(closes.get(key) is True, f"promotion close flag missing: {key}", errors)
    remains = promotion.get("what_remains_open", {})
    for key in [
        "lambda_static_coefficient_representative",
        "lambda_static_times_R_Z_R_X_scaled_rows",
        "selected_second_order_physical_matrices",
        "selected_HYM_projector_source_promotion",
        "higher_response_Rtheta_scalar_rows",
        "Yukawa_mass_mixing_value_closure",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        expect(remains.get(key) is True, f"remaining blocker missing: {key}", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("identity_free_unscaled_pure_Weyl_rows_closed") is True, "identity-free rows not closed", errors)
    for key in [
        "dynamic_C1_identity_row_emitted",
        "identity_subtraction_promoted",
        "lambda_static_coefficient_representative_selected",
        "selected_second_order_physical_matrices_promoted",
        "selected_HYM_projector_values_promoted",
        "higher_response_Rtheta_scalar_rows_executed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(decision.get(key) is False, f"decision overclosed: {key}", errors)
        expect(cert.get(key) is False, f"certificate overclosed: {key}", errors)

    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    expect("R_Z rows = 18" in note, "note missing R_Z count", errors)
    expect("lambda_static representative selected = false" in note, "note missing lambda guard", errors)
    expect("full no-knob closure                  = false" in note, "note missing no-knob guard", errors)

    if errors:
        print("Zero-mode/Hessian primitive row audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Zero-mode/Hessian primitive row audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
