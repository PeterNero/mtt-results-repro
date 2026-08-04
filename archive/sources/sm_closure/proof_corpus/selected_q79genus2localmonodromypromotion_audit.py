from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2localmonodromypromotion"
STATUS = "MTT_U6_Q79_ALL_90_LOCAL_AND_TWO_HANDLE_MONODROMIES_PROMOTED_GLOBAL_RELATION_OPEN"
NEXT = "MTT_Selected_q79GenusTwoDistinguishedCutSystemAndGlobalSurfaceRelation_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79GenusTwoLocalMonodromyPromotion_v1.md"
DATA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localroottrajectoryexecution"
)
TRAJECTORY_BATCH = DATA / "local_trajectory_batch.packet.json"
TUBE_BATCH = DATA / "local_root_tube_batch.packet.json"
BRAID_CERT = DATA / "local_pl_braid_interval_certificate.packet.json"
ZERO_TRANSITION = DATA / "old_to_zero_branch_chart_transition.packet.json"
MINUS_ONE_TRANSITION = DATA / "old_to_minus_one_branch_chart_transition.packet.json"
A113_EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
FALLBACK_ROOT_IDS = {"a34", "a41"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    if os.environ.get("MTT_RECOMPUTE_A115_TRAJECTORIES") == "1":
        subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "run_q79genus2localtrajectorybatch.py"),
                "--jobs",
                "4",
                "--force",
            ],
            cwd=ROOT,
            check=True,
        )
    if os.environ.get("MTT_RECOMPUTE_A115_TUBES") == "1":
        subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "run_q79genus2localtubebatch.py"),
                "--jobs",
                "8",
                "--chunk-size",
                "4000",
                "--force",
            ],
            cwd=ROOT,
            check=True,
        )
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "certify_q79genus2local_pl_braids.py")],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )

    candidate = load(CANDIDATE)
    certificate = load(CERT)
    trajectories = load(TRAJECTORY_BATCH)
    tubes = load(TUBE_BATCH)
    braids = load(BRAID_CERT)
    old_exploration = load(A113_EXPLORATION)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    promoted = outputs["promoted_local_monodromies"]
    generators = outputs["gauss_manin_generators"]
    global_open = outputs["global_relation_open"]
    frontier = outputs["frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(certificate["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash mismatch")
    require(all(candidate["checks"].values()), "candidate check failed")

    require(trajectories["counts"]["trajectory_packets_complete"] == 90, "trajectory count")
    require(trajectories["counts"]["A113_matrix_matches"] == 90, "trajectory matrix matches")
    require(tubes["status"] == "ALL_90_LOCAL_CONTINUOUS_ROOT_TUBES_CLOSED", "tube status")
    require(tubes["counts"]["continuous_root_tube_certificates"] == 90, "tube count")
    require(tubes["counts"]["segments_certified"] == 300428, "tube segment total")
    require(float(tubes["minimums"]["Rouche_relative_margin"]) > 0, "Rouche margin")
    require(float(tubes["minimums"]["pairwise_tube_separation"]) > 0, "tube separation")
    require(braids["status"] == "ALL_90_LOCAL_BRAIDS_AND_SP4Z_ACTIONS_PROMOTED", "braid status")
    require(braids["aggregate"]["promoted_local_matrix_count"] == 90, "braid promotion count")
    require(braids["aggregate"]["interval_certified_crossing_count"] == 2392, "crossing total")
    require(braids["aggregate"]["vanishing_cycle_span_rank"] == 4, "braid span")
    require(float(braids["aggregate"]["minimum_crossing_height_lower"]) > 0, "crossing height")

    intersection = sp.Matrix(
        old_exploration["homology_convention"]["intersection_matrix"]
    )
    identity = sp.eye(4)
    vectors = [
        sp.Matrix(vector)
        for vector in old_exploration["homology_convention"][
            "chain_vectors_for_sigma_1_to_sigma_5"
        ]
    ]
    positive = [identity - vector * vector.T * intersection for vector in vectors]
    negative = [value.inv() for value in positive]
    transitions = {
        False: sp.Matrix(
            load(ZERO_TRANSITION)["homology_marking"][
                "old_to_target_transport_matrix_P"
            ]
        ),
        True: sp.Matrix(
            load(MINUS_ONE_TRANSITION)["homology_marking"][
                "old_to_target_transport_matrix_P"
            ]
        ),
    }
    promoted_rows = {row["root_id"]: row for row in promoted["rows"]}
    old_rows = {row["root_id"]: row for row in old_exploration["monodromies"]}
    tube_rows = {row["root_id"]: row for row in tubes["rows"]}
    vectors_promoted: list[list[int]] = []
    for trajectory_row in trajectories["rows"]:
        root_id = trajectory_row["root_id"]
        packet_path = ROOT / trajectory_row["packet_path"]
        packet = load(packet_path)
        trajectory_path = ROOT / packet["trajectory"]["path"]
        require(sha256(packet_path) == trajectory_row["packet_sha256"], "trajectory packet hash")
        require(sha256(trajectory_path) == trajectory_row["trajectory_sha256"], "trajectory hash")
        action_target = identity
        for generator, sign in packet["braid"]["raw_word"]:
            action_target = (positive if sign == 1 else negative)[generator - 1] * action_target
        transition = transitions[root_id in FALLBACK_ROOT_IDS]
        action_old = transition.inv() * action_target * transition
        expected = sp.Matrix(old_rows[root_id]["homology"]["picard_lefschetz_matrix"])
        require(action_old == expected, f"{root_id} A113 replay mismatch")
        promoted_row = promoted_rows[root_id]
        require(action_old == sp.Matrix(promoted_row["integral_picard_lefschetz_matrix"]), "promoted row mismatch")
        delta = action_old - identity
        require(action_old.T * intersection * action_old == intersection, "nonsymplectic local row")
        require(delta.rank() == 1 and delta * delta == sp.zeros(4), "non-transvection local row")
        tube_row = tube_rows[root_id]
        tube_path = ROOT / tube_row["certificate_path"]
        require(sha256(tube_path) == tube_row["certificate_sha256"], "tube hash")
        tube_certificate = load(tube_path)
        require(tube_certificate["acceptance"]["promotion_ready"], "tube not ready")
        vectors_promoted.append(promoted_row["vanishing_cycle_primitive_up_to_sign"])
    require(sp.Matrix(vectors_promoted).rank() == 4, "promoted span")

    require(promoted["aggregate"]["promoted_local_matrix_count"] == 90, "output local count")
    require(generators["promoted_generators"] == {"local_picard_lefschetz": 90, "torus_handles": 2, "total": 92}, "generator inventory")
    require(not generators["global_surface_relation_checked"], "generator relation invented")
    require(global_open["required"]["ordered_distinguished_cut_system_on_90_punctured_torus"] is None, "cut system invented")
    require(not global_open["required"]["global_surface_relation_checked"], "global relation invented")
    require(global_open["guard"]["beta_C_period_rows_emitted"] == 0, "beta rows invented")
    require(frontier["local_picard_lefschetz_monodromies_promoted"] == 90, "frontier locals")
    require(frontier["torus_handle_monodromies_promoted"] == 2, "frontier handles")
    require(frontier["total_integral_symplectic_actions_promoted"] == 92, "frontier total")
    require(not frontier["global_surface_relation_checked"], "frontier relation")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = ROOT / item["path"]
        require(path.exists(), f"missing authority: {path}")
        require(sha256(path) == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "promotes all 90 local",
        "300428",
        "2392",
        "90/90 integral",
        "90 local plus two",
        "root-id order is not",
        "global rank-four",
        "zero strict MTT source",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A115 q79 genus-two local-monodromy promotion audit: PASS")
    print(f"status={STATUS}")
    print("promoted: 90 local Picard-Lefschetz + 2 torus-handle Sp(4,Z) actions")
    print("open: distinguished cut system, global surface relation, period execution")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
