"""Audit PSM-C1-02 unpatched source-rule proof or honest Galerkin export gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_psm_c1_02_unpatchedsourceruleproof_or_honestgalerkinexport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_unpatched_source_rule_proof_attempt.packet.json"
ROUTE_A_LADDER = PACKET_DIR / "route_a_four_clause_ladder.packet.json"
ROUTE_B = PACKET_DIR / "route_b_honest_galerkin_export_manifest.packet.json"
IMPLICATION = PACKET_DIR / "psm_c1_02_unpatched_closure_implication.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_UnpatchedSourceRuleProof_or_HonestGalerkinExport_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_UNPATCHEDSOURCERULEPROOF_OR_HONESTGALERKINEXPORT_BUILT_INPUTS_SHARP"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    route_a = load(ROUTE_A)
    ladder = load(ROUTE_A_LADDER)
    route_b = load(ROUTE_B)
    implication = load(IMPLICATION)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "status mismatch")
    require(data["active_post_sm_parity_label"] == "PSM-C1-02", "active label mismatch")
    require(data["active_routes"] == ["ROUTE-A", "ROUTE-B"], "active routes mismatch")
    require(data["post_sm_parity_label_context"]["closed_boundary"] == "DONE-PARITY-00", "closed boundary missing")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["closure_claimed"] is False, "candidate overclaimed closure")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(route_a["active_label"] == "PSM-C1-02", "Route A active label mismatch")
    require(route_a["route_label"] == "ROUTE-A", "Route A label mismatch")
    require(route_a["free_axiom_patch_used"] is False, "Route A used patch")
    require(route_a["all_required_clauses_closed_now"] is False, "Route A overclosed")
    require(route_a["unpatched_source_rule_proved_now"] is False, "Route A source rule overproved")
    require(len(route_a["required_clauses"]) == 4, "Route A clause count mismatch")
    require(all(item["closed_now"] is False for item in route_a["required_clauses"].values()), "Route A clause unexpectedly closed")

    require(ladder["active_label"] == "PSM-C1-02", "ladder active label mismatch")
    require(ladder["route_label"] == "ROUTE-A", "ladder route label mismatch")
    require(ladder["first_open_clause"] == "RA-1", "first open clause mismatch")
    require([item["clause_id"] for item in ladder["ordered_clauses"]] == ["RA-1", "RA-2", "RA-3", "RA-4"], "Route A ladder order mismatch")

    require(route_b["active_label"] == "PSM-C1-02", "Route B active label mismatch")
    require(route_b["route_label"] == "ROUTE-B", "Route B label mismatch")
    require(route_b["free_axiom_patch_used"] is False, "Route B used patch")
    require(route_b["ready_as_execution_spec"] is True, "Route B spec should be ready")
    require(route_b["run_now"] is False, "Route B overclaimed run")
    require(route_b["honest_galerkin_table_exported"] is False, "Route B overexported")
    require(route_b["missing_input_count"] == 4, "Route B missing input count mismatch")
    require(route_b["all_missing_inputs_exist_now"] is False, "Route B inputs unexpectedly all exist")
    require(all(item["selected_emitted"] is False for item in route_b["missing_selected_inputs"]), "Route B input overemitted")

    require(implication["active_label"] == "PSM-C1-02", "implication active label mismatch")
    require(implication["source_promotion_conditional_packet_passes"] is True, "conditional source packet should pass")
    require(implication["current_source_promotion_packet_passes"] is False, "current source packet overclaimed")
    require(implication["patched_packet_rejected_for_unpatched_proof"] is True, "patch not rejected")
    require(implication["exact_dynamic_values_ready"] is True, "exact dynamic values should be ready")
    require(implication["closure_claimed"] is False, "implication overclaimed closure")

    require(next_work["active_label"] == "PSM-C1-02", "next active label mismatch")
    require(next_work["primary"]["route_label"] == "ROUTE-A", "next primary route mismatch")
    require(next_work["primary"]["clause_id"] == "RA-1", "next primary clause mismatch")
    require(next_work["secondary"]["route_label"] == "ROUTE-B", "next secondary route mismatch")
    require(next_work["secondary"]["input_id"] == "RB-1", "next secondary input mismatch")
    require(cert["active_label"] == "PSM-C1-02", "cert active label mismatch")
    require(cert["routes"] == ["ROUTE-A", "ROUTE-B"], "cert routes mismatch")
    require(cert["closure_claimed"] is False, "cert overclaimed closure")
    require(cert["route_A_all_clauses_closed"] is False, "cert overclaims Route A")
    require(cert["route_B_run_now"] is False, "cert overclaims Route B")
    require("Status label: `PSM-C1-02 / ROUTE-A / ROUTE-B`" in note, "note missing label")
    require("Closed boundary label: `DONE-PARITY-00`" in note, "note missing closed boundary")

    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
