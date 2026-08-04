from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_end0_direct_ah_ext_form_table_import_certificate.json"
STATUS = "SELECTED_END0_DIRECT_AH_EXT_FORM_TABLE_IMPORTED_NORMALIZED_EXT_TABLE_OPEN"
NEXT = "MTT_Selected_Normalized_Ext_Local_Form_Table_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(all(cert["checks"].values()), "all checks should pass")
    require(all(cert["what_closes_now"].values()), "all closure flags should be true")
    require(all(cert["what_remains_open"].values()), "all blockers should remain open")
    require(cert["next_required_artifact"] == NEXT, "wrong next artifact")

    ext = packet["Ext_local_form_template"]
    require(ext["selected_basis_slot"] == "theta_plus_0_tensor_eta_minus_0", "wrong Ext slot")
    require(
        ext["symbolic_representative"] == "theta_plus_0(z1) tensor eta_minus_0(z2) dbar_z2",
        "wrong Ext symbolic form",
    )
    require(ext["not_yet_numeric_local_form"] is True, "symbolic form must not be numeric")
    require(packet["newton_readiness"]["ready"] is False, "Newton must remain blocked")
    require(
        packet["guardrails"]["symbolic_ext_form_not_used_as_numeric_table"] is True,
        "symbolic-form guardrail missing",
    )
    require("barpartial_End0" in note and STATUS in note and NEXT in note, "note missing essentials")

    print("AUDIT_PASS: direct End0 AH/Ext form table imported; normalized Ext table is next")


if __name__ == "__main__":
    main()
