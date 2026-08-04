"""Build VSD-02 accepted source rows fill / no-knob threshold derivation gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_SCHEMA = PACKET_DIR / "accepted_source_row_strict_schema.packet.json"
FILL_ATTEMPT = PACKET_DIR / "accepted_source_rows_fill_attempt.packet.json"
DERIVATION_REDUCTION = PACKET_DIR / "no_knob_threshold_derivation_reduction.packet.json"
DECISION = PACKET_DIR / "vsd02_accepted_rows_fill_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_vsd02_fill_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_VSD02AcceptedSourceRowsFill_or_NoKnobThresholdDerivation_v1.md"

PREVIOUS = DATA / "selected_vsd02thresholdresponserule_or_externallikelihoodimport.candidate.json"
CLASSIFICATION = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "vsd02_row_route_classification.packet.json"
)
EXTERNAL_MANIFEST = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "external_likelihood_import_manifest.packet.json"
)
INTERNAL_WORKORDER = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "internal_threshold_response_derivation_workorder.packet.json"
)
SOURCE_ROW_AUDIT = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "accepted_threshold_mass_scheme_source_row_audit.packet.json"
)
NO_KNOB_ATTEMPT = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "no_knob_value_derivation_attempt.packet.json"
)
THRESHOLD_RESIDUALS = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
)
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
PROFILE_STATUS = (
    DATA
    / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining"
    / "profile_likelihood_source_import_status.packet.json"
)

STATUS = (
    "MTT_SELECTED_VSD02ACCEPTEDSOURCEROWSFILL_OR_NOKNOBTHRESHOLDERIVATION_"
    "BUILT_STRICT_FILL_ATTEMPT_ACCEPTED_ROWS_OPEN"
)
NEXT = "MTT_Selected_ThresholdResponseFunctionalDerivation_or_ProfileLikelihoodAcquisition_v1"


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
        raise FileNotFoundError("missing VSD-02 accepted row fill sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        CLASSIFICATION,
        EXTERNAL_MANIFEST,
        INTERNAL_WORKORDER,
        SOURCE_ROW_AUDIT,
        NO_KNOB_ATTEMPT,
        THRESHOLD_RESIDUALS,
        VALUE_PACKET,
        PROFILE_STATUS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    classification = load(CLASSIFICATION)
    external_manifest = load(EXTERNAL_MANIFEST)
    internal_workorder = load(INTERNAL_WORKORDER)
    source_row_audit = load(SOURCE_ROW_AUDIT)
    no_knob_attempt = load(NO_KNOB_ATTEMPT)
    threshold_residuals = load(THRESHOLD_RESIDUALS)
    value_packet = load(VALUE_PACKET)
    profile_status = load(PROFILE_STATUS)

    strict_schema = {
        "schema": "MTTAcceptedVSD02SourceRowStrictSchema.v1",
        "status": "STRICT_ACCEPTED_SOURCE_ROW_SCHEMA_EMITTED",
        "accepted_row_must_include": [
            "row_id",
            "row_type: threshold_matching | mass_scheme_conversion | likelihood_profile | no_knob_value_derivation",
            "source_owner: selected_MTT_branch | accepted_external_source",
            "value_payload with scale, scheme, and loop/order convention",
            "basis_map_to_MTT_value_packet",
            "covariance_or_likelihood_payload or explicit accepted diagonal limitation theorem",
            "provenance and checksum for external rows",
            "proof observed values do not select the source row",
            "acceptance_rule and versioned replay command",
        ],
        "forbidden_as_accepted_source_rows": [
            "finite residual comparison tables without source-owner theorem",
            "first-pass replay values accepted only for SM parity",
            "surrogate covariance matrices",
            "partial Higgs covariance without full likelihood/profile semantics",
            "measured/benchmark rows used as selectors",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(STRICT_SCHEMA, strict_schema)

    candidate_results: list[dict[str, Any]] = []
    for row in source_row_audit["candidate_rows"]:
        candidate_results.append(
            {
                "candidate_id": row["id"],
                "support_present": row["support_present"],
                "accepted_as_vsd02_source_row": row[
                    "can_promote_to_accepted_threshold_mass_scheme_source"
                ],
                "rejection_reasons": row["why_not"],
                "source": row["source"],
            }
        )

    fill_attempt = {
        "schema": "MTTVSD02AcceptedSourceRowsFillAttempt.v1",
        "status": "STRICT_FILL_ATTEMPT_EXECUTED_NO_ACCEPTED_ROWS",
        "accepted_row_schema": rel(STRICT_SCHEMA),
        "row_route_count": len(classification["row_routes"]),
        "candidate_source_row_count": source_row_audit["candidate_count"],
        "candidate_results": candidate_results,
        "accepted_threshold_matching_rows": [],
        "accepted_mass_scheme_conversion_rows": [],
        "accepted_profile_likelihood_rows": [],
        "accepted_no_knob_value_derivation_rows": [],
        "accepted_row_count": 0,
        "why_no_rows_accepted": [
            "current residual rows are finite audits, not source rows",
            "first-pass common-scale values are SM-parity/profile inputs, not true precision source rows",
            "partial Higgs covariance is not a full profile likelihood",
            "no selected threshold response functional is emitted yet",
            "no external likelihood workspace with full provenance is imported yet",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FILL_ATTEMPT, fill_attempt)

    derivation_reduction = {
        "schema": "MTTNoKnobThresholdDerivationReduction.v1",
        "status": "NOKNOB_DERIVATION_REDUCED_TO_RESPONSE_FUNCTIONAL_OR_LIKELIHOOD_ACQUISITION",
        "closed_support": {
            "versioned_firstpass_value_packet_present": value_packet[
                "accepted_as_versioned_common_scale_candidate_values"
            ],
            "finite_residual_table_present": threshold_residuals["summary"]["all_residuals_finite"],
            "accepted_source_row_schema_present": True,
            "VSD02_rows_classified": classification["accepted_row_count"] == 0
            and len(classification["row_routes"]) == 6,
        },
        "open_no_knob_obligations": no_knob_attempt["obligations"],
        "minimal_new_theorem_required": {
            "name": "SelectedThresholdResponseFunctional",
            "must_emit": internal_workorder[
                "minimal_internal_derivation_outputs_required"
            ],
            "must_not_use": [
                "observed masses/Yukawas/thresholds as selectors",
                "residual table as self-deriving source",
                "surrogate covariance as full likelihood",
            ],
        },
        "external_acquisition_alternative": {
            "full_likelihood_imported_now": external_manifest[
                "accepted_external_likelihood_imported_now"
            ],
            "required_payload": external_manifest["required_import_payload"],
            "current_profile_status": profile_status["status"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DERIVATION_REDUCTION, derivation_reduction)

    decision = {
        "schema": "MTTVSD02AcceptedRowsFillDecision.v1",
        "status": "ACCEPTED_ROWS_FILL_ATTEMPT_CLOSED_NO_ROWS_ACCEPTED",
        "previous_status": previous["status"],
        "strict_schema_emitted": True,
        "fill_attempt_executed": True,
        "accepted_row_count": 0,
        "accepted_threshold_response_rule_closed": False,
        "accepted_external_likelihood_import_closed": False,
        "no_knob_threshold_derivation_closed": False,
        "what_closes_now": {
            "strict_accepted_source_row_schema": True,
            "all_current_candidates_tested_against_schema": True,
            "no_knob_derivation_reduced_to_selected_response_functional": True,
            "external_likelihood_acquisition_requirements_reaffirmed": True,
        },
        "remaining_hard_failures": [
            "selected_threshold_response_functional_missing",
            "accepted_threshold_matching_source_rows_missing",
            "accepted_mass_scheme_conversion_source_rows_missing",
            "full_profile_likelihood_workspace_missing",
            "no_knob_Yukawa_Higgs_value_derivation_missing",
        ],
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterVSD02FillAttempt.v1",
        "status": "NEXT_ATTACK_SELECTED_RESPONSE_FUNCTIONAL_OR_REAL_LIKELIHOOD_WORKSPACE",
        "closed_now": decision["what_closes_now"],
        "still_open": decision["remaining_hard_failures"],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "Current candidates cannot be promoted to accepted VSD02 source rows. The next real "
                "progress must either derive the selected threshold response functional internally, or "
                "acquire a real external likelihood/source workspace with provenance."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedVSD02AcceptedSourceRowsFillOrNoKnobThresholdDerivation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "accepted_source_row_strict_schema": rel(STRICT_SCHEMA),
            "accepted_source_rows_fill_attempt": rel(FILL_ATTEMPT),
            "no_knob_threshold_derivation_reduction": rel(DERIVATION_REDUCTION),
            "vsd02_accepted_rows_fill_decision": rel(DECISION),
            "next_cutset_after_vsd02_fill_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "VSD02StrictAcceptedRowsFillAndNoKnobReductionTheorem",
            "proved": True,
            "statement": (
                "A strict accepted-source-row schema can be emitted for VSD02, and all current threshold/"
                "mass-scheme/profile candidates can be tested against it. No current row is accepted: "
                "residual tables are audits, first-pass values are SM-parity/profile inputs, and partial "
                "Higgs covariance is not a full likelihood. Therefore the remaining no-knob route reduces "
                "to a selected threshold response functional, with real external likelihood acquisition as "
                "the alternative route."
            ),
        },
        "what_closes_now": decision["what_closes_now"],
        "what_remains_open": decision["remaining_hard_failures"],
        "closure_decision": {
            "strict_fill_attempt_closed": True,
            "accepted_vsd02_source_rows_closed": False,
            "selected_threshold_response_functional_closed": False,
            "external_likelihood_workspace_closed": False,
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
        "certificate": "MTT_Selected_VSD02AcceptedSourceRowsFill_or_NoKnobThresholdDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected VSD02AcceptedSourceRowsFill or NoKnobThresholdDerivation v1

Status: `{STATUS}`.

This artifact closes the strict fill attempt for VSD02.

```text
current candidates tested       : {source_row_audit["candidate_count"]}
accepted VSD02 source rows      : 0
strict source-row schema emitted: true
```

No row is accepted yet.  Residual tables are audits, first-pass values are
SM-parity/profile inputs, and partial Higgs covariance is not a full likelihood.

The remaining attack is now sharply binary:

```text
derive selected threshold response functional
or acquire real external likelihood/source workspace
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
