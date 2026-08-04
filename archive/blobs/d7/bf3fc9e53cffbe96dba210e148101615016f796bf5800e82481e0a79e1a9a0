"""Audit the final two-lane dynamic C1 cutset gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalactionrestrictionemission_or_independentgalerkinrows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_physical_emission_acceptance.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_galerkin_rows_acceptance.packet.json"
CUTSET = PACKET_DIR / "final_dynamic_c1_unpatched_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalActionRestrictionEmission_or_IndependentGalerkinRows_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_physicalactionrestrictionemission_or_independentgalerkinrows.py"

STATUS = "MTT_SELECTED_PHYSICALACTIONRESTRICTION_OR_INDEPENDENTGALERKINROWS_BUILT_FINAL_TWO_LANE_CUTSET_OPEN"
NEXT = "MTT_Selected_PhysicalSourceEmissionValues_or_HonestGalerkinExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("two-lane cutset" in note, "note misses two-lane cutset")
    require("A_selected=12 I_2" in note, "note misses locked A value")

    a = route_a["acceptance_table"]
    require(a["canonical_residual_values_ready"] is True, "Route A residual values not ready")
    require(a["canonical_residual_projector_replay_exact"] is True, "Route A projector replay not exact")
    require(a["b_selected_replay_target_fixed"] is True, "Route A b target not fixed")
    for key in [
        "physical_PhiFinC1_action_restriction_emitted",
        "zero_extra_boundary_or_source_emitted",
        "physical_R_Z_emitted_from_same_branch",
        "physical_R_X_emitted_from_same_branch",
        "physical_b_selected_emitted_from_same_branch",
    ]:
        require(a[key] is False, f"Route A overclaimed {key}")
    require(route_a["lane_closes_now"] is False, "Route A overclosed")
    values = route_a["canonical_values_ready"]
    require(values["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "Route A A mismatch")
    require(values["A_transpose_b"] == [12.0, 12.0], "Route A b mismatch")
    require(values["deltaTheta_C1"] == [1.0, 1.0], "Route A delta mismatch")

    b = route_b["acceptance_table"]
    require(b["strict_replay_passes"] is True, "Route B replay should pass")
    require(b["replay_A_b_delta_fixed"] is True, "Route B replay target not fixed")
    for key in [
        "selected_zero_mode_basis_emitted",
        "primitive_terms_from_independent_galerkin_quadrature",
        "independent_sector_matrices_emitted",
        "b_selected_emitted_by_independent_hessian",
        "selected_source_verified",
        "C33_nonzero_family_rank_tests_evaluated",
    ]:
        require(b[key] is False, f"Route B overclaimed {key}")
    require(route_b["lane_closes_now"] is False, "Route B overclosed")
    require(route_b["replay_support_available"]["zero_mode_basis_dimension"] == 9, "basis dimension mismatch")
    require(route_b["replay_support_available"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "Route B A mismatch")
    require(route_b["replay_support_available"]["A_transpose_b"] == [12.0, 12.0], "Route B b mismatch")
    require(route_b["replay_support_available"]["deltaTheta_C1"] == [1.0, 1.0], "Route B delta mismatch")
    for item in [
        "zero_mode_bases",
        "primitive_three_by_three_contraction_terms",
        "linear_response_matrices",
        "C33/nonzero-family-rank tests",
    ]:
        require(item in route_b["required_outputs"], f"Route B missing required output {item}")

    require(cutset["algebraic_residual_value_problem_closed"] is True, "algebraic value problem not closed")
    require(cutset["value_target_fixed"] is True, "value target not fixed")
    require(cutset["physical_source_gate_open"] is True, "physical gate should be open")
    require(cutset["honest_galerkin_gate_open"] is True, "Galerkin gate should be open")
    require(cutset["route_a_physical_emission_closes"] is False, "cutset Route A overclosed")
    require(cutset["route_b_independent_galerkin_closes"] is False, "cutset Route B overclosed")
    require(cutset["unpatched_dynamic_C1_packet_closed"] is False, "unpatched dynamic C1 overclosed")
    require(cutset["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(cutset["no_knob_closed"] is False, "no-knob overclosed")
    require(cutset["if_close_values"]["A_selected"] == [[12.0, 0.0], [0.0, 12.0]], "cutset A mismatch")
    require(cutset["if_close_values"]["b_selected"] == [12.0, 12.0], "cutset b mismatch")
    require(cutset["if_close_values"]["deltaTheta_C1"] == [1.0, 1.0], "cutset delta mismatch")

    closure = data["closure_decision"]
    require(closure["algebraic_residual_value_problem_closed"] is True, "candidate algebraic closure missing")
    require(closure["route_a_physical_emission_closes"] is False, "candidate Route A overclosed")
    require(closure["route_b_independent_galerkin_closes"] is False, "candidate Route B overclosed")
    require(closure["unpatched_dynamic_C1_packet_closed"] is False, "candidate dynamic C1 overclosed")
    require(closure["true_SM_equivalence_closed"] is False, "candidate true SM overclosed")
    require(closure["no_knob_closed"] is False, "candidate no-knob overclosed")
    require(closure["observed_constants_used_as_selectors"] is False, "candidate observed selectors used")
    require(closure["target_fitting_used"] is False, "candidate target fitting used")

    for label, payload in [
        ("candidate", data),
        ("route_a", route_a),
        ("route_b", route_b),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
