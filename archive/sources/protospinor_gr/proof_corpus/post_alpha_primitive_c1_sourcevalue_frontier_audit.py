from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_primitive_c1_sourcevalue_frontier_certificate.json"
STATUS = "POST_ALPHA_PRIMITIVE_C1_SOURCEVALUE_FRONTIER_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_CanonicalZeroSelection_or_NonInvariantC1Tensor_Fill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["missing_atom_count"] == 24, "wrong missing atom count")
    require(cert["missing_leaf_count"] == 40, "wrong missing leaf count")
    require(cert["reduced_to"] == NEXT, "wrong reduction target")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    require(packet["theorem"]["proved"] is True, "theorem should be proved")
    require(packet["post_alpha_prefix"]["alpha1_driver_verified"] is True, "alpha prefix should remain closed")
    require(packet["post_alpha_prefix"]["honest_dotD_validator_closed"] is True, "honest dotD prefix should remain closed")
    require(len(packet["atom_table"]) == 4, "four sectors should be present")
    require(all(not sector["all_terms_emitted"] for sector in packet["atom_table"].values()), "no sector should be filled")
    require(all(len(sector["missing_terms"]) == 6 for sector in packet["atom_table"].values()), "each sector should miss six terms")
    require(packet["canonical_zero_branch"]["canonical_tensor_zero_response_result_proved_finitely"] is True, "canonical zero test missing")
    require(packet["canonical_zero_branch"]["accepted_as_selected_atom_payload"] is False, "canonical zero must not be selected")
    require(packet["missing_leaf_counts"]["primitive_c1_atom_matrix"] == 24, "wrong primitive atom leaf count")
    require(packet["missing_leaf_counts"]["selected_basis"] == 12, "wrong basis leaf count")
    require(packet["missing_leaf_counts"]["b_selected_source"] == 4, "wrong b-source leaf count")
    require(packet["route_ranking"][0]["route"] == "selected_noninvariant_tensor", "primary route changed")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "filled atom matrices = 0" in note, "note missing essentials")

    print("AUDIT_PASS: primitive C1 source-value frontier imported; 24 atoms remain open")


if __name__ == "__main__":
    main()
