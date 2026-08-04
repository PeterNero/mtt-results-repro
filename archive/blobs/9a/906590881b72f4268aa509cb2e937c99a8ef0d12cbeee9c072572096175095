from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
PACKET = PERIOD_DIRECTORY / "selected_alignment_E32_hensel_seed_and_first_full_interval.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A136.packet.json"
CANDIDATE = ROOT / "candidate_data" / "selected_q79e32thimblehenselseedandfirstfullinterval.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79e32thimblehenselseedandfirstfullinterval.certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79E32ThimbleHenselSeedAndFirstFullInterval_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def path_from_relative(value: str) -> Path:
    return ROOT / Path(value)


def close(left: float, right: float, tolerance: float = 1.0e-15) -> bool:
    return math.isclose(left, right, rel_tol=tolerance, abs_tol=tolerance)


def main() -> int:
    packet = load(PACKET)
    frontier = load(FRONTIER)
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    if packet["artifact"] != "A136":
        raise AssertionError("A136 artifact label changed")
    if candidate["packet_sha256"] != sha256(PACKET):
        raise AssertionError("A136 packet hash mismatch")
    if candidate["frontier_sha256"] != sha256(FRONTIER):
        raise AssertionError("A136 frontier hash mismatch")
    if candidate["note_sha256"] != sha256(NOTE):
        raise AssertionError("A136 note hash mismatch")
    if certificate["candidate_sha256"] != sha256(CANDIDATE):
        raise AssertionError("A136 candidate hash mismatch")
    for authority in packet["authority"]:
        path = path_from_relative(authority["path"])
        if not path.exists() or sha256(path) != authority["sha256"]:
            raise AssertionError(f"A136 authority mismatch: {authority['path']}")

    selected = packet["selected_first_execution"]
    if selected != {
        "distinguished_index": 4,
        "root_id": "selected_009",
        "height_four_chain_coefficient": 2,
        "line_chart": "y",
        "endpoint_cutoff_epsilon": 1.0e-5,
    }:
        raise AssertionError("A136 selected first execution changed")
    seed = packet["certified_local_seed"]
    if not float(seed["node_parameter_radius_upper"]) < 2.0e-80:
        raise AssertionError("A136 node interval is too wide")
    if not float(seed["double_root_radius_upper"]) < 2.0e-80:
        raise AssertionError("A136 double-root interval is too wide")
    if not float(seed["node_jacobian_absolute_lower"]) > 1.0e6:
        raise AssertionError("A136 transverse node Jacobian lost separation")
    if not float(seed["quartic_at_node_absolute_lower"]) > 100.0:
        raise AssertionError("A136 nodal quadratic/quartic coprimality lost")
    if not float(seed["hensel_jacobian_absolute_lower"]) > 1.0e4:
        raise AssertionError("A136 Hensel Jacobian lost invertibility")
    if not float(seed["factor_disk_residual_upper"]) < 1.0e-70:
        raise AssertionError("A136 factor-disk residual is too large")
    if not float(seed["factor_disk_contraction_upper"]) < 1.0e-60:
        raise AssertionError("A136 factor-disk contraction is not decisive")

    execution = packet["certified_interval_execution"]
    if execution["main_certificate_method"] != (
        "six-dimensional homogeneous augmented fundamental frame"
    ):
        raise AssertionError("A136 main certificate method changed")
    if int(execution["main_accepted_steps"]) != 115:
        raise AssertionError("A136 accepted-step count changed")
    if int(execution["main_rejected_steps"]) != 39:
        raise AssertionError("A136 rejected-step count changed")
    if not float(execution["maximum_accepted_lift_correction"]) < 1.0e-8:
        raise AssertionError("A136 accepted correction cap changed")
    if not close(float(execution["final_E32_radius_envelope"]), 1.0e-5):
        raise AssertionError("A136 global radius envelope changed")
    main_radius = float(execution["main_augmented_frame_radius_upper"])
    tail_radius = float(execution["endpoint_tail_radius_upper"])
    full_radius = float(execution["full_interval_radius_upper"])
    if not main_radius < 5.0e-6:
        raise AssertionError("A136 main interval radius is too large")
    if not tail_radius < 1.0e-5:
        raise AssertionError("A136 endpoint-tail radius is too large")
    if not full_radius < 1.5e-5:
        raise AssertionError("A136 full interval radius is too large")
    if execution["independent_A131_center_contained"] is not True:
        raise AssertionError("A136 independent center containment changed")
    if execution["floating_value_used_as_bound"] is not False:
        raise AssertionError("A136 promotes the floating value to a bound")

    ledger = packet["weighted_budget_ledger"]
    coefficient = int(selected["height_four_chain_coefficient"])
    center_difference = float(execution["independent_A131_center_difference"])
    expected_cost = abs(coefficient) * (full_radius + center_difference)
    if not close(
        float(ledger["certified_radius_plus_center_displacement_cost"]),
        expected_cost,
    ):
        raise AssertionError("A136 weighted budget cost mismatch")
    expected_remaining = float(ledger["A134_initial_remaining_budget"]) - expected_cost
    if not close(float(ledger["remaining_budget_after_first_interval"]), expected_remaining):
        raise AssertionError("A136 remaining weighted budget mismatch")
    if int(ledger["selected_support_closed"]) != 1 or int(ledger["selected_support_total"]) != 71:
        raise AssertionError("A136 selected support count changed")
    if int(ledger["selected_l1_closed"]) != 2 or int(ledger["selected_l1_total"]) != 123:
        raise AssertionError("A136 selected L1 count changed")

    scope = packet["scope"]
    if scope["first_selected_full_E32_thimble_interval_closed"] is not True:
        raise AssertionError("A136 first full interval is not marked closed")
    if scope["weighted_71_thimble_interval_closed"] is not False:
        raise AssertionError("A136 overclaims weighted closure")
    if scope["fixed_carrier_exact_separation_closed"] is not False:
        raise AssertionError("A136 overclaims fixed-carrier separation")
    if scope["observed_SM_values_used"] is not False:
        raise AssertionError("A136 imports observed SM values")
    if frontier["selected_support_closed"] != 1 or frontier["selected_support_total"] != 71:
        raise AssertionError("A136 frontier support count changed")
    if not close(
        float(frontier["remaining_weighted_budget"]),
        float(ledger["remaining_budget_after_first_interval"]),
    ):
        raise AssertionError("A136 frontier budget mismatch")

    print("q79 A136 Hensel seed and first full E32 interval audit: PASS")
    print("closed: exact node, quantitative Hensel disk, and endpoint tail for d004")
    print("closed: six-dimensional augmented main transport and oriented full splice")
    print(f"closed: first full radius {full_radius:.6e} inside A134 fallback")
    print("open: remaining 70 thimbles, weighted interval, and fixed-carrier decision")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
