from __future__ import annotations

from q79_height4_target_refined_full_residue_audit_common import audit_target


def main() -> int:
    summary = audit_target(
        index=28,
        root_id="selected_018",
        coefficient=-1,
        artifact="A242",
    )
    print("q79 A242 d028 refined full-residue interval audit: PASS")
    print(
        "closed: d028 node, eight-row main/tail splice, and coefficient-minus-one "
        f"chain ball; max row radius={summary['maximum_full_radius']:.6e}"
    )
    print("open: d015 and 64 successors, moving handle/beta intervals, interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
