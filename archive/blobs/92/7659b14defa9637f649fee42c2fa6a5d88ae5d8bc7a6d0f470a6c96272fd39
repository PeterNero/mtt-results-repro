from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79alignmentcontinuousrootmonodromypromotion"
OUT = ROOT / "candidate_data" / SLUG
A127 = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport.candidate.json"
)
A127_OUT = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
MONODROMY_BATCH = A127_OUT / "selected_alignment_meridian_monodromy_batch.packet.json"
TUBE_BATCH = A127_OUT / "selected_alignment_continuous_root_tube_batch.packet.json"
BRAID_BATCH = A127_OUT / "selected_alignment_interval_braid_and_global_relation.packet.json"
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
WORKER = ROOT / "scripts" / "compute_q79_selected_alignment_single_meridian_monodromy.py"
ROOT_TRANSPORT = ROOT / "scripts" / "q79_selected_alignment_genus2_root_transport.py"
MONODROMY_BATCH_SCRIPT = ROOT / "scripts" / "run_q79_selected_alignment_meridian_monodromy_batch.py"
TUBE_CERTIFIER = ROOT / "scripts" / "certify_q79_selected_alignment_single_root_tubes.py"
TUBE_BATCH_SCRIPT = ROOT / "scripts" / "run_q79_selected_alignment_root_tube_batch.py"
BRAID_WORKER = ROOT / "scripts" / "certify_q79_selected_alignment_single_pl_braid.py"
BRAID_BATCH_SCRIPT = ROOT / "scripts" / "run_q79_selected_alignment_interval_braid_batch.py"
PROMOTED = OUT / "ninety_promoted_selected_alignment_picard_lefschetz_monodromies.packet.json"
FRONTIER = OUT / "U6_frontier_after_A128.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"

STATUS = (
    "MTT_U6_Q79_SELECTED_ALIGNMENT_90_CONTINUOUS_ROOT_TUBES_AND_PL_"
    "MONODROMIES_PROMOTED_ENDPOINT_HANDLE_SYSTEM_OPEN"
)
NEXT = "MTT_Selected_q79SelectedAlignmentHandleMonodromyGlobalRelationAndIntegralH2Basis_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def main() -> int:
    a127 = load(A127)
    monodromy = load(MONODROMY_BATCH)
    tubes = load(TUBE_BATCH)
    braids = load(BRAID_BATCH)
    homology = load(HOMOLOGY)["homology_convention"]
    if not a127["checks"]["selected_alignment_90_node_input_closed"]:
        raise AssertionError("A127 selected endpoint input is unavailable")
    if monodromy["counts"]["monodromy_packets_complete"] != 90:
        raise AssertionError("selected pointwise monodromy inventory is incomplete")
    if tubes["status"] != "ALL_90_SELECTED_ALIGNMENT_CONTINUOUS_ROOT_TUBES_CLOSED":
        raise AssertionError("selected continuous root tubes are incomplete")
    if tubes["authority"]["monodromy_batch_sha256"] != sha256(MONODROMY_BATCH):
        raise AssertionError("root-tube/monodromy authority mismatch")
    if tubes["authority"]["certifier_sha256"] != sha256(TUBE_CERTIFIER):
        raise AssertionError("root-tube certifier authority mismatch")
    if braids["counts"]["selected_local_braids_certified"] != 90:
        raise AssertionError("selected interval local braid inventory is incomplete")
    if braids["authority"]["worker_sha256"] != sha256(BRAID_WORKER):
        raise AssertionError("selected interval braid authority mismatch")

    intersection = sp.Matrix(homology["intersection_matrix"])
    tube_rows = {
        (int(row["distinguished_index"]), row["root_id"]): row
        for row in tubes["rows"]
    }
    braid_rows = {
        (int(row["distinguished_index"]), row["root_id"]): row
        for row in braids["rows"][:90]
    }
    promoted_rows: list[dict] = []
    image_blocks: list[sp.Matrix] = []
    matrix_classes: dict[str, int] = {}
    for row in monodromy["rows"]:
        key = (int(row["distinguished_index"]), row["root_id"])
        if key not in tube_rows:
            raise AssertionError(f"missing selected root-tube certificate {key}")
        if key not in braid_rows:
            raise AssertionError(f"missing selected interval braid certificate {key}")
        packet_path = ROOT / row["packet_path"]
        if sha256(packet_path) != row["packet_sha256"]:
            raise AssertionError(f"selected monodromy hash mismatch {key}")
        packet = load(packet_path)
        tube_row = tube_rows[key]
        tube_path = ROOT / tube_row["certificate_path"]
        if sha256(tube_path) != tube_row["certificate_sha256"]:
            raise AssertionError(f"selected root-tube hash mismatch {key}")
        tube = load(tube_path)
        if tube["authority"]["monodromy_packet_sha256"] != sha256(packet_path):
            raise AssertionError(f"selected tube carrier mismatch {key}")
        if not tube["acceptance"]["promotion_ready"]:
            raise AssertionError(f"selected tube is not promotion ready {key}")
        braid_row = braid_rows[key]
        braid_path = ROOT / braid_row["certificate_path"]
        if sha256(braid_path) != braid_row["certificate_sha256"]:
            raise AssertionError(f"selected interval braid hash mismatch {key}")
        braid = load(braid_path)
        if not all(braid["acceptance"].values()):
            raise AssertionError(f"selected interval braid is not promotion ready {key}")

        matrix = sp.Matrix(packet["homology"]["integral_picard_lefschetz_matrix"])
        delta = matrix - sp.eye(4)
        permutation = packet["braid"]["final_root_permutation"]
        if (
            matrix.T * intersection * matrix != intersection
            or matrix.det() != 1
            or delta.rank() != 1
            or delta * delta != sp.zeros(4)
            or sum(value != index for index, value in enumerate(permutation)) != 2
        ):
            raise AssertionError(f"invalid selected PL row {key}")
        if sp.Matrix(braid["certificate"]["integral_symplectic_matrix"]) != matrix:
            raise AssertionError(f"selected interval braid matrix mismatch {key}")
        image_blocks.append(delta)
        matrix_key = json.dumps(packet["homology"]["integral_picard_lefschetz_matrix"], separators=(",", ":"))
        matrix_classes[matrix_key] = matrix_classes.get(matrix_key, 0) + 1
        promoted_rows.append(
            {
                "distinguished_index": key[0],
                "root_id": key[1],
                "integral_picard_lefschetz_matrix": packet["homology"][
                    "integral_picard_lefschetz_matrix"
                ],
                "endpoint_root_permutation": permutation,
                "certified_path_segments": tube["certificate"]["segments_certified"],
                "minimum_Rouche_relative_margin": tube["certificate"][
                    "minimum_Rouche_relative_margin"
                ],
                "minimum_pairwise_tube_separation": tube["certificate"][
                    "minimum_pairwise_tube_separation"
                ],
                "monodromy_packet_path": relative(packet_path),
                "monodromy_packet_sha256": sha256(packet_path),
                "root_tube_certificate_path": relative(tube_path),
                "root_tube_certificate_sha256": sha256(tube_path),
                "interval_braid_certificate_path": relative(braid_path),
                "interval_braid_certificate_sha256": sha256(braid_path),
                "interval_certified_crossings": braid["certificate"][
                    "interval_certified_crossings"
                ],
                "promotion_checks": {
                    "continuous_disjoint_root_tubes": True,
                    "recorded_and_true_braids_isotopic": True,
                    "polygonal_braid_word_interval_certified": True,
                    "exact_braid_matrix_replay": True,
                    "endpoint_transposition": True,
                    "integral_symplectic": True,
                    "rank_one_unipotent": True,
                },
                "promotion_accepted": True,
            }
        )

    if len(promoted_rows) != 90:
        raise AssertionError("selected promoted PL inventory changed")
    fiber_span_rank = sp.Matrix.hstack(*image_blocks).rank()
    if fiber_span_rank != 4:
        raise AssertionError("selected vanishing images do not span H1")

    promoted = {
        "schema": "MTTQ79NinetyPromotedSelectedAlignmentPicardLefschetzMonodromies.v1",
        "status": "ALL_90_SELECTED_ALIGNMENT_PICARD_LEFSCHETZ_MONODROMIES_PROMOTED",
        "common_marking": {
            "basis": ["a1", "b1", "a2", "b2"],
            "intersection_matrix": homology["intersection_matrix"],
            "branch_chart": "s=1/(t-(2+3i))",
            "projection_angle": "pi/7",
        },
        "rows": promoted_rows,
        "aggregate": {
            "promoted_local_matrix_count": 90,
            "certified_path_segment_count": tubes["counts"]["segments_certified"],
            "minimum_Rouche_relative_margin": tubes["minimums"]["Rouche_relative_margin"],
            "minimum_pairwise_tube_separation": tubes["minimums"]["pairwise_tube_separation"],
            "interval_certified_crossing_count": sum(
                row["interval_certified_crossings"] for row in promoted_rows
            ),
            "distinct_integral_PL_matrices": len(matrix_classes),
            "vanishing_image_span_rank": fiber_span_rank,
        },
        "strict_scope": {
            "selected_local_monodromies_promoted": 90,
            "selected_handle_monodromies_promoted": 0,
            "selected_global_surface_relation_checked": False,
            "endpoint_integral_H2_basis_columns": 0,
            "endpoint_period_columns": 0,
            "observed_SM_values_used": False,
        },
    }
    dump(PROMOTED, promoted)

    frontier = {
        "schema": "MTTU6FrontierAfterA128.v1",
        "status": STATUS,
        "A127_same_carrier_rule_preserved": True,
        "selected_alignment_simple_nodal_fibers": 90,
        "selected_alignment_certified_continuous_root_tubes": 90,
        "selected_alignment_promoted_local_PL_monodromies": 90,
        "selected_alignment_vanishing_image_span_rank": fiber_span_rank,
        "selected_alignment_handle_monodromies": 0,
        "selected_alignment_global_surface_relation_checked": False,
        "selected_alignment_integral_H2_basis_columns": 0,
        "selected_alignment_period_columns": 0,
        "integral_period_branch_selected": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        A127,
        MONODROMY_BATCH,
        TUBE_BATCH,
        BRAID_BATCH,
        HOMOLOGY,
        WORKER,
        ROOT_TRANSPORT,
        MONODROMY_BATCH_SCRIPT,
        TUBE_CERTIFIER,
        TUBE_BATCH_SCRIPT,
        BRAID_WORKER,
        BRAID_BATCH_SCRIPT,
        Path(__file__),
        PROMOTED,
        FRONTIER,
    ]
    candidate = {
        "schema": "MTTSelectedQ79AlignmentContinuousRootMonodromyPromotion.v1",
        "status": STATUS,
        "proof_artifact": "proof_corpus/MTT_Selected_q79AlignmentContinuousRootMonodromyPromotion_v1.md",
        "authority_hashes": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in authority_paths
        ],
        "outputs": {
            "promoted_monodromies": relative(PROMOTED),
            "frontier": relative(FRONTIER),
        },
        "checks": {
            "all_90_selected_continuous_root_tubes_certified": True,
            "all_90_selected_PL_monodromies_promoted": True,
            "vanishing_images_span_rank_four": True,
            "endpoint_integral_basis_invented": False,
            "endpoint_period_rows_invented": False,
            "observed_SM_target_fitting_used": False,
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "certificate": "MTTSelectedQ79AlignmentContinuousRootMonodromyPromotion",
        "status": STATUS,
        "candidate_sha256": sha256(CANDIDATE),
        "selected_continuous_root_tubes_certified": 90,
        "selected_PL_monodromies_promoted": 90,
        "selected_vanishing_image_span_rank": fiber_span_rank,
        "selected_endpoint_integral_H2_basis_columns": 0,
        "selected_endpoint_period_columns": 0,
        "integral_branch_selected": False,
        "observed_SM_target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    print(f"wrote {CERTIFICATE.relative_to(ROOT)}")
    print(
        "A128: all 90 selected-alignment continuous root tubes and local "
        "Picard-Lefschetz monodromies promoted; handle system remains"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
