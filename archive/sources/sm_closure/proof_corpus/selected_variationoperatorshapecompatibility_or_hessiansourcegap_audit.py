"""Audit selected_variationoperatorshapecompatibility_or_hessiansourcegap."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_variationoperatorshapecompatibility_or_hessiansourcegap.candidate.json"
ROUTING = ROOT / "candidate_data" / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "variation_operator_72_slot_routing.packet.json"
COMPAT = ROOT / "candidate_data" / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "variation_operator_shape_compatibility.packet.json"
GAP = ROOT / "candidate_data" / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "hessian_source_and_selection_gap.packet.json"
CERT = ROOT / "certificates" / "selected_variationoperatorshapecompatibility_or_hessiansourcegap_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_VariationOperatorShapeCompatibility_or_HessianSourceGap_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    routing = load(ROUTING)
    compat = load(COMPAT)
    gap = load(GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_VARIATIONOPERATORSHAPECOMPATIBILITY_BUILT_HESSIAN_SOURCE_GAP_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(routing["row_count"] == 72, "wrong row count")
    require(routing["phase_R_Z_rows"] == 36, "wrong phase count")
    require(routing["shift_R_X_rows"] == 36, "wrong shift count")
    require(all(row["operator_shape_attached"] is True for row in routing["rows"]), "shape missing")
    require(all(row["operator_selected_as_source_now"] is False for row in routing["rows"]), "operator source overclosed")
    require(all(row["hessian_counterterm_sourced"] is False for row in routing["rows"]), "hessian overclosed")
    require(compat["compatible_with_72_slot_table"] is True, "compatibility not closed")
    require(compat["operator_shapes_selected_as_source_now"] is False, "source selection overclosed")
    require(compat["all_rows_provenance_independent"] is False, "all rows provenance unexpectedly promoted")
    require(gap["closed_now"]["variation_operator_shapes_routed_to_all_72_slots"] is True, "routing gap not closed")
    require(gap["not_closed"]["selected_phase_shift_variation_operators_pre_residual"] is True, "variation source gap missing")
    require(gap["not_closed"]["selected_hessian_counterterm_source"] is True, "hessian gap missing")
    require(gap["not_closed"]["selected_b_vector_source"] is True, "b source gap missing")
    require(cert["shape_compatibility_closed"] is True, "cert compatibility not closed")
    require(cert["variation_operators_selected_as_source"] is False, "cert source overclosed")
    require(cert["hessian_counterterm_source_closed"] is False, "cert hessian overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("This is not source promotion" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
