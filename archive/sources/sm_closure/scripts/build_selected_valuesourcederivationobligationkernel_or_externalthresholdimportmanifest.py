"""Build value-source derivation obligation kernel or external threshold import manifest."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
KERNEL = PACKET_DIR / "value_source_derivation_obligation_kernel.packet.json"
IMPORT_MANIFEST = PACKET_DIR / "external_threshold_import_manifest.packet.json"
SUPPORT_MATRIX = PACKET_DIR / "support_to_obligation_mapping.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_obligation_kernel.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_obligation_kernel.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ValueSourceDerivationObligationKernel_or_ExternalThresholdImportManifest_v1.md"

PREVIOUS = DATA / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation.candidate.json"
PREVIOUS_DERIVATION = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "no_knob_value_derivation_attempt.packet.json"
)
STATIC_OVERLAP = DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
STATIC_READOUT = (
    DATA
    / "selected_matterslot_readout_backimport_from_smslotfunctor"
    / "selected_static_matterslot_readout.packet.json"
)
ROUTEC_FRONTIER = DATA / "selected_routec_selected_operator_source_and_overlap_tensor_packet.candidate.json"
SOURCE_MAP_OBLIGATION = (
    DATA
    / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
    / "source_map_selection_obligation_kernel.packet.json"
)
RESIDUALS = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
)

STATUS = (
    "MTT_SELECTED_VALUESOURCEDERIVATIONOBLIGATIONKERNEL_OR_EXTERNALTHRESHOLDIMPORTMANIFEST_"
    "BUILT_KERNEL_AND_IMPORT_MANIFEST_VALUES_OPEN"
)
NEXT = "MTT_Selected_FirstValueSourceRowFill_or_ExternalThresholdSourceImport_v1"


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
        raise FileNotFoundError("missing value-source obligation sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_DERIVATION,
        STATIC_OVERLAP,
        STATIC_READOUT,
        ROUTEC_FRONTIER,
        SOURCE_MAP_OBLIGATION,
        RESIDUALS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_derivation = load(PREVIOUS_DERIVATION)
    static_overlap = load(STATIC_OVERLAP)
    static_readout = load(STATIC_READOUT)
    routec = load(ROUTEC_FRONTIER)
    source_obligation = load(SOURCE_MAP_OBLIGATION)
    residuals = load(RESIDUALS)

    required_rows = [
        {
            "id": "VSD-01-selected-overlap-value-kernel",
            "obligation": "selected_overlap_or_operator_kernel",
            "required_payload": [
                "selected dynamic overlap/threshold tensor T_selected",
                "sector rows for u,c,t,d,s,b,e,mu,tau and lambda_H",
                "same-branch proof linking tensor rows to the versioned value packet",
                "no observed masses/mixings/benchmark values as selectors",
            ],
            "local_support": {
                "static_overlap_kernel_selected": static_overlap["selected_overlap_kernel"]["selected"],
                "static_readout_closed": static_readout["status"] == "STATIC_SOURCE_TIER_READOUT_CLOSED",
                "routec_selected_overlap_tensor_closed": routec["best_current_statement"][
                    "selected_overlap_tensor_closed"
                ],
            },
            "closed": False,
            "why_open": "Static overlap/transfer normalization is selected, but the dynamic value-source tensor for Yukawa/Higgs/threshold rows is not emitted.",
        },
        {
            "id": "VSD-02-threshold-response-rule",
            "obligation": "threshold_response_rule",
            "required_payload": [
                "selected response functional mapping internal determinant/threshold candidates to physical threshold rows",
                "scale/scheme declaration",
                "multi-loop or explicitly accepted lower-order convention",
                "proof that observed gauge/Yukawa values do not select the response",
            ],
            "local_support": {
                "source_map_obligation_kernel_built": source_obligation["status"]
                == "SELECTION_OBLIGATION_KERNEL_BUILT_VALUES_OPEN",
                "closed_numeric_facts_present": source_obligation["closed_numeric_facts"][
                    "deltaTheta_equals_1_1"
                ],
                "selected_deltaTheta_C1_emitted": source_obligation["currently_emitted"][
                    "selected_deltaTheta_C1"
                ],
            },
            "closed": False,
            "why_open": "The conditional numeric facts are present, but selected A/b/deltaTheta source emissions remain false.",
        },
        {
            "id": "VSD-03-selected-sm-packet-attachment",
            "obligation": "selected_sm_packet_attachment",
            "required_payload": [
                "representation/operator packet row id",
                "anomaly/covariance certificate id",
                "attachment from value-source rows to selected SM source packet",
                "forbidden measured-slot backflow check",
            ],
            "local_support": {
                "routec_source_level_carrier_closed": routec["best_current_statement"][
                    "source_level_ZX_carrier_closed"
                ],
                "selected_A_selected_closed": routec["best_current_statement"][
                    "selected_A_selected_closed"
                ],
            },
            "closed": False,
            "why_open": "Source-level carrier support is closed, but the selected C1/operator attachment remains open.",
        },
        {
            "id": "VSD-04-local-qft-renormalization-functor",
            "obligation": "local_qft_renormalization_functor",
            "required_payload": [
                "observable functor name and domain/codomain",
                "renormalized parameter slots for thresholds and mass schemes",
                "Ward/anomaly/locality checks",
                "declaration that observable rows are downstream and cannot select MTT source",
            ],
            "local_support": {
                "static_source_tier_readout_closed": static_readout["status"] == "STATIC_SOURCE_TIER_READOUT_CLOSED",
                "downstream_operator_boundary_explicit": "Yukawa magnitudes, CKM/PMNS, masses, or full SM no-knob closure"
                in static_overlap["same_source_consistency"]["downstream_not_included"],
            },
            "closed": False,
            "why_open": "The source/downstream boundary is explicit, but no local-QFT renormalization functor row is emitted here.",
        },
        {
            "id": "VSD-05-external-threshold-import",
            "obligation": "accepted_external_source_escape_hatch",
            "required_payload": [
                "external source label/version",
                "threshold and mass-scheme rows with scale, scheme, loop order, and covariance",
                "basis map to MTT value/profile rows",
                "provenance and checksum",
                "guardrail excluding source selection by observed targets",
            ],
            "local_support": {
                "residual_table_available": residuals["summary"]["all_residuals_finite"],
                "residual_rows_are_accepted_source_rows": residuals[
                    "accepted_as_threshold_matching_values"
                ]
                or residuals["accepted_as_mass_scheme_conversion_values"],
            },
            "closed": False,
            "why_open": "Residual rows are finite but no external accepted source-row file is imported.",
        },
    ]
    closed_rows = [row for row in required_rows if row["closed"]]
    kernel = {
        "schema": "MTTValueSourceDerivationObligationKernel.v1",
        "status": "OBLIGATION_KERNEL_TYPED_REQUIRED_ROWS_OPEN",
        "previous_obligation_count": previous_derivation["obligation_count"],
        "required_rows": required_rows,
        "required_row_count": len(required_rows),
        "closed_row_count": len(closed_rows),
        "first_attack_order": [
            "VSD-01-selected-overlap-value-kernel",
            "VSD-02-threshold-response-rule",
            "VSD-05-external-threshold-import",
            "VSD-04-local-qft-renormalization-functor",
            "VSD-03-selected-sm-packet-attachment",
        ],
        "acceptance_rule": (
            "At least one internal value-source derivation route must emit selected dynamic rows for the "
            "Yukawa/Higgs/threshold packet, or the external import route must supply accepted source rows "
            "with provenance, basis map, and no-selector guardrails."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(KERNEL, kernel)

    import_manifest = {
        "schema": "MTTExternalThresholdImportManifest.v1",
        "status": "IMPORT_MANIFEST_BUILT_NO_ACCEPTED_EXTERNAL_ROWS_PRESENT",
        "accepted_external_rows_present": False,
        "manifest_required_fields": {
            "source": ["label", "version_or_date", "url_or_local_path", "checksum_sha256"],
            "basis": ["input_basis", "output_basis", "redundant_rows_removed", "scheme_scale_map"],
            "threshold_rows": [
                "top_matching",
                "bottom_matching",
                "charm_matching",
                "tau_matching",
                "W_Z_H_electroweak_matching",
                "lambda_H_matching",
            ],
            "mass_scheme_rows": [
                "direct_top_to_running_top",
                "MSbar_quark_scale_transport",
                "pole_or_rest_lepton_to_running_lepton",
                "Higgs_pole_to_running_lambda",
            ],
            "profile_rows": ["covariance_or_likelihood", "loop_order", "uncertainty_model"],
            "guardrails": ["not_used_as_source_selector", "target_fitting_excluded"],
        },
        "current_local_candidates_checked": [
            rel(RESIDUALS),
            rel(STATIC_OVERLAP),
            rel(SOURCE_MAP_OBLIGATION),
        ],
        "why_no_import_yet": [
            "local residual rows do not carry accepted threshold/mass-scheme provenance",
            "static overlap rows do not carry dynamic numerical threshold values",
            "conditional C1 source-map rows are not selected emissions",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(IMPORT_MANIFEST, import_manifest)

    support_matrix = {
        "schema": "MTTSupportToObligationMapping.v1",
        "status": "SUPPORT_MAPPED_NO_OBLIGATION_FULLY_CLOSED",
        "support_rows": [
            {
                "support_id": "static_smslot_overlap_normalization",
                "path": rel(STATIC_OVERLAP),
                "supports_obligations": ["VSD-01-selected-overlap-value-kernel", "VSD-04-local-qft-renormalization-functor"],
                "closes_obligations": [],
            },
            {
                "support_id": "static_matter_slot_readout",
                "path": rel(STATIC_READOUT),
                "supports_obligations": ["VSD-01-selected-overlap-value-kernel", "VSD-03-selected-sm-packet-attachment"],
                "closes_obligations": [],
            },
            {
                "support_id": "routec_conditional_source_map",
                "path": rel(SOURCE_MAP_OBLIGATION),
                "supports_obligations": ["VSD-02-threshold-response-rule"],
                "closes_obligations": [],
            },
            {
                "support_id": "finite_residual_value_table",
                "path": rel(RESIDUALS),
                "supports_obligations": ["VSD-05-external-threshold-import"],
                "closes_obligations": [],
            },
        ],
        "all_support_rows_have_paths": True,
        "any_obligation_closed_by_support": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(SUPPORT_MATRIX, support_matrix)

    promotion = {
        "schema": "MTTPromotionDecisionAfterObligationKernel.v1",
        "status": "KERNEL_AND_IMPORT_MANIFEST_CLOSED_VALUESOURCE_ROWS_OPEN",
        "promotion_tests": {
            "obligation_kernel_built": True,
            "external_import_manifest_built": True,
            "support_to_obligation_mapping_built": True,
            "selected_dynamic_value_source_rows_emitted": False,
            "accepted_external_threshold_rows_imported": False,
            "no_knob_value_derivation_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "promotion_decision": {
            "obligation_kernel_closed": True,
            "import_manifest_closed": True,
            "accepted_for_true_precision_equivalence": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "remaining_hard_failures": [
            "selected_dynamic_value_source_rows_emitted",
            "accepted_external_threshold_rows_imported",
            "no_knob_value_derivation_closed",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROMOTION, promotion)

    cutset = {
        "schema": "MTTNextCutsetAfterObligationKernel.v1",
        "status": "FIRST_VALUE_SOURCE_ROW_OR_EXTERNAL_IMPORT_REQUIRED",
        "closed_now": [
            "typed value-source derivation obligation kernel built",
            "external threshold import manifest built",
            "support-to-obligation mapping built",
            "first attack order fixed",
        ],
        "still_open": [
            "selected dynamic overlap/threshold value-source row",
            "selected threshold response rule",
            "accepted external threshold/mass-scheme source import",
            "local-QFT renormalization functor row",
            "selected SM packet attachment for value-source rows",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The schemas and acceptance tests are now fixed. The next step must fill one first value-source "
                "row or import one accepted external threshold source row that satisfies the manifest."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedValueSourceDerivationObligationKernelOrExternalThresholdImportManifest",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "value_source_derivation_obligation_kernel": rel(KERNEL),
            "external_threshold_import_manifest": rel(IMPORT_MANIFEST),
            "support_to_obligation_mapping": rel(SUPPORT_MATRIX),
            "promotion_decision_after_obligation_kernel": rel(PROMOTION),
            "next_cutset_after_obligation_kernel": rel(CUTSET),
        },
        "theorem": {
            "name": "ValueSourceObligationKernelAndImportManifestTheorem",
            "proved": True,
            "statement": (
                "The open value-source problem can be reduced to five typed source-row obligations and an "
                "external threshold import manifest. Existing static overlap, readout, conditional C1, and "
                "residual-value support maps into these obligations but closes none of them. Thus the next "
                "valid progress must fill a selected dynamic value-source row or import accepted external "
                "threshold/mass-scheme rows with provenance."
            ),
        },
        "what_closes_now": {
            "typed_value_source_obligation_kernel": True,
            "external_threshold_import_manifest": True,
            "support_to_obligation_mapping": True,
            "first_attack_order_fixed": True,
        },
        "what_remains_open": {
            "selected_dynamic_value_source_rows": True,
            "accepted_external_threshold_rows": True,
            "no_knob_value_derivation": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "obligation_kernel_closed": True,
            "import_manifest_closed": True,
            "selected_dynamic_value_source_rows_emitted": False,
            "accepted_external_threshold_rows_imported": False,
            "accepted_for_true_precision_equivalence": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_ValueSourceDerivationObligationKernel_or_ExternalThresholdImportManifest_v1",
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

    note = f"""# MTT Selected ValueSourceDerivationObligationKernel or ExternalThresholdImportManifest v1

Status: `{STATUS}`.

This artifact fixes the remaining source-row problem into a typed obligation
kernel and an external import manifest.

```text
required rows = {kernel["required_row_count"]}
closed rows   = {kernel["closed_row_count"]}
first target  = {kernel["first_attack_order"][0]}
```

It also records that existing static overlap/readout/C1/residual support maps
into the obligations but closes none of them.

Promotion decision:

```text
obligation kernel closed: true
external import manifest closed: true
selected dynamic value-source rows emitted: false
accepted external threshold rows imported: false
true SM equivalence: open
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
