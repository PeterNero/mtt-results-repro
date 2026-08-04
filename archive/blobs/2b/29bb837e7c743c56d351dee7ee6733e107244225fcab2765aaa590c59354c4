from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_c1_primitive_response_on_smooth_bn_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == "ROUTEC_C1_PRIMITIVE_RESPONSE_ON_SMOOTH_BN_IMPORTED_SELECTED_PRIMITIVE_OPEN", "unexpected status")
    require(cert["theorem"]["proved"] is True, "C1 primitive import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["no_go_checks"].values()), "all no-go checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(packet["primitive_tensor"]["nonzero_tensor_slots"] == 729, "wrong tensor slot count")
    require(set(packet["matrix_norms"]) == {"u", "d", "e", "nuD"}, "wrong C1 sectors")
    require(all(value == 0.0 for value in packet["matrix_norms"].values()), "canonical C1 matrices should vanish")
    require(cert["verdict"]["canonical_translation_invariant_C1_response_nonzero"] is False, "canonical C1 must be zero")
    require(cert["verdict"]["nonzero_selected_C1_response_found"] is False, "nonzero selected C1 must not be found")
    require(cert["verdict"]["selected_noninvariant_primitive_required"] is True, "selected non-invariant primitive should be required")
    require(cert["verdict"]["yukawa_CKM_PMNS_claim_allowed"] is False, "flavor claim must not be allowed")
    require(
        cert["verdict"]["next_required_artifact"] == "MTT_Selected_RouteC_NonInvariant_C1_Primitive_or_BasisTransport_Search_v1",
        "wrong next artifact",
    )
    require("No Yukawa, CKM, PMNS" in note and "selection-rule theorem" in note, "note must state boundary")

    print("AUDIT_PASS: C1 primitive no-go imported; selected non-invariant primitive remains open")


if __name__ == "__main__":
    main()
