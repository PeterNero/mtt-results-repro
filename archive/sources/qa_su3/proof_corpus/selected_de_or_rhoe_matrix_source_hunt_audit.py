"""Audit the selected D_E/rho_E matrix source hunt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_de_or_rhoe_matrix_source_hunt_certificate.json"
DATA = REPO / "candidate_data" / "selected_de_or_rhoe_matrix_source_hunt.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Selected_DE_or_RhoE_Matrix_Source_Hunt_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_de_or_rhoe_matrix_source_hunt.py"


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
    routes = {row["route_id"]: row for row in data["route_tests"]}
    checks = [
        check("status", cert["status"] == "QA_SU3_SELECTED_DE_OR_RHOE_MATRIX_SOURCE_HUNT_DONE_SOURCE_NOT_FOUND", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("printed matrices absent", gates["printed_typed_f_g_matrices_found"] is False and gates["printed_DE_matrix_found"] is False and gates["printed_transition_rhoE_found"] is False, gates),
        check("generic flux rejected", routes["printed_flux_monad_operator"]["promotes_matrix_source"] is False and routes["printed_flux_monad_operator"]["verdict"] == "GENERIC_CONTEXT_ONLY", routes["printed_flux_monad_operator"]),
        check("typed interface values open", routes["typed_monad_interface_and_fill"]["promotes_matrix_source"] is False and routes["typed_monad_interface_and_fill"]["verdict"] == "VALIDATOR_READY_VALUES_OPEN", routes["typed_monad_interface_and_fill"]),
        check("q79 guardrail only", gates["q79_validator_patterns_found"] is True and routes["q79_projective_rhoe_transfer"]["promotes_matrix_source"] is False, routes["q79_projective_rhoe_transfer"]),
        check("heat template only", gates["coherent_heat_template_found"] is True and routes["coherent_green_heat_exit"]["promotes_matrix_source"] is False, routes["coherent_green_heat_exit"]),
        check("source not found", gates["selected_matrix_source_found"] is False and gates["qa_su3_packet_closed"] is False, gates),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records minimal packet", "Minimal Closing Packet" in note and "typed f,g matrices" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 D_E/rho_E matrix source hunt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
