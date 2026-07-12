"""Audit geometry-adapted Yukawa basis compression test."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_yukawageometryadaptedbasiscompression_or_nineslotwall"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BASIS = PACKET_DIR / "geometry_adapted_yukawa_basis_inventory.packet.json"
TESTS = PACKET_DIR / "basis_compression_rank_tests.packet.json"
DECISION = PACKET_DIR / "basis_compression_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_YukawaGeometryAdaptedBasisCompression_or_NineSlotWall_v1.md"

STATUS = "MTT_SELECTED_YUKAWA_GEOMETRY_ADAPTED_BASIS_COMPRESSION_TESTED_NINE_SLOT_WALL_RETAINED"
NEXT = "MTT_Selected_YukawaNewSourceRelation_or_NonInvertibleFlavorQuotientTest_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    basis = load(BASIS)
    tests = load(TESTS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["name"] == "YukawaGeometryAdaptedBasisCompressionNoGoTheorem", "theorem name")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem")

    require(basis["status"] == "GEOMETRY_ADAPTED_BASIS_INVENTORY_BUILT", "basis status")
    require(basis["noninvertible_compression_requires_new_source_relation"] is True, "noninvertible boundary")
    require(any("shared/common circle" in item for item in basis["closed_geometry_used"]), "circle geometry missing")
    require(any("qutrit family spectrum" in item for item in basis["closed_geometry_used"]), "qutrit geometry missing")
    for item in basis["admissible_basis_changes_if_family_resolution_retained"]:
        require(item["invertible"] is True, f"{item['basis']} not invertible")
    require(basis["observed_data_used_as_selector"] is False, "basis observed selector")
    require(basis["target_fitting_used"] is False, "basis target fitting")

    require(tests["status"] == "GEOMETRY_ADAPTED_BASIS_COMPRESSION_TESTED_NO_EXACT_REDUCTION", "tests status")
    for key in ["polynomial_coefficient_matrix", "lagrange_family_projector_matrix", "circle_fourier_family_matrix"]:
        packet = tests[key]
        require(packet["rank"] == 3, f"{key} rank")
        require(abs(packet["determinant"]) > 1.0e-9, f"{key} determinant")
        require(packet["rank2_exact_compression_closes"] is False, f"{key} rank2 overclosed")
        require(packet["best_rank2_relative_frobenius_residual"] > 0, f"{key} residual zero")
    checks = tests["basis_transform_checks"]
    require(checks["vandermonde_determinant_nonzero"] is True, "vandermonde singular")
    require(checks["polynomial_to_lagrange_reconstruction_max_abs_residual"] < 1.0e-12, "lagrange reconstruction")
    require(abs(abs(checks["circle_fourier_determinant"]) - 1.0) < 1.0e-12, "circle Fourier determinant")
    require(checks["rank_invariant_under_lagrange_transform"] is True, "lagrange rank invariant")
    require(checks["rank_invariant_under_circle_fourier_transform"] is True, "circle rank invariant")
    require(tests["best_approximate_compression"]["log_magnitude_matrix_rank2_relative_frobenius_residual"] < 0.05, "near-compression clue missing")
    require(tests["accepted_reduced_coefficient_rows"] == 0, "reduced rows overaccepted")
    require(tests["accepted_strict_no_knob_yukawa_rows"] == 0, "strict Yukawa rows overaccepted")
    require(tests["observed_data_used_as_selector"] is False, "tests observed selector")
    require(tests["target_fitting_used"] is False, "tests target fitting")

    require(decision["status"] == "NINE_SLOT_WALL_RETAINED_FOR_CURRENT_CIRCLE_BUNDLE_GEOMETRY", "decision status")
    require(decision["basis_only_reduction_below_nine_closed"] is False, "basis reduction overclosed")
    require(decision["current_geometry_forces_family_resolved_basis_up_to_invertible_rebasing"] is True, "basis forcing boundary")
    require(decision["invertible_geometry_adapted_rebasis_can_reduce_rank"] is False, "rank reduction overclaimed")
    require(decision["noninvertible_reduction_requires_new_selected_source_relation"] is True, "noninvertible next missing")
    require(decision["policy_source_value_row_count"] == 9, "policy row count")
    require(decision["strict_selected_no_knob_coefficient_source_row_count"] == 0, "strict source rows")
    require("does not prove that MTT can never reduce" in decision["what_this_does_not_prove"], "universal boundary missing")
    require(len(decision["legal_next_exits"]) == 3, "legal exits")
    require(len(decision["forbidden_exits"]) == 3, "forbidden exits")

    closure = data["closure_decision"]
    require(closure["geometry_adapted_basis_compression_tested"] is True, "closure not tested")
    require(closure["basis_only_reduction_below_nine_closed"] is False, "closure overclosed basis reduction")
    require(closure["nine_slot_policy_profile_operator_retained"] is True, "policy not retained")
    require(closure["policy_source_value_row_count"] == 9, "closure policy row count")
    require(closure["strict_selected_no_knob_coefficient_source_row_count"] == 0, "closure strict rows")
    require(closure["strict_no_knob_flavor_closure"] is False, "closure strict flavor overclosed")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(closure["full_no_knob_closed"] is False, "no-knob overclosed")

    nums = data["key_numbers"]
    require(nums["polynomial_coefficient_rank"] == 3, "key polynomial rank")
    require(nums["lagrange_projector_rank"] == 3, "key lagrange rank")
    require(nums["circle_fourier_rank"] == 3, "key Fourier rank")
    require(nums["best_rank2_log_magnitude_relative_residual"] > 0, "key near residual")
    require(data["closure_claimed"] is False, "candidate closure claimed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(cert["basis_only_reduction_below_nine_closed"] is False, "cert basis overclosed")
    require(cert["policy_source_value_row_count"] == 9, "cert policy rows")
    require(cert["strict_selected_no_knob_coefficient_source_row_count"] == 0, "cert strict rows")
    require(cert["closure_claimed"] is False, "cert closure")

    for phrase in [
        "bad basis choice",
        "circle/Fourier qutrit basis",
        "rank-2 relative Frobenius residual",
        "strict no-knob coefficient rows     = 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
