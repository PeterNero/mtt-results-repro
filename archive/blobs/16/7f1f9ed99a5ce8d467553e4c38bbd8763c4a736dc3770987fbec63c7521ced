from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_end0_basis_table_or_bn_identification_import_certificate.json"
STATUS = "SELECTED_END0_BN_IDENTIFICATION_REJECTED_DIRECT_TABLE_REDUCED_TO_AH_EXT_LOCAL_FORMS"
NEXT = "MTT_Selected_End0_Direct_Differential_Table_From_AH_Ext_Forms_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["name"] == "SelectedEnd0BasisTableOrBNIdentificationImportNoGo", "wrong theorem")
    require(cert["theorem"]["proved"] is True, "theorem should be proved")
    require(cert["theorem"]["closure_claimed"] is False, "must not claim closure")
    require(all(cert["checks"].values()), "all checks should pass")
    require(all(cert["what_closes_now"].values()), "all closure flags should be true")
    require(all(cert["what_remains_open"].values()), "all blockers should remain open")
    require(cert["next_required_artifact"] == NEXT, "wrong next artifact")

    path_a = packet["path_A_BN"]
    require(path_a["result"] == "REJECTED_AS_SELECTED_END0_TABLE", "B_N should be rejected as selected End0")
    require(path_a["blocking_evidence"]["ordinary_bundle_equivariance"] is False, "ordinary equivariance blocker missing")
    require(path_a["support_retained"]["dimension_match_27"] is True, "B_N support should be retained")
    attempt = packet["direct_table_attempt"]
    require(attempt["closed"] is False, "direct table must remain open")
    require(all(attempt["closed_inputs"].values()), "closed direct-table inputs should all be true")
    require(all(attempt["open_inputs"].values()), "open direct-table inputs should all be true")
    require(packet["guardrails"]["does_not_identify_projective_BN_with_ordinary_End0"] is True, "B_N guardrail missing")
    require(packet["guardrails"]["does_not_use_unselected_cech_fixture_as_selected_ext_forms"] is True, "Cech guardrail missing")
    require("Path A is rejected" in note and "Path B is the rigorous route" in note, "note must state path verdict")
    require(STATUS in note and NEXT in note, "note must record status and next")

    print("AUDIT_PASS: End0/B_N gate imported; direct table reduced to selected AH/Ext local-form data")


if __name__ == "__main__":
    main()
