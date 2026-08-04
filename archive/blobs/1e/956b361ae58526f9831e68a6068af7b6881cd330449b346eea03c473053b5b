from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "same_circle_weight2_bundle_obstruction_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    finite = cert["finite_Z64_result"]
    theorem = cert["theorem"]
    decision = cert["corpus_decision"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more same-circle checks failed")
    require(finite["kernel"] == [0, 32], "weight-two kernel changed")
    require(finite["square_root_character_labels"] == [1, 33], "root pair changed")
    require(finite["root_ratio_character_label"] == 32, "root ratio is not chi_32")
    require(finite["root_ratio_order"] == 2, "root ratio is not order two")
    require(
        "correspondence base Z" in theorem["common_base_typing"]["base"],
        "internal/external comparison is not properly typed",
    )
    require(
        "H^1(Z;Z2)" in theorem["weight2_equivalence"]["equivalent_obstruction"],
        "global Z2 obstruction was not recorded",
    )
    require(
        decision["current_status"]
        == "WEIGHT2_SAME_CIRCLE_REDUCED_TO_Z2_BUNDLE_OBSTRUCTION_ODD_LIFT_SELECTOR_OPEN",
        "same-circle status changed",
    )
    require(
        guards["claims_weight2_data_selects_a_unique_weight1_root"] is False,
        "weight-two data overclaim a root",
    )
    require(
        guards["claims_global_q79_Spin_or_SpinC_closed"] is False,
        "global Spin/SpinC was overclaimed",
    )

    print(
        "AUDIT_PASS: same-circle TT compatibility is reduced to an exact "
        "order-two flat-line obstruction and an odd-weight lift selector"
    )


if __name__ == "__main__":
    main()
