"""Analyze what the Route C branch smoke dotD data can and cannot determine.

The branch-smoke package supplies finite D_E, Green, and dotD response data.
It does not supply the sector-resolved trilinear overlap tensors needed to turn
horizontal zero-mode responses into C1 Yukawa matrices.  This script makes that
remaining dependence explicit and tests the universal-tensor special case.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SMOKE_ROOT = ROOT / "candidate_data" / "iwasawa_route_c_branch_smoke"
OUT = ROOT / "candidate_data" / "iwasawa_route_c_smoke_c1_dependency.candidate.json"
CERT = ROOT / "certificates" / "iwasawa_route_c_smoke_c1_dependency_certificate.json"

BRANCHES = ("current_q79_orientation", "conjugate_q369_orientation")
FAMILY_SLOTS = ("Q", "u", "d", "L", "e", "N")
SECTOR_SLOTS = {
    "u": ("Q", "u", "H"),
    "d": ("Q", "d", "Hdagger"),
    "e": ("L", "e", "Hdagger"),
    "nuD": ("L", "N", "H"),
}
HEAVY_ROWS = (0, 1)
HEAVY_COL = 2
TOL = 1e-12


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def to_complex(value: Any) -> complex:
    if isinstance(value, bool):
        raise TypeError("boolean is not a scalar")
    if isinstance(value, (int, float)):
        return complex(value)
    if isinstance(value, list) and len(value) == 2:
        return complex(float(value[0]), float(value[1]))
    raise TypeError(f"unsupported scalar {value!r}")


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
    if isinstance(value, tuple):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    return value


def read_dotd(branch: str) -> dict[str, Any]:
    return load_json(SMOKE_ROOT / branch / "dotd_response.candidate.json")


def family_response_coefficients(slot: dict[str, Any]) -> list[complex]:
    responses = slot.get("horizontal_response_vectors", [])
    if len(responses) != 3:
        raise ValueError("family slot must have three response vectors")
    coeffs = []
    for vector in responses:
        if len(vector) != 4:
            raise ValueError("family response vector must have dimension four")
        coeffs.append(to_complex(vector[3]))
    return coeffs


def higgs_response_coefficient(slot: dict[str, Any]) -> complex:
    responses = slot.get("horizontal_response_vectors", [])
    if len(responses) != 1 or len(responses[0]) != 2:
        raise ValueError("H slot must have one two-component response vector")
    return to_complex(responses[0][1])


def approx_equal(left: complex, right: complex) -> bool:
    return abs(left - right) < TOL


def all_family_slots_identical(coefficients: dict[str, list[complex]]) -> bool:
    baseline = coefficients["Q"]
    return all(
        all(approx_equal(a, b) for a, b in zip(baseline, coefficients[slot]))
        for slot in FAMILY_SLOTS
    )


def symbolic_matrix_terms(sector: str, left: str, right: str, higgs: str) -> dict[str, Any]:
    left_symbol = f"{left}c"
    right_symbol = f"{right}c"
    h_symbol = "Hc"
    h_zero = "H0" if higgs == "H" else "Hdagger0"
    h_comp = h_symbol if higgs == "H" else "Hdagger_c"

    return {
        "left_zero_mode_response": (
            f"B_{sector},L[i,j] = dotPsi_{left}[i,{left_symbol}] "
            f"* T_{sector}[{left_symbol}, j, {h_zero}]"
        ),
        "right_zero_mode_response": (
            f"B_{sector},R[i,j] = dotPsi_{right}[j,{right_symbol}] "
            f"* T_{sector}[i, {right_symbol}, {h_zero}]"
        ),
        "higgs_zero_mode_response": (
            f"B_{sector},H[i,j] = dotPsi_H[{h_comp}] "
            f"* T_{sector}[i, j, {h_comp}]"
        ),
        "not_determined_by_dotD": [
            "theta_overlap_variation",
            "explicit_vertex",
            "basis_connection unless a selected non-horizontal convention is supplied",
        ],
    }


def heavy_link_formula(
    sector: str,
    left: str,
    right: str,
    higgs: str,
    left_coeffs: list[complex],
    right_coeffs: list[complex],
    h_coeff: complex,
) -> list[dict[str, Any]]:
    h_zero = "H0" if higgs == "H" else "Hdagger0"
    h_comp = "Hc" if higgs == "H" else "Hdagger_c"
    result = []
    for row in HEAVY_ROWS:
        result.append(
            {
                "entry": f"M_{sector}[{row + 1},3]",
                "row_index_zero_based": row,
                "formula": (
                    f"{encode_scalar(left_coeffs[row])} * T_{sector}[{left}c,3,{h_zero}]"
                    f" + {encode_scalar(right_coeffs[HEAVY_COL])} * T_{sector}[{row + 1},{right}c,{h_zero}]"
                    f" + {encode_scalar(h_coeff)} * T_{sector}[{row + 1},3,{h_comp}]"
                    " + theta/vertex/basis terms if selected nonzero"
                ),
                "known_coefficients": {
                    "left_response": left_coeffs[row],
                    "right_response": right_coeffs[HEAVY_COL],
                    "higgs_response": h_coeff,
                },
                "unknown_overlap_slots": [
                    f"T_{sector}[{left}c,3,{h_zero}]",
                    f"T_{sector}[{row + 1},{right}c,{h_zero}]",
                    f"T_{sector}[{row + 1},3,{h_comp}]",
                ],
            }
        )
    return result


def branch_report(branch: str) -> dict[str, Any]:
    dotd = read_dotd(branch)
    slots = dotd["dotd_response_slots"]
    family_coeffs = {
        slot: family_response_coefficients(slots[slot]) for slot in FAMILY_SLOTS
    }
    h_coeff = higgs_response_coefficient(slots["H"])
    family_identical = all_family_slots_identical(family_coeffs)

    sectors: dict[str, Any] = {}
    for sector, (left, right, higgs) in SECTOR_SLOTS.items():
        right_slot = right
        sectors[sector] = {
            "slots": {
                "left": left,
                "right": right,
                "higgs": higgs,
            },
            "symbolic_terms": symbolic_matrix_terms(sector, left, right_slot, higgs),
            "unknown_complex_overlap_slots_if_theta_vertex_basis_absent": {
                "full_matrix": 15,
                "heavy_link_entries_13_23": 5,
                "why": (
                    "3 left-complement slots, 3 right-complement slots, "
                    "and 9 Higgs-complement slots determine a full 3x3 "
                    "response matrix from dotD; heavy links need one left, "
                    "two right, and two Higgs slots."
                ),
            },
            "heavy_link_dependency": heavy_link_formula(
                sector,
                left,
                right_slot,
                higgs,
                family_coeffs[left],
                family_coeffs[right_slot],
                h_coeff,
            ),
        }

    universal_tensor = {
        "assumption": (
            "T_u = T_d and theta/vertex/basis terms agree between u and d; "
            "this is the bare universal E6 tensor case without selected SU(5) "
            "sector splitting or basis transport."
        ),
        "family_dotD_coefficients_identical_for_Q_u_d": family_identical,
        "Delta_t_ud_for_heavy_links": [0.0, 0.0] if family_identical else None,
        "leading_ckm_heavy_link_from_smoke_dotD_only": False if family_identical else None,
        "verdict": (
            "universal tensor gives M_u = M_d, so Route C smoke dotD alone "
            "cannot supply the character-trivial CKM heavy link"
            if family_identical
            else "family coefficients differ, so universal tensor must be evaluated"
        ),
    }

    return {
        "branch_packet": dotd.get("branch_packet", {}),
        "response_coefficients": {
            "family_complement_coefficients": family_coeffs,
            "higgs_complement_coefficient": h_coeff,
            "family_slots_identical": family_identical,
        },
        "sectors": sectors,
        "universal_tensor_test": universal_tensor,
    }


def conjugate_check(reports: dict[str, Any]) -> dict[str, Any]:
    current = reports["current_q79_orientation"]["response_coefficients"]
    conjugate = reports["conjugate_q369_orientation"]["response_coefficients"]
    current_q = current["family_complement_coefficients"]["Q"]
    conjugate_q = conjugate["family_complement_coefficients"]["Q"]
    current_h = current["higgs_complement_coefficient"]
    conjugate_h = conjugate["higgs_complement_coefficient"]
    family_conjugate = all(
        approx_equal(a.conjugate(), b) for a, b in zip(current_q, conjugate_q)
    )
    higgs_conjugate = approx_equal(current_h.conjugate(), conjugate_h)
    return {
        "q79_and_q369_response_coefficients_are_conjugate": (
            family_conjugate and higgs_conjugate
        ),
        "family_q_coefficients": {
            "q79": current_q,
            "q369": conjugate_q,
        },
        "higgs_coefficients": {
            "q79": current_h,
            "q369": conjugate_h,
        },
    }


def build_report() -> dict[str, Any]:
    reports = {branch: branch_report(branch) for branch in BRANCHES}
    branch_guard = conjugate_check(reports)
    all_universal_zero = all(
        report["universal_tensor_test"]["leading_ckm_heavy_link_from_smoke_dotD_only"]
        is False
        for report in reports.values()
    )
    result = {
        "candidate": "IwasawaRouteCSmokeC1Dependency",
        "status": "SYMBOLIC_DEPENDENCY_REDUCED_NUMERIC_VALUES_OPEN",
        "generated_by": "scripts/analyze_iwasawa_route_c_smoke_c1_dependency.py",
        "inputs": {
            "branch_smoke_candidate_data": "candidate_data/iwasawa_route_c_branch_smoke",
            "uses_observed_flavor_data": False,
            "uses_execution_ii_benchmarks": False,
        },
        "branches": reports,
        "conjugate_branch_check": branch_guard,
        "calculation_results": {
            "branch_smoke_dotD_response_is_nonzero": True,
            "branch_pair_coefficients_are_conjugate": branch_guard[
                "q79_and_q369_response_coefficients_are_conjugate"
            ],
            "full_matrix_overlap_unknowns_per_sector": 15,
            "heavy_link_overlap_unknowns_per_sector": 5,
            "universal_tensor_case_gives_Delta_t_zero": all_universal_zero,
            "route_c_smoke_dotD_alone_closes_ckm_heavy_link": False,
            "new_required_selected_data": [
                "sector-resolved trilinear overlap tensors T_s",
                "or selected SU(5) 10/bar5/H basis transport",
                "or selected theta/vertex/basis primitive terms",
            ],
        },
        "what_this_closes": {
            "dotD_to_C1_dependency_map": True,
            "conjugate_branch_response_check": True,
            "universal_E6_tensor_only_ckm_heavy_link_no_go": True,
        },
        "still_open": {
            "selected_sector_overlap_tensors": True,
            "selected_basis_transport_or_projection": True,
            "numeric_C1_response_matrices": True,
            "selected_CKM_heavy_link_packet": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_C1_response": False,
            "claims_selected_overlap_tensor": False,
            "claims_CKM_angles_or_Jarlskog": False,
            "claims_yukawa_magnitudes": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "hard_next_step_status": (
                "Route C smoke dotD reaches the primitive-contraction boundary: "
                "the missing object is now the selected sector-resolved overlap "
                "tensor or selected SU(5) basis transport."
            ),
            "recommended_next_calculation": (
                "derive or search for the selected 10_M/bar5_M/H projection tensor "
                "that distinguishes u from d while preserving the conjugate branch "
                "pair"
            ),
        },
    }
    return encode(result)


def write_outputs(report: dict[str, Any]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    cert = {
        "certificate": "IwasawaRouteCSmokeC1DependencyCertificate",
        "status": report["status"],
        "candidate_data": str(OUT.relative_to(ROOT)).replace("\\", "/"),
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write candidate and certificate files")
    args = parser.parse_args()

    report = build_report()
    if args.write:
        write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
