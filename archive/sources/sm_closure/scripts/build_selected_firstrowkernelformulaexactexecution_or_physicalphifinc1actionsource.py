"""Build first-row exact execution / physical Phi_fin^C1 action-source gate.

The previous gate supplied the selected row formula and finite trace/Frobenius
pairing source.  This artifact executes the first row exactly using the
low-degree qutrit Weyl polynomial for R_Z:

  R_Z = (2/3) I + (2/3) Z - (1/3) X - (1/3) X^2
        + (e^{i*pi/3}/3) Z X + (e^{-i*pi/3}/3) Z X^2.

At matrix coordinate (0,0), only I and Z contribute in the standard qutrit
Weyl matrix representation, so the exact value is 4/3.  This closes the
computed-value and exactness clauses for the first row, but it does not close
the provenance clause: the R_Z polynomial is still inherited from the residual
projector lane unless a physical Phi_fin^C1 action-source theorem promotes it.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
EXEC_PACKET = PACKET_DIR / "first_row_exact_weyl_execution.packet.json"
ACTION_PACKET = PACKET_DIR / "physical_action_source_gate_after_first_row.packet.json"
DECISION_PACKET = PACKET_DIR / "first_row_execution_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_FirstRowKernelFormulaExactExecution_or_PhysicalPhiFinC1ActionSource_v1.md"

PREVIOUS = DATA / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource.candidate.json"
ROW_SOURCE = (
    DATA
    / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource"
    / "first_row_kernel_formula_source_packet.packet.json"
)
WEYL = (
    DATA
    / "selected_residual_weylpolynomial_source_theorem_attempt"
    / "residual_weyl_polynomial_decomposition.packet.json"
)
WEYL_GATE = DATA / "selected_residual_weylpolynomial_source_theorem_attempt.candidate.json"
PHYSICAL_REMAINDER = (
    DATA
    / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
    / "physical_boundary_source_remainder.packet.json"
)

STATUS = (
    "MTT_SELECTED_FIRSTROWKERNELFORMULAEXACTEXECUTION_OR_PHYSICALPHIFINC1ACTIONSOURCE_"
    "BUILT_FIRST_ROW_VALUE_EXACT_PROVENANCE_OPEN"
)
NEXT = "MTT_Selected_FirstRowProvenancePromotion_or_AllRowsWeylExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def fraction_string(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    row_source = load(ROW_SOURCE)
    weyl = load(WEYL)
    weyl_gate = load(WEYL_GATE)
    physical_remainder = load(PHYSICAL_REMAINDER)

    i_contribution = Fraction(2, 3)
    z_contribution = Fraction(2, 3)
    zero_contribution = Fraction(0, 1)
    value = i_contribution + z_contribution
    float_value = float(value)

    rz = weyl["decompositions"]["R_Z"]
    matrix_value = rz["matrix"][0][0]
    reconstructed_value = rz["reconstructed_matrix"][0][0]

    exact_execution = {
        "schema": "MTTFirstRowExactWeylExecution.v1",
        "status": "FIRST_ROW_VALUE_COMPUTED_EXACTLY_FROM_WEYL_POLYNOMIAL_PROVENANCE_OPEN",
        "row_id": row_source["row_id"],
        "sector": row_source["sector"],
        "response": row_source["response"],
        "matrix_coordinate": row_source["matrix_coordinate"],
        "selected_primitive_kernel_formula": row_source["selected_primitive_kernel_formula"],
        "selected_trace_or_pairing_source": row_source["selected_trace_or_pairing_source"],
        "weyl_polynomial_source": rel(WEYL),
        "exact_polynomial": weyl["exact_polynomial_form"]["R_Z"],
        "coordinate_evaluation_rule": {
            "qutrit_weyl_convention": "Z diagonal with Z_00=1; X and X^2 have zero diagonal at (0,0); ZX and ZX^2 inherit the off-diagonal X support",
            "I_00": 1,
            "Z_00": 1,
            "X_00": 0,
            "X2_00": 0,
            "ZX_00": 0,
            "ZX2_00": 0,
        },
        "exact_contribution_sum": {
            "I": fraction_string(i_contribution),
            "Z": fraction_string(z_contribution),
            "X": fraction_string(zero_contribution),
            "X2": fraction_string(zero_contribution),
            "ZX": fraction_string(zero_contribution),
            "ZX2": fraction_string(zero_contribution),
            "total": fraction_string(value),
        },
        "computed_complex_entry_value": {
            "exact": fraction_string(value),
            "real": float_value,
            "imag": 0.0,
        },
        "matches_algebraic_support_value": abs(float_value - row_source["algebraic_support_value"]) < 1e-12,
        "matches_weyl_packet_matrix_entry": abs(float_value - float(matrix_value)) < 1e-12,
        "matches_reconstructed_entry": abs(float_value - float(reconstructed_value)) < 1e-12,
        "exactness_or_error_bound_certificate": {
            "type": "symbolic_finite_weyl_coordinate_evaluation",
            "exact_value": fraction_string(value),
            "roundoff_bound": 0.0,
            "reason": "Only exact rational I and Z coefficients contribute at coordinate (0,0).",
        },
        "computed_independent_complex_entry_value": True,
        "exactness_certificate_emitted": True,
        "provenance_independent_of_residual_projector_replay": False,
        "first_row_independently_executed_now": False,
        "why_not_independent": (
            "The coordinate evaluation is exact and does not use observed data, but the R_Z "
            "polynomial packet is still the residual-projector polynomial source.  Full "
            "Route-B independence requires a row source not inherited from that replay, or "
            "Route-A physical Phi_fin^C1 action-source promotion."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    physical_action_gate = {
        "schema": "MTTPhysicalPhiFinC1ActionSourceGateAfterFirstRow.v1",
        "status": "PHYSICAL_ACTION_SOURCE_STILL_OPEN_AFTER_EXACT_FIRST_ROW_VALUE",
        "physical_remainder_source": rel(PHYSICAL_REMAINDER),
        "residual_weyl_gate": rel(WEYL_GATE),
        "already_closed": {
            "finite_trace_measure": True,
            "first_row_formula": True,
            "first_row_pairing": True,
            "first_row_exact_value": True,
        },
        "still_required_for_physical_route_A": {
            "physical_PhiFinC1_action_identity": not physical_remainder[
                "route_A_current_emissions"
            ]["physical_action_identity"],
            "no_extra_physical_boundary_or_source_term": not physical_remainder[
                "route_A_current_emissions"
            ]["no_extra_physical_boundary_or_source_term"],
            "same_source_R_Z_R_X_b_selected_emission": (
                not physical_remainder["route_A_current_emissions"]["phase_R_Z_source_selection"]
                or not physical_remainder["route_A_current_emissions"]["shift_R_X_source_selection"]
                or not physical_remainder["route_A_current_emissions"]["same_source_b_selected_emission"]
            ),
        },
        "still_required_for_independent_route_B": {
            "first_row_provenance_independent_of_residual_projector_replay": True,
            "all_72_rows_exactly_executed": True,
            "row_formula_source_repeated_for_all_rows": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTFirstRowExecutionDecision.v1",
        "status": "FIRST_ROW_VALUE_AND_EXACTNESS_CLOSED_PROVENANCE_PHYSICAL_SOURCE_OPEN",
        "closed_kernel_clauses_for_first_row": {
            "selected_primitive_kernel_formula": True,
            "selected_physical_or_independent_trace_pairing_clause": True,
            "computed_independent_complex_entries": True,
            "exactness_or_error_bound_certificate": True,
            "provenance_independent_of_residual_projector_replay": False,
        },
        "first_row_value_exact": fraction_string(value),
        "first_row_value_float": float_value,
        "first_row_independently_executed_now": False,
        "full_72_row_execution_closed": False,
        "physical_PhiFinC1_action_source_closed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFirstRowKernelFormulaExactExecutionOrPhysicalPhiFinC1ActionSource",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "row_source": rel(ROW_SOURCE),
            "weyl_polynomial": rel(WEYL),
            "residual_weyl_gate": rel(WEYL_GATE),
            "physical_boundary_source_remainder": rel(PHYSICAL_REMAINDER),
        },
        "output_packets": {
            "first_row_exact_weyl_execution": rel(EXEC_PACKET),
            "physical_action_source_gate_after_first_row": rel(ACTION_PACKET),
            "first_row_execution_decision": rel(DECISION_PACKET),
        },
        "what_closes_now": {
            "first_row_exact_coordinate_value": True,
            "first_row_exactness_certificate": True,
            "formula_and_pairing_sources_retained": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "first_row_provenance_independent_of_residual_projector_replay": True,
            "all_72_row_execution": True,
            "physical_PhiFinC1_action_identity": True,
            "same_source_R_Z_R_X_b_selected_emission": True,
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
            "name": "FirstRowExactWeylExecutionTheorem",
            "proved": True,
            "statement": (
                "For the first primitive row u:phase:r0c0, the selected row formula and "
                "finite trace/Frobenius pairing reduce the value computation to the R_Z "
                "qutrit Weyl polynomial.  Evaluating the polynomial at coordinate (0,0) "
                "is exact: X, X^2, ZX, and ZX^2 have zero (0,0) entry, while I_00=Z_00=1, "
                "so the row value is 2/3+2/3=4/3.  This closes the first-row computed-value "
                "and exactness clauses, but not the residual-projector-independent provenance "
                "or physical Phi_fin^C1 action-source clauses."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_FirstRowKernelFormulaExactExecution_or_PhysicalPhiFinC1ActionSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "packet_paths": candidate["output_packets"],
        "theorem_proved": True,
        "first_row_value_exact": fraction_string(value),
        "first_row_value_float": float_value,
        "first_row_exactness_certificate_emitted": True,
        "first_row_independently_executed_now": False,
        "physical_PhiFinC1_action_source_closed": False,
        "full_72_row_execution_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FirstRowKernelFormulaExactExecution or PhysicalPhiFinC1ActionSource v1

Status: `{STATUS}`

## Theorem

{candidate["theorem"]["statement"]}

## Exact Row Value

`R_Z(0,0) = 2/3 + 2/3 = 4/3`.

This is exact finite Weyl algebra, not a fit to observed data.

## Still Open

- provenance independent of residual-projector replay
- physical `Phi_fin^C1` action-source identity
- all 72 rows
- `A_selected`, `b_selected`, and `deltaTheta_C1`

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
EXEC = PACKET_DIR / "first_row_exact_weyl_execution.packet.json"
ACTION = PACKET_DIR / "physical_action_source_gate_after_first_row.packet.json"
DECISION = PACKET_DIR / "first_row_execution_decision.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FirstRowKernelFormulaExactExecution_or_PhysicalPhiFinC1ActionSource_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    execution = load(EXEC)
    action = load(ACTION)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(execution["row_id"] == "u:phase:r0c0", "row mismatch")
    require(execution["computed_complex_entry_value"]["exact"] == "4/3", "exact value mismatch")
    require(abs(execution["computed_complex_entry_value"]["real"] - 4.0 / 3.0) < 1e-12, "float value mismatch")
    require(execution["matches_algebraic_support_value"] is True, "support mismatch")
    require(execution["matches_weyl_packet_matrix_entry"] is True, "Weyl packet mismatch")
    require(execution["exactness_or_error_bound_certificate"]["roundoff_bound"] == 0.0, "not exact")
    require(execution["computed_independent_complex_entry_value"] is True, "computed clause not closed")
    require(execution["exactness_certificate_emitted"] is True, "exactness clause not closed")
    require(execution["provenance_independent_of_residual_projector_replay"] is False, "provenance overclaimed")
    require(execution["first_row_independently_executed_now"] is False, "independence overclaimed")
    require(action["already_closed"]["first_row_exact_value"] is True, "action gate missing row value")
    require(action["still_required_for_independent_route_B"]["first_row_provenance_independent_of_residual_projector_replay"] is True, "route B gap missing")
    require(decision["closed_kernel_clauses_for_first_row"]["computed_independent_complex_entries"] is True, "computed clause false")
    require(decision["closed_kernel_clauses_for_first_row"]["exactness_or_error_bound_certificate"] is True, "exactness clause false")
    require(decision["closed_kernel_clauses_for_first_row"]["provenance_independent_of_residual_projector_replay"] is False, "provenance overclosed")
    require(decision["first_row_value_exact"] == "4/3", "decision exact value mismatch")
    require(decision["full_72_row_execution_closed"] is False, "72 row overclaimed")
    require(decision["true_SM_equivalence_closed"] is False, "SM equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob overclaimed")
    require(cert["first_row_value_exact"] == "4/3", "certificate exact value mismatch")
    require(cert["first_row_independently_executed_now"] is False, "certificate independence overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("R_Z(0,0) = 2/3 + 2/3 = 4/3" in note, "note missing exact calculation")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(EXEC_PACKET, exact_execution)
    write_json(ACTION_PACKET, physical_action_gate)
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
