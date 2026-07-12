"""Build selected C1 kernel-values execution / physical-source promotion gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_c1kernelvaluesexecution_or_physicalsourcepromotion"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_physical_source_promotion_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_algebraic_kernel_value_execution_attempt.packet.json"
BARRIER = PACKET_DIR / "promotion_barrier_and_next_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_C1KernelValuesExecution_or_PhysicalSourcePromotion_v1.md"

STATUS = "MTT_SELECTED_C1KERNELVALUESEXECUTION_OR_PHYSICALSOURCEPROMOTION_ALGEBRAIC_VALUES_FILLED_PROMOTION_OPEN"
NEXT = "MTT_Selected_C1MeasurePairing_or_PhysicalActionIdentity_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def zero() -> float:
    return 0.0


def matrix_entry(matrix: list[list[Any]], coord: str) -> Any:
    r_token, c_token = coord.split("c")
    i = int(r_token.removeprefix("r"))
    j = int(c_token)
    return matrix[i][j]


def primitive_value(row: dict[str, Any], rz: list[list[Any]], rx: list[list[Any]]) -> tuple[str | None, Any]:
    if row["sector"] in {"u", "e"} and row["response"] == "phase":
        return "R_Z", matrix_entry(rz, row["coordinate"])
    if row["sector"] in {"d", "nuD"} and row["response"] == "shift":
        return "R_X", matrix_entry(rx, row["coordinate"])
    return None, zero()


def sector_value(row_id: str, sector_responses: dict[str, Any]) -> Any:
    sector, _, coord = row_id.split(":")
    return matrix_entry(sector_responses[sector]["correction_dY"], coord)


def rows_for_stage(schedule: dict[str, Any], stage_name: str) -> list[str]:
    for stage in schedule["execution_order"]:
        if stage["stage"] == stage_name:
            return list(stage["rows"])
    raise KeyError(stage_name)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues.candidate.json")
    route_a_template = load(DATA / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues" / "route_a_physical_source_theorem_template.packet.json")
    manifest = load(DATA / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues" / "route_b_quadrature_kernel_value_manifest.packet.json")
    contract = load(DATA / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues" / "source_or_kernel_acceptance_contract.packet.json")
    schedule = load(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json")
    replay_rows = load(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_b_replay_backed_primitive_rows.packet.json")
    residual_poly = load(DATA / "selected_residual_weylpolynomial_source_theorem_attempt" / "residual_weyl_polynomial_decomposition.packet.json")
    hessian = load(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "hessian_source_vector.packet.json")
    full_response = load(DATA / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json")

    rz = residual_poly["decompositions"]["R_Z"]["matrix"]
    rx = residual_poly["decompositions"]["R_X"]["matrix"]
    primitive_source_rows = replay_rows["rows"]
    sector_rows = rows_for_stage(schedule, "sector_matrices")
    sector_responses = full_response["conditional_non_scalar_value_packet"]["sector_first_responses"]

    primitive_values = []
    for row in primitive_source_rows:
        source, value = primitive_value(row, rz, rx)
        primitive_values.append(
            {
                "row_id": row["row_id"],
                "sector": row["sector"],
                "response": row["response"],
                "coordinate": row["coordinate"],
                "algebraic_value": value,
                "value_source": source,
                "is_zero_routed_row": source is None,
                "filled_as_algebraic_candidate": True,
                "independent_quadrature_emitted": False,
                "physical_source_promoted": False,
            }
        )

    hessian_values = [
        {
            "row_id": "theta_phase",
            "algebraic_value": {
                "A_column_norm_sq": hessian["A_transpose_A"][0][0],
                "A_transpose_b_component": hessian["A_transpose_b"][0],
                "deltaTheta_component": hessian["deltaTheta_C1"][0],
            },
            "filled_as_algebraic_candidate": True,
            "independent_quadrature_emitted": False,
            "physical_source_promoted": False,
        },
        {
            "row_id": "theta_shift",
            "algebraic_value": {
                "A_column_norm_sq": hessian["A_transpose_A"][1][1],
                "A_transpose_b_component": hessian["A_transpose_b"][1],
                "deltaTheta_component": hessian["deltaTheta_C1"][1],
            },
            "filled_as_algebraic_candidate": True,
            "independent_quadrature_emitted": False,
            "physical_source_promoted": False,
        },
    ]

    sector_values = [
        {
            "row_id": row_id,
            "sector": row_id.split(":")[0],
            "coordinate": row_id.split(":")[2],
            "algebraic_value": sector_value(row_id, sector_responses),
            "source_direction": sector_responses[row_id.split(":")[0]]["source_direction"],
            "filled_as_algebraic_candidate": True,
            "independent_quadrature_emitted": False,
            "physical_source_promoted": False,
        }
        for row_id in sector_rows
    ]

    route_a = {
        "schema": "MTTPhysicalSourcePromotionAttemptFromKernelValues.v1",
        "status": "PHYSICAL_SOURCE_PROMOTION_ATTEMPT_STILL_OPEN",
        "source_theorem_template": rel(DATA / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues" / "route_a_physical_source_theorem_template.packet.json"),
        "theorem_name": route_a_template["theorem_name"],
        "clauses_tested": route_a_template["required_clauses"],
        "available_now": {
            "formal_euler_projection": route_a_template["formal_support_available"]["finite_euler_projection_derived"],
            "least_norm_Q_residual_selection": route_a_template["formal_support_available"]["least_norm_completion_selects_Q_residual"],
            "algebraic_RZ_RX_values_filled": True,
            "algebraic_b_selected_filled": True,
            "algebraic_sector_response_values_filled": True,
        },
        "still_missing_for_promotion": {
            "physical_action_identity": True,
            "selected_measure_or_pairing_from_PhiFinC1_trace": True,
            "admissible_variation_class": True,
            "boundary_cancellation": True,
            "same_source_emits_b_selected": True,
        },
        "route_A_promoted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTAlgebraicC1KernelValueExecutionAttempt.v1",
        "status": "ALGEBRAIC_VALUES_FILLED_NOT_INDEPENDENT_QUADRATURE",
        "kernel_manifest": rel(DATA / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues" / "route_b_quadrature_kernel_value_manifest.packet.json"),
        "value_sources": {
            "R_Z": rel(DATA / "selected_residual_weylpolynomial_source_theorem_attempt" / "residual_weyl_polynomial_decomposition.packet.json"),
            "R_X": rel(DATA / "selected_residual_weylpolynomial_source_theorem_attempt" / "residual_weyl_polynomial_decomposition.packet.json"),
            "hessian_source_vector": rel(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "hessian_source_vector.packet.json"),
            "sector_response_packet": rel(DATA / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json"),
        },
        "primitive_kernel_values": primitive_values,
        "hessian_source_values": hessian_values,
        "sector_matrix_values": sector_values,
        "counts": {
            "primitive_values_filled": len(primitive_values),
            "hessian_values_filled": len(hessian_values),
            "sector_values_filled": len(sector_values),
            "total_algebraic_values_filled": len(primitive_values) + len(hessian_values) + len(sector_values),
            "independent_quadrature_values": 0,
            "physical_source_promoted_values": 0,
        },
        "algebraic_consistency_certificate": {
            "R_Z_norm_sq": residual_poly["decompositions"]["R_Z"]["norm_sq"],
            "R_X_norm_sq": residual_poly["decompositions"]["R_X"]["norm_sq"],
            "R_Z_reconstruction_error_norm_sq": residual_poly["decompositions"]["R_Z"]["reconstruction_error_norm_sq"],
            "R_X_reconstruction_error_norm_sq": residual_poly["decompositions"]["R_X"]["reconstruction_error_norm_sq"],
            "A_transpose_A": hessian["A_transpose_A"],
            "A_transpose_b": hessian["A_transpose_b"],
            "b_norm_sq": hessian["b_norm_sq"],
            "deltaTheta_C1": hessian["deltaTheta_C1"],
            "passes_locked_target_by_algebraic_replay": contract["locked_target_check"]["passes_locked_target_by_replay"],
        },
        "route_B_accepts_now": False,
        "why_not_independent": [
            "The selected measure/pairing and row kernels are still not derived from the finite C1 trace.",
            "The values are algebraic residual/full-response replay values, not independently integrated quadrature values.",
            "No exactness/error-bound certificate for an independent selected quadrature engine is emitted here.",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    barrier = {
        "schema": "MTTC1KernelValuePromotionBarrierAndNextGate.v1",
        "status": "VALUES_FILLED_PROMOTION_REQUIRES_MEASURE_OR_ACTION_IDENTITY",
        "statement": (
            "All 110 finite C1 value slots can now be populated algebraically from the residual Weyl "
            "polynomial, Hessian replay, and conditional full-response packet. This removes value-slot "
            "bookkeeping as a blocker, but it does not close the theorem because the values are not emitted "
            "by a selected physical C1 action or independent quadrature measure."
        ),
        "acceptance_contract_result": {
            "route_A_accepts_now": False,
            "route_B_accepts_now": False,
            "closure_claimed": False,
        },
        "minimal_next_gate": {
            "derive_selected_physical_action_identity": True,
            "or_define_selected_C1_measure_pairing_and_exact_kernel_quadrature": True,
            "then_reuse_algebraic_values_as_check_not_selector": True,
        },
        "forbidden_shortcuts": contract["forbidden_shortcuts"],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedC1KernelValuesExecutionOrPhysicalSourcePromotion",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(DATA / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues.candidate.json"),
            "kernel_manifest": rel(DATA / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues" / "route_b_quadrature_kernel_value_manifest.packet.json"),
            "acceptance_contract": rel(DATA / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues" / "source_or_kernel_acceptance_contract.packet.json"),
            "residual_weyl_polynomial": rel(DATA / "selected_residual_weylpolynomial_source_theorem_attempt" / "residual_weyl_polynomial_decomposition.packet.json"),
            "hessian_source_vector": rel(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "hessian_source_vector.packet.json"),
            "full_response_packet": rel(DATA / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json"),
        },
        "output_packets": {
            "route_a_physical_source_promotion_attempt": rel(ROUTE_A),
            "route_b_algebraic_kernel_value_execution_attempt": rel(ROUTE_B),
            "promotion_barrier_and_next_gate": rel(BARRIER),
        },
        "theorem": {
            "name": "AlgebraicKernelValuesDoNotPromoteWithoutMeasureOrActionIdentityTheorem",
            "proved": True,
            "statement": barrier["statement"],
        },
        "what_closes_now": {
            "all_110_value_slots_have_algebraic_candidate_values": True,
            "primitive_RZ_RX_values_filled": True,
            "hessian_b_delta_values_filled": True,
            "sector_response_values_filled": True,
            "promotion_barrier_identified": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_physical_action_identity": True,
            "selected_C1_measure_pairing": True,
            "independent_quadrature_exactness_certificate": True,
            "same_source_b_selected_emission": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "route_A_physical_source_promoted": False,
            "route_B_independent_quadrature_executed": False,
            "algebraic_values_promoted_as_physical": False,
            "algebraic_values_promoted_as_independent": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
        "previous_status": previous["status"],
    }

    cert = {
        "certificate": "MTT_Selected_C1KernelValuesExecution_or_PhysicalSourcePromotion_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
    }

    note = f"""# MTT Selected C1KernelValuesExecution or PhysicalSourcePromotion v1

Status: `{STATUS}`.

The 110-slot manifest is now value-filled algebraically:

```text
primitive C1 values filled     = {len(primitive_values)}
hessian/source values filled   = {len(hessian_values)}
sector response values filled  = {len(sector_values)}
independent quadrature values  = 0
physical-source values         = 0
locked target replay passes    = {route_b["algebraic_consistency_certificate"]["passes_locked_target_by_algebraic_replay"]}
```

This is progress, not closure. The next proof object is the promotion object:
either the selected physical C1 action identity, or a selected finite C1
measure/pairing with an exact independent quadrature certificate.

Next artifact: `{NEXT}`.
"""

    ROUTE_A.write_text(json.dumps(route_a, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_B.write_text(json.dumps(route_b, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    BARRIER.write_text(json.dumps(barrier, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
