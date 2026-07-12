"""Audit PhiFin C1 action axiom or independent Galerkin kernel emission gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phifinc1actionaxiom_or_independentgalerkinkernelemission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
AXIOM_CONTRACT = PACKET_DIR / "route_a_phifinc1_action_kernel_axiom_contract.packet.json"
KERNEL_EMISSION = PACKET_DIR / "route_b_independent_galerkin_kernel_emission_contract.packet.json"
VALIDATOR = PACKET_DIR / "four_clause_validator_current_result.packet.json"
CUTSET = PACKET_DIR / "minimal_next_cutset_after_action_kernel_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinC1ActionAxiom_or_IndependentGalerkinKernelEmission_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHIFINC1ACTIONAXIOM_OR_INDEPENDENTGALERKINKERNELEMISSION_BUILT_FOUR_CLAUSE_CONTRACT_OPEN"
NEXT = "MTT_Selected_ActionKernelFourClauseProof_or_IndependentKernelValuesRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(AXIOM_CONTRACT)
    route_b = load(KERNEL_EMISSION)
    validator = load(VALIDATOR)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(data["patched_SM_parity_closure_preserved"] is True, "patched support not preserved")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    expected_four = [
        "selected_pre_residual_variation_functional",
        "same_source_hessian_b_selected",
        "sector_functor_assembly",
        "source_independence_from_residual_projector_replay",
    ]
    require(route_a["four_required_clauses"] == expected_four, "four-clause list mismatch")
    require(all(value is False for value in route_a["current_clause_values"].values()), "route A overfilled")
    require(route_a["conditional_witness_available"] is True, "conditional witness missing")
    require(route_a["proved_now"] is False and route_a["inserted_as_axiom_now"] is False, "route A overpromoted")
    require(
        route_a["if_all_four_clauses_proved"]["unpatched_SM_parity_dynamic_packet_closes"] is True,
        "route A implication missing",
    )

    required_emissions = route_b["required_emissions"]
    require(len(required_emissions) == 6, "route B emission count mismatch")
    require(all(value is False for value in required_emissions.values()), "route B overfilled")
    require(route_b["slot_support"]["primitive_row_slots"] == 72, "primitive slot count mismatch")
    require(route_b["slot_support"]["sector_matrix_slots"] == 36, "sector slot count mismatch")
    require(route_b["slot_support"]["hessian_source_slots"] == 2, "hessian slot count mismatch")
    require(route_b["values_emitted_now"] is False, "route B values overemitted")

    require(validator["current_support_passes"] is False, "current support overaccepted")
    require(validator["conditional_witness_passes"] is True, "conditional witness should pass")
    require(validator["route_A_all_four_clauses_pass"] is False, "route A validator overaccepted")
    require(validator["route_B_all_kernel_values_emitted"] is False, "route B validator overaccepted")
    require(len(validator["why_rejected"]) == 4, "expected four rejection reasons")

    require(cutset["status"] == "NEXT_CUTSET_SELECTED", "cutset status mismatch")
    require(cutset["minimal_route_A"] == expected_four, "cutset route A mismatch")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")

    for key in [
        "four_clause_action_kernel_contract_built",
        "independent_kernel_emission_contract_built",
        "current_rejection_reason_machine_checkable",
        "formal_110_row_values_retained_as_support",
        "observed_constants_excluded_as_selectors",
        "target_fitting_excluded",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")

    for key in [
        "selected_pre_residual_variation_functional",
        "same_source_hessian_b_selected",
        "sector_functor_assembly_as_physical_source",
        "source_independence_from_residual_projector_replay",
        "independent_galerkin_kernel_values",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "no_knob_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")

    decision = data["promotion_decision"]
    for key in [
        "route_A_four_clause_action_kernel_proved",
        "route_A_axiom_inserted",
        "route_B_independent_kernel_emission_run",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    for phrase in [
        "formal 110-row finite replay",
        "remaining Route A proof is exactly four clauses",
        "does not claim unpatched closure",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
