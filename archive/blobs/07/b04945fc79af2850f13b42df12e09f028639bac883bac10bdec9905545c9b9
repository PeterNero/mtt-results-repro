from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_sourcevalue_lambda_frontier_certificate.json"
STATUS = "POST_ALPHA_SOURCEVALUE_AND_LAMBDA_FRONTIER_REDUCED_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_CanonicalZeroSelection_or_NonInvariantC1Tensor_Fill_and_U1HyperchargeSpectrum_v1"


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
    require(packet["theorem"]["proved"] is True, "theorem should be proved as a reduction")
    counts = packet["primitive_c1_frontier"]["missing_leaf_counts"]
    require(counts["primitive_c1_atom_matrix"] == 24, "expected 24 atom matrices")
    require(counts["selected_basis"] == 12, "expected 12 selected basis leaves")
    require(counts["b_selected_source"] == 4, "expected four b rows/zero theorems")
    require(packet["primitive_c1_frontier"]["route_ranking"][0]["route"] == "selected_noninvariant_tensor", "wrong primary C1 route")
    require(packet["lambda12_frontier"]["primary_route"] == "heterotic_or_section_ring_u1_hypercharge_spectrum", "wrong lambda12 primary route")
    require(packet["lambda12_frontier"]["rejected_routes"]["quotient_identity"]["status"].startswith("REJECTED"), "projector shortcut not rejected")
    require(packet["lambda12_frontier"]["rejected_routes"]["central_circle_reuse"]["status"].startswith("REJECTED"), "central-circle shortcut not rejected")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "24 atom matrices" in note, "note missing essentials")
    print("AUDIT_PASS: post-alpha source-value and lambda12 frontier reduced")


if __name__ == "__main__":
    main()
