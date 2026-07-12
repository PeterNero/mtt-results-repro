from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_gr_tt_aint_interface_data_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    require(
        cert["status"] == "SELECTED_GR_TT_AINT_INTERFACE_PACKET_BUILT_OPERATOR_RELATION_OPEN",
        "unexpected status",
    )

    source = cert["source_tests"]
    closed = cert["closed_fields"]
    open_fields = cert["open_fields"]
    selected = cert["selected_data_status"]
    guards = cert["guardrails"]

    require(source["gr_source_defines_spectral_gap_lambda_star"] is True, "GR source should define lambda gap")
    require(source["gr_source_defines_observable_projection"] is True, "GR source should define projection")
    require(source["closure_source_defines_quadratic_cost_hessian"] is True, "closure source should define Hessian")
    require(source["source_derives_c_interface"] is False, "source must not already derive c_interface")
    require(source["source_derives_A_GR_TT_equals_H_TT"] is False, "source must not already derive A=H")
    require(source["source_selects_GR_internal_N_row"] is False, "source must not already select GR N row")
    require(all(closed.values()), "all structural fields should be closed")
    require(open_fields["selected_N_or_internal_volume_row"] is True, "selected row should remain open")
    require(open_fields["operator_relation_A_GR_TT_to_H_TT"] is True, "operator relation should remain open")
    require(open_fields["derived_c_interface"] is True, "c_interface should remain open")
    require(selected["can_compute_GR_TT_modal_gap_now"] is False, "modal gap should remain open")
    require(packet["open_selection_fields"]["derived_c_interface"] is None, "packet must not fill c_interface")
    require(guards["claims_A_GR_TT_equals_H_TT"] is False, "must not claim A=H")
    require(guards["claims_GR_TT_modal_gap_closed"] is False, "must not claim gap closure")
    require(guards["claims_Z64_is_GR_gap"] is False, "must not claim Z64 GR gap")

    print("AUDIT_PASS: selected GR TT/Aint interface packet built; operator relation remains open")


if __name__ == "__main__":
    main()
