from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    ROOT / "certificates" / "q79_spectral_hym_strain_symbol_bridge_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Spectral_HYM_to_RootStack_Strain_Symbol_Bridge_v1.md"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")

    require(all(certificate["checks"].values()), "one or more finite checks failed")
    require(
        certificate["claim_tiers"][
            "spectral_sheet_symbol_to_q79_rootstack_strain_carrier"
        ]
        == "CLOSED_EXACT",
        "spectral sheet-symbol bridge changed",
    )
    require(
        certificate["claim_tiers"][
            "fiberwise_normalized_overlap_metric_on_strain_symbol"
        ]
        == "CLOSED_EXACT_IDENTITY",
        "fiberwise overlap identity changed",
    )
    require(
        certificate["claim_tiers"][
            "literal_full_inverse_Fourier_Mukai_HYM_connection_identity"
        ]
        == "CLOSED_NO_GO_FOR_NONZERO_CHERN_VISIBLE_REALIZATION",
        "literal HYM/root-stack connection no-go changed",
    )
    require(
        certificate["claim_tiers"]["actual_q79_inverse_Fourier_Mukai_visible_bundle"]
        == "OPEN_GERBE_AND_LOCAL_FREENESS"
        and certificate["claim_tiers"]["actual_q79_balanced_HYM_connection"]
        == "OPEN"
        and certificate["claim_tiers"][
            "dynamic_projected_HYM_Hessian_on_TT_standard_block"
        ]
        == "OPEN_REDUCED_TO_SYMMETRIC_2_BY_2_BLOCK",
        "future Fourier-Mukai/HYM boundary was overpromoted",
    )
    require(
        certificate["finite_data"]["conditional_visible_c2"] == 9
        and certificate["finite_data"]["conditional_underlying_real_p1"] == -18,
        "Chern obstruction data changed",
    )
    require(
        certificate["finite_data"][
            "self_adjoint_S3_equivariant_strain_operator_dimension"
        ]
        == 6
        and certificate["finite_data"][
            "lane_preserving_self_adjoint_operator_dimension"
        ]
        == 4
        and certificate["finite_data"][
            "physical_standard_isotypic_Hessian_block_shape"
        ]
        == [2, 2],
        "projected Hessian cutset changed",
    )
    require(
        certificate["guardrails"][
            "claims_flat_rootstack_connection_equals_nonflat_visible_HYM_connection"
        ]
        is False
        and certificate["guardrails"][
            "claims_shared_central_circle_neutralizes_relative_spectral_phases"
        ]
        is False
        and certificate["guardrails"]["adds_fitted_numeric_parameter"] is False,
        "source or topology guardrail changed",
    )
    for phrase in [
        "finite sheet/Weyl symbol",
        "p1(V_R)=c1(V)^2-2*c2(V)=-2*c2(V)",
        "h_DE=0",
        "h_DD=h_EE>0",
        "not the full inverse Fourier-Mukai visible",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: q79 strain is the exact spectral sheet symbol; literal "
        "nonzero-Chern HYM/flat-rootstack identity is ruled out and the dynamic "
        "TT Hessian is reduced to one symmetric 2x2 block"
    )


if __name__ == "__main__":
    main()
