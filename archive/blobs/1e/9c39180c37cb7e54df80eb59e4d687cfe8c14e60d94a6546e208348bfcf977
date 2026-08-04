"""Audit the selected Qa/SU3 monad-difference L2 source attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_monad_difference_l2_source_attempt_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_monad_difference_l2_source.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Monad_Difference_L2_Source_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_monad_difference_l2_source.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    closed = cert["closed_now"]
    open_items = cert["not_closed"]
    validation = cert["validator_comparison"]
    gate = cert["gate_result"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_MONAD_DIFFERENCE_L2_SOURCE_ATTEMPT_SUFFICIENCY_CLOSED_SELECTION_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == cert["closed_now"]
            and computed["not_closed"] == cert["not_closed"]
            and computed["gate_result"] == cert["gate_result"],
            computed["gate_result"],
        ),
        check(
            "template targets monad difference",
            template["status"] == "OPEN_SELECTED_QA_SU3_MONAD_DIFFERENCE_L2_SOURCE_REQUIRED"
            and template["target"]["ordered_difference"] == "L3_minus_K2"
            and template["target"]["L"] == [1, -2, 0]
            and template["target"]["L2"] == [2, -4, 0]
            and template["must_supply"]["typed_g_sections"] is None,
            template,
        ),
        check(
            "ordered lift and sufficiency closed",
            closed["ordered_integral_lift_candidate_found"] is True
            and closed["candidate_stronger_than_finite_mod3_qutrit"] is True
            and closed["hypothetical_selected_packet_passes_ordered_validator"] is True
            and closed["sufficiency_of_selected_monad_difference"] is True,
            closed,
        ),
        check(
            "validator comparison honest",
            validation["hypothetical_selected"]["exit_code"] == 0
            and validation["hypothetical_selected"]["status"] == "PASS"
            and validation["hypothetical_selected"]["open_items"] == []
            and validation["unselected_candidate"]["exit_code"] == 2
            and "source.selected_by_mtt is not true" in validation["unselected_candidate"]["open_items"]
            and validation["promotion_delta_only_source_and_pic0_fields"] is True,
            validation,
        ),
        check(
            "source theorem still open",
            open_items["actual_MTT_selection_of_L3_minus_K2"] is True
            and open_items["typed_monad_sections_for_source"] is True
            and open_items["Pic0_selection_or_quotient"] is True
            and open_items["same_source_D_E_dotD_Riesz_Green"] is True,
            open_items,
        ),
        check(
            "no overclaim",
            cert["guardrails"]["claims_selected_monad_difference_source_proved"] is False
            and cert["guardrails"]["claims_current_corpus_selects_L3_minus_K2"] is False
            and cert["guardrails"]["claims_printed_monad_is_whole_visible_c2_source"] is False
            and cert["guardrails"]["claims_full_SM_closure"] is False
            and gate["monad_difference_l2_source_closed"] is False
            and gate["target_fitting_used"] is False,
            {"guardrails": cert["guardrails"], "gate": gate},
        ),
        check(
            "note records exact next object",
            "Selected_Monad_Difference_L2_Source.v1" in note
            and "sufficiency theorem closed: yes" in note
            and "monad-difference L2 source closed: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 monad-difference L2 source attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
