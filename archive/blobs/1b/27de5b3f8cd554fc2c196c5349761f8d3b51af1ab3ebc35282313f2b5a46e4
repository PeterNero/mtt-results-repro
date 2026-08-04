from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2handlemonodromypromotion"
STATUS = "MTT_U6_Q79_TWO_TORUS_HANDLE_MONODROMIES_PROMOTED_90_LOCAL_AND_GLOBAL_RELATION_OPEN"
NEXT = "MTT_Selected_q79GenusTwoLocalRootTubeAndDistinguishedCutSystemExecution_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79GenusTwoHandleMonodromyPromotion_v1.md"
EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_monodromy_exploration.packet.json"
)
TUBES = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_continuous_root_tube_certificate.packet.json"
)
BRAIDS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_pl_braid_interval_certificate.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    if os.environ.get("MTT_RECOMPUTE_A114_TUBES") == "1":
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "certify_q79genus2handle_root_tubes.py")],
            cwd=ROOT,
            check=True,
        )
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "certify_q79genus2handle_pl_braids.py")],
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
    exploration = load(EXPLORATION)
    tubes = load(TUBES)
    braids = load(BRAIDS)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    promoted = outputs["promoted_handles"]
    open_payload = outputs["local_and_global_open"]
    frontier = outputs["frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(certificate["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash mismatch")
    require(all(candidate["checks"].values()), "candidate check failed")

    require(tubes["status"] == "TWO_HANDLE_CONTINUOUS_ROOT_TUBES_CLOSED", "tube status")
    require(all(tubes["acceptance"].values()), "tube acceptance")
    require(len(tubes["handles"]) == 2, "tube handle count")
    require(sum(row["segments_certified"] for row in tubes["handles"]) == 11932, "tube segment total")
    require(all(row["complete"] for row in tubes["handles"]), "incomplete tube path")
    require(all(float(row["minimum_Rouche_relative_margin"]) > 0 for row in tubes["handles"]), "Rouche margin")
    require(all(float(row["minimum_pairwise_tube_separation"]) > 0 for row in tubes["handles"]), "tube separation")
    require(max(row["maximum_certificate_subdivision_depth"] for row in tubes["handles"]) <= 3, "unexpected tube subdivision")

    require(braids["status"] == "TWO_HANDLE_BRAIDS_AND_SP4Z_ACTIONS_PROMOTED", "braid status")
    require(braids["aggregate"]["promoted_handle_count"] == 2, "braid promotion count")
    require(sum(row["crossing_count"] for row in braids["handles"]) == 74, "crossing total")
    require(all(row["promotion_accepted"] for row in braids["handles"]), "braid promotion")
    require(all(float(row["minimum_crossing_height_lower"]) > 0 for row in braids["handles"]), "crossing height")
    require(all(float(row["minimum_projected_endpoint_pair_difference_lower"]) > 0 for row in braids["handles"]), "endpoint order")

    intersection = sp.Matrix(exploration["homology"]["intersection_matrix"])
    identity = sp.eye(4)
    vectors = [sp.Matrix(row) for row in exploration["homology"]["chain_vectors"]]
    positive = [identity - vector * vector.T * intersection for vector in vectors]
    negative = [value.inv() for value in positive]
    replayed: dict[str, sp.Matrix] = {}
    for braid_row, promoted_row, exploration_row in zip(
        braids["handles"], promoted["handles"], exploration["handles"]
    ):
        require(
            braid_row["name"] == promoted_row["name"] == exploration_row["name"],
            "handle ordering",
        )
        require(braid_row["raw_braid_word"] == exploration_row["raw_braid_word"], "word mismatch")
        action = identity
        for generator, sign in braid_row["raw_braid_word"]:
            action = (positive if sign == 1 else negative)[generator - 1] * action
        require(action == sp.Matrix(promoted_row["integral_symplectic_matrix"]), "promoted matrix replay")
        require(action == sp.Matrix(braid_row["promoted_integral_symplectic_matrix"]), "braid matrix replay")
        require(action.T * intersection * action == intersection, "nonsymplectic action")
        require(action.det() == 1, "determinant mismatch")
        replayed[braid_row["name"]] = action

        trajectory = ROOT / exploration_row["trajectory"]["path"]
        require(sha256(trajectory) == exploration_row["trajectory"]["sha256"], "trajectory hash")
        with np.load(trajectory) as data:
            require(data["roots"].shape == tuple(exploration_row["trajectory"]["arrays"]["roots"]), "trajectory shape")
            require(data["w"].shape == tuple(exploration_row["trajectory"]["arrays"]["w"]), "path shape")

    handle_a = replayed["A"]
    handle_b = replayed["B"]
    commutator = handle_a * handle_b * handle_a.inv() * handle_b.inv()
    require(handle_a * handle_b != handle_b * handle_a, "handle matrices commute")
    require(
        sp.Matrix(promoted["aggregate"]["commutator_A_B_Ainv_Binv"]) == commutator,
        "commutator mismatch",
    )
    require(commutator.T * intersection * commutator == intersection, "commutator nonsymplectic")

    require(open_payload["required"]["continuous_root_tubes_for_90_local_meridians"] == 0, "local tubes invented")
    require(open_payload["required"]["promoted_local_Picard_Lefschetz_matrices"] == 0, "local promotion invented")
    require(open_payload["required"]["ordered_distinguished_cut_system_on_once_based_90_punctured_torus"] is None, "cut system invented")
    require(not open_payload["required"]["global_surface_relation_checked"], "surface relation invented")
    require(open_payload["guard"]["beta_C_period_rows_emitted"] == 0, "beta rows invented")
    require(frontier["torus_handle_monodromies_promoted"] == 2, "frontier handles")
    require(frontier["local_integral_monodromy_matrices_promoted"] == 0, "frontier local promotion")
    require(not frontier["global_surface_relation_checked"], "frontier relation")
    require(frontier["beta_C_period_rows_emitted"] == 0, "frontier beta")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = ROOT / item["path"]
        require(path.exists(), f"missing authority: {path}")
        require(sha256(path) == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "two nonlocal torus-handle actions",
        "11,932",
        "all 74 crossing signs",
        "Birman-Hilden",
        "no longer numerical candidates",
        "does **not** promote the 90 local",
        "distinguished ordered cut system",
        "No MTT source modulus",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A114 q79 genus-two handle-monodromy promotion audit: PASS")
    print(f"status={STATUS}")
    print("promoted: A and B handle monodromies in Sp(4,Z)")
    print("open: 90 local root tubes, distinguished cut system, global relation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
