from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_selected_correction_source_reduction_certificate.json"
STATUS = "POST_ALPHA_SELECTED_CORRECTION_SOURCE_REDUCED_NONIDENTITY_RHOE_BN_OPEN"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["diagnostic_splitter_exists"] is True, "diagnostic splitter should exist")
    require(cert["diagnostic_splitter_promoted"] is False, "diagnostic splitter must not promote")
    require(cert["selected_correction_matrix_source_closed"] is False, "selected correction source should remain open")
    require(all(cert["checks"].values()), "all checks should pass")
    require(packet["theorem"]["proved"] is True, "theorem should be proved")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    diagnostic = packet["diagnostic_representative_support_only"]
    require(diagnostic["candidate_count"] == 1170, "diagnostic search count mismatch")
    require(diagnostic["ckm_commutator_norm_sq"] > 0, "CKM diagnostic should be nonzero")
    require(diagnostic["pmns_commutator_norm_sq"] > 0, "PMNS diagnostic should be nonzero")
    require(diagnostic["cp_odd_trace_commutator_cubed_imag"] > 0, "CP diagnostic should be nonzero")
    require(all(item["current_status"] == "open" for item in packet["required_payload"].values()), "payload should remain open")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "diagnostic splitter selected = false" in note, "note missing essentials")
    print("AUDIT_PASS: selected correction gate reduced to nonidentity rhoE/quotient-valid BN")


if __name__ == "__main__":
    main()
