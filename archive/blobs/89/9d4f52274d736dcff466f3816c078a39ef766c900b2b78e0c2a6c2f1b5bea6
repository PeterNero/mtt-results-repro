"""Audit the selected Qa/SU3 terminal monad lane selector attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_terminal_monad_lane_selector_attempt_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_terminal_monad_lane_selector.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Terminal_Monad_Lane_Selector_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_terminal_monad_lane_selector.py"


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
    gate = cert["gate_result"]
    next_obj = cert["minimal_next_object"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_TERMINAL_MONAD_LANE_SELECTOR_ATTEMPT_CONDITIONAL_UNIQUENESS_CLOSED_LANE_SELECTION_OPEN",
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
            "template targets terminal lane selector",
            template["status"] == "OPEN_SELECTED_QA_SU3_TERMINAL_MONAD_LANE_SELECTOR_REQUIRED"
            and template["conditional_uniqueness_target"]["lane"] == "terminal_monad_differences_L_i_minus_K2"
            and template["conditional_uniqueness_target"]["unique_match"] == "L3-K2"
            and template["conditional_uniqueness_target"]["L2"] == [2, -4, 0],
            template,
        ),
        check(
            "conditional uniqueness closed",
            closed["conditional_uniqueness_inside_terminal_lane"] is True
            and closed["unique_zero_central_terminal_difference"] is True
            and closed["unique_double_target_match"] is True
            and closed["dual_g3_type_identifies_same_line"] is True,
            closed,
        ),
        check(
            "typed monad route currently negative",
            closed["typed_monad_recovery_attempt_closed_negative"] is True
            and closed["spectral_fallback_identified"] is True
            and open_items["typed_sections_or_transition_data"] is True,
            {"closed": closed, "open": open_items},
        ),
        check(
            "remaining gates explicit",
            open_items["source_lane_selector_for_terminal_monad_differences"] is True
            and open_items["Pic0_selection_or_quotient"] is True
            and open_items["binding_to_Appell_Humbert_Cech_transitions"] is True
            and open_items["same_source_D_E_dotD_Riesz_Green"] is True,
            open_items,
        ),
        check(
            "next routes recorded",
            next_obj["name"] == "Selected_Terminal_Monad_Lane_or_Spectral_Galerkin_Source.v1"
            and next_obj["two_allowed_routes"][0]["id"] == "terminal_monad_lane_selector"
            and next_obj["two_allowed_routes"][1]["id"] == "non_invariant_spectral_galerkin_fallback",
            next_obj,
        ),
        check(
            "no overclaim",
            cert["guardrails"]["claims_terminal_lane_selected"] is False
            and cert["guardrails"]["claims_typed_monad_sections_recovered"] is False
            and cert["guardrails"]["claims_full_SM_closure"] is False
            and gate["terminal_monad_lane_selector_closed"] is False
            and gate["target_fitting_used"] is False,
            {"guardrails": cert["guardrails"], "gate": gate},
        ),
        check(
            "note records routes",
            "conditional uniqueness closed: yes" in note
            and "terminal monad lane selector closed: no" in note
            and "non-invariant spectral Galerkin fallback" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 terminal monad lane selector attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
