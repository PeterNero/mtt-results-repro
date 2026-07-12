"""Audit common-circle sector-response execution / csk trace rows."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_commoncirclesectorresponseexecution_or_csktracerows"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
HCEN = DATA / SLUG / "source_level_common_circle_hcen_operator.packet.json"
TRACE_BASIS = DATA / SLUG / "sector_projector_and_family_dual_trace_basis.packet.json"
PHI_CONTRACT = DATA / SLUG / "phi_sector_n_source_value_contract.packet.json"
TRACE_ROWS = DATA / SLUG / "formal_csk_trace_rows_and_policy_replay_guard.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_csk_trace_execution.packet.json"
NOTE = CORPUS / "MTT_Selected_CommonCircleSectorResponseExecution_or_CSKTraceRows_v1.md"

STATUS = (
    "MTT_SELECTED_COMMONCIRCLESECTORRESPONSEEXECUTION_OR_CSKTRACEROWS_"
    "HCEN_AND_TRACE_ENGINE_CLOSED_PHI_VALUES_OPEN"
)
NEXT = "MTT_Selected_PhiSectorNSourceValues_or_NoKnobCSKRows_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    hcen = load(HCEN)
    trace_basis = load(TRACE_BASIS)
    phi_contract = load(PHI_CONTRACT)
    trace_rows = load(TRACE_ROWS)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "CommonCircleSectorResponseExecutionTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["strict_csk_source_theorem_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["H_cen_source_level_operator_emitted"] is True
    assert decision["sector_projectors_constructed"] is True
    assert decision["family_dual_trace_basis_closed"] is True
    assert decision["formal_csk_trace_rows_executed"] is True
    assert decision["formal_csk_trace_row_count"] == 9
    assert decision["Phi_sector_N_source_value_contract_closed"] is True
    assert decision["Phi_sector_N_numeric_values_emitted"] is False
    assert decision["accepted_strict_csk_source_row_count"] == 0
    assert decision["policy_replay_rows_accepted_as_source"] is False
    assert decision["strict_csk_source_theorem_closed"] is False
    assert decision["full_no_knob_closed"] is False
    assert decision["true_SM_equivalence_closed"] is False

    assert hcen["accepted_as_common_circle_source_level_operator"] is True
    assert hcen["accepted_as_csk_numeric_source"] is False
    assert hcen["H_cen"]["order"] == 3
    assert hcen["H_cen"]["unitary"] is True
    assert hcen["H_cen"]["source_level_emitted"] is True
    assert hcen["observed_data_used_as_selector"] is False
    assert hcen["target_fitting_used"] is False

    assert trace_basis["accepted_as_trace_engine"] is True
    assert trace_basis["vandermonde_dual_identity_residual"] < 1e-12
    assert trace_basis["sectors"] == ["u", "d", "e"]
    assert trace_basis["family_polynomial_basis"] == ["1", "F", "F^2"]

    assert phi_contract["contract_closed"] is True
    assert phi_contract["numeric_values_emitted"] is False
    assert phi_contract["accepted_source_value_count"] == 0
    assert len(phi_contract["rows"]) == 9
    assert all(row["source_value_emitted"] is False for row in phi_contract["rows"])
    assert "solving Phi_sector_N from policy c_{s,k} rows" in phi_contract["forbidden_value_sources"]

    assert trace_rows["formal_trace_rows_executed"] is True
    assert trace_rows["formal_trace_row_count"] == 9
    assert trace_rows["strict_source_value_row_count"] == 0
    assert trace_rows["policy_replay_rows_accepted_as_source"] is False
    assert len(trace_rows["rows"]) == 9
    assert all(row["formal_trace_executed"] is True for row in trace_rows["rows"])
    assert all(row["strict_source_value_emitted"] is False for row in trace_rows["rows"])
    assert all(row["accepted_as_no_knob_source_row"] is False for row in trace_rows["rows"])

    assert next_packet["next_required_artifact"] == NEXT
    assert "selected numeric Phi_sector_N values" in next_packet["still_open"]
    assert "policy replay values quarantined as comparison-only" in next_packet["closed_now"]

    assert cert["status"] == STATUS
    assert cert["H_cen_source_level_operator_emitted"] is True
    assert cert["sector_projectors_constructed"] is True
    assert cert["family_dual_trace_basis_closed"] is True
    assert cert["formal_csk_trace_rows_executed"] is True
    assert cert["formal_csk_trace_row_count"] == 9
    assert cert["Phi_sector_N_numeric_values_emitted"] is False
    assert cert["accepted_strict_csk_source_row_count"] == 0
    assert cert["next_required_artifact"] == NEXT
    assert cert["observed_data_used_as_selector"] is False
    assert cert["target_fitting_used"] is False

    assert "CommonCircleSectorResponseExecutionTheorem" in note
    assert "H_cen = diag(1, zeta_3, zeta_3^2)" in note
    assert NEXT in note
    print("common-circle sector-response execution / csk trace rows audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
