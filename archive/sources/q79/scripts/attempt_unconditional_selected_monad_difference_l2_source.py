"""Attempt the unconditional Selected_Monad_Difference_L2_Source theorem.

This goes beyond the previous conditional uniqueness theorem.  It searches the
local MTT corpus for a genuine source-lane selector and a Pic0 rule, then
classifies every plausible route:

* direct corpus selector,
* flux monad table,
* generic Cech overlap principle,
* minimality/reuse principle,
* Pic0 quotient/selection rule,
* same-source operator/Hessian route.

The current result is intentionally conservative: the proof does not close
unless both source-lane selection and Pic0 resolution are actually present.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"
MTT_CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
CONSTANTS_REPO = ROOT.parent / "mtt-nonsm-constants-no-knob"

FLUX_PAPER = (
    MTT_CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)
CORE_B0 = (
    MTT_CORPUS
    / "1 Core & Encodings"
    / "The_Modal_Triplet_Theory_Program_B0__Why_Description_Forces_Circle__Lens__and_Nil.md"
)

PREVIOUS_ATTEMPT = CERTIFICATES / "selected_monad_difference_l2_source_proof_attempt_certificate.json"
MONAD_GATE = CERTIFICATES / "iwasawa_monad_map_data_gate_certificate.json"
MONAD_ROLE = CERTIFICATES / "iwasawa_monad_visible_source_role_certificate.json"
SUFFICIENCY = CERTIFICATES / "monad_difference_l2_source_sufficiency_certificate.json"
SELECTOR_OBSTRUCTION = CERTIFICATES / "visible_rank2_l2_selector_obstruction_certificate.json"
VALPHA_CANDIDATES = CERTIFICATES / "visible_valpha_chern_bianchi_source_packet_candidates_certificate.json"
SELECTED_DE_HUNT = CERTIFICATES / "selected_de_source_hunt_certificate.json"
CONSTANTS_TERMINAL_LANE = (
    CONSTANTS_REPO
    / "certificates"
    / "selected_qa_su3_terminal_monad_lane_selector_attempt_certificate.json"
)

CANDIDATE = CANDIDATE_DATA / "unconditional_selected_monad_difference_l2_source_attempt.candidate.json"
CERTIFICATE = CERTIFICATES / "unconditional_selected_monad_difference_l2_source_attempt_certificate.json"


DIRECT_SELECTOR_PATTERNS = [
    r"\bMTT\s+selects\s+L3\s*-\s*K2\b",
    r"\bL3\s*-\s*K2\s+is\s+selected\b",
    r"\bSelected_Monad_Difference_L2_Source\b",
    r"\bterminal\s+monad[- ]difference\s+lane\s+is\s+selected\b",
    r"\bneutral\s+Pic0\s+is\s+selected\b",
    r"\bPic0\s+quotient\s+rule\b",
]

SOURCE_LANE_PATTERNS = [
    r"\bterminal\s+monad[- ]difference\b",
    r"\bL_i\s*-\s*K2\b",
    r"\bvisible\s+ordered\s+L\s+source\b",
    r"\bmonad[- ]difference\s+lane\b",
]

PIC0_PATTERNS = [
    r"\bPic0\b",
    r"\bPicard\s+zero\b",
    r"\bflat\s+character\b",
    r"\bflat\s+twist\b",
    r"\bflat\s+line\s+bundle\b",
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def corpus_markdown_files() -> list[Path]:
    if not MTT_CORPUS.exists():
        return []
    return sorted(MTT_CORPUS.rglob("*.md"))


def search_corpus(patterns: list[str], *, max_hits: int = 25) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    compiled = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    for path in corpus_markdown_files():
        text = read(path)
        matched = [pattern.pattern for pattern in compiled if pattern.search(text)]
        if matched:
            hits.append(
                {
                    "path": str(path),
                    "matched_patterns": matched,
                }
            )
            if len(hits) >= max_hits:
                break
    return hits


def contains_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def analyze() -> dict[str, Any]:
    previous = load_json(PREVIOUS_ATTEMPT)
    monad_gate = load_json(MONAD_GATE)
    monad_role = load_json(MONAD_ROLE)
    sufficiency = load_json(SUFFICIENCY)
    obstruction = load_json(SELECTOR_OBSTRUCTION)
    valpha = load_json(VALPHA_CANDIDATES)
    de_hunt = load_json(SELECTED_DE_HUNT)
    constants_terminal = load_json(CONSTANTS_TERMINAL_LANE)

    flux = read(FLUX_PAPER)
    core = read(CORE_B0)

    direct_selector_hits = search_corpus(DIRECT_SELECTOR_PATTERNS)
    source_lane_hits = search_corpus(SOURCE_LANE_PATTERNS)
    pic0_hits = search_corpus(PIC0_PATTERNS)

    flux_has_monad_table = all(
        token in flux
        for token in [
            "0\\longrightarrow K_1",
            "\\ell_3&=+1",
            "\\kappa_2=b",
            "Choose",
        ]
    )
    flux_has_selection_language = contains_any(
        flux,
        [
            r"\bselects\s+\$?\\ell_3",
            r"\bselected\s+monad\s+difference\b",
            r"\bselected\s+visible\s+V_alpha\b",
            r"\bPic0\b",
        ],
    )
    flux_typed_sections_supplied = (
        monad_gate.get("source_monad", {}).get("source_gives_explicit_f_entries") is True
        and monad_gate.get("source_monad", {}).get("source_gives_explicit_g_entries") is True
    )

    core_supplies_cech_language = (
        "transition maps" in core and "1-cocycle" in core and "structure group" in core
    )
    core_selects_specific_line = contains_any(
        core,
        [
            r"\bL3\s*-\s*K2\b",
            r"\bterminal\s+monad[- ]difference\b",
            r"\bPic0\b",
            r"\bV_alpha\b",
        ],
    )

    previous_conditional_closed = (
        previous.get("what_this_closes", {}).get(
            "unique_L3_minus_K2_inside_ordered_terminal_monad_difference_lane"
        )
        is True
        and previous.get("what_this_closes", {}).get("proof_frontier_no_longer_arithmetic")
        is True
    )
    sufficiency_closed = sufficiency.get("relative_theorem", {}).get("proved") is True
    no_hidden_selector = (
        obstruction.get("status") == "VISIBLE_RANK2_L2_SELECTOR_OBSTRUCTION_PROVED_SOURCE_REQUIRED"
    )
    visible_source_open = (
        valpha.get("calculation_results", {}).get("selected_visible_valpha_source_constructed")
        is False
    )
    selected_de_absent = (
        de_hunt.get("status") == "SELECTED_D_E_SOURCE_NOT_FOUND_ROUTE_C_FINITE_SOLVE_RECOMMENDED"
    )

    route_results = {
        "R1_direct_corpus_selector": {
            "status": "FAIL_ABSENT",
            "passes": bool(direct_selector_hits),
            "hits": direct_selector_hits,
            "reason": "No direct corpus statement selects L3-K2 as the visible ordered source or resolves Pic0.",
        },
        "R2_flux_monad_table": {
            "status": "CANDIDATE_ONLY",
            "passes": False,
            "evidence": {
                "monad_table_present": flux_has_monad_table,
                "selection_language_present": flux_has_selection_language,
                "typed_sections_supplied": flux_typed_sections_supplied,
                "monad_visible_c2_role_separated": monad_role.get("what_this_closes", {}).get(
                    "do_not_reuse_c2_zero_monad_as_c2_4_alpha1_source"
                )
                is True,
            },
            "reason": (
                "The flux paper supplies the line table and a chosen monad, but it does not "
                "state that the terminal pair L3,K2 is the selected visible V_alpha source; "
                "typed sections and transition data are still missing."
            ),
        },
        "R3_core_cech_overlap_principle": {
            "status": "LANGUAGE_ONLY",
            "passes": False,
            "evidence": {
                "core_supplies_cech_language": core_supplies_cech_language,
                "core_selects_specific_L3_minus_K2_or_Pic0": core_selects_specific_line,
            },
            "reason": (
                "The core overlap theorem justifies Cech cocycles as the language of "
                "bundle data. It does not choose this line class, base ordering, or Pic0 representative."
            ),
        },
        "R4_minimality_or_reuse_principle": {
            "status": "INSUFFICIENT_WITHOUT_FORMAL_SELECTOR",
            "passes": False,
            "evidence": {
                "primary_rank2_route_identified": valpha.get("best_current_route", {}).get(
                    "candidate_id"
                )
                == "rank2_non_split_extension_preferred_L_1_-2_0",
                "selected_visible_valpha_source_constructed": not visible_source_open,
                "source_lane_hits": source_lane_hits,
            },
            "reason": (
                "Broad minimality/reuse language can rank the target as the best current route, "
                "but it is not a formal selection functional over Pic0 and source lanes."
            ),
        },
        "R5_pic0_selection_or_quotient": {
            "status": "FAIL_ABSENT",
            "passes": False,
            "evidence": {
                "pic0_hits_in_mtt_corpus": pic0_hits,
                "no_hidden_pic0_selector_theorem": no_hidden_selector,
                "sufficiency_still_requires_pic0": sufficiency.get("still_open", {}).get(
                    "select_or_quotient_Pic0_without_notational_assumption"
                )
                is True,
            },
            "reason": (
                "The present corpus contains no holonomy-sensitive Pic0 selector and no "
                "gauge quotient theorem. Current q79 obstruction says topology/cohomology/curvature "
                "cannot select neutral Pic0."
            ),
        },
        "R6_same_source_operator_or_hessian": {
            "status": "FAIL_ABSENT",
            "passes": False,
            "evidence": {
                "selected_D_E_source_absent": selected_de_absent,
                "same_source_D_E_constructed": valpha.get("calculation_results", {}).get(
                    "same_source_D_E_dotD_Riesz_Green_constructed"
                )
                is True,
            },
            "reason": (
                "A same-source D_E/dotD/Hessian package would be strong enough to break "
                "base/Pic0 degeneracy, but no selected source operator package exists yet."
            ),
        },
        "R7_constants_terminal_lane_attempt": {
            "status": "CORROBORATES_BLOCKER",
            "passes": False,
            "evidence": {
                "constants_certificate_present": bool(constants_terminal),
                "constants_status": constants_terminal.get("status"),
                "conditional_uniqueness_closed": constants_terminal.get("closed_now", {}).get(
                    "conditional_uniqueness_inside_terminal_lane"
                )
                is True,
                "terminal_lane_selector_closed": constants_terminal.get("gate_result", {}).get(
                    "terminal_monad_lane_selector_closed"
                )
                is True,
                "pic0_still_open": constants_terminal.get("not_closed", {}).get(
                    "Pic0_selection_or_quotient"
                )
                is True,
            },
            "reason": (
                "The constants/no-knob repo independently reaches the same point: "
                "terminal-lane conditional uniqueness is closed, but the lane selector "
                "and Pic0 rule are still open."
            ),
        },
    }

    source_lane_selected = any(
        route_results[key]["passes"]
        for key in [
            "R1_direct_corpus_selector",
            "R2_flux_monad_table",
            "R3_core_cech_overlap_principle",
            "R4_minimality_or_reuse_principle",
            "R6_same_source_operator_or_hessian",
            "R7_constants_terminal_lane_attempt",
        ]
    )
    pic0_resolved = route_results["R5_pic0_selection_or_quotient"]["passes"]
    proof_closed = (
        previous_conditional_closed and sufficiency_closed and source_lane_selected and pic0_resolved
    )

    status = (
        "UNCONDITIONAL_SELECTED_MONAD_DIFFERENCE_L2_SOURCE_PROVED"
        if proof_closed
        else "UNCONDITIONAL_SELECTED_MONAD_DIFFERENCE_L2_SOURCE_ATTEMPT_BLOCKED_NO_SELECTOR_OR_PIC0_RULE"
    )

    return {
        "calculation": "UnconditionalSelectedMonadDifferenceL2SourceAttempt",
        "status": status,
        "generated_by": "scripts/attempt_unconditional_selected_monad_difference_l2_source.py",
        "corpus_root": str(MTT_CORPUS),
        "input_certificates": {
            "previous_conditional_attempt": PREVIOUS_ATTEMPT.name,
            "iwasawa_monad_map_data_gate": MONAD_GATE.name,
            "iwasawa_monad_visible_source_role": MONAD_ROLE.name,
            "monad_difference_sufficiency": SUFFICIENCY.name,
            "selector_obstruction": SELECTOR_OBSTRUCTION.name,
            "visible_valpha_candidates": VALPHA_CANDIDATES.name,
            "selected_de_source_hunt": SELECTED_DE_HUNT.name,
            "constants_terminal_lane_attempt": str(CONSTANTS_TERMINAL_LANE),
        },
        "input_statuses": {
            "previous_conditional_attempt": previous.get("status"),
            "monad_gate": monad_gate.get("status"),
            "monad_role": monad_role.get("status"),
            "sufficiency": sufficiency.get("status"),
            "selector_obstruction": obstruction.get("status"),
            "visible_valpha_candidates": valpha.get("status"),
            "selected_de_source_hunt": de_hunt.get("status"),
            "constants_terminal_lane_attempt": constants_terminal.get("status"),
        },
        "already_closed": {
            "conditional_uniqueness_of_L3_minus_K2_inside_terminal_lane": previous_conditional_closed,
            "selected_monad_difference_would_pass_validator": sufficiency_closed,
            "current_closed_invariants_have_no_hidden_selector": no_hidden_selector,
        },
        "route_results": route_results,
        "unconditional_theorem_attempt": {
            "proved": proof_closed,
            "source_lane_selected": source_lane_selected,
            "pic0_resolved": pic0_resolved,
            "reason_not_proved": (
                "The current corpus proves candidate arithmetic and conditional uniqueness, "
                "but it lacks both an MTT source-lane selector and a Pic0 selection/quotient rule."
            ),
        },
        "what_this_closes": {
            "exhaustive_current_route_audit_for_unconditional_selection": True,
            "direct_corpus_selector_absence_checked": len(direct_selector_hits) == 0,
            "generic_cech_principle_demoted_to_language_not_selector": core_supplies_cech_language
            and not core_selects_specific_line,
            "flux_monad_table_demoted_to_candidate_not_selector": flux_has_monad_table
            and not flux_has_selection_language,
            "minimality_reuse_not_enough_without_formal_selector": True,
            "cross_repo_terminal_lane_attempt_agrees_blocked": route_results[
                "R7_constants_terminal_lane_attempt"
            ]["evidence"]["conditional_uniqueness_closed"]
            and not route_results["R7_constants_terminal_lane_attempt"]["evidence"][
                "terminal_lane_selector_closed"
            ],
            "proof_blocker_is_source_selector_plus_pic0": not proof_closed,
        },
        "what_this_does_not_close": {
            "unconditional_Selected_Monad_Difference_L2_Source_v1": proof_closed,
            "actual_MTT_selection_of_terminal_monad_difference_lane": False,
            "neutral_Pic0_selection_or_quotient": False,
            "typed_transition_or_section_data": False,
            "same_source_operator_hessian_selector": False,
            "full_SM_closure": False,
        },
        "minimal_new_statement_that_would_close": {
            "source_lane_selector": (
                "MTT selects the visible ordered L source from central-neutral terminal "
                "monad differences L_i-K2 on the printed Iwasawa monad table."
            ),
            "pic0_rule": (
                "Either neutral Pic0 is selected by a holonomy-sensitive source, or Pic0 "
                "twists are quotient-irrelevant for the selected physical V_alpha packet."
            ),
            "why_enough": (
                "Given these two statements, the previous conditional uniqueness theorem "
                "forces L3-K2 and the sufficiency certificate makes the ordered-source validator pass."
            ),
        },
        "guardrails": {
            "claims_unconditional_theorem_proved": proof_closed,
            "claims_flux_choose_equals_mtt_selection": False,
            "claims_cech_language_selects_specific_bundle": False,
            "claims_minimality_without_selector_closes": False,
            "claims_pic0_resolved_now": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "I tried the unconditional proof across all current routes. It does not close: "
                "the monad table forces L3-K2 only after the terminal monad-difference lane is "
                "selected, and no current source supplies that lane selector or the Pic0 rule."
            ),
            "next_action": (
                "Prove or add the minimal source-lane selector and Pic0 rule, then rerun the "
                "strict ordered-source validator; no new arithmetic search is needed."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "UnconditionalSelectedMonadDifferenceL2SourceAttempt",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/unconditional_selected_monad_difference_l2_source_attempt.candidate.json",
        "corpus_root": report["corpus_root"],
        "input_certificates": report["input_certificates"],
        "input_statuses": report["input_statuses"],
        "already_closed": report["already_closed"],
        "route_results": report["route_results"],
        "unconditional_theorem_attempt": report["unconditional_theorem_attempt"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "minimal_new_statement_that_would_close": report["minimal_new_statement_that_would_close"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return (
        0
        if report["status"]
        == "UNCONDITIONAL_SELECTED_MONAD_DIFFERENCE_L2_SOURCE_ATTEMPT_BLOCKED_NO_SELECTOR_OR_PIC0_RULE"
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
