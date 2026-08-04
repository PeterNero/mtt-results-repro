from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_normalized_ext_local_form_table_certificate.json"
STATUS = "SELECTED_NORMALIZED_EXT_LOCAL_FORM_TABLE_BUILT_HYM_HODGE_QUADRATURE_OPEN"
NEXT = "MTT_Selected_End0_HYM_Hodge_Quadrature_Projector_Table_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim full closure")
    require(all(cert["checks"].values()), "all checks should pass")
    require(all(cert["what_closes_now"].values()), "all closure flags should be true")
    require(all(cert["what_remains_open"].values()), "all blockers should remain open")
    require(cert["next_required_artifact"] == NEXT, "wrong next artifact")

    table = packet["normalized_ext_local_form_table"]
    require(table["selected_basis_slot"] == "theta_plus_0_tensor_eta_minus_0", "wrong selected slot")
    require(table["selected_normalized_coordinate_vector"] == [1, 0, 0, 0, 0, 0, 0, 0], "wrong unit vector")
    require(table["normalization_convention"]["unit_norm_in_selected_Cech_basis"] is True, "unit convention missing")
    require(
        table["local_form_representative"]["symbolic"]
        == "eta = theta_plus_0(z1) tensor eta_minus_0(z2) dbar_z2",
        "wrong local form",
    )
    require(table["transition_weights"]["pairings"]["E(g5,g6)"] == 0, "shared circle must be degree zero")
    require(packet["End0_insertion"]["safe_for_newton"] is False, "must not be Newton safe")
    require(packet["guardrails"]["does_not_use_old_unselected_fixture"] is True, "fixture guardrail missing")
    require(STATUS in note and NEXT in note and "theta_plus_0_tensor_eta_minus_0 -> 1" in note, "note missing essentials")

    print("AUDIT_PASS: selected normalized Ext local-form table built; HYM/Hodge/quadrature remain open")


if __name__ == "__main__":
    main()
