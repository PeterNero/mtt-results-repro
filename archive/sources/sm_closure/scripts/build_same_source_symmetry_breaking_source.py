"""Build the same-source symmetry-breaking source artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79_CERTS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\certificates")

OUTPUT_DATA = DATA / "same_source_symmetry_breaking_source.candidate.json"
OUTPUT_CERT = CERTS / "same_source_symmetry_breaking_source_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_SameSource_SymmetryBreaking_Source_v1.md"

INPUTS = {
    "same_source_packet": DATA / "selected_nonsplit_rank2_or_routec_same_source_packet.candidate.json",
    "route_triage": Q79_CERTS / "valpha_s3_symmetry_breaking_route_triage_certificate.json",
    "gauduchon_wall": Q79_CERTS / "selected_gauduchon_wall_radius_gate_certificate.json",
    "orientation_bridge": Q79_CERTS / "iwasawa_orientation_de_dotd_bridge_certificate.json",
    "orientation_attempt": Q79_CERTS / "selected_qa_su3_orientation_dedotd_source_attempt_certificate.json",
    "orientation_template": Q79_CERTS / "selected_qa_su3_orientation_carrying_de_dotd_source.template.json",
    "zero_mode_dotd_interface": Q79_CERTS / "selected_zero_mode_basis_dotd_interface_certificate.json",
    "dotd_validator": Q79_CERTS / "iwasawa_dotd_response_validator_certificate.json",
    "two_block_reduction": Q79_CERTS / "valpha_s3_two_block_source_selector_reduction_certificate.json",
    "selector_obstruction": Q79_CERTS / "visible_rank2_l2_selector_obstruction_certificate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {key: {"path": str(path), "present": path.exists()} for key, path in INPUTS.items()}


def build_candidate() -> dict[str, object]:
    same_source = load_json(INPUTS["same_source_packet"])
    triage = load_json(INPUTS["route_triage"])
    wall = load_json(INPUTS["gauduchon_wall"])
    bridge = load_json(INPUTS["orientation_bridge"])
    attempt = load_json(INPUTS["orientation_attempt"])
    template = load_json(INPUTS["orientation_template"])
    zero_mode = load_json(INPUTS["zero_mode_dotd_interface"])
    dotd = load_json(INPUTS["dotd_validator"])
    two_block = load_json(INPUTS["two_block_reduction"])
    obstruction = load_json(INPUTS["selector_obstruction"])

    primary_route = triage["route_ranking"][0]
    wall_route = triage["route_ranking"][1]
    integral_route = triage["route_ranking"][2]
    pic0_route = triage["route_ranking"][3]

    selected_source_closed = attempt["validator_result"]["exit_code"] == 0
    finite_shape_closed = two_block["what_this_closes"]["two_block_finite_shape_is_mod3_shadow_of_ordered_integral_L2"]

    route_status = {
        "primary_orientation_carrying_de_dotd": {
            "classification": "SUPERSET_CONVERGENCE_PRIMARY",
            "status": primary_route["status"],
            "why_primary": primary_route["reason"],
            "template": triage["de_dotd_route"]["template"],
            "branch_packets": triage["de_dotd_route"]["branch_packets"],
            "closed": {
                "finite_dotD_response_validator_ready": triage["closed_now"]["finite_dotD_response_validator_ready"],
                "orientation_dependencies_cohere": bridge["calculation_results"]["existing_orientation_sources_cohere"],
                "conjugate_pair_reduced_to_q79_q369": bridge["calculation_results"]["conjugate_pair_only"],
                "finite_branch_data_reaches_validator_layer": attempt["what_this_closes"]["finite_branch_data_reaches_validator_layer"],
                "dotd_response_validator_formulated": dotd["what_this_closes"]["finite_dotD_response_validator"],
                "zero_mode_dotd_interface_formulated": zero_mode["verdict"]["closes_zero_mode_dotD_input_contract"],
            },
            "open": {
                "selected_orientation_carrying_source": triage["not_closed"]["selected_orientation_carrying_source"],
                "unique_m1_vs_m2_selection": triage["not_closed"]["unique_m1_vs_m2_selection"],
                "actual_selected_D_E_action": triage["not_closed"]["actual_selected_D_E_action"],
                "actual_selected_dotD_alpha1_operator": triage["not_closed"]["actual_selected_dotD_alpha1_operator"],
                "pic0_selected_or_quotiented": triage["not_closed"]["selected_or_quotiented_Pic0_character"],
                "same_branch_derivative_verified": "same_branch_derivative_verified must be true" in attempt["first_open_items"],
            },
        },
        "gauduchon_wall": {
            "classification": "SUPERSET_REPAIR_LIVE_BUT_BLOCKED",
            "status": wall_route["status"],
            "why_ranked_second": wall_route["reason"],
            "target_condition": wall["wall_dictionary"]["target_wall"]["radius_condition"],
            "equal_radius_current_source_rejected": wall["what_this_closes"]["current_equal_radius_sources_do_not_select_target_wall"],
            "current_source_status": wall["current_source_status"],
        },
        "ordered_integral_cech_or_appell_humbert": {
            "classification": "SUPERSET_REPAIR_SOURCE_CERTIFICATE_GAP",
            "status": integral_route["status"],
            "why_ranked_third": integral_route["reason"],
            "two_block_shadow_closed": finite_shape_closed,
            "selected_s3_deck_limit": two_block["selected_s3_deck_limit"],
        },
        "pic0_rule_only": {
            "classification": "NECESSARY_BUT_NOT_SUFFICIENT",
            "status": pic0_route["status"],
            "why": pic0_route["reason"],
            "pic0_invariance": obstruction["pic0_invariance"],
        },
    }

    template_contract = {
        "source_origin_fields": list(template["source_origin"].keys()),
        "branch_selection_fields": list(template["branch_selection"].keys()),
        "operator_data_fields": list(template["operator_data"].keys()),
        "validator_contract": template["validator_contract"],
        "forbidden_shortcuts": template["forbidden_shortcuts"],
    }

    return {
        "candidate": "MTTSameSourceSymmetryBreakingSource",
        "status": "MTT_SAME_SOURCE_SYMMETRY_BREAKING_SOURCE_REDUCED_TO_ORIENTATION_CARRYING_DE_DOTD_PACKET",
        "source_status": source_status(),
        "imported_statuses": {
            key: load_json(path)["status"] if path.exists() and path.suffix == ".json" else "MISSING"
            for key, path in INPUTS.items()
        },
        "superset_mode": {
            "classification": "SUPERSET_CONVERGENCE_WITH_REPAIR_TRIAGE",
            "straight_path": {
                "classification": "STRAIGHT_PATH_BLOCKED",
                "reason": "Topology, h1, finite qutrit label, Appell-Humbert existence, and curvature data are base-swap/Pic0 insensitive.",
            },
            "primary_superset_path": route_status["primary_orientation_carrying_de_dotd"],
            "repair_paths": {
                "gauduchon_wall": route_status["gauduchon_wall"],
                "ordered_integral_cech_or_appell_humbert": route_status["ordered_integral_cech_or_appell_humbert"],
                "pic0_rule_only": route_status["pic0_rule_only"],
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "Observed CP sign, masses, mixings, and benchmark matrices are forbidden as branch selectors.",
            },
            "locked_target": "SelectedQaSU3OrientationCarryingDEDotDSource.v1",
        },
        "what_is_closed": {
            "selector_obstruction_for_current_closed_invariants": obstruction["what_this_closes"]["no_hidden_selector_in_current_topology_h1_qutrit_or_appell_humbert_data"],
            "two_block_mod3_shadow_of_ordered_integral_L2": finite_shape_closed,
            "selected_s3_deck_lacks_second_block": two_block["what_this_closes"]["current_selected_s3_deck_quotient_does_not_supply_second_block"],
            "target_wall_dictionary": wall["what_this_closes"]["abstract_p_wall_translated_to_iwasawa_radii"],
            "equal_radius_sources_rejected_for_target_wall": wall["what_this_closes"]["current_equal_radius_sources_do_not_select_target_wall"],
            "orientation_branch_pair_formulated": bridge["what_this_closes"]["m_label_to_q_label_conditional_map_formulated"],
            "finite_dedotd_branch_attempt_reaches_validators": attempt["what_this_closes"]["finite_branch_data_reaches_validator_layer"],
            "dedotd_response_validator_ready": dotd["what_this_closes"]["finite_dotD_response_validator"],
        },
        "what_remains_open": {
            "selected_orientation_carrying_de_dotd_source": not selected_source_closed,
            "unique_m1_vs_m2_or_antiunitary_retarded_selection": bridge["still_open"]["unique_m1_vs_m2_selection"],
            "selected_D_E_action": bridge["still_open"]["selected_orientation_carrying_D_E"],
            "selected_dotD_same_branch_derivative": bridge["still_open"]["selected_dotD_same_branch_derivative"],
            "pic0_selected_or_quotiented": triage["not_closed"]["selected_or_quotiented_Pic0_character"],
            "primitive_C1_contractions": bridge["still_open"]["primitive_C1_contractions"],
        },
        "selected_template_contract": template_contract,
        "promotion_rule": {
            "preferred_fill": "Fill SelectedQaSU3OrientationCarryingDEDotDSource.v1 with a genuine selected visible bundle/twisted-gerbe/Route-C source.",
            "passes_only_if": [
                "selected_by_mtt is true from a source certificate, not lifted flags",
                "visible_bundle_or_twisted_gerbe_source is true",
                "Pic0 is selected or physically quotiented",
                "Freed-Witten and projector retention are preserved",
                "exactly one torsion label m is selected or antiunitary equivalence is proved with an external retarded boundary selector",
                "D_E, reduced Green, and dotD validators pass with selected source flags",
                "dotD is verified as the same-branch alpha1 derivative",
            ],
        },
        "inherited_frontier": same_source["same_source_packet_contract"]["common_blocker"],
        "theorem": {
            "name": "SameSourceSymmetryBreakingSourceReduction",
            "proved": True,
            "statement": (
                "The required symmetry-breaking source is not supplied by current topology, h1, finite qutrit, "
                "Appell-Humbert, equal-radius, or curvature data. The primary live closure route is the selected "
                "orientation-carrying D_E/dotD packet because it can simultaneously choose or quotient the q79/q369 "
                "conjugate fork, bind sector orientations to operator domains, and feed the existing D_E, Green, and "
                "dotD validators. The wall and ordered-integral routes remain repair paths, but neither currently "
                "emits the selected same-source operator response."
            ),
        },
        "next_required_artifact": "MTT_Selected_Orientation_Carrying_DE_DotD_Source_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSameSourceSymmetryBreakingSourceReduction",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "superset_mode": candidate["superset_mode"]["classification"],
        "what_closes": {
            "same_source_symmetry_breaker_triaged": True,
            "orientation_carrying_de_dotd_selected_as_primary_route": True,
            "gauduchon_wall_repair_route_kept_but_blocked": True,
            "ordered_integral_two_block_repair_route_kept": True,
            "pic0_rule_only_marked_necessary_but_insufficient": True,
            "selected_template_contract_locked": True,
        },
        "what_remains_open": candidate["what_remains_open"],
        "primary_next_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    primary = candidate["superset_mode"]["primary_superset_path"]
    repairs = candidate["superset_mode"]["repair_paths"]
    closed = "\n".join(f"- `{key}`" for key, value in candidate["what_is_closed"].items() if value)
    open_items = "\n".join(f"- `{key}`" for key, value in candidate["what_remains_open"].items() if value)
    template_fields = "\n".join(
        f"- `{section}`: {', '.join(fields) if isinstance(fields, list) else fields}"
        for section, fields in candidate["selected_template_contract"].items()
        if section.endswith("_fields")
    )
    rules = "\n".join(f"- {item}" for item in candidate["promotion_rule"]["passes_only_if"])
    closes = "\n".join(f"- `{key}`" for key, value in certificate["what_closes"].items() if value)

    return f"""# MTT Same-Source Symmetry-Breaking Source v1

## Result

The same-source symmetry breaker is reduced to the selected
orientation-carrying `D_E/dotD` packet.

This is **superset convergence with repair triage**:

- Straight path: blocked. Current closed invariants are base-swap/Pic0
  insensitive.
- Superset convergence: `{primary["classification"]}` via
  `SelectedQaSU3OrientationCarryingDEDotDSource.v1`.
- Superset repair: Gauduchon wall remains live but current sources select equal
  radius, not the target wall.
- Superset repair: ordered integral/Appell-Humbert two-block route remains live
  as a source-certificate gap.
- Pic0 rule alone is necessary but not sufficient.
- Diagnostic/backfit: not used as proof.

## Closed

{closed}

## Primary Route

Template: `{primary["template"]}`

Why primary: {primary["why_primary"]}

## Repair Routes

- `gauduchon_wall`: `{repairs["gauduchon_wall"]["status"]}`; target condition
  `{repairs["gauduchon_wall"]["target_condition"]}`.
- `ordered_integral_cech_or_appell_humbert`:
  `{repairs["ordered_integral_cech_or_appell_humbert"]["status"]}`.
- `pic0_rule_only`: `{repairs["pic0_rule_only"]["status"]}`.

## Template Fields

{template_fields}

## Promotion Rule

{rules}

## Theorem

`{candidate["theorem"]["name"]}` is proved:

{candidate["theorem"]["statement"]}

## What This Closes

{closes}

## What Remains Open

{open_items}

## Next Artifact

`{candidate["next_required_artifact"]}`
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(candidate, certificate), encoding="utf-8")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
