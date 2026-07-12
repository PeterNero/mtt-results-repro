"""Audit terminal axiom-patch application and SM-slot arrow gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_terminal_axiom_patch_apply_or_smslotfunctor_arrowvalues.py"
CANDIDATE = ROOT / "candidate_data" / "terminal_axiom_patch_apply_or_smslotfunctor_arrowvalues.candidate.json"
CERT = ROOT / "certificates" / "terminal_axiom_patch_apply_or_smslotfunctor_arrowvalues_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_TerminalAxiomPatch_Apply_or_SMSlotFunctor_ArrowValues_v1.md"

STATUS = "MTT_TERMINAL_AXIOM_PATCH_APPLIED_CORPUS_AND_SPINE_TERMINAL_SOURCE_CLOSED_SMSLOT_ARROWS_OPEN"
NEXT = "MTT_SelectedSMSlotFunctor_SixArrow_SourceEmission_v1"


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
    axiom = data["axiom_application"]
    replay = data["unconditional_terminal_replay"]
    gate = data["SM_slot_functor_arrow_gate"]
    markers = data["external_paper_patch_verification"]
    decision = data["selection_decision"]
    closes = data["what_closes_now"]
    remains = data["what_remains_open"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "axiom applied to local proof spine and verified in corpus",
            axiom["status"] == "LOCAL_PROOF_SPINE_AXIOM_PATCH_APPLIED"
            and axiom["applied_to_local_proof_spine"] is True
            and axiom["applied_to_external_obsidian_papers"] is True
            and axiom["derived_from_prior_axioms"] is False
            and "observed masses" in axiom["guardrail_text"],
            axiom,
        ),
        check(
            "external paper markers present",
            set(markers) == {"B0", "B2", "B5", "C"}
            and all(item["exists"] for item in markers.values())
            and all(item["all_markers_present"] for item in markers.values()),
            markers,
        ),
        check(
            "terminal replay unconditional in patched spine",
            replay["status"] == "UNCONDITIONAL_IN_PATCHED_PROOF_SPINE"
            and replay["selected_source_label"] == "g3 / L3-K2"
            and replay["selected_L"] == [1, -2, 0]
            and replay["selected_L2"] == [2, -4, 0]
            and replay["selected_c2"] == [4, 0, 0]
            and replay["ordered_source_validator_passes"] is True
            and replay["cohomology_validator_passes"] is True
            and replay["closed_by_axiom_patch_now"] is True,
            replay,
        ),
        check(
            "SM-slot arrow values still open",
            gate["status"] == "STILL_OPEN"
            and gate["stationary_projector_source_available"] is True
            and len(gate["required_arrows"]) == 6
            and gate["failed_conditions"]["selected_sectionring_to_10M_clock_arrow"] is True
            and gate["failed_conditions"]["selected_overlap_transfer_normalization"] is True,
            gate,
        ),
        check(
            "selection decision scoped",
            decision["terminal_axiom_patch_applied"] is True
            and decision["terminal_source_unconditional_in_patched_spine"] is True
            and decision["selected_h1_Ext_packet_unconditional_in_patched_spine"] is True
            and decision["external_papers_updated_now"] is True
            and decision["selected_SMSlotFunctor_values_claimed"] is False
            and decision["can_claim_full_SM_no_knob_closure"] is False,
            decision,
        ),
        check(
            "closure/remainder accounting",
            closes["terminal_axiom_patch_applied_to_local_proof_spine"] is True
            and closes["terminal_axiom_patch_verified_in_external_corpus"] is True
            and closes["terminal_source_unconditional_in_patched_spine"] is True
            and remains["selected_sectionring_to_10M_clock_arrow"] is True
            and remains["selected_U10_Ubar5_source_outputs"] is True
            and remains["full_SM_or_no_knob_closure"] is True,
            {"closes": closes, "remains": remains},
        ),
        check(
            "no overclaim",
            data["closure_claimed"] is False
            and data["unconditional_terminal_source_claimed_in_patched_spine"] is True
            and data["unconditional_terminal_source_claimed_in_patched_corpus"] is True
            and data["selected_SMSlotFunctor_values_claimed"] is False
            and data["external_papers_modified"] is True
            and data["observed_data_used"] is False
            and data["target_fitting_used"] is False
            and cert["selected_SMSlotFunctor_values_claimed"] is False,
            cert,
        ),
        check(
            "theorem and next gate recorded",
            data["theorem"]["proved"] is True
            and data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "does not emit selected SM-slot functor values" in note,
            NOTE,
        ),
    ]

    print("\nMTT terminal axiom-patch application / SM-slot arrow audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
