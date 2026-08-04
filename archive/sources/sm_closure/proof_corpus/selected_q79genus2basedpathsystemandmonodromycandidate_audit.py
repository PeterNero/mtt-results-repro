from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2basedpathsystemandmonodromycandidate"
STATUS = "MTT_U6_Q79_92_BASED_MONODROMY_PATH_CARRIERS_CLOSED_90_SP4Z_CANDIDATES_UNPROMOTED"
NEXT = "MTT_Selected_q79GenusTwoValidatedBraidTubeAndGlobalMonodromyExecution_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79GenusTwoBasedPathSystemAndMonodromyCandidate_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def as_complex(packet: dict[str, str]) -> complex:
    return complex(float(packet["real"]), float(packet["imaginary"]))


def torus_distance(left: complex, right: complex) -> float:
    return min(
        abs(left - (right + horizontal + 1j * vertical))
        for horizontal in (-1, 0, 1)
        for vertical in (-1, 0, 1)
    )


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )
    candidate = load(CANDIDATE)
    certificate = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    balls = outputs["critical_balls"]
    paths = outputs["based_paths"]
    monodromy = outputs["monodromy_candidates"]
    global_open = outputs["global_open"]
    frontier = outputs["frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(certificate["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(
        hashlib.sha256(CANDIDATE.read_bytes()).hexdigest()
        == certificate["candidate_sha256"],
        "candidate hash mismatch",
    )
    require(all(candidate["checks"].values()), "candidate check failed")

    critical = balls["critical_points"]
    require(len(critical) == balls["critical_point_count"] == 90, "critical ball count")
    centers = [as_complex(row["w_ball_mod_Z_plus_iZ"]["center"]) for row in critical]
    radii = [float(row["w_ball_mod_Z_plus_iZ"]["radius_upper"]) for row in critical]
    minimum_lower = min(
        torus_distance(centers[left], centers[right]) - radii[left] - radii[right]
        for left in range(90)
        for right in range(left)
    )
    require(minimum_lower > 0, "torus critical balls overlap")
    require(
        abs(minimum_lower - float(balls["minimum_pairwise_torus_ball_separation_lower"]))
        < 1e-13,
        "pairwise lower bound mismatch",
    )
    require(max(radii) < 1e-12, "critical w enclosure unexpectedly broad")
    require(
        all(float(row["w_ball_mod_Z_plus_iZ"]["elliptic_cubic_absolute_lower"]) > 0 for row in critical),
        "elliptic inverse branch lower bound",
    )

    meridians = paths["positive_based_meridians"]
    handles = paths["torus_handle_paths"]
    require(len(meridians) == 90, "meridian count")
    require(len(handles) == 2, "handle count")
    require(paths["counts"] == {"critical_meridians": 90, "torus_handles": 2, "total_based_loops": 92}, "path totals")
    for index, row in enumerate(meridians):
        require(row["root_id"] == critical[index]["root_id"], "meridian ordering")
        require(float(row["outbound_segment"]["critical_ball_clearance_lower"]) > 0, "outbound puncture clearance")
        require(float(row["outbound_segment"]["elliptic_infinity_clearance_lower"]) > 0, "outbound pole clearance")
        circle = row["positive_meridian"]
        require(circle["orientation"] == "counterclockwise", "meridian orientation")
        require(circle["target_winding_number"] == 1, "meridian winding")
        require(float(circle["target_enclosure_margin_lower"]) > 0, "target not enclosed")
        require(float(circle["other_critical_ball_clearance_lower"]) > 0, "other puncture on circle")
        require(float(circle["elliptic_infinity_clearance_lower"]) > 0, "pole on circle")
    require([row["name"] for row in handles] == ["A", "B"], "handle names")
    require(all(float(row["critical_ball_clearance_lower"]) > 0 for row in handles), "handle puncture clearance")
    require(all(float(row["elliptic_infinity_clearance_lower"]) > 0 for row in handles), "handle pole clearance")
    require(not paths["topology_guard"]["ordered_distinguished_cut_system_closed"], "global cut system invented")

    rows = monodromy["candidate_rows"]
    require(len(rows) == 90, "monodromy candidate count")
    intersection = sp.Matrix(monodromy["intersection_matrix"])
    identity = sp.eye(4)
    vectors: list[list[int]] = []
    for index, row in enumerate(rows):
        require(row["root_id"] == meridians[index]["root_id"], "matrix ordering")
        value = sp.Matrix(row["picard_lefschetz_matrix_candidate"])
        delta = value - identity
        require(value.T * intersection * value == intersection, "candidate nonsymplectic")
        require(delta.rank() == 1, "candidate rank")
        require(delta * delta == sp.zeros(4), "candidate unipotence")
        require(not row["promotion_accepted"], "candidate silently promoted")
        require(row["exact_algebraic_checks"]["raw_word_replays_matrix"], "word replay missing")
        permutation = row["root_permutation"]
        moved = [position for position, target in enumerate(permutation) if position != target]
        require(len(moved) == 2, "permutation not transposition")
        require(permutation[moved[0]] == moved[1] and permutation[moved[1]] == moved[0], "transposition mismatch")
        vectors.append(row["vanishing_cycle_candidate_up_to_sign"])
    require(sp.Matrix(vectors).rank() == 4, "candidate vanishing span")
    require(monodromy["aggregate"]["promoted_integral_monodromy_matrices"] == 0, "matrices overpromoted")
    require(not monodromy["promotion_guard"]["continuous_disjoint_root_tubes_certified"], "root tubes invented")
    require(not monodromy["promotion_guard"]["torus_handle_monodromies_computed"], "handle matrices invented")
    require(not monodromy["promotion_guard"]["global_surface_relation_checked"], "global relation invented")

    require(all(value is None for value in global_open["required"].values()), "global open field invented")
    require(not global_open["acceptance"]["promote_90_candidate_matrices"], "global promotion invented")
    require(global_open["acceptance"]["beta_C_period_rows_emitted"] == 0, "beta rows invented")
    require(frontier["critical_meridian_path_carriers_closed"] == 90, "frontier meridians")
    require(frontier["torus_handle_path_carriers_closed"] == 2, "frontier handles")
    require(frontier["integral_monodromy_candidates_computed"] == 90, "frontier candidates")
    require(frontier["integral_monodromy_matrices_promoted"] == 0, "frontier promotion")
    require(frontier["candidate_vanishing_cycle_span_rank"] == 4, "frontier span")
    require(frontier["beta_C_period_rows_emitted"] == 0, "frontier beta")
    require(frontier["strict_MTT_source_moduli_removed"] == 0, "source moduli removed")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "92 path carriers",
        "integral `Sp(4,Z)` matrices",
        "consistency evidence",
        "Rouche tube currently proves",
        "handle monodromies",
        "zero strict MTT source moduli",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A113 q79 based-path and monodromy-candidate audit: PASS")
    print(f"status={STATUS}")
    print("paths: 90 positive puncture meridians + 2 torus handles certified")
    print("diagnostic: 90/90 integral Sp4Z transvection candidates, rank-4 vanishing span")
    print("promotion: 0/90 until continuous root tubes, A/B matrices and global relation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
