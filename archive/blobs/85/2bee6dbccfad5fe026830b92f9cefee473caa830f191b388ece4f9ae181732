"""Audit the Qa/SU3 finite selected-connection solve packet attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_finite_selected_connection_solve_packet_attempt_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_finite_selected_connection_solve_packet.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Finite_Selected_Connection_Solve_Packet_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_finite_selected_connection_solve_packet.py"


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
    attempt = cert["attempt_result"]
    gate = cert["gate_result"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_FINITE_SELECTED_CONNECTION_SOLVE_PACKET_ATTEMPT_BUILT_SELECTED_SOURCE_OPEN",
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
            "template is open and source-demanding",
            template["status"] == "OPEN_SELECTED_QA_SU3_FINITE_SELECTED_CONNECTION_SOLVE_PACKET_REQUIRED"
            and template["source_requirements"]["same_branch_as_selected_gerbe"] is True
            and template["selected_source_verified"] is False,
            template["source_requirements"],
        ),
        check(
            "honest smoke rejected",
            closed["honest_unselected_smoke_rejected_by_source_gate"] is True
            and cert["validator_results"]["current_q79_orientation_honest_unselected"]["exit_code"] == 1
            and cert["validator_results"]["conjugate_q369_orientation_honest_unselected"]["exit_code"] == 1,
            cert["validator_results"],
        ),
        check(
            "validator pipeline reachable but not selected",
            closed["algebraic_downstream_validators_are_reachable_if_source_is_selected"] is True
            and attempt["current_smoke_can_be_promoted"] is False
            and attempt["current_smoke_useful_as_validator_fixture"] is True,
            attempt,
        ),
        check(
            "remaining selected source solve is explicit",
            open_items["selected_source_verified"] is True
            and open_items["selected_visible_SM_bundle_or_sheaf_model"] is True
            and open_items["finite_rhoE_from_selected_bundle"] is True
            and open_items["same_branch_D_E_dotD_Riesz_Green"] is True,
            open_items,
        ),
        check(
            "no target fitting or false closure",
            attempt["target_fitting_used"] is False
            and attempt["uses_observed_masses_or_mixings"] is False
            and attempt["uses_execution_ii_benchmarks"] is False
            and gate["selected_connection_packet_closed"] is False
            and gate["packet_template_ready"] is True,
            {"attempt": attempt, "gate": gate},
        ),
        check(
            "note records next source solve",
            "Selected_Qa_SU3_Finite_Selected_Connection_Source_Solve_v1" in note
            and "selected connection packet closed: no" in note
            and "target fitting used: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 finite selected-connection solve packet attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
