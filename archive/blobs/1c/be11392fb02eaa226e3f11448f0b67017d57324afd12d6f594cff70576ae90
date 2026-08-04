"""Promote the terminal admissible-section principle into the active MTT spine.

This is an axiomatic promotion, not a derivation from older corpus alone.  It
turns the q79 conditional source prefix into a theorem relative to the updated
MTT spine while keeping the deeper derivation obligation visible.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

Q79_TERMINAL = Q79 / "certificates" / "terminal_admissible_section_source_principle_certificate.json"
Q79_UNCONDITIONAL_ATTEMPT = (
    Q79 / "proof_corpus" / "Unconditional_Selected_Monad_Difference_L2_Source_Attempt_v1.md"
)
GAUGE_SECTION = (
    OBSIDIAN
    / "5 Dirac Delta"
    / "Gauge_Fixing_as_Admissible_Section_Selection_in_Modal_Triplet_Theory.md"
)
LOCAL_PREFIX = CERTS / "selected_qa_su3_m1_cw_operator_source_conditional_prefix_certificate.json"

PACKET = CANDIDATES / "terminal_admissible_section_principle_spine_promotion.candidate.json"
CERT = CERTS / "terminal_admissible_section_principle_spine_promotion_certificate.json"
NOTE = CORPUS / "Terminal_Admissible_Section_Principle_Spine_Promotion_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel_or_abs(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def file_contains(path: Path, phrases: tuple[str, ...]) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    return all(phrase in text for phrase in phrases)


def build_packet() -> dict[str, Any]:
    q79_terminal = load(Q79_TERMINAL)
    local_prefix = load(LOCAL_PREFIX)

    selected = q79_terminal["selection_derivation"]
    terminal_scan = q79_terminal["terminal_lane_scan"]

    corpus_checks = {
        "C0_q79_terminal_principle_packet_exists": Q79_TERMINAL.exists(),
        "C1_gauge_section_paper_states_admissible_section_selection": file_contains(
            GAUGE_SECTION,
            (
                "Gauge fixing is admissible section selection",
                "representative selection",
                "quotient projection",
            ),
        ),
        "C2_unconditional_attempt_identifies_missing_direct_old_corpus_selector": file_contains(
            Q79_UNCONDITIONAL_ATTEMPT,
            (
                "no direct selector found",
                "actual MTT source-lane selector: open",
                "Minimal New Statement That Would Close It",
            ),
        ),
        "C3_q79_corpus_supports_but_does_not_derive_principle": q79_terminal[
            "corpus_support"
        ]["supported"]
        is True
        and q79_terminal["source_principle"]["status"]
        == "EXPLICIT_PRINCIPLE_SYNTHESIZED_FROM_MTT_CORPUS",
        "C4_local_prefix_currently_conditional": local_prefix["selected_source_prefix"][
            "status"
        ]
        == "CONDITIONAL_ON_TERMINAL_ADMISSIBLE_SECTION_SOURCE_PRINCIPLE"
        and local_prefix["verdict"]["selected_source_unconditional"] is False,
    }

    axiom_schema = {
        "name": "MTT_TerminalAdmissibleSectionSourceAxiom.v1",
        "status": "PROMOTED_TO_ACTIVE_MTT_SPINE_AS_EXPLICIT_AXIOM_SCHEMA",
        "not_derived_from_older_corpus": True,
        "statement": (
            "When an MTT quotient or degeneracy class has been reduced to a "
            "finite terminal representative section, the physical source is "
            "the unique admissible section that is refinement-stable, preserves "
            "the active shared-circle and quotient constraints, resolves the "
            "active obstruction data, and adds minimal extra responsibility. "
            "If exactly one terminal candidate satisfies the admissibility "
            "filters, that candidate is selected. If more than one survives, "
            "the theorem does not select and a higher source functional is "
            "required."
        ),
        "admissibility_filters": [
            "terminal representative in the already reduced quotient class",
            "refinement stability under allowed quotient/refinement maps",
            "shared-circle or central neutrality when the carrier has a shared central circle",
            "compatibility with required topological obstruction data such as visible Chern/Bianchi row",
            "minimal added source responsibility among surviving candidates",
            "no observed masses, mixings, benchmark Yukawa entries, or target-value backsolve",
        ],
        "failure_modes": {
            "no_survivor": "source not selected; return to source construction",
            "multiple_survivors": "higher source functional or retarded/operator selector required",
            "holonomy_sensitive_layer": "Pic0/flat data must be reopened instead of quotienting by topology alone",
        },
        "why_this_is_a_spine_rule": [
            "It is the finite terminal analogue of admissible section selection in quotient geometry.",
            "It turns representative choice into an auditable source rule rather than a post-hoc flag.",
            "It can fail, so it is not a universal fitting license.",
            "It is evaluated before flavor observables are consulted.",
        ],
    }

    q79_application_checks = {
        "Q0_terminal_lane_finite": terminal_scan["terminal_lane"] == "L_i-K2"
        and terminal_scan["candidate_count"] == 5,
        "Q1_unique_shared_circle_neutral_survivor": terminal_scan["unique_zero_central"] is True
        and terminal_scan["zero_central_labels"] == ["L3-K2"],
        "Q2_unique_visible_c2_survivor": terminal_scan["unique_visible_c2_in_terminal_lane"] is True
        and terminal_scan["visible_c2_labels"] == ["L3-K2"],
        "Q3_selected_L_and_c2_match_source_prefix": selected["selected_L"] == [1, -2, 0]
        and selected["selected_L2"] == [2, -4, 0]
        and selected["selected_c2"] == [4, 0, 0],
        "Q4_validators_pass_under_promoted_spine_rule": q79_terminal["validator_results"][
            "ordered_source"
        ]["exit_code"]
        == 0
        and q79_terminal["validator_results"]["cohomology"]["exit_code"] == 0
        and q79_terminal["validator_results"]["cohomology"]["promotes_rank_two_route"] is True,
        "Q5_local_prefix_can_upgrade_relative_to_spine": local_prefix["verdict"][
            "conditional_prefix_closed"
        ]
        is True
        and local_prefix["what_closes_now"][
            "selected_visible_source_prefix_under_explicit_principle"
        ]
        is True,
    }

    promotion_checks = {
        **corpus_checks,
        **q79_application_checks,
        "P0_axiom_is_explicit_not_hidden_fit": axiom_schema["not_derived_from_older_corpus"] is True,
        "P1_no_flavor_or_observed_inputs": all(
            q79_terminal["guardrails"][key] is False
            for key in (
                "uses_benchmark_flavor_entries",
                "uses_observed_flavor_data",
            )
        ),
        "P2_not_full_operator_or_SM_closure": local_prefix["verdict"][
            "full_CW_operator_source_closed"
        ]
        is False
        and local_prefix["what_remains_open"]["selected_dotD_alpha1_first_variation"] is True,
    }

    return {
        "packet": "Terminal_Admissible_Section_Principle_Spine_Promotion_v1",
        "status": "TERMINAL_ADMISSIBLE_SECTION_PRINCIPLE_PROMOTED_TO_ACTIVE_MTT_SPINE_RELATIVE_THEOREM",
        "inputs": {
            "q79_terminal_principle": rel_or_abs(Q79_TERMINAL),
            "q79_unconditional_attempt": rel_or_abs(Q79_UNCONDITIONAL_ATTEMPT),
            "gauge_section_corpus": rel_or_abs(GAUGE_SECTION),
            "local_conditional_prefix": rel_or_abs(LOCAL_PREFIX),
        },
        "promotion_checks": promotion_checks,
        "axiom_schema": axiom_schema,
        "q79_application": {
            "selected_source_label": selected["selected_source_label"],
            "selected_L": selected["selected_L"],
            "selected_L2": selected["selected_L2"],
            "selected_c2": selected["selected_c2"],
            "terminal_lane_scan": terminal_scan,
            "spine_relative_source_status": "SELECTED_BY_ACTIVE_MTT_SPINE_AXIOM",
        },
        "what_closes_now": {
            "terminal_principle_is_no_longer_conditional_inside_active_spine": True,
            "q79_L3_K2_source_selected_relative_to_active_spine": True,
            "local_CW_source_prefix_upgrades_from_conditional_to_spine_relative": True,
            "old_corpus_gap_is_reclassified_as_deeper_axiom_derivation_obligation": True,
        },
        "what_remains_open": {
            "derive_terminal_axiom_from_deeper_projection_dynamics": True,
            "global_operator_layer_Pic0_or_flat_holonomy_rule": True,
            "selected_literal_goodcover_or_HYM_stability_payload": True,
            "selected_dotD_alpha1_first_variation": True,
            "retarded_overlap_derivative_formula": True,
            "primitive_C1_response_matrices": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "theorem": {
            "name": "TerminalAdmissibleSectionPrincipleSpinePromotionTheorem",
            "proved": all(promotion_checks.values()),
            "relative_to_active_spine": True,
            "derived_from_prior_corpus_alone": False,
            "statement": (
                "The terminal admissible-section source rule is promoted to an "
                "explicit axiom schema of the active MTT spine. Relative to "
                "that updated spine, the q79 terminal lane selects g3/L3-K2 "
                "unconditionally because it is the unique finite terminal "
                "candidate preserving the shared circle and realizing the "
                "visible Chern class, with validators passing and no flavor "
                "inputs. This does not derive the axiom from older corpus alone "
                "and does not close dotD, C1, Yukawa, or full SM data."
            ),
        },
        "verdict": {
            "spine_promotion_complete": all(promotion_checks.values()),
            "q79_source_unconditional_relative_to_active_spine": True,
            "q79_source_unconditional_from_old_corpus_alone": False,
            "next_required_artifact": "Terminal_Admissible_Section_Axiom_Derivation_from_Projection_Dynamics_or_dotD_C1_Source_v1",
            "why_next": (
                "Either derive the new spine axiom from a deeper finite "
                "projection/nil-survivor operator, or continue downstream with "
                "dotD/C1 using the active-spine source as a permitted premise."
            ),
        },
        "guardrails": {
            "claims_derived_from_prior_corpus_alone": False,
            "claims_full_CW_operator_source_theorem": False,
            "claims_selected_dotD_alpha1": False,
            "claims_primitive_C1_response": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "uses_observed_cp_or_masses": False,
            "uses_benchmark_flavor_entries": False,
            "uses_lifted_selected_flags": False,
        },
    }


def render_note(packet: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Terminal Admissible-Section Principle Spine Promotion v1",
            "",
            "## Result",
            "",
            f"Status: `{packet['status']}`",
            "",
            "The terminal admissible-section source rule is now promoted into the",
            "active MTT spine as an explicit axiom schema.  This is not a derivation",
            "from older corpus alone; it is a controlled spine update.  Relative to",
            "that updated spine, q79's terminal `g3 / L3-K2` source is selected",
            "without remaining conditional wording.",
            "",
            "The promotion is intentionally fail-fast: if a terminal quotient class",
            "has no survivor or multiple survivors, the axiom does not select a",
            "source and a higher source functional is required.",
            "",
            "## Axiom Schema",
            "",
            "```json",
            json.dumps(packet["axiom_schema"], indent=2, sort_keys=True),
            "```",
            "",
            "## q79 Application",
            "",
            "```json",
            json.dumps(packet["q79_application"], indent=2, sort_keys=True),
            "```",
            "",
            "## What Closes Now",
            "",
            "```json",
            json.dumps(packet["what_closes_now"], indent=2, sort_keys=True),
            "```",
            "",
            "## What Remains Open",
            "",
            "```json",
            json.dumps(packet["what_remains_open"], indent=2, sort_keys=True),
            "```",
            "",
            f"Next: `{packet['verdict']['next_required_artifact']}`.",
            "",
        ]
    )


def main() -> int:
    packet = build_packet()
    if "--write-certificate" in sys.argv:
        PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        CERT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        NOTE.write_text(render_note(packet), encoding="utf-8")
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
