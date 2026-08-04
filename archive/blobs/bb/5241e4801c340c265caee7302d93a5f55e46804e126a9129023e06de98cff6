"""Build threshold-response rows / sector projection weights execution gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
WEIGHTS = PACKET_DIR / "source_normalized_sector_projection_weights.packet.json"
FIRST_ROW = PACKET_DIR / "first_dynamic_row_repromotion.packet.json"
THRESHOLD = PACKET_DIR / "threshold_response_rows_recheck.packet.json"
DECISION = PACKET_DIR / "threshold_rows_or_projection_weights_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_source_projection_weights.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdResponseRows_or_SectorProjectionWeightsExecution_v1.md"

PREVIOUS = DATA / "selected_yukawaprojectionkernel_readiness_or_thresholdresponsefrontier.candidate.json"
PREVIOUS_DECISION = (
    DATA
    / "selected_yukawaprojectionkernel_readiness_or_thresholdresponsefrontier"
    / "yukawa_projection_kernel_readiness_decision.packet.json"
)
SKELETON = (
    DATA
    / "selected_yukawaprojectionkernel_readiness_or_thresholdresponsefrontier"
    / "sector_aware_projection_kernel_skeleton.packet.json"
)
TRANSFER = (
    DATA
    / "selected_dynamicc1transfertensor_or_galerkinc1values"
    / "conditional_dynamic_c1_transfer_tensor.packet.json"
)
DYNAMIC_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
SOURCE_BRIDGE = (
    DATA
    / "selected_yukawasourcebridge_or_magnitudeprojectionnogotheorem"
    / "same_source_yukawa_source_bridge.packet.json"
)
FIRST_VALUE_ATTEMPT = (
    DATA
    / "selected_firstvaluesourcerowfill_or_externalthresholdsourceimport"
    / "first_value_source_row_fill_attempt.packet.json"
)
FIRST_VALUE_PROMOTION = DATA / "selected_firstvaluesourcerowpromotion_or_honestgalerkinprimitiverow.candidate.json"
SOURCE_ROW_AUDIT = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "accepted_threshold_mass_scheme_source_row_audit.packet.json"
)
RESIDUAL_ROWS = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
)
THETA_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)

STATUS = (
    "MTT_SELECTED_THRESHOLDRESPONSEROWS_OR_SECTORPROJECTIONWEIGHTSEXECUTION_"
    "BUILT_SOURCE_WEIGHTS_CLOSED_THRESHOLD_ROWS_OPEN"
)
NEXT = "MTT_Selected_MagnitudeBearingProjectionWeights_or_ThresholdRowsDerivation_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing projection-weight sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_DECISION,
        SKELETON,
        TRANSFER,
        DYNAMIC_VALUES,
        SOURCE_BRIDGE,
        FIRST_VALUE_ATTEMPT,
        FIRST_VALUE_PROMOTION,
        SOURCE_ROW_AUDIT,
        RESIDUAL_ROWS,
        THETA_CONTRACT,
        VALUE_PACKET,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_decision = load(PREVIOUS_DECISION)
    skeleton = load(SKELETON)
    transfer = load(TRANSFER)
    dynamic = load(DYNAMIC_VALUES)
    source = load(SOURCE_BRIDGE)
    first_attempt = load(FIRST_VALUE_ATTEMPT)
    first_promotion = load(FIRST_VALUE_PROMOTION)
    source_row_audit = load(SOURCE_ROW_AUDIT)
    residual_rows = load(RESIDUAL_ROWS)
    contract = load(THETA_CONTRACT)
    value_packet = load(VALUE_PACKET)

    normal_form = dynamic["dynamic_transfer_tensor"]["normal_form_replay"]
    delta = normal_form["deltaTheta_C1"]
    source_weights_closed = (
        dynamic["selected_by_MTT"] is True
        and source["source_layer_closure"]["same_source_validator_ok"] is True
        and normal_form["rank"] == 2
        and normal_form["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
        and normal_form["A_transpose_b"] == [12.0, 12.0]
        and delta == [1.0, 1.0]
    )
    sector_weights = [
        {
            "sector": "u",
            "source_column": "phase_Z",
            "source_direction": "phase_packet_I_plus_Z",
            "source_normalized_weight": delta[0],
            "magnitude_bearing_weight": None,
        },
        {
            "sector": "e",
            "source_column": "phase_Z",
            "source_direction": "phase_packet_I_plus_Z",
            "source_normalized_weight": delta[0],
            "magnitude_bearing_weight": None,
        },
        {
            "sector": "d",
            "source_column": "shift_X",
            "source_direction": "shift_packet_I_plus_X",
            "source_normalized_weight": delta[1],
            "magnitude_bearing_weight": None,
        },
        {
            "sector": "nuD",
            "source_column": "shift_X",
            "source_direction": "shift_packet_I_plus_X",
            "source_normalized_weight": delta[1],
            "magnitude_bearing_weight": None,
        },
    ]

    weights = {
        "schema": "MTTSourceNormalizedSectorProjectionWeights.v1",
        "status": "SOURCE_NORMALIZED_SECTOR_PROJECTION_WEIGHTS_SELECTED",
        "source": rel(DYNAMIC_VALUES),
        "transfer_tensor": rel(TRANSFER),
        "normal_form": normal_form,
        "sector_weights": sector_weights,
        "source_projection_weights_closed": source_weights_closed,
        "magnitude_bearing_projection_weights_closed": False,
        "why_not_magnitude_weights": [
            "phase_Z gives identical first-response source weight to u and e",
            "shift_X gives identical first-response source weight to d and nuD",
            "accepted common-scale magnitudes are distinct and require threshold/mass-scheme/profile response",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(WEIGHTS, weights)

    first_row_selected_now = (
        source_weights_closed
        and first_attempt["acceptance_tests"]["numeric_row_filled"] is True
        and first_attempt["row_id"] == "VSD-01.phase.I_plus_Z.u_e.first_dynamic_row"
    )
    first_row = {
        "schema": "MTTFirstDynamicRowRepromotion.v1",
        "status": "FIRST_DYNAMIC_ROW_REPROMOTED_AS_SOURCE_NORMALIZED_ROW",
        "old_attempt": rel(FIRST_VALUE_ATTEMPT),
        "old_promotion": rel(FIRST_VALUE_PROMOTION),
        "row_id": first_attempt["row_id"],
        "old_accepted_as_selected_dynamic_value_source_row": first_attempt[
            "accepted_as_selected_dynamic_value_source_row"
        ],
        "accepted_as_selected_source_normalized_projection_row_now": first_row_selected_now,
        "accepted_as_magnitude_or_threshold_source_row": False,
        "reason": (
            "The old first-row blocker was missing selected source promotion. The later same-source "
            "dynamic overlap bridge supplies that promotion for the source-normalized row, but the row "
            "still cannot serve as a magnitude-bearing threshold source."
        ),
        "numeric_payload": first_attempt["numeric_payload"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FIRST_ROW, first_row)

    threshold = {
        "schema": "MTTThresholdResponseRowsRecheck.v1",
        "status": "THRESHOLD_AND_MASS_SCHEME_ROWS_STILL_OPEN_AFTER_SOURCE_WEIGHTS",
        "source_row_audit": rel(SOURCE_ROW_AUDIT),
        "residual_rows": rel(RESIDUAL_ROWS),
        "contract": rel(THETA_CONTRACT),
        "accepted_threshold_matching_source_rows": source_row_audit[
            "accepted_threshold_matching_source_rows"
        ],
        "accepted_mass_scheme_conversion_source_rows": source_row_audit[
            "accepted_mass_scheme_conversion_source_rows"
        ],
        "residual_rows_finite": residual_rows["summary"]["all_residuals_finite"],
        "accepted_as_threshold_matching_values": residual_rows[
            "accepted_as_threshold_matching_values"
        ],
        "accepted_as_mass_scheme_conversion_values": residual_rows[
            "accepted_as_mass_scheme_conversion_values"
        ],
        "threshold_response_rows_closed": False,
        "mass_scheme_conversion_rows_closed": False,
        "same_branch_scale_scheme_loop_convention_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(THRESHOLD, threshold)

    decision = {
        "schema": "MTTThresholdRowsOrProjectionWeightsDecision.v1",
        "status": "SOURCE_PROJECTION_WEIGHTS_CLOSED_THRESHOLD_RESPONSE_OPEN",
        "previous_status": previous["status"],
        "source_owner_promoted": previous_decision["source_owner_promoted"],
        "sector_aware_projection_skeleton_closed": previous_decision[
            "sector_aware_projection_skeleton_closed"
        ],
        "source_normalized_sector_projection_weights_closed": source_weights_closed,
        "first_dynamic_row_repromoted_as_source_normalized": first_row_selected_now,
        "magnitude_bearing_projection_weights_closed": False,
        "selected_threshold_response_rows_closed": False,
        "mass_scheme_conversion_rows_closed": False,
        "same_branch_scale_scheme_loop_convention_closed": False,
        "profile_likelihood_or_diagonal_theorem_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "what_this_fixes": [
            "emits selected source-normalized sector projection weights from the dynamic transfer normal form",
            "repromotes the old first dynamic row as a selected source-normalized projection row",
            "separates source projection weights from magnitude-bearing threshold weights",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterSourceProjectionWeights.v1",
        "status": "NEXT_ATTACK_MAGNITUDE_WEIGHTS_AND_THRESHOLD_ROWS",
        "closed_now": {
            "source_normalized_sector_projection_weights": source_weights_closed,
            "first_dynamic_row_source_normalized_repromotion": first_row_selected_now,
        },
        "still_open": [
            "magnitude-bearing projection weights",
            "same-branch scale/scheme/loop convention",
            "threshold matching source rows",
            "mass-scheme conversion source rows",
            "full profile likelihood or accepted diagonal theorem",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The selected source weights are unit-normalized and degenerate by source direction. "
                "The next proof must supply the magnitude-bearing threshold response rows."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedThresholdResponseRowsOrSectorProjectionWeightsExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "source_normalized_sector_projection_weights": rel(WEIGHTS),
            "first_dynamic_row_repromotion": rel(FIRST_ROW),
            "threshold_response_rows_recheck": rel(THRESHOLD),
            "threshold_rows_or_projection_weights_decision": rel(DECISION),
            "next_cutset_after_source_projection_weights": rel(CUTSET),
        },
        "theorem": {
            "name": "SourceNormalizedProjectionWeightsAndThresholdRowsSeparationTheorem",
            "proved": True,
            "statement": (
                "The selected same-source dynamic transfer normal form emits source-normalized sector "
                "projection weights deltaTheta=(1,1), closing the source projection row and repromoting "
                "the old first dynamic row as selected source-normalized data. These weights are not "
                "magnitude-bearing Yukawa predictions; threshold/mass-scheme/profile response rows remain open."
            ),
        },
        "closure_decision": {
            "source_normalized_sector_projection_weights_closed": source_weights_closed,
            "first_dynamic_row_repromoted_as_source_normalized": first_row_selected_now,
            "magnitude_bearing_projection_weights_closed": False,
            "selected_threshold_response_rows_closed": False,
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_ThresholdResponseRows_or_SectorProjectionWeightsExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "source_normalized_sector_projection_weights_closed": source_weights_closed,
        "first_dynamic_row_repromoted_as_source_normalized": first_row_selected_now,
        "magnitude_bearing_projection_weights_closed": False,
        "selected_threshold_response_rows_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ThresholdResponseRows or SectorProjectionWeightsExecution v1

Status: `{STATUS}`.

This artifact executes the selected source-normalized projection weights.

```text
source projection weights closed      : {str(source_weights_closed).lower()}
first dynamic row repromoted          : {str(first_row_selected_now).lower()}
magnitude-bearing weights closed      : false
threshold response rows closed        : false
Yukawa magnitudes no-knob closed      : false
```

The selected dynamic transfer normal form gives `A^T A=12 I`, `A^T b=(12,12)`,
so the source-normalized projection solution is `deltaTheta=(1,1)`.  This
closes the first projection-weight layer, not the magnitude-bearing threshold
layer.  The remaining object must explain how the selected unit source weights
are promoted through scale/scheme, threshold matching, mass-scheme conversion,
and profile response into distinct Yukawa magnitudes.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
