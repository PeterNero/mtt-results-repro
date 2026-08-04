from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "phifin_operator_payload_scaffold_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    insertion = Path(cert["paper_insertion_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "PHIFIN_OPERATOR_PAYLOAD_SCAFFOLD_IMPORTED_SOURCE_PROMOTION_AND_C1_OPEN",
        "unexpected Phi_fin operator scaffold status",
    )
    require(cert["theorem"]["proved"] is True, "operator scaffold theorem should be proved")
    require(cert["verdict"]["phi_fin_finite_operator_scaffold_imported"] is True, "scaffold should import")
    require(cert["verdict"]["phi_fin_full_selected_payload_emitted"] is False, "full Phi_fin must remain open")
    require(cert["verdict"]["selected_source_flags_may_be_set_true"] is False, "source flags must remain false")
    require(cert["verdict"]["nonzero_C1_payload_closed"] is False, "nonzero C1 must remain open")
    require(all(cert["closed_now"].values()), "all closed-now claims should pass")
    require(all(cert["still_open"].values()), "all still-open gates should remain true")
    require(all(value is False for value in cert["source_flags"].values()), "source flags must be false")
    require(len(set(cert["basis_ids"].values())) == 1, "operator layers must share a basis")

    for name, item in cert["D_E_summary"].items():
        require(item["domain_dimension"] == 27, f"{name} D_E domain dimension changed")
        require(item["matrix_shape_matches_complement_to_domain"], f"{name} D_E matrix shape invalid")
        require(item["zero_mode_count_matches_expected_kernel"], f"{name} zero mode count mismatch")
    for name, item in cert["dotD_projector_summary"].items():
        require(item["dotD_alpha1_matrix_shape"] == [27, 27], f"{name} dotD shape invalid")
        require(item["sector_projector_shape"] == [27, 27], f"{name} projector shape invalid")
        require(item["horizontal_gauge_verified"] is True, f"{name} horizontal gauge not verified")
        require(item["green_operator_verified"] is True, f"{name} green operator not verified")
        require(item["selected_dotD_source_verified"] is False, f"{name} dotD selected flag must be false")
        require(item["alpha1_driver_verified"] is False, f"{name} alpha1 flag must be false")

    require(packet["C1_summary"]["theorem"]["proved"] is True, "C1 no-go theorem should be proved")
    require(packet["C1_summary"]["what_closes_now"]["canonical_tensor_zero_response_result_proved_finitely"] is True, "C1 zero-response no-go missing")
    require("honest unpromoted model-active payloads" in note, "note must preserve unpromoted boundary")
    require("canonical translation-invariant primitive" in insertion, "insertion must state C1 boundary")
    require(all(cert["guardrails"].values()), "all guardrails must hold")

    print("AUDIT_PASS: Phi_fin operator scaffold imported; source promotion and nonzero C1 remain open")


if __name__ == "__main__":
    main()
