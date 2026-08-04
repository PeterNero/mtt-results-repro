"""Audit terminal admissible-section axiom insertion and SM-slot functor package."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_terminaladmissible_axiominsertion_and_smslotfunctor.py"
CANDIDATE = ROOT / "candidate_data" / "terminaladmissible_axiominsertion_and_smslotfunctor.candidate.json"
CERT = ROOT / "certificates" / "terminaladmissible_axiominsertion_and_smslotfunctor_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_TerminalAdmissibleSection_AxiomInsertion_and_SelectedSMSlotFunctor_v1.md"

STATUS = "MTT_TERMINALADMISSIBLE_AXIOM_INSERTION_PACKAGE_BUILT_SMSLOTFUNCTOR_SIGNATURE_OPEN"
NEXT = "MTT_SelectedSMSlotFunctor_ValueEmission_or_AxiomPaperPatch_v1"


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
    insertion = data["insertion_package"]
    replay = data["after_insertion_replay"]
    functor = data["SM_slot_functor_signature"]
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
            "insertion package ready",
            insertion["status"] == "INSERTION_READY_NOT_APPLIED_TO_CORPUS"
            and insertion["axiom_name"] == "TerminalAdmissibleSectionSelectionAxiom"
            and len(insertion["target_papers"]) == 4
            and "observed masses" in insertion["guardrail_text"]
            and "Terminal admissible-section selection axiom" in insertion["paper_ready_insert"],
            insertion,
        ),
        check(
            "after insertion replay exact",
            replay["can_rerun_terminal_source_as_unconditional_after_insertion"] is True
            and replay["promoted_items_after_insertion"]["selected_source_label"] == "g3 / L3-K2"
            and replay["promoted_items_after_insertion"]["selected_L"] == [1, -2, 0]
            and replay["promoted_items_after_insertion"]["selected_L2"] == [2, -4, 0]
            and replay["promoted_items_after_insertion"]["ordered_source_validator_passes"] is True
            and "has not yet been inserted" in replay["why_not_replayed_now_as_unconditional"],
            replay,
        ),
        check(
            "SM-slot functor signature built",
            functor["status"] == "SIGNATURE_BUILT_VALUES_OPEN"
            and functor["domain"]["selected_terminal_source"] == "g3 / L3-K2"
            and functor["domain"]["stationary_projector_source"]["selected_projector_source_verified"] is True
            and functor["codomain"]["matter_slots"]["10_M_clock"] == ["u", "e"]
            and functor["codomain"]["matter_slots"]["1_M_Dirac_shift"] == ["nuD"]
            and len(functor["required_arrows"]) == 6,
            functor,
        ),
        check(
            "functor values still open",
            functor["support_already_closed"]["finite_q79_polarization_support"] is True
            and functor["support_already_closed"]["structural_1M_rule_available"] is True
            and functor["support_already_closed"]["stationary_projector_source_promoted"] is True
            and functor["values_not_yet_emitted"]["selected_functor_arrows"] is True,
            functor,
        ),
        check(
            "closure/remainder accounting",
            closes["axiom_insertion_package_ready"] is True
            and closes["SM_slot_functor_signature_built"] is True
            and remains["actually_insert_or_prove_terminal_axiom"] is True
            and remains["selected_SM_slot_functor_values"] is True
            and remains["selected_overlap_transfer_normalization"] is True,
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
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT terminal admissible-section axiom insertion / SM-slot functor audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
