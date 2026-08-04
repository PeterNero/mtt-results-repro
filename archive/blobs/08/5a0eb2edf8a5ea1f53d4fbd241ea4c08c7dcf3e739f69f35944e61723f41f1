from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HESSIAN = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "hessian"
)
MAIN = HESSIAN / "d074.mainH.interval.json"
TAIL = HESSIAN / "d074.tailH.interval.json"
FULL = HESSIAN / "d074.fullH.interval.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def audit_authorities(packet: dict, label: str) -> None:
    require(bool(packet.get("authority")), f"{label} authority is empty")
    for name, row in packet["authority"].items():
        path = ROOT / row.get("path", "")
        require(path.is_file(), f"{label} authority is absent: {name}")
        require(
            sha256(path) == row.get("sha256"),
            f"{label} authority is stale: {name}",
        )


def main() -> int:
    main_packet = load(MAIN)
    tail_packet = load(TAIL)
    full_packet = load(FULL)
    budget = 0.6 / 76
    half = budget / 2
    main_radius = float(
        main_packet["summary"]["main_Hessian_product_box_frobenius_radius_upper"]
    )
    tail_radius = float(
        tail_packet["summary"]["tail_Hessian_product_box_frobenius_radius_upper"]
    )
    full_radius = float(
        full_packet["summary"]["full_Hessian_product_box_frobenius_radius_upper"]
    )
    require(
        all(math.isfinite(value) for value in (main_radius, tail_radius, full_radius)),
        "nonfinite radius",
    )
    require(main_radius > half, "d074 no longer witnesses an asymmetric allocation")
    require(tail_radius <= half, "d074 tail exceeds its diagnostic half budget")
    require(full_radius <= budget, "d074 full radius exceeds the controlling budget")
    require(
        full_radius <= main_radius + tail_radius + 1.0e-15,
        "spliced Frobenius radius violates the component triangle bound",
    )
    authority = full_packet["authority"]
    require(
        authority["A380_main_Hessian"]["sha256"] == sha256(MAIN),
        "full/main hash mismatch",
    )
    require(
        authority["A381_tail_Hessian"]["sha256"] == sha256(TAIL),
        "full/tail hash mismatch",
    )
    require(
        full_packet["strict_scope"]["target_full_Hessian_interval_closed"] is True,
        "d074 full interval is not closed",
    )
    for packet, label in (
        (main_packet, "d074 main"),
        (tail_packet, "d074 tail"),
        (full_packet, "d074 full"),
    ):
        require(
            packet["strict_scope"]["observed_SM_values_used"] is False,
            f"{label} used observed values",
        )
        audit_authorities(packet, label)
    print(
        "PASS: d074 certifies the asymmetric component-budget lemma; "
        f"main={main_radius:.12g} tail={tail_radius:.12g} "
        f"full={full_radius:.12g} budget={budget:.12g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
