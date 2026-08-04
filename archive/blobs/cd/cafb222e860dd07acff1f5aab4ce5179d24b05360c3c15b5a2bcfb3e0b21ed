from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "lens_to_stf_source_identification_attempt_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "LENS_TO_STF_SOURCE_IDENTIFICATION_BLOCKED_GAUGE_FLAT_LENS_EVIDENCE",
        "unexpected status",
    )
    summary = cert["evidence_summary"]
    tests = cert["source_tests"]
    guardrails = cert["guardrails"]

    require(cert["input_certificate"]["stf_bridge_closed"] is True, "STF bridge should be closed")
    require(summary["lens_transport_sources"], "expected lens transport evidence")
    require(summary["bookkeeping_strain_curvature_sources"], "expected strain/curvature route evidence")
    require(summary["gauge_flat_lens_sources"], "expected gauge-flat lens evidence")
    require(tests["direct_lens_to_stf_metric_shear_found"] is False, "direct lens-to-STF source should be absent")
    require(tests["direct_lens_to_stf_closed"] is False, "lens-to-STF should remain open")
    require(
        tests["source_promotes_minimal_cln_candidate"] is False,
        "minimal CLN candidate must not be source-promoted",
    )
    require(
        tests["points_away_from_lens_tt_identification"] is True,
        "source evidence should point away from lens=TT identification",
    )
    require(guardrails["claims_lens_is_selected_TT_source"] is False, "must not claim lens selected TT source")
    require(guardrails["claims_full_GR_closed"] is False, "must not claim full GR closure")

    print("AUDIT_PASS: lens-to-STF source identification is blocked; closure-strain route is next")


if __name__ == "__main__":
    main()
