from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "hessian"
    / "precision.manifest.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def audit_authorities(packet: dict, label: str) -> None:
    authority = packet.get("authority", {})
    require(bool(authority), f"{label} authority is empty")
    for name, row in authority.items():
        path = ROOT / row.get("path", "")
        require(path.is_file(), f"{label} authority is absent: {name}")
        require(sha256(path) == row.get("sha256"), f"{label} authority is stale: {name}")


def main() -> int:
    packet = load(MANIFEST)
    require(
        packet["schema"] == "MTTQ79HeightFourPrecisionHessianQueueManifest.v1",
        "precision-manifest schema changed",
    )
    require(
        packet["status"] == "ALL_76_COEFFICIENT_WEIGHTED_HESSIAN_BUDGETS_CLOSED",
        "precision-manifest execution is incomplete",
    )
    budget = float(packet["budget"]["total_target_chain_and_wall_Frobenius_budget"])
    require(budget == 0.6, "precision total budget changed")
    require(int(packet["budget"]["target_count"]) == 76, "precision target count changed")
    require(int(packet["budget"]["wall_index"]) == 65, "precision wall index changed")
    require(int(packet["budget"]["wall_extra_weight"]) == 3, "precision wall weight changed")
    require(
        packet["budget"]["component_split_rule"]
        == (
            "main/tail half budgets are sufficient diagnostics only; the certified "
            "spliced full product-box Frobenius radius is the necessary acceptance gate"
        ),
        "precision component split theorem changed",
    )

    rows = packet["targets"]
    require(len(rows) == 76, "precision target inventory is not 76")
    require(
        [int(row["A219_profile_priority_rank"]) for row in rows] == list(range(1, 77)),
        "precision rank order changed",
    )
    require(
        len({int(row["distinguished_index"]) for row in rows}) == 76,
        "precision target inventory repeats an index",
    )
    contribution_sum = 0.0
    for row in rows:
        index = int(row["distinguished_index"])
        coefficient = int(row["signed_chain_coefficient"])
        expected_weight = abs(coefficient) + (3 if index == 65 else 0)
        require(
            int(row["effective_absolute_weight_including_wall"]) == expected_weight,
            f"precision effective weight changed for d{index:03d}",
        )
        expected_budget = budget / (76 * expected_weight)
        recorded_budget = float(row["full_Frobenius_radius_budget"])
        require(
            abs(recorded_budget - expected_budget) <= 1.0e-18,
            f"precision budget changed for d{index:03d}",
        )
        require(
            row["main_certificate_current"] is True,
            f"d{index:03d} main certificate is absent or stale",
        )
        require(
            row["tail_certificate_current"] is True,
            f"d{index:03d} tail certificate is absent or stale",
        )
        require(row["full_budget_pass"] is True, f"d{index:03d} full packet is over budget")
        for part in ("main", "tail", "full"):
            path = ROOT / row[f"{part}_path"]
            require(path.is_file(), f"d{index:03d} {part} packet is absent")
            require(
                sha256(path) == row[f"{part}_sha256"],
                f"d{index:03d} {part} packet hash is stale",
            )
            audit_authorities(load(path), f"d{index:03d} {part}")
        radius = float(row["full_Frobenius_radius"])
        require(math.isfinite(radius) and radius >= 0.0, f"d{index:03d} radius is invalid")
        require(radius <= recorded_budget, f"d{index:03d} radius exceeds its budget")
        contribution_sum += expected_weight * radius

    counts = packet["counts"]
    require(int(counts["main_certificates_current"]) == 76, "main certificate count changed")
    require(int(counts["tail_certificates_current"]) == 76, "tail certificate count changed")
    require(int(counts["full_budget"]) == 76, "full precision count changed")
    require(int(packet["remaining_full_budget_count"]) == 0, "precision remainder is nonzero")
    require(
        contribution_sum <= budget * (1.0 + 1.0e-14),
        "coefficient-weighted target contribution exceeds the global budget",
    )
    scope = packet["strict_scope"]
    for key in (
        "exact_A231_integer_coefficients_used",
        "d065_extra_PL_wall_weight_included",
        "all_76_component_certificates_current",
        "main_tail_half_split_is_diagnostic_not_required",
        "all_76_full_Hessian_budgets_closed",
    ):
        require(scope[key] is True, f"precision strict scope lost {key}")
    require(scope["observed_SM_values_used"] is False, "observed values entered precision execution")
    require(scope["A384_point_Jacobian_nonsingularity_closed"] is False, "precision manifest overclaims A384")
    require(scope["interval_Newton_existence_and_uniqueness_closed"] is False, "precision manifest overclaims interval Newton")
    require(scope["full_SM_closure_proved"] is False, "precision manifest overclaims full SM closure")
    audit_authorities(packet, "precision manifest")
    print(
        "PASS: all 76 target Hessians and nested authorities replay within the "
        f"coefficient-weighted global Frobenius budget; used={contribution_sum:.12g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
