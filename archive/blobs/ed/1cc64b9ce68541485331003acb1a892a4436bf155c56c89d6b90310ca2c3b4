from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79alignmenthandlesandglobalsurfacerelation"
OUT = ROOT / "candidate_data" / SLUG
A128 = ROOT / "candidate_data" / "selected_q79alignmentcontinuousrootmonodromypromotion.candidate.json"
A128_PROMOTED = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentcontinuousrootmonodromypromotion"
    / "ninety_promoted_selected_alignment_picard_lefschetz_monodromies.packet.json"
)
A127_OUT = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
FAN = A127_OUT / "selected_alignment_distinguished_radial_fan.interval.packet.json"
HANDLE_PATHS = A127_OUT / "selected_alignment_torus_handle_paths.interval.packet.json"
HANDLE_DIRECTORY = A127_OUT / "selected_alignment_handle_monodromy"
HANDLE_A = HANDLE_DIRECTORY / "handle_A.packet.json"
HANDLE_B = HANDLE_DIRECTORY / "handle_B.packet.json"
ADAPTER_A = A127_OUT / "selected_alignment_meridian_monodromy" / "d091_handle_A.packet.json"
ADAPTER_B = A127_OUT / "selected_alignment_meridian_monodromy" / "d092_handle_B.packet.json"
TUBE_A = A127_OUT / "selected_alignment_continuous_root_tubes" / "d091_handle_A.root_tube_certificate.packet.json"
TUBE_B = A127_OUT / "selected_alignment_continuous_root_tubes" / "d092_handle_B.root_tube_certificate.packet.json"
BRAID_RELATION = A127_OUT / "selected_alignment_interval_braid_and_global_relation.packet.json"
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
HANDLE_PATH_SCRIPT = ROOT / "scripts" / "build_q79_selected_alignment_handle_paths.py"
HANDLE_WORKER = ROOT / "scripts" / "compute_q79_selected_alignment_handle_monodromy.py"
ADAPTER_SCRIPT = ROOT / "scripts" / "build_q79_selected_alignment_handle_tube_adapters.py"
TUBE_CERTIFIER = ROOT / "scripts" / "certify_q79_selected_alignment_single_root_tubes.py"
BRAID_WORKER = ROOT / "scripts" / "certify_q79_selected_alignment_single_pl_braid.py"
BRAID_BATCH_SCRIPT = ROOT / "scripts" / "run_q79_selected_alignment_interval_braid_batch.py"
FACTORIZATION = OUT / "selected_alignment_global_integral_gauss_manin_factorization.packet.json"
FRONTIER = OUT / "U6_frontier_after_A129.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"

STATUS = (
    "MTT_U6_Q79_SELECTED_ALIGNMENT_TWO_HANDLES_AND_GLOBAL_INTEGRAL_H1_"
    "SURFACE_RELATION_CLOSED_ENDPOINT_H2_PRESENTATION_OPEN"
)
NEXT = "MTT_Selected_q79SelectedAlignmentIntegralSurfaceCyclePresentation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def matrix_rows(value: sp.Matrix) -> list[list[int]]:
    return [[int(value[row, column]) for column in range(value.cols)] for row in range(value.rows)]


def primitive_vanishing_cycle(action: sp.Matrix, intersection: sp.Matrix) -> tuple[list[int], int]:
    delta = action - sp.eye(4)
    column = next(
        delta[:, index]
        for index in range(delta.cols)
        if any(delta[row, index] != 0 for row in range(delta.rows))
    )
    divisor = 0
    for value in column:
        divisor = math.gcd(divisor, abs(int(value)))
    vector = sp.Matrix([int(value) // divisor for value in column])
    for value in vector:
        if value != 0:
            if value < 0:
                vector = -vector
            break
    if sp.eye(4) + vector * vector.T * intersection == action:
        sign = 1
    elif sp.eye(4) - vector * vector.T * intersection == action:
        sign = -1
    else:
        raise AssertionError("selected primitive vanishing-cycle replay failed")
    return [int(value) for value in vector], sign


def main() -> int:
    a128 = load(A128)
    promoted = load(A128_PROMOTED)
    fan = load(FAN)
    handle_paths = load(HANDLE_PATHS)
    braid_relation = load(BRAID_RELATION)
    homology = load(HOMOLOGY)["homology_convention"]
    if not a128["checks"]["all_90_selected_PL_monodromies_promoted"]:
        raise AssertionError("A128 selected local promotion is unavailable")
    if not fan["topology"]["ordered_distinguished_cut_system_closed"]:
        raise AssertionError("selected distinguished fan is not closed")
    if handle_paths["status"] != "SELECTED_ALIGNMENT_A_AND_B_TORUS_HANDLE_CARRIERS_CERTIFIED":
        raise AssertionError("selected handle carriers are unavailable")
    if not all(float(value) > 0 for value in handle_paths["minimums"].values()):
        raise AssertionError("selected handle carrier clearance failed")
    if not all(braid_relation["acceptance"].values()):
        raise AssertionError("selected interval braid relation is not promoted")
    if not braid_relation["global_surface_relation"]["exact_integer_matrix_equality"]:
        raise AssertionError("selected global surface relation is not exact")

    intersection = sp.Matrix(homology["intersection_matrix"])
    handle_packets = {"A": load(HANDLE_A), "B": load(HANDLE_B)}
    adapters = {"A": (ADAPTER_A, load(ADAPTER_A)), "B": (ADAPTER_B, load(ADAPTER_B))}
    tube_paths = {"A": TUBE_A, "B": TUBE_B}
    braid_rows = {
        row["root_id"]: row for row in braid_relation["rows"][90:]
    }
    handle_actions: dict[str, sp.Matrix] = {}
    handle_rows: list[dict] = []
    for name in ("A", "B"):
        packet_path = HANDLE_A if name == "A" else HANDLE_B
        packet = handle_packets[name]
        trajectory_path = ROOT / packet["trajectory"]["path"]
        if sha256(trajectory_path) != packet["trajectory"]["sha256"]:
            raise AssertionError(f"selected handle {name} trajectory hash")
        adapter_path, adapter = adapters[name]
        if adapter["authority"]["handle_monodromy_packet_sha256"] != sha256(packet_path):
            raise AssertionError(f"selected handle {name} adapter authority")
        tube_path = tube_paths[name]
        tube = load(tube_path)
        if tube["authority"]["monodromy_packet_sha256"] != sha256(adapter_path):
            raise AssertionError(f"selected handle {name} tube authority")
        if not tube["acceptance"]["promotion_ready"]:
            raise AssertionError(f"selected handle {name} tube promotion")
        braid_row = braid_rows[f"handle_{name}"]
        braid_path = ROOT / braid_row["certificate_path"]
        if sha256(braid_path) != braid_row["certificate_sha256"]:
            raise AssertionError(f"selected handle {name} braid authority")
        braid = load(braid_path)
        if not all(braid["acceptance"].values()):
            raise AssertionError(f"selected handle {name} braid promotion")
        action = sp.Matrix(packet["homology"]["integral_symplectic_matrix"])
        if (
            action.det() != 1
            or action.T * intersection * action != intersection
            or sp.Matrix(braid["certificate"]["integral_symplectic_matrix"]) != action
        ):
            raise AssertionError(f"selected handle {name} matrix")
        handle_actions[name] = action
        handle_rows.append(
            {
                "name": name,
                "integral_symplectic_matrix": matrix_rows(action),
                "endpoint_root_permutation": packet["braid"]["final_root_permutation"],
                "certified_path_segments": tube["certificate"]["segments_certified"],
                "interval_certified_crossings": braid["certificate"]["interval_certified_crossings"],
                "trajectory_path": relative(trajectory_path),
                "trajectory_sha256": sha256(trajectory_path),
                "root_tube_certificate_path": relative(tube_path),
                "root_tube_certificate_sha256": sha256(tube_path),
                "interval_braid_certificate_path": relative(braid_path),
                "interval_braid_certificate_sha256": sha256(braid_path),
                "promotion_accepted": True,
            }
        )

    ordered_product = sp.eye(4)
    factors: list[dict] = []
    for expected_index, row in enumerate(promoted["rows"], 1):
        if int(row["distinguished_index"]) != expected_index:
            raise AssertionError("selected distinguished factor order changed")
        action = sp.Matrix(row["integral_picard_lefschetz_matrix"])
        vector, sign = primitive_vanishing_cycle(action, intersection)
        if sign != 1:
            raise AssertionError("selected positive meridian has negative PL sign")
        ordered_product = action * ordered_product
        factors.append(
            {
                "distinguished_index": expected_index,
                "root_id": row["root_id"],
                "positive_vanishing_cycle_up_to_sign": vector,
                "positive_picard_lefschetz_matrix": matrix_rows(action),
                "certified_path_segments": row["certified_path_segments"],
                "interval_certified_crossings": row["interval_certified_crossings"],
            }
        )

    boundary = (
        handle_actions["B"].inv()
        * handle_actions["A"].inv()
        * handle_actions["B"]
        * handle_actions["A"]
    )
    if ordered_product != boundary:
        raise AssertionError("selected factor product and handle boundary disagree")
    if matrix_rows(ordered_product) != braid_relation["global_surface_relation"][
        "ordered_distinguished_action_product"
    ]:
        raise AssertionError("selected factorization/relation packet disagreement")
    vanishing_rank = sp.Matrix(
        [factor["positive_vanishing_cycle_up_to_sign"] for factor in factors]
    ).rank()
    if vanishing_rank != 4:
        raise AssertionError("selected vanishing cycles do not span H1")

    factorization = {
        "schema": "MTTQ79SelectedAlignmentGlobalIntegralGaussManinFactorization.v1",
        "status": "SELECTED_ALIGNMENT_GLOBAL_INTEGRAL_H1_GAUSS_MANIN_FACTORIZATION_CLOSED",
        "base": {
            "normalized_torus": "C/(Z+iZ)",
            "base_point": "(1+i)/4",
            "fiber_genus": 2,
            "homology_basis": ["a1", "b1", "a2", "b2"],
            "intersection_matrix": homology["intersection_matrix"],
        },
        "distinguished_cut_system": {
            "generator_count": 90,
            "ordering_rule": fan["ordering"]["rule"],
            "ordered_root_ids": fan["ordering"]["root_ids"],
        },
        "factors": factors,
        "handle_actions": {
            "A": matrix_rows(handle_actions["A"]),
            "B": matrix_rows(handle_actions["B"]),
        },
        "handle_promotions": handle_rows,
        "surface_relation": braid_relation["global_surface_relation"],
        "action_convention": braid_relation["action_convention"],
        "exact_checks": {
            "all_90_factors_positive_rank_one_PL_transvections": True,
            "all_90_factors_integral_symplectic": True,
            "both_handle_actions_integral_symplectic": True,
            "vanishing_cycle_span_rank_four": True,
            "ordered_product_equals_handle_boundary": True,
            "global_integral_H1_representation_closed": True,
        },
    }
    dump(FACTORIZATION, factorization)
    frontier = {
        "schema": "MTTU6FrontierAfterA129.v1",
        "status": STATUS,
        "selected_alignment_local_PL_monodromies_promoted": 90,
        "selected_alignment_torus_handle_monodromies_promoted": 2,
        "selected_alignment_ordered_distinguished_cut_system_closed": True,
        "selected_alignment_global_integral_H1_surface_relation_closed": True,
        "selected_alignment_vanishing_cycle_span_rank": vanishing_rank,
        "selected_alignment_integral_H2_basis_columns": 0,
        "selected_alignment_period_columns": 0,
        "integral_period_branch_selected": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        A128,
        A128_PROMOTED,
        FAN,
        HANDLE_PATHS,
        HANDLE_A,
        HANDLE_B,
        ADAPTER_A,
        ADAPTER_B,
        TUBE_A,
        TUBE_B,
        BRAID_RELATION,
        HOMOLOGY,
        HANDLE_PATH_SCRIPT,
        HANDLE_WORKER,
        ADAPTER_SCRIPT,
        TUBE_CERTIFIER,
        BRAID_WORKER,
        BRAID_BATCH_SCRIPT,
        Path(__file__),
        FACTORIZATION,
        FRONTIER,
    ]
    candidate = {
        "schema": "MTTSelectedQ79AlignmentHandlesAndGlobalSurfaceRelation.v1",
        "status": STATUS,
        "proof_artifact": "proof_corpus/MTT_Selected_q79AlignmentHandlesAndGlobalSurfaceRelation_v1.md",
        "authority_hashes": [
            {"path": relative(path), "sha256": sha256(path)} for path in authority_paths
        ],
        "outputs": {
            "global_factorization": relative(FACTORIZATION),
            "frontier": relative(FRONTIER),
        },
        "checks": {
            "both_selected_handle_carriers_certified": True,
            "both_selected_handle_root_tubes_certified": True,
            "both_selected_handle_braids_interval_certified": True,
            "both_selected_handle_monodromies_promoted": True,
            "all_90_selected_positive_PL_factors_promoted": True,
            "ordered_product_equals_handle_boundary_exactly": True,
            "global_integral_H1_representation_closed": True,
            "endpoint_integral_H2_basis_invented": False,
            "observed_SM_target_fitting_used": False,
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "certificate": "MTTSelectedQ79AlignmentHandlesAndGlobalSurfaceRelation",
        "status": STATUS,
        "candidate_sha256": sha256(CANDIDATE),
        "selected_handle_monodromies_promoted": 2,
        "selected_global_integral_H1_surface_relation_closed": True,
        "selected_endpoint_integral_H2_basis_columns": 0,
        "selected_endpoint_period_columns": 0,
        "integral_branch_selected": False,
        "observed_SM_target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    print(f"wrote {CERTIFICATE.relative_to(ROOT)}")
    print("A129: selected A/B handles and exact global integral H1 surface relation closed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
