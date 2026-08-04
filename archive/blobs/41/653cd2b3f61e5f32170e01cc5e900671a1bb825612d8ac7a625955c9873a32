"""Build the terminal monad lane / Pic0 quotient source audit artifact."""

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

OUTPUT_DATA = DATA / "selected_terminal_monad_lane_pic0_quotient_source.candidate.json"
OUTPUT_CERT = CERTS / "selected_terminal_monad_lane_pic0_quotient_source_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_Terminal_Monad_Lane_Pic0_Quotient_Source_v1.md"

LOCAL_INPUTS = {
    "ordered_valpha_pic0_repair": CERTS / "selected_qa_su3_ordered_valpha_pic0_source_repair_certificate.json",
    "nonsm_terminal_lane_attempt": NONSM / "certificates" / "selected_qa_su3_terminal_monad_lane_selector_attempt_certificate.json",
    "q79_conditional_monad_difference": Q79 / "certificates" / "selected_monad_difference_l2_source_proof_attempt_certificate.json",
    "q79_unconditional_monad_difference": Q79 / "certificates" / "unconditional_selected_monad_difference_l2_source_attempt_certificate.json",
    "q79_monad_sufficiency": Q79 / "certificates" / "monad_difference_l2_source_sufficiency_certificate.json",
    "q79_deck_cech_lift": Q79 / "certificates" / "time_oriented_m1_deck_cech_lift_certificate.json",
    "q79_fixed_gerbe_representative": Q79 / "certificates" / "time_oriented_fixed_gerbe_representative_certificate.json",
    "q79_flat_gerbe_promotion": Q79 / "certificates" / "time_oriented_m1_flat_gerbe_promotion_certificate.json",
    "q79_smooth_s3_lift_attempt": Q79 / "certificates" / "visible_twisted_s3_smooth_source_lift_attempt_certificate.json",
    "q79_hym_operator_attempt": Q79 / "certificates" / "selected_hym_operator_source_attempt_certificate.json",
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


def build_candidate() -> dict[str, object]:
    ordered_repair = load_json(LOCAL_INPUTS["ordered_valpha_pic0_repair"])
    terminal = load_json(LOCAL_INPUTS["nonsm_terminal_lane_attempt"])
    conditional = load_json(LOCAL_INPUTS["q79_conditional_monad_difference"])
    unconditional = load_json(LOCAL_INPUTS["q79_unconditional_monad_difference"])
    suff = load_json(LOCAL_INPUTS["q79_monad_sufficiency"])
    deck = load_json(LOCAL_INPUTS["q79_deck_cech_lift"])
    fixed_gerbe = load_json(LOCAL_INPUTS["q79_fixed_gerbe_representative"])
    flat_gerbe = load_json(LOCAL_INPUTS["q79_flat_gerbe_promotion"])
    smooth_s3 = load_json(LOCAL_INPUTS["q79_smooth_s3_lift_attempt"])
    hym = load_json(LOCAL_INPUTS["q79_hym_operator_attempt"])

    selected_candidate = conditional["terminal_monad_difference_scan"]["selected_candidate_inside_lane"]
    return {
        "candidate": "MTTSelectedTerminalMonadLanePic0QuotientSource",
        "status": "MTT_SELECTED_TERMINAL_MONAD_LANE_PIC0_QUOTIENT_SOURCE_AUDITED_PIC0_GATE_OPEN",
        "source_status": source_status(),
        "imported_results": {
            "previous_frontier": {
                "status": ordered_repair["status"],
                "next_required_artifact": ordered_repair["next_required_artifact"],
                "closure_claimed": ordered_repair["closure_claimed"],
            },
            "terminal_lane_attempt": {
                "status": terminal["status"],
                "conditional_uniqueness_closed": terminal["gate_result"]["conditional_uniqueness_closed"],
                "terminal_monad_lane_selector_closed": terminal["gate_result"]["terminal_monad_lane_selector_closed"],
                "minimal_next_object": terminal["minimal_next_object"]["name"],
                "not_closed": terminal["not_closed"],
            },
            "conditional_monad_difference": {
                "status": conditional["status"],
                "proved": conditional["conditional_uniqueness_theorem"]["proved"],
                "selected_candidate_inside_lane": selected_candidate,
                "does_not_close": conditional["what_this_does_not_close"],
            },
            "unconditional_monad_difference": {
                "status": unconditional["status"],
                "proved": unconditional["unconditional_theorem_attempt"]["proved"],
                "minimal_new_statement_that_would_close": unconditional["minimal_new_statement_that_would_close"],
            },
            "monad_sufficiency": {
                "status": suff["status"],
                "relative_theorem_proved": suff["relative_theorem"]["proved"],
                "hypothetical_selected_validation_exit_code": suff["packets"]["hypothetical_selected_validation"]["exit_code"],
            },
            "finite_deck_cech_lift": {
                "status": deck["status"],
                "what_this_closes": deck["what_this_closes"],
                "still_open": deck["still_open"],
                "deck_quotient_target": deck["deck_quotient_map"]["target"],
                "active_quotient_delta_zero": deck["calculation_results"]["active_quotient_delta_zero"],
            },
            "fixed_gerbe_representative": {
                "status": fixed_gerbe["status"],
                "q79_torsion_label_m": fixed_gerbe["branch_representatives"]["time_oriented_q79"]["torsion_label_m"],
                "q79_orientation": fixed_gerbe["branch_representatives"]["time_oriented_q79"]["orientation"],
                "selected_D_E_dotD_constructed": fixed_gerbe["calculation_results"]["selected_D_E_dotD_constructed"],
                "still_open": fixed_gerbe["still_open"],
            },
            "flat_gerbe_promotion": {
                "status": flat_gerbe["status"],
                "conditional_flat_gerbe_representative_exists": flat_gerbe["calculation_results"]["conditional_flat_gerbe_representative_exists"],
                "selected_flat_gerbe_representative_closed": flat_gerbe["calculation_results"]["selected_flat_gerbe_representative_closed"],
                "selected_D_E_dotD_constructed": flat_gerbe["calculation_results"]["selected_D_E_dotD_constructed"],
                "still_open": flat_gerbe["still_open"],
            },
            "smooth_s3_lift_attempt": {
                "status": smooth_s3["status"],
                "conditional_smooth_flat_S3_model_available": smooth_s3["calculation_results"]["conditional_smooth_flat_S3_model_available"],
                "selected_smooth_S3_source_constructed": smooth_s3["calculation_results"]["selected_smooth_S3_source_constructed"],
                "still_open": smooth_s3["still_open"],
            },
            "hym_operator_attempt": {
                "status": hym["status"],
                "selected_hym_operator_source_verified": hym["calculation_results"]["selected_hym_operator_source_verified"],
                "still_open": hym["still_open"],
            },
        },
        "terminal_lane_audit": {
            "conditional_unique_target_inside_lane": True,
            "selected_ordered_difference": "L3-K2",
            "selected_ordered_difference_L": selected_candidate["value"],
            "selected_ordered_difference_L2": selected_candidate["double_value"],
            "strict_ordered_validator_would_pass_after_source_and_pic0": True,
            "source_lane_selected_by_mtt": False,
            "standard_lattice_or_equivalent_selected": False,
            "base_factor_order_selected": False,
        },
        "pic0_route_audit": [
            {
                "id": "naive_physical_pic0_quotient",
                "status": "REJECTED_UNPROVED",
                "reason": "Flat Pic0 twists are holonomy data and can change transition/operator/spectral data unless a physical-invariance theorem is supplied.",
                "may_be_reopened_by": "A same-source theorem proving all physical V_alpha observables, D_E/dotD, Riesz/Green, and overlap data descend to the Pic0 quotient.",
            },
            {
                "id": "neutral_pic0_holonomy_selection",
                "status": "OPEN_ABSENT",
                "reason": "No corpus certificate currently selects the neutral Pic0 character by a holonomy-sensitive rule.",
                "may_be_reopened_by": "A selected Appell-Humbert/Cech/Deligne representative whose source forces the neutral flat character.",
            },
            {
                "id": "finite_gerbe_torsion_replacement",
                "status": "LIVE_PARTIAL",
                "reason": "The q79/F branch fixes m=1 and a deck-level F_3^2 cocycle; this can replace smooth Pic0 ambiguity only after selected cover, restrictions, projectors, and operator data are supplied.",
                "already_closed": [
                    "finite q79/F torsion label m=1",
                    "deck pullback cocycle with active quotient delta zero",
                    "conditional flat torsion gerbe promotion",
                ],
            },
            {
                "id": "same_source_operator_selector",
                "status": "LIVE_ABSENT",
                "reason": "A selected D_E/dotD/Riesz/Green package would decide which flat/twisted source is physical, but current HYM/operator certificates still block there.",
                "may_be_reopened_by": "Selected visible SM bundle/operator source with Route-C residual, D_E, dotD, projector retention, and Green data.",
            },
        ],
        "theorem": {
            "name": "TerminalMonadLanePic0GateTheorem",
            "proved": True,
            "statement": (
                "Current corpus data reduce the ordered Qa/SU3 source problem to a terminal-lane "
                "selector plus a Pic0/torsion-gerbe physical-source rule. They do not prove a "
                "Pic0 quotient or neutral Pic0 selection."
            ),
            "corollary": (
                "The artifact closes the audit of the proposed terminal monad lane Pic0 shortcut: "
                "the shortcut is not a theorem yet; the next legal closing object is a Pic0 "
                "invariance theorem or a selected gerbe/twisted D_E source."
            ),
        },
        "gate_results": {
            "terminal_lane_pic0_source_audited": True,
            "terminal_lane_conditional_uniqueness_imported": True,
            "L3_K2_inside_lane_forced": True,
            "source_lane_selector_absent": True,
            "standard_lattice_base_order_absent": True,
            "naive_pic0_quotient_rejected": True,
            "neutral_pic0_selection_absent": True,
            "finite_gerbe_torsion_route_live": True,
            "smooth_gerbe_source_still_open": True,
            "same_source_operator_selector_still_open": True,
            "selected_terminal_lane_pic0_source_proved": False,
            "selected_Qa_SU3_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "next_required_artifact": "MTT_Selected_Pic0_Invariance_or_Gerbe_Twisted_DE_Source_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedTerminalMonadLanePic0QuotientSource",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "terminal_lane_pic0_shortcut_audited": True,
            "conditional_L3_K2_uniqueness_inside_terminal_lane_imported": True,
            "strict_ordered_validator_dependency_identified": True,
            "naive_pic0_quotient_rejected_until_invariance_theorem": True,
            "finite_gerbe_torsion_route_positioned_as_live_repair": True,
        },
        "what_remains_open": {
            "terminal_monad_lane_selector": True,
            "standard_lattice_and_base_order_source": True,
            "Pic0_invariance_or_neutral_selection_theorem": True,
            "selected_cover_or_good_cover_Deligne_Cech_data": True,
            "Freed_Witten_and_projector_retention": True,
            "selected_D_E_dotD_Riesz_Green": True,
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
    routes = []
    for route in candidate["pic0_route_audit"]:
        routes.append(
            f"### `{route['id']}`\n\n"
            f"Status: `{route['status']}`\n\n"
            f"{route['reason']}"
        )
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    terminal = candidate["terminal_lane_audit"]
    return f"""# MTT Selected Terminal Monad Lane Pic0 Quotient Source v1

## Purpose

This artifact evaluates the proposed shortcut:

```text
replace the open ordered V_alpha/Pic0 gate by selecting the terminal monad
lane and quotienting Pic0.
```

It is an audit theorem, not a closure theorem.  It preserves the strong
terminal-lane result while blocking the unjustified Pic0 shortcut.

## Inputs

{sources}

## Imported Status

- Previous frontier: `{imported["previous_frontier"]["status"]}`
- Terminal lane attempt: `{imported["terminal_lane_attempt"]["status"]}`
- Conditional monad difference: `{imported["conditional_monad_difference"]["status"]}`
- Unconditional monad difference: `{imported["unconditional_monad_difference"]["status"]}`
- Monad sufficiency: `{imported["monad_sufficiency"]["status"]}`
- Deck/Cech lift: `{imported["finite_deck_cech_lift"]["status"]}`
- Fixed gerbe representative: `{imported["fixed_gerbe_representative"]["status"]}`
- Flat gerbe promotion: `{imported["flat_gerbe_promotion"]["status"]}`
- Smooth S3 lift: `{imported["smooth_s3_lift_attempt"]["status"]}`
- HYM operator attempt: `{imported["hym_operator_attempt"]["status"]}`

## Terminal Lane Result

Inside the terminal monad-difference lane, the ordered target is forced:

- ordered difference: `{terminal["selected_ordered_difference"]}`
- `L`: `{terminal["selected_ordered_difference_L"]}`
- `L2`: `{terminal["selected_ordered_difference_L2"]}`

The strict ordered-source validator would pass after source-selection and
Pic0 fields are supplied.  The corpus does not yet prove that MTT selects the
terminal lane itself, the standard/equivalent lattice, or the base order.

## Pic0 Route Audit

{chr(10).join(routes)}

## Theorem

`{candidate["theorem"]["name"]}` is proved as an audit theorem:

{candidate["theorem"]["statement"]}

Corollary:

{candidate["theorem"]["corollary"]}

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
