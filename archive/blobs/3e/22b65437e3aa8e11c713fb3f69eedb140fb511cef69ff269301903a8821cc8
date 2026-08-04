"""Audit selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource.candidate.json"
CERT = ROOT / "certificates" / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource_certificate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
FORMAL = PACKET_DIR / "formal_110_row_replay_integrated.packet.json"
PROMOTION = PACKET_DIR / "physical_source_promotion_cutset.packet.json"
DECISION = PACKET_DIR / "all_rows_provenance_decision.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AllRowsProvenancePromotion_or_PhysicalPhiFinC1ActionSource_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    formal = load(FORMAL)
    promotion = load(PROMOTION)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_ALLROWSPROVENANCEPROMOTION_OR_PHYSICALPHIFINC1ACTIONSOURCE_BUILT_FORMAL_110_ROW_REPLAY_PHYSICAL_SOURCE_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(formal["row_counts"]["primitive_rows"] == 72, "primitive count mismatch")
    require(formal["row_counts"]["sector_matrix_rows"] == 36, "sector count mismatch")
    require(formal["row_counts"]["hessian_source_rows"] == 2, "hessian count mismatch")
    require(formal["row_counts"]["total_rows"] == 110, "total count mismatch")
    require(formal["all_72_primitive_rows_exact"] is True, "72 rows not exact")
    require(formal["formal_110_rows_executed"] is True, "formal rows not executed")
    require(formal["formal_110_matches_prior_replay"] is True, "formal replay mismatch")
    require(formal["hessian_source_rows"]["A_transpose_A"] == 12.0, "hessian norm mismatch")
    require(formal["hessian_source_rows"]["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(formal["hessian_source_rows"]["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta mismatch")
    require(formal["patched_parity_reference"]["patched_A_selected_emitted"] is True, "patched reference missing")
    require(formal["patched_parity_reference"]["unpatched_A_selected_emitted"] is False, "unpatched overclaimed")
    require(promotion["route_A_physical_action_source"]["closed"] is False, "route A overclosed")
    require(promotion["route_B_independent_provenance"]["closed"] is False, "route B overclosed")
    require(promotion["route_B_independent_provenance"]["all_72_primitive_values_exact"] is True, "route B values missing")
    require(decision["formal_110_row_replay_closed"] is True, "formal replay not closed")
    require(decision["formal_A_b_deltaTheta_replay_closed"] is True, "formal linear replay not closed")
    require(decision["A_selected_promoted_unpatched"] is False, "A selected overpromoted")
    require(decision["b_selected_promoted_unpatched"] is False, "b selected overpromoted")
    require(decision["physical_PhiFinC1_action_source_closed"] is False, "physical source overclosed")
    require(decision["provenance_independent_of_residual_projector_replay"] is False, "provenance overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "SM equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob overclaimed")
    require(cert["formal_110_row_replay_closed"] is True, "cert formal replay missing")
    require(cert["physical_PhiFinC1_action_source_closed"] is False, "cert physical overclosed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("total formal rows: 110" in note, "note missing total rows")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
