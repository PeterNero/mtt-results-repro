from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "q79_signed_sheet_w2_branch_divisor_reduction_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    finite = cert["finite_data"]
    universal = cert["universal_w2_theorem"]
    branch = cert["branch_divisor_theorem"]
    complement = cert["complement_decision"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more w2/branch checks failed")
    require(
        finite["signed_transposition_eigenvalues"] == [-1, -1, 1],
        "signed transposition restriction changed",
    )
    require(universal["result"] == "w2(E_rho_plus)=a cup a", "w2 formula changed")
    require(branch["branch_class"] == "[B]=6H", "q79 branch class changed")
    require(finite["branch_lattice_divisibility"] == 6, "branch divisibility changed")
    require(finite["Z6_to_Z4_odd_lift_images"] == [], "an impossible Z4 lift appeared")
    require(
        complement["status"]
        == "STRICT_SPIN_NOGO_CONDITIONAL_ON_SELECTED_BRANCH_COMPLEMENT_H1_Z6",
        "conditional Spin decision changed",
    )
    require(
        tiers["selected_q79_branch_complement_H1_is_Z6"] == "OPEN_ONE_GEOMETRIC_CHECK",
        "branch complement was silently promoted",
    )
    require(
        guards["claims_strict_q79_Spin_no_go_unconditional"] is False,
        "strict Spin no-go was overclaimed",
    )
    require(
        guards["claims_SpinC_follows_from_nonzero_w2"] is False,
        "SpinC was inferred without a determinant line",
    )

    print(
        "AUDIT_PASS: universal w2=a^2 and q79 branch class 6H are closed; "
        "the strict-Spin no-go retains its one explicit complement hypothesis"
    )


if __name__ == "__main__":
    main()
