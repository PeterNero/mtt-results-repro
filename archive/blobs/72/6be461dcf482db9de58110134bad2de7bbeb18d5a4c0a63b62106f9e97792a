"""Audit the geometric Cech/HYM obligation reduction after BN27 one-premise closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_geometric_cechhym_obligation_reduction_after_onepremise.py"

SLUG = "selected_geometric_cechhym_obligation_reduction_after_onepremise"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Geometric_CechHYM_Obligation_Reduction_After_OnePremise_v1.md"
CECH_PACKET = PACKET_DIR / "cech_goodcover_to_class_representative_reduction.packet.json"
HYM_PACKET = PACKET_DIR / "hym_support_to_ende_value_obligation_reduction.packet.json"
GATE_PACKET = PACKET_DIR / "onepremise_geometric_connection_row_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cechclass_or_hymende_values_contract.packet.json"

STATUS = (
    "MTT_SELECTED_GEOMETRIC_CECHHYM_OBLIGATION_REDUCTION_AFTER_ONEPREMISE_"
    "REDUCED_TO_CLASS_REPRESENTATIVE_AND_HYMENDE_VALUES"
)
NEXT = "MTT_Selected_CechClassRepresentative_or_HYMEndEConnectionValues_v1"
PREMISE_NAME = "SelectedBN27ThresholdSourceEmissionPrinciple"
GEOMETRIC_ROWS = [
    "cech_transition_cocycles",
    "selected_HYM_or_projective_connection_coefficients",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    cech = load(CECH_PACKET)
    hym = load(HYM_PACKET)
    gate = load(GATE_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, cech, hym, gate, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["premise_name"] == PREMISE_NAME, "premise name mismatch")
    require(decision["premise_count"] == 1, "premise count mismatch")
    require(decision["strict_final_connection_tables_accepted"] == 4, "strict count drifted")
    require(decision["one_premise_final_connection_tables_accepted"] == 6, "one-premise count drifted")
    require(decision["geometric_connection_rows_required"] == 2, "geometric required mismatch")
    require(decision["geometric_connection_rows_accepted"] == 0, "geometric rows overaccepted")
    require(decision["cech_goodcover_knob_removed"] is True, "Cech support missing")
    require(decision["cech_row_reduced_to_selected_class_representative"] is True, "Cech reduction missing")
    require(decision["hym_support_imported"] is True, "HYM support missing")
    require(decision["hym_row_reduced_to_selected_EndE_values"] is True, "HYM reduction missing")
    require(decision["cech_transition_cocycles_final_row_accepted"] is False, "Cech row overaccepted")
    require(
        decision["selected_HYM_or_projective_connection_coefficients_final_row_accepted"] is False,
        "HYM row overaccepted",
    )
    require(decision["strict_no_knob_closed"] is False, "strict no-knob overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim")

    require(cech["row"] == "cech_transition_cocycles", "Cech row id")
    require(cech["accepted_as_final_connection_table_row"] is False, "Cech packet overaccepted")
    require(cech["support_imported"]["good_cover_removed_as_physical_knob"] is True, "good-cover knob not removed")
    require(cech["support_imported"]["finite_to_smooth_flat_gerbe_source_functor"] is True, "flat functor missing")
    require(cech["reduced_obligation"]["selected_s3_differential_cohomology_class"] is True, "S3 class missing")
    require(cech["still_open"]["literal_Deligne_Cech_transition_data_emitted"] is False, "literal Cech data overemitted")
    require(cech["still_open"]["cech_transition_cocycles_final_row_accepted"] is False, "Cech final overaccepted")

    require(hym["row"] == "selected_HYM_or_projective_connection_coefficients", "HYM row id")
    require(hym["accepted_as_final_connection_table_row"] is False, "HYM packet overaccepted")
    require(hym["support_imported"]["diagonal_rank2_HYM_residual_slot_closed"] is True, "rank2 HYM support missing")
    require(hym["support_imported"]["directionwise_End0_D_E_connection_matrices"] is True, "End0 support missing")
    require(hym["support_imported"]["finite_values_shape_complete"] is True, "finite shape support missing")
    require(hym["reduced_obligation"]["equivalent_EndE_operator_values_allowed"] is True, "EndE exit missing")
    require(hym["still_open"]["selected_operator_values_closed"] is False, "selected operator values overclosed")
    require(hym["still_open"]["actual_visible_operator_payload_emitted"] is False, "visible payload overemitted")
    require(
        hym["still_open"]["selected_HYM_or_projective_connection_coefficients_final_row_accepted"] is False,
        "HYM final overaccepted",
    )

    require(gate["premise_name"] == PREMISE_NAME, "gate premise mismatch")
    require(gate["strict_final_connection_table_count"] == "4/8", "gate strict count")
    require(gate["one_premise_final_connection_table_count"] == "6/8", "gate one-premise count")
    require(gate["geometric_connection_rows_required"] == 2, "gate required mismatch")
    require(gate["geometric_connection_rows_accepted"] == 0, "gate overaccepted rows")
    require(gate["geometric_rows"] == GEOMETRIC_ROWS, "gate rows mismatch")
    require(gate["cech_row_accepted"] is False, "gate Cech overaccepted")
    require(gate["hym_row_accepted"] is False, "gate HYM overaccepted")

    require(next_packet["remaining_exact_rows"] == GEOMETRIC_ROWS, "next remaining rows mismatch")
    require(next_packet["one_premise_count_before_next"] == "6/8", "next before count")
    require(next_packet["one_premise_count_after_success"] == "8/8", "next after count")
    require(
        "abstract HYM existence alone" in next_packet["must_not_count_as_final_rows"],
        "next packet missing HYM guard",
    )
    require(
        "good-cover refinement invariance alone" in next_packet["must_not_count_as_final_rows"],
        "next packet missing Cech guard",
    )

    require(cert["one_premise_final_connection_tables_accepted"] == 6, "cert count")
    require(cert["geometric_connection_rows_accepted"] == 0, "cert geometric overaccepted")
    require(cert["remaining_geometric_connection_rows"] == GEOMETRIC_ROWS, "cert remaining rows")
    require(cert["cech_row_reduced_not_closed"] is True, "cert Cech boundary")
    require(cert["hym_row_reduced_not_closed"] is True, "cert HYM boundary")
    require(cert["strict_no_knob_closed"] is False, "cert strict overclaim")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM overclaim")

    require("final connection tables: `6/8`" in note, "note count")
    require("geometric rows accepted: `0/2`" in note, "note geometric count")
    require("does not close strict no-knob SM equivalence" in note, "note guard")
    require(NEXT in note, "note next")

    print("Geometric Cech/HYM obligation reduction audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
