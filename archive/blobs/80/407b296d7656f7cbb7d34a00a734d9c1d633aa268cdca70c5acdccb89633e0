from __future__ import annotations

from q79_height4_target_refined_full_residue_audit_common import audit_target


def main() -> int:
    summary = audit_target(
        index=62,
        root_id="selected_087",
        coefficient=-1,
        artifact="A229",
    )
    print("q79 A229 d062 refined full-residue interval audit: PASS")
    print(
        "closed: d062 node, eight-row main/tail splice, and coefficient-minus-one "
        f"chain ball; max row radius={summary['maximum_full_radius']:.6e}"
    )
    print("open: exact selected-chain recomposition and interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
