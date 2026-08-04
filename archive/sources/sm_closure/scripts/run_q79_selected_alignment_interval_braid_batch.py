from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
MONODROMY_BATCH = DIRECTORY / "selected_alignment_meridian_monodromy_batch.packet.json"
MONODROMY = DIRECTORY / "selected_alignment_meridian_monodromy"
TUBES = DIRECTORY / "selected_alignment_continuous_root_tubes"
CERTIFICATES = DIRECTORY / "selected_alignment_interval_braid_certificates"
OUTPUT = DIRECTORY / "selected_alignment_interval_braid_and_global_relation.packet.json"
WORKER = ROOT / "scripts" / "certify_q79_selected_alignment_single_pl_braid.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stem(index: int, root_id: str) -> str:
    return f"d{index:03d}_{root_id}"


def packet_path(index: int, root_id: str) -> Path:
    return MONODROMY / f"{stem(index, root_id)}.packet.json"


def tube_path(index: int, root_id: str) -> Path:
    return TUBES / f"{stem(index, root_id)}.root_tube_certificate.packet.json"


def certificate_path(index: int, root_id: str) -> Path:
    return CERTIFICATES / f"{stem(index, root_id)}.braid_certificate.packet.json"


def valid(index: int, root_id: str) -> dict | None:
    path = certificate_path(index, root_id)
    if not path.exists():
        return None
    certificate = load(path)
    return certificate if (
        certificate["distinguished_index"] == index
        and certificate["root_id"] == root_id
        and certificate["authority"]["typed_monodromy_packet_sha256"]
        == sha256(packet_path(index, root_id))
        and certificate["authority"]["root_tube_certificate_sha256"]
        == sha256(tube_path(index, root_id))
        and all(certificate["acceptance"].values())
    ) else None


def run(index: int, root_id: str, force: bool) -> tuple[int, str, bool]:
    if not force and valid(index, root_id) is not None:
        return index, root_id, True
    result = subprocess.run(
        [
            sys.executable,
            str(WORKER),
            "--distinguished-index",
            str(index),
            "--root-id",
            root_id,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0 or valid(index, root_id) is None:
        raise RuntimeError(
            f"{stem(index, root_id)} failed code={result.returncode}\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return index, root_id, False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=8)
    parser.add_argument("--force", action="store_true")
    arguments = parser.parse_args()
    monodromy = load(MONODROMY_BATCH)
    rows = [
        (int(row["distinguished_index"]), row["root_id"])
        for row in monodromy["rows"]
    ] + [(91, "handle_A"), (92, "handle_B")]

    failures: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=arguments.jobs) as executor:
        futures = {
            executor.submit(run, index, root_id, arguments.force): (index, root_id)
            for index, root_id in rows
        }
        for future in concurrent.futures.as_completed(futures):
            index, root_id = futures[future]
            try:
                _, _, reused = future.result()
                print(
                    f"{stem(index, root_id)}: {'reused' if reused else 'certified'}",
                    flush=True,
                )
            except Exception as error:
                failures.append(str(error))
                print(f"{stem(index, root_id)}: FAILED", flush=True)
    if failures:
        raise RuntimeError("\n\n".join(failures))

    certificates = [valid(index, root_id) for index, root_id in rows]
    if any(value is None for value in certificates):
        raise AssertionError("selected interval braid batch is incomplete")
    complete = [value for value in certificates if value is not None]
    local = complete[:90]
    handles = {value["root_id"][-1]: value for value in complete[90:]}
    ordered_product = sp.eye(4)
    for value in local:
        ordered_product = sp.Matrix(
            value["certificate"]["integral_symplectic_matrix"]
        ) * ordered_product
    handle_a = sp.Matrix(handles["A"]["certificate"]["integral_symplectic_matrix"])
    handle_b = sp.Matrix(handles["B"]["certificate"]["integral_symplectic_matrix"])
    boundary = handle_b.inv() * handle_a.inv() * handle_b * handle_a
    if ordered_product != boundary:
        raise AssertionError("selected ordered PL product misses handle boundary")

    finite_crossing_heights = [
        float(value["certificate"]["minimum_crossing_height_lower"])
        for value in complete
        if value["certificate"]["minimum_crossing_height_lower"] is not None
    ]
    finite_event_gaps = [
        float(value["certificate"]["minimum_same_segment_event_parameter_gap_lower"])
        for value in complete
        if value["certificate"]["minimum_same_segment_event_parameter_gap_lower"] is not None
    ]
    payload = {
        "schema": "MTTQ79SelectedAlignmentIntervalBraidAndGlobalRelation.v1",
        "status": "ALL_90_SELECTED_PL_AND_TWO_HANDLE_BRAIDS_PROMOTED_GLOBAL_RELATION_CLOSED",
        "authority": {
            "monodromy_batch_sha256": sha256(MONODROMY_BATCH),
            "worker_sha256": sha256(WORKER),
        },
        "action_convention": {
            "path_concatenation": "gamma then delta",
            "left_action_rule": "M(gamma then delta)=M(delta)*M(gamma)",
            "positive_cut_square_boundary_path": "A*B*A^-1*B^-1",
            "positive_boundary_action": "B^-1*A^-1*B*A",
            "positive_distinguished_path_product": "m1*m2*...*m90",
            "ordered_matrix_product": "M90*M89*...*M1",
        },
        "global_surface_relation": {
            "pi1_path_relation": "A*B*A^-1*B^-1=m1*m2*...*m90",
            "handle_boundary_action": [[int(value) for value in boundary.row(index)] for index in range(4)],
            "ordered_distinguished_action_product": [[int(value) for value in ordered_product.row(index)] for index in range(4)],
            "exact_integer_matrix_equality": True,
        },
        "counts": {
            "selected_local_braids_certified": 90,
            "selected_handle_braids_certified": 2,
            "interval_braid_certificates": 92,
            "certified_path_segments": sum(
                value["certificate"]["certified_path_segments"] for value in complete
            ),
            "interval_certified_crossings": sum(
                value["certificate"]["interval_certified_crossings"] for value in complete
            ),
            "multi_event_segments": sum(
                value["certificate"]["multi_event_segment_count"] for value in complete
            ),
        },
        "minimums": {
            "projected_endpoint_pair_difference_lower": format(
                min(float(value["certificate"]["minimum_projected_endpoint_pair_difference_lower"]) for value in complete),
                ".17g",
            ),
            "crossing_height_lower": format(min(finite_crossing_heights), ".17g"),
            "same_segment_event_parameter_gap_lower": (
                format(min(finite_event_gaps), ".17g") if finite_event_gaps else None
            ),
        },
        "rows": [
            {
                "distinguished_index": index,
                "root_id": root_id,
                "certificate_path": str(certificate_path(index, root_id).relative_to(ROOT)).replace("\\", "/"),
                "certificate_sha256": sha256(certificate_path(index, root_id)),
                "integral_symplectic_matrix": value["certificate"]["integral_symplectic_matrix"],
            }
            for (index, root_id), value in zip(rows, complete)
        ],
        "acceptance": {
            "all_92_continuous_braid_isotopies_certified": True,
            "all_92_polygonal_braid_words_interval_certified": True,
            "all_92_exact_integral_matrix_replays_match": True,
            "global_integral_H1_surface_relation_closed": True,
        },
        "strict_scope": {
            "endpoint_integral_H2_basis_columns": 0,
            "endpoint_period_columns": 0,
            "integral_period_branch_selected": False,
            "observed_SM_values_used": False,
        },
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    print(json.dumps(payload["counts"], indent=2, sort_keys=True))
    print(json.dumps(payload["minimums"], indent=2, sort_keys=True))
    print(json.dumps(payload["global_surface_relation"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
