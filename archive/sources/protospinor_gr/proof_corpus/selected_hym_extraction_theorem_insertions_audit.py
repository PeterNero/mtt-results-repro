from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_hym_extraction_theorem_insertions_certificate.json"
STATUS = "SELECTED_HYM_EXTRACTION_THEOREM_INSERTIONS_BUILT_VALUE_SOLVE_OPEN"
NEXT = "MTT_Selected_HYM_SelectedConnection_or_RouteC_SelectedResidual_ValueSolve_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    strominger = Path(cert["paper_insertions_written"]["strominger"]).read_text(encoding="utf-8")
    theta = Path(cert["paper_insertions_written"]["theta"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected theorem insertion status")
    require(cert["theorem"]["proved"] is True, "extraction criterion theorem should be proved")
    require(cert["theorem"]["name"] == "SelectedHYMConnectionToFiniteOperatorExtractionCriterion", "wrong theorem")
    require(len(cert["theorem"]["required_fields"]) == 10, "criterion must preserve ten required fields")
    require(all(cert["checks"].values()), "all insertion checks should pass")
    require(all(cert["guardrails"].values()), "all guardrails must hold")

    boundary = cert["current_run_boundary"]
    require(boundary["selected_values_emitted"] is False, "current run must not emit selected values")
    require(boundary["can_emit_A_selected"] is False, "A_selected must remain blocked")
    require(boundary["can_emit_b_selected"] is False, "b_selected must remain blocked")
    require(boundary["next_required_artifact"] == NEXT, "next artifact changed")

    require("Theorem: Selected HYM Connection-to-Finite-Operator Extraction Criterion" in strominger, "missing Strominger theorem heading")
    require("if and only if" in strominger, "Strominger theorem must be biconditional")
    require("Abstract HYM existence alone does not prove the theorem" in strominger, "must block abstract HYM overclaim")
    require("Lifted selected flags" in strominger, "must block lifted selected flags")
    require("observed masses" in strominger, "must block observed masses")
    require("Current Honest Packet No-Go" in strominger, "must include current no-go corollary")
    require(NEXT in strominger, "Strominger insertion must preserve next gate")

    require("Theorem: Conditional A_selected Promotion Guardrail" in theta, "missing Theta guardrail theorem")
    require("conditional" in theta.lower(), "Theta insertion must mark conditional systems")
    require("A_selected" in theta and "b_selected" in theta, "Theta insertion must guard A_selected and b_selected")
    require("observed masses" in theta, "Theta insertion must block target data")
    require(NEXT in theta, "Theta insertion must preserve next gate")

    require(STATUS in note, "note must record status")
    require(NEXT in note, "note must record next artifact")
    require(packet["paper_insertions"]["strominger"] == cert["paper_insertions_written"]["strominger"], "packet/cert Strominger path mismatch")
    require(packet["paper_insertions"]["theta"] == cert["paper_insertions_written"]["theta"], "packet/cert Theta path mismatch")

    print("AUDIT_PASS: selected HYM extraction theorem insertions are rigorous and preserve value-solve boundary")


if __name__ == "__main__":
    main()
