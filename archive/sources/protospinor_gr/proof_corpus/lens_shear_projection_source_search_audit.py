from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "lens_shear_projection_source_search_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "LENS_SHEAR_PROJECTION_SOURCE_SEARCH_BLOCKED_DIRECT_SELECTION_MISSING",
        "unexpected status",
    )
    summary = cert["evidence_summary"]
    require(summary["indirect_lens_transport_sources"], "expected indirect lens transport evidence")
    require(summary["tt_sector_sources"], "expected TT sector evidence")
    tests = cert["promotion_tests"]
    require(tests["formal_candidate_passes_rank_test"] is True, "formal candidate should still pass")
    require(tests["source_selection_closed"] is False, "source selection should remain open")
    require(
        tests["relative_plus_cross_normalization_selected"] is False,
        "relative normalization should remain open",
    )
    require(cert["blocked_claim"]["blocked"] is True, "blocked claim should be blocked")
    require(cert["candidate_retained"]["retain_formal_candidate"] is True, "candidate should be retained")
    require(cert["guardrails"]["claims_selected_P_GR"] is False, "must not claim selected P_GR")
    require(cert["guardrails"]["claims_selected_GR_Hessian"] is False, "must not claim selected Hessian")

    print("AUDIT_PASS: lens shear projection source search blocks promotion and retains candidate")


if __name__ == "__main__":
    main()

