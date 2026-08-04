"""Audit selected qutrit-Weyl carrier theorem / HYM overlap value-source gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_qutritweylcarriertheorem_or_hymoverlapvaluesourcegate"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_QutritWeylCarrierTheorem_or_HYMOverlapValueSourceGate_v1.md"

STATUS = "MTT_SELECTED_QUTRITWEYLCARRIERTHEOREM_OR_HYMOVERLAPVALUESOURCEGATE_CLOSED_CARRIER_SELECTED_VALUE_ROWS_OPEN"
NEXT = "MTT_Selected_HYMOverlapValueSourceTheorem_or_QutritSpectralTriplePackaging_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["closure_claimed"] is True, "carrier gate should close")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM equivalence overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    carrier = data["selected_qutrit_weyl_carrier_theorem"]
    require(carrier["proved"] is True, "carrier theorem not proved")
    require(carrier["finite_rank"] == 27, "rank mismatch")
    require(carrier["carrier"] == "Q_sel^U", "carrier mismatch")
    require(carrier["raw_27_mode_truncation_claimed_closed"] is False, "raw truncation overclaimed")
    require(carrier["source_level_qutrit_weyl_carrier_closed"] is True, "source carrier missing")
    require(carrier["finite_stone_von_neumann_projective_rhoe_selected_up_to_gauge"] is True, "Stone-von Neumann import missing")
    require(carrier["active_shift"] == [1, 1], "active shift mismatch")

    dyn = data["dynamic_c1_carrier_evaluation"]
    require(dyn["proved"] is True, "dynamic C1 eval not proved")
    require(dyn["R_Z"]["coefficient_count"] == 6, "R_Z coefficient mismatch")
    require(abs(dyn["R_Z"]["norm_sq"] - 4.0) < 1e-12, "R_Z norm mismatch")
    require(dyn["R_Z"]["reconstruction_error_norm_sq_less_than"] <= 1e-30, "R_Z error guard missing")
    require(dyn["R_X"]["coefficient_count"] == 3, "R_X coefficient mismatch")
    require(abs(dyn["R_X"]["norm_sq"] - 2.0) < 1e-12, "R_X norm mismatch")
    require(dyn["R_X"]["reconstruction_error_norm_sq_less_than"] <= 1e-30, "R_X error guard missing")
    require(dyn["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(dyn["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(dyn["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta mismatch")
    require(dyn["row_counts"]["formal_110_total_rows"] == 110, "row count mismatch")

    gate = data["hym_overlap_value_source_gate"]
    require(gate["selected_as_next_route"] is True, "HYM route not selected")
    require(gate["value_rows_emitted_now"] is False, "value rows overemitted")
    require(gate["current_degeneracy_nogo_imported"] is True, "degeneracy no-go missing")
    require(gate["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")

    require(data["e6_status"]["claim_e6_identity_now"] is False, "E6 overclaimed")
    require(data["decision"]["selected_qutrit_weyl_carrier_theorem_closed"] is True, "decision carrier mismatch")
    require(data["decision"]["hym_overlap_value_source_rows_closed"] is False, "decision value overclosed")
    require(data["decision"]["next_artifact"] == NEXT, "next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")

    for phrase in [
        "raw 27-mode truncation is not claimed closed",
        "R_Z coefficient count",
        "HYM/Strominger overlap theorem",
        "does not identify `Q_sel^U` with the E6 fundamental representation",
        f"MTT_Selected_HYMOverlapValueSourceTheorem_or_QutritSpectralTriplePackaging_v1",
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
