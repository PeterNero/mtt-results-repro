"""Build the U1/Y Route-C operator-layer Pic0 or selected-residual split gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

INPUTS = {
    "operator_source_bridge": DATA / "selected_u1y_routec_operator_source_identity_bridge_subpacket.candidate.json",
    "q79_selector_obstruction": Q79 / "certificates" / "visible_rank2_l2_selector_obstruction_certificate.json",
    "q79_source_ambiguity": Q79 / "certificates" / "visible_rank2_l2_source_ambiguity_classification_certificate.json",
    "q79_valpha_candidates": Q79 / "certificates" / "visible_valpha_chern_bianchi_source_packet_candidates_certificate.json",
    "sm_source_origin_lemma": SM / "candidate_data" / "routec_selected_source_origin_lemma.candidate.json",
    "sm_source_way_forward": SM / "candidate_data" / "routec_selected_source_origin_way_forward.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_operatorlayer_pic0_or_selected_residual_source_subpacket.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_operatorlayer_pic0_or_selected_residual_source_subpacket_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_OperatorLayerPic0_or_SelectedResidual_Source_Subpacket_v1.md"

STATUS = "U1Y_ROUTEC_OPERATORLAYER_PIC0_OR_SELECTED_RESIDUAL_SPLIT_BUILT_PRIMARY_PHIFIN"
NEXT = "Selected_U1Y_RouteC_FiniteEmissionMorphism_PhiFin_Subpacket_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    bridge = load(INPUTS["operator_source_bridge"])
    selector = load(INPUTS["q79_selector_obstruction"])
    ambiguity = load(INPUTS["q79_source_ambiguity"])
    valpha = load(INPUTS["q79_valpha_candidates"])
    origin = load(INPUTS["sm_source_origin_lemma"])
    way = load(INPUTS["sm_source_way_forward"])

    pic0_lane = {
        "lane": "operator_layer_pic0_selection_or_quotient",
        "status": "NECESSARY_BUT_NOT_SUFFICIENT_CURRENT_SOURCE_NOGO",
        "can_close_bridge_alone": False,
        "support": {
            "pic0_invariance_proved": selector["pic0_invariance"],
            "flat_pic0_preserves_c1": ambiguity["selection_tests"]["flat_Pic0_characters_preserve_c1"],
            "hodge_dimensions_flat_twist_invariant": ambiguity["selection_tests"][
                "nonzero_elliptic_degrees_make_hodge_dimensions_flat_twist_invariant"
            ],
            "no_hidden_selector_in_current_data": selector["what_this_closes"][
                "no_hidden_selector_in_current_topology_h1_qutrit_or_appell_humbert_data"
            ],
        },
        "blockers": [
            "neutral Pic0 is not selected by current curvature/topology data",
            "Pic0 quotient alone does not construct selected HYM/Route-C residual",
            "Pic0 quotient alone does not emit D_E/Riesz/Green/dotD",
            "Pic0 quotient alone does not prove same-source Chern-Weil/GS row",
        ],
        "accepts_if": [
            "a holonomy-sensitive same-source term selects a flat character",
            "or a physical quotient theorem proves all operator observables descend through Pic0",
            "and the quotient is tied to the selected q79/F,m=1 operator source",
        ],
    }

    residual_lane = {
        "lane": "selected_residual_hym_strominger_source",
        "status": "PRIMARY_LIVE_REDUCED_TO_FINITE_EMISSION_MORPHISM",
        "can_close_bridge_alone": False,
        "can_close_bridge_with_pic0_side_condition": True,
        "support": {
            "fixed_topological_sector_named": origin["gate_matrix"]["G1_fixed_topological_sector_named"]["passes"],
            "mtt_strominger_selection_available": origin["gate_matrix"]["G2_MTT_Strominger_selection_available"]["passes"],
            "same_source_support_converges": origin["gate_matrix"]["G3_same_source_support_converges"]["passes"],
            "rank2_non_split_primary_candidate": valpha["calculation_results"]["primary_candidate_is_rank2_non_split_extension"],
            "route_c_fallback_preserved": valpha["calculation_results"]["route_c_kept_as_parallel_fallback"],
        },
        "blockers": {
            "finite_emission_morphism": not origin["gate_matrix"]["G4_minimizer_to_finite_packet_morphism"]["passes"],
            "operator_payload": not origin["gate_matrix"]["G5_operator_payload_emitted"]["passes"],
            "prove_hym_or_route_c_residual": valpha["still_open"]["prove_HYM_or_Route_C_residual"],
            "derive_same_total_source_DE_dotD_Riesz_Green": valpha["still_open"][
                "derive_same_total_source_D_E_dotD_Riesz_Green"
            ],
            "pic0_side_condition": True,
        },
        "accepts_if": origin["finite_emission_morphism_contract"]["acceptance_tests"],
        "contract": origin["finite_emission_morphism_contract"],
    }

    route_decision = {
        "primary_next_lane": "selected_residual_hym_strominger_source",
        "primary_next_artifact": NEXT,
        "reason": [
            "Pic0-only is a necessary side condition but cannot emit the operator payload.",
            "The selected source-origin lemma already reduces the residual/Strominger route to one named missing object: Phi_fin.",
            "Phi_fin would turn selected_source_verified from a lifted flag into a theorem-derived field and feed the validators.",
        ],
        "pic0_policy": "carry Pic0 as an explicit side condition for Phi_fin, not as a standalone closure claim",
    }

    candidate = {
        "candidate": "SelectedU1YRouteCOperatorLayerPic0OrSelectedResidualSourceSubpacket",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": bridge["status"],
        "pic0_lane": pic0_lane,
        "residual_lane": residual_lane,
        "route_decision": route_decision,
        "source_split_result": {
            "pic0_closed": False,
            "selected_residual_closed": False,
            "bridge_closed": False,
            "primary_route_selected": "Phi_fin",
            "current_source_nogo": True,
            "mathematical_impossibility_claimed": False,
        },
        "what_closes_now": {
            "pic0_only_route_demoted_to_side_condition": True,
            "selected_residual_route_ranked_primary": True,
            "finite_emission_morphism_named_as_next_object": True,
            "hidden_pic0_selector_rejected": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            **bridge["what_remains_open"],
            "Phi_fin": True,
            "finite_truncation_error_gap": True,
            "selected_source_verified_theorem_field": True,
            "operator_payload_DE_Riesz_Green_dotD": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_pic0_closed": False,
            "claims_selected_residual_closed": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_lambda12": False,
            "claims_full_closure": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "target_fitting_used": False,
        },
        "imported_way_forward_status": way["status"],
    }

    cert = {
        "certificate": "SelectedU1YRouteCOperatorLayerPic0OrSelectedResidualSourceSubpacket",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "pic0_closed": False,
        "selected_residual_closed": False,
        "bridge_closed": False,
        "primary_next_artifact": NEXT,
        "current_source_nogo": True,
        "mathematical_impossibility_claimed": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C OperatorLayerPic0 or SelectedResidual Source Subpacket v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"pic0_closed = {str(cert['pic0_closed']).lower()}",
        f"selected_residual_closed = {str(cert['selected_residual_closed']).lower()}",
        f"bridge_closed = {str(cert['bridge_closed']).lower()}",
        f"primary_next_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The split gate is now constructed. Operator-layer Pic0 is necessary,",
        "but current curvature/topology/cohomology data cannot select the neutral",
        "flat character and Pic0 alone cannot emit the operator payload. The",
        "primary live route is therefore the selected residual/Strominger route,",
        "reduced to the finite emission morphism `Phi_fin`.",
        "",
        "## Lane Verdicts",
        "",
        "| Lane | Status | Can close bridge alone | Verdict |",
        "| --- | --- | --- | --- |",
        f"| `operator_layer_pic0_selection_or_quotient` | `{candidate['pic0_lane']['status']}` | `false` | necessary side condition, no standalone closure |",
        f"| `selected_residual_hym_strominger_source` | `{candidate['residual_lane']['status']}` | `false` | primary route with Pic0 side condition |",
        "",
        "## Why PhiFin Is Next",
        "",
    ]
    for reason in candidate["route_decision"]["reason"]:
        lines.append(f"- {reason}")
    lines.extend(
        [
            "",
            "## PhiFin Acceptance Tests",
            "",
        ]
    )
    for test in candidate["residual_lane"]["accepts_if"]:
        lines.append(f"- {test}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not claim Pic0 closure from curvature/topology alone.",
            "- Do not turn lifted residual flags into selected-source evidence.",
            "- Do not compute `lambda_12`, `A_selected`, or `b_selected` from this split gate.",
            "- Do not use observed or benchmark data.",
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
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
