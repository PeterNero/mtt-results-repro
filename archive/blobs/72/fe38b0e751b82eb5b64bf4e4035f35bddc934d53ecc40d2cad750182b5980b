from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_routec_frontier_synchronization_certificate.json"
STATUS = "POST_ALPHA_ROUTEC_FRONTIER_SYNCHRONIZED_WEYLPAIR_PROVENANCE_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["theorem"]["proved"] is True, "synchronization theorem should be proved")
    require(cert["post_alpha_ready"] is True, "post-alpha gate should be ready")
    require(all(cert["routec_chain"].values()), "Route-C chain should pass")
    require(all(cert["still_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    frontier = cert["current_frontier"]
    require(frontier["not_linear_algebra"] is True, "frontier should move past linear algebra")
    require(frontier["not_raw_nonidentity_rhoE"] is True, "frontier should move past raw rhoE")
    require(frontier["not_raw_smooth_BN_scaffold"] is True, "frontier should move past raw BN scaffold")
    require(frontier["next_required_artifact"] == NEXT, "wrong next artifact")
    require("Weyl-pair source provenance" in frontier["blocker"], "wrong blocker")

    locked = packet["locked_solve"]
    require(locked["rank"] == 2, "conditional solve rank mismatch")
    require(locked["relative_residual"] < 1e-12, "conditional solve residual too large")
    require(packet["payload_reclassification"]["b_selected_or_homogeneous_zero_theorem"] == "b_selected still not emitted", "b_selected boundary lost")
    require(packet["guardrails"]["does_not_promote_conditional_A_to_A_selected"] is True, "A_selected guardrail lost")
    require(STATUS in note and NEXT in note and "No observed masses" in note, "note missing essentials")

    print("AUDIT_PASS: post-alpha frontier synchronized to Weyl-pair source provenance gate")


if __name__ == "__main__":
    main()
