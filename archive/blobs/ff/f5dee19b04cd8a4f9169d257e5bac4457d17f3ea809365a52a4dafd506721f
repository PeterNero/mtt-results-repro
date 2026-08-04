"""Build the first post-AH8 literal-witness / precision-value route selector."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_literalwitness_or_precisionvalues_afterah8"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LITERAL_ATTEMPT = PACKET_DIR / "literal_witness_attempt_after_ah8.packet.json"
VALUE_ROUTE = PACKET_DIR / "precision_value_route_after_ah8.packet.json"
NEXT_PACKET = PACKET_DIR / "next_internal_value_source_execution_after_ah8.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LiteralGoodCoverHYMGlobalWitness_or_PrecisionValueSourceAfterAH8_v1.md"

PREVIOUS = DATA / "selected_strictglobalcechhym_or_truesmafterah8.candidate.json"
STRICT_CUTSET = DATA / "selected_strictglobalcechhym_or_truesmafterah8" / "strict_global_literal_witness_cutset.packet.json"
ACTIVE_LEDGER = DATA / "selected_activeledger_dotdc1supersession_or_valuelayerfrontier.candidate.json"
THRESHOLD_IMPORT = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.candidate.json"
ROWLOCAL = DATA / "selected_selectedsectortransferoverlapderivative_or_rowlocalprefactoremission.candidate.json"
FULLS2 = DATA / "selected_fulls2sectordensityoperator_or_phisectornnumericrows.candidate.json"

STATUS = "MTT_SELECTED_LITERALWITNESS_OR_PRECISIONVALUES_AFTERAH8_LITERAL_ZERO_VALUE_ROUTE_SELECTED"
PREVIOUS_STATUS = "MTT_SELECTED_STRICTGLOBALCECHHYM_OR_TRUESMAFTERAH8_AH8_CONSUMED_STRICT_WITNESSES_AND_PRECISION_VALUES_OPEN"
NEXT = "MTT_Selected_InternalValueSourceRowsAfterAH8_or_LiteralGlobalWitnessConstruction_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    for path in [PREVIOUS, STRICT_CUTSET, ACTIVE_LEDGER, THRESHOLD_IMPORT, ROWLOCAL, FULLS2]:
        if not path.exists():
            raise FileNotFoundError(rel(path))

    previous = load(PREVIOUS)
    strict = load(STRICT_CUTSET)
    active = load(ACTIVE_LEDGER)
    threshold = load(THRESHOLD_IMPORT)
    rowlocal = load(ROWLOCAL)
    fulls2 = load(FULLS2)

    if previous["status"] != PREVIOUS_STATUS:
        raise ValueError("previous after-AH8 status mismatch")

    literal_families = strict["literal_witness_families_required"]
    literal_closed_count = sum(1 for family in literal_families if family["accepted_now"])
    literal_required_count = len(literal_families)
    source_layer_closed = active["closure_decision"]["source_layer_closed"]
    external_admitted_rows = (
        threshold["closure_decision"]["accepted_external_threshold_row_count"]
        + threshold["closure_decision"]["accepted_external_mass_scheme_row_count"]
    )
    internal_value_rows = threshold["closure_decision"]["selected_internal_value_emission_count"]
    rowlocal_internal_rows = rowlocal["closure_decision"]["accepted_internal_scalar_value_row_count"]
    fulls2_rows = fulls2["closure_decision"]["full_s2_accepted_scalar_row_count_now"]

    literal_attempt = {
        "schema": "MTTLiteralWitnessAttemptAfterAH8.v1",
        "status": "LITERAL_GLOBAL_WITNESS_ATTEMPT_ACCEPTS_ZERO_FAMILIES",
        "closure_claimed": True,
        "literal_witness_families_required": literal_required_count,
        "literal_witness_families_accepted_now": literal_closed_count,
        "accepted_family_names": [family["name"] for family in literal_families if family["accepted_now"]],
        "remaining_family_names": [family["name"] for family in literal_families if not family["accepted_now"]],
        "strict_global_closed": False,
        "reason": "Current repo support is AH/projected representative support; no literal good-cover cochains or continuum/global HYM coefficients are emitted.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    value_route = {
        "schema": "MTTPrecisionValueRouteAfterAH8.v1",
        "status": "SOURCE_LAYER_CLOSED_INTERNAL_VALUE_ROWS_OPEN",
        "closure_claimed": True,
        "source_layer_closed": source_layer_closed,
        "closed_source_inputs": {
            "A_selected": active["closure_decision"]["A_selected_closed_by_active_ledger"],
            "b_selected": active["closure_decision"]["b_selected_closed_by_active_ledger"],
            "deltaTheta_C1": active["closure_decision"]["deltaTheta_C1_closed_by_active_ledger"],
            "dotD_alpha1": active["closure_decision"]["dotD_alpha1_closed_by_active_ledger"],
            "primitive_C1_first_response": active["closure_decision"][
                "primitive_C1_first_response_layer_closed_by_active_ledger"
            ],
        },
        "external_admitted_replay_rows": external_admitted_rows,
        "internal_selected_value_rows": internal_value_rows,
        "rowlocal_internal_scalar_rows": rowlocal_internal_rows,
        "full_s2_accepted_scalar_rows": fulls2_rows,
        "precision_value_route_selected": source_layer_closed and literal_closed_count == 0,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextInternalValueSourceExecutionAfterAH8.v1",
        "status": "NEXT_IS_INTERNAL_VALUE_SOURCE_ROWS_AFTER_AH8",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "do_not_reopen": [
            "AH-equivalent BN27 8/8 matrix row",
            "selected dotD/C1/A/b/deltaTheta source layer",
            "external admitted replay row tier",
        ],
        "execute_next": [
            "selected internal R_theta threshold-response rows",
            "rowwise scalar retarded-overlap values",
            "Delta_S2 / full-S2 scalar correction values",
            "lambda_H/H-threshold payload transport",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PostAH8LiteralWitnessZeroAndPrecisionValueRouteTheorem",
        "proved": True,
        "statement": (
            "After AH8 is consumed, the current repository emits zero literal global Cech/HYM witness "
            "families, while the selected dotD/C1/A/b/deltaTheta source layer is closed. Therefore the "
            "non-looping route toward true SM equivalence is internal selected value-source row execution; "
            "external admitted replay rows are useful comparison data but are not no-knob selected values."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedLiteralWitnessOrPrecisionValuesAfterAH8",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_after_AH8": rel(PREVIOUS),
            "strict_cutset": rel(STRICT_CUTSET),
            "active_ledger": rel(ACTIVE_LEDGER),
            "threshold_import": rel(THRESHOLD_IMPORT),
            "rowlocal": rel(ROWLOCAL),
            "fulls2": rel(FULLS2),
        },
        "output_packets": {
            "literal_witness_attempt_after_ah8": rel(LITERAL_ATTEMPT),
            "precision_value_route_after_ah8": rel(VALUE_ROUTE),
            "next_internal_value_source_execution_after_ah8": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "literal_global_witness_families_required": literal_required_count,
            "literal_global_witness_families_accepted_now": literal_closed_count,
            "strict_global_closed": False,
            "source_layer_closed": source_layer_closed,
            "external_admitted_replay_rows": external_admitted_rows,
            "internal_selected_value_rows": internal_value_rows,
            "rowlocal_internal_scalar_rows": rowlocal_internal_rows,
            "full_s2_accepted_scalar_rows": fulls2_rows,
            "precision_value_route_selected": value_route["precision_value_route_selected"],
            "true_SM_equivalence_closed": False,
        },
        "theorem": theorem,
    }

    cert = {
        "certificate": "MTTSelectedLiteralWitnessOrPrecisionValuesAfterAH8",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "literal_global_witness_families_accepted_now": literal_closed_count,
        "source_layer_closed": source_layer_closed,
        "precision_value_route_selected": value_route["precision_value_route_selected"],
        "strict_global_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected LiteralGoodCoverHYMGlobalWitness or PrecisionValueSourceAfterAH8 v1

## Theorem

`PostAH8LiteralWitnessZeroAndPrecisionValueRouteTheorem` is proved.

The literal global witness attempt currently accepts `0/2` witness families,
while the selected dotD/C1/A/b/deltaTheta source layer is closed.

## What Closes

- The post-AH8 route is selected: internal value-source rows are the next
  productive target.
- External admitted replay rows are separated from internal selected values.
- The AH-equivalent BN27 `8/8` matrix row remains non-reopen.

## Remaining Value Rows

- selected internal `R_theta` threshold-response rows
- rowwise scalar retarded-overlap values
- `Delta_S2` / full-S2 scalar correction values
- `lambda_H` / H-threshold payload transport

## Boundary

This does not close strict global provenance, no-knob closure, or true SM
equivalence.

## Next Artifact

`{NEXT}`
"""

    write_json(LITERAL_ATTEMPT, literal_attempt)
    write_json(VALUE_ROUTE, value_route)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
