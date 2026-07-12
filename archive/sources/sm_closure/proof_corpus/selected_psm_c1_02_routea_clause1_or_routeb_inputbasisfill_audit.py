"""Audit PSM-C1-02 Route-A RA-1 or Route-B RB-1 input basis fill."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_psm_c1_02_routea_clause1_or_routeb_inputbasisfill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_ra1_physical_c1_variation_principle_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_rb1_zero_mode_basis_input_fill.packet.json"
RB1_INPUT = ROOT / "candidate_data" / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution" / "inputs" / "zero_mode_basis.packet.json"
DECISION = PACKET_DIR / "psm_c1_02_ra1_rb1_decision.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_RouteAClause1_PhysicalC1Variation_or_RouteBInputBasisFill_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_ROUTEA_RA1_OR_ROUTEB_RB1_BUILT_RB1_INPUT_FILLED_SELECTION_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    rb1 = load(RB1_INPUT)
    decision = load(DECISION)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "status mismatch")
    require(data["active_post_sm_parity_label"] == "PSM-C1-02", "active label mismatch")
    require(data["active_routes"] == ["ROUTE-A/RA-1", "ROUTE-B/RB-1"], "active routes mismatch")
    require(data["post_sm_parity_label_context"]["closed_boundary"] == "DONE-PARITY-00", "closed boundary missing")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["closure_claimed"] is False, "candidate overclaimed closure")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(route_a["active_label"] == "PSM-C1-02", "Route A active label mismatch")
    require(route_a["route_label"] == "ROUTE-A", "Route A label mismatch")
    require(route_a["clause_id"] == "RA-1", "Route A clause mismatch")
    require(route_a["closed_now"] is False, "RA-1 overclosed")
    require(route_a["free_axiom_patch_used"] is False, "RA-1 used patch")
    require(route_a["conditional_witness_value"] is True, "RA-1 conditional witness missing")

    require(route_b["active_label"] == "PSM-C1-02", "Route B active label mismatch")
    require(route_b["route_label"] == "ROUTE-B", "Route B label mismatch")
    require(route_b["input_id"] == "RB-1", "Route B input mismatch")
    require(route_b["input_file_exists_now"] is True and RB1_INPUT.exists(), "RB-1 input file missing")
    require(route_b["basis_dimension"] == 9, "RB-1 basis dimension mismatch")
    require(route_b["selected_emitted"] is False, "RB-1 overemitted")
    require(route_b["theorem_derived"] is False, "RB-1 overderived")
    require(route_b["source_owner_verified"] is False, "RB-1 source oververified")
    require(route_b["remaining_route_b_input_count_after_rb1"] == 3, "remaining Route B count mismatch")

    require(rb1["active_label"] == "PSM-C1-02", "RB-1 active label mismatch")
    require(rb1["route_label"] == "ROUTE-B", "RB-1 route label mismatch")
    require(rb1["input_id"] == "RB-1", "RB-1 input id mismatch")
    require(rb1["basis_dimension"] == 9 and len(rb1["basis"]) == 9, "RB-1 basis rows mismatch")
    require(rb1["selected_emitted"] is False, "RB-1 selected overemitted")
    require(rb1["support_selected_source_verified"] is False, "support basis oververified")
    require(rb1["hym_selected_values_emitted"] is False, "HYM values overemitted")
    require(rb1["hym_projector_values_open"] is True, "HYM projector values should be open")

    require(decision["active_label"] == "PSM-C1-02", "decision active label mismatch")
    require(decision["route_A"]["clause_id"] == "RA-1", "decision Route A clause mismatch")
    require(decision["route_A"]["closed_now"] is False, "decision RA-1 overclosed")
    require(decision["route_B"]["input_id"] == "RB-1", "decision Route B input mismatch")
    require(decision["route_B"]["input_filled_now"] is True, "decision RB-1 not filled")
    require(decision["route_B"]["selected_source_promoted_now"] is False, "decision RB-1 overpromoted")
    require(decision["route_B"]["remaining_input_count"] == 3, "decision remaining count mismatch")

    require(next_work["active_label"] == "PSM-C1-02", "next active label mismatch")
    require(next_work["primary"]["route_label"] == "ROUTE-A", "next primary route mismatch")
    require(next_work["primary"]["clause_id"] == "RA-1", "next primary clause mismatch")
    require(next_work["secondary"]["route_label"] == "ROUTE-B", "next secondary route mismatch")
    require(next_work["secondary"]["input_id"] == "RB-2", "next secondary input mismatch")

    require(cert["active_label"] == "PSM-C1-02", "cert active label mismatch")
    require(cert["closure_claimed"] is False, "cert overclaimed closure")
    require(cert["route_A_RA1_closed"] is False, "cert RA-1 overclosed")
    require(cert["route_B_RB1_input_filled"] is True, "cert RB-1 not filled")
    require(cert["route_B_RB1_selected_promoted"] is False, "cert RB-1 overpromoted")
    require("Status label: `PSM-C1-02 / ROUTE-A / RA-1`" in note, "note missing labels")
    require("Closed boundary label: `DONE-PARITY-00`" in note, "note missing closed boundary")

    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
