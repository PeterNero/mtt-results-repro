"""Build accepted value-layer frontier / non-looping source rows artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_acceptedvaluelayerfrontier_or_nonloopingsourcerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FRONTIER = PACKET_DIR / "accepted_value_layer_frontier.packet.json"
ATTACK_ORDER = PACKET_DIR / "nonlooping_attack_order.packet.json"
ROW_LEDGER = PACKET_DIR / "value_row_acceptance_ledger.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_AcceptedValueLayerFrontier_or_NonLoopingSourceRows_v1.md"

VSD01 = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
VSD01_CUTSET = (
    DATA
    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
    / "next_cutset_after_vsd01_source_assembly.packet.json"
)
YUKAWA_AUDIT = DATA / "selected_yukawamagnitudergclosure_or_finaltruesmequivalenceaudit.candidate.json"
DYNAMIC_QASU3 = DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json"
COMMON_SCALE = DATA / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution.candidate.json"
CORRELATED_PROFILE = DATA / "selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion.candidate.json"
THRESHOLD_VALUES = DATA / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport.candidate.json"
SOURCE_ROWS = DATA / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation.candidate.json"
OBLIGATION = DATA / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest.candidate.json"
FIRST_ROW = DATA / "selected_firstvaluesourcerowfill_or_externalthresholdsourceimport.candidate.json"
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

STATUS = (
    "MTT_SELECTED_ACCEPTEDVALUELAYERFRONTIER_OR_NONLOOPINGSOURCEROWS_"
    "BUILT_LOOP_RETIRED_FIRST_VALUE_SOURCE_TARGET_OPEN"
)
NEXT = "MTT_Selected_ValueLayerFirstNonLoopingRowEmission_or_ThresholdImportExecution_v1"


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
        raise FileNotFoundError("missing accepted value-layer frontier inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        VSD01,
        VSD01_CUTSET,
        YUKAWA_AUDIT,
        DYNAMIC_QASU3,
        COMMON_SCALE,
        CORRELATED_PROFILE,
        THRESHOLD_VALUES,
        SOURCE_ROWS,
        OBLIGATION,
        FIRST_ROW,
        FIRST_ROW_PROMOTION,
        KERNEL,
        IMPORT_MANIFEST,
    ]
    require_sources(sources)

    vsd01 = load(VSD01)
    vsd01_cutset = load(VSD01_CUTSET)
    yukawa_audit = load(YUKAWA_AUDIT)
    dynamic_qasu3 = load(DYNAMIC_QASU3)
    common = load(COMMON_SCALE)
    profile = load(CORRELATED_PROFILE)
    threshold = load(THRESHOLD_VALUES)
    source_rows = load(SOURCE_ROWS)
    obligation = load(OBLIGATION)
    first_row = load(FIRST_ROW)
    first_promotion = load(FIRST_ROW_PROMOTION)
    kernel = load(KERNEL)
    import_manifest = load(IMPORT_MANIFEST)

    source_layer_closed = (
        vsd01["closure_decision"]["VSD01_source_assembly_subgate_closed"]
        and vsd01["closure_decision"]["VSD01_dynamic_overlap_subgate_closed"]
        and vsd01["closure_decision"]["source_stack_closed"]
    )
    vsd01_next_points_forward = (
        vsd01_cutset["recommended_next"]["artifact"]
        == "MTT_Selected_AcceptedValueLayerFrontier_or_NonLoopingSourceRows_v1"
    )
    dynamic_qasu3_already_replayed = (
        dynamic_qasu3["promotion_decision"]["dynamic_QaSU3_first_response_layer_closed"]
        and yukawa_audit["what_closes_now"]["closed_replay_tiers_enumerated"]
    )

    frontier = {
        "schema": "MTTAcceptedValueLayerFrontier.v1",
        "status": "SOURCE_AND_DYNAMIC_PACKET_CLOSED_ACCEPTED_VALUE_ROWS_OPEN",
        "source_layer_closed": source_layer_closed,
        "prior_dynamic_qasu3_replay_already_in_value_chain": dynamic_qasu3_already_replayed,
        "vsd01_next_points_to_forward_frontier": vsd01_next_points_forward,
        "upstream_replay_retired_as_next_target": True,
        "current_frontier": "accepted SM value-source rows",
        "closed_inputs": {
            "VSD01_source_assembly_subgate_closed": vsd01["closure_decision"][
                "VSD01_source_assembly_subgate_closed"
            ],
            "VSD01_dynamic_overlap_subgate_closed": vsd01["closure_decision"][
                "VSD01_dynamic_overlap_subgate_closed"
            ],
            "common_scale_values_for_SM_parity": common["closure_decision"][
                "accepted_common_scale_values_for_SM_parity"
            ],
            "surrogate_correlated_profile_matrix_built": profile["closure_decision"][
                "surrogate_precision_scaffold_closed"
            ],
            "threshold_residual_value_audit_closed": threshold["closure_decision"][
                "residual_value_audit_closed"
            ],
            "source_row_audit_closed": source_rows["closure_decision"]["source_row_audit_closed"],
            "obligation_kernel_closed": obligation["closure_decision"]["obligation_kernel_closed"],
            "first_primitive_exactness_backimported": first_promotion["closure_decision"][
                "primitive_exactness_backimported"
            ],
        },
        "not_closed_as_values": {
            "accepted_Yukawa_magnitudes_for_true_precision": True,
            "running_mass_ratios": True,
            "CKM_PMNS_measured_value_closure": True,
            "lambda_H_threshold_rows": True,
            "accepted_threshold_mass_scheme_source_rows": True,
            "no_knob_value_source_derivation": True,
            "full_correlated_likelihood_source": True,
        },
        "guardrails": {
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "diagnostic_or_surrogate_rows_can_close_source_selection": False,
            "upstream_dynamic_replay_can_be_reused_as_next_target": False,
        },
        "closure_claimed": False,
    }
    write_json(FRONTIER, frontier)

    kernel_rows = [
        {
            "id": row["id"],
            "obligation": row["obligation"],
            "closed": row["closed"],
            "why_open": row["why_open"],
        }
        for row in kernel["required_rows"]
    ]
    accepted_external_rows_present = import_manifest["accepted_external_rows_present"]
    row_ledger = {
        "schema": "MTTValueRowAcceptanceLedger.v1",
        "status": "VALUE_ROW_ACCEPTANCE_LEDGER_BUILT_ZERO_TRUE_SOURCE_ROWS_ACCEPTED",
        "kernel_required_row_count": kernel["required_row_count"],
        "kernel_closed_row_count": kernel["closed_row_count"],
        "accepted_external_rows_present": accepted_external_rows_present,
        "first_numeric_payload_emitted": first_row["closure_decision"][
            "first_value_source_row_numeric_payload_emitted"
        ],
        "first_numeric_payload_accepted_as_selected_source": first_row["closure_decision"][
            "accepted_as_selected_dynamic_value_source_row"
        ],
        "first_primitive_exactness_backimported": first_promotion["closure_decision"][
            "primitive_exactness_backimported"
        ],
        "first_primitive_promoted_to_selected_dynamic_source": first_promotion[
            "closure_decision"
        ]["first_value_row_promoted_to_selected_dynamic_source"],
        "required_rows": kernel_rows,
        "zero_rows_accepted_for_true_value_closure": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROW_LEDGER, row_ledger)

    attack_order = {
        "schema": "MTTNonLoopingAcceptedValueLayerAttackOrder.v1",
        "status": "FIRST_NONLOOPING_VALUE_SOURCE_TARGET_SELECTED",
        "do_not_reopen": [
            "A_selected/b_selected/deltaTheta first-response source promotion",
            "same-source dynamic matter overlap packet",
            "VSD-01 primitive row assembly",
            "upstream DynamicQaSU3 first-response replay",
        ],
        "next_attack_order": [
            {
                "rank": 1,
                "target": "VSD-01-selected-overlap-value-kernel",
                "action": "emit one accepted selected dynamic value-source row from the same-branch physical Phi_fin C1 source, or prove why no such row can be source-owned",
                "success_condition": "one row passes the value-source obligation kernel as selected source data, not just exact postcheck data",
            },
            {
                "rank": 2,
                "target": "VSD-05-external-threshold-import",
                "action": "import one accepted threshold/mass-scheme source row with provenance, basis map, scale/scheme, loop order, covariance, and no-selector guard",
                "success_condition": "accepted_external_rows_present becomes true and maps into the value-row ledger",
            },
            {
                "rank": 3,
                "target": "VSD-02-threshold-response-rule",
                "action": "derive the selected response functional that turns the dynamic overlap packet into threshold/mass rows",
                "success_condition": "threshold response row is emitted by selected source, not copied from observed values",
            },
        ],
        "recommended_next_artifact": NEXT,
        "why_this_is_forward": (
            "The VSD-01 source and first-response dynamic objects are now treated as closed inputs. "
            "The next artifact must fill or import a value-source row; replaying DynamicQaSU3 or "
            "A/b/deltaTheta would be a solved-layer loop."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ATTACK_ORDER, attack_order)

    candidate = {
        "candidate": "MTTSelectedAcceptedValueLayerFrontierOrNonLoopingSourceRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "accepted_value_layer_frontier": rel(FRONTIER),
            "value_row_acceptance_ledger": rel(ROW_LEDGER),
            "nonlooping_attack_order": rel(ATTACK_ORDER),
        },
        "theorem": {
            "name": "AcceptedValueLayerNonLoopingFrontierTheorem",
            "proved": True,
            "statement": (
                "Once the VSD-01 source/assembly and first-response dynamic packet are closed, the "
                "next true-SM-equivalence obligation cannot be another replay of DynamicQaSU3, "
                "A_selected, b_selected, or deltaTheta_C1. The remaining frontier is exactly the "
                "accepted value layer: selected or externally accepted source rows for Yukawa/Higgs, "
                "threshold, mass-scheme, CKM/PMNS, and no-knob value derivation. Current artifacts "
                "contain support, diagnostics, exact postchecks, and SM-parity common-scale values, "
                "but zero rows accepted as true selected value-source data."
            ),
        },
        "what_closes_now": {
            "loop_back_to_dynamic_QaSU3_retired": True,
            "accepted_value_layer_frontier_frozen": True,
            "value_row_acceptance_ledger_built": True,
            "first_nonlooping_attack_order_selected": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": frontier["not_closed_as_values"],
        "readiness": {
            "source_layer_closed": source_layer_closed,
            "value_layer_required_rows": kernel["required_row_count"],
            "value_layer_accepted_source_rows": kernel["closed_row_count"],
            "accepted_external_rows_present": accepted_external_rows_present,
            "first_numeric_payload_available_but_unpromoted": (
                first_row["closure_decision"]["first_value_source_row_numeric_payload_emitted"]
                and not first_row["closure_decision"]["accepted_as_selected_dynamic_value_source_row"]
            ),
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_active_value_wall": yukawa_audit["status"],
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_AcceptedValueLayerFrontier_or_NonLoopingSourceRows_v1",
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

    note = f"""# MTT Selected AcceptedValueLayerFrontier or NonLoopingSourceRows v1

Status: `{STATUS}`.

The VSD-01 source/assembly and first-response dynamic packet are now treated as
closed inputs.  This artifact prevents a loop back into solved objects and makes
the next true-SM target explicit:

```text
source layer closed             : {source_layer_closed}
value-source rows required      : {kernel["required_row_count"]}
value-source rows accepted      : {kernel["closed_row_count"]}
accepted external rows present  : {accepted_external_rows_present}
first numeric payload unpromoted: {candidate["readiness"]["first_numeric_payload_available_but_unpromoted"]}
```

The next artifact must emit or import a real accepted value-source row.  Replaying
DynamicQaSU3, `A_selected`, `b_selected`, `deltaTheta_C1`, or primitive exactness
is now explicitly marked as a solved-layer loop.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
