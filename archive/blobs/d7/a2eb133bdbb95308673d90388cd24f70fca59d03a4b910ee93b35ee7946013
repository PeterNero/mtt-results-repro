from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
TAIL = DIRECTORY / "d087.n3.tail8.interval.json"
FULL = DIRECTORY / "d087.n3.full8.interval.json"
TAIL_NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD087FullResidueTailInterval_A221_v1.md"
FULL_NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD087FullResidueInterval_A222_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify_authority(rows: dict[str, dict]) -> None:
    for name, row in rows.items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing A221/A222 authority {name}: {path}")
        require(
            sha256(path) == row["sha256"],
            f"stale A221/A222 authority {name}: {path}",
        )


def main() -> int:
    for path in (TAIL, FULL, TAIL_NOTE, FULL_NOTE):
        require(path.exists(), f"missing A221/A222 artifact: {path}")
    tail = load(TAIL)
    full = load(FULL)
    require(
        tail["schema"] == "MTTQ79HeightFourD087FullResidueTailInterval.v1",
        "A221 schema changed",
    )
    require(
        tail["status"]
        == "D087_N3_ALL_EIGHT_NODE_TO_CUTOFF_RESIDUE_TAILS_INTERVAL_CERTIFIED",
        "A221 status changed",
    )
    require(
        full["schema"] == "MTTQ79HeightFourD087FullResidueInterval.v1",
        "A222 schema changed",
    )
    require(
        full["status"] == "D087_N3_FULL_EIGHT_ROW_PERIOD_VECTOR_INTERVAL_CERTIFIED",
        "A222 status changed",
    )
    verify_authority(tail["authority"])
    verify_authority(full["authority"])

    tails = tail["all_eight_endpoint_tails"]
    tail_radii = [float(value) for value in tails["interval_radius_uppers"]]
    require(len(tail_radii) == 8, "A221 does not emit eight tail radii")
    require(
        all(math.isfinite(value) and value > 0.0 for value in tail_radii),
        "A221 carries a nonfinite tail radius",
    )
    require(max(tail_radii) < 3.0e-5, "A221 tail radius regressed above 3e-5")
    require(
        len(tail["regular_segments"]) == 96,
        "A221 geometric partition changed",
    )
    require(
        all(
            row["factor_overlap_with_node_side_neighbor"]
            for row in tail["regular_segments"]
        ),
        "A221 Hensel factor chain lost overlap",
    )
    require(
        tail["strict_scope"]["all_eight_node_to_cutoff_tail_intervals_closed"],
        "A221 all-tail scope reopened",
    )
    require(
        not tail["strict_scope"]["full_d087_period_vector_interval_closed"],
        "A221 incorrectly claims the full splice",
    )

    rows = full["residue_rows"]
    require(len(rows) == 8, "A222 does not emit eight full rows")
    require(
        all(row["floating_value_contained"] for row in rows),
        "A222 floating containment diagnostic failed",
    )
    require(
        all(float(row["containment_margin"]) > 0.0 for row in rows),
        "A222 has a nonpositive containment margin",
    )
    summary = full["summary"]
    require(summary["certified_rows"] == 8, "A222 certified-row count changed")
    require(
        float(summary["maximum_full_interval_radius_upper"]) < 1.0e-3,
        "A222 full-vector radius regressed above 1e-3",
    )
    require(
        float(summary["minimum_floating_containment_margin"]) > 0.0,
        "A222 floating containment margin is not positive",
    )
    scope = full["strict_scope"]
    require(
        scope["full_d087_period_vector_interval_closed"],
        "A222 full d087 vector scope reopened",
    )
    require(
        not scope["floating_values_used_as_bounds"],
        "A222 promoted a floating diagnostic to an error bound",
    )
    require(not scope["covariant_zero_proved"], "A222 overclaims the zero")

    print("q79 A221/A222 d087 full-residue interval audit: PASS")
    print(
        "closed: eight local tails and full d087 vector; "
        f"maximum radius={float(summary['maximum_full_interval_radius_upper']):.6e}"
    )
    print("open: d034, d041, d030, d062 and rank-3 interval recomposition")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
