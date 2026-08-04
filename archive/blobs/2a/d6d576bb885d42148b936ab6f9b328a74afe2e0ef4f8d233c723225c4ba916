from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_enriched_weylpair_static_provenance_certificate.json"
STATUS = "POST_ALPHA_ENRICHED_WEYLPAIR_STATIC_PROVENANCE_CLOSED_DYNAMIC_C1_VALUES_OPEN"
NEXT = "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim dynamic closure")
    require(cert["theorem"]["proved"] is True, "static provenance theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    decision = cert["frontier_decision"]
    require(decision["static_enriched_weylpair_provenance_closed"] is True, "static provenance not closed")
    require(decision["dynamic_C1_values_promoted"] is False, "dynamic values promoted")
    require(decision["frontier_is_dynamic_C1_transfer_tensor_or_galerkin_values"] is True, "wrong frontier")
    require(decision["next_required_artifact"] == NEXT, "wrong next artifact")

    static = packet["static_source_provenance"]
    require(static["phase_Z_to"] == ["u", "e"], "Z route drift")
    require(static["shift_X_to"] == ["d", "nuD"], "X route drift")
    require(static["active_shift_1_1_proved"] is True, "active shift support lost")
    require(static["normalization"]["selected_overlap_transfer_normalization"] is True, "normalization lost")

    boundary = packet["dynamic_boundary"]
    require(boundary["conditional_value_run_ready"] is True, "conditional run readiness lost")
    require(boundary["conditional_rank"] == 2, "rank drift")
    require(boundary["A_transpose_A_if_promoted"] == [[12.0, 0.0], [0.0, 12.0]], "wrong A^T A")
    require(boundary["A_transpose_b_if_promoted"] == [12.0, 12.0], "wrong A^T b")
    require("dynamic source-to-C1 overlap tensor or transfer functor" in boundary["open_dynamic_requirements"], "dynamic transfer gate lost")
    require("b_selected and Hessian/kernel normalization for A_selected" in boundary["open_dynamic_requirements"], "b/A normalization gate lost")
    require("linear_response_matrices" in packet["honest_galerkin_required_outputs"], "Galerkin output gate lost")
    require(STATUS in note and NEXT in note and "Static enriched Weyl-pair provenance is now closed" in note, "note missing essentials")
    print("AUDIT_PASS: enriched Weyl-pair static provenance closed; dynamic C1 values remain open")


if __name__ == "__main__":
    main()
