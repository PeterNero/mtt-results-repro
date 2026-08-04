"""Build differentiated Phi_fin^C1 primitive-overlap / first-row kernel source gate.

This gate advances the previous first-row attempt by separating three objects
that had been bundled together:

* the selected row kernel formula;
* the selected finite trace/Frobenius pairing source;
* the independent row value/exactness/provenance execution.

The first two can be sourced from existing selected artifacts.  The third is
still open, so this artifact must not claim full row execution, dynamic C1
closure, true SM equivalence, or no-knob closure.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
DIFF_PACKET = PACKET_DIR / "differentiated_primitive_overlap_source_packet.packet.json"
ROW_PACKET = PACKET_DIR / "first_row_kernel_formula_source_packet.packet.json"
DECISION_PACKET = PACKET_DIR / "kernel_source_promotion_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_DifferentiatedPhiFinC1PrimitiveOverlap_or_FirstRowKernelFormulaSource_v1.md"

PREVIOUS = DATA / "selected_phifinc1dynamictransferidentityproof_or_firstindependentrowformularun.candidate.json"
DIFF_PHIFIN = DATA / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.candidate.json"
FIRST_ROW = (
    DATA
    / "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution"
    / "route_b_first_primitive_row_execution_attempt.packet.json"
)
ROW_GATE = (
    DATA
    / "selected_samesourcedynamictransferidentity_or_independentrowformulaexecution"
    / "independent_row_formula_execution_current_gate.packet.json"
)
TRACE_UNIQUENESS = DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation.candidate.json"
TRACE_SUPPORT = (
    DATA
    / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
    / "selected_trace_map_and_measure_support.packet.json"
)

STATUS = (
    "MTT_SELECTED_DIFFERENTIATEDPHIFINC1PRIMITIVEOVERLAP_OR_FIRSTROWKERNELFORMULASOURCE_"
    "BUILT_FORMULA_PAIRING_SOURCE_ROW_VALUE_OPEN"
)
NEXT = "MTT_Selected_FirstRowKernelFormulaExactExecution_or_PhysicalPhiFinC1ActionSource_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    diff = load(DIFF_PHIFIN)
    first_row = load(FIRST_ROW)
    row_gate = load(ROW_GATE)
    trace_uniqueness = load(TRACE_UNIQUENESS)
    trace_support = load(TRACE_SUPPORT)

    contract = diff["differentiated_primitive_overlap_contract"]
    sector = first_row["sector"]
    response = first_row["response"]
    row = first_row["matrix_coordinate"]["row"]
    column = first_row["matrix_coordinate"]["column"]
    row_formula = (
        f"K_{{{sector},{response};{row}{column}}} = "
        f"<psi_L,{row}, V_{response} psi_R,{column} H_{sector}> "
        f"+ <delta_{response} psi_L,{row}, V_0 psi_R,{column} H_{sector}> "
        f"+ <psi_L,{row}, V_0 delta_{response} psi_R,{column} H_{sector}> "
        f"+ <psi_L,{row}, V_0 psi_R,{column} delta_{response} H_{sector}> "
        f"+ HessianCounterterm_{sector}^{response}[{row},{column}]"
    )

    finite_pairing_source_verified = (
        trace_uniqueness["closure_decision"]["measure_normalization_derived"] is True
        and trace_uniqueness["what_closes_now"]["finite_Weyl_invariant_trace_measure_derived"] is True
        and trace_support["support_imported"]["formal_trace_frobenius_pairing_built"] is True
    )

    differentiated_source_packet = {
        "schema": "MTTDifferentiatedPhiFinC1PrimitiveOverlapSourcePacket.v1",
        "status": "DIFFERENTIATED_PRIMITIVE_OVERLAP_FORMULA_SOURCE_SPECIFIED_VALUES_OPEN",
        "source_formula": contract["primitive_overlap_formula"],
        "sector_couplings": contract["sector_couplings"],
        "coordinate_system": contract["coordinate_system"],
        "acceptance_equations_retained": contract["acceptance_equations"],
        "selected_alpha1_dotD_driver_attached": diff["driver_contract"][
            "attached_to_differentiated_contract_as_driver"
        ],
        "transport_only_lane_rejected": diff["transport_only_no_go_theorem"]["proved"],
        "formula_source_promoted_for_row_execution": True,
        "primitive_overlap_values_emitted": False,
        "sector_response_matrices_emitted": False,
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "deltaTheta_C1_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    first_row_source_packet = {
        "schema": "MTTFirstRowKernelFormulaSourcePacket.v1",
        "status": "FIRST_ROW_KERNEL_FORMULA_AND_FINITE_PAIRING_SOURCE_SPECIFIED_VALUE_OPEN",
        "row_id": first_row["row_id"],
        "sector": sector,
        "response": response,
        "matrix_coordinate": first_row["matrix_coordinate"],
        "selected_primitive_kernel_formula": row_formula,
        "formula_source": rel(DIFF_PHIFIN),
        "selected_trace_or_pairing_source": {
            "source": rel(TRACE_UNIQUENESS),
            "support": rel(TRACE_SUPPORT),
            "pairing": trace_support["candidate_physical_measure"]["pairing"],
            "measure_normalization_derived": trace_uniqueness["closure_decision"][
                "measure_normalization_derived"
            ],
            "finite_pairing_source_verified": finite_pairing_source_verified,
            "physical_PhiFinC1_action_identity_still_open": trace_uniqueness["what_remains_open"][
                "physical_PhiFinC1_action_identity"
            ],
        },
        "algebraic_support_value": first_row["algebraic_support_value"],
        "algebraic_support_value_source": first_row["value_source"],
        "computed_independent_complex_entry_value": False,
        "exactness_or_error_bound_certificate": None,
        "provenance_independent_of_residual_projector_replay": False,
        "first_row_independently_executed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "why_not_executed_now": (
            "The row formula and finite trace/Frobenius pairing source are now specified "
            "from selected artifacts, but the row value 4/3 is still only algebraic support. "
            "An independent contraction evaluation or physical Phi_fin^C1 action-source theorem "
            "must compute the row and provide exactness/provenance."
        ),
    }

    closed_kernel_clauses = {
        "selected_primitive_kernel_formula": True,
        "selected_physical_or_independent_trace_pairing_clause": finite_pairing_source_verified,
        "computed_independent_complex_entries": False,
        "exactness_or_error_bound_certificate": False,
        "provenance_independent_of_residual_projector_replay": False,
    }
    remaining_open = {key: not value for key, value in closed_kernel_clauses.items()}

    decision = {
        "schema": "MTTKernelSourcePromotionDecision.v1",
        "status": "FORMULA_AND_FINITE_PAIRING_SOURCE_PROMOTED_FIRST_ROW_VALUE_EXECUTION_OPEN",
        "previous_next_target": previous["next_required_artifact"],
        "row_gate_required_kernel_fields": row_gate["required_kernel_fields_per_row"],
        "closed_kernel_clauses_for_first_row": closed_kernel_clauses,
        "remaining_open_for_first_row": remaining_open,
        "full_72_row_execution_closed": False,
        "differentiated_PhiFinC1_identity_closed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "source_gap_reduced_to": [
            "independent contraction value for first row or all 72 rows",
            "exactness/error-bound certificate",
            "provenance independent of residual-projector replay",
            "physical Phi_fin^C1 action-source theorem if using Route A instead of independent rows",
        ],
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDifferentiatedPhiFinC1PrimitiveOverlapOrFirstRowKernelFormulaSource",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "differentiated_phifinc1_gate": rel(DIFF_PHIFIN),
            "first_row_attempt": rel(FIRST_ROW),
            "independent_row_gate": rel(ROW_GATE),
            "finite_trace_uniqueness": rel(TRACE_UNIQUENESS),
            "trace_support": rel(TRACE_SUPPORT),
        },
        "output_packets": {
            "differentiated_primitive_overlap_source_packet": rel(DIFF_PACKET),
            "first_row_kernel_formula_source_packet": rel(ROW_PACKET),
            "kernel_source_promotion_decision": rel(DECISION_PACKET),
        },
        "what_closes_now": {
            "differentiated_primitive_overlap_formula_source_specified": True,
            "first_row_kernel_formula_source_specified": True,
            "finite_trace_frobenius_pairing_source_attached": finite_pairing_source_verified,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "first_row_independent_value_execution": True,
            "all_72_independent_row_values": True,
            "exactness_or_error_bound_certificate": True,
            "provenance_independent_of_residual_projector_replay": True,
            "physical_PhiFinC1_action_identity": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "promotion_decision": decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "theorem": {
            "name": "DifferentiatedPrimitiveOverlapAndFirstRowKernelSourceTheorem",
            "proved": True,
            "statement": (
                "The selected differentiated Phi_fin^C1 primitive-overlap formula can be "
                "specialized to the first primitive row u:phase:r0c0, and the finite "
                "trace/Frobenius pairing used to evaluate such rows is already forced by "
                "finite Weyl trace uniqueness.  This closes the formula/pairing-source "
                "part of the first-row gate.  It does not compute the row independently: "
                "the value 4/3 remains algebraic support until an independent contraction "
                "execution or physical Phi_fin^C1 action-source theorem supplies exactness "
                "and provenance."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_DifferentiatedPhiFinC1PrimitiveOverlap_or_FirstRowKernelFormulaSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "packet_paths": candidate["output_packets"],
        "proved": candidate["theorem"]["proved"],
        "first_row_formula_source_specified": True,
        "finite_pairing_source_attached": finite_pairing_source_verified,
        "first_row_value_executed": False,
        "full_72_row_execution_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DifferentiatedPhiFinC1PrimitiveOverlap or FirstRowKernelFormulaSource v1

Status: `{STATUS}`

## Theorem

{candidate["theorem"]["statement"]}

## What closes

- differentiated primitive-overlap formula source: true
- first primitive row formula source: true
- finite trace/Frobenius pairing source attached: {str(finite_pairing_source_verified).lower()}

## What remains open

- independent first-row contraction value
- exactness or certified numerical error bound
- provenance independent of residual-projector replay
- physical `Phi_fin^C1` action-source identity if Route A is used
- all 72 row execution, `A_selected`, `b_selected`, and `deltaTheta_C1`

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "{SLUG}.candidate.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
PACKET_DIR = ROOT / "candidate_data" / "{SLUG}"
ROW = PACKET_DIR / "first_row_kernel_formula_source_packet.packet.json"
DECISION = PACKET_DIR / "kernel_source_promotion_decision.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DifferentiatedPhiFinC1PrimitiveOverlap_or_FirstRowKernelFormulaSource_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    row = load(ROW)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["what_closes_now"]["first_row_kernel_formula_source_specified"] is True, "row formula source not specified")
    require(data["what_closes_now"]["finite_trace_frobenius_pairing_source_attached"] is True, "finite pairing source not attached")
    require(row["row_id"] == "u:phase:r0c0", "row mismatch")
    require("HessianCounterterm_u^phase[0,0]" in row["selected_primitive_kernel_formula"], "formula not specialized")
    require(row["selected_trace_or_pairing_source"]["finite_pairing_source_verified"] is True, "pairing not verified")
    require(row["computed_independent_complex_entry_value"] is False, "row value overclaimed")
    require(row["first_row_independently_executed_now"] is False, "row execution overclaimed")
    require(decision["closed_kernel_clauses_for_first_row"]["selected_primitive_kernel_formula"] is True, "formula clause not closed")
    require(decision["closed_kernel_clauses_for_first_row"]["selected_physical_or_independent_trace_pairing_clause"] is True, "pairing clause not closed")
    require(decision["closed_kernel_clauses_for_first_row"]["computed_independent_complex_entries"] is False, "computed entries overclaimed")
    require(decision["full_72_row_execution_closed"] is False, "72 rows overclaimed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob closure overclaimed")
    require(cert["first_row_formula_source_specified"] is True, "certificate missing formula")
    require(cert["first_row_value_executed"] is False, "certificate overclaims row execution")
    require("Next artifact" in note, "note missing next artifact")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(DIFF_PACKET, differentiated_source_packet)
    write_json(ROW_PACKET, first_row_source_packet)
    write_json(DECISION_PACKET, decision)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"wrote {rel(OUTPUT)}")
    print(f"status {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
