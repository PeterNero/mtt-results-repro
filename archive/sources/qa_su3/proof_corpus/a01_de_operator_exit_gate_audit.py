"""Audit the selected A01/D_E operator-exit gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "a01_de_operator_exit_gate_certificate.json"
DATA = REPO / "candidate_data" / "a01_de_operator_exit_gate.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_A01_DE_Operator_Exit_Gate_v1.md"
SCRIPT = REPO / "scripts" / "build_a01_de_operator_exit_gate.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    gates = data["gate_results"]
    reqs = {row["name"]: row["present_now"] for row in data["acceptance_interface"]}
    checks = [
        check("status", cert["status"] == "QA_SU3_A01_DE_OPERATOR_EXIT_ACCEPTANCE_GATE_BUILT_SELECTED_MATRICES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("eleven spaces carried", data["required_section_space_count"] == 11 and cert["what_closes"]["eleven_required_section_spaces_carried_forward"] is True, data["required_section_spaces"]),
        check("validator shapes only", gates["validator_shapes_available"] is True and cert["what_closes"]["validator_shapes_identified_as_reusable_only"] is True, gates),
        check("selected matrices open", reqs["selected_f_and_g_matrices"] is False and gates["selected_typed_matrices_supplied"] is False, reqs),
        check("operator matrix open", reqs["selected_DE_or_rhoE_matrix"] is False and gates["selected_operator_matrix_supplied"] is False, reqs),
        check("shortcuts rejected", "identity rho_E" in data["rejected_shortcuts"] and "direct q79/S3 finite torsion import" in data["rejected_shortcuts"], data["rejected_shortcuts"]),
        check("exit not promoted", gates["operator_exit_promoted"] is False and gates["all_required_operator_exit_inputs_present"] is False, gates),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next matrix packet", cert["next_required_artifact"] in note and "identity rho_E" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 A01/D_E operator-exit gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
