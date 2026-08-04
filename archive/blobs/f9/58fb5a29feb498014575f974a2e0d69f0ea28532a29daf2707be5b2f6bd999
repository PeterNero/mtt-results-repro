"""Audit transport/alpha1 reconciliation and sector-charge source cutset."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_transportalpha1_reconciliation_or_sectorcharge_sourcecutset"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FRONTIER = PACKET_DIR / "reconciled_transport_alpha1_sector_frontier.packet.json"
CUTSET = PACKET_DIR / "sectorcharge_1m_or_transportclosed_replay_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TransportAlpha1_Reconciliation_or_SectorCharge_SourceCutset_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    frontier = load(FRONTIER)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_TRANSPORTALPHA1_RECONCILIATION_BUILT_SECTOR_SOURCE_CUTSET_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["SM_parity_closed"] is True, "SM parity should remain closed")
    require(data["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(data["no_knob_closed"] is False, "no-knob overclaimed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(frontier["transport_trace_closed_functionally"] is True, "transport trace not closed functionally")
    require(frontier["functional_rho_s_candidate_closed"] is True, "functional rho_s not closed")
    require(frontier["same_branch_alpha1_derivative_retired"] is True, "alpha1 derivative not retired")
    require(frontier["selected_dotD_source_verified_retired"] is True, "dotD source not retired")
    require(frontier["alpha1_driver_verified_retired"] is True, "alpha1 driver not retired")
    require(frontier["old_sectorcharge_alpha1_open_field_is_superseded"] is True, "old alpha1 field not superseded")

    still = frontier["still_open"]
    require(still["selected_zero_mode_bases_K_s"] is True, "zero-mode source overclosed")
    require(still["selected_rho_s_source_map"] is True, "rho_s source overclosed")
    require(still["selected_sector_charge_or_chirality_table"] is True, "sector charge overclosed")
    require(still["selected_1M_Dirac_neutrino_rule"] is True, "1M rule overclosed")
    require(still["transport_closed_finite_validator_replay"] is True, "finite replay overclosed")
    require(still["actual_QaSU3_operator_packet"] is True, "Qa/SU3 overclosed")

    require("route_A_sector_source_emission" in cutset["legal_next_routes"], "route A missing")
    require("route_B_transport_closed_validator_replay" in cutset["legal_next_routes"], "route B missing")
    require("alpha1 driver normalization" in cutset["retired_as_primary_blockers"], "alpha1 retirement missing")
    require(len(cutset["forbidden_shortcuts"]) == 4, "forbidden shortcuts changed")
    require(cutset["closure_claimed"] is False, "cutset closure overclaimed")

    require(cert["alpha1_retired_as_primary_blocker"] is True, "certificate missing alpha1 retirement")
    require(cert["sector_source_or_transport_closed_replay_open"] is True, "certificate missing open gate")
    require(data["next_required_artifact"] == "MTT_Selected_SectorCharge_1MDirac_SourceEmission_or_TransportClosedValidatorReplay_v1", "wrong next artifact")
    require("What remains is not another scalar normalization search." in note, "note missing scalar guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
