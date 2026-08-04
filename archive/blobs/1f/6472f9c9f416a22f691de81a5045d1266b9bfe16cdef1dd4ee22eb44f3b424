from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    ROOT
    / "certificates"
    / "q79_finite_rootstack_reynolds_tt_hessian_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Finite_RootStack_Reynolds_TT_Hessian_and_Direct_Operator_Exit_v1.md"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    tiers = certificate["claim_tiers"]
    finite = certificate["finite_data"]
    guards = certificate["guardrails"]

    require(all(certificate["checks"].values()), "one or more exact checks failed")
    require(
        tiers["normalized_S3_Haar_trace"] == "CLOSED_EXACT_UNIQUE"
        and tiers["finite_rootstack_projected_Hessian"] == "CLOSED_EXACT",
        "finite source theorem was weakened",
    )
    require(
        finite["normalized_hessian_spectrum"] == {"0": 2, "1": 4}
        and finite["normalized_hessian_rank"] == 4,
        "finite Hessian spectrum changed",
    )
    require(
        finite["TT_multiplicity_block"] == [["1", "0"], ["0", "1"]],
        "projected TT block is not identity",
    )
    require(
        finite["dimensionless_fitted_parameters"] == 0
        and finite["overall_action_normalizations"] == 1,
        "parameter ledger changed",
    )
    require(
        tiers["actual_q79_balanced_continuum_HYM_Hessian"] == "OPEN"
        and guards["claims_actual_continuum_HYM_Hessian_computed"] is False,
        "continuum HYM was overpromoted",
    )
    require(
        tiers["rank2_row_model_directly_equals_rank3_q79_spectral_bundle"]
        == "CLOSED_NO_GO_TYPE_MISMATCH"
        and guards["claims_rank2_HYM_row_model_is_rank3_spectral_bundle"] is False,
        "rank-2/rank-3 type guard changed",
    )
    for phrase in [
        "P_Haar = (1/6) sum_{g in S3} rho(g)",
        "H_fin = kappa_fin (I-P_Haar)",
        "H_std = kappa_fin I2",
        "h_DE = 0",
        "old `2/11` Fourier-Mukai count therefore remains correct",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: normalized S3 Haar mismatch emits the exact finite q79 "
        "TT Hessian block I2 with zero dimensionless fits; continuum HYM remains separate"
    )


if __name__ == "__main__":
    main()
