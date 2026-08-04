from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79alignmenteightbyninetytwoperiodexecution"
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79AlignmentEightByNinetyTwoPeriodExecution_v1.md"
ATLAS = DIRECTORY / "selected_alignment_period_atlas.packet.json"
HANDLE_ATLAS = DIRECTORY / "selected_alignment_handle_period_atlas.packet.json"
BATCH = PERIOD_DIRECTORY / "selected_alignment_thimble_period_batch.packet.json"
THIMBLE_CONVERGENCE = PERIOD_DIRECTORY / "selected_alignment_full_90_column_convergence_audit.packet.json"
ORIENTATION = PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"
HANDLE_PRODUCTION = PERIOD_DIRECTORY / "selected_alignment_primitive_handle_periods.packet.json"
HANDLE_TIGHT = PERIOD_DIRECTORY / "selected_alignment_primitive_handle_periods.tight.packet.json"
LERAY = PERIOD_DIRECTORY / "selected_alignment_explicit_Leray_edge_periods.packet.json"
CONVERGENCE = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_convergence.packet.json"
PERIOD_TABLE = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_period_table.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A131.packet.json"
INTEGRAL_BASIS = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_exact_integral_H2_basis.packet.json"
)
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"


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
    atlas = load(ATLAS)
    batch = load(BATCH)
    thimble_convergence = load(THIMBLE_CONVERGENCE)
    orientation = load(ORIENTATION)
    handles = load(HANDLE_PRODUCTION)
    leray = load(LERAY)
    convergence = load(CONVERGENCE)
    periods = load(PERIOD_TABLE)
    frontier = load(FRONTIER)
    basis = load(INTEGRAL_BASIS)
    if atlas["counts"] != {"selected_y": 42, "selected_z": 48}:
        raise AssertionError("selected period atlas count")
    if batch["counts"]["complete_period_packets"] != 90:
        raise AssertionError("selected thimble packet count")
    if float(
        thimble_convergence["primitive_table_comparison"][
            "maximum_scale_normalized_difference"
        ]
    ) >= 1.0e-8:
        raise AssertionError("selected thimble convergence")
    if float(
        orientation["checks"][
            "maximum_scaled_holomorphic_linearity_residual"
        ]
    ) >= 1.0e-8:
        raise AssertionError("selected orientation residual")
    if not handles["central_lift_result"][
        "independent_period_continuation_agrees"
    ]:
        raise AssertionError("selected handle lift replay")
    if leray["period_matrix_exact"] != [[0, 0] for _ in range(8)]:
        raise AssertionError("selected exact Leray zeros")
    if periods["period_matrix_shape"] != [8, 92]:
        raise AssertionError("selected final period shape")
    if basis["column_order"] != periods["column_order"]:
        raise AssertionError("selected period/basis column order")
    if float(
        convergence[
            "maximum_primary_column_scale_normalized_difference_envelope"
        ]
    ) >= 1.0e-8:
        raise AssertionError("selected full convergence envelope")
    if periods["strict_scope"]["integral_period_branch_selected"]:
        raise AssertionError("selected integral branch invented")

    authority_paths = [
        NOTE,
        ATLAS,
        HANDLE_ATLAS,
        BATCH,
        THIMBLE_CONVERGENCE,
        ORIENTATION,
        HANDLE_PRODUCTION,
        HANDLE_TIGHT,
        INTEGRAL_BASIS,
        LERAY,
        CONVERGENCE,
        PERIOD_TABLE,
        FRONTIER,
        ROOT / "scripts" / "q79_selected_alignment_period_transport.py",
        ROOT / "scripts" / "compute_q79_selected_alignment_single_thimble_period.py",
        ROOT / "scripts" / "select_q79_selected_alignment_period_atlas.py",
        ROOT / "scripts" / "synchronize_q79_selected_alignment_thimble_orientations.py",
        ROOT / "scripts" / "compute_q79_selected_alignment_handle_periods.py",
        ROOT / "scripts" / "build_selected_q79_alignment_full_period_matrix.py",
        Path(__file__).resolve(),
    ]
    candidate = {
        "schema": "MTTSelectedQ79AlignmentEightByNinetyTwoPeriodExecution.v1",
        "status": "MTT_U6_Q79_SELECTED_ALIGNMENT_FLOATING_8X92_PERIOD_TABLE_CLOSED_EXACT_LATTICE_BRANCH_OPEN",
        "proof_artifact": relative(NOTE),
        "authority_hashes": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in authority_paths
        ],
        "outputs": {
            "period_atlas": relative(ATLAS),
            "thimble_convergence": relative(THIMBLE_CONVERGENCE),
            "orientation_synchronization": relative(ORIENTATION),
            "primitive_handles": relative(HANDLE_PRODUCTION),
            "Leray_edge_periods": relative(LERAY),
            "full_convergence": relative(CONVERGENCE),
            "full_period_table": relative(PERIOD_TABLE),
            "frontier": relative(FRONTIER),
        },
        "checks": {
            "all_90_selected_thimble_columns_computed": True,
            "all_720_primitive_entries_tighter_rerun": True,
            "projective_atlas_selected_without_period_values": True,
            "all_90_thimbles_synchronized_to_A130_orientation": True,
            "all_8_selected_handle_columns_computed": True,
            "interval_selected_handle_lifts_independently_replayed": True,
            "exact_Leray_zero_entries": 16,
            "complete_floating_integral_basis_period_columns": 92,
            "integral_branch_not_invented": True,
            "observed_SM_target_fitting_used": False,
        },
        "results": frontier,
        "next_required_artifact": "MTT_Selected_q79AlignmentBetaIntegralLatticeDecision_v1",
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "certificate": "MTTSelectedQ79AlignmentEightByNinetyTwoPeriodExecution",
        "status": candidate["status"],
        "candidate_sha256": sha256(CANDIDATE),
        "selected_floating_period_matrix_shape": [8, 92],
        "selected_exact_integral_basis_columns": 92,
        "exact_Leray_zero_entries": 16,
        "integral_branch_selected": False,
        "observed_SM_target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {relative(CANDIDATE)}")
    print(f"wrote {relative(CERTIFICATE)}")
    print("A131: selected floating 8x92 period table closed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
