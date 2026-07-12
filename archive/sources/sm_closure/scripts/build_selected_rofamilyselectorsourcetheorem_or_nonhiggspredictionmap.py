"""Build the RO family-selector source theorem and refreshed full payload.

The previous artifact filled all RO.* slots, but only the provenance certificate
was source-closed.  This artifact tries the next theorem:

* promote RO.family_selector at the retarded-overlap family-class level, using
  the selected charged retarded-overlap spectral-pairing lemma and same-source
  dynamic matter overlap packet;
* refresh the full RO payload after that theorem;
* reattempt the non-Higgs prediction map with the family selector now closed.

Current result: the family selector is source-selected as a family class, but
the HRG numeric specialization/value source, strict H map, non-Higgs HRG map,
and non-Higgs prediction remain open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FAMILY_THEOREM = PACKET_DIR / "ro_family_selector_source_theorem.packet.json"
FULL_PAYLOAD = PACKET_DIR / "ro_full_payload_after_family_selector.packet.json"
NONHIGGS_ATTEMPT = PACKET_DIR / "ro_nonhiggs_prediction_map_attempt_after_selector.packet.json"
UNIVERSAL_GATE = PACKET_DIR / "ro_universal_admission_gate_after_selector.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_ro_family_selector_theorem.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ROFamilySelectorSourceTheorem_or_NonHiggsPredictionMap_v1.md"

PREVIOUS = DATA / "selected_retardedoverlapfamilyselector_or_hrgsourcepayloadfill.candidate.json"
PREVIOUS_SELECTOR = (
    DATA
    / "selected_retardedoverlapfamilyselector_or_hrgsourcepayloadfill"
    / "ro_family_selector.packet.json"
)
PREVIOUS_VALUE = (
    DATA
    / "selected_retardedoverlapfamilyselector_or_hrgsourcepayloadfill"
    / "ro_value_source.packet.json"
)
PREVIOUS_H_MAP = (
    DATA
    / "selected_retardedoverlapfamilyselector_or_hrgsourcepayloadfill"
    / "ro_h_sector_map.packet.json"
)
PREVIOUS_NONHIGGS = (
    DATA
    / "selected_retardedoverlapfamilyselector_or_hrgsourcepayloadfill"
    / "ro_nonhiggs_sector_map.packet.json"
)
PREVIOUS_EVALUATOR = (
    DATA
    / "selected_retardedoverlapfamilyselector_or_hrgsourcepayloadfill"
    / "ro_nonhiggs_prediction_evaluator.packet.json"
)
PREVIOUS_PROVENANCE = (
    DATA
    / "selected_retardedoverlapfamilyselector_or_hrgsourcepayloadfill"
    / "ro_provenance_certificate.packet.json"
)
PAIRING_CANDIDATE = DATA / "selected_retardedoverlapspectralpairinglemma_or_independentquadraturevalues.candidate.json"
PAIRING_LEMMA = (
    DATA
    / "selected_retardedoverlapspectralpairinglemma_or_independentquadraturevalues"
    / "selected_retarded_overlap_spectral_pairing_lemma.packet.json"
)
READINESS = (
    DATA
    / "selected_physicaldotdalpha1sectortransferretardedoverlapkernel_or_empiricalkparityimport"
    / "retarded_overlap_kernel_readiness_after_stationary_transfer.packet.json"
)
SAME_SOURCE_OVERLAP = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_packet.packet.json"
)
CROSSUSE = (
    DATA
    / "universal_crossuse_parameter_admissibility_theorem"
    / "crossuse_admissibility_theorem.packet.json"
)

STATUS = (
    "MTT_SELECTED_ROFAMILYSELECTORSOURCETHEOREM_OR_NONHIGGSPREDICTIONMAP_"
    "FAMILY_SELECTOR_CLOSED_VALUE_MAP_OPEN"
)
NEXT = "MTT_Selected_ROValueSource_or_NonHiggsMapExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing RO selector theorem inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_SELECTOR,
        PREVIOUS_VALUE,
        PREVIOUS_H_MAP,
        PREVIOUS_NONHIGGS,
        PREVIOUS_EVALUATOR,
        PREVIOUS_PROVENANCE,
        PAIRING_CANDIDATE,
        PAIRING_LEMMA,
        READINESS,
        SAME_SOURCE_OVERLAP,
        CROSSUSE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    selector_prev = load(PREVIOUS_SELECTOR)
    value_prev = load(PREVIOUS_VALUE)
    h_map_prev = load(PREVIOUS_H_MAP)
    nonhiggs_prev = load(PREVIOUS_NONHIGGS)
    evaluator_prev = load(PREVIOUS_EVALUATOR)
    provenance_prev = load(PREVIOUS_PROVENANCE)
    pairing_candidate = load(PAIRING_CANDIDATE)
    pairing_lemma = load(PAIRING_LEMMA)
    readiness = load(READINESS)
    same_source = load(SAME_SOURCE_OVERLAP)
    crossuse = load(CROSSUSE)

    hrg_value = previous["key_numbers"]["UP_RET_OVERLAP_HRG"]

    family_theorem = {
        "schema": "MTTROFamilySelectorSourceTheorem.v1",
        "id": "RO.family_selector",
        "status": "RO_FAMILY_SELECTOR_SOURCE_SELECTED_AS_FAMILY_CLASS",
        "closure_claimed": True,
        "theorem": {
            "name": "ROFamilySelectorSourceTheorem",
            "proved": True,
            "statement": (
                "The selected same-source dynamic matter overlap packet and the "
                "charged retarded-overlap spectral-pairing lemma emit a selected "
                "row-local retarded-overlap family on the charged u,d,e sectors. "
                "Therefore RO.family_selector is source-selected at the family-class "
                "level. This does not select the HRG numeric specialization, does "
                "not derive R_H^RG, and does not admit UP-RET-OVERLAP.HRG as a "
                "universal primitive."
            ),
        },
        "source_selected": True,
        "selected_scope": {
            "primitive_class": "UP-RET-OVERLAP",
            "family_class_selected": True,
            "charged_sectors_selected": pairing_lemma["scope"]["charged_sectors_closed"],
            "H_sector_specialization_selected": False,
            "HRG_numeric_value_source_selected": False,
            "nonHiggs_prediction_map_selected": False,
        },
        "source_support": {
            "same_source_dynamic_matter_overlap_status": same_source["status"],
            "same_source_dynamic_packet_validates": pairing_lemma["proof_clauses"][
                "same_source_dynamic_packet_validates"
            ],
            "selected_retarded_overlap_pairing_status": pairing_lemma["status"],
            "retarded_overlap_pairing_proved": pairing_candidate["closure_decision"][
                "retarded_overlap_spectral_pairing_lemma_proved"
            ],
            "charged_strict_Lrowlocal_row_count": pairing_candidate["closure_decision"][
                "charged_strict_Lrowlocal_row_count"
            ],
            "retarded_kernel_readiness_status": readiness["status"],
        },
        "nonpromotion_boundaries": [
            "Family-class selection is not HRG value selection.",
            "Charged retarded-overlap rows do not select the H/lambda threshold multiplier.",
            "No non-Higgs map currently consumes UP-RET-OVERLAP.HRG.",
            "Calibrating HRG on lambda_H still forbids lambda_H prediction credit.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    value_after = {
        **value_prev,
        "status": "RO_VALUE_SOURCE_EMPIRICAL_VALUE_FILLED_FAMILY_SELECTED_SOURCE_VALUE_OPEN",
        "family_selector_source_selected": True,
        "source_selected": False,
        "source_value_emitted": False,
        "HRG_numeric_specialization_source_selected": False,
        "blocking_reasons": [
            "RO.family_selector is now source-selected only at family-class level.",
            "The HRG value remains calibrated on lambda_H(M_t), not source-derived.",
            "No determinant/index/RG source rule derives the numeric HRG value.",
            "No non-Higgs prediction has validated the same value without retuning.",
        ],
    }

    h_map_after = {
        **h_map_prev,
        "status": "RO_H_SECTOR_MAP_EMPIRICAL_FILLED_FAMILY_SELECTED_STRICT_SOURCE_OPEN",
        "family_selector_source_selected": True,
        "source_selected": False,
        "strict_H_sector_map_emitted": False,
        "HRG_numeric_specialization_source_selected": False,
    }

    nonhiggs_rows_after = []
    for row in nonhiggs_prev["map_rows"]:
        row_after = dict(row)
        if row_after["domain"] in {
            "alpha/source-strength",
            "dynamic C1 overlap/value tensor",
            "generic non-Higgs threshold/RG observable",
        }:
            row_after["family_selector_available_now"] = True
            row_after["blocking_reason_after_selector"] = (
                row_after["blocking_reason"]
                + " The RO family class is now selected, but this row still lacks a typed "
                "sector insertion map using the HRG numeric specialization."
            )
        else:
            row_after["family_selector_available_now"] = True
            row_after["blocking_reason_after_selector"] = row_after["blocking_reason"]
        row_after["accepted_as_crossuse_map"] = False
        row_after["prediction_emitted_without_retuning"] = False
        row_after["same_HRG_primitive_map_available"] = False
        nonhiggs_rows_after.append(row_after)

    nonhiggs_attempt = {
        "schema": "MTTRONonHiggsPredictionMapAttemptAfterSelector.v1",
        "id": "RO.nonHiggs_sector_map",
        "status": "RO_NONHIGGS_PREDICTION_MAP_REATTEMPTED_AFTER_SELECTOR_ZERO_ACCEPTED",
        "closure_claimed": True,
        "family_selector_source_selected": True,
        "source_selected": False,
        "tested_map_count": nonhiggs_prev["tested_map_count"],
        "accepted_crossuse_map_count": 0,
        "map_rows": nonhiggs_rows_after,
        "decision": {
            "accepted_RO_nonHiggs_sector_map": False,
            "nonHiggs_prediction_emitted": False,
            "crossuse_prediction_passed": False,
            "UP_RET_OVERLAP_HRG_universal_admitted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    evaluator_after = {
        **evaluator_prev,
        "status": "RO_NONHIGGS_PREDICTION_EVALUATOR_REPLAYED_AFTER_SELECTOR_ZERO_PREDICTIONS",
        "family_selector_source_selected": True,
        "source_selected": False,
        "execution_result": {
            **evaluator_prev["execution_result"],
            "accepted_nonHiggs_sector_map_count": 0,
            "prediction_count": 0,
            "crossuse_prediction_passed": False,
            "universal_primitive_admitted": False,
        },
    }

    provenance_after = {
        **provenance_prev,
        "status": "RO_PROVENANCE_CERTIFICATE_UPDATED_AFTER_FAMILY_SELECTOR_THEOREM",
        "source_selected": True,
        "certificate_closes": provenance_prev["certificate_closes"]
        + ["RO.family_selector source-selected at family-class level"],
        "provenance_ledger": {
            **provenance_prev["provenance_ledger"],
            "RO.family_selector": "source-selected as retarded-overlap family class; HRG specialization not selected",
            "RO.value_source": "empirical calibrated value filled; source value still not emitted",
            "RO.H_sector_map": "controlled empirical H map filled; strict H source map not emitted",
            "RO.nonHiggs_sector_map": "reattempted after family selector; zero accepted maps",
            "RO.nonHiggs_prediction_evaluator": "replayed after family selector; zero predictions",
        },
    }

    full_payload = {
        "schema": "MTTROFullPayloadAfterFamilySelectorTheorem.v1",
        "status": "RO_FULL_PAYLOAD_BUILT_FAMILY_SELECTOR_SOURCE_CLOSED_VALUE_MAP_OPEN",
        "closure_claimed": True,
        "payload_rows": [
            {
                "id": "RO.family_selector",
                "status": family_theorem["status"],
                "source_selected": True,
                "strict_source_payload": True,
            },
            {
                "id": "RO.value_source",
                "status": value_after["status"],
                "source_selected": False,
                "strict_source_payload": False,
            },
            {
                "id": "RO.H_sector_map",
                "status": h_map_after["status"],
                "source_selected": False,
                "strict_source_payload": False,
            },
            {
                "id": "RO.nonHiggs_sector_map",
                "status": nonhiggs_attempt["status"],
                "source_selected": False,
                "strict_source_payload": False,
            },
            {
                "id": "RO.nonHiggs_prediction_evaluator",
                "status": evaluator_after["status"],
                "source_selected": False,
                "strict_source_payload": False,
            },
            {
                "id": "RO.provenance_certificate",
                "status": provenance_after["status"],
                "source_selected": True,
                "strict_source_payload": True,
            },
        ],
        "source_selected_payload_count": 2,
        "strict_source_payload_count_excluding_provenance": 1,
        "all_payload_slots_filled": True,
        "all_required_payloads_source_selected": False,
        "HRG_numeric_specialization_source_selected": False,
        "nonHiggs_prediction_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    universal_gate = {
        "schema": "MTTROUniversalAdmissionGateAfterSelector.v1",
        "status": "RO_UNIVERSAL_ADMISSION_GATE_FAMILY_SELECTED_HRG_NOT_ADMITTED",
        "closure_claimed": True,
        "policy_import": crossuse["admission_criteria"],
        "family_selector_source_selected": True,
        "value_source_derived": False,
        "nonHiggs_prediction_emitted": False,
        "UP_RET_OVERLAP_family_class_selected": True,
        "UP_RET_OVERLAP_HRG_universal_admitted": False,
        "admission_failure_reasons": [
            "HRG numeric specialization is calibrated, not source-derived.",
            "No non-Higgs prediction uses the same HRG value without retuning.",
            "The H-sector map remains empirical/conditional rather than strict source.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterROFamilySelectorTheorem.v1",
        "status": "NEXT_FRONTIER_RO_VALUE_SOURCE_OR_NONHIGGS_MAP_EXECUTION",
        "closure_claimed": True,
        "closed_here": [
            "RO.family_selector source-selected at retarded-overlap family-class level",
            "full RO payload rebuilt after selector theorem",
            "non-Higgs prediction map reattempted after selector theorem",
            "universal admission gate replayed and still rejects HRG",
            "provenance certificate updated after selector theorem",
        ],
        "still_open": [
            "source-derived RO.value_source or strict R_H^RG",
            "strict source-selected RO.H_sector_map",
            "accepted RO.nonHiggs_sector_map using HRG specialization",
            "non-Higgs prediction emitted without retuning",
            "universal admission of UP-RET-OVERLAP.HRG",
            "strict selected K_threshold.Omega_H.lambda",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedROFamilySelectorSourceTheoremOrNonHiggsPredictionMap",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": family_theorem["theorem"],
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "RO_family_selector_source_selected": True,
            "RO_family_selector_HRG_specialization_selected": False,
            "RO_value_source_derived": False,
            "RO_H_sector_map_strict_source_selected": False,
            "RO_nonHiggs_sector_map_accepted": False,
            "RO_nonHiggs_prediction_emitted": False,
            "RO_provenance_certificate_closed": True,
            "UP_RET_OVERLAP_HRG_universal_admitted": False,
            "UP_RET_OVERLAP_HRG_H_only_empirical": True,
            "conditional_empirical_H_K_layer_10_of_10": True,
            "strict_source_tier_9_of_10": True,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG": hrg_value,
            "source_selected_payload_count": full_payload["source_selected_payload_count"],
            "strict_source_payload_count_excluding_provenance": full_payload[
                "strict_source_payload_count_excluding_provenance"
            ],
            "accepted_nonHiggs_map_count": 0,
            "nonHiggs_prediction_count": 0,
            "charged_strict_Lrowlocal_row_count": pairing_candidate["closure_decision"][
                "charged_strict_Lrowlocal_row_count"
            ],
        },
        "packets": {
            "family_theorem": rel(FAMILY_THEOREM),
            "full_payload": rel(FULL_PAYLOAD),
            "nonhiggs_attempt": rel(NONHIGGS_ATTEMPT),
            "universal_gate": rel(UNIVERSAL_GATE),
            "cutset": rel(CUTSET),
        },
        "what_closes": {
            "RO_family_selector_source_theorem": True,
            "full_RO_payload_after_selector": True,
            "nonHiggs_prediction_map_reattempt_after_selector": True,
            "universal_admission_replay_after_selector": True,
            "provenance_update_after_selector": True,
        },
        "what_remains_open": {
            "source_derived_RO_value_source": True,
            "strict_source_selected_RO_H_sector_map": True,
            "accepted_RO_nonHiggs_sector_map": True,
            "RO_nonHiggs_prediction_without_retuning": True,
            "universal_admission_of_HRG": True,
            "strict_selected_K_threshold_Omega_H_lambda": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedROFamilySelectorSourceTheoremOrNonHiggsPredictionMap",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "proof_note": rel(NOTE),
        "verified_packets": list(candidate["packets"].values()),
        "closure_claimed": True,
        "RO_family_selector_source_selected": True,
        "RO_family_selector_HRG_specialization_selected": False,
        "RO_value_source_derived": False,
        "accepted_nonHiggs_map_count": 0,
        "nonHiggs_prediction_count": 0,
        "UP_RET_OVERLAP_HRG_universal_admitted": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected RO Family Selector Source Theorem or Non-Higgs Prediction Map v1

Status: `{STATUS}`

## Theorem

`RO.family_selector` is now source-selected at the retarded-overlap
family-class level.  The proof source is the selected same-source dynamic matter
overlap packet plus the charged retarded-overlap spectral-pairing lemma:

```text
abs(<K_s,g, K_row K_s,g>) = abs(Tr(P_s,g H1_s)),  s in {{u,d,e}}
```

This selects the `UP-RET-OVERLAP` family class.  It does **not** select the HRG
numeric specialization.

## Full Payload After Theorem

- `RO.family_selector`: source-selected as family class.
- `RO.value_source`: still empirical calibrated HRG value, source value open.
- `RO.H_sector_map`: still controlled empirical, strict H map open.
- `RO.nonHiggs_sector_map`: reattempted after selector theorem, `0` accepted maps.
- `RO.nonHiggs_prediction_evaluator`: replayed after selector theorem, `0` predictions.
- `RO.provenance_certificate`: updated and closed.

## Boundary

`UP-RET-OVERLAP.HRG={hrg_value}` is still calibrated, not source-derived.
`lambda_H` remains calibration, not prediction.  The universal admission gate
still rejects HRG because no non-Higgs prediction uses the same HRG value without
retuning.

## Next

`{NEXT}`
"""

    write_json(FAMILY_THEOREM, family_theorem)
    write_json(FULL_PAYLOAD, full_payload)
    write_json(NONHIGGS_ATTEMPT, nonhiggs_attempt)
    write_json(UNIVERSAL_GATE, universal_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    for path in [OUTPUT, CERT, NOTE]:
        print(f"Wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
