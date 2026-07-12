from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_end0_hym_hodge_quadrature_projector_table_certificate.json"
STATUS = "SELECTED_END0_HODGE_QUADRATURE_TABLE_BUILT_HYM_PROJECTOR_VALUES_OPEN"
NEXT = "MTT_Selected_HYM_Correction_and_Gauge_Projector_Value_Table_v1"


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

    hodge = packet["Hodge_Lambda_table"]
    require(hodge["Lambda_i_ea_ebar_b"]["i*e1_wedge_ebar1"] == 1, "Lambda diagonal wrong")
    require(hodge["Lambda_i_ea_ebar_b"]["i*e1_wedge_ebar2"] == 0, "Lambda off-diagonal wrong")
    require(hodge["primitive_diagonal_basis"]["Lambda(P12)"] == 0, "primitive P12 wrong")
    quad = packet["quadrature_table"]
    require(quad["eta_00_unrescaled_norm_square_exact_expression"] == "1/sqrt(32)", "wrong eta norm")
    require(quad["eta_00_unit_L2_rescale_factor_exact_expression"] == "32^(1/4)", "wrong eta rescale")
    require(packet["HYM_correction_table"]["selected_connection_coefficients_emitted"] is False, "HYM values must be open")
    require(packet["gauge_projector_table"]["projector_values_emitted"] is False, "projector values must be open")
    require(packet["End0_operator_table"]["newton_ready"] is False, "Newton must remain blocked")
    require(STATUS in note and NEXT in note and "eta_00^unit" in note, "note missing essentials")

    print("AUDIT_PASS: End0 Hodge/Lambda and quadrature table built; HYM/projector values remain open")


if __name__ == "__main__":
    main()
