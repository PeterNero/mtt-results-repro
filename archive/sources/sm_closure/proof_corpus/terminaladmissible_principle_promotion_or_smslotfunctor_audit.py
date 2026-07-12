"""Audit terminal admissible-section principle promotion."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_terminaladmissible_principle_promotion_or_smslotfunctor.py"
CANDIDATE = ROOT / "candidate_data" / "terminaladmissible_principle_promotion_or_smslotfunctor.candidate.json"
CERT = ROOT / "certificates" / "terminaladmissible_principle_promotion_or_smslotfunctor_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_TerminalAdmissibleSection_PrinciplePromotion_or_SelectedSMSlotFunctor_v1.md"

STATUS = "MTT_TERMINALADMISSIBLE_PRINCIPLE_PROMOTION_AUDITED_AXIOM_INSERTION_OR_SMSLOTFUNCTOR_OPEN"
NEXT = "MTT_TerminalAdmissibleSection_AxiomInsertion_and_SelectedSMSlotFunctor_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    audit = data["promotion_audit"]
    axiom = data["proposed_axiom"]
    slot = data["SM_slot_functor_parallel"]
    closes = data["what_closes_now"]
    remains = data["what_remains_open"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "strategy guarded",
            data["superset_strategy"]["using_one_straight_path"] is False
            and data["superset_strategy"]["observed_data_used"] is False
            and data["superset_strategy"]["target_fitting_used"] is False,
            data["superset_strategy"],
        ),
        check(
            "corpus support collected",
            audit["corpus_supports"]["local_admissible_sections_exist"] is True
            and audit["corpus_supports"]["gauge_fixing_is_admissible_section_selection"] is True
            and audit["corpus_supports"]["nil_boundaries_select_discrete_survivors"] is True
            and audit["corpus_supports"]["minimal_extension_required_by_saturation"] is True,
            audit["corpus_supports"],
        ),
        check(
            "missing axiom identified",
            audit["not_yet_in_corpus_as_general_axiom"][
                "terminal_unique_refinement_stable_survivor_selects_source"
            ]
            is True
            and audit["not_yet_in_corpus_as_general_axiom"][
                "minimal_added_obstruction_responsibility_total_order"
            ]
            is True
            and "generally non-canonical" in audit["why_not_enough_for_unconditional_proof"],
            audit,
        ),
        check(
            "axiom drafted with guardrail",
            axiom["name"] == "TerminalAdmissibleSectionSelectionAxiom"
            and "exactly one representative" in axiom["statement"]
            and "If more than one representative" in axiom["statement"]
            and "observed masses" in axiom["guardrail_clause"],
            axiom,
        ),
        check(
            "q79 terminal case matched",
            axiom["why_it_matches_terminal_q79_case"]["unique_refinement_stable_candidate_under_filters"]
            == "g3 / L3-K2"
            and axiom["why_it_matches_terminal_q79_case"]["shared_circle_constraint"] == "central degree zero",
            axiom["why_it_matches_terminal_q79_case"],
        ),
        check(
            "SM slot route retained",
            slot["can_bypass_axiom_promotion_for_slot_readout"] is True
            and any("U_10" in item for item in slot["must_emit"])
            and any("1_M" in item for item in slot["must_emit"]),
            slot,
        ),
        check(
            "closure/remainder accounting",
            closes["exact_axiom_text_drafted"] is True
            and closes["noncanonical_gauge_fixing_guardrail_retained"] is True
            and remains["insert_axiom_into_target_papers_or_prove_from_projection_admissibility"] is True
            and remains["selected_SM_slot_functor"] is True,
            {"closes": closes, "remains": remains},
        ),
        check(
            "no overclaim",
            data["closure_claimed"] is False
            and data["unconditional_MTT_closure_claimed"] is False
            and cert["unconditional_MTT_closure_claimed"] is False
            and data["observed_data_used"] is False
            and data["target_fitting_used"] is False,
            cert,
        ),
        check(
            "theorem and next gate recorded",
            data["theorem"]["proved"] is True
            and data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and f"`{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT terminal admissible-section principle promotion audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
