from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "q79_ordinary_exterior_dual_hym_nogo_and_derived_kernel_cutset_certificate.json"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(CERT.read_text(encoding="utf-8"))
    require(all(data["checks"].values()), "an exact matrix/topology check failed")
    require(
        data["claim_tiers"][
            "ordinary_dual_and_exterior_square_preserve_HYM_equations"
        ]
        == "CLOSED_EXACT",
        "ordinary HYM covariance tier changed",
    )
    require(
        data["claim_tiers"]["ordinary_dual_or_exterior_square_realizes_JDE"]
        == "CLOSED_NO_GO",
        "ordinary JDE no-go changed",
    )
    require(
        data["claim_tiers"]["nonzero_c3_branch_is_complex_linearly_self_dual"]
        == "CLOSED_NO_GO",
        "c3 self-duality obstruction changed",
    )
    require(
        data["finite_data"]["reference_c3"] == 6
        and data["finite_data"]["dual_reference_c3"] == -6,
        "chirality exchange changed",
    )
    require(
        data["finite_data"]["derived_kernel_contract_rows_available"] == 2
        and data["finite_data"]["derived_kernel_contract_rows_required"] == 11,
        "derived-kernel cutset count changed",
    )
    require(
        data["claim_tiers"]["nonlocal_same_branch_Fourier_Mukai_JDE_autoequivalence"]
        == "OPEN_EXACT_KERNEL_AND_EXT1_CONTRACT_EMITTED",
        "nonlocal derived exit was overpromoted",
    )
    require(
        not data["guardrails"][
            "claims_derived_equivalence_preserves_the_physical_HYM_metric_automatically"
        ],
        "derived equivalence was mistaken for HYM metric invariance",
    )
    require(
        not data["guardrails"]["claims_opposite_chirality_branch_is_same_selected_branch"],
        "opposite chirality was identified with one selected branch",
    )
    print("Q79_ORDINARY_EXTERIOR_DUAL_HYM_NOGO_DERIVED_KERNEL_CUTSET_AUDIT_PASS")


if __name__ == "__main__":
    main()
