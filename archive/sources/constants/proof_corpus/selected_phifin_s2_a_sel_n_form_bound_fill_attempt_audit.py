"""Audit Selected_PhiFin_S2_A_sel_N_Form_Bound_Fill_Attempt_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_phifin_s2_a_sel_n_form_bound_fill_attempt_certificate.json"
PACKET = REPO / "candidate_data" / "selected_phifin_s2_a_sel_n_form_bound_fill_attempt.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_PhiFin_S2_A_sel_N_Form_Bound_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_phifin_s2_a_sel_n_form_bound_fill.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = load(CERT)
    packet = load(PACKET)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    script_cert = json.loads(proc.stdout)
    route2 = packet["route_results"]["route_2_explicit_A_sel_N"]["diagnostic_27_mode_eta"]
    route3 = packet["route_results"]["route_3_form_bound"]
    closure = packet["current_closure"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "FORM_BOUND_NUMERICALLY_WITHIN_BUDGET_PROVENANCE_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "basis and small solve",
        packet["basis"]["required_basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3"
        and packet["basis"]["dimension"] == 27
        and packet["basis"]["small_solve_basis_compatible"] is False,
        packet["basis"],
    )
    ok &= check(
        "diagnostic eta computed and below threshold",
        route2["max_eta_if_provenance_were_supplied"] == 1.0
        and route2["all_sectors_pass_threshold_numerically"] is True
        and route2["all_sectors_selected_source_verified"] is False
        and route2["sector_eta"]["H"]["eta_if_treated_as_A_sel_N"] == 1.0,
        route2,
    )
    ok &= check(
        "form-bound route not promoted",
        route3["passes_threshold_if_provenance_were_supplied"] is True
        and route3["closed"] is False
        and "unpromoted" in route3["reason"],
        route3,
    )
    ok &= check(
        "closure remains honest",
        closure["diagnostic_eta_computed"] is True
        and closure["diagnostic_eta_below_threshold"] is True
        and closure["selected_A_sel_N_emitted"] is False
        and closure["selected_form_bound_emitted"] is False
        and closure["selected_gap_error_certificate_closed"] is False,
        closure,
    )
    ok &= check(
        "key finding",
        packet["key_finding"]["numerical_problem"] is False
        and packet["key_finding"]["provenance_problem"] is True,
        packet["key_finding"],
    )
    ok &= check(
        "minimal fix named",
        packet["minimal_fix_to_close"]["name"]
        == "Selected_PhiFin_S2_27_Mode_Provenance_Theorem_v1",
        packet["minimal_fix_to_close"],
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["does_not_promote_diagnostic_eta"] is True
        and cert["guardrails"]["does_not_flip_selected_source_flags"] is True
        and cert["guardrails"]["does_not_accept_small_solve_dimension_mismatch"] is True,
        cert["guardrails"],
    )
    ok &= check(
        "note records result",
        "remaining problem is provenance, not size" in note
        and "max diagnostic eta = 1.0" in note,
        NOTE,
    )

    print("\nSelected PhiFin S2 A_sel,N form-bound fill attempt audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
