"""Audit dynamic C1 proof-cycle condensation / cycle-exit gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicc1proofcycle_condensation_or_cycleexit"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CYCLE_PACKET = PACKET_DIR / "dynamic_c1_attempt_cycle_condensation.packet.json"
CUTSET_PACKET = PACKET_DIR / "shared_cycle_exit_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicC1ProofCycleCondensation_or_CycleExit_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DYNAMICC1_PROOF_CYCLE_CONDENSED_SHARED_EXIT_CUTSET_OPEN"
NEXT = "MTT_Selected_CycleExit_MinimizerTrace_or_IndependentQuadratureRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cycle = load(CYCLE_PACKET)
    cutset = load(CUTSET_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(cycle["status"] == "CYCLE_CONDENSED", "cycle status mismatch")
    require(cycle["node_count"] >= 20, "cycle too small")
    require(cycle["all_nodes_present"] is True, "cycle nodes missing")
    require(cycle["all_next_edges_match_declared_cycle"] is True, "cycle edge mismatch")
    require(cycle["all_guardrails_preserved"] is True, "cycle guardrail mismatch")
    require(cycle["important_flags_pass"] is True, "important flag mismatch")
    for node in cycle["nodes"]:
        require(node["closure_claimed"] is False, f"closure overclaimed in {node['slug']}")
        require(node["target_fitting_used"] is False, f"target fitting in {node['slug']}")
        require(node["observed_data_used"] is False, f"observed data in {node['slug']}")

    require(cutset["status"] == "SHARED_EXIT_CUTSET_SELECTED", "cutset status mismatch")
    require("Phi_fin^C1" in cutset["shared_missing_object"], "missing shared object")
    require(cutset["already_closed_inside_cycle"]["dynamic_dotD_trace_binding"] is True, "dotD not closed inside cycle")
    require(cutset["already_closed_inside_cycle"]["formal_C1_defect_functional_uniqueness"] is True, "functional source not closed")
    require(cutset["straight_route"]["name"] == "minimizer_trace_first_variation_route", "straight route mismatch")
    require(cutset["parallel_route"]["name"] == "independent_quadrature_hessian_route", "parallel route mismatch")
    require(cutset["locked_target"]["A_transpose_b"] == [12.0, 12.0], "locked b mismatch")
    require(cutset["locked_target"]["deltaTheta_C1"] == [1.0, 1.0], "locked delta mismatch")
    require(cutset["superset_strategy"]["using_combined_paths"] is True, "superset strategy missing")

    for key in [
        "proof_cycle_detected_and_condensed",
        "backfill_does_not_move_frontier_backward",
        "shared_missing_object_identified",
        "straight_and_parallel_superset_paths_locked_to_same_target",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "I1_selected_minimizer_to_PhiFin_trace",
        "I5_selected_dotD_C1_response",
        "I10_PhiFinC1_minimizes_defect_functional",
        "I11_first_variation_boundary_cancellation",
        "independent_quadrature_rows",
        "selected_b_selected",
        "sector_response_matrices",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")

    decision = data["promotion_decision"]
    for key in [
        "cycle_exit_proved",
        "straight_route_accepted",
        "parallel_route_accepted",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("cycle nodes" in note and "Shared exit cutset" in note, "note missing summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
