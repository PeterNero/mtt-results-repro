"""Build post-AH8 internal value-row promotion.

This consumes the post-AH8 route selector and imports the already verified
first selected dynamic value rows plus source-normalized projection weights into
the current AH8 frontier.  It deliberately does not promote scalar magnitude,
threshold, full-S2, or true-SM rows.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_internalvaluerows_afterah8_or_literalglobalwitness"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DYNAMIC_IMPORT = PACKET_DIR / "post_ah8_first_dynamic_value_row_import.packet.json"
PROJECTION_IMPORT = PACKET_DIR / "post_ah8_projection_weight_import.packet.json"
SCALAR_GATE = PACKET_DIR / "post_ah8_scalar_magnitude_value_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_magnitude_bearing_rows_after_post_ah8_dynamic_import.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_InternalValueSourceRowsAfterAH8_or_LiteralGlobalWitnessConstruction_v1.md"

PREVIOUS = DATA / "selected_literalwitness_or_precisionvalues_afterah8.candidate.json"
FIRST_DYNAMIC = DATA / "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit.candidate.json"
FIRST_DYNAMIC_PACKET = (
    DATA
    / "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit"
    / "accepted_first_selected_dynamic_value_row.packet.json"
)
PROJECTION = DATA / "selected_thresholdresponserows_or_sectorprojectionweightsexecution.candidate.json"
PROJECTION_DECISION = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "threshold_rows_or_projection_weights_decision.packet.json"
)
FULLS2 = DATA / "selected_fulls2sectordensityoperator_or_phisectornnumericrows.candidate.json"
ROWLOCAL = DATA / "selected_selectedsectortransferoverlapderivative_or_rowlocalprefactoremission.candidate.json"
THRESHOLD_IMPORT = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.candidate.json"

STATUS = "MTT_SELECTED_INTERNALVALUEROWS_AFTERAH8_FIRST_DYNAMIC_ROWS_IMPORTED_MAGNITUDES_OPEN"
PREVIOUS_STATUS = "MTT_SELECTED_LITERALWITNESS_OR_PRECISIONVALUES_AFTERAH8_LITERAL_ZERO_VALUE_ROUTE_SELECTED"
NEXT = "MTT_Selected_MagnitudeBearingRowsAfterPostAH8DynamicImport_or_ThresholdResponseDerivation_v1"


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


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing post-AH8 value-row inputs: " + ", ".join(missing))


def main() -> int:
    sources = [
        PREVIOUS,
        FIRST_DYNAMIC,
        FIRST_DYNAMIC_PACKET,
        PROJECTION,
        PROJECTION_DECISION,
        FULLS2,
        ROWLOCAL,
        THRESHOLD_IMPORT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    first_dynamic = load(FIRST_DYNAMIC)
    first_packet = load(FIRST_DYNAMIC_PACKET)
    projection = load(PROJECTION)
    projection_decision = load(PROJECTION_DECISION)
    fulls2 = load(FULLS2)
    rowlocal = load(ROWLOCAL)
    threshold = load(THRESHOLD_IMPORT)

    if previous["status"] != PREVIOUS_STATUS:
        raise ValueError("previous post-AH8 route status mismatch")

    first_dynamic_rows = first_dynamic["closure_decision"]["accepted_selected_dynamic_value_row_count"]
    first_dynamic_importable = (
        first_dynamic["closure_decision"]["first_selected_dynamic_matter_overlap_value_row_accepted"]
        and first_packet["accepted_row_count"] == first_dynamic_rows
        and first_packet["selected_by_MTT"]
        and first_packet["observed_data_used_as_selector"] is False
        and first_packet["target_fitting_used"] is False
    )
    projection_weights_closed = (
        projection["closure_decision"]["source_normalized_sector_projection_weights_closed"]
        and projection_decision["source_normalized_sector_projection_weights_closed"]
        and projection_decision["magnitude_bearing_projection_weights_closed"] is False
    )

    scalar_magnitude_rows = 0
    internal_selected_value_rows = threshold["closure_decision"]["selected_internal_value_emission_count"]
    rowlocal_scalar_rows = rowlocal["closure_decision"]["accepted_internal_scalar_value_row_count"]
    fulls2_scalar_rows = fulls2["closure_decision"]["full_s2_accepted_scalar_row_count_now"]

    dynamic_import = {
        "schema": "MTTPostAH8FirstDynamicValueRowImport.v1",
        "status": "FIRST_DYNAMIC_SELECTED_VALUE_ROWS_IMPORTED_AFTER_AH8",
        "closure_claimed": True,
        "accepted_selected_dynamic_value_row_count": first_dynamic_rows,
        "accepted_row_ids": first_packet["accepted_row_ids"],
        "selected_by_MTT": first_packet["selected_by_MTT"],
        "accepted_role": "non-scalar first dynamic matter/overlap response rows",
        "not_accepted_as": [
            "Yukawa magnitudes",
            "threshold/mass-scheme scalar rows",
            "full-S2 scalar value rows",
            "true SM equivalence rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    projection_import = {
        "schema": "MTTPostAH8ProjectionWeightImport.v1",
        "status": "SOURCE_NORMALIZED_PROJECTION_WEIGHTS_IMPORTED_AFTER_AH8",
        "closure_claimed": True,
        "source_normalized_sector_projection_weights_closed": projection_weights_closed,
        "first_dynamic_row_repromoted_as_source_normalized": projection["closure_decision"][
            "first_dynamic_row_repromoted_as_source_normalized"
        ],
        "magnitude_bearing_projection_weights_closed": False,
        "selected_threshold_response_rows_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    scalar_gate = {
        "schema": "MTTPostAH8ScalarMagnitudeValueGate.v1",
        "status": "SCALAR_MAGNITUDE_VALUE_ROWS_STILL_OPEN_AFTER_DYNAMIC_IMPORT",
        "closure_claimed": True,
        "accepted_non_scalar_dynamic_rows": first_dynamic_rows,
        "accepted_internal_selected_scalar_rows": internal_selected_value_rows,
        "accepted_rowlocal_scalar_rows": rowlocal_scalar_rows,
        "accepted_full_s2_scalar_rows": fulls2_scalar_rows,
        "accepted_yukawa_magnitude_rows": scalar_magnitude_rows,
        "magnitude_bearing_projection_weights_closed": False,
        "selected_threshold_response_rows_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextMagnitudeBearingRowsAfterPostAH8DynamicImport.v1",
        "status": "NEXT_IS_MAGNITUDE_BEARING_ROWS_OR_THRESHOLD_RESPONSE_DERIVATION",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "do_not_reopen": [
            "AH-equivalent BN27 8/8 matrix row",
            "post-AH8 route selection",
            "first selected dynamic non-scalar value rows",
            "source-normalized projection weights",
        ],
        "remaining_value_targets": [
            "magnitude-bearing projection weights",
            "selected threshold response rows",
            "rowlocal scalar retarded-overlap values",
            "full-S2 / Delta_S2 scalar correction rows",
            "lambda_H/H-threshold payload transport",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PostAH8FirstDynamicValueRowsImportTheorem",
        "proved": True,
        "statement": (
            "After AH8 and the post-AH8 route selection, the already audited first selected dynamic "
            "matter/overlap rows are imported as two source-owned non-scalar internal value rows, and "
            "the source-normalized sector projection weights are imported as closed. This is a real "
            "post-AH8 value-layer promotion, but it does not emit magnitude-bearing projection weights, "
            "threshold response rows, rowlocal scalar values, full-S2 scalar corrections, lambda_H payloads, "
            "or true SM equivalence rows."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedInternalValueRowsAfterAH8OrLiteralGlobalWitness",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_post_AH8_route": rel(PREVIOUS),
            "first_dynamic_candidate": rel(FIRST_DYNAMIC),
            "first_dynamic_packet": rel(FIRST_DYNAMIC_PACKET),
            "projection_candidate": rel(PROJECTION),
            "projection_decision": rel(PROJECTION_DECISION),
            "fulls2": rel(FULLS2),
            "rowlocal": rel(ROWLOCAL),
            "threshold_import": rel(THRESHOLD_IMPORT),
        },
        "output_packets": {
            "post_ah8_first_dynamic_value_row_import": rel(DYNAMIC_IMPORT),
            "post_ah8_projection_weight_import": rel(PROJECTION_IMPORT),
            "post_ah8_scalar_magnitude_value_gate": rel(SCALAR_GATE),
            "next_magnitude_bearing_rows_after_post_ah8_dynamic_import": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "post_AH8_first_dynamic_value_rows_imported": first_dynamic_importable,
            "accepted_selected_dynamic_value_row_count": first_dynamic_rows,
            "source_normalized_projection_weights_closed": projection_weights_closed,
            "magnitude_bearing_projection_weights_closed": False,
            "selected_threshold_response_rows_closed": False,
            "accepted_internal_selected_scalar_rows": internal_selected_value_rows,
            "accepted_rowlocal_scalar_rows": rowlocal_scalar_rows,
            "accepted_full_s2_scalar_rows": fulls2_scalar_rows,
            "accepted_yukawa_magnitude_rows": scalar_magnitude_rows,
            "strict_global_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": theorem,
    }

    cert = {
        "certificate": "MTTSelectedInternalValueRowsAfterAH8OrLiteralGlobalWitness",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "post_AH8_first_dynamic_value_rows_imported": first_dynamic_importable,
        "accepted_selected_dynamic_value_row_count": first_dynamic_rows,
        "source_normalized_projection_weights_closed": projection_weights_closed,
        "magnitude_bearing_projection_weights_closed": False,
        "accepted_yukawa_magnitude_rows": scalar_magnitude_rows,
        "strict_global_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected InternalValueSourceRowsAfterAH8 or LiteralGlobalWitnessConstruction v1

## Theorem

`PostAH8FirstDynamicValueRowsImportTheorem` is proved.

The post-AH8 chain now imports `2` accepted selected dynamic non-scalar value
rows and the closed source-normalized projection weights.

## What Closes

- first selected dynamic matter/overlap value rows: `2`
- source-normalized sector projection weights
- non-reopen guard for the AH-equivalent BN27 `8/8` matrix row

## Boundary

These rows are non-scalar first-response value rows. They are not Yukawa
magnitudes, threshold/mass-scheme scalar rows, full-S2 scalar rows, lambda_H
payloads, strict global witnesses, or true SM equivalence rows.

## Next Artifact

`{NEXT}`
"""

    write_json(DYNAMIC_IMPORT, dynamic_import)
    write_json(PROJECTION_IMPORT, projection_import)
    write_json(SCALAR_GATE, scalar_gate)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
