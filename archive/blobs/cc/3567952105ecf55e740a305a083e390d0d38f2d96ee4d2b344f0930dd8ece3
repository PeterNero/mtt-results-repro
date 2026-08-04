"""Audit selected HYM-overlap value-source / qutrit spectral packaging."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MATRIX = PACKET_DIR / "qutrit_weyl_27x27_matrix_realization.packet.json"
SPECTRAL = PACKET_DIR / "finite_spectral_triple_packaging.packet.json"
VALUE = PACKET_DIR / "hym_overlap_value_source_obstruction_and_lift.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_qutrit_spectral_packaging.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HYMOverlapValueSourceTheorem_or_QutritSpectralTriplePackaging_v1.md"
STATUS = "MTT_SELECTED_HYMOVERLAPVALUESOURCE_OR_QUTRITSPECTRALTRIPLEPACKAGING_FINITE_27X27_PACKAGE_CLOSED_VALUE_ROWS_OPEN"
NEXT = "MTT_Selected_HYMOverlapValueSourceTheorem_or_SelectedOverlapKernelRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    data = load(DATA)
    matrix = load(MATRIX)
    spectral = load(SPECTRAL)
    value = load(VALUE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["closure_claimed"] is True, "closure flag missing")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(matrix["carrier_dimension"] == 27, "carrier dimension mismatch")
    require(matrix["qutrit_weyl_basis_dimension"] == 9, "qutrit basis mismatch")
    require(matrix["left_Z27_rank"] == 27, "L_Z rank mismatch")
    require(matrix["left_X27_rank"] == 27, "L_X rank mismatch")
    require(matrix["algebra_basis_rank_in_End_HQ"] == 27, "algebra rank mismatch")
    require(matrix["algebra_basis_expected_rank"] == 27, "expected rank mismatch")
    require(matrix["left_Z27_sparse_nonzero_count"] == 27, "L_Z sparse count mismatch")
    require(matrix["left_X27_sparse_nonzero_count"] == 27, "L_X sparse count mismatch")
    require(matrix["weyl_relation_error_frobenius"] < 1e-12, "Weyl relation error too large")
    require(matrix["weyl_orthogonality_max_abs_error"] < 1e-12, "orthogonality error too large")
    require(matrix["left_action_relation_error_frobenius"] < 1e-12, "left relation error too large")
    require(matrix["left_Z27_unitarity_error_frobenius"] < 1e-12, "L_Z unitarity error too large")
    require(matrix["left_X27_unitarity_error_frobenius"] < 1e-12, "L_X unitarity error too large")

    require(spectral["selected_from_previous_gate"] is True, "previous selected gate not imported")
    require(spectral["hilbert_dimension"] == 27, "spectral dimension mismatch")
    require(spectral["algebra_vector_rank"] == 27, "spectral algebra rank mismatch")
    require(spectral["response_operator_imports"]["sector_response_matrices_promoted_strict"] is True, "dynamic C1 import missing")
    require("full_Connes_real_spectral_triple_axioms" in spectral["not_claimed"], "Connes guardrail missing")

    require(value["hym_overlap_value_source_theorem_closed"] is False, "HYM values overclosed")
    require(value["current_accepted_scalar_value_rows"] == 0, "accepted scalar rows overclaimed")
    require(value["required_total_row_count"] == 10, "required row count mismatch")
    require(value["selected_projector_values_promoted"] if "selected_projector_values_promoted" in value else True, "unused compatibility")
    require(value["degeneracy_nogo_imported"] is True, "degeneracy no-go missing")

    require(cutset["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("SelectedFiniteQutritSpectralPackagingTheorem" in cutset["closed_now"], "packaging theorem not closed")
    require("SelectedHYMOverlapValueSourceTheorem" in cutset["still_open"], "HYM value source not open")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(cert["finite_qutrit_spectral_package_closed"] is True, "certificate package not closed")
    require(cert["hym_overlap_value_source_rows_closed"] is False, "certificate value overclosed")

    for phrase in [
        "actual 27-by-27 left-action matrix realization",
        "not a full Connes finite spectral triple claim",
        "not an E6 identity claim",
        "accepted scalar source rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
