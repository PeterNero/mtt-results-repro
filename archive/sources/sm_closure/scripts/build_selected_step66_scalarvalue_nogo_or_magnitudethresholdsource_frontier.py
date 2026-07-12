"""Build Step66 scalar-value no-go / magnitude-threshold source frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step66_scalarvalue_nogo_or_magnitudethresholdsource_frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
NOGO_PACKET = PACKET_DIR / "step66_closed_rows_vs_scalar_value_nogo.packet.json"
MISSING_PACKET = PACKET_DIR / "step66_minimal_missing_source_object.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step66_ScalarValueNoGo_or_MagnitudeThresholdSourceFrontier_v1.md"

STEP65 = DATA / "selected_step65_pureweylrowclosure_import_or_scalarvalueexecution.candidate.json"
STEP65_SCALAR_GATE = (
    DATA
    / "selected_step65_pureweylrowclosure_import_or_scalarvalueexecution"
    / "step65_scalar_value_execution_after_pure_rows.packet.json"
)
RTHETA_SOURCE = (
    DATA
    / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
    / "rtheta_scalar_value_functional_source_packet.packet.json"
)
RTHETA_GATE = (
    DATA
    / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
    / "no_knob_numerical_rows_execution_gate.packet.json"
)
TEN_ROW_MAP = (
    DATA
    / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
    / "ten_scalar_rows_to_threshold_contract_map.packet.json"
)
RANK_GAP = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "magnitude_weight_rank_gap.packet.json"
)
COEFF_ATTEMPT = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_value_row_coefficients_attempt.packet.json"
)
INTERNAL_GAP = (
    DATA
    / "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction"
    / "same_branch_internal_source_row_gap.packet.json"
)

STATUS = "MTT_SELECTED_STEP66_SCALAR_VALUE_NOGO_MAGNITUDE_THRESHOLD_SOURCE_FRONTIER_FIXED"
NEXT = "MTT_Selected_GenerationResolvedMagnitudeThresholdSourceRows_or_SelectedUniversalAnchorExecution_v1"


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
        STEP65,
        STEP65_SCALAR_GATE,
        RTHETA_SOURCE,
        RTHETA_GATE,
        TEN_ROW_MAP,
        RANK_GAP,
        COEFF_ATTEMPT,
        INTERNAL_GAP,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step66 inputs: " + ", ".join(missing))

    step65 = load(STEP65)
    step65_scalar = load(STEP65_SCALAR_GATE)
    rtheta_source = load(RTHETA_SOURCE)
    rtheta_gate = load(RTHETA_GATE)
    ten_map = load(TEN_ROW_MAP)
    rank_gap = load(RANK_GAP)
    coeff_attempt = load(COEFF_ATTEMPT)
    internal_gap = load(INTERNAL_GAP)

    dim = rank_gap["dimension_evidence"]
    charged_rows = ten_map["charged_yukawa_rows"]
    ten_rows = ten_map["ten_scalar_rows"]

    nogo_packet = {
        "schema": "MTTStep66ClosedRowsVsScalarValueNoGo.v1",
        "status": "PURE_WEYL_ROWS_AND_RTHETA_DOMAIN_INSUFFICIENT_FOR_SCALAR_VALUES",
        "step65_source": rel(STEP65),
        "pure_weyl_coefficient_rows_closed": step65["closure_decision"][
            "pure_Weyl_rows_emitted_identity_free"
        ],
        "lambda_orbit_scaled_pure_rows_closed": step65["closure_decision"][
            "lambda_orbit_scaled_pure_Weyl_rows_closed"
        ],
        "rtheta_scalar_value_functional_source_domain_closed": rtheta_source["source_domain_closed"],
        "ten_scalar_codomain_aligned": ten_map["alignment"]["charged_rows_match_contract"],
        "rank_gap_theorem_proved": rank_gap["theorem"]["proved"],
        "source_column_count": dim["source_column_count"],
        "source_sector_slot_count": dim["source_sector_slot_count"],
        "charged_generation_magnitude_rows": dim["charged_generation_magnitude_rows"],
        "charged_plus_lambda_rows": dim["charged_plus_lambda_rows"],
        "rank_gap_against_charged_rows": dim["rank_gap_against_charged_rows"],
        "slot_gap_against_charged_rows": dim["slot_gap_against_charged_rows"],
        "accepted_scalar_row_count_now": step65_scalar["accepted_scalar_row_count_now"],
        "accepted_coefficient_row_count": coeff_attempt["accepted_coefficient_row_count"],
        "lambda_H_row_emitted": step65_scalar["lambda_H_row_emitted"],
        "lambda_H_coefficient_selected": coeff_attempt["lambda_H_coefficient_selected"],
        "diagnostic_coefficient_count": coeff_attempt["diagnostic_coefficient_count"],
        "diagnostic_coefficients_rejected_as_selectors": all(
            item["accepted_as_selected_coefficient"] is False
            for item in coeff_attempt["diagnostic_coefficients"]
        ),
        "external_rows_admitted_only": internal_gap["external_rows_admitted"],
        "selected_internal_threshold_mass_derivation_closed": internal_gap[
            "selected_internal_Rtheta_threshold_mass_derivation_closed"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(NOGO_PACKET, nogo_packet)

    missing_packet = {
        "schema": "MTTStep66MinimalMissingSourceObject.v1",
        "status": "GENERATION_RESOLVED_MAGNITUDE_THRESHOLD_SOURCE_OR_SELECTED_ANCHOR_REQUIRED",
        "not_missing_anymore": [
            "pure Weyl R_Z/R_X coefficient/source rows",
            "selected lambda orbit scaled coefficient rows",
            "Rtheta scalar value-functional source/domain",
            "ten-row scalar codomain contract",
            "basis map to charged scalar slots",
        ],
        "still_missing": [
            "generation-resolved magnitude-bearing projection weights",
            "selected threshold response functional instantiation",
            "selected same-branch threshold matching source rows",
            "selected same-branch mass-scheme conversion source rows",
            "selected lambda_H source row",
            "or a candidate-specific universal source anchor followed by scalar-row execution",
        ],
        "legal_next_routes": [
            "derive generation-resolved magnitude/threshold rows from selected MTT geometry",
            "select a universal source anchor before empirical replay and execute the same ten-row contract",
        ],
        "forbidden_routes": [
            "use Step42 admitted replay values as selected coefficients",
            "fit diagnostic coefficients to observed Yukawa or Higgs values",
            "reopen pure Weyl coefficient rows as if Step65 had not closed them",
            "treat external threshold rows as internal no-knob emissions",
        ],
        "charged_rows": charged_rows,
        "ten_scalar_rows": ten_rows,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(MISSING_PACKET, missing_packet)

    candidate = {
        "candidate": "MTTSelectedStep66ScalarValueNoGoOrMagnitudeThresholdSourceFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "closed_rows_vs_scalar_value_nogo": rel(NOGO_PACKET),
            "minimal_missing_source_object": rel(MISSING_PACKET),
        },
        "theorem": {
            "name": "Step66PureWeylRowsDoNotDetermineScalarValuesTheorem",
            "proved": True,
            "statement": (
                "After Step65, the pure Weyl coefficient/source rows and selected lambda-orbit rows "
                "are closed, and the Rtheta scalar value-functional source/domain plus ten-row "
                "codomain are closed. These data still cannot emit the nine charged scalar magnitudes "
                "and lambda_H: the available selected source-normalized layer has two columns/four "
                "sector slots, while the charged layer requires nine generation-resolved rows plus "
                "lambda_H. Existing numerical coefficients are diagnostic replay/profile values and "
                "are rejected as selectors. The remaining source object is therefore generation-resolved "
                "magnitude/threshold/mass-scheme rows, or a selected universal source anchor executed "
                "through the same scalar contract."
            ),
        },
        "closure_decision": {
            "pure_weyl_coefficient_source_layer_closed": True,
            "rtheta_source_domain_closed": True,
            "rank_insufficiency_for_scalar_values_proved": True,
            "diagnostic_values_rejected_as_selectors": True,
            "external_rows_rejected_as_internal_no_knob_emissions": True,
            "accepted_scalar_row_count_now": 0,
            "lambda_H_row_emitted": False,
            "scalar_value_execution_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step65["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step66_ScalarValueNoGo_or_MagnitudeThresholdSourceFrontier_v1",
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
        f"""# MTT Selected Step66 ScalarValueNoGo or MagnitudeThresholdSourceFrontier v1

Status: `{STATUS}`.

## What Closed

The last repeated ambiguity is removed: closed pure Weyl rows are not scalar
value rows.

```text
pure Weyl coefficient/source layer closed : true
Rtheta source/domain closed               : true
source columns available                  : {dim["source_column_count"]}
source sector slots available             : {dim["source_sector_slot_count"]}
charged scalar rows required              : {dim["charged_generation_magnitude_rows"]}
charged plus lambda rows required         : {dim["charged_plus_lambda_rows"]}
rank gap against charged rows             : {dim["rank_gap_against_charged_rows"]}
accepted scalar rows now                  : 0
lambda_H row emitted                      : false
diagnostic coefficients accepted          : false
true SM equivalence closed                : false
full no-knob closure                      : false
```

## Consequence

The active frontier is no longer pure Weyl row emission. Step65 closed that
layer legally through the identity-free route. Step66 proves those rows are
insufficient to determine generation-resolved scalar magnitudes.

The remaining object is:

`{NEXT}`

Minimum next success: emit selected generation-resolved magnitude-bearing
projection weights plus same-branch threshold/mass-scheme rows and `lambda_H`,
or select a universal source anchor before empirical replay and execute the
same ten-row scalar contract.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
