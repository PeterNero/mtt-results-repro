"""Calculate the current Route B final missing heavy-link object.

This script uses the strongest current SU(5) qutrit polarization packet:

    U_10 = I_3,
    U_bar5 = F.

It converts the relative transport U_10^dagger U_bar5 into the Route B
heavy-link packet format.  In the current repository this is a conditional
exact fixture, not selected MTT data, because the upstream polarization packet
is still explicitly unselected.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
POLARIZATION_PACKET = ROOT / "certificates" / "selected_su5_qutrit_polarization_data.attempt.json"
ROUTE_B_CALCULATOR = ROOT / "scripts" / "compute_route_b_heavy_link_delta_t.py"
OUT = ROOT / "candidate_data" / "route_b_final_missing_object_attempt.candidate.json"
CERT = ROOT / "certificates" / "route_b_final_missing_object_attempt_certificate.json"
TOL = 1e-10
HEAVY_LINKS = ((0, 2), (1, 2))


Matrix = list[list[complex]]


def parse_complex(value: Any) -> complex:
    if isinstance(value, bool):
        raise TypeError(f"booleans are not numeric entries: {value!r}")
    if isinstance(value, (int, float)):
        return complex(value)
    if isinstance(value, str):
        return complex(value.replace("i", "j"))
    if isinstance(value, list) and len(value) == 2:
        return complex(float(value[0]), float(value[1]))
    raise TypeError(f"cannot parse complex entry {value!r}")


def parse_matrix(raw: list[list[Any]]) -> Matrix:
    return [[parse_complex(entry) for entry in row] for row in raw]


def identity() -> Matrix:
    return [[1.0 + 0j if row == col else 0j for col in range(3)] for row in range(3)]


def dagger(matrix: Matrix) -> Matrix:
    return [[matrix[col][row].conjugate() for col in range(3)] for row in range(3)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sum(left[row][mid] * right[mid][col] for mid in range(3)) for col in range(3)]
        for row in range(3)
    ]


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return [[left[row][col] - right[row][col] for col in range(3)] for row in range(3)]


def max_abs(matrix: Matrix) -> float:
    return max(abs(entry) for row in matrix for entry in row)


def is_unitary(matrix: Matrix) -> bool:
    return max_abs(matrix_sub(matmul(dagger(matrix), matrix), identity())) < TOL


def heavy_vector(matrix: Matrix) -> list[complex]:
    return [matrix[row][col] for row, col in HEAVY_LINKS]


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


def load_route_b_calculator() -> Any:
    spec = importlib.util.spec_from_file_location("route_b_calculator", ROUTE_B_CALCULATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {ROUTE_B_CALCULATOR}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def relative_transport_from_packet(packet: dict[str, Any]) -> tuple[Matrix, Matrix, Matrix]:
    sector_data = packet["sector_basis_data"]
    u10 = parse_matrix(sector_data["10_M"]["basis_matrix_U10"])
    ubar5 = parse_matrix(sector_data["bar5_M"]["basis_matrix_Ubar5"])
    return u10, ubar5, matmul(dagger(u10), ubar5)


def route_b_packet(
    selected_source: bool, delta_t: list[complex], source_status: str
) -> dict[str, Any]:
    role = "SELECTED_DATA" if selected_source else "UNSELECTED_FIXTURE"
    status = (
        "CALCULATED_SELECTED_ROUTE_B_FINAL_OBJECT"
        if selected_source
        else "CALCULATED_CONDITIONAL_EXACT_FIXTURE_SELECTION_OPEN"
    )
    return {
        "schema": "RouteBHeavyLinkOverlapDifferencePacket.v1",
        "status": status,
        "candidate_role": role,
        "branch": "current_q79_orientation",
        "source": {
            "source_kind": "selected_su5_qutrit_polarization_packet_attempt",
            "source_certificate": "selected_su5_qutrit_polarization_data.attempt.json",
            "source_status": source_status,
            "selected_by_mtt": selected_source,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "overlap_differences": {
            "A_left_delta": 0.0,
            "B_right_row1_delta": 0.0,
            "B_right_row2_delta": 0.0,
            "C_higgs_row1_delta": 0.0,
            "C_higgs_row2_delta": 0.0,
        },
        "extra_delta_t_terms": {
            "theta_overlap_variation_delta": [0.0, 0.0],
            "explicit_vertex_delta": [0.0, 0.0],
            "basis_connection_delta": encode(delta_t),
        },
    }


def calculate() -> dict[str, Any]:
    packet = json.loads(POLARIZATION_PACKET.read_text(encoding="utf-8"))
    source = packet.get("source", {})
    upstream = packet.get("upstream_status", {})
    selected_source = source.get("selected_by_mtt") is True
    u10, ubar5, relative = relative_transport_from_packet(packet)
    delta_t = heavy_vector(relative)
    route_packet = route_b_packet(selected_source, delta_t, str(packet.get("status")))

    route_b = load_route_b_calculator()
    route_b_report, route_b_failures = route_b.compute(route_packet)

    status = (
        "ROUTE_B_FINAL_MISSING_OBJECT_CALCULATED_SELECTED"
        if route_b_report["promotes_to_selected_CKM_heavy_link_input"]
        else "ROUTE_B_FINAL_MISSING_OBJECT_CALCULATED_CONDITIONAL_SELECTION_OPEN"
    )

    exact = {
        "omega": "exp(2*pi*i/3)",
        "Delta_t_symbolic": ["1/sqrt(3)", "omega^2/sqrt(3)"],
        "Delta_t_numeric": delta_t,
        "overlap_differences": route_packet["overlap_differences"],
        "theta_overlap_variation_delta": [0.0, 0.0],
        "explicit_vertex_delta": [0.0, 0.0],
        "basis_connection_delta": delta_t,
    }

    report = {
        "candidate": "RouteBFinalMissingObjectCalculationAttempt",
        "status": status,
        "generated_by": "scripts/calculate_route_b_final_missing_object.py",
        "inputs": {
            "polarization_packet": str(POLARIZATION_PACKET.relative_to(ROOT)),
            "route_b_calculator": str(ROUTE_B_CALCULATOR.relative_to(ROOT)),
            "source_status": packet.get("status"),
            "source_selected_by_mtt": selected_source,
            "candidate_role": route_packet["candidate_role"],
        },
        "calculation_results": {
            "U10_unitary": is_unitary(u10),
            "Ubar5_unitary": is_unitary(ubar5),
            "relative_transport": relative,
            "relative_transport_rule": "U_10^dagger U_bar5 = F",
            "heavy_link_entries": "(1,3),(2,3) in one-based notation",
            "final_missing_object_if_selected": exact,
            "route_b_packet_promotes_to_selected_input": route_b_report[
                "promotes_to_selected_CKM_heavy_link_input"
            ],
            "route_b_packet_structurally_nonzero": route_b_report[
                "leading_noncommutation_structurally_nonzero"
            ],
            "route_b_failures": route_b_failures,
        },
        "route_b_overlap_difference_packet": route_packet,
        "route_b_calculator_report": route_b_report,
        "what_this_calculates": {
            "five_overlap_difference_slots": True,
            "selected_or_zero_extra_term_slots": True,
            "Delta_t_from_current_strongest_transport_packet": True,
            "exact_q79_route_b_candidate": True,
        },
        "still_open": {
            "selected_source_promotion": not selected_source,
            "selected_gerbe_or_zero_mode_origin_for_U10_Ubar5": not selected_source,
            "selected_overlap_kernel_prefactor": True,
            "canonical_kinetic_metrics": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_data_without_source": selected_source is False
            and route_b_report["promotes_to_selected_CKM_heavy_link_input"],
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "claims_CKM_angles_or_Jarlskog": False,
            "claims_yukawa_magnitudes": False,
            "claims_full_SM_closure": False,
        },
        "upstream_status": upstream,
        "verdict": {
            "exact_final_object_calculated_conditionally": True,
            "selected_final_object_calculated_now": route_b_report[
                "promotes_to_selected_CKM_heavy_link_input"
            ],
            "selected_promotion_blocker": (
                "The current U_10=I_3, U_bar5=F packet is an UNSELECTED_FIXTURE. "
                "Close selected gerbe/twisted-bundle source promotion or derive "
                "U_10,U_bar5 from selected monad/Cech/Galerkin zero modes."
            ),
        },
    }
    return encode(report)


def certificate_from(report: dict[str, Any]) -> dict[str, Any]:
    calc = report["calculation_results"]
    return {
        "certificate": "RouteBFinalMissingObjectCalculationAttempt",
        "status": report["status"],
        "purpose": (
            "Calculate the Route B final missing heavy-link object from the "
            "strongest current SU(5) qutrit polarization packet, while refusing "
            "selected promotion unless the source is selected."
        ),
        "depends_on": [
            "route_b_heavy_link_overlap_difference_calculator_certificate.json",
            "selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json",
            "qutrit_polarization_transport_lemma_certificate.json",
            "su5_qutrit_basis_transport_heavy_link_candidate_certificate.json",
        ],
        "analysis_script": "scripts/calculate_route_b_final_missing_object.py",
        "candidate_packet": "candidate_data/route_b_final_missing_object_attempt.candidate.json",
        "calculation_results": {
            "U10_unitary": calc["U10_unitary"],
            "Ubar5_unitary": calc["Ubar5_unitary"],
            "relative_transport_rule": calc["relative_transport_rule"],
            "Delta_t_symbolic": calc["final_missing_object_if_selected"]["Delta_t_symbolic"],
            "Delta_t_numeric": calc["final_missing_object_if_selected"]["Delta_t_numeric"],
            "overlap_differences_all_zero": all(
                value == 0.0
                for value in calc["final_missing_object_if_selected"][
                    "overlap_differences"
                ].values()
            ),
            "nonzero_slot": "basis_connection_delta",
            "route_b_packet_structurally_nonzero": calc["route_b_packet_structurally_nonzero"],
            "route_b_packet_promotes_to_selected_input": calc[
                "route_b_packet_promotes_to_selected_input"
            ],
        },
        "what_this_closes": report["what_this_calculates"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }


def main() -> int:
    report = calculate()
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(certificate_from(report), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
