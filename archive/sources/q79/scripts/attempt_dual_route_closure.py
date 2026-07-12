"""Attempt both forward routes after the SU(5) block-orientation split.

Route A asks whether the monolithic high-scale SU(5)/E6 tensor source is
available now.

Route B asks whether the block-factorized sector-resolved route is structurally
capable of producing a nonzero CKM heavy-link once selected overlap data are
supplied.  It computes the finite linear map

    selected overlap differences -> Delta_t = (M_d13-M_u13, M_d23-M_u23)

from the current Route C branch-smoke dotD coefficients.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
OUT = ROOT / "candidate_data" / "dual_route_closure_attempt.candidate.json"
CERT = CERTIFICATES / "dual_route_closure_attempt_certificate.json"
TOL = 1e-12

BRANCHES = ("current_q79_orientation", "conjugate_q369_orientation")
DIFFERENCE_VARIABLES = (
    "A_left_delta",
    "B_right_row1_delta",
    "B_right_row2_delta",
    "C_higgs_row1_delta",
    "C_higgs_row2_delta",
)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_cert(name: str) -> dict[str, Any]:
    return load_json(CERTIFICATES / name)


def to_complex(value: Any) -> complex:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return complex(value)
    if isinstance(value, list) and len(value) == 2:
        return complex(float(value[0]), float(value[1]))
    raise TypeError(f"unsupported complex scalar {value!r}")


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


def rank_complex(matrix: list[list[complex]]) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = None
        for row in range(rank, rows):
            if abs(work[row][col]) > TOL:
                pivot = row
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][col]
        work[rank] = [entry / scale for entry in work[rank]]
        for row in range(rows):
            if row == rank or abs(work[row][col]) <= TOL:
                continue
            factor = work[row][col]
            work[row] = [entry - factor * work[rank][idx] for idx, entry in enumerate(work[row])]
        rank += 1
        if rank == rows:
            break
    return rank


def branch_dependency(branch_name: str, dependency: dict[str, Any]) -> dict[str, Any]:
    branch = dependency["branches"][branch_name]
    u_entries = branch["sectors"]["u"]["heavy_link_dependency"]
    d_entries = branch["sectors"]["d"]["heavy_link_dependency"]

    # The smoke package has identical Q/u/d family coefficients, but we read
    # the u-sector symbols to keep the calculation tied to the generated data.
    row1 = u_entries[0]["known_coefficients"]
    row2 = u_entries[1]["known_coefficients"]
    left_0 = to_complex(row1["left_response"])
    left_1 = to_complex(row2["left_response"])
    right = to_complex(row1["right_response"])
    higgs = to_complex(row1["higgs_response"])

    linear_map = [
        [left_0, right, 0j, higgs, 0j],
        [left_1, 0j, right, 0j, higgs],
    ]
    rank = rank_complex(linear_map)
    variable_count = len(DIFFERENCE_VARIABLES)
    nullity = variable_count - rank

    same_coefficients_between_u_d = (
        u_entries[0]["known_coefficients"] == d_entries[0]["known_coefficients"]
        and u_entries[1]["known_coefficients"] == d_entries[1]["known_coefficients"]
    )

    # These are unselected algebraic witnesses.  They prove structural
    # reachability of two independent heavy-link directions, not a prediction.
    witness_delta_13 = {
        "description": "sets only B_right_row1_delta = 1/right_response",
        "overlap_differences": {
            "A_left_delta": 0j,
            "B_right_row1_delta": 1.0 / right,
            "B_right_row2_delta": 0j,
            "C_higgs_row1_delta": 0j,
            "C_higgs_row2_delta": 0j,
        },
        "Delta_t": [1.0 + 0j, 0j],
    }
    witness_delta_23 = {
        "description": "sets only B_right_row2_delta = 1/right_response",
        "overlap_differences": {
            "A_left_delta": 0j,
            "B_right_row1_delta": 0j,
            "B_right_row2_delta": 1.0 / right,
            "C_higgs_row1_delta": 0j,
            "C_higgs_row2_delta": 0j,
        },
        "Delta_t": [0j, 1.0 + 0j],
    }

    return {
        "branch": branch_name,
        "branch_packet": branch["branch_packet"],
        "coefficient_matrix_rows_Delta13_Delta23": linear_map,
        "difference_variables": list(DIFFERENCE_VARIABLES),
        "rank_over_complex": rank,
        "nullity_over_complex": nullity,
        "same_coefficients_between_u_and_d": same_coefficients_between_u_d,
        "universal_equal_overlap_case_delta_t": [0j, 0j],
        "nonzero_delta_t_structurally_reachable": rank == 2,
        "algebraic_witnesses_unselected": {
            "Delta_t_10": witness_delta_13,
            "Delta_t_01": witness_delta_23,
        },
        "interpretation": (
            "Route B is not structurally dead: selected sector-resolved overlap "
            "differences can generate a two-complex-dimensional heavy-link target. "
            "However, the current corpus supplies none of those selected overlap "
            "differences, so no value is predicted."
        ),
    }


def analyze() -> dict[str, Any]:
    projection = load_cert("su5_projection_tensor_derivation_attempt_certificate.json")
    source_attempt = load_cert("selected_su5_source_proof_attempt_certificate.json")
    split = load_cert("su5_block_orientation_route_split_certificate.json")
    dependency = load_json(ROOT / "candidate_data" / "iwasawa_route_c_smoke_c1_dependency.candidate.json")
    missing = load_cert("selected_missing_data_calculation_certificate.json")

    route_a_closed = (
        projection.get("calculation_results", {}).get("finite_projection_tensor_derived") is True
        and source_attempt.get("verdict", {}).get("remaining_proof_closed") is True
        and split.get("calculation_results", {}).get("selected_source_closed") is True
    )
    route_a = {
        "route": "A_high_scale_SU5_E6_multiplet_source",
        "status": "BLOCKED_SELECTED_HIGH_SCALE_SOURCE_NOT_FOUND",
        "finite_tensor_available": projection.get("calculation_results", {}).get(
            "finite_projection_tensor_derived"
        )
        is True,
        "selected_source_closed": source_attempt.get("verdict", {}).get(
            "remaining_proof_closed"
        )
        is True,
        "block_packets_source_monolithic_tensor": split.get("calculation_results", {}).get(
            "monolithic_su5_tensor_inherits_from_block_route"
        )
        is True,
        "closes_now": route_a_closed,
        "next_input": (
            "selected high-scale SU(5)/E6 multiplet source proving coherent "
            "10_M and bar5_M polarizations plus compatible Higgs/projection data"
        ),
    }

    route_b_branches = {
        branch: branch_dependency(branch, dependency) for branch in BRANCHES
    }
    route_b_rank_ok = all(
        item["rank_over_complex"] == 2 and item["nonzero_delta_t_structurally_reachable"]
        for item in route_b_branches.values()
    )
    route_b_selected_values_available = (
        missing.get("computed_result", {}).get("selected_dotd_response_slot_data_found") is True
        and missing.get("computed_result", {}).get("missing_primitive_contraction_matrices", 24) == 0
    )
    route_b = {
        "route": "B_block_factorized_sector_resolved_C1",
        "status": (
            "STRUCTURALLY_CAPABLE_VALUES_OPEN"
            if route_b_rank_ok
            else "STRUCTURALLY_BLOCKED"
        ),
        "branches": route_b_branches,
        "closes_now": route_b_rank_ok and route_b_selected_values_available,
        "selected_values_available": route_b_selected_values_available,
        "selected_data_still_missing": [
            "selected sector-resolved overlap differences for u versus d",
            "selected theta/vertex/basis primitive heavy-link differences, if nonzero",
            "selected D_E/dotD source flags rather than Route C smoke flags",
            "selected C1 primitive contraction matrices or reduced heavy-link scalars",
        ],
    }

    both_routes_close_now = route_a["closes_now"] or route_b["closes_now"]
    return encode(
        {
            "candidate": "DualRouteClosureAttempt",
            "status": "DUAL_ROUTE_ATTEMPT_REDUCED_ROUTE_B_TO_RANK_TWO_LINEAR_MAP_VALUES_OPEN",
            "generated_by": "scripts/attempt_dual_route_closure.py",
            "routes": {
                "A_high_scale_SU5_E6_multiplet_source": route_a,
                "B_block_factorized_sector_resolved_C1": route_b,
            },
            "calculation_results": {
                "route_A_high_scale_tensor_closes_now": route_a["closes_now"],
                "route_B_sector_resolved_linear_map_rank_two": route_b_rank_ok,
                "route_B_nonzero_delta_t_structurally_reachable": route_b_rank_ok,
                "route_B_selected_values_available": route_b_selected_values_available,
                "both_routes_close_now": both_routes_close_now,
                "first_remaining_numeric_object": (
                    "five complex selected overlap-difference slots for u versus d "
                    "heavy links, or an equivalent selected primitive C1 heavy-link packet"
                ),
                "minimal_route_B_difference_variables": list(DIFFERENCE_VARIABLES),
            },
            "what_this_closes": {
                "route_A_current_blocker_identified": True,
                "route_B_linear_dependency_computed": True,
                "route_B_structural_nonzero_CKM_heavy_link_possible": route_b_rank_ok,
                "universal_equal_overlap_block_case_zero_confirmed": True,
                "selected_values_not_fitted_or_invented": True,
            },
            "still_open": {
                "selected_high_scale_SU5_E6_source": not route_a["closes_now"],
                "selected_route_B_overlap_differences": not route_b_selected_values_available,
                "selected_C1_heavy_link_packet": True,
                "selected_yukawa_magnitudes": True,
                "full_SM_closure": True,
            },
            "guardrails": {
                "claims_route_A_selected_source": False,
                "claims_route_B_selected_values": False,
                "uses_algebraic_witnesses_as_predictions": False,
                "uses_observed_flavor_data": False,
                "uses_benchmark_flavor_entries": False,
                "claims_full_SM_closure": False,
            },
            "verdict": {
                "attempted_both_routes": True,
                "route_A_result": "finite tensor remains conditional; selected high-scale source absent",
                "route_B_result": (
                    "sector-resolved block route has rank-two access to Delta_t, "
                    "so it can in principle generate CKM heavy-link mismatch once "
                    "selected overlap/C1 primitives are supplied"
                ),
                "next_step": (
                    "construct a selected Route B heavy-link primitive packet: "
                    "the five u-d overlap differences A_left, B_right_row1, "
                    "B_right_row2, C_higgs_row1, C_higgs_row2, plus any selected "
                    "theta/vertex/basis terms."
                ),
            },
        }
    )


def write_outputs(report: dict[str, Any]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    cert = {
        "certificate": "DualRouteClosureAttemptCertificate",
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
    report = analyze()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
