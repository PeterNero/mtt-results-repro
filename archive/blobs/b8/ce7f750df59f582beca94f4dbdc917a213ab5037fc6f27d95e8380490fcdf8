from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_tt_qsector_spectral_gap_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    require(
        cert["status"] == "TT_QSECTOR_GAP_REDUCED_TO_OPERATOR_SPECTRUM_NUMERIC_VALUE_OPEN",
        "unexpected status",
    )

    source = cert["source_tests"]
    closed = cert["closed_now"]
    candidates = cert["candidate_gap_classification"]
    remaining = cert["remaining_exact_gate"]
    guards = cert["guardrails"]

    require(source["qg_defines_E_external_TT"] is True, "QG should define E")
    require(source["qg_defines_Aint_internal_gap_block"] is True, "QG should define Aint")
    require(source["qg_defines_full_A_as_direct_sum"] is True, "QG should define A direct sum")
    require(source["qg_states_blocks_commute"] is True, "block commutation should be sourced")
    require(source["qg_states_TT_Q_gap_positive"] is True, "positive TT Q gap should be sourced")
    require(source["qg_computes_numeric_TT_gap"] is False, "numeric TT gap should remain open")
    require(source["z64_numeric_gap_sourced"] is True, "Z64 numeric gap should be sourced")
    require(all(closed.values()), "all closed_now fields should be true")
    require(candidates["closure_metric_1"]["selected_as_TT_Q_gap"] is False, "unit gap must not be selected")
    require(candidates["kappa_STF_rows"]["selected_as_TT_Q_gap"] is False, "kappa rows must not be selected")
    require(candidates["z64_15"]["selected_as_TT_Q_gap"] is False, "Z64 must not be selected")
    require(candidates["new_TT_value"]["allowed"] is True, "new TT value route should be allowed")
    require(remaining["name"] == "Selected_TT_QSector_Eigenpacket", "wrong remaining gate")
    require(packet["open_required_data"]["eigenvalue_computation_for_E_on_Q_TT"] is None, "packet must not fill eigenvalue")
    require(guards["claims_numeric_TT_gap"] is False, "must not claim numeric TT gap")
    require(guards["claims_gap_equals_z64_15"] is False, "must not claim Z64 gap")
    require(guards["claims_physical_modal_gap"] is False, "must not claim physical gap")

    print("AUDIT_PASS: TT Q-sector gap reduced to operator spectrum; numeric value remains open")


if __name__ == "__main__":
    main()
