from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "spectral_action_einstein_ir_limit_certificate.json"
NOTE = ROOT / "proof_corpus" / "Spectral_Action_Einstein_IR_Limit_and_Vacuum_Obstruction_v1.md"

STATUS = (
    "SPECTRAL_EINSTEIN_WEYL_IR_RATIO_CLOSED_CONDITIONAL_ONE_ATOM_TIER_"
    "BARE_VACUUM_OBSTRUCTION_CLOSED_FULL_ACTION_SELECTION_AND_REMAINDER_OPEN"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    normalized_note = " ".join(note.lower().split())
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]
    ir = cert["Einstein_Weyl_IR_theorem"]

    require(cert["status"] == STATUS, "spectral IR status changed")
    require(all(cert["checks"].values()), "one or more spectral IR checks failed")
    require(
        cert["active_finite_Dirac_branch"]["c_R"] == 0.0
        and cert["active_finite_Dirac_branch"]["d_R"] == 0.0,
        "active Dirac-only Majorana invariants changed",
    )
    require(
        ir["beta_squared_over_Lambda_squared_exact"] == "20/(3 tau_int)"
        and ir["relative_Weyl_correction"] == "epsilon_W(p)=p^2/beta^2",
        "Einstein/Weyl ratio changed",
    )
    require(
        tiers["dimensionless_Einstein_Weyl_ratio"]
        == "CLOSED_CONDITIONAL_ON_A53_ONE_ATOM_TIER"
        and tiers["full_spectral_heat_kernel_remainder_bound"] == "OPEN",
        "conditional IR boundary was lost",
    )
    require(
        tiers["bare_spectral_vacuum_small_or_cancelled"] == "CLOSED_NO"
        and tiers["selected_Lambda_eff"] == "OPEN",
        "vacuum obstruction changed",
    )
    require(
        tiers["absolute_Newton_normalization"] == "OPEN_ONE_DIMENSIONFUL_SCALE"
        and tiers["selected_MTT_product_spectral_action"] == "OPEN",
        "action or scale was overpromoted",
    )
    require(
        not guards["claims_A53_point_measure_unconditionally_selected"]
        and not guards["claims_asymptotic_spectral_remainder_controlled"]
        and not guards["claims_observed_Newton_constant_derived"]
        and not guards["claims_cosmological_constant_solved"],
        "epistemic guard failed",
    )
    for phrase in [
        "Exact Einstein/Weyl crossover",
        "beta^2/Lambda^2 = 20/(3 tau_int)",
        "Vacuum obstruction",
        "does not yet bound all omitted higher heat-kernel terms",
    ]:
        require(phrase.lower() in normalized_note, f"note missing: {phrase}")

    print(
        "AUDIT_PASS: conditional spectral Einstein/Weyl IR ratio closed; "
        "full remainder, action selection, Newton scale, and Lambda_eff remain open"
    )


if __name__ == "__main__":
    main()
