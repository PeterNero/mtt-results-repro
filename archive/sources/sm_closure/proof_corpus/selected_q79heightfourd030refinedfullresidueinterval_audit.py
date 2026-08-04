from __future__ import annotations

from q79_height4_target_refined_full_residue_audit_common import audit_target


def main() -> int:
    summary = audit_target(
        index=30,
        root_id="selected_034",
        coefficient=3,
        artifact="A228",
    )
    print("q79 A228 d030 refined full-residue interval audit: PASS")
    print(
        "closed: deep-pair d030 node, eight-row main/tail splice, and "
        "coefficient-three chain ball; "
        f"max row radius={summary['maximum_full_radius']:.6e}"
    )
    print("open: remaining exact chain, moving handle/beta intervals, and interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
