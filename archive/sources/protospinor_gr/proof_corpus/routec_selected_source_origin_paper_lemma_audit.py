from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_selected_source_origin_paper_lemma_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    insertion = Path(cert["paper_insertion_written"]).read_text(encoding="utf-8")
    theorem = cert["theorem"]
    verdict = cert["verdict"]
    boundary = cert["proof_boundary"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "ROUTEC_SOURCE_ORIGIN_CONDITIONAL_LEMMA_PROVED_PAPER_INSERTION_BUILT_PHI_FIN_OPEN",
        "unexpected Route-C source-origin paper lemma status",
    )
    require(verdict["support_part_proved"] is True, "support part should be proved")
    require(verdict["conditional_routec_source_origin_lemma_proved"] is True, "conditional lemma should be proved")
    require(verdict["unconditional_routec_source_origin_lemma_proved"] is False, "unconditional lemma must remain open")
    require(verdict["selected_matter_stress_coefficients_closed"] is False, "stress coefficients must remain open")
    require(verdict["paper_ready_insertion_written"] is True, "paper insertion must be written")
    require(theorem["conditional_status"] == "PROVED_FROM_PHI_FIN_EMISSION_PREMISE", "conditional theorem status changed")
    require(theorem["unconditional_status"] == "NOT_PROVED_WITH_CURRENT_CERTIFICATES", "unconditional status changed")
    require(boundary["as_conditional_lemma_and_proof_slot"] is True, "must be a conditional paper slot")
    require(boundary["as_full_unconditional_theorem"] is False, "must not be full theorem")
    require(all(cert["closed_support_premises"].values()), "all support premises should be closed")
    require(all(cert["open_payload_premises"].values()), "payload premises should remain open")
    require(packet["paper_draft_excerpt_status"] == "APPENDIX_DRAFT_PROOF_SLOT_OPEN", "sm-parity draft status changed")

    require("Conditional Route-C Source Origin" in insertion, "insertion must contain lemma heading")
    require("The support part of this lemma is proved" in insertion, "insertion must state support proof")
    require("unconditional theorem is not yet proved" in insertion, "insertion must preserve caveat")
    require("No observed masses" in insertion, "insertion must include no-target guardrail")
    require("conditional source-origin lemma" in note, "note must summarize conditional result")
    require(all(guards.values()), "all guardrails must hold")

    print("AUDIT_PASS: Route-C source-origin conditional lemma proved and paper insertion written; Phi_fin remains open")


if __name__ == "__main__":
    main()
