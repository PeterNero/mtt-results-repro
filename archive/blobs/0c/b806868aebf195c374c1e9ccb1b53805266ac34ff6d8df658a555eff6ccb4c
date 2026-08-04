"""Audit the selected Qa/SU3 finite selected-connection source solve attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_finite_selected_connection_source_solve_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Finite_Selected_Connection_Source_Solve_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_finite_selected_connection_source_solve.py"


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
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    closed = cert["closed_now"]
    open_items = cert["not_closed"]
    gate = cert["gate_result"]
    attempts = cert["attempts"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_SELECTED_CONNECTION_SOURCE_SOLVE_ATTEMPT_BLOCKED_BY_SELECTED_OPERATOR_SOURCE",
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
            "projective mesh validated",
            closed["projective_qutrit_mesh_validated"] is True
            and cert["projective_validator_result"]["exit_code"] == 0
            and cert["projective_validator_result"]["projective_report"]["central_twist_is_nontrivial"] is True,
            cert["projective_validator_result"]["projective_report"],
        ),
        check(
            "block architecture and curvature available",
            closed["block_factorized_family_higgs_architecture_validated"] is True
            and closed["visible_green_schwarz_curvature_available"] is True
            and attempts["block_factorized_family_plus_higgs"]["can_close_selected_source"] is False,
            closed,
        ),
        check(
            "all tested routes fail only as selected source proof",
            attempts["ordinary_route_c_smoke"]["can_close_selected_source"] is False
            and attempts["projective_qutrit_gerbe_rhoE"]["can_close_selected_source"] is False
            and attempts["visible_green_schwarz_curvature_route"]["can_close_selected_source"] is False,
            attempts,
        ),
        check(
            "selected operator source remains the minimal obstruction",
            open_items["selected_visible_operator_source_packet"] is True
            and open_items["selected_visible_SM_bundle_or_sheaf_model"] is True
            and open_items["selected_D_E_dotD_Riesz_Green"] is True
            and cert["minimal_obstruction"]["name"] == "selected_visible_operator_source_packet",
            open_items,
        ),
        check(
            "no false selected-source claim",
            cert["guardrails"]["claims_selected_source_solved"] is False
            and cert["guardrails"]["claims_selected_D_E_constructed"] is False
            and cert["guardrails"]["uses_observed_masses_or_mixings"] is False
            and gate["selected_connection_source_solved"] is False
            and gate["all_current_non_source_blockers_reduced"] is True,
            {"guardrails": cert["guardrails"], "gate": gate},
        ),
        check(
            "note records the minimal obstruction",
            "selected visible operator-source packet" in note
            and "selected connection source solved: no" in note
            and "target fitting used: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 finite selected-connection source solve attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
