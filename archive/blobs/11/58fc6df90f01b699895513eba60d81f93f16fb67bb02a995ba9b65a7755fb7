from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "protospinor_odd_weight_lift_selector_dichotomy_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    theorem = cert["theorem"]
    result = cert["corpus_result"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more odd-lift checks failed")
    table = theorem["even_odd_selector_theorem"]["finite_table"]
    require(table["2"]["roots_indistinguishable"] is True, "TT sees the root sign")
    require(table["1"]["root_ratio_label"] == 32, "weight one lost chi_32")
    require(table["3"]["root_ratio_label"] == 32, "odd-weight rule failed")
    require(
        theorem["bundle_lift_statement"]["weight_one_lift_exists_iff"]
        == "D is trivial as a flat unitary line system",
        "bundle root obstruction changed",
    )
    require(theorem["strict_Spin_route"]["current_status"] == "OPEN", "Spin overclaim")
    require(theorem["SpinC_route"]["current_status"] == "OPEN", "SpinC overclaim")
    require(
        result["strongest_current_status"]
        == "EVEN_TT_AMBIGUITY_PROVED_SHARED_Z2_SPIN_SELECTOR_CUTSET_ISOLATED_NO_ROOT_SELECTED",
        "frontier status changed",
    )
    require(
        guards["claims_equal_group_order_proves_same_geometric_object"] is False,
        "order-two objects were conflated",
    )
    require(
        guards["claims_terminal_return_selects_chi1_or_chi33"] is False,
        "terminal parity overclaims a root",
    )

    print(
        "AUDIT_PASS: TT is even-weight blind, the proto-spinor odd-weight selector "
        "cutset is exact, and no unsupported root selection was promoted"
    )


if __name__ == "__main__":
    main()
