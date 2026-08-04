from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_c1_defect_functional_source_or_quadrature_data_fill_certificate.json"
STATUS = "POST_ALPHA_C1_DEFECT_FUNCTIONAL_SOURCE_IMPORTED_PHYSICAL_APPLICATION_OPEN"
NEXT = "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(cert["theorem"]["proved"] is True, "functional source theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    decision = cert["frontier_decision"]
    require(decision["unique_formal_C1_defect_functional_sourced"] is True, "functional source missing")
    require(decision["physical_PhiFinC1_application_rule_open"] is True, "physical application should remain open")
    require(decision["independent_quadrature_data_open"] is True, "quadrature data should remain open")
    require(decision["frontier_is_PhiFinC1_minimization_or_independent_quadrature_table"] is True, "wrong frontier")
    require(decision["next_required_artifact"] == NEXT, "wrong next artifact")

    functional = packet["c1_defect_functional_uniqueness_source"]
    require(functional["status"] == "UNIQUE_QUADRATIC_DEFECT_FUNCTIONAL_SELECTED_AS_FORMAL_SOURCE", "wrong functional status")
    require(functional["functional_name"] == "C1DefectLeakageFunctional", "functional name drift")
    require(functional["uniqueness_result"]["unique_up_to_overall_positive_scale"] is True, "scale uniqueness missing")
    require(functional["uniqueness_result"]["overall_scale_cancels_from_euler_projection"] is True, "scale cancellation missing")
    require(functional["what_this_does_not_source"]["physical_PhiFinC1_variation_minimizes_this_functional"] is True, "physical gap hidden")

    quadrature = packet["independent_quadrature_data_fill_attempt"]
    require(quadrature["status"] == "DATA_REQUIREMENTS_RESTATED_NO_INDEPENDENT_VALUES_FILLED", "wrong quadrature status")
    require(all(value is False for value in quadrature["input_data_available_now"].values()), "independent data overclaimed")
    require(len(quadrature["required_values"]) == 6, "required value count drift")

    gap = packet["phifinc1_physical_application_source_gap"]
    require(gap["status"] == "FUNCTIONAL_SOURCED_PHYSICAL_APPLICATION_RULE_OPEN", "wrong gap status")
    require(gap["remaining_physical_application_rule"]["not_proved_now"] is True, "application rule overclaimed")
    require(gap["if_supplied_then"]["physical_PhiFinC1_applies_Q_residual"] is True, "sufficiency drift")
    require(STATUS in note and NEXT in note and "no longer to invent a functional" in note, "note missing essentials")
    print("AUDIT_PASS: C1 defect functional source imported; physical PhiFinC1 application remains open")


if __name__ == "__main__":
    main()
