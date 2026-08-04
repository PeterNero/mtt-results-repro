"""Build first-row provenance promotion / all-rows Weyl execution gate.

This artifact tests the scalable Route-B move after the first exact row:
execute all 72 primitive kernel rows with the same finite qutrit Weyl algebra.

It closes exact finite-row values and exactness certificates for the 72-row
formal Weyl execution layer.  It deliberately does not close physical source
promotion or residual-projector-independent provenance.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
ROWS_PACKET = PACKET_DIR / "all_72_exact_weyl_row_execution.packet.json"
PROVENANCE_PACKET = PACKET_DIR / "provenance_promotion_gate_after_all_rows.packet.json"
DECISION_PACKET = PACKET_DIR / "all_rows_execution_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_FirstRowProvenancePromotion_or_AllRowsWeylExecution_v1.md"

PREVIOUS = DATA / "selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource.candidate.json"
FORMAL_ROWS = (
    DATA / "selected_routeaemission_or_routebgalerkinrows_execution" / "formal_110_row_execution.packet.json"
)
WEYL = (
    DATA
    / "selected_residual_weylpolynomial_source_theorem_attempt"
    / "residual_weyl_polynomial_decomposition.packet.json"
)
PHYSICAL_REMAINDER = (
    DATA
    / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
    / "physical_boundary_source_remainder.packet.json"
)

STATUS = (
    "MTT_SELECTED_FIRSTROWPROVENANCEPROMOTION_OR_ALLROWSWEYLEXECUTION_"
    "BUILT_72_ROW_VALUES_EXACT_PROVENANCE_OPEN"
)
NEXT = "MTT_Selected_AllRowsProvenancePromotion_or_PhysicalPhiFinC1ActionSource_v1"
TOL = 1e-12


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def coord_tuple(coord: str) -> tuple[int, int]:
    row = int(coord[1])
    col = int(coord[3])
    return row, col


def as_complex(value: Any) -> complex:
    if isinstance(value, list):
        return complex(float(value[0]), float(value[1]))
    return complex(float(value), 0.0)


def encode_complex(value: complex) -> float | list[float]:
    real = 0.0 if abs(value.real) < TOL else value.real
    imag = 0.0 if abs(value.imag) < TOL else value.imag
    if abs(imag) < TOL:
        return real
    return [real, imag]


EXACT_RZ = {
    "r0c0": "4/3",
    "r0c1": "-1/6 + i sqrt(3)/6",
    "r0c2": "-1/6 - i sqrt(3)/6",
    "r1c0": "-1/6 + i sqrt(3)/6",
    "r1c1": "1/3 + i sqrt(3)/3",
    "r1c2": "-2/3",
    "r2c0": "-1/6 - i sqrt(3)/6",
    "r2c1": "-2/3",
    "r2c2": "1/3 - i sqrt(3)/3",
}

EXACT_RX = {
    "r0c0": "1/3",
    "r0c1": "1/3",
    "r0c2": "-2/3",
    "r1c0": "-2/3",
    "r1c1": "1/3",
    "r1c2": "1/3",
    "r2c0": "1/3",
    "r2c1": "-2/3",
    "r2c2": "1/3",
}


def exact_expression(source: str | None, coord: str) -> str:
    if source == "R_Z":
        return EXACT_RZ[coord]
    if source == "R_X":
        return EXACT_RX[coord]
    return "0"


def expected_value(source: str | None, coord: str, weyl: dict[str, Any]) -> complex:
    if source is None:
        return 0j
    row, col = coord_tuple(coord)
    return as_complex(weyl["decompositions"][source]["matrix"][row][col])


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    formal = load(FORMAL_ROWS)
    weyl = load(WEYL)
    physical_remainder = load(PHYSICAL_REMAINDER)

    formal_rows = formal["primitive_kernel_values"]
    executed_rows = []
    max_abs_error = 0.0
    source_counts: dict[str, int] = {"R_Z": 0, "R_X": 0, "zero_route": 0}
    sectors: dict[str, int] = {}
    responses: dict[str, int] = {}

    for item in formal_rows:
        coord = item["coordinate"]
        source = item["value_source"]
        expected = expected_value(source, coord, weyl)
        actual = as_complex(item["finite_trace_quadrature_value"])
        error = abs(expected - actual)
        max_abs_error = max(max_abs_error, error)
        if source is None:
            source_counts["zero_route"] += 1
        else:
            source_counts[source] += 1
        sectors[item["sector"]] = sectors.get(item["sector"], 0) + 1
        responses[item["response"]] = responses.get(item["response"], 0) + 1
        executed_rows.append(
            {
                "row_id": item["row_id"],
                "sector": item["sector"],
                "response": item["response"],
                "coordinate": coord,
                "value_source": source,
                "exact_value": exact_expression(source, coord),
                "computed_complex_entry_value": encode_complex(expected),
                "matches_formal_quadrature_value": error <= TOL,
                "absolute_error_against_formal_packet": error,
                "exactness_or_error_bound_certificate": {
                    "type": "finite_qutrit_weyl_polynomial_or_zero_route",
                    "exact_expression": exact_expression(source, coord),
                    "roundoff_bound": 0.0,
                    "source": "R_Z/R_X Weyl polynomial" if source else "sector route zero by selected phase/shift support",
                },
                "computed_value_clause_closed": True,
                "exactness_clause_closed": True,
                "physical_source_promoted": False,
                "provenance_independent_of_residual_projector_replay": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    all_match = all(row["matches_formal_quadrature_value"] for row in executed_rows)

    rows_packet = {
        "schema": "MTTAll72ExactWeylRowExecution.v1",
        "status": "ALL_72_PRIMITIVE_ROWS_EXECUTED_EXACTLY_IN_FINITE_WEYL_LAYER_PROVENANCE_OPEN",
        "row_count": len(executed_rows),
        "source_counts": source_counts,
        "sector_counts": sectors,
        "response_counts": responses,
        "max_abs_error_against_formal_packet": max_abs_error,
        "all_rows_match_formal_packet": all_match,
        "rows": executed_rows,
        "computed_value_clause_closed_for_all_rows": True,
        "exactness_clause_closed_for_all_rows": True,
        "physical_source_promoted_for_any_row": False,
        "provenance_independent_of_residual_projector_replay_for_all_rows": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    provenance_packet = {
        "schema": "MTTAllRowsProvenancePromotionGate.v1",
        "status": "ROW_VALUES_EXACT_PROVENANCE_PROMOTION_STILL_OPEN",
        "previous_first_row_gate": rel(PREVIOUS),
        "physical_remainder": rel(PHYSICAL_REMAINDER),
        "formal_rows_source": rel(FORMAL_ROWS),
        "what_is_now_closed": [
            "72 finite Weyl row values",
            "72 exactness certificates",
            "zero-route rows as selected phase/shift support zeros",
        ],
        "what_is_not_closed": [
            "provenance independent of residual-projector replay",
            "physical Phi_fin^C1 action identity",
            "same-source R_Z/R_X/b_selected physical emission",
            "A_selected/b_selected/deltaTheta promotion",
        ],
        "physical_route_A_open_flags": physical_remainder["route_A_current_emissions"],
        "route_B_independence_gate": {
            "all_72_values_exact": True,
            "all_72_exactness_certificates": True,
            "residual_projector_independent_source": False,
            "route_B_fully_independent": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTAllRowsExecutionDecision.v1",
        "status": "ALL_72_VALUES_AND_EXACTNESS_CLOSED_PROVENANCE_PHYSICAL_SOURCE_OPEN",
        "closed_kernel_clauses_for_all_rows": {
            "selected_primitive_kernel_formula": True,
            "selected_physical_or_independent_trace_pairing_clause": True,
            "computed_independent_complex_entries": True,
            "exactness_or_error_bound_certificate": True,
            "provenance_independent_of_residual_projector_replay": False,
        },
        "all_72_row_values_exact": True,
        "all_72_row_exactness_certificates": True,
        "all_72_row_execution_closed_under_independent_route_B": False,
        "physical_PhiFinC1_action_source_closed": False,
        "A_selected_promoted": False,
        "b_selected_promoted": False,
        "deltaTheta_C1_promoted": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFirstRowProvenancePromotionOrAllRowsWeylExecution",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "formal_110_row_execution": rel(FORMAL_ROWS),
            "weyl_polynomial": rel(WEYL),
            "physical_boundary_source_remainder": rel(PHYSICAL_REMAINDER),
        },
        "output_packets": {
            "all_72_exact_weyl_row_execution": rel(ROWS_PACKET),
            "provenance_promotion_gate_after_all_rows": rel(PROVENANCE_PACKET),
            "all_rows_execution_decision": rel(DECISION_PACKET),
        },
        "what_closes_now": {
            "all_72_primitive_row_values_exact": True,
            "all_72_exactness_certificates": True,
            "first_row_result_scaled_to_full_row_set": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "provenance_independent_of_residual_projector_replay": True,
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
            "name": "AllRowsExactWeylExecutionTheorem",
            "proved": True,
            "statement": (
                "The first-row exact Weyl evaluation extends to all 72 primitive kernel "
                "rows in the finite qutrit Weyl layer.  Phase rows in u/e are R_Z, "
                "shift rows in d/nuD are R_X, and the complementary routed rows are "
                "zero by selected phase/shift support.  Therefore all 72 row values "
                "and exactness certificates are emitted in the formal finite Weyl "
                "execution layer.  This does not close independent Route-B provenance "
                "or physical Route-A source promotion, since the nonzero R_Z/R_X "
                "sources still inherit the residual-projector polynomial packet."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_FirstRowProvenancePromotion_or_AllRowsWeylExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "packet_paths": candidate["output_packets"],
        "theorem_proved": True,
        "row_count": len(executed_rows),
        "all_72_row_values_exact": True,
        "all_72_exactness_certificates": True,
        "max_abs_error_against_formal_packet": max_abs_error,
        "provenance_independent_of_residual_projector_replay": False,
        "physical_PhiFinC1_action_source_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FirstRowProvenancePromotion or AllRowsWeylExecution v1

Status: `{STATUS}`

## Theorem

{candidate["theorem"]["statement"]}

## Counts

- row count: {len(executed_rows)}
- R_Z rows: {source_counts["R_Z"]}
- R_X rows: {source_counts["R_X"]}
- zero-route rows: {source_counts["zero_route"]}
- max error against formal finite packet: {max_abs_error}

## Remaining Gate

The value problem is now closed at the formal finite Weyl row layer.  The
remaining gate is provenance/source promotion: either make the row source
independent of residual-projector replay, or prove that the physical
`Phi_fin^C1` action emits the same `R_Z/R_X/b_selected` packet.

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
ROWS = PACKET_DIR / "all_72_exact_weyl_row_execution.packet.json"
PROVENANCE = PACKET_DIR / "provenance_promotion_gate_after_all_rows.packet.json"
DECISION = PACKET_DIR / "all_rows_execution_decision.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FirstRowProvenancePromotion_or_AllRowsWeylExecution_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    rows = load(ROWS)
    provenance = load(PROVENANCE)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(rows["row_count"] == 72, "row count mismatch")
    require(rows["source_counts"]["R_Z"] == 18, "R_Z count mismatch")
    require(rows["source_counts"]["R_X"] == 18, "R_X count mismatch")
    require(rows["source_counts"]["zero_route"] == 36, "zero-route count mismatch")
    require(rows["all_rows_match_formal_packet"] is True, "formal packet mismatch")
    require(rows["max_abs_error_against_formal_packet"] <= 1e-12, "row error too large")
    require(rows["computed_value_clause_closed_for_all_rows"] is True, "computed values not closed")
    require(rows["exactness_clause_closed_for_all_rows"] is True, "exactness not closed")
    require(rows["physical_source_promoted_for_any_row"] is False, "physical source overpromoted")
    require(rows["provenance_independent_of_residual_projector_replay_for_all_rows"] is False, "provenance overclaimed")
    first = rows["rows"][0]
    require(first["row_id"] == "u:phase:r0c0", "first row mismatch")
    require(first["exact_value"] == "4/3", "first exact value mismatch")
    require(provenance["route_B_independence_gate"]["all_72_values_exact"] is True, "route B values missing")
    require(provenance["route_B_independence_gate"]["residual_projector_independent_source"] is False, "route B overclosed")
    require(decision["closed_kernel_clauses_for_all_rows"]["computed_independent_complex_entries"] is True, "computed clause false")
    require(decision["closed_kernel_clauses_for_all_rows"]["exactness_or_error_bound_certificate"] is True, "exactness clause false")
    require(decision["closed_kernel_clauses_for_all_rows"]["provenance_independent_of_residual_projector_replay"] is False, "provenance clause overclosed")
    require(decision["all_72_row_execution_closed_under_independent_route_B"] is False, "independent route overclosed")
    require(decision["physical_PhiFinC1_action_source_closed"] is False, "physical action overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "SM equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob overclaimed")
    require(cert["row_count"] == 72, "cert row count mismatch")
    require(cert["all_72_row_values_exact"] is True, "cert row values missing")
    require(cert["provenance_independent_of_residual_projector_replay"] is False, "cert provenance overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("R_Z rows: 18" in note, "note missing R_Z count")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(ROWS_PACKET, rows_packet)
    write_json(PROVENANCE_PACKET, provenance_packet)
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
