from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "sector_zeromode_end0_tensorproduct_construct_certificate.json"
STATUS = "SECTOR_ZEROMODE_END0_TENSORPRODUCT_CARRIER_CONSTRUCTED_SOURCE_ACTION_OPEN"
NEXT = "MTT_Selected_SectorZeroMode_SourcePayload_Search_or_Emission_Attempt_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(all(cert["checks"].values()), "all checks should pass")
    summary = packet["constructed_carrier_summary"]
    require(summary["total_dimension"] == 19, "wrong total dimension")
    require(summary["rank_match"]["matches_expected_sector_kernel_rank_sum"] is True, "rank mismatch")
    validation = packet["validation"]
    require(validation["all_lie_checks_pass"] is True, "lie checks failed")
    require(validation["all_projectors_idempotent"] is True, "projector idempotence failed")
    require(validation["all_projectors_commute_with_End0_action"] is True, "projectors must commute")
    require(validation["projectors_sum_to_identity"] is True, "projectors must sum to identity")
    require(validation["sector_T3_response_norms"]["H"]["zero_response"] is True, "H must be singlet")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "6*3 + 1 = 19" in note, "note missing essentials")
    print("AUDIT_PASS: End0 tensor-product sector carrier constructed; source action remains open")


if __name__ == "__main__":
    main()
