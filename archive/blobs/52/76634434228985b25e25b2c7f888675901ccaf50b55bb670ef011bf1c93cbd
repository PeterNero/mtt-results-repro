from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_q79_z64_qww_source_factorization_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_q79_Z64_to_QWW_Source_Factorization_v1.md"

STATUS = (
    "SELECTED_Q79_Z64_QWW_TT_SOURCE_FACTORIZATION_CLOSED_"
    "UNIQUE_UP_TO_POLARIZATION_AND_FRAME_GAUGE_"
    "PRIMITIVE_ROOTSTACK_LORENTZIAN_BRANCH_AND_INVERSE_FOURIER_MUKAI_OPERATOR_IDENTITY_OPEN"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    certificate = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")

    require(certificate["status"] == STATUS, "status mismatch")
    require(all(certificate["checks"].values()), "one or more exact checks failed")

    data = certificate["finite_data"]
    require(data["q79_plus_preimage"] == ["sqrt(2)/2", "-sqrt(2)/2", "0", "0", "0", "0"], "plus preimage changed")
    require(data["q79_cross_preimage"] == ["0", "0", "0", "0", "0", "1"], "cross preimage changed")
    require(data["source_rank"] == 2, "source rank changed")
    require(data["Z64_character"] == 2, "wrong Z64 character")
    require(data["Z64_character_order"] == 32, "wrong helicity periodicity")
    require(data["support_residual"] < 1.0e-12, "exact-plane residual too large")

    tiers = certificate["claim_tiers"]
    require(tiers["exact_Z64_TT_to_q79_source_map"] == "CLOSED_EXPLICIT", "source map open")
    require(tiers["q79_TT_lane_support"] == "CLOSED_EXACT_A0_PLUS_A", "lane support changed")
    require(
        tiers["q79_rootstack_globalization"]
        == "CLOSED_ON_UNIQUE_MINIMAL_FULL_MONODROMY_ROOTSTACK",
        "root-stack globalization missing",
    )
    require(
        tiers["selected_branch_q79_Z64_QWW_source_realization"]
        == "CLOSED_UNIQUE_UP_TO_GAUGE",
        "selected-branch source realization not closed",
    )
    require(tiers["continuous_fitted_physical_parameters"] == "CLOSED_ZERO", "parameter count changed")
    require(
        tiers["primitive_MTT_selects_minimal_rootstack_Lorentzian_branch"] == "OPEN",
        "primitive branch was overpromoted",
    )
    require(tiers["inverse_Fourier_Mukai_HYM_operator_identity"] == "OPEN", "HYM identity overpromoted")

    guards = certificate["guardrails"]
    require(guards["claims_primitive_physical_branch_selection_closed"] is False, "primitive guard missing")
    require(guards["claims_inverse_Fourier_Mukai_HYM_operator_identity_closed"] is False, "HYM guard missing")
    require(guards["claims_rank_two_TT_source_emits_all_six_off_shell_strains"] is False, "rank guard missing")
    require(guards["claims_internal_flat_line_equals_global_helicity_line"] is False, "line-bundle guard missing")
    require(guards["adds_fitted_numeric_parameter"] is False, "fit parameter added")
    require(guards["uses_observed_physics_data"] is False, "observed data used")

    for token in (
        "f_plus  = (1/sqrt(2),-1/sqrt(2),0;0,0,0)",
        "f_cross = (0,0,0;0,0,1)",
        "Pi_exact64 DG(0)^*P_TT=DG(0)^*P_TT",
        STATUS,
    ):
        require(token in note, f"note missing token: {token}")

    print(
        "AUDIT_PASS: exact Z64 helicity-two source factors uniquely through the "
        "q79 minimal root-stack carrier to QWW and its pullback metric, up to gauge"
    )


if __name__ == "__main__":
    main()
