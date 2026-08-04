"""Audit latest source-frontier reconciliation / dynamic C1 proof gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_latest_sourcefrontier_reconciliation_or_dynamicc1proofgate"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FRONTIER = PACKET_DIR / "latest_source_frontier_reconciled.packet.json"
DYNAMIC_GATE = PACKET_DIR / "dynamic_c1_remaining_proof_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LatestSourceFrontier_Reconciliation_or_DynamicC1ProofGate_v1.md"

STATUS = "MTT_SELECTED_LATEST_SOURCEFRONTIER_RECONCILED_DYNAMICC1_PROOFGATE_OPEN"
NEXT = "MTT_Selected_DeriveResidualProjectorAxiom_or_IndependentGalerkinC1Execution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    frontier = load(FRONTIER)
    dynamic_gate = load(DYNAMIC_GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")

    require(data["SM_parity_closed"] is True, "SM parity reopened")
    require(data["true_SM_equivalence_closed"] is False, "true SM equivalence overclaimed")
    require(data["no_knob_closed"] is False, "no-knob overclaimed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    static = frontier["static_source_tier"]
    for key in [
        "all_six_SM_slot_arrows_closed",
        "selected_terminal_to_SU5_E6_slot_packet",
        "selected_U10_Ubar5_source_outputs",
        "selected_static_sector_route_Z_to_u_e_X_to_d_nuD",
        "selected_static_1M_Dirac_neutrino_shift_rule",
        "selected_static_finite_trace_transfer_normalization",
    ]:
        require(static[key] is True, f"static source closure missing: {key}")

    dynamic = frontier["dynamic_C1_tier"]
    require(dynamic["patched_spine_dynamic_packet_closed"] is True, "patched dynamic C1 not closed")
    require(dynamic["unpatched_dynamic_packet_closed"] is False, "unpatched dynamic C1 overclosed")
    require(dynamic["source_map_selection_test_built"] is True, "source map test missing")
    require(dynamic["if_selected_dynamic_packet_closure_exact"] is True, "conditional dynamic closure missing")

    for key, value in frontier["stale_blockers_retired"].items():
        require(value is True, f"stale blocker not retired: {key}")
    for key, value in frontier["still_open"].items():
        require(value is True, f"open gate missing: {key}")

    require("route_A_unpatched_derivation" in dynamic_gate["legal_routes"], "route A missing")
    require("route_B_independent_Galerkin_execution" in dynamic_gate["legal_routes"], "route B missing")
    require(len(dynamic_gate["forbidden_shortcuts"]) == 4, "forbidden shortcuts changed")
    require(dynamic_gate["closure_claimed"] is False, "dynamic gate closure overclaimed")

    for key in [
        "latest_source_frontier_reconciled",
        "static_U10_Ubar5_1M_overlap_gates_retired",
        "dynamic_C1_unpatched_proof_gate_selected",
        "patched_spine_vs_unpatched_noknob_boundary_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    require(cert["static_source_tier_closed"] is True, "certificate static tier missing")
    require(cert["dynamic_C1_unpatched_proof_gate_open"] is True, "certificate dynamic gate missing")
    require("The static source frontier is now closed" in note, "note missing static closure")
    require("not a no-knob derivation" in note, "note missing no-knob guard")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
