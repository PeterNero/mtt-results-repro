from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2distinguishedcutsystemandglobalrelation"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}_certificate.json"
FAN = ROOT / "candidate_data" / SLUG / "distinguished_radial_fan.packet.json"
FACTORIZATION = (
    ROOT / "candidate_data" / SLUG / "global_integral_gauss_manin_factorization.packet.json"
)
PERIOD_READY = ROOT / "candidate_data" / SLUG / "eight_prym_period_transport.ready.json"
FRONTIER = ROOT / "candidate_data" / SLUG / "U6_frontier_after_A116.packet.json"
EXECUTION = ROOT / "candidate_data" / "selected_q79genus2distinguishedmeridianexecution"
TRAJECTORY_BATCH = EXECUTION / "distinguished_trajectory_batch.packet.json"
TUBE_BATCH = EXECUTION / "distinguished_root_tube_batch.packet.json"
BRAID_RELATION = (
    EXECUTION / "distinguished_pl_braid_and_global_relation_certificate.packet.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_q79GenusTwoDistinguishedCutSystemAndGlobalSurfaceRelation_v1.md"
)
A113_EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
HANDLE_PROMOTION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromypromotion"
    / "two_promoted_torus_handle_monodromies.packet.json"
)
STATUS = "MTT_U6_Q79_GLOBAL_INTEGRAL_GAUSS_MANIN_FACTORIZATION_CLOSED_PERIOD_EXECUTION_OPEN"
NEXT = "MTT_Selected_q79GenusTwoEightPrymPeriodRowsAndIntegralBranch_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "build_selected_q79genus2distinguishedcutsystem.py"),
        ],
        cwd=ROOT,
        check=True,
    )
    recompute_trajectories = os.environ.get("MTT_RECOMPUTE_A116_TRAJECTORIES") == "1"
    recompute_tubes = os.environ.get("MTT_RECOMPUTE_A116_TUBES") == "1"
    trajectory_command = [
        sys.executable,
        str(ROOT / "scripts" / "run_q79genus2distinguishedtrajectorybatch.py"),
        "--jobs",
        "4",
    ]
    if recompute_trajectories:
        trajectory_command.append("--force")
    subprocess.run(trajectory_command, cwd=ROOT, check=True)
    tube_command = [
        sys.executable,
        str(ROOT / "scripts" / "run_q79genus2distinguishedtubebatch.py"),
        "--jobs",
        "8",
    ]
    if recompute_trajectories or recompute_tubes:
        tube_command.append("--force")
    subprocess.run(tube_command, cwd=ROOT, check=True)
    subprocess.run(
        [
            sys.executable,
            str(
                ROOT
                / "scripts"
                / "certify_q79genus2distinguished_pl_braids_and_global_relation.py"
            ),
        ],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            str(
                ROOT
                / "scripts"
                / "build_selected_q79genus2distinguishedcutsystemandglobalrelation.py"
            ),
        ],
        cwd=ROOT,
        check=True,
    )

    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    fan = load(FAN)
    trajectories = load(TRAJECTORY_BATCH)
    tubes = load(TUBE_BATCH)
    braids = load(BRAID_RELATION)
    factorization = load(FACTORIZATION)
    period_ready = load(PERIOD_READY)
    frontier = load(FRONTIER)
    old_exploration = load(A113_EXPLORATION)
    handles = load(HANDLE_PROMOTION)

    require(candidate["status"] == certificate["status"] == STATUS, "status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(certificate["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash mismatch")
    require(all(candidate["checks"].values()), "candidate check failed")

    require(fan["topology"]["ordered_distinguished_cut_system_closed"], "fan topology")
    require(len(fan["distinguished_positive_meridians"]) == 90, "fan count")
    require(len(set(fan["ordering"]["root_ids"])) == 90, "fan ids")
    require(
        [row["root_id"] for row in fan["distinguished_positive_meridians"]]
        == fan["ordering"]["root_ids"],
        "fan ordering",
    )
    require(
        all(float(value) > 0 for value in fan["geometric_certificate"].values()),
        "fan margin",
    )

    require(trajectories["counts"]["trajectory_packets_complete"] == 90, "trajectory count")
    require(trajectories["counts"]["saved_samples_total"] == 229526, "sample total")
    require(tubes["counts"]["continuous_root_tube_certificates"] == 90, "tube count")
    require(tubes["counts"]["segments_certified"] == 229436, "tube segment total")
    require(float(tubes["minimums"]["Rouche_relative_margin"]) > 0, "Rouche margin")
    require(float(tubes["minimums"]["pairwise_tube_separation"]) > 0, "tube separation")
    require(braids["aggregate"]["promoted_distinguished_matrix_count"] == 90, "promotion count")
    require(braids["aggregate"]["interval_certified_crossing_count"] == 3476, "crossing total")
    require(braids["aggregate"]["vanishing_cycle_span_rank"] == 4, "span rank")
    require(float(braids["aggregate"]["minimum_crossing_height_lower"]) > 0, "crossing height")
    require(all(braids["acceptance"].values()), "braid acceptance")

    intersection = sp.Matrix(
        old_exploration["homology_convention"]["intersection_matrix"]
    )
    identity = sp.eye(4)
    product = identity
    vectors: list[list[int]] = []
    for expected_index, row in enumerate(braids["rows"], 1):
        require(row["distinguished_index"] == expected_index, "factor order")
        require(row["promotion_accepted"], "factor not promoted")
        require(row["picard_lefschetz_twist_sign"] == 1, "negative factor")
        action = sp.Matrix(row["promoted_integral_symplectic_matrix_A114_marking"])
        vector = sp.Matrix(row["vanishing_cycle_primitive_up_to_sign"])
        delta = action - identity
        require(action.T * intersection * action == intersection, "nonsymplectic factor")
        require(action.det() == 1, "factor determinant")
        require(delta.rank() == 1 and delta * delta == sp.zeros(4), "non-PL factor")
        require(action == identity + vector * vector.T * intersection, "PL replay")
        product = action * product
        vectors.append([int(value) for value in vector])
    require(sp.Matrix(vectors).rank() == 4, "vanishing span")

    handle_rows = {row["name"]: row for row in handles["handles"]}
    handle_a = sp.Matrix(handle_rows["A"]["integral_symplectic_matrix"])
    handle_b = sp.Matrix(handle_rows["B"]["integral_symplectic_matrix"])
    boundary = handle_b.inv() * handle_a.inv() * handle_b * handle_a
    require(product == boundary, "surface relation")
    require(
        braids["global_surface_relation"]["exact_integer_matrix_equality"],
        "relation flag",
    )
    require(
        sp.Matrix(
            braids["global_surface_relation"]["ordered_distinguished_action_product"]
        )
        == boundary,
        "relation payload",
    )
    require(
        factorization["exact_checks"]["global_integral_H1_representation_closed"],
        "factorization closure",
    )
    require(len(factorization["factors"]) == 90, "factorization rows")
    require(period_ready["next_execution"]["additive_period_table_shape"] == [8, 92], "period shape")
    require(period_ready["not_yet_emitted"]["numerical_period_entries"] == 0, "periods invented")
    require(frontier["ordered_distinguished_cut_system_closed"], "frontier cut system")
    require(frontier["global_integral_H1_surface_relation_closed"], "frontier relation")
    require(frontier["beta_C_period_rows_emitted"] == 0, "beta rows invented")
    require(not frontier["integral_period_branch_selected"], "branch invented")
    require(not frontier["gerbe_zero_or_no_go_executed"], "gerbe result invented")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = ROOT / item["path"]
        require(path.exists(), f"missing authority: {path}")
        require(sha256(path) == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "ordered distinguished cut system",
        "229,436 path segments",
        "3,476",
        "M_90 ... M_2 M_1 = B^-1 A^-1 B A",
        "does not select the A109 marked K3",
        "8x92",
    ):
        require(phrase in note, f"note missing phrase: {phrase}")

    print("A116 q79 distinguished-cut/global-relation audit: PASS")
    print(f"status={STATUS}")
    print("closed: ordered 90-meridian fan and global integral H1 Gauss-Manin relation")
    print("open: 8x92 Prym periods, integral branch, covariant gerbe zero/no-go")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
