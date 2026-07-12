"""Audit the selected Qa/SU3 visible L2 orientation source attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_visible_l2_orientation_source_attempt_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_visible_l2_orientation_source.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Visible_L2_Orientation_Source_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_visible_l2_orientation_source.py"


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
    validation = cert["ordered_source_validation"]
    gate = cert["gate_result"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_VISIBLE_L2_ORIENTATION_SOURCE_ATTEMPT_REDUCED_TO_ORDERED_SOURCE_PACKET",
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
            "template targets ordered source",
            template["status"] == "OPEN_SELECTED_QA_SU3_VISIBLE_L2_ORIENTATION_SOURCE_REQUIRED"
            and template["target_ordered_matrix"]["L"] == [1, -2, 0]
            and template["must_supply"]["base_swap_broken_by_source"] is None
            and template["must_supply"]["pic0_resolution_rule"] is None,
            template,
        ),
        check(
            "shortcuts ruled out",
            closed["finite_qutrit_orientation_insufficient"] is True
            and closed["equal_radius_import_rejected"] is True
            and closed["current_appell_humbert_attempt_refused_honestly"] is True,
            closed,
        ),
        check(
            "ordered validator open items exact",
            validation["current_attempt_exit_code"] == 2
            and validation["current_attempt_status"] == "OPEN"
            and "source.selected_by_mtt is not true" in validation["current_attempt_open_items"]
            and "selection evidence missing: base_swap_broken_by_source"
            in validation["current_attempt_open_items"]
            and "Pic0 character not selected or quotiented" in validation["current_attempt_open_items"],
            validation,
        ),
        check(
            "remaining gate is selected ordered packet",
            open_items["selected_source_status"] is True
            and open_items["base_factor_order_selected"] is True
            and open_items["base_swap_broken_by_source"] is True
            and open_items["Pic0_resolution"] is True
            and gate["remaining_gate_is_ordered_selected_source_packet"] is True,
            {"open": open_items, "gate": gate},
        ),
        check(
            "no overclaim",
            cert["guardrails"]["claims_orientation_source_closed"] is False
            and cert["guardrails"]["claims_target_wall_selected"] is False
            and cert["guardrails"]["claims_finite_qutrit_selects_integer_branch"] is False
            and cert["guardrails"]["claims_full_SM_closure"] is False
            and gate["target_fitting_used"] is False,
            {"guardrails": cert["guardrails"], "gate": gate},
        ),
        check(
            "note records machine-checkable next object",
            "visible_rank2_l2_ordered_source.selected.json" in note
            and "visible L2 orientation source closed: no" in note
            and "orientation gap machine-checkable: yes" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 visible L2 orientation source attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
