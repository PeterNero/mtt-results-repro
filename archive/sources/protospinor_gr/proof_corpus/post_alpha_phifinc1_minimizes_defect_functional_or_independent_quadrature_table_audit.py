from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "post_alpha_phifinc1_minimizes_defect_functional_or_independent_quadrature_table_certificate.json"
)
STATUS = "POST_ALPHA_PHIFINC1_MINIMIZES_DEFECT_FUNCTIONAL_OR_INDEPENDENT_QUADRATURE_TABLE_IMPORTED_BINDING_REDUCTION_OPEN"
NEXT = "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1"


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
    require(cert["theorem"]["proved"] is True, "binding bridge theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    frontier = cert["frontier_decision"]
    require(frontier["I10_binding_theorem_slot_created"] is True, "I10 slot missing")
    require(frontier["I1_minimizer_trace_open"] is True, "I1 should remain open")
    require(frontier["I5_dotD_C1_response_open"] is True, "I5 should remain open")
    require(frontier["independent_quadrature_table_values_open"] is True, "quadrature values should remain open")
    require(frontier["frontier_is_minimizer_trace_C1_payload_theorem_or_quadrature_values"] is True, "wrong frontier")
    require(frontier["next_required_artifact"] == NEXT, "wrong next artifact")

    binding = packet["phifinc1_minimizer_binding_reduction"]
    require(binding["status"] == "REDUCED_TO_MINIMIZER_TRACE_AND_C1_RESPONSE_THEOREM_SLOTS", "wrong binding status")
    require(binding["proved_now"] is False, "I10 overclaimed")
    require(binding["new_binding_theorem_slot"]["id"] == "I10_phifinc1_minimizes_c1_defect_functional", "I10 id drift")
    require(len(binding["new_binding_theorem_slot"]["dependencies"]) == 3, "dependency count drift")

    quadrature = packet["independent_quadrature_table_template"]
    require(quadrature["status"] == "TEMPLATE_READY_VALUES_EMPTY", "wrong quadrature status")
    require(quadrature["values_filled_now"] is False, "quadrature values overfilled")
    require(quadrature["acceptance_tests"]["A_shape"] == [72, 2], "A shape drift")
    require(quadrature["acceptance_tests"]["b_shape"] == [72], "b shape drift")
    require(len(quadrature["required_values"]) == 6, "required values drift")

    require(NEXT in note and "I10" in note and "Phi_fin" in note, "note missing essentials")
    print("AUDIT_PASS: PhiFinC1 minimization/quadrature-table bridge imported; I10 and table values remain open")


if __name__ == "__main__":
    main()
