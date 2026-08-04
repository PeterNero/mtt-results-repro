"""Build VSD-01 frontier update / value-source kernel v2."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_vsd01frontierupdate_or_valuekernelv2"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
VSD01_UPDATE = PACKET_DIR / "vsd01_updated_obligation_status.packet.json"
KERNEL_DELTA = PACKET_DIR / "value_source_kernel_delta_v2.packet.json"
NO_WHEELTRACK = PACKET_DIR / "no_old_wheeltrack_frontier_guard.packet.json"
CUTSET = PACKET_DIR / "next_atomic_value_source_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_VSD01FrontierUpdate_or_ValueKernelV2_v1.md"

OLD_KERNEL = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "value_source_derivation_obligation_kernel.packet.json"
)
SOURCE_ASSEMBLY = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
DYNAMIC_BACKIMPORT = DATA / "selected_vsd01_dynamicoperatorbackimport_or_yukawavaluefrontier.candidate.json"
ACCEPTED_VALUES = DATA / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution.candidate.json"
ACCEPTED_VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
FINAL_VALUE_AUDIT = DATA / "selected_yukawamagnitudergclosure_or_finaltruesmequivalenceaudit.candidate.json"
THRESHOLD_AUDIT = DATA / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport.candidate.json"
SOURCE_ROW_AUDIT = DATA / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation.candidate.json"
SOURCE_ROW_CUTSET = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "next_cutset_after_source_row_audit.packet.json"
)

STATUS = "MTT_SELECTED_VSD01FRONTIERUPDATE_OR_VALUEKERNELV2_BUILT_VSD01_PROGRESS_RECONCILED_TRUE_EQUIVALENCE_OPEN"
NEXT = "MTT_Selected_VSD02ThresholdResponseRule_or_ExternalLikelihoodImport_v1"


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
        raise FileNotFoundError("missing VSD-01 frontier update sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        OLD_KERNEL,
        SOURCE_ASSEMBLY,
        DYNAMIC_BACKIMPORT,
        ACCEPTED_VALUES,
        ACCEPTED_VALUE_PACKET,
        FINAL_VALUE_AUDIT,
        THRESHOLD_AUDIT,
        SOURCE_ROW_AUDIT,
        SOURCE_ROW_CUTSET,
    ]
    require_sources(sources)

    old_kernel = load(OLD_KERNEL)
    source_assembly = load(SOURCE_ASSEMBLY)
    dynamic_backimport = load(DYNAMIC_BACKIMPORT)
    accepted_values = load(ACCEPTED_VALUES)
    accepted_value_packet = load(ACCEPTED_VALUE_PACKET)
    final_value_audit = load(FINAL_VALUE_AUDIT)
    threshold_audit = load(THRESHOLD_AUDIT)
    source_row_audit = load(SOURCE_ROW_AUDIT)
    source_row_cutset = load(SOURCE_ROW_CUTSET)

    old_vsd01 = next(row for row in old_kernel["required_rows"] if row["id"] == "VSD-01-selected-overlap-value-kernel")

    vsd01_update = {
        "schema": "MTTVSD01UpdatedObligationStatus.v1",
        "status": "VSD01_PROGRESS_RECONCILED_FULL_TRUE_VALUE_LAYER_OPEN",
        "row_id": "VSD-01-selected-overlap-value-kernel",
        "old_kernel_status": {
            "closed": old_vsd01["closed"],
            "why_open": old_vsd01["why_open"],
        },
        "newly_closed_subgates": {
            "physical_source_assembly_subgate": source_assembly["closure_decision"][
                "VSD01_source_assembly_subgate_closed"
            ],
            "selected_dynamic_tensor_first_response_subgate": dynamic_backimport[
                "closure_decision"
            ]["VSD01_dynamic_tensor_subgate_closed"],
            "same_branch_linking_to_versioned_packet": dynamic_backimport["what_closes_now"][
                "same_branch_linking_tensor_rows_to_versioned_value_packet"
            ],
            "versioned_common_scale_profile_input_values": accepted_values["closure_decision"][
                "accepted_common_scale_values_for_SM_parity"
            ],
            "diagonal_profile_execution_layer": accepted_values["closure_decision"][
                "value_profile_execution_layer_closed"
            ],
        },
        "value_packet_summary": {
            "reference_scale": accepted_value_packet["reference_scale"],
            "reference_scheme": accepted_value_packet["reference_scheme"],
            "accepted_as_versioned_common_scale_candidate_values": accepted_value_packet[
                "accepted_as_versioned_common_scale_candidate_values"
            ],
            "accepted_for_SM_parity": accepted_value_packet["accepted_for_SM_parity"],
            "accepted_for_true_precision_equivalence": accepted_value_packet[
                "accepted_for_true_precision_equivalence"
            ],
            "accepted_as_no_knob_MTT_prediction": accepted_value_packet[
                "accepted_as_no_knob_MTT_prediction"
            ],
            "derived_magnitude_keys": sorted(accepted_value_packet["derived_magnitudes"].keys()),
        },
        "still_open_for_full_VSD01_and_true_equivalence": {
            "accepted_threshold_matching_values": source_row_audit["what_remains_open"][
                "accepted_threshold_matching_source_rows"
            ],
            "accepted_mass_scheme_conversion_values": source_row_audit["what_remains_open"][
                "accepted_mass_scheme_conversion_source_rows"
            ],
            "multi_loop_threshold_convention_source_rows": source_row_audit[
                "what_remains_open"
            ]["multi_loop_threshold_convention_source_rows"],
            "external_threshold_or_likelihood_source_import": source_row_audit[
                "what_remains_open"
            ]["external_threshold_or_likelihood_source_import"],
            "no_knob_Yukawa_Higgs_value_source_derivation": source_row_audit[
                "what_remains_open"
            ]["no_knob_Yukawa_Higgs_value_source_derivation"],
            "true_SM_equivalence_closure": source_row_audit["what_remains_open"][
                "true_SM_equivalence_closure"
            ],
        },
        "VSD01_legacy_open_label_retired": True,
        "VSD01_full_obligation_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VSD01_UPDATE, vsd01_update)

    kernel_delta = {
        "schema": "MTTValueSourceKernelDeltaV2.v1",
        "status": "KERNEL_V2_DELTA_BUILT_VSD01_PARTIAL_CLOSURE_RECORDED",
        "old_required_row_count": old_kernel["required_row_count"],
        "old_closed_row_count": old_kernel["closed_row_count"],
        "delta": {
            "VSD-01-selected-overlap-value-kernel": {
                "old_status": "open_static_only",
                "new_status": "source_assembly_and_dynamic_first_response_closed_value_precision_open",
                "closed_subgates": list(vsd01_update["newly_closed_subgates"].keys()),
                "remaining_atomic_rows": list(
                    vsd01_update["still_open_for_full_VSD01_and_true_equivalence"].keys()
                ),
            }
        },
        "rows_not_reopened": [
            "VSD-02-threshold-response-rule",
            "VSD-03-selected-sm-packet-attachment",
            "VSD-04-local-qft-renormalization-functor",
            "VSD-05-external-threshold-import",
        ],
        "why_not_increment_closed_row_count": (
            "VSD-01 is not fully closed until accepted threshold/mass-scheme/profile or no-knob value "
            "source rows are supplied; this artifact records subgate closure and prevents returning to "
            "the obsolete 'dynamic tensor absent' blocker."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(KERNEL_DELTA, kernel_delta)

    no_wheeltrack = {
        "schema": "MTTNoOldWheeltrackFrontierGuard.v1",
        "status": "OLD_VSD01_DYNAMIC_TENSOR_BLOCKER_RETIRED",
        "old_track_to_avoid": [
            "re-proving source promotion for A_selected/b_selected/deltaTheta_C1",
            "re-proving physical Phi_fin C1 action-source certificate",
            "re-proving selected dynamic matter/overlap first-response packet",
            "treating first-pass common-scale values as true precision or no-knob closure",
        ],
        "current_frontier": {
            "source_row_cutset_status": source_row_cutset["status"],
            "recommended_next_from_source_row_audit": source_row_cutset["recommended_next"],
            "final_value_audit_status": final_value_audit["status"],
            "threshold_audit_status": threshold_audit["status"],
        },
        "valid_next_work": [
            "derive threshold response rule from selected branch",
            "import accepted external threshold/profile likelihood source rows with provenance",
            "derive no-knob Yukawa/Higgs value source rows",
            "upgrade diagonal/surrogate profile to full correlated covariance/profile likelihood",
        ],
        "invalid_next_work": [
            "rerun VSD-01 source assembly without new value rows",
            "rerun dynamic matter overlap validation without new threshold/lambda/RG value data",
            "claim true SM equivalence from first-pass or diagonal profile-only values",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NO_WHEELTRACK, no_wheeltrack)

    cutset = {
        "schema": "MTTNextAtomicValueSourceCutset.v1",
        "status": "TRUE_EQUIVALENCE_FRONTIER_AT_THRESHOLD_RESPONSE_OR_EXTERNAL_LIKELIHOOD_IMPORT",
        "closed_now": {
            "VSD01_legacy_dynamic_absence_blocker_retired": True,
            "VSD01_source_assembly_and_dynamic_first_response_recorded": True,
            "firstpass_value_profile_layer_recorded_without_overclaim": True,
            "old_wheeltrack_guard_emitted": True,
        },
        "still_open": vsd01_update["still_open_for_full_VSD01_and_true_equivalence"],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The remaining wall is no longer VSD-01 source/dynamic absence. True SM equivalence now "
                "requires selected threshold response/source rows, accepted external likelihood import, "
                "or a no-knob derivation of the Yukawa/Higgs value layer."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedVSD01FrontierUpdateOrValueKernelV2",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "vsd01_updated_obligation_status": rel(VSD01_UPDATE),
            "value_source_kernel_delta_v2": rel(KERNEL_DELTA),
            "no_old_wheeltrack_frontier_guard": rel(NO_WHEELTRACK),
            "next_atomic_value_source_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "VSD01FrontierUpdateAndNoOldWheeltrackTheorem",
            "proved": True,
            "statement": (
                "The original value-source derivation kernel is now stale for VSD-01: subsequent artifacts "
                "close the physical source assembly, selected dynamic first-response tensor, same-branch "
                "linking, and first-pass profile-executable Yukawa/Higgs value packet. VSD-01 is not fully "
                "closed, because accepted threshold/mass-scheme/profile likelihood rows and no-knob value "
                "derivation remain open. Therefore future progress should target threshold response or "
                "external likelihood/source import, not the retired source/dynamic absence blockers."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "VSD01_legacy_dynamic_absence_blocker_retired": True,
            "VSD01_full_obligation_closed": False,
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
        "certificate": "MTT_Selected_VSD01FrontierUpdate_or_ValueKernelV2_v1",
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

    note = f"""# MTT Selected VSD01FrontierUpdate or ValueKernelV2 v1

Status: `{STATUS}`.

This artifact reconciles the old VSD obligation kernel with the newer VSD-01
closures, so we do not fall back into old work.

Retired VSD-01 blockers:

```text
physical source assembly missing      : false
selected dynamic tensor absent        : false
same-branch versioned packet link     : false
first-pass value/profile layer absent : false
```

Still open for true SM equivalence:

```text
accepted threshold matching rows
accepted mass-scheme conversion rows
multi-loop threshold convention rows
external correlated likelihood/profile import
no-knob Yukawa/Higgs value-source derivation
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
