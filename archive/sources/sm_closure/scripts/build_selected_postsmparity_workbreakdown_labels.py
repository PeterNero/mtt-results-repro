"""Build stable labels for the post-SM-parity work breakdown."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_postsmparity_workbreakdown_labels"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LABELS = PACKET_DIR / "canonical_work_labels.packet.json"
MATRIX = PACKET_DIR / "remaining_work_status_matrix.packet.json"
ROUTE_MAP = PACKET_DIR / "route_label_map.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PostSMParity_WorkBreakdown_Labels_v1.md"

STATUS = "MTT_SELECTED_POSTSMPARITY_WORKBREAKDOWN_LABELS_BUILT"
NEXT_ARTIFACT = "MTT_Selected_SameSourceDynamicPhiFinC1_or_HonestGalerkinExecution_RouteTest_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    frontier = load(DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier" / "dynamic_qasu3_c1_frontier.packet.json")
    routes = load(DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier" / "three_route_closure_contract.packet.json")
    boundary = load(DATA / "selected_smparityfrozenboundary_or_postsmparityfrontier" / "frozen_smparity_boundary.packet.json")

    closed_labels = [
        {
            "id": "DONE-PARITY-00",
            "category": "closed_boundary",
            "name": "SM-parity replay boundary",
            "status": "CLOSED_FROZEN",
            "evidence": rel(DATA / "selected_smparityfrozenboundary_or_postsmparityfrontier" / "frozen_smparity_boundary.packet.json"),
            "use_going_forward": "Never reopen as active blocker unless a frozen-tier audit fails.",
        },
        {
            "id": "DONE-SOURCE-00",
            "category": "closed_boundary",
            "name": "finite selected operator-source slot layer",
            "status": "CLOSED_FROZEN",
            "evidence": rel(DATA / "selected_heattorsionresponse_finalgate" / "post_eight_slot_true_equivalence_frontier.packet.json"),
            "use_going_forward": "Source-slot assembly is complete: 8/8 closed, 0 remaining.",
        },
        {
            "id": "DONE-DYN-SUPPORT-00",
            "category": "closed_support",
            "name": "post-source dynamic support package",
            "status": "CLOSED_SUPPORT",
            "evidence": rel(DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier" / "dynamic_qasu3_c1_frontier.packet.json"),
            "use_going_forward": "Use as support only; it does not close selected dynamic values.",
        },
    ]

    remaining_labels = [
        {
            "id": "PSM-DYN-01",
            "category": "dynamic_operator_packet",
            "subcategory": "Qa/SU3_dynamic_packet",
            "name": "actual dynamic Qa/SU3 operator packet",
            "status": "OPEN",
            "source_key": "actual_dynamic_QaSU3_operator_packet",
            "closure_condition": "Emit the selected dynamic HYM/End0/C1 packet, not just static route labels or finite source-slot support.",
            "primary_routes": ["ROUTE-C", "ROUTE-B", "ROUTE-A"],
        },
        {
            "id": "PSM-C1-01",
            "category": "dynamic_C1_source",
            "subcategory": "differentiated_PhiFinC1",
            "name": "selected differentiated Phi_fin^C1 source map",
            "status": "OPEN_PRIMARY",
            "source_key": "selected_differentiated_PhiFinC1_source_map",
            "closure_condition": "Prove physical differentiated Phi_fin^C1 applies Q_residual to selected phase/shift legs from the same branch.",
            "primary_routes": ["ROUTE-A"],
        },
        {
            "id": "PSM-C1-02",
            "category": "dynamic_C1_values",
            "subcategory": "primitive_overlap",
            "name": "selected primitive C1 overlap contractions",
            "status": "OPEN",
            "source_key": "selected_primitive_C1_overlap_contractions",
            "closure_condition": "Emit selected primitive C1 contraction values or an honest selected Galerkin replacement.",
            "primary_routes": ["ROUTE-A", "ROUTE-B"],
        },
        {
            "id": "PSM-C1-03",
            "category": "dynamic_C1_values",
            "subcategory": "A_selected",
            "name": "selected A_selected response/Hessian operator",
            "status": "OPEN",
            "source_key": "selected_A_selected",
            "closure_condition": "Promote a theorem-derived selected 72-real response/Hessian operator; conditional replay alone is insufficient.",
            "primary_routes": ["ROUTE-A", "ROUTE-B", "ROUTE-C"],
        },
        {
            "id": "PSM-C1-04",
            "category": "dynamic_C1_values",
            "subcategory": "b_selected",
            "name": "selected b_selected source vector",
            "status": "OPEN_PRIMARY",
            "source_key": "selected_b_selected",
            "closure_condition": "Emit same-source b_selected or Hessian source vector; without it deltaTheta_C1 is not selected.",
            "primary_routes": ["ROUTE-A", "ROUTE-B"],
        },
        {
            "id": "PSM-C1-05",
            "category": "dynamic_C1_values",
            "subcategory": "deltaTheta_C1",
            "name": "selected deltaTheta_C1 solve",
            "status": "OPEN_DEPENDS_ON_PSM-C1-03_PSM-C1-04",
            "source_key": "selected_deltaTheta_C1",
            "closure_condition": "Solve with selected A_selected and b_selected; conditional [1,1] replay is not enough.",
            "primary_routes": ["ROUTE-A", "ROUTE-B", "ROUTE-C"],
        },
        {
            "id": "PSM-C1-06",
            "category": "dynamic_C1_values",
            "subcategory": "sector_response_matrices",
            "name": "selected sector response matrices",
            "status": "OPEN",
            "source_key": "selected_sector_response_matrices",
            "closure_condition": "Emit selected non-scalar sector response matrices with family-rank/nonzero checks.",
            "primary_routes": ["ROUTE-A", "ROUTE-B", "ROUTE-C"],
        },
        {
            "id": "PSM-S2-01",
            "category": "full_operator_values",
            "subcategory": "full_S2",
            "name": "full S2 value emission beyond D_E/gap",
            "status": "OPEN_DOWNSTREAM_OF_DYNAMIC_PACKET",
            "source_key": "full_S2_value_emission_beyond_DE_gap",
            "closure_condition": "Emit full S2 values beyond the finite D_E/gap/heat layer, including dynamic C1-compatible values.",
            "primary_routes": ["ROUTE-C", "ROUTE-A", "ROUTE-B"],
        },
        {
            "id": "PSM-QFT-01",
            "category": "precision_observable_replay",
            "subcategory": "QFT_RG_threshold_covariance",
            "name": "precision QFT observable functor",
            "status": "OPEN_PARALLEL",
            "source_key": "precision_QFT_observable_functor",
            "closure_condition": "Map selected packet plus admitted replay inputs to accepted RG/threshold/covariance/profile observables.",
            "primary_routes": ["ROUTE-C"],
        },
        {
            "id": "PSM-NK-01",
            "category": "no_knob_upgrade",
            "subcategory": "value_derivation",
            "name": "no-proxy/no-knob value derivation",
            "status": "OPEN_STRONGER_THAN_TRUE_EQUIVALENCE",
            "source_key": "no_knob_value_derivation",
            "closure_condition": "Derive SM numerical values without admitting them as measured replay inputs or fitting targets.",
            "primary_routes": ["ROUTE-C", "ROUTE-A", "ROUTE-B"],
        },
    ]

    route_labels = [
        {
            "id": "ROUTE-A",
            "source_route_id": "route_A_same_source_dynamic_PhiFinC1",
            "name": "same-source dynamic Phi_fin^C1 source rule",
            "status": "OPEN_PRIMARY",
            "owns_labels": ["PSM-C1-01", "PSM-C1-02", "PSM-C1-03", "PSM-C1-04", "PSM-C1-05", "PSM-C1-06"],
            "first_test": "A1_source_rule_test",
        },
        {
            "id": "ROUTE-B",
            "source_route_id": "route_B_honest_selected_Galerkin_C1_execution",
            "name": "honest selected Galerkin C1 execution",
            "status": "OPEN_REPLACEMENT",
            "owns_labels": ["PSM-DYN-01", "PSM-C1-02", "PSM-C1-03", "PSM-C1-04", "PSM-C1-05", "PSM-C1-06"],
            "first_test": "B1_galerkin_readiness_test",
        },
        {
            "id": "ROUTE-C",
            "source_route_id": "route_C_superset_bridge",
            "name": "same-branch superset bridge",
            "status": "OPEN_BRIDGE",
            "owns_labels": ["PSM-DYN-01", "PSM-S2-01", "PSM-QFT-01", "PSM-NK-01"],
            "first_test": "C1_superset_bridge_test",
        },
    ]

    frontier_keys = set(frontier["open_dynamic_targets"].keys())
    label_keys = {item["source_key"] for item in remaining_labels}
    labels_cover_frontier = frontier_keys == label_keys
    route_ids_match = [route["source_route_id"] for route in route_labels] == [route["id"] for route in routes["routes"]]

    labels = {
        "schema": "MTTCanonicalPostSMParityWorkLabels.v1",
        "status": "CANONICAL_POSTSMPARITY_LABELS_LOCKED",
        "label_rule": {
            "required_reference_format": "Use label IDs such as PSM-C1-04, not vague phrases like 'the remaining blocker'.",
            "closed_prefixes": ["DONE-PARITY", "DONE-SOURCE", "DONE-DYN-SUPPORT"],
            "remaining_prefixes": ["PSM-DYN", "PSM-C1", "PSM-S2", "PSM-QFT", "PSM-NK"],
            "route_prefixes": ["ROUTE-A", "ROUTE-B", "ROUTE-C"],
        },
        "closed_labels": closed_labels,
        "remaining_labels": remaining_labels,
        "route_labels": route_labels,
        "coverage": {
            "frontier_open_keys": sorted(frontier_keys),
            "remaining_label_source_keys": sorted(label_keys),
            "labels_cover_frontier": labels_cover_frontier,
            "route_ids_match_frontier_contract": route_ids_match,
            "remaining_label_count": len(remaining_labels),
            "closed_label_count": len(closed_labels),
            "route_label_count": len(route_labels),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    matrix = {
        "schema": "MTTRemainingWorkStatusMatrix.v1",
        "status": "REMAINING_WORK_MATRIX_LOCKED",
        "current_active_label": "PSM-C1-01",
        "current_active_route": "ROUTE-A",
        "next_required_artifact": NEXT_ARTIFACT,
        "work_matrix": remaining_labels,
        "closed_support_matrix": closed_labels,
        "dependency_order": [
            "PSM-C1-01",
            "PSM-C1-04",
            "PSM-C1-03",
            "PSM-C1-05",
            "PSM-C1-02",
            "PSM-C1-06",
            "PSM-DYN-01",
            "PSM-S2-01",
            "PSM-QFT-01",
            "PSM-NK-01",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_map = {
        "schema": "MTTRouteLabelMap.v1",
        "status": "ROUTE_LABEL_MAP_LOCKED",
        "routes": route_labels,
        "source_contract": rel(DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier" / "three_route_closure_contract.packet.json"),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem_proved = (
        boundary["boundary_locks"]
        and labels_cover_frontier
        and route_ids_match
        and frontier["starting_point"]["source_slots_remaining"] == 0
    )

    candidate = {
        "candidate": "MTTSelectedPostSMParityWorkBreakdownLabels",
        "status": STATUS,
        "inputs": {
            "postsource_frontier": rel(DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier" / "dynamic_qasu3_c1_frontier.packet.json"),
            "three_route_contract": rel(DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier" / "three_route_closure_contract.packet.json"),
            "frozen_boundary": rel(DATA / "selected_smparityfrozenboundary_or_postsmparityfrontier" / "frozen_smparity_boundary.packet.json"),
        },
        "output_packets": {
            "canonical_work_labels": rel(LABELS),
            "remaining_work_status_matrix": rel(MATRIX),
            "route_label_map": rel(ROUTE_MAP),
        },
        "theorem": {
            "name": "CanonicalPostSMParityWorkLabelTheorem",
            "proved": theorem_proved,
            "statement": (
                "Every currently open post-SM-parity target is assigned a stable label, category, "
                "subcategory, closure condition, and route ownership. Future artifacts must cite these labels "
                "rather than reopening SM-parity or referring to ambiguous remaining blockers."
            ),
        },
        "what_closes_now": {
            "canonical_remaining_work_labels_locked": True,
            "frontier_open_targets_fully_covered": labels_cover_frontier,
            "route_labels_locked": route_ids_match,
            "current_active_label_selected": "PSM-C1-01",
        },
        "what_remains_open": {item["id"]: True for item in remaining_labels},
        "closure_decision": {
            "label_artifact_closed": theorem_proved,
            "SM_parity_reopened": False,
            "finite_source_slots_reopened": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": theorem_proved,
    }

    cert = {
        "certificate": "MTT_Selected_PostSMParity_WorkBreakdown_Labels_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "remaining_label_count": len(remaining_labels),
        "closed_label_count": len(closed_labels),
        "route_label_count": len(route_labels),
        "current_active_label": "PSM-C1-01",
        "current_active_route": "ROUTE-A",
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note_lines = [
        "# MTT Selected PostSMParity WorkBreakdown Labels v1",
        "",
        "This artifact gives stable labels to every remaining post-SM-parity part.",
        "",
        "Going forward, cite labels instead of vague blocker names.",
        "",
        "Closed/frozen labels:",
    ]
    for item in closed_labels:
        note_lines.append(f"- `{item['id']}`: {item['name']} ({item['status']})")
    note_lines.extend(["", "Remaining labels:"])
    for item in remaining_labels:
        note_lines.append(f"- `{item['id']}` / `{item['subcategory']}`: {item['name']} ({item['status']})")
    note_lines.extend(
        [
            "",
            "Route labels:",
            "- `ROUTE-A`: same-source dynamic `Phi_fin^C1` source rule",
            "- `ROUTE-B`: honest selected Galerkin C1 execution",
            "- `ROUTE-C`: same-branch superset bridge",
            "",
            "Current active work:",
            "",
            "- `PSM-C1-01` through `ROUTE-A`",
            "",
            f"Next artifact: `{NEXT_ARTIFACT}`.",
        ]
    )
    note = "\n".join(note_lines) + "\n"

    for path, payload in [
        (LABELS, labels),
        (MATRIX, matrix),
        (ROUTE_MAP, route_map),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
