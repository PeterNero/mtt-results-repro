"""Audit selected-source paper integration manifest."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_source_paper_integration_manifest.candidate.json"
CERT = REPO / "certificates" / "selected_source_paper_integration_manifest_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Source_Paper_Integration_Manifest_v1.md"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    insertions = data["insertions"]
    ids = {item["id"] for item in insertions}
    all_have_targets = all(item["target_papers"] for item in insertions)
    all_have_obligations = all(len(item["proof_obligations"]) >= 4 for item in insertions)
    all_have_safe_wording = all(item["safe_wording"] for item in insertions)
    blockers = {blocker for item in insertions for blocker in item["current_blockers_resolved_if_proved"]}

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_SOURCE_PAPER_INTEGRATION_MANIFEST_BUILT_INSERTIONS_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("six insertions", len(insertions) == 6, ids),
        check(
            "critical insertions present",
            {
                "I1_selected_strominger_minimizer_to_phifin_trace",
                "I2_projective_rhoe_source_promotion",
                "I3_smooth_bn_galerkin_lift_theorem",
                "I4_selected_DE_action_and_source_flags",
                "I5_dotD_alpha1_and_C1_response",
                "I6_parameter_policy_appendix_update",
            }.issubset(ids),
            ids,
        ),
        check("targets present", all_have_targets, insertions),
        check("proof obligations present", all_have_obligations, insertions),
        check("safe wording present", all_have_safe_wording, insertions),
        check(
            "selected flags covered",
            "operator_slots[*].selected_source_verified" in blockers
            and "selected_dotD_source_verified" in blockers
            and "alpha1_driver_verified" in blockers,
            blockers,
        ),
        check(
            "global guardrails",
            data["global_rules"]["do_not_set_selected_flags_without_named_theorem"] is True
            and data["global_rules"]["diagnostic_lifts_are_algebraic_smoke_tests_only"] is True
            and data["global_rules"]["observed_data_cannot_select_sources"] is True,
            data["global_rules"],
        ),
        check("closure not claimed", data["closure_claimed"] is False, data["what_remains_open"]),
        check("no target fitting", data["target_fitting_used"] is False, data["target_fitting_used"]),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_Source_Paper_Appendix_Drafts_v1",
            data["next_required_artifact"],
        ),
        check(
            "note records policy",
            "diagnostic lifted flags can prove algebraic consistency only" in note
            and "Selected D_E Action" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected-source paper integration manifest audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
