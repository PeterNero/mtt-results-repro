from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "btt_adjoint_shape_map_typing_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["replacement_packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "BTT_IMAGE_GATE_CORRECTED_TO_ADJOINT_SUPPORT_NONZERO_CLOSED_SUPPORT_OPEN",
        "unexpected status",
    )
    source = cert["source_tests"]
    closed = cert["closed_now"]
    conclusion = cert["conclusion"]
    guards = cert["guardrails"]

    require(source["shape_map_B_is_DG_Pi_coh"] is True, "B shape map not sourced")
    require(source["propagator_is_B_Ainv_Bstar"] is True, "BA^-1B* source missing")
    require(source["kernel_inverse_on_TT"] is True, "TT inverse kernel source missing")
    require(source["physical_TT_two_point_function"] is True, "physical TT source missing")
    require(source["exact_z64_branch_retained_by_Pi_coh"] is True, "exact Z64 coherent retention missing")
    require(source["exact_z64_branch_selected_tower"] is True, "exact Z64 dstar source missing")

    require(closed["B_TT_weight2"] is True, "weight should remain closed")
    require(closed["B_TT_BRST_compatible"] is True, "BRST should remain closed")
    require(closed["TT_coupling_nonzero_for_adjoint_support"] is True, "TT adjoint nonzero should close")
    require(closed["exact_Z64_branch_available_and_coherent"] is True, "Z64 branch should be available")

    require(packet["schema"] == "SelectedTTAdjointShapeSupport.v1", "wrong packet schema")
    require(packet["operator"] == "J_TT := Pi_exact64 B^* P_TT", "wrong corrected operator")
    require(packet["required_to_close_lambda_GR_TT_15"]["Pi_exact64_Bstar_PTT_equals_Bstar_PTT"] is None, "support must remain open")

    require(conclusion["old_BTT_image_gate_valid_as_written"] is False, "old gate must be rejected")
    require(conclusion["correct_gate_is_adjoint_support"] is True, "adjoint gate must replace image gate")
    require(conclusion["TT_adjoint_coupling_nonzero"] is True, "nonzero adjoint coupling should close")
    require(conclusion["unconditional_lambda_GR_TT_15"] is False, "must not overclose lambda")
    require("not the correctly typed object" in note, "note should flag typing correction")

    require(guards["claims_B_maps_TT_to_internal_branch"] is False, "must not claim wrong direction")
    require(guards["claims_adjoint_support_exactly_dstar_k2"] is False, "must not claim exact support")
    require(guards["claims_unconditional_lambda_GR_TT_15"] is False, "must not claim final lambda")
    require(guards["uses_observed_GR_data"] is False, "must not use observed data")

    print("AUDIT_PASS: BTT image gate corrected to adjoint support; nonzero closed, exact support open")


if __name__ == "__main__":
    main()
