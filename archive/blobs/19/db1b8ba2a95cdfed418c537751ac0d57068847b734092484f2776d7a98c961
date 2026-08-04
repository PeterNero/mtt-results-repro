"""Attempt to fill the selected SU(5) qutrit polarization packet.

This uses the strongest currently available route in the proof package: the
block-factorized qutrit family-twist candidate plus the finite qutrit
polarization lemma.  The attempt deliberately does not claim selected MTT data
unless the upstream certificates prove selected source promotion.

The output packet is validator-ready.  At present it is expected to pass the
finite algebra as an UNSELECTED_FIXTURE and not promote the heavy-link
candidate to selected input.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
DEFAULT_OUTPUT = CERTIFICATES / "selected_su5_qutrit_polarization_data.attempt.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_su5_qutrit_polarization.py"
OMEGA = complex(-0.5, math.sqrt(3) / 2.0)
TOL = 1e-10


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def encode_scalar(value: complex) -> float | list[float]:
    real = 0.0 if abs(value.real) < TOL else value.real
    imag = 0.0 if abs(value.imag) < TOL else value.imag
    if imag == 0.0:
        return real
    return [real, imag]


def encode(value: Any) -> Any:
    if isinstance(value, complex):
        return encode_scalar(value)
    if isinstance(value, list):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    return value


def identity() -> list[list[complex]]:
    return [[1 + 0j if row == col else 0j for col in range(3)] for row in range(3)]


def clock() -> list[list[complex]]:
    return [[OMEGA**row if row == col else 0j for col in range(3)] for row in range(3)]


def shift() -> list[list[complex]]:
    return [[1 + 0j if row == (col + 1) % 3 else 0j for col in range(3)] for row in range(3)]


def fourier() -> list[list[complex]]:
    scale = 1.0 / math.sqrt(3)
    return [[OMEGA ** (row * col) * scale for col in range(3)] for row in range(3)]


def dagger(matrix: list[list[complex]]) -> list[list[complex]]:
    return [[matrix[col][row].conjugate() for col in range(3)] for row in range(3)]


def matmul(
    left: list[list[complex]],
    right: list[list[complex]],
) -> list[list[complex]]:
    return [
        [sum(left[row][mid] * right[mid][col] for mid in range(3)) for col in range(3)]
        for row in range(3)
    ]


def parse_report(output: str) -> dict[str, Any]:
    match = re.search(r"polarization_validation_report=(\{.*\})", output)
    if not match:
        return {}
    return json.loads(match.group(1))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "report": parse_report(proc.stdout),
    }


def upstream_status() -> dict[str, Any]:
    block = load_json(CERTIFICATES / "iwasawa_block_factorized_twisted_packet_candidate_certificate.json")
    gerbe = load_json(CERTIFICATES / "iwasawa_discrete_gerbe_holonomy_candidate_certificate.json")
    twisted = load_json(CERTIFICATES / "iwasawa_twisted_source_packet_fill_attempt_certificate.json")
    selector_gate = load_json(CERTIFICATES / "su5_qutrit_polarization_selection_gate_certificate.json")

    selected_source_available = (
        block.get("calculation_results", {}).get("selected_source_promotion_ready") is True
        and gerbe.get("verdict", {}).get("selection_remains_open") is False
        and twisted.get("verdict", {}).get("promotion_packet_passes") is True
    )
    finite_sector_projectors_filled = (
        twisted.get("filled_fields", {}).get("block_factorized_sector_maps") is True
    )
    selected_projector_retention_filled = (
        twisted.get("unfilled_fields", {}).get(
            "selected_twisted_projector_retention_for_selected_source"
        )
        is False
    )
    return {
        "block_factorized_candidate_valid": block.get("calculation_results", {}).get(
            "block_factorized_candidate_valid"
        )
        is True,
        "block_factorized_selected_source_ready": block.get("calculation_results", {}).get(
            "selected_source_promotion_ready"
        )
        is True,
        "gerbe_candidate_map_closed": gerbe.get("verdict", {}).get("candidate_holonomy_map_closed")
        is True,
        "gerbe_selection_remains_open": gerbe.get("verdict", {}).get("selection_remains_open")
        is True,
        "twisted_packet_selected_source_filled": twisted.get("verdict", {}).get(
            "promotion_packet_passes"
        )
        is True,
        "finite_block_factorized_sector_projectors_filled": finite_sector_projectors_filled,
        "selected_projector_retention_filled": selected_projector_retention_filled,
        "sector_projectors_filled": (
            finite_sector_projectors_filled and selected_projector_retention_filled
        ),
        "prior_selector_gate_proved_from_current_data": selector_gate.get("verdict", {}).get(
            "sector_polarization_selection_proved_from_current_data"
        )
        is True,
        "selected_source_available": selected_source_available,
    }


def build_attempt_packet(status: dict[str, Any]) -> dict[str, Any]:
    selected_source_available = status["selected_source_available"]
    candidate_role = "SELECTED_DATA" if selected_source_available else "UNSELECTED_FIXTURE"
    selected_by_mtt = bool(selected_source_available)
    fixture_only = not selected_by_mtt
    z = clock()
    x = shift()
    f = fourier()
    f_dag = dagger(f)

    return encode(
        {
            "schema": "SelectedSU5QutritPolarizationData.v1",
            "status": (
                "SELECTED_DATA_ATTEMPT"
                if selected_source_available
                else "UNSELECTED_FIXTURE_STRONGEST_CURRENT_ROUTE"
            ),
            "candidate_role": candidate_role,
            "purpose": (
                "Attempted fill from the block-factorized qutrit/twisted-family route. "
                "Finite transport is supplied; selected source promotion is inherited only "
                "if upstream gerbe/zero-mode certificates close."
            ),
            "source": {
                "source_kind": "selected_gerbe_twisted_bundle",
                "source_certificate": (
                    "iwasawa_block_factorized_twisted_packet_candidate_certificate.json; "
                    "iwasawa_discrete_gerbe_holonomy_candidate_certificate.json; "
                    "qutrit_polarization_transport_lemma_certificate.json"
                ),
                "selected_by_mtt": selected_by_mtt,
                "fixture_only": fixture_only,
                "uses_observed_flavor_inputs": False,
                "uses_benchmark_flavor_inputs": False,
                "why_not_selected_if_fixture": (
                    None
                    if selected_source_available
                    else "The qutrit/twisted-family route is finite and validated, but selected gerbe source promotion, sector projectors, and zero-mode bases remain open."
                ),
            },
            "upstream_status": status,
            "sector_basis_data": {
                "10_M": {
                    "basis_matrix_U10": identity(),
                    "L2_metric": identity(),
                    "selected_operator_or_projector": "qutrit family block in clock-polarized frame",
                    "polarization": "clock",
                    "clock_operator_matrix_in_basis": z,
                    "shift_operator_matrix_in_basis": x,
                    "source_certificate": "qutrit_polarization_transport_lemma_certificate.json",
                },
                "bar5_M": {
                    "basis_matrix_Ubar5": f,
                    "L2_metric": identity(),
                    "selected_operator_or_projector": "qutrit family block in shift-polarized frame",
                    "polarization": "shift",
                    "clock_operator_matrix_in_basis": matmul(matmul(f_dag, z), f),
                    "shift_operator_matrix_in_basis": matmul(matmul(f_dag, x), f),
                    "source_certificate": "qutrit_polarization_transport_lemma_certificate.json",
                },
            },
            "shared_family_frame": {
                "coordinate_frame_certified_common": True,
                "cross_pairing_metric_10_bar5": identity(),
                "source_certificate": "finite qutrit carrier shared-family frame; selected source open",
            },
            "acceptance_tests": {
                "U10_unitary_in_selected_metric": True,
                "Ubar5_unitary_in_selected_metric": True,
                "relative_transport_equals_F_mod_rephase_permutation": True,
                "orientation_selects_F_not_F_conjugate": True,
                "derived_without_observed_flavor_inputs": True,
            },
            "guardrails": {
                "do_not_fill_from_CKM_or_mass_data": True,
                "do_not_treat_exterior_square_duality_as_Fourier_transport": True,
                "do_not_use_common_Fourier_basis_change_as_physical_mixing": True,
            },
        }
    )


def analyze(output: Path) -> dict[str, Any]:
    status = upstream_status()
    packet = build_attempt_packet(status)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    validator = run_validator(output)
    return {
        "calculation": "SelectedSU5QutritPolarizationPacketFillAttempt",
        "output_packet": str(output.relative_to(ROOT)),
        "upstream_status": status,
        "packet_status": packet.get("status"),
        "candidate_role": packet.get("candidate_role"),
        "validator": validator,
        "verdict": {
            "finite_packet_constructed": True,
            "validator_exit_code": validator["exit_code"],
            "validator_passes_finite_algebra": validator["exit_code"] == 0,
            "orientation": validator["report"].get("orientation_mod_rephase_permutation"),
            "promotes_to_selected_heavy_link_input": validator["report"].get(
                "promotes_to_selected_heavy_link_input"
            )
            is True,
            "selected_source_available": status["selected_source_available"],
            "next_required_input": (
                "selected gerbe/twisted-bundle source promotion with selected projector retention, "
                "or selected monad/Cech/Galerkin zero-mode U_10,U_bar5 data"
            ),
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="attempt packet path",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = analyze(args.output.resolve())
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["validator"]["exit_code"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
