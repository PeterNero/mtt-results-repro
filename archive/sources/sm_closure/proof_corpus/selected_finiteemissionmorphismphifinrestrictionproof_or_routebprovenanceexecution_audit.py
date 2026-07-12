"""Audit selected Phi_fin finite-emission restriction proof attack."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finiteemissionmorphismphifinrestrictionproof_or_routebprovenanceexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FUNCTIONAL_PROOF = PACKET_DIR / "functional_phi_fin_restriction_proof.packet.json"
MORPHISM_GATE = PACKET_DIR / "finite_emission_morphism_restriction_gate.packet.json"
UNPATCHED_ATTEMPT = PACKET_DIR / "unpatched_route_a_source_certificate_attempt.packet.json"
UNPATCHED_VALIDATOR = PACKET_DIR / "unpatched_route_a_validator_result.packet.json"
CONDITIONAL_VALIDATOR = PACKET_DIR / "conditional_route_a_validator_replay.packet.json"
ROUTE_B_STATUS = PACKET_DIR / "route_b_provenance_execution_status.packet.json"
TRANSPORT_CONTRACT = PACKET_DIR / "transport_closed_finite_replay_contract.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_finite_emission_restriction_attack.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteEmissionMorphismPhiFinRestrictionProof_or_RouteBProvenanceExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_FINITEEMISSIONMORPHISMPHIFINRESTRICTIONPROOF_OR_ROUTEBPROVENANCEEXECUTION_"
    "BUILT_FUNCTIONAL_RESTRICTION_PROVED_FINITE_REPLAY_OPEN"
)
NEXT = "MTT_Selected_TransportClosedPhiFinFiniteReplay_or_SymbolicConjugationValidator_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    functional = load(FUNCTIONAL_PROOF)
    gate = load(MORPHISM_GATE)
    unpatched_attempt = load(UNPATCHED_ATTEMPT)
    unpatched_validator = load(UNPATCHED_VALIDATOR)
    conditional_validator = load(CONDITIONAL_VALIDATOR)
    route_b = load(ROUTE_B_STATUS)
    transport = load(TRANSPORT_CONTRACT)
    cutset = load(NEXT_CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(functional["status"] == "FUNCTIONAL_RESTRICTION_PROVED_FINITE_EMISSION_PROMOTION_OPEN", "functional status mismatch")
    require(functional["restriction_map_matched"]["same_map_at_functional_level"] is True, "functional map not matched")
    require(functional["restriction_map_matched"]["same_map_as_finite_emission_morphism"] is False, "finite map overmatched")
    require(functional["finite_replay_boundary"]["finite_27_mode_validator_replay_closed"] is False, "finite replay overclosed")
    require(functional["finite_replay_boundary"]["direct_truncated_relative_residual"] > 0.0, "missing finite replay obstruction")

    current = gate["current_gate_values"]
    require(current["finite_codomain_schema_built"] is True, "Phi_fin schema missing")
    require(current["source_origin_reduced_to_phi_fin"] is True, "source origin reduction missing")
    require(current["functional_gauge_transported_phi_fin_trace_proved"] is True, "functional trace missing")
    require(current["functional_restriction_map_matched"] is True, "functional restriction missing")
    require(current["finite_27_mode_validator_replay_closed"] is False, "finite replay overclaimed")
    require(current["transport_closed_basis_or_symbolic_validator_emitted"] is False, "transport validator overemitted")
    require(current["unpatched_source_row_premise_free"] is False, "premise-free row overclaimed")
    require(current["finite_emission_morphism_restriction_proved"] is False, "finite morphism overproved")

    route_a = unpatched_attempt["route_A_physical_source_certificate"]
    require(route_a["physical_action_restricts_to_selected_finite_Weyl_quotient"] is False, "unpatched attempt overfilled")
    require(unpatched_validator["returncode"] == 1, "unpatched validator should reject")
    require(any("Route A missing" in line for line in unpatched_validator["stderr_lines"]), "Route A missing error absent")
    require(conditional_validator["returncode"] == 0, "conditional validator should pass")
    require(any("PASS" in line for line in conditional_validator["stdout"]), "conditional validator PASS absent")

    require(route_b["all_72_primitive_rows_executed"] is True, "Route B primitive rows not ready")
    require(route_b["formal_110_rows_executed"] is True, "Route B formal rows not ready")
    require(route_b["selected_basis_independent_of_residual_projector"] is False, "Route B basis overfilled")
    require(route_b["quadrature_rule_independent_of_locked_target"] is False, "Route B quadrature overfilled")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "Route B replay overfilled")
    require(route_b["exactness_or_error_certificates_attached"] is False, "Route B exactness overfilled")

    require(transport["required_object"] == NEXT, "transport contract next mismatch")
    require(transport["minimal_numerical_obstruction"]["direct_truncated_relative_residual"] > 0.0, "transport obstruction absent")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(data["promotion_decision"]["functional_phi_fin_restriction_proved"] is True, "functional proof not promoted")
    require(data["promotion_decision"]["finite_emission_morphism_restriction_proved"] is False, "finite morphism overpromoted")
    require(data["promotion_decision"]["unpatched_route_A_source_certificate_valid"] is False, "unpatched Route A overpromoted")
    require("The finite emission morphism is still not premise-free" in note, "note missing guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
