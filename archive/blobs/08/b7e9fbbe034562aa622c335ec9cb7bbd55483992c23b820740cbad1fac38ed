from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_weylpair_frontier_reconciliation_certificate.json"
STATUS = "ROUTEC_WEYLPAIR_FRONTIER_RECONCILED_SOURCE_PROVENANCE_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "frontier reconciliation theorem should be proved")
    require(all(cert["chain_checks"].values()), "chain checks should pass")
    require(all(cert["counterexample_checks"].values()), "counterexample checks should pass")
    require(all(cert["weylpair_checks"].values()), "Weyl-pair checks should pass")
    require(all(cert["solve_checks"].values()), "solve checks should pass")
    require(all(cert["guardrails"].values()), "guardrails should pass")

    verdict = cert["verdict"]
    require(verdict["conditional_A_solve_closed"] is True, "conditional solve should be closed")
    require(verdict["algebraic_rank_obstruction_absent"] is True, "rank obstruction should be absent")
    require(verdict["selected_source_provenance_proved"] is False, "source provenance must remain open")
    require(verdict["A_selected_emitted"] is False, "A_selected must remain unpromoted")
    require(verdict["b_selected_emitted"] is False, "b_selected must remain open")
    require(verdict["honest_selected_deltaTheta_solve_run"] is False, "selected solve must remain open")
    require(verdict["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    require(packet["locked_solve"]["rank"] == 2, "conditional solve rank mismatch")
    require(packet["locked_solve"]["relative_residual"] < 1e-12, "conditional residual too large")
    require(
        "remaining blocker is no longer rank" in note
        and "No observed masses" in note
        and NEXT_ARTIFACT in note,
        "note must state frontier and guardrails",
    )

    print("AUDIT_PASS: Weyl-pair frontier reconciled; source provenance is the next gate")


if __name__ == "__main__":
    main()
