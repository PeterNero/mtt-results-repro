from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2thimbleperiodexecution"
OUTPUT_DIR = ROOT / "candidate_data" / SLUG
BATCH = OUTPUT_DIR / "distinguished_thimble_period_batch.packet.json"
PRIMITIVE = OUTPUT_DIR / "primitive_thimble_period_candidate_table.packet.json"
CLOSED = OUTPUT_DIR / "closed_thimble_period_candidate_table.packet.json"
REPRESENTATIVE = OUTPUT_DIR / "representative_convergence_audit.packet.json"
FULL = OUTPUT_DIR / "full_90_column_convergence_audit.packet.json"
SUMMARY = OUTPUT_DIR / "certified_thimble_period_execution.packet.json"
FRONTIER = OUTPUT_DIR / "U6_frontier_after_A118.packet.json"
PRESENTATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2integralsurfacecyclepresentation"
    / "integral_surface_cycle_presentation.packet.json"
)
ENGINE = ROOT / "scripts" / "q79genus2_period_transport.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_q79GenusTwoCertifiedThimblePeriodExecution_v1.md"
)
STATUS = (
    "MTT_U6_Q79_ALL_THIMBLE_PERIODS_FLOATING_CONVERGED_"
    "HANDLE_LERAY_INTERVAL_PROMOTION_OPEN"
)
NEXT = "MTT_Selected_q79GenusTwoHandleAndLerayPeriodExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def parse_complex(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def table(packet: dict) -> np.ndarray:
    return np.asarray(
        [
            [parse_complex(value) for value in row]
            for row in packet["period_rows"]
        ],
        dtype=np.complex128,
    )


def main() -> int:
    if os.environ.get("MTT_RECOMPUTE_A118_PERIODS") == "1":
        subprocess.run(
            [
                sys.executable,
                str(
                    ROOT
                    / "scripts"
                    / "run_q79genus2distinguished_thimble_period_batch.py"
                ),
                "--jobs",
                "6",
                "--force",
            ],
            cwd=ROOT,
            check=True,
        )
    if os.environ.get("MTT_RECOMPUTE_A118_CONVERGENCE") == "1":
        subprocess.run(
            [
                sys.executable,
                str(
                    ROOT
                    / "scripts"
                    / "audit_q79genus2thimbleperiodconvergence.py"
                ),
                "--jobs",
                "5",
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
                    / "audit_q79genus2fullthimbleperiodconvergence.py"
                ),
                "--jobs",
                "6",
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
                / "build_selected_q79genus2certifiedthimbleperiodexecution.py"
            ),
        ],
        cwd=ROOT,
        check=True,
    )

    batch = load(BATCH)
    primitive_packet = load(PRIMITIVE)
    closed_packet = load(CLOSED)
    representative = load(REPRESENTATIVE)
    full = load(FULL)
    summary = load(SUMMARY)
    frontier = load(FRONTIER)
    presentation = load(PRESENTATION)
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    engine_hash = sha256(ENGINE)

    require(candidate["status"] == certificate["status"] == STATUS, "status")
    require(summary["status"] == frontier["status"] == STATUS, "packet status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(certificate["next_required_artifact"] == NEXT, "certificate next")
    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    require(all(candidate["checks"].values()), "candidate checks")
    require(summary["A119_supersession"]["primitive_90_column_table_remains_valid"], "primitive table retention")
    require(summary["A119_supersession"]["old_86_column_TK_table_is_diagnostic_only"], "old TK scope")
    require(not summary["A119_supersession"]["old_86_column_table_promoted_to_final_integral_H2"], "old TK overpromotion")
    require(candidate["supersession"]["old_TK_integral_basis_interpretation_retired"], "candidate supersession")
    require(certificate["old_TK_integral_basis_interpretation_superseded_by_A119"], "certificate supersession")

    require(batch["authority"]["period_engine_sha256"] == engine_hash, "batch engine")
    require(full["authority"]["period_engine_sha256"] == engine_hash, "full engine")
    require(
        representative["authority"]["period_engine_sha256"] == engine_hash,
        "representative engine",
    )
    require(batch["counts"]["complete_period_packets"] == 90, "packet count")
    require(batch["counts"]["primitive_complex_entries"] == 720, "primitive count")
    require(batch["counts"]["closed_thimble_complex_entries"] == 688, "closed count")

    primitive = table(primitive_packet)
    closed = table(closed_packet)
    require(primitive.shape == (8, 90), "primitive shape")
    require(closed.shape == (8, 86), "closed shape")
    root_ids = primitive_packet["column_root_ids"]
    require(len(root_ids) == 90, "root id count")
    replay_columns: list[np.ndarray] = []
    for index, root_id in enumerate(root_ids, start=1):
        packet = load(
            OUTPUT_DIR
            / f"d{index:03d}_{root_id}.thimble_period.candidate.json"
        )
        require(packet["distinguished_index"] == index, "ray index")
        require(packet["root_id"] == root_id, "ray root id")
        require(
            packet["authority"]["period_engine_sha256"] == engine_hash,
            "ray engine authority",
        )
        replay_columns.append(
            np.asarray(
                [
                    parse_complex(value)
                    for value in packet["execution"]["period_values"]
                ],
                dtype=np.complex128,
            )
        )
    replay = np.column_stack(replay_columns)
    require(np.array_equal(primitive, replay), "primitive replay")

    kernel = np.asarray(
        presentation["thimble_boundary_lattice"][
            "closed_thimble_kernel_basis_columns"
        ],
        dtype=np.int64,
    )
    require(kernel.shape == (90, 86), "kernel shape")
    require(
        np.allclose(closed, primitive @ kernel, rtol=0.0, atol=2.0e-14),
        "closed-thimble assembly",
    )

    primitive_comparison = full["primitive_table_comparison"]
    closed_comparison = full["closed_thimble_table_comparison"]
    require(full["strict_scope"]["all_90_columns_independently_rerun"], "full rerun")
    require(full["strict_scope"]["all_720_primitive_entries_compared"], "720 compared")
    require(full["strict_scope"]["all_688_closed_thimble_entries_compared"], "688 compared")
    require(
        float(primitive_comparison["maximum_scale_normalized_difference"])
        < 2.0e-8,
        "primitive floating convergence",
    )
    require(
        float(closed_comparison["maximum_scale_normalized_difference"])
        < 1.0e-8,
        "closed floating convergence",
    )
    require(
        primitive_comparison["columns_exceeding_scale_normalized_threshold"][
            "1.0e-07"
        ]
        == 0,
        "primitive 1e-7 threshold",
    )
    require(
        float(batch["minimums"]["local_direct_other_root_normalized_clearance"])
        > 1.0,
        "local direct clearance",
    )
    require(
        float(batch["minimums"]["endpoint_tail_other_root_normalized_clearance"])
        > 16.0,
        "endpoint tail clearance",
    )

    strict = summary["strict_scope"]
    require(strict["floating_thimble_execution_closed"], "floating execution")
    require(strict["full_floating_convergence_audit_closed"], "floating audit")
    require(not strict["interval_period_enclosure_closed"], "interval overclaim")
    require(not strict["handle_period_execution_closed"], "handle overclaim")
    require(not strict["Leray_edge_period_execution_closed"], "edge overclaim")
    require(not strict["beta_vector_closed"], "beta overclaim")
    require(not strict["integral_branch_selected"], "branch overclaim")
    require(not strict["gerbe_zero_or_no_go_closed"], "gerbe overclaim")
    require(not strict["full_U6_closed"], "U6 overclaim")
    require(frontier["final_integral_period_columns_executed"] == 86, "frontier columns")
    require(frontier["final_integral_period_columns_required"] == 92, "frontier target")
    require(frontier["handle_columns_executed"] == 0, "frontier handles")
    require(frontier["Leray_edge_columns_executed"] == 0, "frontier edges")

    for item in candidate["authority_hashes"]:
        path = ROOT / item["path"]
        require(path.exists(), f"missing authority: {path}")
        require(sha256(path) == item["sha256"], f"authority hash: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "90/90 primitive thimble columns",
        "86/86 closed-thimble columns",
        "1.4942421223033762e-8",
        "6.494312080665152e-9",
        "not interval enclosures",
        "four punctured-torus handle periods",
        "two explicit Leray-edge lifts",
        "Supersession notice",
        "not final integral `H2`",
    ):
        require(phrase in note, f"note phrase: {phrase}")

    print("A118 q79 certified thimble-period execution audit: PASS")
    print(f"status={STATUS}")
    print("retained: 90 primitive floating columns and independent convergence rerun")
    print("superseded: old 86-column TK integral-basis interpretation; see A119")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
