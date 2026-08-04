"""Build VSD-02 threshold response rule / external likelihood import classifier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CLASSIFICATION = PACKET_DIR / "vsd02_row_route_classification.packet.json"
EXTERNAL_MANIFEST = PACKET_DIR / "external_likelihood_import_manifest.packet.json"
INTERNAL_WORKORDER = PACKET_DIR / "internal_threshold_response_derivation_workorder.packet.json"
DECISION = PACKET_DIR / "vsd02_threshold_response_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_vsd02_classification.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_VSD02ThresholdResponseRule_or_ExternalLikelihoodImport_v1.md"

FRONTIER = DATA / "selected_vsd01frontierupdate_or_valuekernelv2.candidate.json"
FRONTIER_CUTSET = (
    DATA
    / "selected_vsd01frontierupdate_or_valuekernelv2"
    / "next_atomic_value_source_cutset.packet.json"
)
THRESHOLD_AUDIT = DATA / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport.candidate.json"
THRESHOLD_RESIDUALS = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
)
SOURCE_ROW_AUDIT = DATA / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation.candidate.json"
SOURCE_ROW_AUDIT_PACKET = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "accepted_threshold_mass_scheme_source_row_audit.packet.json"
)
SOURCE_ROW_CUTSET = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "next_cutset_after_source_row_audit.packet.json"
)
ACCEPTED_VALUES = DATA / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution.candidate.json"
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
PROFILE_IMPORT = DATA / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining.candidate.json"
PROFILE_STATUS = (
    DATA
    / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining"
    / "profile_likelihood_source_import_status.packet.json"
)
EXTERNAL_HIGGS = DATA / "selected_externalprofilelikelihoodimport_or_qasu3slotselectionproof.candidate.json"
EXTERNAL_HIGGS_COV = (
    DATA
    / "selected_externalprofilelikelihoodimport_or_qasu3slotselectionproof"
    / "external_higgs_decay_correlation_covariance_import.packet.json"
)
HIGGS_IMPORTED = DATA / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood.candidate.json"
OFFICIAL_HIGGS_GATE = (
    DATA
    / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood"
    / "official_lhchxswg_likelihood_gate.packet.json"
)
OFFICIAL_HIGGS_AUDIT = (
    DATA
    / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihooddecision"
    / "official_likelihood_source_audit.packet.json"
)
THRESHOLD_CONTRACT = (
    DATA
    / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
    / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_VSD02THRESHOLDRESPONSERULE_OR_EXTERNALLIKELIHOODIMPORT_"
    "BUILT_ROUTE_CLASSIFICATION_ACCEPTED_ROWS_OPEN"
)
NEXT = "MTT_Selected_VSD02AcceptedSourceRowsFill_or_NoKnobThresholdDerivation_v1"


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
        raise FileNotFoundError("missing VSD-02 classifier sources: " + ", ".join(missing))


def route_row(row_id: str, accepted: bool, partial: bool, internal_support: bool, external_support: bool, missing: list[str]) -> dict[str, Any]:
    if accepted:
        bucket = "accepted_now"
    elif internal_support and not external_support:
        bucket = "internal_derivation_candidate_open"
    elif external_support and not internal_support:
        bucket = "external_import_candidate_open"
    elif internal_support and external_support:
        bucket = "dual_route_open"
    elif partial:
        bucket = "partial_support_not_accepted"
    else:
        bucket = "missing_source_theorem"
    return {
        "row_id": row_id,
        "bucket": bucket,
        "accepted_now": accepted,
        "partial_support_present": partial,
        "internal_derivation_support_present": internal_support,
        "external_import_support_present": external_support,
        "missing_for_acceptance": missing,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        FRONTIER,
        FRONTIER_CUTSET,
        THRESHOLD_AUDIT,
        THRESHOLD_RESIDUALS,
        SOURCE_ROW_AUDIT,
        SOURCE_ROW_AUDIT_PACKET,
        SOURCE_ROW_CUTSET,
        ACCEPTED_VALUES,
        VALUE_PACKET,
        PROFILE_IMPORT,
        PROFILE_STATUS,
        EXTERNAL_HIGGS,
        EXTERNAL_HIGGS_COV,
        HIGGS_IMPORTED,
        OFFICIAL_HIGGS_GATE,
        OFFICIAL_HIGGS_AUDIT,
        THRESHOLD_CONTRACT,
    ]
    require_sources(sources)

    frontier = load(FRONTIER)
    frontier_cutset = load(FRONTIER_CUTSET)
    threshold_audit = load(THRESHOLD_AUDIT)
    threshold_residuals = load(THRESHOLD_RESIDUALS)
    source_row_audit = load(SOURCE_ROW_AUDIT)
    source_row_audit_packet = load(SOURCE_ROW_AUDIT_PACKET)
    source_row_cutset = load(SOURCE_ROW_CUTSET)
    accepted_values = load(ACCEPTED_VALUES)
    value_packet = load(VALUE_PACKET)
    profile_import = load(PROFILE_IMPORT)
    profile_status = load(PROFILE_STATUS)
    external_higgs = load(EXTERNAL_HIGGS)
    external_higgs_cov = load(EXTERNAL_HIGGS_COV)
    higgs_imported = load(HIGGS_IMPORTED)
    official_higgs_gate = load(OFFICIAL_HIGGS_GATE)
    official_higgs_audit = load(OFFICIAL_HIGGS_AUDIT)
    threshold_contract = load(THRESHOLD_CONTRACT)

    rows = [
        route_row(
            "VSD02-threshold-matching-values",
            accepted=False,
            partial=threshold_residuals["summary"]["all_residuals_finite"],
            internal_support=True,
            external_support=False,
            missing=[
                "selected threshold response functional",
                "accepted threshold matching source values",
                "multi-loop threshold convention",
            ],
        ),
        route_row(
            "VSD02-mass-scheme-conversion-values",
            accepted=False,
            partial=threshold_residuals["summary"]["all_residuals_finite"],
            internal_support=True,
            external_support=False,
            missing=[
                "accepted mass-scheme conversion rows",
                "scheme/source provenance",
                "basis map to common-scale Yukawa/Higgs packet",
            ],
        ),
        route_row(
            "VSD02-full-profile-likelihood",
            accepted=False,
            partial=profile_status["surrogate_profile_retained"],
            internal_support=False,
            external_support=False,
            missing=profile_status["required_import_payload"],
        ),
        route_row(
            "VSD02-Higgs-decay-covariance-profile",
            accepted=False,
            partial=external_higgs_cov["import_result"][
                "accepted_as_Higgs_decay_covariance_profile_candidate"
            ],
            internal_support=False,
            external_support=True,
            missing=[
                "official full likelihood or nuisance/profile semantics",
                "non-Higgs observable covariance/profile rows",
                "accepted true-equivalence profile rule",
            ],
        ),
        route_row(
            "VSD02-official-LHCHXSWG-likelihood",
            accepted=False,
            partial=official_higgs_audit["published_profile_replay_available"],
            internal_support=False,
            external_support=False,
            missing=official_higgs_audit["required_for_official_likelihood_promotion"],
        ),
        route_row(
            "VSD02-no-knob-Yukawa-Higgs-value-derivation",
            accepted=False,
            partial=True,
            internal_support=True,
            external_support=False,
            missing=[
                "selected threshold response rule from MTT branch",
                "no-knob source derivation for Y_u/Y_d/Y_e/lambda_H magnitudes",
                "proof values are not benchmark/observed selector rows",
            ],
        ),
    ]

    classification = {
        "schema": "MTTVSD02RowRouteClassification.v1",
        "status": "VSD02_ROWS_CLASSIFIED_ACCEPTED_ROWS_OPEN",
        "target": "VSD-02-threshold-response-rule",
        "frontier_source": rel(FRONTIER),
        "row_routes": rows,
        "bucket_counts": {
            bucket: sum(1 for row in rows if row["bucket"] == bucket)
            for bucket in sorted({row["bucket"] for row in rows})
        },
        "accepted_row_count": sum(1 for row in rows if row["accepted_now"]),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CLASSIFICATION, classification)

    external_manifest = {
        "schema": "MTTExternalLikelihoodImportManifest.v1",
        "status": "PARTIAL_HIGGS_COVARIANCE_PRESENT_FULL_LIKELIHOOD_ABSENT",
        "accepted_external_likelihood_imported_now": False,
        "partial_external_rows": {
            "higgs_decay_covariance_candidate": {
                "present": external_higgs_cov["import_result"][
                    "external_correlated_covariance_submatrix_imported"
                ],
                "accepted_as_full_true_equivalence_profile": external_higgs_cov[
                    "import_result"
                ]["accepted_as_full_true_equivalence_profile"],
                "source": external_higgs_cov["external_source"],
                "row_count": external_higgs_cov["restricted_decay_sector"]["row_count"],
            },
            "published_profile_replay": {
                "present": higgs_imported["closure_decision"]["imported_profile_replay_closed"],
                "accepted_as_official_LHCHXSWG_likelihood": higgs_imported[
                    "closure_decision"
                ]["accepted_as_official_LHCHXSWG_likelihood"],
            },
        },
        "full_profile_likelihood_status": {
            "published_or_reconstructed_profile_imported": profile_status[
                "published_or_reconstructed_profile_imported"
            ],
            "official_machine_readable_likelihood_imported": official_higgs_gate[
                "official_machine_readable_likelihood_imported"
            ],
            "profile_likelihood_scan_imported": official_higgs_gate[
                "profile_likelihood_scan_imported"
            ],
            "nuisance_profile_semantics_imported": official_higgs_gate[
                "nuisance_profile_semantics_imported"
            ],
        },
        "required_import_payload": profile_status["required_import_payload"],
        "official_likelihood_required_payload": official_higgs_audit[
            "required_for_official_likelihood_promotion"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXTERNAL_MANIFEST, external_manifest)

    internal_workorder = {
        "schema": "MTTInternalThresholdResponseDerivationWorkorder.v1",
        "status": "INTERNAL_THRESHOLD_RESPONSE_WORKORDER_BUILT_VALUES_OPEN",
        "accepted_firstpass_value_packet": {
            "source": rel(VALUE_PACKET),
            "reference_scale": value_packet["reference_scale"],
            "reference_scheme": value_packet["reference_scheme"],
            "accepted_as_versioned_common_scale_candidate_values": value_packet[
                "accepted_as_versioned_common_scale_candidate_values"
            ],
            "accepted_for_true_precision_equivalence": value_packet[
                "accepted_for_true_precision_equivalence"
            ],
        },
        "finite_residual_support": {
            "source": rel(THRESHOLD_RESIDUALS),
            "row_count": threshold_residuals["summary"]["row_count"],
            "all_residuals_finite": threshold_residuals["summary"]["all_residuals_finite"],
            "accepted_as_threshold_matching_values": threshold_residuals[
                "accepted_as_threshold_matching_values"
            ],
            "accepted_as_mass_scheme_conversion_values": threshold_residuals[
                "accepted_as_mass_scheme_conversion_values"
            ],
        },
        "acceptance_contract": {
            "source": rel(THRESHOLD_CONTRACT),
            "values_promotable_now": threshold_contract["values_promotable_now"],
            "threshold_matching_required": threshold_contract["threshold_matching_required"],
            "mass_scheme_conversion_required": threshold_contract[
                "mass_scheme_conversion_required"
            ],
            "covariance_policy": threshold_contract["covariance_policy"],
        },
        "minimal_internal_derivation_outputs_required": [
            "selected response functional mapping MTT dynamic packet to threshold rows",
            "explicit scale/scheme/loop-order convention",
            "mass-scheme conversion maps for top, bottom, charm, tau, W/Z/H/lambda",
            "threshold covariance response or accepted diagonal limitation theorem",
            "proof no observed values select the response",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INTERNAL_WORKORDER, internal_workorder)

    decision = {
        "schema": "MTTVSD02ThresholdResponseDecision.v1",
        "status": "VSD02_CLASSIFIED_NO_ACCEPTED_THRESHOLD_RESPONSE_YET",
        "frontier_status": frontier["status"],
        "source_row_audit_status": source_row_audit["status"],
        "source_row_audit_packet_status": source_row_audit_packet.get("status"),
        "frontier_cutset_status": frontier_cutset["status"],
        "accepted_threshold_response_rule_closed": False,
        "accepted_external_likelihood_import_closed": False,
        "internal_derivation_closed": False,
        "what_is_newly_closed": {
            "row_route_classification": True,
            "external_import_manifest": True,
            "internal_derivation_workorder": True,
            "partial_higgs_covariance_separated_from_full_likelihood": True,
            "old_VSD01_reentry_prevented": True,
        },
        "remaining_atomic_requirements": [
            "accepted threshold matching source rows",
            "accepted mass-scheme conversion source rows",
            "full profile/covariance likelihood import or reconstruction",
            "multi-loop threshold convention values",
            "no-knob derivation of Yukawa/Higgs value rows",
        ],
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterVSD02Classification.v1",
        "status": "VSD02_ACCEPTED_SOURCE_ROWS_OR_INTERNAL_DERIVATION_REQUIRED",
        "closed_now": decision["what_is_newly_closed"],
        "still_open": decision["remaining_atomic_requirements"],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The VSD02 rows are now classified. The next progress must fill accepted source rows "
                "for threshold/mass-scheme/profile data, or derive those rows internally from the selected "
                "MTT branch. Partial Higgs covariance is useful but not a full likelihood."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedVSD02ThresholdResponseRuleOrExternalLikelihoodImport",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "vsd02_row_route_classification": rel(CLASSIFICATION),
            "external_likelihood_import_manifest": rel(EXTERNAL_MANIFEST),
            "internal_threshold_response_derivation_workorder": rel(INTERNAL_WORKORDER),
            "vsd02_threshold_response_decision": rel(DECISION),
            "next_cutset_after_vsd02_classification": rel(CUTSET),
        },
        "theorem": {
            "name": "VSD02RouteClassificationAndImportSeparationTheorem",
            "proved": True,
            "statement": (
                "Given the VSD01 frontier update, threshold residual audit, source-row audit, external "
                "profile import status, and Higgs covariance import lanes, every remaining VSD02 value row "
                "can be classified without returning to the retired VSD01 blocker. Finite residual and "
                "first-pass value support exist, and a partial Higgs covariance candidate is imported, but "
                "no accepted threshold/mass-scheme source rows, full profile likelihood, or no-knob value "
                "derivation is closed yet."
            ),
        },
        "what_closes_now": decision["what_is_newly_closed"],
        "what_remains_open": decision["remaining_atomic_requirements"],
        "closure_decision": {
            "VSD02_route_classification_closed": True,
            "accepted_threshold_response_rule_closed": False,
            "accepted_external_likelihood_import_closed": False,
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
        "certificate": "MTT_Selected_VSD02ThresholdResponseRule_or_ExternalLikelihoodImport_v1",
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

    note = f"""# MTT Selected VSD02ThresholdResponseRule or ExternalLikelihoodImport v1

Status: `{STATUS}`.

This artifact classifies the live VSD02 rows after VSD-01 source/dynamic
closure.  It does not return to the old VSD-01 track.

Closed now:

```text
row route classification                 : true
external likelihood/import manifest       : true
internal threshold-response workorder     : true
partial Higgs covariance separated cleanly : true
```

Not closed:

```text
accepted threshold matching source rows
accepted mass-scheme conversion source rows
full profile/covariance likelihood import
multi-loop threshold convention values
no-knob Yukawa/Higgs value derivation
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
