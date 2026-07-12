from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_primitive_c1_atom_nogo_frontier_certificate.json"
STATUS = "POST_ALPHA_PRIMITIVE_C1_ATOM_NOGO_FRONTIER_BUILT_VALUES_OPEN"
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
    require(cert["primitive_C1_atoms_emitted"] is False, "atoms should remain open")
    require(cert["missing_leaf_count"] == 40, "wrong missing leaf count")
    require(cert["canonical_zero_selected"] is False, "canonical zero should not be selected")
    require(all(cert["checks"].values()), "all checks should pass")
    require(packet["theorem"]["proved"] is True, "theorem should be proved")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(packet["fill_attempt"]["filled_atom_matrices"] == 0, "should fill zero atoms")
    require(packet["fill_attempt"]["open_atom_matrices"] == 24, "should keep 24 atoms open")
    require(packet["canonical_zero_branch"]["accepted_as_selected_atom_payload"] is False, "zero branch overpromoted")
    require(packet["missing_leaf_counts"] == {"selected_basis": 12, "primitive_c1_atom_matrix": 24, "b_selected_source": 4}, "wrong leaf counts")
    require([route["route"] for route in packet["route_ranking"]] == ["selected_noninvariant_tensor", "canonical_zero_selection", "typed_connection_derivation"], "wrong route ranking")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "Legal closing routes" in note, "note missing essentials")
    print("AUDIT_PASS: primitive C1 atom no-go/frontier imported; three legal routes remain")


if __name__ == "__main__":
    main()
