"""Audit PSM-C1-02 RA-1 derivation attack or RB-2 primitive terms fill."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_psm_c1_02_ra1_derivationattack_or_rb2_primitivetermsfill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_ra1_derivation_attack_with_external_variational_support.packet.json"
ROUTE_B = PACKET_DIR / "route_b_rb2_primitive_contraction_terms_fill.packet.json"
RB2_INPUT = ROOT / "candidate_data" / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution" / "inputs" / "primitive_contraction_terms.packet.json"
SUPERSET = PACKET_DIR / "psm_c1_02_superset_strategy_external_alignment.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_RouteA_RA1_DerivationAttack_or_RouteB_RB2_PrimitiveTermsFill_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_RA1_DERIVATIONATTACK_OR_RB2_PRIMITIVETERMSFILL_BUILT_RB2_INPUT_FILLED_SELECTION_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    rb2 = load(RB2_INPUT)
    superset = load(SUPERSET)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "status mismatch")
    require(data["active_post_sm_parity_label"] == "PSM-C1-02", "active label mismatch")
    require(data["active_routes"] == ["ROUTE-A/RA-1", "ROUTE-B/RB-2"], "active routes mismatch")
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
    require(len(route_a["external_alignment"]) == 3, "external references missing")
    require(all(ref["used_as_source_proof"] is False for ref in route_a["external_alignment"]), "external source overused")
    require(set(route_a["refined_RA1_target"]) == {"RA1a", "RA1b", "RA1c", "RA1d"}, "RA-1 refined clauses mismatch")

    require(route_b["active_label"] == "PSM-C1-02", "Route B active label mismatch")
    require(route_b["route_label"] == "ROUTE-B", "Route B label mismatch")
    require(route_b["input_id"] == "RB-2", "Route B input mismatch")
    require(route_b["input_file_exists_now"] is True and RB2_INPUT.exists(), "RB-2 input file missing")
    require(route_b["primitive_row_count"] == 72, "Route B row count mismatch")
    require(route_b["selected_emitted"] is False, "Route B overemitted")
    require(route_b["theorem_derived"] is False, "Route B overderived")
    require(route_b["source_owner_verified"] is False, "Route B source oververified")
    require(route_b["remaining_route_b_input_count_after_rb2"] == 2, "Route B remaining count mismatch")

    require(rb2["active_label"] == "PSM-C1-02", "RB-2 active label mismatch")
    require(rb2["route_label"] == "ROUTE-B", "RB-2 route label mismatch")
    require(rb2["input_id"] == "RB-2", "RB-2 input id mismatch")
    require(rb2["row_count"] == 72 and len(rb2["rows"]) == 72, "RB-2 row count mismatch")
    require(rb2["all_rows_have_values"] is True, "RB-2 values missing")
    require(rb2["all_rows_selected"] is False, "RB-2 rows overselected")
    require(rb2["computed_from_independent_galerkin_quadrature"] is False, "RB-2 overclaims independent quadrature")
    require(rb2["selected_emitted"] is False, "RB-2 overemitted")
    require(rb2["theorem_derived"] is False, "RB-2 overderived")
    require(rb2["source_owner_verified"] is False, "RB-2 source oververified")
    require(all(row["residual_replay_dependency"] is True for row in rb2["rows"]), "RB-2 rows should disclose replay dependency")
    require(all(row["selected_emitted"] is False for row in rb2["rows"]), "RB-2 row overemitted")

    require(superset["active_label"] == "PSM-C1-02", "superset active label mismatch")
    require(superset["closed_boundary"] == "DONE-PARITY-00", "superset boundary mismatch")
    require(superset["paths_used_as_knobs"] is False, "superset paths used as knobs")
    require("72 primitive row contract" in superset["locked_target"], "superset target mismatch")
    require(all(ref["used_as_source_proof"] is False for ref in superset["external_references"]), "external references overused")

    require(next_work["active_label"] == "PSM-C1-02", "next active label mismatch")
    require(next_work["primary"]["route_label"] == "ROUTE-A", "next primary route mismatch")
    require(next_work["primary"]["clause_id"] == "RA-1", "next primary clause mismatch")
    require(next_work["secondary"]["route_label"] == "ROUTE-B", "next secondary route mismatch")
    require(next_work["secondary"]["input_id"] == "RB-3", "next secondary input mismatch")

    require(cert["active_label"] == "PSM-C1-02", "cert active label mismatch")
    require(cert["closure_claimed"] is False, "cert overclaimed closure")
    require(cert["route_A_RA1_closed"] is False, "cert RA-1 overclosed")
    require(cert["route_B_RB2_input_filled"] is True, "cert RB-2 not filled")
    require(cert["route_B_RB2_selected_promoted"] is False, "cert RB-2 overpromoted")
    require(cert["primitive_row_count"] == 72, "cert row count mismatch")
    require("Status label: `PSM-C1-02 / ROUTE-A / RA-1`" in note, "note missing labels")
    require("External references are methodological only" in note, "note missing external guardrail")

    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
