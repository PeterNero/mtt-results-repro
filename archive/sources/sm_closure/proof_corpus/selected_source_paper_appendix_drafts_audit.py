"""Audit selected-source paper appendix draft packet."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_source_paper_appendix_drafts.candidate.json"
CERT = REPO / "certificates" / "selected_source_paper_appendix_drafts_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Source_Paper_Appendix_Drafts_v1.md"
DRAFT_DIR = REPO / "proof_corpus" / "paper_appendix_drafts" / "selected_source"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    drafts = [entry for entries in data["drafts_by_paper"].values() for entry in entries]
    insertion_ids = set(data["insertion_index"])
    draft_texts = [(REPO / entry["draft_path"]).read_text(encoding="utf-8") for entry in drafts]
    all_drafts_exist = all((REPO / entry["draft_path"]).exists() for entry in drafts)
    all_open = all(
        item["status"] == "APPENDIX_DRAFT_PROOF_SLOT_OPEN"
        and item["promotes_selected_flags_now"] is False
        for item in data["insertion_index"].values()
    )
    all_guarded = all(
        "does not promote any lifted diagnostic flag" in text
        and "No observed masses, mixings, thresholds, or fitted constants" in text
        and "Safe wording before proof" in text
        for text in draft_texts
    )
    all_have_artifacts = all(
        len(item["validation_artifacts"]) >= 1 for item in data["insertion_index"].values()
    )

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_SOURCE_PAPER_APPENDIX_DRAFTS_BUILT_PROOF_SLOTS_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("draft directory exists", DRAFT_DIR.exists(), DRAFT_DIR),
        check("draft count", len(drafts) == 15 and cert["draft_count"] == 15, len(drafts)),
        check("draft files exist", all_drafts_exist, [entry["draft_path"] for entry in drafts]),
        check(
            "six insertion ids",
            {
                "I1_selected_strominger_minimizer_to_phifin_trace",
                "I2_projective_rhoe_source_promotion",
                "I3_smooth_bn_galerkin_lift_theorem",
                "I4_selected_DE_action_and_source_flags",
                "I5_dotD_alpha1_and_C1_response",
                "I6_parameter_policy_appendix_update",
            }.issubset(insertion_ids),
            insertion_ids,
        ),
        check("proof slots stay open", all_open, data["insertion_index"]),
        check("guardrails in every draft", all_guarded, [entry["draft_path"] for entry in drafts]),
        check("validation artifacts listed", all_have_artifacts, data["insertion_index"]),
        check(
            "policy blocks promotion",
            data["policy"]["appendix_sections_are_proof_slots"] is True
            and data["policy"]["selected_flags_promoted_now"] is False
            and data["policy"]["diagnostic_lifts_remain_diagnostic_only"] is True
            and data["policy"]["target_fitting_used"] is False
            and data["policy"]["observed_constants_as_selectors"] is False,
            data["policy"],
        ),
        check(
            "prior repo policy aligned",
            len(data["prior_repo_patterns"]) == 2
            and {entry["repo"] for entry in data["prior_repo_patterns"]}
            == {"mtt-q79-proof-repro", "mtt-nonsm-constants-no-knob"},
            data["prior_repo_patterns"],
        ),
        check("closure not claimed", data["closure_claimed"] is False, data["what_remains_open"]),
        check(
            "note summarizes next",
            "Next numerical artifact" in note
            and "selected flag can be set true only after the matching theorem slot is proved" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected-source paper appendix drafts audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
