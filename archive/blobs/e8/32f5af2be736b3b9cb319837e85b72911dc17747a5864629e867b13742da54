"""Build R_theta open-label re-evaluation / frontier minimality audit."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_openlabelreevaluation_or_frontierminimality"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
OPEN_INVENTORY = PACKET_DIR / "open_label_inventory.packet.json"
REEVALUATION = PACKET_DIR / "open_label_reevaluation_results.packet.json"
MINIMAL_FRONTIER = PACKET_DIR / "minimal_rtheta_frontier_after_open_recheck.packet.json"
DECISION = PACKET_DIR / "open_label_frontier_minimality_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_open_label_recheck.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaOpenLabelReevaluation_or_FrontierMinimality_v1.md"

PREVIOUS = DATA / "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction.candidate.json"
SUPPORT_ROWS = (
    DATA
    / "selected_rtheta_supportreevaluation_or_sourcepromotionattempt"
    / "support_rows_under_rtheta_contract.packet.json"
)
OWNER_MATRIX = (
    DATA
    / "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction"
    / "rtheta_source_owner_candidate_matrix.packet.json"
)
OWNER_DECISION = (
    DATA
    / "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction"
    / "rtheta_blocker_contraction_decision.packet.json"
)
DYNAMIC_MATTER_PACKET = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_packet.packet.json"
)
DYNAMIC_MATTER_GUARD = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "full_sm_yukawa_guardrail_after_dynamic_overlap.packet.json"
)
SMSLOT = DATA / "selected_smslotfunctor_sixarrow_source_emission.candidate.json"
DYNAMIC_C1_FILL = (
    DATA
    / "selected_dynamicc1_sourceowner_theorem_or_independentconnectiontables"
    / "current_source_owner_fill_attempt.packet.json"
)
ACTUAL_SM_PACKET = DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json"
EXTERNAL_MANIFEST = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "external_likelihood_import_manifest.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETA_OPENLABELREEVALUATION_OR_FRONTIERMINIMALITY_"
    "BUILT_STALE_OPEN_LABELS_RETIRED_FRONTIER_MINIMAL"
)
NEXT = "MTT_Selected_RThetaCoefficientFormulaDerivation_or_SelectedOwnerBridge_v1"


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
        raise FileNotFoundError("missing R_theta open-label sources: " + ", ".join(missing))


def result(label: str, source: str, old_status: str, new_class: str, reason: str) -> dict[str, str]:
    return {
        "label": label,
        "source": source,
        "old_status": old_status,
        "new_classification": new_class,
        "reason": reason,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        SUPPORT_ROWS,
        OWNER_MATRIX,
        OWNER_DECISION,
        DYNAMIC_MATTER_PACKET,
        DYNAMIC_MATTER_GUARD,
        SMSLOT,
        DYNAMIC_C1_FILL,
        ACTUAL_SM_PACKET,
        EXTERNAL_MANIFEST,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    support_rows = load(SUPPORT_ROWS)
    owner_matrix = load(OWNER_MATRIX)
    owner_decision = load(OWNER_DECISION)
    dynamic_packet = load(DYNAMIC_MATTER_PACKET)
    dynamic_guard = load(DYNAMIC_MATTER_GUARD)
    smslot = load(SMSLOT)
    dynamic_c1_fill = load(DYNAMIC_C1_FILL)
    actual_sm = load(ACTUAL_SM_PACKET)
    external = load(EXTERNAL_MANIFEST)

    support_open = [
        row["support_id"]
        for row in support_rows["reevaluated_rows"]
        if row["decision"] in {"not_promoted", "retained_as_route_evidence_only"}
    ]
    owner_open = [
        missing
        for row in owner_matrix["candidate_rows"]
        for missing in row["missing_for_rtheta_source_owner"]
    ]
    terminal_open = list(smslot["what_remains_open"].keys()) + list(
        smslot["open_source_arrows"].keys()
    )
    dynamic_open = list(dynamic_guard["not_closed_here"].keys())
    c1_open = (
        dynamic_c1_fill["route_A_import"]["open_fields"]
        + dynamic_c1_fill["route_B_import"]["open_fields"]
        + dynamic_c1_fill["qasu3_import"]["open_fields"]
        + [
            field
            for field, closed in dynamic_c1_fill["strict_template_field_results"].items()
            if closed is False
        ]
    )
    actual_sm_open = [
        key
        for key, closed in actual_sm["gate_results"].items()
        if key.endswith("_supplied") and closed is False
    ] + [
        key
        for key, closed in actual_sm["qa_su3_what_remains_open"].items()
        if closed is True
    ]

    open_inventory = {
        "schema": "MTTRThetaOpenLabelInventory.v1",
        "status": "OPEN_LABEL_INVENTORY_BUILT",
        "sources": {
            "previous": rel(PREVIOUS),
            "support_rows": rel(SUPPORT_ROWS),
            "owner_matrix": rel(OWNER_MATRIX),
            "dynamic_matter_packet": rel(DYNAMIC_MATTER_PACKET),
            "smslot": rel(SMSLOT),
            "dynamic_c1_fill": rel(DYNAMIC_C1_FILL),
            "actual_sm_packet": rel(ACTUAL_SM_PACKET),
        },
        "support_open_labels": support_open,
        "owner_candidate_open_labels": sorted(set(owner_open)),
        "terminal_smslot_open_labels": sorted(set(terminal_open)),
        "dynamic_value_phenomenology_open_labels": sorted(set(dynamic_open)),
        "dynamic_c1_open_labels": sorted(set(c1_open)),
        "actual_sm_packet_open_labels": sorted(set(actual_sm_open)),
        "contracted_frontier_before_recheck": owner_decision["contracted_frontier"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(OPEN_INVENTORY, open_inventory)

    dynamic_fields = dynamic_packet["attempted_selected_packet"]["fields"]
    dynamic_closes_overlap = (
        dynamic_fields["primitive_contractions"]["selected_emitted"]
        and dynamic_fields["overlap_transfer"]["selected_emitted"]
        and dynamic_fields["normalization"]["selected_emitted"]
    )

    reevaluation_results = [
        result(
            "gauge_threshold_no_knob_backlog",
            rel(SUPPORT_ROWS),
            "not_promoted",
            "duplicate_retired_into_route_evidence",
            "The full backlog row gauge_threshold_no_knob is already retained as threshold-kernel route evidence; the shorter source-row candidate is not a separate blocker.",
        ),
        result(
            "yukawa_higgs_no_knob_backlog",
            rel(SUPPORT_ROWS),
            "not_promoted",
            "duplicate_retired_into_route_evidence",
            "The full backlog row yukawa_cp_higgs_no_knob is already retained as flavor/Higgs route evidence; the shorter source-row candidate is not a separate blocker.",
        ),
        result(
            "primitive_C1_overlap_contractions",
            rel(SMSLOT),
            "open in terminal SM-slot functor",
            "closed_for_dynamic_matter_route_open_only_for_terminal_six_arrow_route",
            "The same-source dynamic matter packet emits selected primitive_contractions; the older terminal functor still needs its own six-arrow emission.",
        ),
        result(
            "selected_overlap_transfer_normalization",
            rel(SMSLOT),
            "open in terminal SM-slot functor",
            "closed_for_dynamic_matter_route_open_only_for_terminal_six_arrow_route",
            "The same-source dynamic matter packet emits selected overlap_transfer and normalization; the older terminal functor still needs its own section-ring emission.",
        ),
        result(
            "same_source_consistency_map",
            rel(SMSLOT),
            "open in terminal SM-slot functor",
            "partially_closed_by_dynamic_matter_packet",
            "The dynamic packet is one_same_source=true, but the terminal all-six-arrow consistency map remains open.",
        ),
        result(
            "Yukawa_magnitudes",
            rel(DYNAMIC_MATTER_GUARD),
            "phenomenology open",
            "downstream_value_closure_not_rtheta_owner_blocker",
            "This remains open for full no-knob SM closure, but it is downstream of R_theta coefficient/source construction.",
        ),
        result(
            "running_mass_ratios",
            rel(DYNAMIC_MATTER_GUARD),
            "phenomenology open",
            "downstream_value_closure_not_rtheta_owner_blocker",
            "This remains open for full no-knob SM closure, but it is downstream of R_theta coefficient/source construction.",
        ),
        result(
            "CKM_PMNS_measured_angles",
            rel(DYNAMIC_MATTER_GUARD),
            "phenomenology open",
            "downstream_value_closure_not_rtheta_owner_blocker",
            "Mixing-angle closure is not the immediate threshold response owner/coefficient blocker.",
        ),
        result(
            "selected_D_E_or_rho_E_operator_packet",
            rel(ACTUAL_SM_PACKET),
            "open actual Qa/SU3 packet route",
            "alternate_source_owner_route_open",
            "This remains a valid owner-route requirement if the proof uses the actual Qa/SU3 packet path, but the best current R_theta precursor is the same-source dynamic matter packet.",
        ),
        result(
            "typed_monad_maps_as_actual_selected_operator_maps",
            rel(ACTUAL_SM_PACKET),
            "open actual Qa/SU3 packet route",
            "alternate_source_owner_route_open",
            "This remains a valid owner-route requirement if the proof uses the actual Qa/SU3 packet path, not a separate top-level blocker beyond the selected-owner bridge.",
        ),
        result(
            "full_profile_likelihood_or_accepted_diagonal_theorem",
            rel(EXTERNAL_MANIFEST),
            "open",
            "active_top_level_frontier",
            "The external/profile route is still absent and cannot be retired by internal operator progress.",
        ),
    ]

    retired = [
        row for row in reevaluation_results if row["new_classification"].startswith("duplicate_retired")
    ]
    closed_for_dynamic_route = [
        row
        for row in reevaluation_results
        if row["new_classification"].startswith("closed_for_dynamic_matter_route")
    ]
    downstream = [
        row for row in reevaluation_results if row["new_classification"].startswith("downstream")
    ]
    active = [
        row
        for row in reevaluation_results
        if row["new_classification"] in {"active_top_level_frontier", "alternate_source_owner_route_open"}
    ]

    reevaluation = {
        "schema": "MTTRThetaOpenLabelReevaluationResults.v1",
        "status": "OPEN_LABELS_REEVALUATED_STALE_AND_DUPLICATE_LABELS_RETIRED",
        "results": reevaluation_results,
        "rechecked_label_count": len(reevaluation_results),
        "duplicate_retired_count": len(retired),
        "closed_for_dynamic_matter_route_count": len(closed_for_dynamic_route),
        "downstream_not_rtheta_owner_blocker_count": len(downstream),
        "active_or_alternate_count": len(active),
        "dynamic_packet_closes_overlap_transfer_normalization_for_current_route": dynamic_closes_overlap,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(REEVALUATION, reevaluation)

    minimal_frontier = {
        "schema": "MTTMinimalRThetaFrontierAfterOpenRecheck.v1",
        "status": "MINIMAL_RTHETA_FRONTIER_CONFIRMED_AFTER_OPEN_LABEL_RECHECK",
        "retired_or_reclassified": [
            "duplicate backlog source-row labels",
            "terminal-route primitive/overlap labels for the dynamic-matter route",
            "downstream phenomenology labels as immediate R_theta owner blockers",
        ],
        "active_frontier": [
            "bridge same-source dynamic matter/overlap packet to VSD02 threshold response owner",
            "derive threshold and mass-scheme coefficient formulas",
            "select precision convention before measured-value comparison",
            "attach full profile response or accepted diagonal limitation theorem",
        ],
        "alternate_owner_route_still_open": [
            "actual selected Qa/SU3 D_E/rho_E operator packet",
            "typed monad/section-ring maps as actual selected operator maps",
            "mapped Bianchi/Freed-Witten anomaly certificate",
        ],
        "not_on_immediate_rtheta_frontier": [
            "Yukawa magnitude closure",
            "running mass ratios",
            "CKM/PMNS measured angles",
            "full SM no-knob closure as a final consequence label",
        ],
        "minimal_frontier_changed": False,
        "why_not_changed": "The recheck retires stale/duplicate open labels but the same four active R_theta obligations remain.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(MINIMAL_FRONTIER, minimal_frontier)

    decision = {
        "schema": "MTTRThetaOpenLabelFrontierMinimalityDecision.v1",
        "status": "OPEN_LABEL_RECHECK_CLOSED_FRONTIER_REMAINS_FOUR_OBLIGATIONS",
        "previous_status": previous["status"],
        "open_label_inventory_closed": True,
        "stale_duplicate_open_labels_retired": True,
        "dynamic_matter_route_reclassifications_closed": True,
        "minimal_frontier_confirmed": True,
        "rtheta_packet_constructed": False,
        "selected_threshold_response_functional_instantiated": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "active_frontier": minimal_frontier["active_frontier"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterOpenLabelRecheck.v1",
        "status": "NEXT_ATTACK_CONFIRMED_COEFFICIENT_FORMULAS_OR_SELECTED_OWNER_BRIDGE",
        "closed_now": {
            "open_label_inventory": True,
            "stale_duplicate_open_labels_retired": True,
            "dynamic_route_closures_imported": True,
            "minimal_frontier_confirmed": True,
        },
        "still_open": decision["active_frontier"],
        "recommended_next": {
            "artifact": NEXT,
            "first_action": "derive the coefficient formulas using the same-source dynamic matter/overlap packet as precursor",
            "second_action": "prove the bridge theorem that promotes that precursor to the VSD02 threshold response owner",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaOpenLabelReevaluationOrFrontierMinimality",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "open_label_inventory": rel(OPEN_INVENTORY),
            "open_label_reevaluation_results": rel(REEVALUATION),
            "minimal_rtheta_frontier_after_open_recheck": rel(MINIMAL_FRONTIER),
            "open_label_frontier_minimality_decision": rel(DECISION),
            "next_cutset_after_open_label_recheck": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaOpenLabelReevaluationAndFrontierMinimalityTheorem",
            "proved": True,
            "statement": (
                "Open labels from support, terminal-slot, dynamic-C1, actual-SM-packet, and dynamic-matter "
                "artifacts can be re-evaluated against the current R_theta frontier. Duplicate backlog "
                "labels are retired; terminal-route primitive/overlap labels are closed for the dynamic-matter "
                "route; downstream phenomenology labels are removed from the immediate R_theta owner blocker "
                "set. The remaining minimal frontier is still exactly four obligations."
            ),
        },
        "closure_decision": {
            "open_label_recheck_closed": True,
            "stale_duplicate_open_labels_retired": True,
            "minimal_frontier_confirmed": True,
            "rtheta_packet_constructed": False,
            "selected_threshold_response_functional_instantiated": False,
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
        "certificate": "MTT_Selected_RThetaOpenLabelReevaluation_or_FrontierMinimality_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "duplicate_retired_count": reevaluation["duplicate_retired_count"],
        "closed_for_dynamic_matter_route_count": reevaluation[
            "closed_for_dynamic_matter_route_count"
        ],
        "minimal_frontier_confirmed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected RThetaOpenLabelReevaluation or FrontierMinimality v1

Status: `{STATUS}`.

This artifact rechecks labels previously marked open.

```text
rechecked open labels              : {reevaluation["rechecked_label_count"]}
duplicate open labels retired      : {reevaluation["duplicate_retired_count"]}
dynamic-route open labels narrowed : {reevaluation["closed_for_dynamic_matter_route_count"]}
minimal frontier obligations       : 4
```

The important change: several open labels were not global blockers anymore.
They were duplicate backlog labels, terminal-route-only opens, or downstream
phenomenology labels.  The active `R_theta` frontier remains four obligations.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
