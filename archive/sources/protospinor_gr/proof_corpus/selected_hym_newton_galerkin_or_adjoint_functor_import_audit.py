from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_hym_newton_galerkin_or_adjoint_functor_import_certificate.json"
STATUS = "SELECTED_HYM_ADJOINT_TRANSFER_IMPORTED_FIRST_COEFFICIENT_SOLVE_TABLES_OPEN"
NEXT = "MTT_Selected_End0_Basis_Differential_Table_or_BN_Identification_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["name"] == "SelectedHYMAdjointTransferAndFirstCoefficientSolveImport", "wrong theorem")
    require(cert["theorem"]["proved"] is True, "theorem should be proved")
    require(cert["theorem"]["closure_claimed"] is False, "must not claim full closure")
    require(all(cert["checks"].values()), "all checks should pass")
    require(all(cert["what_closes_now"].values()), "all closure flags should be true")
    require(all(cert["what_remains_open"].values()), "all remaining blockers should remain open")
    require(cert["next_required_artifact"] == NEXT, "wrong next artifact")

    transfer = packet["adjoint_transfer"]
    require(transfer["source_rank"] == 2, "source rank should be 2")
    require(transfer["carrier_rank"] == 3, "adjoint carrier rank should be 3")
    require(transfer["continuous_parameters_added"] == 0, "transfer must add no knobs")
    require(transfer["finite_basis_identification_closed"] is False, "finite basis identification should remain open")

    manifest = packet["first_coefficient_solve"]["unknown_manifest"]
    require(manifest["Hermitian_metric_endomorphism_coefficients"] == 81, "wrong Hermitian unknown count")
    require(manifest["connection_one_form_coefficients"] == 486, "wrong connection unknown count")
    require(manifest["total_first_newton_unknown_slots_if_connection_form_used"] == 567, "wrong total unknown count")
    require(packet["promotion"]["may_promote_A_selected_or_b_selected"] is False, "must not promote A/b selected")
    require(packet["guardrails"]["no_cech_vector_as_connection_coefficients"] is True, "Ext/Cech guardrail missing")
    require("rank-3" in note and "End_0(V_alpha)" in note, "note must explain adjoint transfer")
    require("total connection-form solve slots" in note, "note must record unknown manifest")
    require(STATUS in note and NEXT in note, "note must record status and next")

    print("AUDIT_PASS: adjoint transfer imported; first coefficient solve remains blocked by finite differential tables")


if __name__ == "__main__":
    main()
