"""Audit CKM sector-pair weight source reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ckmsectorpairweightsourcetheorem_or_fullflavorgalerkinrun"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
IMPORT = PACKET_DIR / "second_order_orbit_import_for_ckm_weights.packet.json"
EXTRACTION = PACKET_DIR / "orbit_invariant_weight_extraction_attempt.packet.json"
REDUCTION = PACKET_DIR / "ckm_weight_scalar_functional_reduction.packet.json"
DECISION = PACKET_DIR / "ckm_weight_source_acceptance_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CKMSectorPairWeightSourceTheorem_or_FullFlavorGalerkinRun_v1.md"

STATUS = "MTT_SELECTED_CKMSECTORPAIR_WEIGHT_SOURCE_ATTEMPT_ORBIT_IMPORTED_SCALAR_EVALUATOR_OPEN"
NEXT = "MTT_Selected_CKMWeightScalarEvaluator_or_SelectedFlavorGalerkinValues_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    imported = load(IMPORT)
    extraction = load(EXTRACTION)
    reduction = load(REDUCTION)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["name"] == "CKMSectorPairWeightSourceReductionTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")

    closure = data["closure_decision"]
    for key in [
        "second_order_orbit_imported",
        "pure_weyl_lambda_orbit_rows_imported",
        "orbit_invariant_extraction_attempt_executed",
        "ckm_weight_scalar_functional_reduction_closed",
    ]:
        require(closure[key] is True, f"missing true closure flag: {key}")
    require(closure["selected_weight_rows"] == 0, "selected weights overaccepted")
    require(closure["accepted_exact_ckm_correction_rows"] == 0, "exact CKM corrections overaccepted")
    require(closure["accepted_no_knob_CKM_angle_rows"] == 0, "no-knob angles overaccepted")
    for key in [
        "CKM_angle_magnitudes_derived_exact",
        "Jarlskog_source_derived_without_measured_angles",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
    ]:
        require(closure[key] is False, f"overclaim: {key}")

    require(imported["status"] == "SECOND_ORDER_ORBIT_AND_PURE_WEYL_ROWS_IMPORTED_FOR_CKM_WEIGHT_SOURCE_ATTEMPT", "import status")
    require(imported["pure_weyl_rows_closed"] is True, "pure rows not closed")
    require(imported["lambda_orbit_scaled_pure_rows_closed"] is True, "lambda orbit rows not closed")
    require(imported["second_order_orbit_matrix_packet_closed"] is True, "orbit packet not closed")
    require(imported["qualitative_three_family_splitting_closed"] is True, "three family not closed")
    require(imported["qualitative_CP_nonzero_closed"] is True, "CP not closed")
    require(imported["individual_lambda_representative_selected"] is False, "lambda representative overselected")
    require(imported["orbit_invariants"]["hermitian_spectrum_each_sector"] == [1.0, 4.0, 7.0], "spectrum")
    require(imported["orbit_invariants"]["commutator_norm_sq"] == 324.0, "comm norm")
    require(imported["orbit_invariants"]["cp_odd_exact_magnitude"] == "972*sqrt(3)", "CP magnitude")
    require(imported["target_fitting_used"] is False, "import target fit")

    require(extraction["status"] == "ORBIT_INVARIANT_WEIGHT_EXTRACTION_EXECUTED_NO_ACCEPTED_ROWS", "extraction status")
    require(extraction["candidate_count"] > 1000, "extraction too small")
    require(extraction["accepted_weight_rows"] == 0, "extraction accepted weights")
    require(extraction["accepted_exact_ckm_correction_rows"] == 0, "extraction accepted corrections")
    for row in ["W12", "W23", "W13"]:
        require(extraction["best_by_weight"][row]["accepted"] is False, f"accepted {row}")
        require(extraction["best_by_weight"][row]["relative_residual"] >= 0.0, f"residual {row}")
    require(extraction["observed_data_used_as_selector"] is False, "extraction observed selector")
    require(extraction["target_fitting_used"] is False, "extraction target fit")

    require(reduction["status"] == "CKM_WEIGHT_SOURCE_REDUCED_TO_SELECTED_SCALAR_EVALUATOR", "reduction status")
    require(reduction["weight_rows"] == ["W12", "W23", "W13"], "weight rows")
    require("selected scalar evaluator E_CKM^12" in reduction["what_remains_missing"], "E12 missing")
    require("pure Weyl coefficient/source rows" in reduction["what_is_no_longer_missing"], "pure rows not retired")
    require("E_CKM^ij = Tr_N" in reduction["minimal_evaluator"], "minimal evaluator")
    require(reduction["observed_data_used_as_selector"] is False, "reduction observed selector")
    require(reduction["target_fitting_used"] is False, "reduction target fit")

    require(decision["status"] == "ORBIT_LAYER_IMPORTED_WEIGHT_SOURCE_ROWS_REMAIN_OPEN", "decision status")
    require(decision["second_order_orbit_imported"] is True, "decision orbit")
    require(decision["orbit_invariant_extraction_attempt_executed"] is True, "decision extraction")
    require(decision["ckm_weight_scalar_functional_reduction_closed"] is True, "decision reduction")
    require(decision["selected_weight_rows"] == 0, "decision weights")
    require(decision["accepted_exact_ckm_correction_rows"] == 0, "decision corrections")
    require(decision["next_required_artifact"] == NEXT, "decision next")
    for key in [
        "CKM_angle_magnitudes_derived_exact",
        "Jarlskog_source_derived_without_measured_angles",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")

    nums = data["key_numbers"]
    require(nums["orbit_spectrum"] == [1.0, 4.0, 7.0], "key spectrum")
    require(nums["commutator_norm_sq"] == 324.0, "key comm norm")
    require(abs(nums["cp_odd_abs"] - 1683.5533849569488) < 1e-9, "key CP")
    require(abs(nums["q448_weights"]["W12"] - 1.41236734693301) < 1e-12, "W12")
    require(abs(nums["q448_weights"]["W23"] - 6.829844553504131) < 1e-12, "W23")
    require(abs(nums["q448_weights"]["W13"] - 23.10800759390179) < 1e-12, "W13")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector")
    require(data["observed_data_used_for_postcheck"] is True, "postcheck")
    require(data["target_fitting_used"] is False, "target fitting")
    require(cert["selected_weight_rows"] == 0, "cert weights")
    require(cert["ckm_weight_scalar_functional_reduction_closed"] is True, "cert reduction")
    require(cert["closure_claimed"] is False, "cert closure")
    require("Accepted selected weight rows remain `0/3`" in note, "note boundary")
    require(NEXT in note, "note next")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
