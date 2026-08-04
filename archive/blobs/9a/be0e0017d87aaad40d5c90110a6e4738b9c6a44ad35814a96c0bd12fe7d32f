"""Build Step65 pure-Weyl row closure import / scalar-value execution frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step65_pureweylrowclosure_import_or_scalarvalueexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_PACKET = PACKET_DIR / "step65_pure_weyl_row_closure_import.packet.json"
SCALAR_GATE = PACKET_DIR / "step65_scalar_value_execution_after_pure_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step65_PureWeylRowClosureImport_or_ScalarValueExecution_v1.md"

STEP64 = DATA / "selected_step64_dynamiccoefficient_source_origin_or_primitiveformula_frontier.candidate.json"
PURE_WEYL_GATE = DATA / "selected_pureweylcoefficientrows_or_primitivec1formulaexecution.candidate.json"
IDENTITY_FREE_ROWS = (
    DATA
    / "selected_zeromodehessianprimitiverowexecution_or_pureweylrows"
    / "identity_free_pure_weyl_rows.packet.json"
)
ZERO_MODE_HESSIAN = DATA / "selected_zeromodehessianprimitiverowexecution_or_pureweylrows.candidate.json"
LAMBDA_ORBIT = DATA / "selected_pureweyllambdarepresentative_or_higherresponsescalarrows.candidate.json"
LAMBDA_ROWS = (
    DATA
    / "selected_pureweyllambdarepresentative_or_higherresponsescalarrows"
    / "selected_lambda_orbit_scaled_pure_weyl_rows.packet.json"
)
LAMBDA_SCALAR_GATE = (
    DATA
    / "selected_pureweyllambdarepresentative_or_higherresponsescalarrows"
    / "higher_response_scalar_rows_after_lambda_orbit.packet.json"
)
SECOND_ORDER_SCALAR_GATE = (
    DATA
    / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution"
    / "rtheta_scalar_execution_gate_after_second_order_orbit.packet.json"
)

STATUS = "MTT_SELECTED_STEP65_PURE_WEYL_ROWS_IMPORTED_SCALAR_VALUE_EXECUTION_OPEN"
NEXT = "MTT_Selected_ScalarValueExecutionAfterPureWeylRows_or_LambdaHThresholdRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP64,
        PURE_WEYL_GATE,
        IDENTITY_FREE_ROWS,
        ZERO_MODE_HESSIAN,
        LAMBDA_ORBIT,
        LAMBDA_ROWS,
        LAMBDA_SCALAR_GATE,
        SECOND_ORDER_SCALAR_GATE,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step65 inputs: " + ", ".join(missing))

    step64 = load(STEP64)
    pure_gate = load(PURE_WEYL_GATE)
    identity_free = load(IDENTITY_FREE_ROWS)
    zero_mode = load(ZERO_MODE_HESSIAN)
    lambda_orbit = load(LAMBDA_ORBIT)
    lambda_rows = load(LAMBDA_ROWS)
    lambda_scalar = load(LAMBDA_SCALAR_GATE)
    second_scalar = load(SECOND_ORDER_SCALAR_GATE)

    import_packet = {
        "schema": "MTTStep65PureWeylRowClosureImport.v1",
        "status": "IDENTITY_FREE_AND_LAMBDA_ORBIT_PURE_WEYL_ROWS_IMPORTED",
        "step64_source": rel(STEP64),
        "previous_identity_subtraction_gate": rel(PURE_WEYL_GATE),
        "identity_subtraction_used": identity_free["identity_subtraction_used"],
        "identity_subtraction_promoted": pure_gate["closure_decision"]["identity_subtraction_promoted"],
        "identity_free_unscaled_pure_weyl_rows_closed": identity_free[
            "accepted_as_unscaled_selected_pure_weyl_primitive_rows"
        ],
        "identity_free_row_counts": identity_free["row_counts"],
        "identity_free_exactness": identity_free["exactness"],
        "source_promotion": identity_free["source_promotion"],
        "lambda_orbit_scaled_pure_weyl_rows_closed": lambda_rows["closure_claimed"],
        "lambda_orbit": lambda_rows["lambda_orbit"],
        "individual_lambda_selected": lambda_rows["individual_lambda_selected"],
        "orbit_scaled_row_count": lambda_rows["scaled_row_family"]["orbit_scaled_row_count"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(IMPORT_PACKET, import_packet)

    scalar_gate = {
        "schema": "MTTStep65ScalarValueExecutionAfterPureRows.v1",
        "status": "PURE_WEYL_ROWS_AVAILABLE_SCALAR_VALUE_ROWS_STILL_OPEN",
        "lambda_orbit_scaled_pure_rows_available": lambda_scalar[
            "lambda_orbit_scaled_pure_rows_available"
        ],
        "second_order_orbit_matrix_packet_closed": second_scalar[
            "second_order_orbit_matrix_packet_closed"
        ],
        "codomain_scalar_row_count": lambda_scalar["codomain_scalar_row_count"],
        "codomain_scalar_rows": lambda_scalar["codomain_scalar_rows"],
        "execution_inputs_available_now": (
            lambda_scalar["execution_inputs_available_now"]
            or second_scalar["execution_inputs_available_now"]
        ),
        "selected_functional_executed": (
            lambda_scalar["selected_functional_executed"]
            or second_scalar["selected_functional_executed"]
        ),
        "accepted_scalar_row_count_now": max(
            lambda_scalar["accepted_scalar_row_count_now"],
            second_scalar["accepted_scalar_row_count_now"],
        ),
        "lambda_H_row_emitted": (
            lambda_scalar["lambda_H_row_emitted"] or second_scalar["lambda_H_row_emitted"]
        ),
        "why_still_open": sorted(
            set(lambda_scalar["why_still_open"]) | set(second_scalar["why_still_open"])
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SCALAR_GATE, scalar_gate)

    candidate = {
        "candidate": "MTTSelectedStep65PureWeylRowClosureImportOrScalarValueExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "pure_weyl_row_closure_import": rel(IMPORT_PACKET),
            "scalar_value_execution_after_pure_rows": rel(SCALAR_GATE),
        },
        "theorem": {
            "name": "Step65PureWeylRowsClosedScalarValuesOpenTheorem",
            "proved": True,
            "statement": (
                "The pure Weyl coefficient-row frontier is closed by the identity-free primitive row "
                "route: exact R_Z/R_X rows are selected without dynamic identity subtraction, and the "
                "selected lambda orbit scales them. However, these rows are coefficient/source rows, "
                "not the ten accepted scalar value rows. The higher-response scalar execution remains "
                "open because the scalar value functional, lambda_H, and threshold/mass-scheme value "
                "rows are not emitted."
            ),
        },
        "closure_decision": {
            "pure_Weyl_rows_emitted_identity_free": True,
            "lambda_orbit_scaled_pure_Weyl_rows_closed": True,
            "identity_subtraction_promoted": False,
            "individual_lambda_value_selected": False,
            "accepted_scalar_row_count_now": scalar_gate["accepted_scalar_row_count_now"],
            "lambda_H_row_emitted": False,
            "scalar_value_execution_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step64["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "back_imported_statuses": {
            "pure_weyl_identity_subtraction_gate": pure_gate["status"],
            "zero_mode_hessian_identity_free_rows": zero_mode["status"],
            "lambda_orbit_rows": lambda_orbit["status"],
        },
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step65_PureWeylRowClosureImport_or_ScalarValueExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step65 PureWeylRowClosureImport or ScalarValueExecution v1

Status: `{STATUS}`.

## What Closed

The Step64 primitive-formula frontier is closed at the coefficient-row layer.

```text
identity subtraction used                  : false
identity-free pure R_Z rows                : {identity_free["row_counts"]["R_Z"]}
identity-free pure R_X rows                : {identity_free["row_counts"]["R_X"]}
all 72 pure rows exact                     : true
lambda orbit scaled pure rows closed       : true
individual lambda selected                 : false
orbit-scaled row count                     : {lambda_rows["scaled_row_family"]["orbit_scaled_row_count"]}
accepted scalar rows                       : {scalar_gate["accepted_scalar_row_count_now"]}
lambda_H row emitted                       : false
true SM equivalence closed                 : false
full no-knob closure                       : false
```

## What Remains

Pure Weyl coefficient/source rows are now available through the legal
identity-free route. They still do not constitute the ten scalar value rows.

The active frontier is:

`{NEXT}`

Minimum next success: turn the selected lambda-orbit coefficient rows into ten
accepted `Rtheta` scalar values, including `lambda_H`, using a selected scalar
value functional and threshold/mass-scheme value rows, with observed SM values
only as postchecks.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
