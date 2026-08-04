from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
PRIMITIVE_THIMBLES = PERIOD_DIRECTORY / "selected_alignment_primitive_thimble_period_table.packet.json"
THIMBLE_CONVERGENCE = PERIOD_DIRECTORY / "selected_alignment_full_90_column_convergence_audit.packet.json"
ORIENTATION = PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"
HANDLE_PRODUCTION = PERIOD_DIRECTORY / "selected_alignment_primitive_handle_periods.packet.json"
HANDLE_TIGHT = PERIOD_DIRECTORY / "selected_alignment_primitive_handle_periods.tight.packet.json"
INTEGRAL_BASIS = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_exact_integral_H2_basis.packet.json"
)
LERAY_BASIS = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_Leray_edge_basis.packet.json"
)
RESIDUES = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_prym_residues_and_delta_normal_function.packet.json"
)
LERAY_PERIODS = PERIOD_DIRECTORY / "selected_alignment_explicit_Leray_edge_periods.packet.json"
CONVERGENCE = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_convergence.packet.json"
PERIOD_TABLE = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_period_table.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A131.packet.json"


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


def decode_complex(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_table(rows: list[list[dict[str, str]]]) -> np.ndarray:
    return np.asarray(
        [[decode_complex(value) for value in row] for row in rows],
        dtype=np.complex128,
    )


def encode_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def encode_matrix(matrix: np.ndarray) -> list[list[dict[str, str]]]:
    return [
        [encode_complex(complex(value)) for value in row] for row in matrix
    ]


def main() -> int:
    primitive_packet = load(PRIMITIVE_THIMBLES)
    thimble_convergence = load(THIMBLE_CONVERGENCE)
    orientation = load(ORIENTATION)
    handle_production_packet = load(HANDLE_PRODUCTION)
    handle_tight_packet = load(HANDLE_TIGHT)
    integral_basis_packet = load(INTEGRAL_BASIS)
    leray_basis = load(LERAY_BASIS)
    residues = load(RESIDUES)

    primitive_thimbles = complex_table(primitive_packet["period_rows"])
    signs = np.asarray(orientation["column_signs"], dtype=np.int64)
    production_handles = complex_table(
        handle_production_packet["primitive_handle_period_matrix"]
    )
    tight_handles = complex_table(
        handle_tight_packet["primitive_handle_period_matrix"]
    )
    primary_basis = np.asarray(
        integral_basis_packet["primary_basis"]["basis_columns"],
        dtype=np.int64,
    )
    if primitive_thimbles.shape != (8, 90) or signs.shape != (90,):
        raise AssertionError("selected primitive thimble table shape")
    if production_handles.shape != (8, 8) or tight_handles.shape != (8, 8):
        raise AssertionError("selected primitive handle table shape")
    if primary_basis.shape != (98, 90):
        raise AssertionError("selected A130 primary basis shape")
    if integral_basis_packet["column_order"][-2:] != [
        "Leray_F",
        "Leray_Gamma0",
    ]:
        raise AssertionError("selected A130 Leray column order")

    oriented_thimbles = primitive_thimbles * signs[np.newaxis, :]
    primitive_chain = np.hstack([oriented_thimbles, production_handles])
    primary_periods = primitive_chain @ primary_basis
    exact_edge_zero = np.zeros((8, 2), dtype=np.complex128)
    final_periods = np.hstack([primary_periods, exact_edge_zero])
    if final_periods.shape != (8, 92):
        raise AssertionError("selected final period table shape")

    if residues["residue_forms"]["exact_linear_rank"] != 8:
        raise AssertionError("selected primitive residue rank")
    if leray_basis["edge_basis"]["rank"] != 2:
        raise AssertionError("selected Leray edge rank")
    leray = {
        "schema": "MTTQ79SelectedAlignmentExplicitLerayEdgePeriods.v1",
        "status": "SELECTED_ALIGNMENT_TWO_PRIMITIVE_LERAY_EDGE_COLUMNS_EXACTLY_ZERO",
        "edge_basis": leray_basis["edge_basis"],
        "residue_argument": {
            "A111_exact_traceless_residue_rank": 8,
            "forms": primitive_packet["form_names"],
            "statement": "The eight traceless alignment residues span the primitive holomorphic two-form subspace. The A130 fiber and adjusted horizontal Leray classes are Poincare dual to ambient restrictions, so every primitive residue pairing with either class is exactly zero.",
        },
        "period_column_order": ["Leray_F", "Leray_Gamma0"],
        "period_matrix_shape": [8, 2],
        "period_matrix_exact": [[0, 0] for _ in range(8)],
        "authority": {
            "selected_Leray_basis_sha256": sha256(LERAY_BASIS),
            "exact_residue_packet_sha256": sha256(RESIDUES),
            "builder_source_sha256": sha256(Path(__file__).resolve()),
        },
        "strict_scope": {
            "exact_topological_zero": True,
            "floating_quadrature_used": False,
            "observed_SM_values_used": False,
        },
    }
    dump(LERAY_PERIODS, leray)

    convergence_rows = {
        int(row["distinguished_index"]): row
        for row in thimble_convergence[
            "columns_by_decreasing_scale_normalized_difference"
        ]
    }
    if set(convergence_rows) != set(range(1, 91)):
        raise AssertionError("selected thimble convergence inventory")
    delta_thimble = np.column_stack(
        [
            np.asarray(
                [
                    float(value)
                    for value in convergence_rows[index][
                        "rowwise_absolute_differences"
                    ]
                ],
                dtype=np.float64,
            )
            for index in range(1, 91)
        ]
    )
    delta_handle = np.abs(production_handles - tight_handles)
    primary_envelope = (
        delta_thimble @ np.abs(primary_basis[:90, :])
        + delta_handle @ np.abs(primary_basis[90:98, :])
    )
    maximum_primary_absolute = float(np.max(primary_envelope))
    column_scaled = [
        float(
            np.max(primary_envelope[:, column])
            / max(
                float(np.max(np.abs(primary_periods[:, column]))),
                np.finfo(float).tiny,
            )
        )
        for column in range(90)
    ]
    maximum_primary_scaled = max(column_scaled)
    maximum_handle_absolute = float(np.max(delta_handle))
    maximum_handle_scaled = maximum_handle_absolute / max(
        float(np.max(np.abs(production_handles))), np.finfo(float).tiny
    )
    if maximum_primary_scaled >= 1.0e-7:
        raise AssertionError("selected primary period convergence envelope")
    convergence = {
        "schema": "MTTQ79SelectedAlignmentFullIntegralBasisConvergence.v1",
        "status": "SELECTED_ALIGNMENT_TWO_RUN_ERROR_ENVELOPE_PROPAGATED_TO_ALL_NINETY_PRIMARY_COLUMNS",
        "primitive_thimble_baseline_and_tighter_comparison": {
            "entries_compared": 720,
            "maximum_scale_normalized_difference": thimble_convergence[
                "primitive_table_comparison"
            ]["maximum_scale_normalized_difference"],
        },
        "primitive_handle_baseline_parameters": handle_production_packet[
            "execution"
        ],
        "primitive_handle_tighter_parameters": handle_tight_packet["execution"],
        "maximum_primitive_handle_absolute_difference": format(
            maximum_handle_absolute, ".17g"
        ),
        "maximum_primitive_handle_scale_normalized_difference": format(
            maximum_handle_scaled, ".17g"
        ),
        "propagation_formula": "DeltaPi <= DeltaT*abs(U_thimble)+DeltaH*abs(U_handle)",
        "primary_entrywise_absolute_difference_envelope_rows": [
            [format(float(value), ".17g") for value in row]
            for row in primary_envelope
        ],
        "maximum_primary_absolute_difference_envelope": format(
            maximum_primary_absolute, ".17g"
        ),
        "maximum_primary_column_scale_normalized_difference_envelope": format(
            maximum_primary_scaled, ".17g"
        ),
        "column_scale_normalized_envelopes": [
            format(value, ".17g") for value in column_scaled
        ],
        "authority": {
            "thimble_convergence_sha256": sha256(THIMBLE_CONVERGENCE),
            "handle_baseline_sha256": sha256(HANDLE_PRODUCTION),
            "handle_tighter_sha256": sha256(HANDLE_TIGHT),
            "selected_integral_basis_sha256": sha256(INTEGRAL_BASIS),
            "builder_source_sha256": sha256(Path(__file__).resolve()),
        },
        "strict_scope": {
            "all_8x90_primary_entries_have_floating_error_envelopes": True,
            "two_exact_zero_Leray_columns_appended": True,
            "interval_period_enclosure": False,
        },
    }
    dump(CONVERGENCE, convergence)

    period_table = {
        "schema": "MTTQ79SelectedAlignmentFullIntegralBasisPeriodTable.v1",
        "status": "SELECTED_ALIGNMENT_FLOATING_EIGHT_BY_NINETY_TWO_INTEGRAL_BASIS_PERIOD_TABLE_CLOSED",
        "form_names": primitive_packet["form_names"],
        "period_matrix_shape": [8, 92],
        "column_order": integral_basis_packet["column_order"],
        "period_matrix_rows": encode_matrix(final_periods),
        "assembly": {
            "primitive_thimble_shape": [8, 90],
            "canonical_thimble_orientation_signs_applied": 90,
            "primitive_handle_shape": [8, 8],
            "primitive_chain_shape": [8, 98],
            "A130_primary_integer_basis_shape": [98, 90],
            "primary_period_shape": [8, 90],
            "exact_zero_Leray_edge_shape": [8, 2],
            "formula": "Pi=[(T*diag(sigma) | H)*U_A130 | 0_(8x2)]",
        },
        "maximum_absolute_entry": format(
            float(np.max(np.abs(final_periods))), ".17g"
        ),
        "floating_error_envelope": {
            "maximum_primary_absolute": format(
                maximum_primary_absolute, ".17g"
            ),
            "maximum_primary_column_scale_normalized": format(
                maximum_primary_scaled, ".17g"
            ),
        },
        "authority": {
            "primitive_thimble_table_sha256": sha256(PRIMITIVE_THIMBLES),
            "thimble_orientation_sha256": sha256(ORIENTATION),
            "primitive_handle_baseline_sha256": sha256(HANDLE_PRODUCTION),
            "selected_integral_H2_basis_sha256": sha256(INTEGRAL_BASIS),
            "exact_Leray_periods_sha256": sha256(LERAY_PERIODS),
            "full_convergence_sha256": sha256(CONVERGENCE),
            "builder_source_sha256": sha256(Path(__file__).resolve()),
        },
        "strict_scope": {
            "same_selected_carrier_as_A127_beta": True,
            "exact_integral_H2_basis_columns": 92,
            "floating_complex_period_entries": 720,
            "exact_zero_period_entries": 16,
            "interval_certified_nonzero_period_entries": 0,
            "integral_period_branch_selected": False,
            "observed_SM_values_used": False,
        },
    }
    dump(PERIOD_TABLE, period_table)

    frontier = {
        "schema": "MTTU6FrontierAfterA131.v1",
        "status": "SELECTED_ALIGNMENT_FLOATING_8X92_PERIOD_TABLE_CLOSED_EXACT_LATTICE_BRANCH_OPEN",
        "selected_alignment_exact_integral_H2_basis_columns": 92,
        "selected_alignment_floating_period_columns": 92,
        "selected_alignment_floating_complex_period_entries": 720,
        "selected_alignment_exact_zero_Leray_entries": 16,
        "selected_alignment_interval_period_entries": 0,
        "integral_period_branch_selected": False,
        "U6_strong_CP_closed": False,
        "next_required_artifact": "MTT_Selected_q79AlignmentBetaIntegralLatticeDecision_v1",
    }
    dump(FRONTIER, frontier)
    print(f"wrote {PERIOD_TABLE.relative_to(ROOT)}")
    print(
        "A131 floating 8x92 selected-alignment period table closed; "
        f"maximum propagated scaled envelope={maximum_primary_scaled:.6e}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
