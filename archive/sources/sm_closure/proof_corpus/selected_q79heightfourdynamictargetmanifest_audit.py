from __future__ import annotations

import hashlib
import json
from pathlib import Path

from q79_height4_target_refined_full_residue_audit_common import audit_target


ROOT = Path(__file__).resolve().parents[1]
PROBE = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
)
VALIDATED = PROBE / "validated_transport"
MANIFEST = VALIDATED / "n3.dynamic_targets.manifest.json"
ADAPTER = ROOT / "scripts" / "certify_q79_height4_dynamic_target_full_residue_interval.py"
A123 = (
    ROOT
    / "candidate_data"
    / "selected_q79projectivelinechartcovarianceandellzerocontinuation"
    / "projective_line_chart_covariance_theorem.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify_authority(rows: dict[str, dict], label: str) -> None:
    for name, row in rows.items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing {label} authority {name}")
        require(sha256(path) == row["sha256"], f"stale {label} authority {name}")


def main() -> int:
    require(MANIFEST.exists(), "missing dynamic target manifest")
    manifest = load(MANIFEST)
    require(
        manifest["schema"] == "MTTQ79HeightFourDynamicTargetManifest.v1",
        "dynamic target manifest schema changed",
    )
    verify_authority(manifest["authority"], "dynamic manifest")
    require(
        manifest["authority"]["dynamic_target_adapter"]["sha256"] == sha256(ADAPTER),
        "dynamic adapter manifest hash changed",
    )
    entries = manifest["targets_in_A219_priority_order"]
    ranks = [int(row["A219_priority_rank"]) for row in entries]
    require(ranks == list(range(16, 16 + len(entries))), "dynamic ranks are not contiguous")
    require(int(manifest["target_count"]) == len(entries), "dynamic manifest count changed")
    for entry in entries:
        index = int(entry["distinguished_index"])
        artifact = entry["artifact"]
        chart = entry["line_chart"]
        pair = [int(value) for value in entry["expected_pair_zero_based"]]
        full_path = ROOT / entry["full_interval_path"]
        require(full_path.exists(), f"missing dynamic full packet d{index:03d}")
        require(
            sha256(full_path) == entry["full_interval_sha256"],
            f"stale dynamic full packet d{index:03d}",
        )
        summary = audit_target(
            index=index,
            root_id=entry["root_id"],
            coefficient=int(entry["signed_coefficient"]),
            artifact=artifact,
            line_chart=chart,
        )
        stem = f"d{index:03d}.n3"
        checkpoint = load(VALIDATED / f"{stem}.main8.refined.checkpoint.json")
        main_packet = load(VALIDATED / f"{stem}.main8.refined.json")
        tail_packet = load(VALIDATED / f"{stem}.tail8.refined.json")
        full = load(full_path)
        require(checkpoint["complete"], f"{artifact} checkpoint incomplete")
        require(
            checkpoint["dynamic_target_adapter_sha256"] == sha256(ADAPTER),
            f"{artifact} checkpoint adapter hash changed",
        )
        require(checkpoint["line_chart"] == chart, f"{artifact} checkpoint chart changed")
        require(
            checkpoint["cutoff_pair_zero_based"] == pair,
            f"{artifact} checkpoint pair changed",
        )
        require(
            float(checkpoint["configuration"]["maximum_integral_radius"]) == 1.0e-4,
            f"{artifact} radius gate changed",
        )
        require(
            main_packet["selected_target"]["near_node_colliding_pair_zero_based"] == pair,
            f"{artifact} main pair changed",
        )
        require(
            tail_packet["selected_target"]["cutoff_pair_zero_based"] == pair,
            f"{artifact} tail pair changed",
        )
        require(
            full["authority"]["dynamic_target_adapter"]["sha256"] == sha256(ADAPTER),
            f"{artifact} full adapter hash changed",
        )
        require(
            full["dynamic_target_adapter"][
                "pair_reselected_by_n3_certified_node_geometry"
            ],
            f"{artifact} lost independent n3 pair reselection",
        )
        require(
            full["strict_scope"][
                "prior_E32_pair_used_only_as_predeclared_consistency_check"
            ],
            f"{artifact} promoted the old pair clue into a bound",
        )
        if chart == "z":
            require(
                checkpoint["A123_sha256"] == sha256(A123),
                f"{artifact} A123 checkpoint hash changed",
            )
            require(
                full["strict_scope"]["A123_projective_z_chart_covariance_consumed"],
                f"{artifact} lost A123 z-chart provenance",
            )
            require(
                full["strict_scope"]["native_z_chart_interval_system_used"],
                f"{artifact} lost native-z interval system",
            )
        require(summary["maximum_full_radius"] < 1.0e-4, f"{artifact} full radius regressed")
    print("q79 dynamic target manifest audit: PASS")
    print(
        f"closed: {len(entries)} contiguous dynamic targets, A219 ranks "
        f"16-{15 + len(entries)}"
    )
    print(f"open target count: {61 - len(entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
