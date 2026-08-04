from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_closureshadowgaugeactionaxiomderivation_or_explicitadoptionandheldoutvalidation"
STATUS = (
    "MTT_SELECTED_CSGA1_HEATSHADOW_DERIVED_AT_REGIMELOCAL_ACTION_TIER_"
    "ONLY_FINITE_MATCHING_COMPLETENESS_AND_STRICT_PEW_REMAIN"
)
NEXT = "MTT_Selected_FiniteMatchingCompletenessFromUnifiedAction_or_ExplicitBoundaryAdoptionAndHeldOutValidation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    semigroup = load(ROOT / "candidate_data" / SLUG / "fixed_point_semigroup_to_damped_overlap_derivation.packet.json")
    action = load(ROOT / "candidate_data" / SLUG / "regime_local_unified_action_restriction.packet.json")
    reduction = load(ROOT / "candidate_data" / SLUG / "closure_shadow_axiom_clause_reduction.packet.json")
    gate = load(ROOT / "candidate_data" / SLUG / "remaining_finite_matching_completeness_gate.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_ClosureShadowGaugeActionAxiomDerivation_or_ExplicitAdoptionAndHeldOutValidation_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(all(semigroup["fixed_point_theorem_import"].values()), "fixed-point markers")
    check(semigroup["selected_time_identity"]["residual"] < 1e-15, "time identity")
    check(semigroup["finite_execution"]["commutator_Hcl_PhiC1_residual"] < 1e-14, "commutator")
    check(semigroup["finite_execution"]["factorization_residual"] < 1e-13, "factorization")
    check(semigroup["theorem"]["proved_at_fixed_point_gradient_flow_tier"], "semigroup theorem")
    check(all(action["corpus_markers"].values()), "action markers")
    check(action["CSGA1_heat_shadow_derived_at_regime_local_action_tier"], "CSGA1")
    check(not action["scope"]["global_microscopic_action_derived"], "global overclaim")
    check(reduction["clause_status"]["CSGA1_heat_shadow"]["closed"], "CSGA1 reduction")
    check(not reduction["clause_status"]["CSGA2_finite_matching_completeness"]["closed_strictly"], "CSGA2 overclaim")
    check(reduction["remaining_structural_action_premise_count"] == 1, "premise count")
    check(reduction["conditional_current_standard"]["relative_gauge_action_closed"], "current tier")
    check(all(gate["closed"].values()), "closed gate")
    check(all(gate["open"].values()), "open gate")
    check(gate["remaining_relative_gauge_numerical_objects"] == 0, "numeric objects")
    check(cert["strict_gauge_values_accepted"] == 0, "strict values")
    check(cert["conditional_gauge_values_emitted"] == 3, "conditional values")
    check(cert["new_continuous_numerical_parameters"] == cert["new_discrete_numerical_parameters"] == 0, "parameters")
    for phrase in ["CSGA1 is derivable at the action tier", "One clause remains", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("closure-shadow action axiom derivation audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
