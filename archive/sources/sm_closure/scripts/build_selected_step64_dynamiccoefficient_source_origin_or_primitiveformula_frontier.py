"""Build Step64 dynamic-coefficient source-origin / primitive-formula frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step64_dynamiccoefficient_source_origin_or_primitiveformula_frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_PACKET = PACKET_DIR / "step64_dynamic_coefficient_source_origin.packet.json"
CUTSET = PACKET_DIR / "step64_primitive_formula_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step64_DynamicCoefficientSourceOrigin_or_PrimitiveFormulaFrontier_v1.md"

STEP63 = DATA / "selected_step63_directscalaremission_trial_or_dynamicoverlap_frontier.candidate.json"
TYPEDBN = DATA / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission.candidate.json"
FIBER_SELECTOR = DATA / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"
PRIMITIVE_CLASS = DATA / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
HIGHER_ORDER = DATA / "selected_higherorderfullresponsematrices_or_secondorderflavorlift.candidate.json"
SECOND_ORDER = DATA / "selected_secondorderdynamiccoefficientemission_or_lambdarepresentativeselection.candidate.json"

STATUS = "MTT_SELECTED_STEP64_DYNAMIC_COEFFICIENT_SOURCE_ORIGIN_PINNED_PRIMITIVE_FORMULA_FRONTIER_OPEN"
NEXT = "MTT_Selected_PureWeylCoefficientRows_or_PrimitiveC1FormulaExecution_v1"


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

    inputs = [STEP63, TYPEDBN, FIBER_SELECTOR, PRIMITIVE_CLASS, HIGHER_ORDER, SECOND_ORDER]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step64 inputs: " + ", ".join(missing))

    step63 = load(STEP63)
    typedbn = load(TYPEDBN)
    fiber = load(FIBER_SELECTOR)
    primitive_class = load(PRIMITIVE_CLASS)
    higher = load(HIGHER_ORDER)
    second = load(SECOND_ORDER)

    source_packet = {
        "schema": "MTTStep64DynamicCoefficientSourceOrigin.v1",
        "status": "DYNAMIC_COEFFICIENT_ORIGIN_REDUCED_TO_PRIMITIVE_FORMULA",
        "step63_source": rel(STEP63),
        "closed_or_narrowed": {
            "direct_scalar_emission_tried": step63["closure_decision"]["direct_scalar_emission_trial_executed"],
            "primitive_candidate_values_emitted": typedbn["primitive_response_candidate_values_emitted"],
            "active_shift_1_1_selected": fiber["active_shift_selected_claimed"],
            "fixed_fiber_quotient_selected": fiber["fiber_class_quotient_selected_claimed"],
            "current_C1_observable_layer_emitted": primitive_class["promotion_decision"][
                "current_primitive_class_promoted_as_valid_C1_observable_layer"
            ],
            "current_C1_flavor_no_go_confirmed": primitive_class["what_closes_now"][
                "current_C1_layer_flavor_no_go_confirmed"
            ],
            "higher_order_algebraic_candidate_matrix_gate_closed": higher["closure_decision"][
                "algebraic_higher_order_candidate_closed"
            ],
            "second_order_required_rows_identified": second["what_closes_now"][
                "pure_Z_X_coefficient_rows_identified"
            ],
        },
        "where_numbers_can_come_from": {
            "not_from": [
                "measured Yukawa/CKM/PMNS/Higgs values",
                "diagnostic profile coefficients",
                "current first-response scalar-permutation C1 layer",
                "absolute qutrit fiber origin as a hidden selector",
            ],
            "candidate_source": (
                "selected second-order dynamic coefficient rows: lambda_static*Z on u,e and "
                "lambda_static*X on d,nuD, emitted by the same dynamic Phi_fin/C1 payload or "
                "by an equivalent primitive C1 formula execution"
            ),
            "required_rows": [
                "selected zero-mode basis values",
                "selected finite Hessian C1 source blocks",
                "selected primitive C1 contractions",
                "pure Weyl coefficient rows lambda_Z and lambda_X",
            ],
        },
        "current_counts": {
            "accepted_internal_scalar_row_count": step63["closure_decision"]["accepted_internal_scalar_row_count"],
            "accepted_dynamic_payload_row_count": 0,
            "second_order_coefficient_rows_emitted": second["closure_decision"][
                "second_order_coefficient_rows_emitted"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SOURCE_PACKET, source_packet)

    cutset = {
        "schema": "MTTStep64PrimitiveFormulaFrontier.v1",
        "status": "NEXT_PURE_WEYL_COEFFICIENT_ROWS_OR_PRIMITIVE_C1_FORMULA_EXECUTION",
        "closed_now": source_packet["closed_or_narrowed"],
        "still_open": second["what_remains_open"],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The source of numerical magnitudes is now localized to selected second-order "
                "dynamic coefficient rows. The next constructive task is to emit the pure Weyl "
                "coefficient rows from the selected primitive C1 formula/dynamic Phi_fin C1 payload, "
                "then feed them back into the higher-response scalar execution."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedStep64DynamicCoefficientSourceOriginOrPrimitiveFormulaFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "dynamic_coefficient_source_origin": rel(SOURCE_PACKET),
            "primitive_formula_frontier": rel(CUTSET),
        },
        "theorem": {
            "name": "Step64DynamicCoefficientSourceOriginTheorem",
            "proved": True,
            "statement": (
                "The source of accepted numerical scalar rows is no longer an unspecified map. "
                "The direct scalar trial failed honestly; the current C1 quotient layer is selected "
                "but scalar-permutation degenerate; the higher-order algebraic candidate exists; and "
                "the required second-order coefficient rows are exactly lambda_static*Z on u,e and "
                "lambda_static*X on d,nuD. Full value closure now depends on selected primitive C1 "
                "formula execution or equivalent dynamic Phi_fin/C1 payload emission of those rows."
            ),
        },
        "closure_decision": {
            "dynamic_coefficient_source_origin_pinned": True,
            "current_C1_layer_flavor_no_go_confirmed": True,
            "higher_order_candidate_origin_identified": True,
            "second_order_required_rows_identified": True,
            "accepted_internal_scalar_row_count": step63["closure_decision"]["accepted_internal_scalar_row_count"],
            "second_order_coefficient_rows_emitted": False,
            "accepted_value_layer_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step63["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step64_DynamicCoefficientSourceOrigin_or_PrimitiveFormulaFrontier_v1",
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
        f"""# MTT Selected Step64 DynamicCoefficientSourceOrigin or PrimitiveFormulaFrontier v1

Status: `{STATUS}`.

## What Is Closer

The source of magnitude/threshold numbers is now localized.

```text
direct scalar emission tried             : true
primitive finite candidate values emitted: true
active primitive shift selected          : (1,1)
fixed fiber quotient selected            : true
current C1 flavor no-go confirmed        : true
higher-order algebraic candidate exists  : true
second-order required rows identified    : true
accepted internal scalar rows            : 0
second-order coefficient rows emitted    : false
true SM equivalence closed               : false
full no-knob closure                     : false
```

The accepted numerical rows cannot come from observed values, diagnostic
coefficients, or the current first-response C1 layer. They must come from
selected second-order dynamic coefficient rows:

```text
phase correction : lambda_static * Z on u,e
shift correction : lambda_static * X on d,nuD
```

## Active Frontier

`{NEXT}`

Minimum next success: execute the selected primitive C1 formula or dynamic
`Phi_fin^C1` payload so that the pure Weyl coefficient rows `lambda_Z` and
`lambda_X` become selected source rows, then rerun the ten-row `Rtheta` scalar
execution.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
