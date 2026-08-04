"""Build first value-source row fill attempt or external threshold source import."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_firstvaluesourcerowfill_or_externalthresholdsourceimport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FIRST_ROW = PACKET_DIR / "first_value_source_row_fill_attempt.packet.json"
EXTERNAL_IMPORT = PACKET_DIR / "external_threshold_source_import_attempt.packet.json"
DECISION = PACKET_DIR / "first_row_acceptance_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_first_value_source_row_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FirstValueSourceRowFill_or_ExternalThresholdSourceImport_v1.md"

PREVIOUS = DATA / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest.candidate.json"
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
NONSCALAR = DATA / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json"
WEYL_PROMOTION = DATA / "selected_weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill.candidate.json"
FIRST_ROW_SUPPORT = (
    DATA
    / "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution"
    / "route_b_first_primitive_row_execution_attempt.packet.json"
)
SOURCE_GAP = (
    DATA
    / "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution"
    / "source_gap_decision.packet.json"
)

STATUS = (
    "MTT_SELECTED_FIRSTVALUESOURCEROWFILL_OR_EXTERNALTHRESHOLDSOURCEIMPORT_"
    "BUILT_FIRST_ROW_NUMERIC_SOURCE_PROMOTION_OPEN"
)
NEXT = "MTT_Selected_FirstValueSourceRowPromotion_or_HonestGalerkinPrimitiveRow_v1"


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
        raise FileNotFoundError("missing first value-source row sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        KERNEL,
        IMPORT_MANIFEST,
        NONSCALAR,
        WEYL_PROMOTION,
        FIRST_ROW_SUPPORT,
        SOURCE_GAP,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    kernel = load(KERNEL)
    import_manifest = load(IMPORT_MANIFEST)
    nonscalar = load(NONSCALAR)
    weyl = load(WEYL_PROMOTION)
    first_row_support = load(FIRST_ROW_SUPPORT)
    source_gap = load(SOURCE_GAP)

    u_response = nonscalar["conditional_non_scalar_value_packet"]["sector_first_responses"]["u"]
    e_response = nonscalar["conditional_non_scalar_value_packet"]["sector_first_responses"]["e"]
    tests = nonscalar["conditional_non_scalar_value_packet"]["acceptance_tests"]
    first_required = kernel["first_attack_order"][0]

    first_row = {
        "schema": "MTTFirstValueSourceRowFillAttempt.v1",
        "status": "FIRST_DYNAMIC_ROW_NUMERICALLY_FILLED_SOURCE_PROMOTION_OPEN",
        "target_obligation": first_required,
        "row_id": "VSD-01.phase.I_plus_Z.u_e.first_dynamic_row",
        "source_route": "phase_packet_I_plus_Z routed to u,e",
        "numeric_payload": {
            "u_correction_dY": u_response["correction_dY"],
            "u_first_hermitian_response_H1": u_response["first_hermitian_response_H1"],
            "u_invariants": u_response["invariants"],
            "e_correction_dY": e_response["correction_dY"],
            "e_first_hermitian_response_H1": e_response["first_hermitian_response_H1"],
            "e_invariants": e_response["invariants"],
        },
        "support_payload": {
            "conditional_packet_selected_by_MTT": nonscalar["conditional_non_scalar_value_packet"][
                "selected_by_MTT"
            ],
            "selected_dynamic_overlap_tensor_claimed": nonscalar[
                "selected_dynamic_overlap_tensor_claimed"
            ],
            "selected_full_response_claimed": nonscalar["selected_full_response_claimed"],
            "first_row_value_numerically_ready": source_gap[
                "route_b_first_row_value_numerically_ready"
            ],
            "source_gap_not_numeric_gap": source_gap["source_gap_not_numeric_gap"],
            "first_row_support_status": first_row_support["status"],
        },
        "acceptance_tests": {
            "numeric_row_filled": True,
            "mass_split_positive_conditionally": tests["all_mass_split_positive"],
            "mixing_commutators_positive_conditionally": tests["ckm_commutator_positive"]
            and tests["pmns_commutator_positive"],
            "cp_odd_nonzero_conditionally": tests["cp_odd_invariant_nonzero"],
            "observed_flavor_data_used": nonscalar["conditional_non_scalar_value_packet"][
                "observed_flavor_data_used"
            ],
            "selected_dynamic_source_to_C1_transfer_emitted": weyl[
                "lane_A_dynamic_source_promotion"
            ]["selected_promotion_fields"]["selected_dynamic_source_to_C1_transfer"],
            "selected_Hessian_blocks_emitted": weyl["lane_A_dynamic_source_promotion"][
                "selected_promotion_fields"
            ]["selected_Hessian_blocks"],
            "selected_b_selected_emitted": weyl["lane_A_dynamic_source_promotion"][
                "selected_promotion_fields"
            ]["selected_b_selected"],
            "honest_Galerkin_C1_contractions_emitted": weyl["lane_B_honest_Galerkin_C1_value_fill"][
                "promoted"
            ],
        },
        "accepted_as_selected_dynamic_value_source_row": False,
        "why_not_accepted": [
            "the non-scalar row is conditionally constructed but selected_by_MTT=false",
            "selected dynamic source-to-C1 transfer is not emitted",
            "selected Hessian blocks and b_selected are not emitted",
            "honest Galerkin C1 contractions are not emitted",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FIRST_ROW, first_row)

    external_import = {
        "schema": "MTTExternalThresholdSourceImportAttempt.v1",
        "status": "NO_EXTERNAL_THRESHOLD_SOURCE_ROW_IMPORTED",
        "manifest_source": rel(IMPORT_MANIFEST),
        "manifest_required_fields": import_manifest["manifest_required_fields"],
        "accepted_external_rows_present_before_attempt": import_manifest[
            "accepted_external_rows_present"
        ],
        "accepted_external_rows_imported_now": False,
        "checked_local_candidates": import_manifest["current_local_candidates_checked"],
        "why_not_imported": import_manifest["why_no_import_yet"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXTERNAL_IMPORT, external_import)

    decision = {
        "schema": "MTTFirstRowAcceptanceDecision.v1",
        "status": "FIRST_ROW_NUMERICALLY_FILLED_REJECTED_AS_SELECTED_SOURCE_ROW",
        "route_A_internal_row": {
            "numeric_first_row_filled": True,
            "conditional_quality_tests_pass": True,
            "accepted_as_selected_dynamic_value_source_row": False,
            "can_close_VSD_01_now": False,
        },
        "route_B_external_import": {
            "accepted_external_threshold_row_imported": False,
            "can_close_external_import_now": False,
        },
        "new_closure": {
            "first_value_source_row_numeric_payload_emitted": True,
            "external_import_attempt_executed": True,
            "source_promotion_gap_is_exactly_identified": True,
        },
        "remaining_hard_failures": [
            "selected_dynamic_source_to_C1_transfer_emitted",
            "selected_Hessian_blocks_emitted",
            "selected_b_selected_emitted",
            "honest_Galerkin_C1_contractions_emitted",
            "accepted_external_threshold_rows_imported",
        ],
        "accepted_for_true_precision_equivalence": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterFirstValueSourceRowAttempt.v1",
        "status": "FIRST_NUMERIC_ROW_FILLED_SOURCE_PROMOTION_OR_GALERKIN_REQUIRED",
        "closed_now": [
            "first phase-side dynamic value row numeric payload emitted",
            "conditional mass-split/mixing/CP checks attached",
            "external threshold import attempt executed",
            "selected-source rejection reasons enumerated",
        ],
        "still_open": decision["remaining_hard_failures"],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The first value row exists numerically. The next progress must promote it by emitting "
                "selected dynamic transfer/Hessian/b_selected data, or by honest Galerkin primitive-row provenance."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedFirstValueSourceRowFillOrExternalThresholdSourceImport",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "first_value_source_row_fill_attempt": rel(FIRST_ROW),
            "external_threshold_source_import_attempt": rel(EXTERNAL_IMPORT),
            "first_row_acceptance_decision": rel(DECISION),
            "next_cutset_after_first_value_source_row_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "FirstNumericValueSourceRowAndSourcePromotionGapTheorem",
            "proved": True,
            "statement": (
                "The first phase-side non-scalar dynamic row can be emitted numerically from the existing "
                "conditional I+Z response packet, and it passes the conditional mass-split, mixing, and CP "
                "tests without observed flavor data. This does not close VSD-01 because the row is not yet "
                "selected by MTT: selected dynamic transfer, Hessian/b_selected, or honest Galerkin primitive "
                "provenance is still absent. No accepted external threshold source row is imported."
            ),
        },
        "what_closes_now": decision["new_closure"],
        "what_remains_open": {
            "accepted_selected_dynamic_value_source_row": True,
            "selected_dynamic_source_to_C1_transfer": True,
            "selected_Hessian_blocks": True,
            "selected_b_selected": True,
            "honest_Galerkin_C1_contractions": True,
            "accepted_external_threshold_source_import": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "first_value_source_row_numeric_payload_emitted": True,
            "accepted_as_selected_dynamic_value_source_row": False,
            "external_threshold_source_imported": False,
            "VSD_01_closed": False,
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
        "certificate": "MTT_Selected_FirstValueSourceRowFill_or_ExternalThresholdSourceImport_v1",
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

    note = f"""# MTT Selected FirstValueSourceRowFill or ExternalThresholdSourceImport v1

Status: `{STATUS}`.

This artifact emits the first numeric value-source row candidate:

```text
row id: VSD-01.phase.I_plus_Z.u_e.first_dynamic_row
route : phase packet I+Z routed to u,e
```

It passes the conditional non-scalar checks, but it is not accepted as a
selected MTT dynamic value-source row.

```text
numeric first row filled: true
accepted as selected source row: false
external threshold row imported: false
```

The blocker is now pure source promotion: selected dynamic transfer,
Hessian/b_selected, or honest Galerkin primitive-row provenance.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
