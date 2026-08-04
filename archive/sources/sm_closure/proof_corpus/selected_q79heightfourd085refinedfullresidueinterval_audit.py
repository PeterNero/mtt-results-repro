from __future__ import annotations

from q79_height4_target_refined_full_residue_audit_common import audit_target


def main() -> int:
    summary = audit_target(
        index=85,
        root_id="selected_077",
        coefficient=-1,
        artifact="A232",
    )
    print("q79 A232 d085 refined full-residue interval audit: PASS")
    print(
        "closed: d085 node, eight-row main/tail splice, and coefficient-minus-one "
        f"chain ball; max row radius={summary['maximum_full_radius']:.6e}"
    )
    print("open: d082 z-chart transport, remaining chain, and interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
