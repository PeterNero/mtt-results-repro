from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_minimizer_trace_c1_payload_or_quadrature_values_certificate.json"
STATUS = "POST_ALPHA_MINIMIZER_TRACE_C1_PAYLOAD_OR_QUADRATURE_VALUES_IMPORTED_CONTRACT_OPEN"
NEXT = "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(cert["theorem"]["proved"] is True, "payload contract theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    payload = packet["i10_minimizer_trace_c1_payload_contract"]
    require(payload["status"] == "PAYLOAD_CERTIFICATE_CONTRACT_BUILT_VALUES_OPEN", "wrong payload status")
    require(payload["promotion_rule"]["current_all_payload_certificates_verified"] is False, "payload certificate overclaimed")
    require(len(payload["payload_certificate_required"]) == 3, "payload requirement count drift")

    quadrature = packet["quadrature_values_staging_tables"]
    require(quadrature["status"] == "TABLES_STAGED_VALUES_EMPTY", "wrong quadrature status")
    require(quadrature["values_filled_now"] is False, "quadrature values overclaimed")
    require(all(len(rows) == 0 for rows in quadrature["tables"].values()), "quadrature tables should be empty")
    require(quadrature["expected_minimum_counts"]["primitive_contraction_rows"] == 18, "primitive count drift")

    manifest = packet["closure_acceptance_manifest"]
    require(manifest["status"] == "DUAL_ROUTE_ACCEPTANCE_MANIFEST_BUILT_OPEN", "wrong manifest status")
    require(manifest["closure_claimed_now"] is False, "manifest closure overclaimed")
    require(manifest["route_A_i10_payload_certificate"]["accepted_now"] is False, "route A overclaimed")
    require(manifest["route_B_independent_quadrature_values"]["accepted_now"] is False, "route B overclaimed")
    require(manifest["replay_target_if_accepted"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "wrong Gram")
    require(manifest["replay_target_if_accepted"]["A_transpose_b"] == [12.0, 12.0], "wrong ATb")
    require(manifest["replay_target_if_accepted"]["deltaTheta_C1"] == [1.0, 1.0], "wrong DeltaTheta")
    require(STATUS in note and NEXT in note and "Neither route is accepted yet" in note, "note missing essentials")
    print("AUDIT_PASS: minimizer trace C1 payload/quadrature value contract imported; both routes remain open")


if __name__ == "__main__":
    main()
