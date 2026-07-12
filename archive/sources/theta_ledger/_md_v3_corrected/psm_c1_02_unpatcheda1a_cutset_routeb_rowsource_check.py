"""Audit the imported PSM-C1-02 A1a / Route-B row-source cutset."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
JSON_PATH = ROOT / "selected_psm_c1_02_unpatcheda1a_cutset_routeb_rowsource.import.json"
MD_PATH = ROOT / "PSM_C1_02_UnpatchedA1a_Cutset_or_RouteB_RowSource_Import_v1.md"

EXPECTED_STATUS = "IMPORTED_A1A_CUTSET_ROUTEB_ROWSOURCE_LAST_FIELD_OPEN"
EXPECTED_NEXT = "MTT_Selected_PSM_C1_02_PhysicalBoundaryFirstVariation_or_RouteBRowSourceIndependence_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    text = MD_PATH.read_text(encoding="utf-8", errors="ignore")

    require(data["status"] == EXPECTED_STATUS, "unexpected status")
    require(data["next_required_artifact"] == EXPECTED_NEXT, "unexpected next artifact")
    require(data["closure_claimed"] is False, "closure must not be claimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    route_a = data["route_A"]
    require(route_a["conditional_i10_i11_witness_passes"] is True, "conditional Route A witness should pass")
    require(route_a["current_i10_packet_rejected"] is True, "current Route A rejection not recorded")
    require(len(route_a["remaining_fields"]) == 3, "Route A should have three remaining fields")

    route_b = data["route_B"]
    for key in [
        "selected_basis_independent_of_residual_projector",
        "quadrature_rule_independent_of_locked_target",
        "all_72_primitive_rows_executed",
        "formal_110_rows_executed",
        "exactness_or_error_certificates_attached",
    ]:
        require(route_b[key] is True, f"Route B field should be closed: {key}")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "Route B missing field should stay open")
    require(route_b["target_theorem"] == "SelectedRowSourceIndependenceFromResidualProjectorReplayTheorem", "wrong target theorem")

    for phrase in [
        "rejects Route B on exactly one field",
        "source_independent_of_residual_projector_replay",
        "SelectedRowSourceIndependenceFromResidualProjectorReplayTheorem",
    ]:
        require(phrase in text, f"missing markdown phrase: {phrase}")

    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    print("PASS selected_psm_c1_02_unpatcheda1a_cutset_routeb_rowsource.import.json")


if __name__ == "__main__":
    main()
