"""Build the concrete value-slot manifest for final dynamic C1 closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalsourceemissionvalues_or_honestgalerkinexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_emission_value_slots.packet.json"
ROUTE_B = PACKET_DIR / "route_b_honest_execution_workorder.packet.json"
RESULT = PACKET_DIR / "closure_attempt_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalSourceEmissionValues_or_HonestGalerkinExecution_v1.md"

STATUS = "MTT_SELECTED_PHYSICALSOURCEEMISSIONVALUES_OR_HONESTGALERKINEXECUTION_BUILT_VALUE_SLOTS_OPEN"
NEXT = "MTT_Selected_RouteAPhysicalEmissionValues_or_RouteBRowExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def slot(name: str, required_type: str, acceptance: str) -> dict[str, Any]:
    return {
        "name": name,
        "required_type": required_type,
        "acceptance": acceptance,
        "value": None,
        "theorem_derived": False,
        "same_branch": False,
        "selected_source_verified": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    cutset_gate = load(DATA / "selected_physicalactionrestrictionemission_or_independentgalerkinrows.candidate.json")
    cutset = load(
        DATA
        / "selected_physicalactionrestrictionemission_or_independentgalerkinrows"
        / "final_dynamic_c1_unpatched_cutset.packet.json"
    )
    route_a_accept = load(
        DATA
        / "selected_physicalactionrestrictionemission_or_independentgalerkinrows"
        / "route_a_physical_emission_acceptance.packet.json"
    )
    route_b_accept = load(
        DATA
        / "selected_physicalactionrestrictionemission_or_independentgalerkinrows"
        / "route_b_independent_galerkin_rows_acceptance.packet.json"
    )

    route_a_slots = {
        "schema": "MTTRouteAPhysicalEmissionValueSlots.v1",
        "status": "ROUTE_A_VALUE_SLOTS_DECLARED_VALUES_NOT_EMITTED",
        "slots": [
            slot(
                "physical_PhiFinC1_action_restriction",
                "selected action-to-finite-quotient identity",
                "The physical Phi_fin^C1 first variation restricts to the selected finite Weyl quotient.",
            ),
            slot(
                "zero_extra_boundary_or_source_term",
                "vanishing/cancellation certificate",
                "No unaccounted physical boundary/source contribution survives the restriction.",
            ),
            slot(
                "physical_R_Z",
                "same-branch residual operator",
                "The phase residual equals the canonical finite R_Z from the same selected source branch.",
            ),
            slot(
                "physical_R_X",
                "same-branch residual operator",
                "The shift residual equals the canonical finite R_X from the same selected source branch.",
            ),
            slot(
                "physical_b_selected",
                "same-branch Hessian/source vector",
                "The physical Hessian/source vector emits b_selected=(12,12) with A^T A=12 I_2.",
            ),
        ],
        "acceptance_table_import": route_a_accept["acceptance_table"],
        "all_values_emitted_now": False,
        "lane_closes_now": False,
        "if_all_values_emit": cutset["if_close_values"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    required = route_b_accept["required_outputs"]
    route_b_workorder = {
        "schema": "MTTRouteBHonestExecutionWorkorder.v1",
        "status": "ROUTE_B_EXECUTION_WORKORDER_DECLARED_ROWS_NOT_EXECUTED",
        "strict_coordinate_target": route_b_accept["replay_support_available"]["strict_coordinate_target"],
        "row_blocks_to_emit": [
            {
                "name": "selected_zero_mode_bases",
                "required_output": "zero_mode_bases",
                "current_replay_support": "canonical qutrit matrix-unit basis, support-level only",
                "row_count": 9,
                "executed_now": False,
                "selected_source_verified": False,
            },
            {
                "name": "primitive_three_by_three_contraction_terms",
                "required_output": "primitive_three_by_three_contraction_terms",
                "current_replay_support": "R_Z/R_X residual-projector rows, not independent quadrature",
                "row_count": 72,
                "executed_now": False,
                "selected_source_verified": False,
            },
            {
                "name": "linear_response_matrices",
                "required_output": "linear_response_matrices",
                "current_replay_support": "four sector matrices routed u,e to R_Z and d,nuD to R_X",
                "row_count": 36,
                "executed_now": False,
                "selected_source_verified": False,
            },
            {
                "name": "hessian_source_vector",
                "required_output": "A_selected, b_selected, deltaTheta_C1",
                "current_replay_support": "A^T A=12 I_2, A^T b=(12,12), deltaTheta=(1,1)",
                "row_count": 2,
                "executed_now": False,
                "selected_source_verified": False,
            },
            {
                "name": "C33_nonzero_family_rank_tests",
                "required_output": "C33/nonzero-family-rank tests",
                "current_replay_support": "declared as required but not evaluated as an independent selected test",
                "row_count": None,
                "executed_now": False,
                "selected_source_verified": False,
            },
        ],
        "required_outputs": required,
        "acceptance_table_import": route_b_accept["acceptance_table"],
        "all_rows_executed_now": False,
        "lane_closes_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    result = {
        "schema": "MTTPhysicalSourceEmissionOrHonestGalerkinExecutionResult.v1",
        "status": "NO_FINAL_VALUES_EMITTED_CLOSURE_OBJECT_NOW_PRECISE",
        "route_a_value_slots_filled": False,
        "route_b_honest_rows_executed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "what_is_new": [
            "final Route A physical emission slots are named and typed",
            "final Route B honest execution row blocks are named and counted",
            "the locked value target is preserved without using replay as proof",
        ],
        "next_actionable_targets": [
            "emit one Route A physical slot from the selected Phi_fin^C1/action branch",
            "or execute one Route B primitive row block with independent provenance",
            "then rerun this manifest and promote only if the acceptance booleans flip by theorem or execution",
        ],
        "locked_if_close_values": cutset["if_close_values"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalSourceEmissionValuesOrHonestGalerkinExecution",
        "status": STATUS,
        "inputs": {
            "two_lane_cutset_gate": rel(DATA / "selected_physicalactionrestrictionemission_or_independentgalerkinrows.candidate.json"),
            "final_dynamic_c1_cutset": rel(
                DATA
                / "selected_physicalactionrestrictionemission_or_independentgalerkinrows"
                / "final_dynamic_c1_unpatched_cutset.packet.json"
            ),
        },
        "output_packets": {
            "route_a_emission_value_slots": rel(ROUTE_A),
            "route_b_honest_execution_workorder": rel(ROUTE_B),
            "closure_attempt_result": rel(RESULT),
        },
        "theorem": {
            "name": "PhysicalSourceEmissionValuesOrHonestGalerkinExecutionManifestTheorem",
            "proved": True,
            "statement": (
                "The final dynamic-C1 closure object can now be represented as concrete value slots. "
                "Route A requires five same-branch physical emissions; Route B requires the selected "
                "zero-mode, primitive, sector, Hessian, and C33/rank execution blocks. This theorem "
                "does not emit the values; it makes the remaining proof object fully checkable."
            ),
        },
        "closure_decision": {
            "value_slots_manifest_built": True,
            "route_a_values_emitted": False,
            "route_b_rows_executed": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_cutset_status": cutset_gate["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalSourceEmissionValues_or_HonestGalerkinExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "value_slots_manifest_built": True,
        "route_a_values_emitted": False,
        "route_b_rows_executed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalSourceEmissionValues or HonestGalerkinExecution v1

Status: `{STATUS}`.

This artifact turns the two-lane dynamic-C1 cutset into concrete value slots.
It emits no physical values and executes no independent Galerkin rows yet.

Route A must fill the same-branch physical slots:
`Phi_fin^C1` action restriction, zero extra boundary/source term, physical
`R_Z`, physical `R_X`, and physical `b_selected`.

Route B must execute the selected zero-mode basis, primitive contraction terms,
sector response matrices, Hessian/source vector, and C33/nonzero-family-rank
tests with independent provenance.

The locked if-close target remains `A_selected=12 I_2`, `b_selected=(12,12)`,
and `deltaTheta_C1=(1,1)`.  It is not used as a selector.
"""

    for path, payload in [
        (ROUTE_A, route_a_slots),
        (ROUTE_B, route_b_workorder),
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
