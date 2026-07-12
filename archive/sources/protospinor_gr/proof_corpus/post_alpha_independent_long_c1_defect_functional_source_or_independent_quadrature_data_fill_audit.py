from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_c1_defect_functional_source_or_independent_quadrature_data_fill_certificate.json"
)
STATUS = (
    "POST_ALPHA_INDEPENDENT_LONG_C1_DEFECT_FUNCTIONAL_SOURCE_OR_INDEPENDENT_QUADRATURE_DATA_FILL_"
    "REANCHORED_FUNCTIONAL_SOURCED_APPLICATION_OPEN"
)
NEXT = "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(cert["theorem"]["proved"] is True, "bridge theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    previous = packet["fresh_previous_certificate"]
    require(previous["theorem"]["proved"] is True, "previous theorem not proved")
    require(previous["frontier_decision"]["next_required_artifact"].endswith("QuadratureDataFill_v1"), "previous frontier drift")

    frontier = cert["frontier_decision"]
    require(frontier["unique_formal_C1_defect_functional_sourced"] is True, "functional not sourced")
    require(frontier["physical_PhiFinC1_application_rule_open"] is True, "physical application overclosed")
    require(frontier["independent_quadrature_data_open"] is True, "quadrature data overclosed")
    require(
        frontier["frontier_is_PhiFinC1_minimizes_defect_functional_or_independent_quadrature_table"] is True,
        "wrong frontier",
    )
    require(frontier["next_required_artifact"] == NEXT, "wrong next artifact")

    uniqueness = packet["c1_defect_functional_uniqueness_source"]
    require(
        uniqueness["status"] == "UNIQUE_QUADRATIC_DEFECT_FUNCTIONAL_SELECTED_AS_FORMAL_SOURCE",
        "wrong uniqueness status",
    )
    require(uniqueness["functional_name"] == "C1DefectLeakageFunctional", "functional drift")
    require(uniqueness["uniqueness_result"]["unique_up_to_overall_positive_scale"] is True, "uniqueness missing")
    require(uniqueness["uniqueness_result"]["overall_scale_cancels_from_euler_projection"] is True, "scale guard missing")
    require(uniqueness["what_this_does_not_source"]["physical_PhiFinC1_variation_minimizes_this_functional"] is True, "physical application overclaimed")

    quadrature = packet["independent_quadrature_data_fill_attempt"]
    require(quadrature["status"] == "DATA_REQUIREMENTS_RESTATED_NO_INDEPENDENT_VALUES_FILLED", "wrong quadrature status")
    require(not any(quadrature["input_data_available_now"].values()), "quadrature values overfilled")
    require(quadrature["observed_data_used"] is False, "observed data used")
    require(quadrature["target_fitting_used"] is False, "target fitting used")

    gap = packet["phifinc1_physical_application_source_gap"]
    require(gap["status"] == "FUNCTIONAL_SOURCED_PHYSICAL_APPLICATION_RULE_OPEN", "wrong gap status")
    require(gap["now_available"]["unique_formal_C1_defect_functional"] is True, "functional source missing")
    require(gap["remaining_physical_application_rule"]["not_proved_now"] is True, "physical rule overclosed")

    require(STATUS in note and NEXT in note and "functional-choice ambiguity" in note, "note missing essentials")
    print(
        "AUDIT_PASS: reanchored long-chain C1 defect functional source imported; "
        "physical PhiFinC1 binding and quadrature values remain open"
    )


if __name__ == "__main__":
    main()
