from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "post_alpha_minimizer_trace_c1_payload_theorem_or_quadrature_table_values_certificate.json"
)
STATUS = "POST_ALPHA_MINIMIZER_TRACE_C1_PAYLOAD_THEOREM_OR_QUADRATURE_TABLE_VALUES_IMPORTED_CONTRACT_OPEN"
NEXT = "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(cert["theorem"]["proved"] is True, "payload contract bridge should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    frontier = cert["frontier_decision"]
    require(frontier["route_A_payload_certificate_contract_built"] is True, "route A contract missing")
    require(frontier["route_B_quadrature_values_tables_staged"] is True, "route B tables missing")
    require(frontier["closure_acceptance_manifest_built"] is True, "manifest missing")
    require(frontier["frontier_is_I10_payload_certificate_or_independent_quadrature_values_fill"] is True, "wrong frontier")
    require(frontier["next_required_artifact"] == NEXT, "wrong next artifact")

    payload = packet["i10_minimizer_trace_c1_payload_contract"]
    require(payload["status"] == "PAYLOAD_CERTIFICATE_CONTRACT_BUILT_VALUES_OPEN", "wrong payload status")
    require(payload["promotion_rule"]["current_all_payload_certificates_verified"] is False, "payload overclaimed")
    require(len(payload["payload_certificate_required"]) == 3, "payload requirement count drift")

    quadrature = packet["quadrature_values_staging_tables"]
    require(quadrature["status"] == "TABLES_STAGED_VALUES_EMPTY", "wrong quadrature status")
    require(quadrature["values_filled_now"] is False, "quadrature overfilled")
    require(all(len(rows) == 0 for rows in quadrature["tables"].values()), "tables should be empty")
    require(quadrature["expected_minimum_counts"]["primitive_contraction_rows"] == 18, "primitive row count drift")

    manifest = packet["closure_acceptance_manifest"]
    require(manifest["status"] == "DUAL_ROUTE_ACCEPTANCE_MANIFEST_BUILT_OPEN", "wrong manifest status")
    require(manifest["closure_claimed_now"] is False, "manifest overclaimed")
    require(manifest["route_A_i10_payload_certificate"]["accepted_now"] is False, "route A overclaimed")
    require(manifest["route_B_independent_quadrature_values"]["accepted_now"] is False, "route B overclaimed")
    require(manifest["replay_target_if_accepted"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "Gram drift")
    require(manifest["replay_target_if_accepted"]["A_transpose_b"] == [12.0, 12.0], "ATb drift")
    require(manifest["replay_target_if_accepted"]["deltaTheta_C1"] == [1.0, 1.0], "DeltaTheta drift")

    require(NEXT in note and "Neither route is accepted yet" in note, "note missing essentials")
    print("AUDIT_PASS: minimizer trace C1 payload theorem/quadrature table values bridge imported; routes remain open")


if __name__ == "__main__":
    main()
