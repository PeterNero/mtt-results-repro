from __future__ import annotations

from q79_height4_target_refined_full_residue_audit_common import audit_target


def main() -> int:
    summary = audit_target(
        index=47,
        root_id="selected_058",
        coefficient=-4,
        artifact="A238",
    )
    print("q79 A238 d047 refined full-residue interval audit: PASS")
    print(
        "closed: d047 node, eight-row main/tail splice, and coefficient-minus-four "
        f"chain ball; max row radius={summary['maximum_full_radius']:.6e}"
    )
    print("open: d079 and 66 successors, moving handle/beta intervals, interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
