"""Audit dynamic first-response matrix attempt for scalar K-row emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicretardedoverlapderivativerows_or_tschemelambdahsourceexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROMOTION_ATTEMPT = PACKET_DIR / "dynamic_matrix_to_scalar_retarded_row_promotion_attempt.packet.json"
MISSING_EVALUATOR = PACKET_DIR / "rowwise_scalar_evaluator_missing.packet.json"
EMISSION = PACKET_DIR / "dynamic_retarded_row_emission_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_dynamic_retarded_row_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicRetardedOverlapDerivativeRows_or_TSchemeLambdaHSourceExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_DYNAMICRETARDEDOVERLAPDERIVATIVEROWS_OR_TSCHEMELAMBDAHSOURCEEXECUTION_"
    "BUILT_MATRIX_SUPPORT_SCALAR_EVALUATOR_OPEN"
)
NEXT = "MTT_Selected_RowwiseScalarRetardedOverlapQuadratureValues_or_TSchemeLambdaHExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its local theorem")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    promotion = load(PROMOTION_ATTEMPT)
    missing = load(MISSING_EVALUATOR)
    emission = load(EMISSION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("promotion", promotion),
        ("missing evaluator", missing),
        ("emission", emission),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")

    decision = data["closure_decision"]
    require(decision["dynamic_first_response_matrix_support_imported"] is True, "matrix support not imported")
    require(decision["dynamic_matrix_to_scalar_retarded_rows_tested"] is True, "promotion not tested")
    require(decision["matrix_support_promoted_to_scalar_retarded_rows"] is False, "matrix shortcut overpromoted")
    require(decision["rowwise_scalar_retarded_overlap_evaluator_emitted"] is False, "scalar evaluator overemitted")
    require(decision["selected_T_scheme_rows_emitted"] is False, "T_scheme overemitted")
    require(decision["selected_lambda_H_payload_emitted"] is False, "lambda_H overemitted")
    require(decision["accepted_selected_retarded_derivative_row_count"] == 0, "derivative rows overaccepted")
    require(decision["accepted_selected_K_source_row_count"] == 0, "K rows overaccepted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["controlled_empirical_K_import_available"] is True, "empirical K unavailable")
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclaimed")

    require(
        promotion["status"] == "SELECTED_DYNAMIC_MATRICES_AVAILABLE_NOT_SCALAR_RETARDED_ROWS",
        "promotion status mismatch",
    )
    require(promotion["value_role"] == "first selected dynamic matter/overlap operator packet", "value role changed")
    require(promotion["matrix_sectors_available"] == ["d", "e", "nuD", "u"], "matrix sectors changed")
    require(promotion["k_sectors_required"] == ["H", "d", "e", "u"], "K sectors changed")
    require(promotion["charged_k_sectors_with_matrix_support"] == ["d", "e", "u"], "charged support changed")
    require(promotion["higgs_lambda_matrix_support_available"] is False, "H matrix support overclaimed")
    support = promotion["first_response_support_closes"]
    for key in [
        "operator_values_selected_emitted",
        "primitive_C1_contractions_selected_emitted_first_response_layer",
        "same_source_dynamic_matter_overlap_packet_validates",
        "dynamic_value_acceptance_tests_pass_conditionally",
        "qualitative_non_scalar_tests_pass",
    ]:
        require(support[key] is True, f"support missing {key}")
    guardrails = promotion["guardrails"]
    require(guardrails["Yukawa_magnitudes_predicted"] is False, "Yukawa magnitudes overpredicted")
    require(guardrails["full_mass_spectrum_predicted"] is False, "mass spectrum overpredicted")
    require(guardrails["CKM_PMNS_measured_angles_predicted"] is False, "mixing angles overpredicted")
    require(guardrails["full_SM_no_knob_closed"] is False, "full no-knob overclosed")
    result = promotion["promotion_result"]
    require(result["matrix_support_accepted_as_same_source_support"] is True, "matrix support not accepted")
    require(result["matrix_support_promoted_to_scalar_retarded_rows"] is False, "matrix shortcut promoted")

    require(
        missing["status"] == "ROWWISE_SCALAR_RETARDED_OVERLAP_EVALUATOR_NOT_EMITTED",
        "missing evaluator status mismatch",
    )
    for key in [
        "physical_dotD_alpha1_available",
        "stationary_sector_transfer_available",
        "dynamic_first_response_support_available",
        "rowlocal_functional_contract_defined",
    ]:
        require(missing["available_inputs"][key] is True, f"available input missing {key}")
    for key in [
        "selected_ordered_zero_mode_basis_matrix_elements_executed",
        "selected_retarded_overlap_scalar_kernel_evaluated",
        "selected_finite_quadrature_Q_sel_executed",
        "selected_T_scheme_rows_instantiated",
        "selected_lambda_H_H_sector_payload_emitted",
    ]:
        require(missing["missing_inputs"][key] is True, f"missing input not recorded {key}")
    for phrase in [
        "build the selected ordered basis K_s,g for u,d,e,H inside the stationary sector packet",
        "evaluate L_rowlocal(s,g)=abs(<K_s,g, K_row(A_HYM,G,dotD_alpha1) K_s,g>) as scalar rows",
        "instantiate T_scheme(s,g) from the same-branch threshold/mass/profile functional",
        "emit lambda_H from the H-sector quartic/threshold payload",
    ]:
        require(phrase in missing["minimum_new_computation"], f"minimum computation missing {phrase}")
    for phrase in [
        "take matrix traces/eigenvalues from the first-response packet as K rows without the row-local functional",
        "borrow empirical K residuals as derivative rows",
        "fit T_scheme from observed Yukawa/Higgs values",
    ]:
        require(phrase in missing["forbidden_shortcuts"], f"forbidden shortcut missing {phrase}")

    require(
        emission["status"] == "DYNAMIC_MATRIX_SUPPORT_IMPORTED_ZERO_SCALAR_K_ROWS_EMITTED",
        "emission status mismatch",
    )
    require(emission["previous_row_count"] == 10, "previous row count mismatch")
    require(emission["row_count"] == 10, "row count mismatch")
    require(emission["empirical_K_row_count"] == 10, "empirical K count mismatch")
    require(emission["accepted_selected_retarded_derivative_row_count"] == 0, "retarded rows overaccepted")
    require(emission["accepted_T_scheme_row_count"] == 0, "T_scheme rows overaccepted")
    require(emission["accepted_selected_K_source_row_count"] == 0, "K rows overaccepted")
    require(emission["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(emission["lambda_H_value_row_emitted"] is False, "lambda_H overemitted")
    for row in emission["row_attempts"]:
        if row["sector"] == "H":
            require(row["selected_dynamic_matrix_support_available"] is False, "H matrix support overclaimed")
            require(row["selected_lambda_H_payload_emitted"] is False, "H lambda overemitted")
        else:
            require(row["selected_dynamic_matrix_support_available"] is True, f"{row['omega_id']} matrix support missing")
            require(row["selected_lambda_H_payload_emitted"] is None, f"{row['omega_id']} lambda marker mismatch")
        require(
            row["selected_dynamic_matrix_can_supply_scalar_retarded_row"] is False,
            f"{row['omega_id']} matrix shortcut accepted",
        )
        require(
            row["selected_rowwise_scalar_quadrature_evaluator_emitted"] is False,
            f"{row['omega_id']} scalar evaluator overemitted",
        )
        require(
            row["selected_retarded_overlap_derivative_row_emitted"] is False,
            f"{row['omega_id']} derivative row overemitted",
        )
        require(row["selected_T_scheme_row_emitted"] is False, f"{row['omega_id']} T_scheme overemitted")
        require(row["selected_K_threshold_row_emitted"] is False, f"{row['omega_id']} K row overemitted")
        require(row["accepted_as_no_knob_source_row"] is False, f"{row['omega_id']} no-knob overaccepted")
        require(row["observed_data_used_as_selector"] is False, f"{row['omega_id']} observed selector")
        require(row["target_fitting_used"] is False, f"{row['omega_id']} target fitting")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "selected dynamic first-response matrices imported as same-source support",
        "direct promotion of first-response matrices to scalar K rows tested and rejected",
        "H/lambda absence from dynamic matter matrix support recorded",
        "rowwise scalar quadrature/evaluator identified as the missing object",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed_here missing {phrase}")
    for phrase in [
        "selected rowwise scalar retarded-overlap quadrature values L_rowlocal(s,g)",
        "selected threshold-scheme rows T_scheme.*",
        "selected lambda_H H-sector quartic/threshold payload",
        "ten selected K_threshold rows",
    ]:
        require(phrase in cutset["still_open"], f"cutset still_open missing {phrase}")

    for phrase in [
        "selected dynamic matrix support imported : true",
        "matrix -> scalar K-row shortcut tested   : true",
        "matrix support promoted to scalar rows   : false",
        "rowwise scalar evaluator emitted         : false",
        "selected T_scheme rows emitted           : false",
        "selected lambda_H payload emitted        : false",
        "accepted selected K rows                 : 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
