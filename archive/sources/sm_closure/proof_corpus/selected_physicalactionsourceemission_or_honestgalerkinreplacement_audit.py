"""Audit physical action-source emission / honest Galerkin replacement gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_physical_source_emission_validator.packet.json"
ROUTE_B = PACKET_DIR / "route_b_honest_galerkin_replacement_contract.packet.json"
ATTACK = PACKET_DIR / "dual_route_attack_queue.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalActionSourceEmission_or_HonestGalerkinReplacement_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHYSICALACTIONSOURCEEMISSION_OR_HONESTGALERKINREPLACEMENT_BUILT_DUAL_ROUTE_CONTRACT_OPEN"
NEXT = "MTT_Selected_RouteAEmissionOrRouteBGalerkinRowsExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    attack = load(ATTACK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(route_a["status"] == "ROUTE_A_PHYSICAL_SOURCE_EMISSION_NOT_YET_EMITTED", "route A status mismatch")
    require(len(route_a["required_emissions"]) == 6, "route A requirements incomplete")
    for key, value in route_a["current_emissions"].items():
        require(value is False, f"route A emission overclaimed: {key}")
    require(route_a["all_required_emitted_now"] is False, "route A all-emitted overclaimed")
    require(route_a["route_A_closes_now"] is False, "route A closure overclaimed")
    require("same physical Phi_fin" in route_a["validator_rule"], "route A same-source rule missing")

    require(route_b["status"] == "ROUTE_B_CONTRACT_BUILT_VALUES_NOT_EXECUTED", "route B status mismatch")
    target = route_b["strict_coordinate_target"]
    require(target["total_real_coordinates"] == 72, "72-real target mismatch")
    require(target["sectors"] == ["u", "e", "d", "nuD"], "sector target mismatch")
    rows = route_b["kernel_row_contract"]
    require(rows["primitive_rows"] == 72, "primitive row count mismatch")
    require(rows["hessian_source_rows"] == 2, "Hessian row count mismatch")
    require(rows["sector_matrix_rows"] == 36, "sector row count mismatch")
    require(rows["total_rows"] == 110, "total row count mismatch")
    require(rows["algebraic_replay_values_filled"] == 110, "algebraic replay count mismatch")
    require(len(route_b["acceptance_tests"]) == 6, "route B acceptance tests incomplete")
    require(len(route_b["forbidden_shortcuts"]) == 4, "route B guardrails incomplete")
    state = route_b["current_route_state"]
    require(state["selected_source_verified"] is False, "selected source overclaimed")
    require(state["can_replace_source_map_now"] is False, "replacement overclaimed")
    require(state["independent_rows_executed_now"] is False, "independent rows overclaimed")
    require(state["route_B_closes_now"] is False, "route B closure overclaimed")

    require(attack["status"] == "TWO_LEGAL_ATTACKS_FIXED_NEITHER_EXECUTED", "attack status mismatch")
    require(len(attack["route_A_next_minimal_actions"]) == 4, "route A attack queue incomplete")
    require(len(attack["route_B_next_minimal_actions"]) == 4, "route B attack queue incomplete")
    for key, value in attack["already_not_blockers"].items():
        require(value is True, f"not-blocker missing: {key}")
    for key, value in attack["remaining_cutset"].items():
        require(value is True, f"remaining cutset missing: {key}")

    for key in [
        "route_A_validator_built",
        "route_B_replacement_contract_built",
        "kernel_row_counts_locked",
        "dual_route_attack_queue_built",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "route_A_physical_source_emission",
        "route_B_independent_Galerkin_rows",
        "A_selected",
        "b_selected",
        "deltaTheta_C1",
        "sector_response_matrices",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key, value in data["promotion_decision"].items():
        require(value is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "closure overclaimed")
    require("Route A physical source emission closes now = False" in note, "note missing route A guardrail")
    require("Route B honest Galerkin replacement closes = False" in note, "note missing route B guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
