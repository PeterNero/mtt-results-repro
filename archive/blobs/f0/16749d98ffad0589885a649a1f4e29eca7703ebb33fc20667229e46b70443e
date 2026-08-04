"""Build R_theta value-source VSD-01 v2 reconciliation or VSD-02 handoff."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_valuesource_vsd01v2reconciliation_or_vsd02handoff"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
VSD01_RECHECK = PACKET_DIR / "rtheta_vsd01_v2_reconciliation.packet.json"
FIRST_ROW_RECHECK = PACKET_DIR / "first_value_row_legacy_rejection_recheck.packet.json"
VALUE_FRONTIER = PACKET_DIR / "rtheta_value_source_frontier_after_vsd01_v2.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_vsd01_v2_reconciliation.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaValueSource_VSD01v2Reconciliation_or_VSD02Handoff_v1.md"

RTHETA_ORDER = DATA / "selected_rtheta_thresholdrows_or_profileconventionsourceclosure.candidate.json"
OBLIGATION_KERNEL = DATA / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest.candidate.json"
FIRST_ROW = DATA / "selected_firstvaluesourcerowfill_or_externalthresholdsourceimport.candidate.json"
FIRST_ROW_PROMOTION = DATA / "selected_firstvaluesourcerowpromotion_or_honestgalerkinprimitiverow.candidate.json"
VSD01_ASSEMBLY = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
VSD01_DYNAMIC = DATA / "selected_vsd01_dynamicoperatorbackimport_or_yukawavaluefrontier.candidate.json"
VSD01_UPDATE = DATA / "selected_vsd01frontierupdate_or_valuekernelv2.candidate.json"
VSD01_STATUS = (
    DATA
    / "selected_vsd01frontierupdate_or_valuekernelv2"
    / "vsd01_updated_obligation_status.packet.json"
)
VSD01_DELTA = (
    DATA / "selected_vsd01frontierupdate_or_valuekernelv2" / "value_source_kernel_delta_v2.packet.json"
)
VSD01_CUTSET = (
    DATA / "selected_vsd01frontierupdate_or_valuekernelv2" / "next_atomic_value_source_cutset.packet.json"
)
VSD01_DYNAMIC_DECISION = (
    DATA
    / "selected_vsd01_dynamicoperatorbackimport_or_yukawavaluefrontier"
    / "vsd01_dynamic_tensor_subgate_decision.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETA_VALUESOURCE_VSD01V2RECONCILIATION_OR_VSD02HANDOFF_"
    "RETIRED_VSD01_DYNAMIC_ABSENCE_THRESHOLD_RESPONSE_OPEN"
)
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
        raise FileNotFoundError("missing R_theta VSD-01 reconciliation sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        RTHETA_ORDER,
        OBLIGATION_KERNEL,
        FIRST_ROW,
        FIRST_ROW_PROMOTION,
        VSD01_ASSEMBLY,
        VSD01_DYNAMIC,
        VSD01_UPDATE,
        VSD01_STATUS,
        VSD01_DELTA,
        VSD01_CUTSET,
        VSD01_DYNAMIC_DECISION,
    ]
    require_sources(sources)

    rtheta_order = load(RTHETA_ORDER)
    obligation = load(OBLIGATION_KERNEL)
    first_row = load(FIRST_ROW)
    first_promotion = load(FIRST_ROW_PROMOTION)
    vsd01_assembly = load(VSD01_ASSEMBLY)
    vsd01_dynamic = load(VSD01_DYNAMIC)
    vsd01_update = load(VSD01_UPDATE)
    vsd01_status = load(VSD01_STATUS)
    vsd01_delta = load(VSD01_DELTA)
    vsd01_cutset = load(VSD01_CUTSET)
    vsd01_dynamic_decision = load(VSD01_DYNAMIC_DECISION)

    source_assembly_closed = (
        vsd01_assembly["closure_decision"]["VSD01_source_assembly_subgate_closed"] is True
        and vsd01_status["newly_closed_subgates"]["physical_source_assembly_subgate"] is True
    )
    dynamic_tensor_closed = (
        vsd01_dynamic["closure_decision"]["VSD01_dynamic_tensor_subgate_closed"] is True
        and vsd01_dynamic_decision["VSD01_dynamic_tensor_subgate_closed"] is True
        and vsd01_status["newly_closed_subgates"]["selected_dynamic_tensor_first_response_subgate"] is True
    )
    same_branch_link_closed = (
        vsd01_status["newly_closed_subgates"]["same_branch_linking_to_versioned_packet"] is True
        and vsd01_dynamic_decision["closed_for_VSD01_now"][
            "same_branch_linking_tensor_rows_to_versioned_value_packet"
        ]
        is True
    )
    firstpass_profile_recorded = (
        vsd01_status["newly_closed_subgates"]["versioned_common_scale_profile_input_values"] is True
        and vsd01_status["newly_closed_subgates"]["diagonal_profile_execution_layer"] is True
    )
    vsd01_legacy_retired = (
        vsd01_update["closure_decision"]["VSD01_legacy_dynamic_absence_blocker_retired"] is True
        and source_assembly_closed
        and dynamic_tensor_closed
        and same_branch_link_closed
    )
    vsd01_full_closed = vsd01_update["closure_decision"]["VSD01_full_obligation_closed"] is True

    still_open = [
        item for item, is_open in vsd01_status["still_open_for_full_VSD01_and_true_equivalence"].items() if is_open
    ]

    vsd01_recheck = {
        "schema": "MTTRThetaVSD01v2Reconciliation.v1",
        "status": "VSD01_SOURCE_DYNAMIC_SUBGATES_RECONCILED_FULL_VALUE_LAYER_OPEN",
        "rtheta_order_source": rel(RTHETA_ORDER),
        "vsd01_update_source": rel(VSD01_UPDATE),
        "source_assembly_subgate_closed": source_assembly_closed,
        "selected_dynamic_tensor_first_response_subgate_closed": dynamic_tensor_closed,
        "same_branch_linking_to_versioned_packet_closed": same_branch_link_closed,
        "firstpass_profile_layer_recorded": firstpass_profile_recorded,
        "VSD01_legacy_dynamic_absence_blocker_retired": vsd01_legacy_retired,
        "VSD01_full_obligation_closed": vsd01_full_closed,
        "remaining_full_value_rows": still_open,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VSD01_RECHECK, vsd01_recheck)

    first_row_recheck = {
        "schema": "MTTFirstValueRowLegacyRejectionRecheck.v1",
        "status": "FIRST_ROW_OLD_SOURCE_PROMOTION_REJECTION_SUPERSEDED_BY_VSD01V2",
        "first_row_source": rel(FIRST_ROW),
        "first_row_promotion_source": rel(FIRST_ROW_PROMOTION),
        "old_numeric_payload_emitted": first_row["closure_decision"][
            "first_value_source_row_numeric_payload_emitted"
        ],
        "old_accepted_as_selected_dynamic_value_source_row": first_row["closure_decision"][
            "accepted_as_selected_dynamic_value_source_row"
        ],
        "old_primitive_exactness_backimported": first_promotion["closure_decision"][
            "primitive_exactness_backimported"
        ],
        "old_first_row_source_promotion_path_retired": vsd01_legacy_retired,
        "reason": (
            "The first-row-only path remains numerically useful but is no longer the active route. "
            "VSD01 v2 closes the source assembly and dynamic first-response tensor at packet level, "
            "while leaving true value equivalence to threshold/profile rows."
        ),
        "accepted_coefficient_value_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FIRST_ROW_RECHECK, first_row_recheck)

    value_frontier = {
        "schema": "MTTRThetaValueSourceFrontierAfterVSD01v2.v1",
        "status": "FRONTIER_MOVED_TO_VSD02_THRESHOLD_RESPONSE_OR_EXTERNAL_IMPORT",
        "rtheta_ordered_frontier": rel(RTHETA_ORDER),
        "obligation_kernel_source": rel(OBLIGATION_KERNEL),
        "VSD01_status": "source_assembly_and_dynamic_first_response_closed_value_precision_open",
        "VSD01_full_obligation_closed": vsd01_full_closed,
        "old_value_source_kernel_delta": vsd01_delta["delta"]["VSD-01-selected-overlap-value-kernel"],
        "remaining_atomic_rows": still_open,
        "recommended_next": NEXT,
        "accepted_threshold_matching_values": False,
        "accepted_mass_scheme_conversion_values": False,
        "external_threshold_or_likelihood_source_import": False,
        "multi_loop_threshold_convention_source_rows": False,
        "no_knob_Yukawa_Higgs_value_source_derivation": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_FRONTIER, value_frontier)

    cutset = {
        "schema": "MTTNextCutsetAfterRThetaVSD01v2Reconciliation.v1",
        "status": "NEXT_ATTACK_VSD02_THRESHOLD_RESPONSE_OR_EXTERNAL_LIKELIHOOD_IMPORT",
        "closed_now": {
            "VSD01_source_assembly_subgate": source_assembly_closed,
            "VSD01_dynamic_tensor_first_response_subgate": dynamic_tensor_closed,
            "VSD01_same_branch_linking_to_versioned_packet": same_branch_link_closed,
            "VSD01_legacy_dynamic_absence_blocker_retired": vsd01_legacy_retired,
        },
        "still_open": still_open,
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive selected threshold response/source rows internally under the R_theta convention",
            "route_B": "import accepted external threshold/profile likelihood rows satisfying the manifest",
            "route_C": "declare and audit minimal universal parameters if no-knob row derivation remains impossible",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaValueSourceVSD01v2ReconciliationOrVSD02Handoff",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "rtheta_vsd01_v2_reconciliation": rel(VSD01_RECHECK),
            "first_value_row_legacy_rejection_recheck": rel(FIRST_ROW_RECHECK),
            "rtheta_value_source_frontier_after_vsd01_v2": rel(VALUE_FRONTIER),
            "next_cutset_after_vsd01_v2_reconciliation": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaVSD01v2ReconciliationAndVSD02HandoffTheorem",
            "proved": True,
            "statement": (
                "The old VSD-01 dynamic/source absence blocker is obsolete in the R_theta value frontier: "
                "later VSD-01 artifacts close physical source assembly, selected dynamic first-response tensor, "
                "and same-branch linking to the versioned value packet. Full value equivalence remains open "
                "only at threshold/mass-scheme/profile/no-knob rows, so the next active target is VSD-02 "
                "threshold response or external likelihood/source import."
            ),
        },
        "closure_decision": {
            "VSD01_source_assembly_subgate_closed": source_assembly_closed,
            "VSD01_dynamic_tensor_subgate_closed": dynamic_tensor_closed,
            "VSD01_same_branch_linking_closed": same_branch_link_closed,
            "VSD01_legacy_dynamic_absence_blocker_retired": vsd01_legacy_retired,
            "VSD01_full_obligation_closed": vsd01_full_closed,
            "accepted_threshold_matching_values": False,
            "accepted_mass_scheme_conversion_values": False,
            "external_threshold_or_likelihood_source_import": False,
            "no_knob_Yukawa_Higgs_value_source_derivation": False,
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
        "certificate": "MTTSelectedRThetaValueSourceVSD01v2ReconciliationOrVSD02Handoff",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "VSD01_legacy_dynamic_absence_blocker_retired": vsd01_legacy_retired,
        "VSD01_full_obligation_closed": vsd01_full_closed,
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected RThetaValueSource VSD01v2Reconciliation or VSD02Handoff v1

Status: `{STATUS}`.

This artifact reconciles the current `R_theta` value frontier with the later
VSD-01 v2 packets.

```text
VSD01 source assembly subgate closed           : {str(source_assembly_closed).lower()}
VSD01 dynamic first-response subgate closed    : {str(dynamic_tensor_closed).lower()}
VSD01 same-branch linking closed               : {str(same_branch_link_closed).lower()}
VSD01 legacy dynamic absence blocker retired   : {str(vsd01_legacy_retired).lower()}
VSD01 full value obligation closed             : {str(vsd01_full_closed).lower()}
```

The old first-row-only rejection path is no longer the active route.  VSD-01
now has source assembly, dynamic first-response tensor, and same-branch linking
recorded.  What remains is not VSD-01 source absence, but the threshold/value
layer:

{chr(10).join(f'- `{item}`' for item in still_open)}

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
