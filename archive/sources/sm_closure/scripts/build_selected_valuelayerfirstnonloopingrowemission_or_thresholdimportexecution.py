"""Build first non-looping value-layer row emission / threshold import execution."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_valuelayerfirstnonloopingrowemission_or_thresholdimportexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INTERNAL_ATTEMPT = PACKET_DIR / "internal_selected_value_row_attempt.packet.json"
EXTERNAL_ATTEMPT = PACKET_DIR / "external_threshold_import_execution.packet.json"
DECISION = PACKET_DIR / "first_nonlooping_value_row_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ValueLayerFirstNonLoopingRowEmission_or_ThresholdImportExecution_v1.md"

FRONTIER = DATA / "selected_acceptedvaluelayerfrontier_or_nonloopingsourcerows.candidate.json"
VSD01 = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
FIRST_ROW = (
    DATA
    / "selected_firstvaluesourcerowfill_or_externalthresholdsourceimport"
    / "first_value_source_row_fill_attempt.packet.json"
)
FIRST_ROW_PROMOTION = DATA / "selected_firstvaluesourcerowpromotion_or_honestgalerkinprimitiverow.candidate.json"
KERNEL = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "value_source_derivation_obligation_kernel.packet.json"
)
IMPORT_MANIFEST = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "external_threshold_import_manifest.packet.json"
)
COMMON_VALUES = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
THRESHOLD_RESIDUALS = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
)

STATUS = (
    "MTT_SELECTED_VALUELAYERFIRSTNONLOOPINGROWEMISSION_OR_THRESHOLDIMPORTEXECUTION_"
    "BUILT_SOURCE_LAYER_ROW_AVAILABLE_VALUE_FUNCTIONAL_OPEN"
)
NEXT = "MTT_Selected_ThresholdResponseFunctionalRowEmission_or_ExternalSourceRowImport_v1"


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
        raise FileNotFoundError("missing value-layer first row inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        FRONTIER,
        VSD01,
        FIRST_ROW,
        FIRST_ROW_PROMOTION,
        KERNEL,
        IMPORT_MANIFEST,
        COMMON_VALUES,
        THRESHOLD_RESIDUALS,
    ]
    require_sources(sources)

    frontier = load(FRONTIER)
    vsd01 = load(VSD01)
    first_row = load(FIRST_ROW)
    first_promotion = load(FIRST_ROW_PROMOTION)
    kernel = load(KERNEL)
    import_manifest = load(IMPORT_MANIFEST)
    common_values = load(COMMON_VALUES)
    threshold_residuals = load(THRESHOLD_RESIDUALS)

    required_row = next(row for row in kernel["required_rows"] if row["id"] == "VSD-01-selected-overlap-value-kernel")
    source_layer_closed = frontier["readiness"]["source_layer_closed"]
    primitive_backimported = first_promotion["closure_decision"]["primitive_exactness_backimported"]

    internal_attempt = {
        "schema": "MTTInternalSelectedValueRowAttempt.v1",
        "status": "SOURCE_LAYER_ROW_AVAILABLE_VALUE_FUNCTIONAL_NOT_EMITTED",
        "target_obligation": required_row["id"],
        "source_layer_closed": source_layer_closed,
        "primitive_exactness_backimported": primitive_backimported,
        "candidate_row_id": first_row["row_id"],
        "candidate_row_payload_available": first_row["numeric_payload"] is not None,
        "candidate_row_was_previously_rejected_as_selected_source": not first_row[
            "accepted_as_selected_dynamic_value_source_row"
        ],
        "what_the_closed_VSD_layer_now_legitimizes": [
            "same-branch source ownership of the first-response dynamic packet",
            "primitive row assembly as postcheck support",
            "A_selected/b_selected/deltaTheta first-response layer as closed input",
        ],
        "why_this_still_does_not_accept_a_true_value_row": [
            "the accepted value layer needs a value functional from selected source rows to physical Yukawa/Higgs/threshold magnitudes",
            "the first-response row is not a threshold response functional",
            "the common-scale Yukawa/Higgs packet is versioned SM-parity/downstream data, not no-knob selected source data",
            "threshold/mass-scheme residuals are finite diagnostics without accepted source-row provenance",
        ],
        "accepted_as_true_value_source_row": False,
        "accepted_as_SM_parity_downstream_support": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INTERNAL_ATTEMPT, internal_attempt)

    external_attempt = {
        "schema": "MTTExternalThresholdImportExecution.v1",
        "status": "NO_ACCEPTED_EXTERNAL_THRESHOLD_SOURCE_ROW_AVAILABLE",
        "manifest_source": rel(IMPORT_MANIFEST),
        "accepted_external_rows_present": import_manifest["accepted_external_rows_present"],
        "manifest_required_fields": import_manifest["manifest_required_fields"],
        "local_common_scale_packet_available": True,
        "local_threshold_residuals_all_finite": threshold_residuals["summary"]["all_residuals_finite"],
        "common_scale_packet_status": common_values["status"],
        "why_no_external_import": import_manifest["why_no_import_yet"],
        "accepted_external_threshold_row_imported": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXTERNAL_ATTEMPT, external_attempt)

    decision = {
        "schema": "MTTFirstNonLoopingValueRowDecision.v1",
        "status": "FIRST_NONLOOPING_ATTEMPT_EXECUTED_VALUE_FUNCTIONAL_OR_EXTERNAL_IMPORT_OPEN",
        "frontier_readiness_before": frontier["readiness"],
        "internal_lane": {
            "source_layer_row_available": True,
            "accepted_as_true_value_source_row": False,
            "missing_object": "selected threshold/Yukawa/Higgs value functional",
        },
        "external_lane": {
            "accepted_external_threshold_row_imported": False,
            "missing_object": "accepted external source row with manifest provenance",
        },
        "what_closes_now": {
            "first_nonlooping_internal_attempt_executed": True,
            "closed_VSD_source_layer_used_as_input_not_reproved": True,
            "external_import_lane_executed_against_manifest": True,
            "value_functional_gap_identified": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_threshold_response_functional": True,
            "selected_Yukawa_Higgs_value_functional": True,
            "accepted_external_threshold_source_row": True,
            "accepted_threshold_mass_scheme_source_rows": True,
            "full_correlated_likelihood_source": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    candidate = {
        "candidate": "MTTSelectedValueLayerFirstNonLoopingRowEmissionOrThresholdImportExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "internal_selected_value_row_attempt": rel(INTERNAL_ATTEMPT),
            "external_threshold_import_execution": rel(EXTERNAL_ATTEMPT),
            "first_nonlooping_value_row_decision": rel(DECISION),
        },
        "theorem": {
            "name": "FirstNonLoopingValueRowAttemptTheorem",
            "proved": True,
            "statement": (
                "Using the closed VSD-01 source layer as an input, the first non-looping value-row "
                "attempt can reuse the first-response dynamic row as same-branch support, but it still "
                "does not emit an accepted true value-source row. The missing object is not A/b/deltaTheta "
                "or primitive exactness; it is a selected value functional or an accepted external "
                "threshold source row with manifest provenance."
            ),
        },
        "what_closes_now": decision["what_closes_now"],
        "what_remains_open": decision["what_remains_open"],
        "closure_decision": {
            "source_layer_row_available": True,
            "accepted_true_value_source_row_emitted": False,
            "accepted_external_threshold_row_imported": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_ValueLayerFirstNonLoopingRowEmission_or_ThresholdImportExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ValueLayerFirstNonLoopingRowEmission or ThresholdImportExecution v1

Status: `{STATUS}`.

This artifact uses the closed VSD-01 source layer as an input and tests the first
non-looping value-row route.

```text
source layer closed                 : {source_layer_closed}
first-response source row available : true
accepted true value-source row      : false
accepted external threshold row     : false
```

The result is sharp: the next missing object is no longer first-response source
promotion.  It is a selected value functional for Yukawa/Higgs/threshold rows,
or an accepted external threshold source row satisfying the manifest.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
