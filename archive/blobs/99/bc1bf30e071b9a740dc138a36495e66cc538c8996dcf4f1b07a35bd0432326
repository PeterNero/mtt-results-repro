from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    ROOT
    / "certificates"
    / "q79_finite_source_tegr_classical_closure_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Finite_Source_TEGR_Classical_Closure_and_Parameter_Ledger_v1.md"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    tiers = certificate["claim_tiers"]
    ledger = certificate["parameter_ledger"]
    guards = certificate["guardrails"]

    require(all(certificate["checks"].values()), "one or more composition checks failed")
    require(
        tiers["classical_GR_equivalence_at_declared_finite_source_IR_tier"]
        == "CLOSED_CONDITIONAL_WITH_TWO_EFFECTIVE_GRAVITATIONAL_COORDINATES",
        "declared classical closure tier changed",
    )
    require(
        ledger["continuous_effective_law_parameter_count"] == 2
        and ledger["dimensionless_gravity_shape_parameters"] == 0
        and ledger["independent_stress_normalizations"] == 0
        and ledger["independent_TEGR_constitutive_ratios"] == 0,
        "classical parameter count changed",
    )
    require(
        ledger["initial_or_boundary_state"]["counted_as_law_parameter"] is False,
        "state data were incorrectly counted as a coupling",
    )
    require(
        tiers["full_quantum_gravity"] == "OPEN"
        and tiers["higher_derivative_quantum_UV_completion"] == "OPEN"
        and guards["claims_quantum_gravity_closed"] is False,
        "quantum tier was overpromoted",
    )
    require(
        guards["claims_numeric_Newton_constant_derived"] is False
        and guards["claims_cosmological_constant_derived"] is False
        and guards["uses_observed_GR_values"] is False,
        "scale, Lambda, or data guardrail changed",
    )
    for phrase in [
        "H_std = kappa_e I2",
        "kappa_h = kappa_e/4",
        "(c1,c2,c3) proportional to (1/4,1/2,-1)",
        "exactly two continuous effective",
        "State is not a coupling",
        "Full quantum gravity is not yet closed",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: finite q79 TT shape plus strict same-source TEGR closes "
        "the declared two-derivative classical GR tier with exactly kappa and Lambda; QG remains open"
    )


if __name__ == "__main__":
    main()
