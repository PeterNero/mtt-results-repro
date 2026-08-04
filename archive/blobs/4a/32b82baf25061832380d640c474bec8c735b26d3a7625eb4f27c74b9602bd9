from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import sys

from flint import acb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_selected_side_beta_defect_transport as validated


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
PACKET = VALIDATED / "n3.common_junction_edge_ledger.a403.json"
A400 = VALIDATED / "n3.relative_chain_identity.a400.json"
A401 = VALIDATED / "n3.lower_b_contour_homotopy.a401.json"
A402S = VALIDATED / "n3.beta_minus_B.source.a402s.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
TARGET_ENGINE = ROOT / "scripts" / "certify_q79_height4_target_full_residue_interval.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ctx.dps = 100
    packet = load(PACKET)
    identity = load(A400)
    roots = load(A401)
    source = load(A402S)
    if packet["artifact"] != "A403" or not packet["theorem"]["proved"]:
        raise AssertionError("A403 theorem packet is not closed")
    for name, path in {
        "A400_relative_chain_identity": A400,
        "A401_complete_critical_value_inventory": A401,
        "A402S_correlated_beta_minus_B_source": A402S,
        "A383_selected_handle_execution": A383,
        "straight_thimble_transport_engine": TARGET_ENGINE,
    }.items():
        if packet["authority"][name]["sha256"] != sha256(path):
            raise AssertionError(f"stale A403 authority: {name}")

    radius = 1.0 / 5.0
    distances = []
    a401_by_index = {}
    for row in roots["critical_value_certificate"]["nodes"]:
        value = validated.decoded_acb(row["normalized_parameter_ball"])
        distances.append(validated.lower(abs(value)))
        a401_by_index[int(row["distinguished_index"])] = row
    minimum = min(distances)
    clearance = math.nextafter(minimum - radius, -math.inf)
    disk = packet["root_free_junction_disk"]
    if disk["exact_radius"] != "1/5" or clearance <= 0.0:
        raise AssertionError("A403 root-free disk failed")
    if not math.isclose(
        float(disk["critical_value_clearance_from_closed_disk_lower"]),
        clearance,
        rel_tol=2.0e-15,
        abs_tol=0.0,
    ):
        raise AssertionError("A403 disk clearance does not replay")

    chain = [int(value) for value in identity["selected_branch"]["primitive_chain_coordinates_Z98"]]
    expected = {index: value for index, value in enumerate(chain[:90], start=1) if value}
    rows = packet["oriented_edge_ledger"]["selected_thimble_rows"]
    actual = {
        int(row["distinguished_index"]): int(row["signed_chain_coefficient"])
        for row in rows
    }
    if actual != expected or len(rows) != 76:
        raise AssertionError("A403 thimble ledger does not replay A400")
    for index, row in actual.items():
        path = VALIDATED / f"d{index:03d}.n3.node.refined.json"
        label = f"d{index:03d}_certified_node"
        if packet["authority"][label]["sha256"] != sha256(path):
            raise AssertionError(f"stale A403 node authority: d{index:03d}")
        node = load(path)
        parameter = validated.decoded_acb(node["certified_node"]["parameter_ball"])
        source_row = a401_by_index[index]
        shift = source_row["normalizing_lattice_shift"]
        normalized = validated.decoded_acb(source_row["normalized_parameter_ball"])
        if not (parameter + acb(int(shift[0]), int(shift[1]))).overlaps(normalized):
            raise AssertionError(f"A403 node {index} fails torus identification")
        if validated.lower(abs(parameter)) <= radius:
            raise AssertionError(f"A403 node {index} enters the root-free disk")

    handles = packet["oriented_edge_ledger"]["selected_handle_rows"]
    if [int(row["signed_coefficient"]) for row in handles] != chain[90:]:
        raise AssertionError("A403 handle ledger does not replay A400")
    trunk = packet["oriented_edge_ledger"]["shared_trunk"]
    if trunk["aggregate_boundary_coordinates_Z4"] != [0, 0, 0, 0]:
        raise AssertionError("A403 common trunk is not exactly zero")
    if identity["selected_branch"]["A130_boundary_image_Z4"] != [0, 0, 0, 0]:
        raise AssertionError("A400 boundary authority changed")
    if not source["strict_scope"]["beta_minus_B_initial_source_interval_closed"]:
        raise AssertionError("A402S source authority changed")
    scope = packet["strict_scope"]
    if not scope["aggregate_common_trunk_cancellation_proved"]:
        raise AssertionError("A403 trunk theorem flag is false")
    if scope["outer_thimble_and_arc_transports_executed"] or scope["covariant_zero_proved"]:
        raise AssertionError("A403 overclaims numerical execution")
    print(
        "PASS: A403 independently certifies the root-free radius-1/5 junction, "
        "replays all 76 thimbles and eight handles, and verifies the zero trunk"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
