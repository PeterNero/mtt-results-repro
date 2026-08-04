from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np

from q79_selected_alignment_genus2_root_transport import decode_acb
from q79_selected_alignment_period_transport import (
    Q79SelectedAlignmentPeriodRootTransport,
)
from q79genus2_root_transport import midpoint


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
Y_FIBRATION = DIRECTORY / "selected_alignment_genus2_fibration_seed.interval.packet.json"
FAN = DIRECTORY / "selected_alignment_distinguished_radial_fan.interval.packet.json"
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
FACTORIZATION = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmenthandlesandglobalsurfacerelation"
    / "selected_alignment_global_integral_gauss_manin_factorization.packet.json"
)
PRESENTATION = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_coupled_integral_H2_chain_presentation.packet.json"
)
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
OUTPUT = PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode_complex(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def encode_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def encode_matrix(matrix: np.ndarray) -> list[list[dict[str, str]]]:
    return [
        [encode_complex(complex(value)) for value in row] for row in matrix
    ]


def period_path(row: dict) -> Path:
    return PERIOD_DIRECTORY / (
        f"d{row['distinguished_index']:03d}_{row['root_id']}"
        ".thimble_period.candidate.json"
    )


def base_y_to_z_transition(homology: dict) -> np.ndarray:
    transport = Q79SelectedAlignmentPeriodRootTransport(
        Y_FIBRATION,
        homology,
        omitted=2 + 3j,
        dps=80,
    )
    a_value, b_value = [
        midpoint(value) for value in transport.ab_at(transport.base)
    ]
    packet = load(Y_FIBRATION)
    alignment = np.asarray(
        [
            [midpoint(decode_acb(value)) for value in row]
            for row in packet["source"]["alignment_interval"]
        ],
        dtype=np.complex128,
    )
    line = alignment @ np.asarray([a_value, b_value, 1 + 0j])
    alpha = -line[0] / line[1]
    gamma = -line[2] / line[1]
    common = -(line[1] ** 2) / (line[2] ** 2)
    transition = np.zeros((5, 5), dtype=np.complex128)
    for power in range(5):
        for index in range(power + 1):
            transition[power, index] = (
                common
                * math.comb(power, index)
                * alpha ** (power - index)
                * gamma**index
            )
    return transition


def main() -> int:
    fan_rows = load(FAN)["distinguished_positive_meridians"]
    factorization = load(FACTORIZATION)
    factors = factorization["factors"]
    if [row["root_id"] for row in fan_rows] != [
        row["root_id"] for row in factors
    ]:
        raise AssertionError("selected fan/factor orientation order changed")
    presentation = load(PRESENTATION)
    pivots = [
        int(value) - 1
        for value in presentation["vanishing_lattice"][
            "unimodular_pivot_indices_one_based"
        ]
    ]
    if len(pivots) != 4:
        raise AssertionError("selected orientation pivot count")
    vectors = np.asarray(
        [row["positive_vanishing_cycle_up_to_sign"] for row in factors],
        dtype=np.int64,
    ).T
    if round(np.linalg.det(vectors[:, pivots])) not in (-1, 1):
        raise AssertionError("selected orientation pivots are not unimodular")

    homology = load(HOMOLOGY)["homology_convention"]
    transition = base_y_to_z_transition(homology)
    packets = [load(period_path(row)) for row in fan_rows]
    packet_hashes = [sha256(period_path(row)) for row in fan_rows]
    base_periods = np.empty((5, 90), dtype=np.complex128)
    for column, packet in enumerate(packets):
        values = np.asarray(
            [
                decode_complex(row["value"])
                for row in packet["execution"][
                    "base_fiber_propagated_periods"
                ]
            ],
            dtype=np.complex128,
        )
        if packet.get("line_chart", "y") == "z":
            values = np.linalg.solve(transition, values)
        base_periods[:, column] = values

    candidates: list[dict] = []
    pivot_vectors = vectors[:, pivots]
    for tail in itertools.product((-1, 1), repeat=3):
        pivot_signs = np.asarray((1, *tail), dtype=np.int64)
        basis = (
            base_periods[:, pivots]
            * pivot_signs[np.newaxis, :]
        ) @ np.linalg.inv(pivot_vectors)
        signs = np.ones(90, dtype=np.int64)
        residuals = np.empty(90, dtype=np.float64)
        for column in range(90):
            predicted = basis @ vectors[:, column]
            # Only t^0 dt/u and t^1 dt/u descend to compact H1.  The three
            # higher meromorphic rows remember a puncture-at-infinity lift.
            positive = np.linalg.norm(
                base_periods[:2, column] - predicted[:2]
            )
            negative = np.linalg.norm(
                -base_periods[:2, column] - predicted[:2]
            )
            signs[column] = 1 if positive <= negative else -1
            residuals[column] = min(positive, negative) / max(
                np.linalg.norm(predicted[:2]),
                np.linalg.norm(base_periods[:2, column]),
                np.finfo(float).tiny,
            )
        candidates.append(
            {
                "pivot_signs": pivot_signs,
                "basis": basis,
                "signs": signs,
                "residuals": residuals,
                "maximum_scaled_residual": float(np.max(residuals)),
                "rms_scaled_residual": float(
                    np.sqrt(np.mean(residuals**2))
                ),
            }
        )
    candidates.sort(
        key=lambda row: (
            row["maximum_scaled_residual"], row["rms_scaled_residual"]
        )
    )
    selected = candidates[0]
    rejected = candidates[1]
    if selected["maximum_scaled_residual"] >= 1.0e-7:
        worst = np.argsort(selected["residuals"])[-10:][::-1]
        raise AssertionError(
            "selected orientation synchronization residual: "
            f"best={selected['maximum_scaled_residual']:.17g}, "
            f"next={rejected['maximum_scaled_residual']:.17g}, "
            f"pivots={selected['pivot_signs'].tolist()}, "
            f"worst={[(int(i + 1), float(selected['residuals'][i])) for i in worst]}"
        )
    if rejected["maximum_scaled_residual"] <= 100 * selected[
        "maximum_scaled_residual"
    ]:
        raise AssertionError("selected orientation synchronization ambiguous")

    basis = selected["basis"]
    holomorphic = basis[:2, :]
    a_periods = holomorphic[:, [0, 2]]
    b_periods = holomorphic[:, [1, 3]]
    riemann = np.linalg.solve(a_periods, b_periods)
    symmetry_error = float(np.max(np.abs(riemann - riemann.T)))
    imaginary_eigenvalues = np.linalg.eigvalsh(riemann.imag)
    if symmetry_error >= 1.0e-7:
        raise AssertionError("synchronized Riemann matrix is not symmetric")
    if float(np.min(imaginary_eigenvalues)) <= 0:
        raise AssertionError("synchronized Riemann matrix positivity failed")

    signs = selected["signs"]
    payload = {
        "schema": "MTTQ79SelectedAlignmentThimbleOrientationSynchronization.v1",
        "status": "ALL_NINETY_NUMERICAL_THIMBLES_HOLOMORPHICALLY_SYNCHRONIZED_TO_A130_CANONICAL_ORIENTATION",
        "orientation_equation": "sigma_i*p_i^hol=P_marked^hol*v_i, where v_i is the A130 first-nonzero-positive compact-H1 vanishing vector",
        "canonical_global_sign_gauge": (
            f"sigma_{pivots[0] + 1:03d}=+1"
        ),
        "unimodular_pivot_indices_one_based": [value + 1 for value in pivots],
        "pivot_signs": selected["pivot_signs"].astype(int).tolist(),
        "column_signs": signs.astype(int).tolist(),
        "columns_flipped": [
            index + 1 for index, value in enumerate(signs) if value == -1
        ],
        "marked_base_period_matrix": encode_matrix(basis),
        "base_y_to_z_five_period_transition": encode_matrix(transition),
        "checks": {
            "maximum_scaled_holomorphic_linearity_residual": format(
                selected["maximum_scaled_residual"], ".17g"
            ),
            "rms_scaled_holomorphic_linearity_residual": format(
                selected["rms_scaled_residual"], ".17g"
            ),
            "next_best_maximum_scaled_residual": format(
                rejected["maximum_scaled_residual"], ".17g"
            ),
            "next_best_to_selected_maximum_residual_ratio": format(
                rejected["maximum_scaled_residual"]
                / selected["maximum_scaled_residual"],
                ".17g",
            ),
            "normalized_Riemann_matrix": encode_matrix(riemann),
            "Riemann_symmetry_error": format(symmetry_error, ".17g"),
            "Riemann_imaginary_eigenvalues": [
                format(float(value), ".17g")
                for value in imaginary_eigenvalues
            ],
        },
        "authority": {
            "distinguished_fan_sha256": sha256(FAN),
            "selected_global_factorization_sha256": sha256(FACTORIZATION),
            "selected_integral_presentation_sha256": sha256(PRESENTATION),
            "selected_y_fibration_sha256": sha256(Y_FIBRATION),
            "homology_convention_sha256": sha256(HOMOLOGY),
            "ordered_period_packet_hashes_sha256": hashlib.sha256(
                "".join(packet_hashes).encode("ascii")
            ).hexdigest(),
            "synchronizer_source_sha256": sha256(Path(__file__).resolve()),
        },
        "strict_scope": {
            "all_90_selected_base_vanishing_period_vectors_used": True,
            "all_90_A130_canonical_vanishing_vectors_used": True,
            "compact_H1_holomorphic_rows_used_for_orientation": 2,
            "higher_meromorphic_rows_used_for_orientation": 0,
            "higher_meromorphic_rows_retain_puncture_lift_dependence": True,
            "orientation_only_no_period_magnitude_selection": True,
            "observed_SM_values_used": False,
            "floating_linearity_certificate": True,
            "interval_orientation_certificate": False,
        },
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
