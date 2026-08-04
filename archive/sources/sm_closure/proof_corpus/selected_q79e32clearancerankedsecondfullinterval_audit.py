from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from q79_y_chart_conservative_extension import compatible_source_hash


SLUG = "selected_q79e32clearancerankedsecondfullinterval"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
LEGACY_D047_TAIL_SHA256 = "34195caa0a17c11dbe19f80a3b48491063c9c8e9762d810d79c4e08b43b01d37"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(left: float, right: float, tolerance: float = 1.0e-15) -> bool:
    return abs(left - right) <= tolerance * max(1.0, abs(left), abs(right))


def compatible_d047_tail_refinement(path: Path, expected: str) -> bool:
    if path.name != "d047_selected_058.E32_tail.interval.packet.json":
        return False
    if expected != LEGACY_D047_TAIL_SHA256:
        return False
    main_path = path.with_name("d047_selected_058.E32_main.interval.packet.json")
    archived_main_path = path.with_name(
        "d047_selected_058.E32_main.pre_tail_refinement.interval.packet.json"
    )
    if not main_path.exists() or not archived_main_path.exists():
        return False
    tail = load(path)
    main = load(main_path)
    archived_main = load(archived_main_path)
    return bool(
        tail["scope"]["endpoint_tail_interval_closed"]
        and len(tail["regular_segments"]) == 768
        and float(tail["E32_endpoint_tail"]["interval_radius_upper"])
        < 3.3274612007971886e-6
        and main["scope"]["refined_endpoint_tail_cutoff_payload_contained"]
        and main["scope"]["refined_tail_main_transport_reuse_promoted"]
        and main["refined_tail_reuse_promotion"]["all_refined_cutoff_balls_contained"]
        and main["authority"]["certified_tail_cutoff_period_source_sha256"]
        == sha256(path)
        and main["authority"]["pre_refinement_main_source_sha256"]
        == sha256(archived_main_path)
        and archived_main["authority"]["certified_tail_cutoff_period_source_sha256"]
        == expected
    )


def verify_authority(rows: list[dict]) -> None:
    for row in rows:
        path = ROOT / row["path"]
        require(path.exists(), f"missing authority {path}")
        require(
            compatible_source_hash(path, row["sha256"])
            or compatible_d047_tail_refinement(path, row["sha256"]),
            f"authority hash {path}",
        )


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    require(
        certificate["candidate_sha256"] == sha256(CANDIDATE),
        "candidate certificate hash",
    )
    packet_path = ROOT / candidate["packet"]
    frontier_path = ROOT / candidate["frontier"]
    note_path = ROOT / candidate["note"]
    require(candidate["packet_sha256"] == sha256(packet_path), "packet hash")
    require(candidate["frontier_sha256"] == sha256(frontier_path), "frontier hash")
    require(candidate["note_sha256"] == sha256(note_path), "note hash")
    packet = load(packet_path)
    frontier = load(frontier_path)
    verify_authority(packet["authority"])
    require(packet["artifact"] == "A137", "artifact id")
    require(
        packet["status"]
        == "SECOND_SELECTED_FULL_E32_THIMBLE_INTERVAL_CLOSED_WEIGHTED_BATCH_OPEN",
        "packet status",
    )

    authority = {row["path"]: ROOT / row["path"] for row in packet["authority"]}
    a134_path = next(
        path
        for name, path in authority.items()
        if name.endswith("selected_alignment_height4_E32_handle_interval_and_thimble_cutset.packet.json")
    )
    d004_path = next(
        path for name, path in authority.items() if name.endswith("d004_selected_009.E32_full.interval.packet.json")
    )
    d061_full_path = next(
        path for name, path in authority.items() if name.endswith("d061_selected_088.E32_full.interval.packet.json")
    )
    d061_main_path = next(
        path for name, path in authority.items() if name.endswith("d061_selected_088.E32_main.interval.packet.json")
    )
    d061_tail_path = next(
        path for name, path in authority.items() if name.endswith("d061_selected_088.E32_tail.interval.packet.json")
    )
    d047_tail_path = next(
        path for name, path in authority.items() if name.endswith("d047_selected_058.E32_tail.interval.packet.json")
    )
    a134 = load(a134_path)
    d004 = load(d004_path)
    d061 = load(d061_full_path)
    d061_main = load(d061_main_path)
    d061_tail = load(d061_tail_path)
    d047_tail = load(d047_tail_path)

    for internal in d061_main["authority"].values():
        if not isinstance(internal, str) or len(internal) != 64:
            continue
    for key, value in d061_main["authority"].items():
        if key.endswith("_sha256"):
            path_key = key.removesuffix("_sha256")
            path = ROOT / d061_main["authority"][path_key]
            require(
                compatible_source_hash(path, value),
                f"d061 main authority {path}",
            )
    verify_authority(d061["authority"])

    coefficients = {
        int(row["distinguished_index"]): int(row["coefficient"])
        for row in a134["selected_E32_decomposition"]["primitive_thimble_chain"]
    }
    require(coefficients[4] == 2, "d004 coefficient")
    require(coefficients[61] == -3, "d061 coefficient")
    require(coefficients[47] == 4, "d047 coefficient")
    fallback = float(
        a134["strict_budget_ledger"]["sufficient_uniform_per_unit_thimble_radius"]
    )
    rows = {int(row["distinguished_index"]): row for row in packet["closed_interval_ledger"]}
    require(set(rows) == {4, 61}, "closed support ids")
    total_cost = 0.0
    for index, full in ((4, d004), (61, d061)):
        radius = float(full["full_E32_thimble"]["interval_radius_upper"])
        displacement = float(
            full["full_E32_thimble"]["floating_candidate_center_difference"]
        )
        expected = abs(coefficients[index]) * (radius + displacement)
        total_cost += expected
        require(close(rows[index]["weighted_radius_plus_displacement_cost"], expected), f"weighted cost d{index:03d}")
        require(radius < fallback, f"fallback d{index:03d}")
        require(full["full_E32_thimble"]["floating_candidate_contained"], f"floating containment d{index:03d}")

    ledger = packet["weighted_budget_ledger"]
    initial = float(
        a134["strict_budget_ledger"]["remaining_weighted_thimble_combination_radius_budget"]
    )
    require(close(ledger["certified_radius_plus_displacement_cost"], total_cost), "total certified cost")
    require(close(ledger["remaining_budget_after_two_intervals"], initial - total_cost), "remaining budget")
    require(ledger["selected_support_closed"] == 2, "support closed")
    require(ledger["selected_support_total"] == 71, "support total")
    require(ledger["selected_l1_closed"] == 5, "L1 closed")
    require(ledger["selected_l1_total"] == 123, "L1 total")
    require(ledger["remaining_support"] == 69, "remaining support")
    require(ledger["remaining_l1_weight"] == 118, "remaining L1")

    homotopy = d061_main["polygonal_homotopy"]
    require(float(homotopy["detour_signed_right_offset"]) == 0.0, "d061 collinear segmentation")
    require(homotopy["relative_homotopy_class_equals_original_radial_path"], "d061 relative homotopy")
    require(homotopy["critical_winding_vector_is_zero"], "critical winding")
    require(homotopy["chart_zero_winding_vector_is_zero"], "chart winding")
    require(homotopy["elliptic_pole_winding_vector_is_zero"], "pole winding")
    require(float(homotopy["other_critical_ball_clearance_lower"]) > 0, "critical clearance")
    require(float(homotopy["selected_y_chart_zero_clearance_lower"]) > 0, "chart clearance")
    require(float(homotopy["elliptic_infinity_clearance_lower"]) > 0, "pole clearance")
    require(len(d061_tail["regular_segments"]) == 384, "d061 tail segment count")
    require(d061_tail["scope"]["endpoint_tail_interval_closed"], "d061 tail closure")
    require(d061_main["scope"]["main_homogeneous_Gauss_Manin_segment_interval_closed"], "d061 main closure")
    require(d061["scope"]["single_full_E32_thimble_interval_closed"], "d061 full closure")
    require(d047_tail["scope"]["endpoint_tail_interval_closed"], "d047 diagnostic tail")
    require(not packet["hard_ray_diagnostic"]["full_main_interval_closed"], "d047 hard main remains open")

    require(frontier["selected_support_closed"] == 2, "frontier support")
    require(frontier["selected_l1_closed"] == 5, "frontier L1")
    require(not packet["scope"]["weighted_71_thimble_interval_closed"], "weighted interval remains open")
    require(not packet["scope"]["fixed_carrier_exact_separation_closed"], "fixed carrier remains open")
    require(not candidate["closure_claimed"], "candidate overclaims closure")
    require(not certificate["closure_claimed"], "certificate overclaims closure")
    print("q79 A137 clearance-ranked second full E32 interval audit: PASS")
    print("closed: d061 exact node/Hensel tail, final-radius main transport, and full splice")
    print("closed: 2/71 support and L1 5/123 inside the weighted budget")
    print("open: d047 hard main, remaining 69 thimbles, z-chart adapter, and weighted sum")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
