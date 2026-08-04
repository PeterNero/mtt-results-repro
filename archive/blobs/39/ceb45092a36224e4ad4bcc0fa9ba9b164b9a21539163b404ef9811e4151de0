"""Audit selected SM-slot functor value emission or axiom patch gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_smslotfunctor_valueemission_or_axiompatch.py"
CANDIDATE = ROOT / "candidate_data" / "selected_smslotfunctor_valueemission_or_axiompatch.candidate.json"
CERT = ROOT / "certificates" / "selected_smslotfunctor_valueemission_or_axiompatch_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SelectedSMSlotFunctor_ValueEmission_or_AxiomPaperPatch_v1.md"

STATUS = "MTT_SELECTED_SMSLOTFUNCTOR_VALUE_EMISSION_BLOCKED_AXIOM_PATCH_READY"
NEXT = "MTT_TerminalAxiomPatch_Apply_or_SMSlotFunctor_ArrowValues_v1"


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
    patch = data["axiom_patch_bundle"]
    attempt = data["selected_SM_slot_functor_value_emission_attempt"]
    decision = data["selection_decision"]
    closes = data["what_closes_now"]
    remains = data["what_remains_open"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "superset strategy guarded",
            data["superset_strategy"]["using_one_straight_path"] is False
            and data["superset_strategy"]["observed_data_used"] is False
            and data["superset_strategy"]["target_fitting_used"] is False
            and "apply" in data["superset_strategy"]["route_A"]
            and "emit" in data["superset_strategy"]["route_B"],
            data["superset_strategy"],
        ),
        check(
            "axiom patch ready but unapplied",
            patch["status"] == "READY_TO_APPLY_NOT_APPLIED"
            and len(patch["target_papers"]) == 4
            and "Terminal admissible-section selection axiom" in patch["patch_text"]
            and patch["post_patch_replay"]["can_rerun_terminal_source_unconditionally"] is True
            and patch["post_patch_replay"]["requires_actual_patch_or_internal_derivation"] is True,
            patch,
        ),
        check(
            "value emission blocked exactly at selected arrows",
            attempt["status"] == "ATTEMPTED_BLOCKED_BY_SELECTED_ARROW_VALUES"
            and len(attempt["legal_emission_conditions"]) == 6
            and attempt["support_available"]["finite_q79_U10_Ubar5"] is True
            and attempt["support_available"]["structural_1M_rule"] is True
            and attempt["support_available"]["stationary_projector_source_promoted"] is True
            and attempt["failed_conditions"]["selected_sectionring_to_10M_clock_arrow"] is True
            and attempt["failed_conditions"]["selected_overlap_transfer_normalization"] is True,
            attempt,
        ),
        check(
            "selection decision does not overclaim",
            decision["route_A_axiom_patch_ready"] is True
            and decision["route_B_direct_value_emission_closed"] is False
            and decision["can_claim_selected_SMSlotFunctor_values_now"] is False
            and decision["can_claim_unconditional_terminal_source_now"] is False
            and decision["can_claim_after_actual_axiom_patch"]["terminal_source_and_h1_Ext"] is True
            and decision["can_claim_after_actual_axiom_patch"]["SM_slot_functor_values"] is False,
            decision,
        ),
        check(
            "closure/remainder accounting",
            closes["axiom_patch_bundle_ready"] is True
            and closes["direct_value_emission_no_overclaim_proved"] is True
            and closes["rho_s_alone_rejected_as_slot_selector"] is True
            and remains["apply_or_derive_terminal_admissible_section_axiom"] is True
            and remains["selected_U10_Ubar5_source_outputs"] is True
            and remains["same_source_consistency_map"] is True,
            {"closes": closes, "remains": remains},
        ),
        check(
            "theorem and guardrails",
            data["theorem"]["proved"] is True
            and data["closure_claimed"] is False
            and data["unconditional_terminal_source_claimed"] is False
            and data["selected_SMSlotFunctor_values_claimed"] is False
            and data["observed_data_used"] is False
            and data["target_fitting_used"] is False
            and cert["selected_SMSlotFunctor_values_claimed"] is False,
            cert,
        ),
        check(
            "note and next gate recorded",
            data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "The stationary `rho_s` source alone is not enough" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected SM-slot functor value emission / axiom patch audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
