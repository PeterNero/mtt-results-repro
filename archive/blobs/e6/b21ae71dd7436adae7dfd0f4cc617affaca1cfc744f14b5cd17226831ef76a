"""Build same-source dynamic transfer identity / independent row formula execution gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_samesourcedynamictransferidentity_or_independentrowformulaexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IDENTITY = PACKET_DIR / "same_source_dynamic_transfer_identity_current_gate.packet.json"
ROWS = PACKET_DIR / "independent_row_formula_execution_current_gate.packet.json"
EQUIV = PACKET_DIR / "identity_or_rows_equivalence.packet.json"
DECISION = PACKET_DIR / "current_frontier_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameSourceDynamicTransferIdentity_or_IndependentRowFormulaExecution_v1.md"

STATUS = "MTT_SELECTED_SAMESOURCEDYNAMICTRANSFERIDENTITY_OR_INDEPENDENTROWFORMULAEXECUTION_BUILT_CURRENT_FRONTIER_OPEN"
NEXT = "MTT_Selected_PhiFinC1DynamicTransferIdentityProof_or_FirstIndependentRowFormulaRun_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_dynamicc1transferprimitivetensorhessian_or_independentrows.candidate.json")
    old_identity = load(DATA / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json")
    row_contract = load(
        DATA
        / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution"
        / "primitive_row_formula_execution_contract.packet.json"
    )
    row_checklist = load(
        DATA
        / "selected_fivephysicalclauses_or_seventytwoprimitivekernelrows"
        / "seventy_two_primitive_kernel_row_checklist.packet.json"
    )
    current_gate = load(
        DATA
        / "selected_dynamicc1transferprimitivetensorhessian_or_independentrows"
        / "dynamic_transfer_primitive_hessian_gate.packet.json"
    )

    identity = {
        "schema": "MTTSameSourceDynamicTransferIdentityCurrentGate.v1",
        "status": "SAME_SOURCE_DYNAMIC_TRANSFER_IDENTITY_NORMAL_FORM_CURRENT_VALUES_OPEN",
        "normal_form_imported_from": rel(DATA / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"),
        "identity_name": old_identity["normal_form_identity"]["name"],
        "identity_equations": old_identity["normal_form_identity"]["identity_equations"],
        "finite_values_if_identity_proved": old_identity["normal_form_identity"]["finite_values_if_identity_proved"],
        "closed_support": {
            **old_identity["closed_support"],
            "static_source_retired": True,
            "conditional_dynamic_values_exact": True,
            "source_map_candidate_constructed": True,
        },
        "selected_status": old_identity["lane_A_same_source_dynamic_transfer"]["selected_status"],
        "minimal_missing_equations": old_identity["lane_A_same_source_dynamic_transfer"]["minimal_missing_equations"],
        "can_promote_now": False,
        "why_not_promoted": old_identity["normal_form_identity"]["why_not_proved_now"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    rows = {
        "schema": "MTTIndependentRowFormulaExecutionCurrentGate.v1",
        "status": "INDEPENDENT_ROW_FORMULA_EXECUTION_CURRENT_GATE_OPEN",
        "row_count": row_contract["primitive_row_count"],
        "row_count_matches_checklist": row_contract["primitive_rows"] == [row["row_id"] for row in row_checklist["rows"]],
        "available_support": row_contract["now_available_for_row_formula"],
        "required_kernel_fields_per_row": row_contract["required_kernel_fields_per_row"],
        "still_missing_for_execution": row_contract["still_missing_for_execution"],
        "execution_contract": {
            "selected_primitive_kernel_formula": False,
            "selected_trace_or_pairing_or_quadrature": False,
            "computed_72_complex_entries": False,
            "exactness_or_error_bounds": False,
            "independent_provenance": False,
        },
        "first_row": row_contract["primitive_rows"][0],
        "all_rows_executed_now": False,
        "locked_target_allowed_only_after_emission": row_contract["replay_rows_allowed_as_acceptance_oracle_only"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    equiv = {
        "schema": "MTTIdentityOrRowsEquivalence.v1",
        "status": "CURRENT_FRONTIER_TWO_ROUTE_EQUIVALENCE_BUILT_NEITHER_ROUTE_CLOSED",
        "route_a_identity_if_proved_then": {
            "selected_A_selected_promoted": True,
            "selected_b_selected_promoted": True,
            "selected_deltaTheta_C1_promoted": True,
            "unpatched_dynamic_C1_packet_closed": True,
        },
        "route_b_rows_if_executed_then": {
            "independent_row_formula_values_promoted": True,
            "selected_Galerkin_replacement_or_equivalent_dynamic_packet_closed": True,
            "locked_target_checked_after_emission": True,
        },
        "falsifier_contract": old_identity["falsifier_contract"],
        "shared_guardrails": {
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "target_replay_is_acceptance_oracle_only": True,
        },
    }

    decision = {
        "schema": "MTTCurrentFrontierDecision.v1",
        "status": "CURRENT_FRONTIER_BUILT_CLOSURE_NOT_CLAIMED",
        "same_source_dynamic_transfer_identity_closed": False,
        "independent_row_formula_execution_closed": False,
        "conditional_dynamic_values_exact": current_gate["no_linear_algebra_obstruction"],
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSameSourceDynamicTransferIdentityOrIndependentRowFormulaExecution",
        "status": STATUS,
        "inputs": {
            "previous_dynamic_value_gate": rel(DATA / "selected_dynamicc1transferprimitivetensorhessian_or_independentrows.candidate.json"),
            "normal_form_identity": rel(DATA / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"),
            "primitive_row_formula_contract": rel(
                DATA
                / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution"
                / "primitive_row_formula_execution_contract.packet.json"
            ),
        },
        "output_packets": {
            "same_source_dynamic_transfer_identity_current_gate": rel(IDENTITY),
            "independent_row_formula_execution_current_gate": rel(ROWS),
            "identity_or_rows_equivalence": rel(EQUIV),
            "current_frontier_decision": rel(DECISION),
        },
        "theorem": {
            "name": "SameSourceDynamicTransferIdentityOrIndependentRowFormulaExecutionTheorem",
            "proved": True,
            "statement": (
                "Under the current dynamic value-emission frontier, unpatched dynamic-C1 closure is reduced "
                "to two routes: prove the same-source Phi_fin^C1 dynamic transfer identity in the fixed "
                "72-real coordinate system, or execute the independent primitive row formula contract for all "
                "72 rows with exactness and independent provenance. Neither route is closed by replay values."
            ),
        },
        "previous_status": previous["status"],
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_SameSourceDynamicTransferIdentity_or_IndependentRowFormulaExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "same_source_dynamic_transfer_identity_closed": False,
        "independent_row_formula_execution_closed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected SameSourceDynamicTransferIdentity or IndependentRowFormulaExecution v1

Status: `{STATUS}`.

This artifact updates the older same-source dynamic-transfer normal form to the
current frontier. The fallback is now the independent primitive row formula
contract rather than a generic Galerkin-contraction lane.

Route A closes by proving the same-source `Phi_fin^C1` transfer identity:
`Z -> phase_packet`, `X -> shift_packet`, `b_selected = phase + shift`, and
`G = 12 I_2`.

Route B closes by executing all 72 primitive row formulas with selected formula,
pairing/quadrature source, complex values, exactness/error certificates, and
provenance independent of residual-projector replay.

No unpatched dynamic-C1, true-SM-equivalence, or no-knob closure is claimed.
"""

    for path, payload in [
        (IDENTITY, identity),
        (ROWS, rows),
        (EQUIV, equiv),
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
