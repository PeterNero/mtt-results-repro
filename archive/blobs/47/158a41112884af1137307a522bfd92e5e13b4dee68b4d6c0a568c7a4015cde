from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_weylpair_transfer_reduction_certificate.json"
STATUS = "POST_ALPHA_WEYLPAIR_TRANSFER_REDUCED_SECTOR_ROUTING_NORMALIZATION_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(all(cert["checks"].values()), "all certificate checks should pass")
    require(packet["primitive_only_counterexample"]["target_in_primitive_span"] is False, "primitive-only span must fail")
    require(packet["weylpair_algebra"]["target_in_weylpair_span"] is True, "Weyl pair should span target conditionally")
    require(packet["weylpair_algebra"]["rank"] == 2, "Weyl pair rank should be two")
    require(packet["source_provenance"]["source_level_weyl_carrier"]["proved"] is True, "source-level Weyl carrier should be proved")
    require(packet["conditional_transfer"]["phase_residual"] == 0.0, "phase transfer should be exact")
    require(packet["conditional_transfer"]["shift_residual"] == 0.0, "shift transfer should be exact")
    require(packet["conditional_transfer"]["selected_status"]["promote_to_A_selected_allowed"] is False, "must not promote A")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "Primitive-only C1 is now retired" in note, "note missing essentials")
    print("AUDIT_PASS: post-alpha Weyl-pair transfer reduced without selected promotion")


if __name__ == "__main__":
    main()
