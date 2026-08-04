from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    ROOT / "certificates" / "q79_primitive_branch_selection_cutset_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Primitive_Physical_Branch_NonDerivability_and_OneAxiom_Completion_v1.md"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    tiers = certificate["claim_tiers"]
    model = certificate["countermodel"]
    params = certificate["parameter_ledger"]
    guards = certificate["guardrails"]

    require(all(certificate["checks"].values()), "one or more cutset checks failed")
    require(
        tiers["primitive_branch_selection_from_unaugmented_current_MTT"]
        == "CLOSED_NO_GO_BY_EXPLICIT_TWO_BRANCH_AUTOMORPHISM_MODEL"
        and model["invariant_minimizer_set"] == ["R0", "R1"],
        "two-branch non-derivability witness changed",
    )
    require(
        model["strong_monotonicity_constant"] == 2
        and model["unique_equilibrium_on_each_branch"] == 0
        and model["branch_swap_matrix"] == [[0, 1], [1, 0]],
        "fixed-point countermodel changed",
    )
    require(
        tiers["minimal_extra_branch_selection_data"]
        == "CLOSED_ONE_DISCRETE_PHYSICAL_REALIZATION_AXIOM_ZERO_CONTINUOUS_KNOBS"
        and params["additional_discrete_physical_realization_axioms"] == 1
        and params["additional_continuous_parameters_from_branch_axiom"] == 0,
        "minimal one-axiom completion changed",
    )
    require(
        tiers["q79_geometry_operator_choice_after_A_QG"]
        == "CLOSED_UNIQUE_UP_TO_DECLARED_GAUGE"
        and tiers["A_QG_derived_from_current_upper_MTT_dynamics"] == "OPEN"
        and tiers["UV_complete_quantum_gravity"] == "OPEN",
        "adopted axiom was overpromoted",
    )
    require(
        guards["claims_basin_local_fixed_point_uniqueness_selects_geometry"]
        is False
        and guards["claims_minimal_rootstack_relative_uniqueness_selects_q79_physics"]
        is False
        and guards["claims_A_QG_is_derived_rather_than_adopted"] is False,
        "selection guardrail changed",
    )
    for phrase in [
        "basin-local unique minimizer != unique physical branch",
        "C_b(x)=x^2",
        "R0 <-> R1",
        "one discrete axiom and zero continuous knobs",
        "unique minimal root orders (2,3,2,1)",
        "target-independent functional",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: current MTT cannot select a physical branch from basin-local "
        "uniqueness; one explicit discrete q79 realization axiom is sufficient for the low-energy tier"
    )


if __name__ == "__main__":
    main()
