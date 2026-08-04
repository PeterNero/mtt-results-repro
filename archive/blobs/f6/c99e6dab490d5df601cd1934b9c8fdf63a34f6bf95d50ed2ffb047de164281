"""Audit PhiFinC1 action restriction / boundary-source emission gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phifinc1_actionrestriction_or_boundarysource_emission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
VALIDATOR = PACKET_DIR / "route_a_action_restriction_validator_v2.packet.json"
SOURCE_EMISSION = PACKET_DIR / "same_source_boundary_and_residual_emission_contract.packet.json"
IF_CLOSES = PACKET_DIR / "if_action_restriction_emitted_dynamic_c1_closure.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinC1_ActionRestriction_or_BoundarySource_Emission_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_phifinc1_actionrestriction_or_boundarysource_emission.py"

STATUS = "MTT_SELECTED_PHIFINC1_ACTIONRESTRICTION_OR_BOUNDARYSOURCE_EMISSION_BUILT_MEASURE_RETIRED_SOURCE_OPEN"
NEXT = "MTT_Selected_SameSourceBoundaryResidualEmission_or_UnpatchedGalerkinReplacement_v1"


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
    validator = load(VALIDATOR)
    source = load(SOURCE_EMISSION)
    if_closes = load(IF_CLOSES)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require("finite measure-normalization blocker is retired" in note, "note misses measure retirement")
    require("remaining unpatched dynamic C1 gate is physical source emission" in note, "note misses source gate")

    closed = validator["closed_subclauses"]
    for key in [
        "finite_selected_C1_quotient",
        "selected_Weyl_variation_algebra",
        "finite_measure_normalization_trace_Frobenius",
        "algebraic_finite_boundary_cancellation",
    ]:
        require(closed[key] is True, f"closed subclause missing: {key}")

    required = validator["still_required_physical_subclauses"]
    for key in [
        "physical_PhiFinC1_action_restriction",
        "no_extra_physical_boundary_or_source_term",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
        "same_source_b_selected_emission",
    ]:
        require(required[key] is True, f"physical subclause not required: {key}")
    require(validator["route_A_currently_closes"] is False, "Route A overclosed")

    must_emit = source["must_emit_from_same_physical_branch"]
    for item in [
        "physical_PhiFinC1_action_identity",
        "restriction map from physical Phi_fin^C1/action to selected finite Weyl quotient",
        "zero extra boundary/source term or emitted cancellation term",
        "phase residual source R_Z",
        "shift residual source R_X",
        "Hessian/source vector b_selected",
    ]:
        require(item in must_emit, f"emission missing: {item}")
    require(source["b_selected_replay_available"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A replay mismatch")
    require(source["b_selected_replay_available"]["A_transpose_b"] == [12.0, 12.0], "b replay mismatch")
    require(source["b_selected_replay_available"]["deltaTheta_C1"] == [1.0, 1.0], "delta replay mismatch")
    require(source["b_selected_replay_available"]["same_source_b_selected_emitted_now"] is False, "b overemitted")

    antecedent = if_closes["antecedent"]
    require(antecedent["measure_normalization_derived"] is True, "measure antecedent missing")
    for key in [
        "physical_PhiFinC1_action_restriction_emitted",
        "no_extra_boundary_source_emitted",
        "phase_R_Z_source_emitted",
        "shift_R_X_source_emitted",
        "b_selected_emitted",
    ]:
        require(antecedent[key] is False, f"antecedent overemitted: {key}")
    consequent = if_closes["consequent_if_antecedent_true"]
    require(consequent["physical_A_selected"] == [[12.0, 0.0], [0.0, 12.0]], "if-close A mismatch")
    require(consequent["physical_b_selected"] == [12.0, 12.0], "if-close b mismatch")
    require(consequent["physical_deltaTheta_C1"] == [1.0, 1.0], "if-close delta mismatch")
    require(consequent["unpatched_SM_parity_dynamic_packet_closed"] is True, "if-close implication missing")
    require(if_closes["promoted_now"] is False, "if-close overpromoted")

    closure = data["closure_decision"]
    require(closure["measure_normalization_derived"] is True, "measure closure missing")
    require(closure["physical_action_restriction_emitted"] is False, "action restriction overemitted")
    require(closure["no_extra_boundary_source_emitted"] is False, "boundary/source overemitted")
    require(closure["same_source_R_Z_R_X_b_selected_emitted"] is False, "same-source residuals overemitted")
    require(closure["unpatched_A_selected_emitted"] is False, "unpatched A overclaimed")
    require(closure["unpatched_b_selected_emitted"] is False, "unpatched b overclaimed")
    require(closure["unpatched_deltaTheta_C1_emitted"] is False, "unpatched delta overclaimed")
    require(closure["unpatched_dynamic_C1_packet_closed"] is False, "unpatched closure overclaimed")
    require(closure["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(closure["no_knob_closed"] is False, "no-knob overclaimed")

    for label, payload in [
        ("candidate", data),
        ("validator", validator),
        ("source", source),
        ("if_closes", if_closes),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
