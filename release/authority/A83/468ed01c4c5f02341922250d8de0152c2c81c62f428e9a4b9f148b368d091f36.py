from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_sharedcircleclosurehessiantogaugezeromoderestrictionandcountertermcompleteness"
STATUS = (
    "MTT_SELECTED_CANONICAL_COVARIANT_GAUGE_RESTRICTION_CLOSED_ONE_EXPLICIT_CLOSURESHADOW_"
    "ACTION_PREMISE_IDENTIFIED_CONDITIONAL_RELATIVE_ACTION_CLOSED_STRICT_DERIVATION_OPEN"
)
NEXT = "MTT_Selected_ClosureShadowGaugeActionAxiomDerivation_or_ExplicitAdoptionAndHeldOutValidation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    restriction = load(ROOT / "candidate_data" / SLUG / "canonical_heat_density_and_gauge_zero_mode_hessian.packet.json")
    independence = load(ROOT / "candidate_data" / SLUG / "closure_cost_vs_physical_action_logical_independence.packet.json")
    axiom = load(ROOT / "candidate_data" / SLUG / "minimal_closure_shadow_gauge_action_axiom.packet.json")
    conditional = load(ROOT / "candidate_data" / SLUG / "conditional_action_counterterm_and_spectator_execution.packet.json")
    gate = load(ROOT / "candidate_data" / SLUG / "remaining_axiom_derivation_or_adoption_gate.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_SharedCircleClosureHessianToGaugeZeroModeRestrictionAndCountertermCompleteness_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(restriction["finite_density"]["dimension"] == 18, "density dimension")
    check(restriction["finite_density"]["positive_definite"], "density positivity")
    check(restriction["finite_density"]["commutes_with_gauge_action"], "commutant")
    check(restriction["gauge_covariantization"]["mathematical_restriction_closed"], "restriction")
    check(restriction["gauge_covariantization"]["kinetic_residual"] < 1e-13, "K replay")
    check(restriction["gauge_covariantization"]["ratio_residual"] < 1e-14, "ratio replay")
    check(independence["theorem"]["proved"], "independence theorem")
    check(independence["proto_spinor_boundary"]["closure_cost_explicitly_not_a_Lagrangian"], "ProtoSpinor guard")
    check(independence["spectral_shadow_boundary"]["proper_time_representation_stated_as_assumption"], "proper-time guard")
    check(axiom["name"] == "ClosureShadowGaugeActionAxiom", "axiom name")
    check(axiom["parameter_policy"]["structural_action_premises"] == 1, "premise count")
    check(axiom["parameter_policy"]["new_continuous_numerical_parameters"] == 0, "numeric parameters")
    check(not axiom["epistemic_status"]["derived_from_current_MTT_axioms"], "axiom overclaim")
    check(conditional["conditional_results"]["gauge_K_rows_emitted"] == 3, "conditional rows")
    check(conditional["conditional_results"]["A75_relative_counterterm_coordinates_fixed_to"] == [0.0, 0.0], "counterterms")
    check(not conditional["unconditional_results"]["physical_action_source_closed"], "physical source overclaim")
    check(all(gate["closed"].values()), "closed gate")
    check(all(gate["open"].values()), "open gate")
    check(cert["strict_gauge_values_accepted"] == 0, "strict values")
    check(cert["conditional_gauge_values_emitted"] == 3, "conditional values")
    check(cert["new_continuous_numerical_parameters"] == cert["new_discrete_numerical_parameters"] == 0, "parameters")
    for phrase in ["Exact covariant restriction", "Why physical identity does not follow automatically", "Minimal sufficient premise", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("shared-circle closure Hessian/gauge restriction audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
