"""Attempt Route A RZ/RX/b source emission or Route B first primitive row."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_rzrxb_source_emission_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_first_primitive_row_execution_attempt.packet.json"
DECISION = PACKET_DIR / "source_gap_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalRZRXBSourceEmission_or_PrimitiveRowFirstExecution_v1.md"

STATUS = "MTT_SELECTED_PHYSICALRZRXBSOURCEEMISSION_OR_PRIMITIVEROWFIRSTEXECUTION_ATTEMPTED_SUPPORT_ONLY"
NEXT = "MTT_Selected_PhysicalActionSourceRule_or_IndependentPrimitiveKernelFormula_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_fivephysicalclauses_or_seventytwoprimitivekernelrows.candidate.json")
    canonical = load(
        DATA
        / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
        / "canonical_residual_operator_values.packet.json"
    )
    physical_status = load(
        DATA
        / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
        / "same_source_physical_emission_status.packet.json"
    )
    algebraic_rows = load(
        DATA
        / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion"
        / "route_b_algebraic_kernel_value_execution_attempt.packet.json"
    )
    checklist = load(
        DATA
        / "selected_fivephysicalclauses_or_seventytwoprimitivekernelrows"
        / "seventy_two_primitive_kernel_row_checklist.packet.json"
    )

    first_row_target = checklist["rows"][0]
    first_row_support = next(
        row for row in algebraic_rows["primitive_kernel_values"] if row["row_id"] == first_row_target["row_id"]
    )

    route_a = {
        "schema": "MTTRouteARZRXBSourceEmissionAttempt.v1",
        "status": "RZ_RX_B_VALUES_READY_PHYSICAL_SOURCE_EMISSION_NOT_PROVED",
        "canonical_R_Z_support": {
            "available": canonical["mathematical_residual_values_ready"],
            "exact_polynomial": canonical["R_Z"]["exact_polynomial"],
            "norm_sq": canonical["R_Z"]["norm_sq"],
            "reconstruction_error_norm_sq": canonical["R_Z"]["reconstruction_error_norm_sq"],
            "physical_same_source_emission_claimed": canonical["physical_same_source_emission_claimed"],
        },
        "canonical_R_X_support": {
            "available": canonical["mathematical_residual_values_ready"],
            "exact_polynomial": canonical["R_X"]["exact_polynomial"],
            "norm_sq": canonical["R_X"]["norm_sq"],
            "reconstruction_error_norm_sq": canonical["R_X"]["reconstruction_error_norm_sq"],
            "physical_same_source_emission_claimed": canonical["physical_same_source_emission_claimed"],
        },
        "b_selected_support": physical_status["b_selected_replay"],
        "same_source_physical_R_Z_emitted": False,
        "same_source_physical_R_X_emitted": False,
        "same_source_physical_b_selected_emitted": False,
        "physical_action_restriction_emitted": False,
        "no_extra_boundary_or_source_emitted": False,
        "route_a_closed_now": False,
        "why_not_closed": (
            "The exact finite Weyl values and replay b vector exist, but current packets still mark them as "
            "canonical/replay support rather than same-branch physical Phi_fin^C1 source emissions."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTRouteBFirstPrimitiveRowExecutionAttempt.v1",
        "status": "FIRST_PRIMITIVE_ROW_REHEARSED_FROM_ALGEBRAIC_SUPPORT_NOT_INDEPENDENTLY_EXECUTED",
        "row_id": first_row_target["row_id"],
        "sector": first_row_target["sector"],
        "response": first_row_target["response"],
        "matrix_coordinate": first_row_target["matrix_coordinate"],
        "algebraic_support_value": first_row_support["algebraic_value"],
        "value_source": first_row_support["value_source"],
        "filled_as_algebraic_candidate": first_row_support["filled_as_algebraic_candidate"],
        "independent_quadrature_emitted": first_row_support["independent_quadrature_emitted"],
        "physical_source_promoted": first_row_support["physical_source_promoted"],
        "selected_primitive_kernel_formula": None,
        "selected_trace_or_pairing_source": None,
        "exactness_or_error_bound_certificate": None,
        "provenance_independent_of_residual_projector_replay": False,
        "first_row_independently_executed_now": False,
        "why_not_closed": (
            "The row has an exact algebraic replay value, but Route B requires an independent selected kernel "
            "formula, pairing/quadrature source, exactness certificate, and provenance independent of residual replay."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTSourceGapDecision.v1",
        "status": "FIRST_ATTACK_FINDS_SOURCE_PROMOTION_GAP_NOT_NUMERIC_GAP",
        "route_a_values_numerically_ready": True,
        "route_a_same_source_physical_emission_closed": False,
        "route_b_first_row_value_numerically_ready": True,
        "route_b_first_row_independent_execution_closed": False,
        "source_gap_not_numeric_gap": True,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalRZRXBSourceEmissionOrPrimitiveRowFirstExecution",
        "status": STATUS,
        "inputs": {
            "execution_checklist": rel(DATA / "selected_fivephysicalclauses_or_seventytwoprimitivekernelrows.candidate.json"),
            "canonical_residual_values": rel(
                DATA
                / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
                / "canonical_residual_operator_values.packet.json"
            ),
            "same_source_physical_emission_status": rel(
                DATA
                / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
                / "same_source_physical_emission_status.packet.json"
            ),
            "algebraic_kernel_value_execution_attempt": rel(
                DATA
                / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion"
                / "route_b_algebraic_kernel_value_execution_attempt.packet.json"
            ),
        },
        "output_packets": {
            "route_a_rzrxb_source_emission_attempt": rel(ROUTE_A),
            "route_b_first_primitive_row_execution_attempt": rel(ROUTE_B),
            "source_gap_decision": rel(DECISION),
        },
        "theorem": {
            "name": "PhysicalRZRXBOrFirstPrimitiveRowSourceGapTheorem",
            "proved": True,
            "statement": (
                "The next attack shows the remaining dynamic-C1 blocker is not the numeric value of R_Z, R_X, "
                "b_selected, or the first primitive row. Those values are already available as canonical or replay "
                "support. What is missing is source promotion: either same-branch physical Phi_fin^C1 emission or "
                "independent selected primitive kernel formula execution."
            ),
        },
        "previous_status": previous["status"],
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalRZRXBSourceEmission_or_PrimitiveRowFirstExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "route_a_closed_now": False,
        "route_b_first_row_independent_execution_closed": False,
        "source_gap_not_numeric_gap": True,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalRZRXBSourceEmission or PrimitiveRowFirstExecution v1

Status: `{STATUS}`.

This artifact tries the first concrete attack after the final execution
checklist.

Route A: `R_Z`, `R_X`, and `b_selected` are numerically ready as canonical
finite-Weyl/replay support, but they are not yet same-branch physical
`Phi_fin^C1` source emissions.

Route B: the first primitive row `u:phase:r0c0` has an algebraic support value,
but it is not independently executed from a selected primitive kernel formula
with a selected pairing source and exactness/provenance certificate.

So the remaining blocker is source promotion, not value search.
"""

    for path, payload in [
        (ROUTE_A, route_a),
        (ROUTE_B, route_b),
        (DECISION, decision),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
