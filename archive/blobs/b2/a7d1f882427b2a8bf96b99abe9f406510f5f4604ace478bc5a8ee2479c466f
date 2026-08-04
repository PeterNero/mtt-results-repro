from __future__ import annotations

from q79_height4_target_refined_full_residue_audit_common import audit_target


def main() -> int:
    summary = audit_target(
        index=41,
        root_id="selected_090",
        coefficient=-1,
        artifact="A227",
    )
    print("q79 A227 d041 refined full-residue interval audit: PASS")
    print(
        "closed: d041 node, eight-row main/tail splice, and coefficient-minus-one "
        f"chain ball; max row radius={summary['maximum_full_radius']:.6e}"
    )
    print("open: d030, d062, selected-chain recomposition, and interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
