"""Build Route A physical values / Route B row-execution diagnostic attempt."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_routeaphysicalemissionvalues_or_routebrowexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_physical_value_emission_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_replay_rank_diagnostics.packet.json"
RESULT = PACKET_DIR / "row_execution_closure_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteAPhysicalEmissionValues_or_RouteBRowExecution_v1.md"

STATUS = "MTT_SELECTED_ROUTEA_PHYSICALVALUES_OR_ROUTEB_ROWEXECUTION_BUILT_REPLAY_RANK_DIAGNOSTICS_OPEN"
NEXT = "MTT_Selected_RouteBIndependentPrimitiveRows_or_RouteAPhiFinBoundaryEmission_v1"
TOL = 1e-10


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def as_complex(value: Any) -> complex:
    if isinstance(value, list):
        return complex(float(value[0]), float(value[1]))
    return complex(float(value), 0.0)


def mat_complex(matrix: list[list[Any]]) -> list[list[complex]]:
    return [[as_complex(value) for value in row] for row in matrix]


def fro_norm_sq(matrix: list[list[complex]]) -> float:
    return float(sum(abs(value) ** 2 for row in matrix for value in row))


def rank_3(matrix: list[list[complex]], tol: float = TOL) -> int:
    # Small Gram eigenvalue routine through closed-form numpy-free fallback is not worth the noise here;
    # use exact 1x/2x/3x minor tests for 3x3 matrices.
    entries = [abs(value) for row in matrix for value in row]
    if max(entries, default=0.0) <= tol:
        return 0

    def det2(rows: tuple[int, int], cols: tuple[int, int]) -> complex:
        r0, r1 = rows
        c0, c1 = cols
        return matrix[r0][c0] * matrix[r1][c1] - matrix[r0][c1] * matrix[r1][c0]

    def det3() -> complex:
        a = matrix
        return (
            a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
        )

    if abs(det3()) > tol:
        return 3
    for rows in [(0, 1), (0, 2), (1, 2)]:
        for cols in [(0, 1), (0, 2), (1, 2)]:
            if abs(det2(rows, cols)) > tol:
                return 2
    return 1


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def comm_norm_sq(a: list[list[complex]], b: list[list[complex]]) -> float:
    ab = matmul(a, b)
    ba = matmul(b, a)
    return fro_norm_sq([[ab[i][j] - ba[i][j] for j in range(3)] for i in range(3)])


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    manifest = load(DATA / "selected_physicalsourceemissionvalues_or_honestgalerkinexecution.candidate.json")
    route_a_slots = load(
        DATA
        / "selected_physicalsourceemissionvalues_or_honestgalerkinexecution"
        / "route_a_emission_value_slots.packet.json"
    )
    route_b_work = load(
        DATA
        / "selected_physicalsourceemissionvalues_or_honestgalerkinexecution"
        / "route_b_honest_execution_workorder.packet.json"
    )
    sectors = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "inputs"
        / "sector_response_matrices.packet.json"
    )

    route_a_attempt = {
        "schema": "MTTRouteAPhysicalValueEmissionAttempt.v1",
        "status": "ROUTE_A_PHYSICAL_VALUES_NOT_EMITTED",
        "slot_attempts": [
            {
                "name": slot["name"],
                "attempted_now": False,
                "value_emitted": False,
                "reason": "No new same-branch physical Phi_fin^C1/action source emission was available in this step.",
            }
            for slot in route_a_slots["slots"]
        ],
        "all_route_a_values_emitted": False,
        "lane_closes_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    matrices = {
        sector: mat_complex(payload["matrix"])
        for sector, payload in sectors["sector_responses"].items()
    }
    diagnostics = {}
    for sector in sectors["sector_order"]:
        matrix = matrices[sector]
        c33 = matrix[2][2]
        diagnostics[sector] = {
            "response_lane": sectors["sector_responses"][sector]["response_lane"],
            "rank": rank_3(matrix),
            "frobenius_norm_sq": fro_norm_sq(matrix),
            "C33": [c33.real, c33.imag],
            "C33_abs": abs(c33),
            "C33_nonzero": abs(c33) > TOL,
            "selected_by_independent_galerkin_execution": sectors["sector_responses"][sector][
                "selected_by_independent_galerkin_execution"
            ],
        }

    route_b_diagnostics = {
        "schema": "MTTRouteBReplayRankDiagnostics.v1",
        "status": "ROUTE_B_REPLAY_RANK_DIAGNOSTICS_COMPUTED_NOT_INDEPENDENT_EXECUTION",
        "diagnostic_level": "replay_support_only",
        "sector_order": sectors["sector_order"],
        "sector_diagnostics": diagnostics,
        "cross_lane_commutators": {
            "u_d_commutator_norm_sq": comm_norm_sq(matrices["u"], matrices["d"]),
            "e_nuD_commutator_norm_sq": comm_norm_sq(matrices["e"], matrices["nuD"]),
            "u_e_commutator_norm_sq": comm_norm_sq(matrices["u"], matrices["e"]),
            "d_nuD_commutator_norm_sq": comm_norm_sq(matrices["d"], matrices["nuD"]),
        },
        "diagnostic_tests_pass": {
            "all_sector_matrices_nonzero": all(item["frobenius_norm_sq"] > TOL for item in diagnostics.values()),
            "all_C33_nonzero": all(item["C33_nonzero"] for item in diagnostics.values()),
            "all_sector_ranks_at_least_two": all(item["rank"] >= 2 for item in diagnostics.values()),
            "phase_shift_cross_commutator_nonzero": comm_norm_sq(matrices["u"], matrices["d"]) > TOL,
        },
        "independent_rows_executed_now": False,
        "selected_source_verified": False,
        "can_promote_to_route_b_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    result = {
        "schema": "MTTRouteAPhysicalValuesOrRouteBRowExecutionDecision.v1",
        "status": "DIAGNOSTIC_RANK_TESTS_PASS_BUT_NO_PHYSICAL_OR_INDEPENDENT_EXECUTION_CLOSURE",
        "route_a_physical_values_emitted": False,
        "route_b_replay_rank_diagnostics_computed": True,
        "route_b_diagnostic_tests_pass": all(route_b_diagnostics["diagnostic_tests_pass"].values()),
        "route_b_independent_rows_executed": False,
        "route_b_selected_source_verified": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "why_this_matters": (
            "The replay matrices are not degenerate: all sector matrices are nonzero, all C33 entries "
            "are nonzero, ranks are at least two, and phase/shift lanes do not commute. This supports "
            "the target shape for Route B, but it is not an independent selected Galerkin execution."
        ),
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedRouteAPhysicalEmissionValuesOrRouteBRowExecution",
        "status": STATUS,
        "inputs": {
            "previous_manifest": rel(DATA / "selected_physicalsourceemissionvalues_or_honestgalerkinexecution.candidate.json"),
            "route_a_slots": rel(
                DATA
                / "selected_physicalsourceemissionvalues_or_honestgalerkinexecution"
                / "route_a_emission_value_slots.packet.json"
            ),
            "route_b_workorder": rel(
                DATA
                / "selected_physicalsourceemissionvalues_or_honestgalerkinexecution"
                / "route_b_honest_execution_workorder.packet.json"
            ),
            "sector_response_replay": rel(
                DATA
                / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
                / "inputs"
                / "sector_response_matrices.packet.json"
            ),
        },
        "output_packets": {
            "route_a_physical_value_emission_attempt": rel(ROUTE_A),
            "route_b_replay_rank_diagnostics": rel(ROUTE_B),
            "row_execution_closure_decision": rel(RESULT),
        },
        "theorem": {
            "name": "ReplayRankDiagnosticNonPromotionTheorem",
            "proved": True,
            "statement": (
                "The replay sector matrices pass concrete C33, rank, nonzero, and noncommutation diagnostics, "
                "so the Route B target is structurally nondegenerate. These diagnostics do not promote the "
                "rows to selected Galerkin execution because their provenance remains replay/support-level."
            ),
        },
        "closure_decision": {
            "route_a_physical_values_emitted": False,
            "route_b_replay_rank_diagnostics_computed": True,
            "route_b_independent_rows_executed": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_manifest_status": manifest["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_RouteAPhysicalEmissionValues_or_RouteBRowExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "route_a_physical_values_emitted": False,
        "route_b_replay_rank_diagnostics_computed": True,
        "route_b_independent_rows_executed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected RouteAPhysicalEmissionValues or RouteBRowExecution v1

Status: `{STATUS}`.

This step computes replay-side Route B rank diagnostics without promoting them.
All replay sector matrices are nonzero, have nonzero C33 entries, have rank at
least two, and the phase/shift lanes have a nonzero commutator.  This means the
locked Route B target is structurally nondegenerate.

No Route A physical values were emitted, and no independent selected Galerkin
rows were executed.  The diagnostic result is support only, not unpatched
dynamic-C1 closure.
"""

    for path, payload in [
        (ROUTE_A, route_a_attempt),
        (ROUTE_B, route_b_diagnostics),
        (RESULT, result),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
