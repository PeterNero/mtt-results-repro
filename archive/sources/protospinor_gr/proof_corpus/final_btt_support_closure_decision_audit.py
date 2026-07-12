from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "final_btt_support_closure_decision_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    template = json.loads(Path(cert["required_theorem_template_written"]).read_text(encoding="utf-8"))

    require(
        cert["status"] == "FINAL_BTT_SUPPORT_GATE_CLOSED_AS_SOURCE_OPEN_NOT_DERIVABLE",
        "unexpected status",
    )
    source = cert["source_tests"]
    decision = cert["decision"]
    guards = cert["guardrails"]

    require(source["central_paper_labels_core_claim_as_interpretive_synthesis"] is True, "interpretive label missing")
    require(source["central_paper_says_we_show_means_synthesize"] is True, "synthesis guardrail missing")
    require(source["central_unique_shared_channel_claim_present"] is True, "central channel claim missing")
    require(source["central_gravity_shared_circle_claim_present"] is True, "gravity shared circle claim missing")
    require(source["central_gravity_strain_claim_present"] is True, "gravity strain claim missing")
    require(source["independence_no_go_closed"] is True, "independence no-go missing")
    require(source["adjoint_nonzero_closed"] is True, "adjoint nonzero missing")
    require(source["uniqueness_ready"] is True, "uniqueness not ready")

    require(decision["can_close_unconditionally_from_current_corpus"] is False, "must not close unconditionally")
    require(decision["can_close_conditionally_with_template_theorem"] is True, "conditional theorem should close")
    require("not a standalone theorem" in decision["why_not_unconditional"], "decision should explain source gap")
    require(template["schema"] == "CentralCircleTTAdjointSupportTheorem.v1", "wrong template")
    require(template["then_existing_results_imply"]["lambda_GR_TT_internal_normalized"] == 15.0, "lambda consequence mismatch")
    require("Unique Missing Theorem" in note, "note should identify missing theorem")

    require(guards["claims_unconditional_lambda_GR_TT_15"] is False, "must not overclaim lambda")
    require(guards["uses_interpretive_synthesis_as_proof"] is False, "must not use synthesis as proof")
    require(guards["claims_exact_support_sourced"] is False, "must not claim support sourced")
    require(guards["uses_observed_GR_data"] is False, "must not use observed data")

    print("AUDIT_PASS: final BTT support gate closed as source-open and not derivable from current corpus")


if __name__ == "__main__":
    main()
