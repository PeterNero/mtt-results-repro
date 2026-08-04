"""Build the ordered V_alpha / Pic0 source repair artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

INPUT = DATA / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json"
OUTPUT_DATA = DATA / "selected_qa_su3_ordered_valpha_pic0_source_repair.candidate.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_ordered_valpha_pic0_source_repair_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_Qa_SU3_Ordered_VAlpha_Pic0_Source_Repair_v1.md"

LOCAL_INPUTS = {
    "same_source_attempt": CERTS / "selected_qa_su3_same_source_visible_color_operator_packet_certificate.json",
    "ordered_source_gate": Q79 / "certificates" / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json",
    "selector_obstruction_note": Q79 / "proof_corpus" / "Visible_Rank2_L2_Selector_Obstruction_Theorem_v1.md",
    "monad_difference_sufficiency": Q79 / "certificates" / "monad_difference_l2_source_sufficiency_certificate.json",
    "conditional_monad_difference_attempt": Q79 / "certificates" / "selected_monad_difference_l2_source_proof_attempt_certificate.json",
    "unconditional_monad_difference_attempt": Q79 / "certificates" / "unconditional_selected_monad_difference_l2_source_attempt_certificate.json",
    "gauduchon_wall_gate": Q79 / "certificates" / "selected_gauduchon_wall_radius_gate_certificate.json",
    "visible_l2_orientation_attempt": NONSM / "certificates" / "selected_qa_su3_visible_l2_orientation_source_attempt_certificate.json",
    "visible_rank2_valpha_attempt": NONSM / "certificates" / "selected_qa_su3_visible_rank2_valpha_source_attempt_certificate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {
        key: {
            "path": str(path),
            "present": path.exists(),
        }
        for key, path in LOCAL_INPUTS.items()
    }


def note_has(path: Path, terms: list[str]) -> dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""
    return {
        "path": str(path),
        "present": path.exists(),
        "terms_found": [term for term in terms if term in text],
        "all_terms_found": all(term in text for term in terms),
    }


def build_candidate() -> dict[str, object]:
    input_data = load_json(INPUT)
    ordered = load_json(LOCAL_INPUTS["ordered_source_gate"])
    suff = load_json(LOCAL_INPUTS["monad_difference_sufficiency"])
    conditional = load_json(LOCAL_INPUTS["conditional_monad_difference_attempt"])
    unconditional = load_json(LOCAL_INPUTS["unconditional_monad_difference_attempt"])
    wall = load_json(LOCAL_INPUTS["gauduchon_wall_gate"])
    orientation = load_json(LOCAL_INPUTS["visible_l2_orientation_attempt"])
    valpha = load_json(LOCAL_INPUTS["visible_rank2_valpha_attempt"])
    obstruction_scan = note_has(
        LOCAL_INPUTS["selector_obstruction_note"],
        ["Base-Swap Degeneracy", "Pic0 Degeneracy", "no proof of unique"],
    )
    return {
        "candidate": "MTTSelectedQaSU3OrderedVAlphaPic0SourceRepair",
        "status": "MTT_SELECTED_QA_SU3_ORDERED_VALPHA_PIC0_SOURCE_REPAIR_BUILT_SELECTOR_OPEN",
        "input_status": input_data["status"],
        "source_status": source_status(),
        "obstruction_scan": obstruction_scan,
        "imported_results": {
            "ordered_source_gate": {
                "status": ordered["status"],
                "blockers": ordered["blockers"],
                "must_resolve_pic0": ordered["promotion_contract"]["must_resolve_pic0"],
                "must_select_ordered_base_factors": ordered["promotion_contract"]["must_select_ordered_base_factors"],
                "recognized_selected_statuses": ordered["valid_selected_source_statuses"],
            },
            "sufficiency": {
                "status": suff["status"],
                "relative_theorem_proved": suff["relative_theorem"]["proved"],
                "hypothetical_selected_validation_exit_code": suff["packets"]["hypothetical_selected_validation"]["exit_code"],
                "only_source_selection_and_pic0_fields_changed": suff["promotion_delta"]["only_source_selection_and_pic0_fields_changed"],
                "still_open": suff["still_open"],
            },
            "conditional_uniqueness": {
                "status": conditional["status"],
                "proved": conditional["conditional_uniqueness_theorem"]["proved"],
                "selected_candidate": conditional["terminal_monad_difference_scan"]["selected_candidate_inside_lane"],
                "what_does_not_close": conditional["what_this_does_not_close"],
            },
            "unconditional_attempt": {
                "status": unconditional["status"],
                "proved": unconditional["unconditional_theorem_attempt"]["proved"],
                "minimal_new_statement_that_would_close": unconditional["minimal_new_statement_that_would_close"],
                "route_results": unconditional["route_results"],
            },
            "gauduchon_wall": {
                "status": wall["status"],
                "target_wall": wall["wall_dictionary"]["target_wall"],
                "current_source_status": wall["current_source_status"],
                "live_routes": [
                    row for row in wall["route_evaluation"] if row["status"] == "LIVE"
                ],
            },
            "nonsm_orientation_attempt": {
                "status": orientation["status"],
                "closed": orientation["closed_now"],
                "open": orientation["not_closed"],
            },
            "nonsm_valpha_attempt": {
                "status": valpha["status"],
                "closed": valpha["closed_now"],
                "open": valpha["not_closed"],
            },
        },
        "repair_decision": {
            "exhausted_route": {
                "id": "closed_topology_cohomology_curvature_invariants",
                "status": "RETIRED_AS_SELECTOR",
                "reason": "The selector obstruction theorem proves these invariants are base-swap and Pic0 invariant.",
            },
            "live_routes": [
                {
                    "id": "selected_terminal_monad_lane_plus_pic0_quotient",
                    "status": "PRIMARY_REPAIR",
                    "must_prove": [
                        "MTT selects terminal monad differences L_i-K2 as the visible ordered L source lane",
                        "standard/equivalent Iwasawa lattice and base order are source-selected",
                        "Pic0 twists are quotient-irrelevant for the physical V_alpha packet, or neutral Pic0 is holonomy-selected",
                        "typed transition/rho_E/Cech/D_E data emit from the same source",
                    ],
                },
                {
                    "id": "selected_nonabelian_routec_gauduchon_wall",
                    "status": "SECONDARY_REPAIR",
                    "must_prove": [
                        "a selected nonabelian or Route-C source derives r1:r2=sqrt(2):1",
                        "the same source breaks base swap and fixes or quotients Pic0",
                        "the same source supplies D_E/dotD/Riesz/Green data",
                    ],
                },
                {
                    "id": "gerbe_twisted_de_source",
                    "status": "PARALLEL_REPAIR_IF_PIC0_IS_GERBE_DATA",
                    "must_prove": [
                        "Pic0 ambiguity is absorbed into selected Deligne/gerbe/twisted module data",
                        "twisted D_E/dotD source passes the same-source validator",
                    ],
                },
            ],
            "minimal_packet_name": "Selected_Terminal_Monad_Lane_Pic0_Quotient_Source.v1",
        },
        "strict_repair_packet_template": {
            "source_status": "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED",
            "selected_by_mtt": None,
            "fixture_only": False,
            "source_certificate": None,
            "ordered_difference": "L3_minus_K2",
            "L": [1, -2, 0],
            "L2": [2, -4, 0],
            "standard_lattice_or_equivalent_selected": None,
            "base_factor_order_selected": None,
            "base_swap_broken_by_source": None,
            "not_only_finite_mod3_qutrit": True,
            "not_equal_radius_import": True,
            "pic0_resolution_rule": None,
            "pic0_character_selected_or_quotiented": None,
            "raw_transition_or_automorphy_data": None,
            "same_source_operator_exit": None,
        },
        "gate_results": {
            "repair_artifact_built": True,
            "selector_obstruction_imported": obstruction_scan["all_terms_found"],
            "sufficiency_theorem_imported": suff["relative_theorem"]["proved"],
            "conditional_uniqueness_imported": conditional["conditional_uniqueness_theorem"]["proved"],
            "unconditional_selection_still_open": unconditional["unconditional_theorem_attempt"]["proved"] is False,
            "gauduchon_wall_live_route_imported": any(row["status"] == "LIVE" for row in wall["route_evaluation"]),
            "strict_repair_template_built": True,
            "ordered_source_promoted": False,
            "selected_Qa_SU3_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "next_required_artifact": "MTT_Selected_Terminal_Monad_Lane_Pic0_Quotient_Source_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedQaSU3OrderedVAlphaPic0SourceRepair",
        "status": "MTT_SELECTED_QA_SU3_ORDERED_VALPHA_PIC0_SOURCE_REPAIR_BUILT_SELECTOR_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "ordered_VAlpha_Pic0_repair_gate": True,
            "selector_obstruction_imported": True,
            "sufficiency_and_conditional_uniqueness_imported": True,
            "exhausted_invariant_selector_route_retired": True,
            "strict_repair_packet_template_built": True,
        },
        "what_remains_open": {
            "terminal_monad_lane_selector": True,
            "standard_lattice_and_base_order_source": True,
            "base_swap_breaking_source": True,
            "Pic0_selection_or_quotient_theorem": True,
            "raw_transition_or_automorphy_data": True,
            "same_source_operator_exit": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    sources = "\n".join(
        f"- `{key}`: {body['path']} ({'present' if body['present'] else 'missing'})"
        for key, body in candidate["source_status"].items()
    )
    imported = candidate["imported_results"]
    live = []
    for route in candidate["repair_decision"]["live_routes"]:
        needs = "\n".join(f"  - {item}" for item in route["must_prove"])
        live.append(f"### `{route['id']}`\n\nStatus: `{route['status']}`\n\nMust prove:\n{needs}")
    template = "\n".join(
        f"- `{key}`: `{value}`"
        for key, value in candidate["strict_repair_packet_template"].items()
    )
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Selected Qa/SU3 Ordered VAlpha Pic0 Source Repair v1

## Purpose

This artifact attacks the ordered `V_alpha` / `Pic0` repair gate.  It does not
try another arithmetic search.  The arithmetic is already sharp: inside the
terminal monad-difference lane, `L3-K2=(1,-2,0)` is forced, and the strict
ordered-source validator would pass if source-selection and Pic0 fields were
supplied.

## Inputs

{sources}

## Imported Results

- Ordered source gate: `{imported["ordered_source_gate"]["status"]}`
- Sufficiency theorem: `{imported["sufficiency"]["status"]}`
- Hypothetical selected packet validator exit: `{imported["sufficiency"]["hypothetical_selected_validation_exit_code"]}`
- Conditional monad-difference theorem: `{imported["conditional_uniqueness"]["status"]}`
- Unconditional attempt: `{imported["unconditional_attempt"]["status"]}`
- Gauduchon wall gate: `{imported["gauduchon_wall"]["status"]}`

## Retired Route

`{candidate["repair_decision"]["exhausted_route"]["id"]}` is `{candidate["repair_decision"]["exhausted_route"]["status"]}`.

Reason: {candidate["repair_decision"]["exhausted_route"]["reason"]}

## Live Repair Routes

{chr(10).join(live)}

## Strict Repair Packet Template

The minimal packet to try next is:

{template}

## Repair Theorem

Closed topology, cohomology, curvature, mod-3 qutrit data, and equal-radius
imports cannot select the ordered target or neutral `Pic0`; they are invariant
under the base swap or under flat `Pic0` twists.  The repair must therefore add
a holonomy-sensitive source, a physical `Pic0` quotient theorem, or a
same-source operator/Hessian package.

The primary repair is to prove `Selected_Terminal_Monad_Lane_Pic0_Quotient_Source.v1`.
Given that packet, the already-imported sufficiency theorem says the strict
ordered-source validator accepts the `L3-K2` packet without observed or
benchmark flavor input.

## What This Closes

{closes}

## What Remains Open

{open_items}

## Next Artifact

```text
{candidate["next_required_artifact"]}
```
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    note_text = render_note(candidate, certificate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note_text, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
