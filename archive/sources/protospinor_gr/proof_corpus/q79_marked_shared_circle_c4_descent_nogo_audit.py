from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "q79_marked_shared_circle_c4_descent_nogo_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(CERT.read_text(encoding="utf-8"))
    require(all(data["checks"].values()), "a marked-circle descent check failed")
    require(
        data["claim_tiers"]["C4_preserves_the_marked_shared_circle_direction"]
        == "CLOSED_NO_GO",
        "shared-circle marking no-go changed",
    )
    require(
        data["claim_tiers"][
            "autonomous_Lens_descent_in_current_marked_shared_circle_setup"
        ]
        == "CLOSED_NO_GO_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING",
        "marked Lens descent was reopened or overpromoted",
    )
    require(
        data["finite_data"]["quarterturn_Chern_image"] == [0, 1]
        and data["finite_data"]["quarterturn_shared_circle_image"] == [-1, 0],
        "quarter-turn images changed",
    )
    require(
        data["finite_data"]["unoriented_marked_stabilizer_orders"] == [1, 2],
        "marked stabilizer changed",
    )
    require(
        data["finite_data"]["unmarked_modular_exit_contract_rows_available"] == 0
        and data["finite_data"]["unmarked_modular_exit_contract_rows_required"] == 5,
        "unmarked modular contract changed",
    )
    require(
        not data["guardrails"][
            "claims_unmarked_torus_modular_equivalence_preserves_a_marked_shared_circle"
        ],
        "unmarked modular equivalence was confused with marked descent",
    )
    print("Q79_MARKED_SHARED_CIRCLE_C4_DESCENT_NOGO_AUDIT_PASS")


if __name__ == "__main__":
    main()
