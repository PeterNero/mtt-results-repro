"""Construct the three-lane attempt for the selected U1/Y source solve."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
CONSTANTS = ROOT.parent / "mtt-nonsm-constants-no-knob"

INPUTS = {
    "closure_ladder": DATA / "selected_u1y_full_closure_execution_attempt.candidate.json",
    "gauduchon_gate": DATA / "selected_u1y_gauduchon_chamber_or_selected_residual_source.candidate.json",
    "source_augmentation_fill": DATA / "source_augmentation_iwasawa_monad_maps_fill_attempt.candidate.json",
    "gerbe_twisted_fill": DATA / "gerbe_twisted_local_system_response_fill_attempt.candidate.json",
    "routec_source_template": CONSTANTS / "certificates" / "selected_qa_su3_routec_source_solve.template.json",
}

OUTPUT_DATA = DATA / "selected_u1y_visible_bundle_or_routec_source_solve_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_visible_bundle_or_routec_source_solve_attempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_Visible_Bundle_or_RouteC_Source_Solve_Attempt_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def lane_status(filled: list[str], required: list[str], invalid: bool = False) -> str:
    if invalid:
        return "INVALID_FOR_SELECTED_SOURCE_SOLVE"
    if set(filled) == set(required):
        return "CLOSED_SELECTED_SOURCE_SOLVE"
    if filled:
        return "PARTIAL_SELECTED_SOURCE_SOLVE"
    return "BLOCKED_SELECTED_SOURCE_SOLVE"


def build_lane(
    *,
    name: str,
    role: str,
    route: str,
    filled: dict[str, Any],
    blockers: dict[str, Any],
    evidence: dict[str, Any],
    required: list[str],
    invalid: bool = False,
) -> dict[str, Any]:
    filled_keys = [key for key in required if key in filled and filled[key] is not None]
    missing_keys = [key for key in required if key not in filled or filled[key] is None]
    return {
        "name": name,
        "role": role,
        "route": route,
        "status": lane_status(filled_keys, required, invalid),
        "closed": not invalid and not missing_keys,
        "invalid": invalid,
        "filled_fields": filled,
        "filled_count": len(filled_keys),
        "missing_fields": missing_keys,
        "missing_count": len(missing_keys),
        "blockers": blockers,
        "evidence": evidence,
        "target_fitting_used": False,
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    closure = load(INPUTS["closure_ladder"])
    gauduchon = load(INPUTS["gauduchon_gate"])
    source_aug = load(INPUTS["source_augmentation_fill"])
    gerbe = load(INPUTS["gerbe_twisted_fill"])
    template = load(INPUTS["routec_source_template"])

    required = list(template["must_supply"].keys())

    lane_a = build_lane(
        name="LaneA_TypedMonad_SectionRing",
        role="Gold-standard ordinary visible bundle/sheaf construction.",
        route="typed Cech/monad transition data plus Iwasawa section ring",
        required=required,
        filled={
            "mtt_selection_certificate_for_q79_F_m1_branch": {
                "source_certificate": source_aug["partial_packet"]["selected_branch"]["source_certificate"],
                "target_residual_used": source_aug["partial_packet"]["selected_branch"]["target_residual_used"],
                "status": source_aug["gate_results"]["source_certificate"],
            },
            "selected_visible_sm_bundle_or_sheaf_model": {
                "monad_topology": source_aug["fillable_from_source"]["monad_topology"],
                "quotient": source_aug["partial_packet"]["geometry"]["quotient"],
                "universal_cover": source_aug["partial_packet"]["geometry"]["universal_cover"],
                "status": "PARTIAL_MONAD_TOPOLOGY_ONLY",
            },
        },
        blockers={
            "automorphy_cocycle": source_aug["gate_results"]["automorphy_cocycle"],
            "section_ring": source_aug["gate_results"]["section_ring"],
            "g_f_zero": source_aug["gate_results"]["g_f_zero"],
            "operator_exit": source_aug["gate_results"]["operator_exit"],
            "hard_blockers": source_aug["hard_blockers"],
        },
        evidence={
            "input_status": source_aug["input_status"],
            "why_not_enough": source_aug["local_frame_mismatch"]["why_not_enough"],
        },
    )

    lane_b = build_lane(
        name="LaneB_RouteC_FiniteCochain",
        role="Most computable next route: finite selected source first, smooth promotion second.",
        route="finite q79/F cochain source with selected projector and operator exits",
        required=required,
        filled={
            "mtt_selection_certificate_for_q79_F_m1_branch": {
                "closure_ladder_first_blocker": closure["first_blocker"]["name"],
                "formal_lift_rejected": gauduchon["decision"]["formal_lift_rejected"],
                "target_fitting_used": False,
            },
            "route_c_residual_packet_with_selected_source_verified": {
                "honest_residual_zero_shape_available": gauduchon["residual_values"]["honest_residual_zero"],
                "honest_selected_source_verified": gauduchon["residual_values"]["honest_selected_source_verified"],
                "accepted_as_proof": False,
                "status": "SHAPE_AVAILABLE_SOURCE_FLAG_MISSING",
            },
        },
        blockers={
            "finite_selected_source": "missing selected finite cochain complex with source-derived selected_source_verified=true",
            "rhoE_transition_data": "missing finite rho_E cocycle table from same source",
            "DE_action": "missing induced D_E action matrices from same source",
            "riesz_green_dotd": "missing same-source projector, gap, reduced Green, and dotD responses",
            "primitive_overlaps": "missing primitive C1/Yukawa overlap contractions",
        },
        evidence={
            "why_lane_b_first": [
                "does not require global section-ring repair before testing finite source data",
                "matches current validator architecture",
                "can later be promoted to smooth/sheaf data by a separate theorem",
            ],
            "existing_zero_shape_is_not_enough": gauduchon["residual_values"]["why_formal_lift_rejected"],
        },
    )

    lane_c = build_lane(
        name="LaneC_ProjectiveGerbe_LocalSystem",
        role="Superset route if ordinary line-bundle data is not selected by MTT.",
        route="projective gerbe/twisted module or holonomy-sensitive local system",
        required=required,
        filled={
            "mtt_selection_certificate_for_q79_F_m1_branch": {
                "source_identity": gerbe["partial_packet"]["source_certificate"]["source_identity"],
                "target_fitting_used": False,
            },
            "coherent_projector_retention": {
                "projector_retention_policy": gerbe["partial_packet"]["admissibility"]["projector_retention_policy"],
                "status": "OPEN_POLICY_REQUIRED",
            },
            "finite_rhoE_transition_data_not_pure_gauge_smoke": {
                "rho_E": gerbe["partial_packet"]["finite_response"]["rho_E"],
                "local_system_representation": gerbe["partial_packet"]["gerbe_or_local_system"][
                    "rho_E_local_system_representation"
                ],
                "status": "OPEN_PROJECTIVE_RESPONSE_REQUIRED",
            },
        },
        blockers={
            "same_branch_representative": gerbe["fill_result"]["same_branch_representative_filled"],
            "module_action": gerbe["fill_result"]["same_branch_rhoE_or_local_system_filled"],
            "section_constants": gerbe["fill_result"]["section_bases_and_constants_filled"],
            "finite_response": gerbe["fill_result"]["finite_response_filled"],
            "listed_blockers": gerbe["blockers"],
        },
        evidence={
            "twist_cancellation_table_filled": gerbe["fill_result"]["twist_cancellation_table_filled"],
            "primitive_complex_central_support_filled": gerbe["fill_result"]["primitive_complex_central_support_filled"],
            "global_gerbe_curvature_available": gerbe["fill_result"]["global_gerbe_curvature_available"],
        },
    )

    lanes = [lane_a, lane_b, lane_c]
    lane_order = [
        "LaneB_RouteC_FiniteCochain",
        "LaneC_ProjectiveGerbe_LocalSystem",
        "LaneA_TypedMonad_SectionRing",
    ]
    best_lane = "LaneB_RouteC_FiniteCochain"

    shared_schema = {
        key: {
            "required": True,
            "filled_by_any_lane": any(key in lane["filled_fields"] and lane["filled_fields"][key] is not None for lane in lanes),
            "closed_by_any_lane": any(lane["closed"] and key in lane["filled_fields"] for lane in lanes),
        }
        for key in required
    }

    candidate = {
        "candidate": "SelectedU1YVisibleBundleOrRouteCSourceSolveAttempt",
        "schema": template["schema"],
        "status": "VISIBLE_BUNDLE_OR_ROUTEC_SOURCE_SOLVE_ATTEMPT_EXECUTED_FINITE_COHCHAIN_ROUTE_PRIORITIZED",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "required_fields": required,
        "accepted_source_routes": template["accepted_source_routes"],
        "forbidden_shortcuts": template["forbidden_shortcuts"],
        "lanes": lanes,
        "shared_schema_coverage": shared_schema,
        "decision": {
            "all_three_lanes_executed": True,
            "source_solve_closed": False,
            "full_sm_or_lambda12_closed": False,
            "best_next_lane": best_lane,
            "lane_priority_order": lane_order,
            "why_best_lane": [
                "it asks first for the finite selected source object the validators can consume",
                "it avoids treating typed monad labels as global sections",
                "it avoids treating gerbe existence or twist cancellation as a local-system response",
                "it cleanly separates finite-source closure from later smooth promotion",
            ],
            "next_artifact_to_build": "Selected_U1Y_RouteC_Finite_Cochain_Source_Construct_v1",
        },
        "next_artifact_contract": {
            "name": "Selected_U1Y_RouteC_Finite_Cochain_Source_Construct_v1",
            "must_emit": [
                "finite cochain complex C^bullet_{q79,F,m=1}",
                "selected projector Pi_sel and retention proof",
                "rho_E transition/cocycle table with non-pure-gauge check",
                "D_E action matrices induced from the same cochain source",
                "Riesz projector, spectral gap, and reduced Green operator",
                "dotD_alpha1 and horizontal response vectors",
                "Route-C residual table with source-derived selected_source_verified=true",
                "primitive C1/Yukawa overlap contraction table or explicit no-go",
            ],
            "validators_to_run_after_emit": closure["first_blocker"]["then_run"],
            "forbidden_inputs": [
                "observed masses, mixings, CP signs, or electroweak values",
                "benchmark flavor matrices",
                "formal-lift selected flags",
                "route-c smoke residuals without selected source verification",
            ],
        },
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedU1YVisibleBundleOrRouteCSourceSolveAttempt",
        "status": candidate["status"],
        "source_solve_closed": candidate["decision"]["source_solve_closed"],
        "best_next_lane": best_lane,
        "next_artifact_to_build": candidate["decision"]["next_artifact_to_build"],
        "all_three_lanes_executed": True,
        "lane_statuses": {lane["name"]: lane["status"] for lane in lanes},
        "lane_missing_counts": {lane["name"]: lane["missing_count"] for lane in lanes},
        "full_sm_or_lambda12_closed": False,
        "target_fitting_used": False,
    }

    note = render_note(candidate, cert)
    return candidate, cert, note


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lanes = candidate["lanes"]
    lines = [
        "# Selected U1Y Visible Bundle or Route-C Source Solve Attempt v1",
        "",
        "## Result",
        "",
        "```text",
        f"source_solve_closed = {str(candidate['decision']['source_solve_closed']).lower()}",
        f"full_sm_or_lambda12_closed = {str(candidate['decision']['full_sm_or_lambda12_closed']).lower()}",
        f"all_three_lanes_executed = {str(candidate['decision']['all_three_lanes_executed']).lower()}",
        f"best_next_lane = {candidate['decision']['best_next_lane']}",
        f"next_artifact_to_build = {candidate['decision']['next_artifact_to_build']}",
        "```",
        "",
        "The selected U1/Y source solve has now been attacked through three",
        "separate construction lanes. None closes the source object yet. The",
        "finite Route-C cochain lane is the correct next executable path because",
        "it can emit the exact validator-ready rho_E, D_E, Riesz/Green, dotD,",
        "and primitive-overlap tables before any smooth-promotion theorem is used.",
        "",
        "## Lane Outcomes",
        "",
        "| Lane | Status | Filled | Missing | Role |",
        "| --- | --- | ---: | ---: | --- |",
    ]
    for lane in lanes:
        lines.append(
            f"| `{lane['name']}` | `{lane['status']}` | {lane['filled_count']} | {lane['missing_count']} | {lane['role']} |"
        )
    lines.extend(
        [
            "",
            "## Decision",
            "",
            f"- best_next_lane = `{candidate['decision']['best_next_lane']}`",
            f"- next_artifact_to_build = `{candidate['decision']['next_artifact_to_build']}`",
            "- source_solve_closed = `false`",
            "- lambda_12_closed = `false`",
            "- target_fitting_used = `false`",
            "",
            "## Why Lane B First",
            "",
        ]
    )
    for item in candidate["decision"]["why_best_lane"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Next Artifact Contract",
            "",
            "The next artifact must emit:",
            "",
        ]
    )
    for item in candidate["next_artifact_contract"]["must_emit"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "After emission, run:",
            "",
        ]
    )
    for item in candidate["next_artifact_contract"]["validators_to_run_after_emit"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
        ]
    )
    for item in candidate["next_artifact_contract"]["forbidden_inputs"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Certificate",
            "",
            "```json",
            json.dumps(cert, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    candidate, cert, note = build()
    DATA.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    PROOF.mkdir(parents=True, exist_ok=True)
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
