"""Audit the typed monad D_E / rho_E data interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "typed_monad_de_or_rhoe_data_interface_certificate.json"
DATA = REPO / "candidate_data" / "typed_monad_de_or_rhoe_data_interface.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Typed_Monad_DE_or_RhoE_Data_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_typed_monad_de_or_rhoe_data_interface.py"
VALIDATOR = REPO / "scripts" / "validate_typed_monad_packet.py"
TEMPLATE = REPO / "certificates" / "typed_monad_de_or_rhoe_data.template.json"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    val = subprocess.run([sys.executable, str(VALIDATOR), str(TEMPLATE)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = data["interface_result"]
    checks = [
        check("status", cert["status"] == "QA_SU3_TYPED_MONAD_DE_OR_RHOE_DATA_INTERFACE_BUILT_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("validator open exit", val.returncode == 2 and "OPEN" in val.stdout, val.stdout.strip()),
        check("interface built", result["interface_built"] is True and result["validator_built"] is True, result),
        check("packet absent", result["typed_monad_packet_available"] is False and result["de_operator_packet_available"] is False and result["rhoe_packet_available"] is False, result),
        check("requirements explicit", len(data["acceptance_interface"]["typed_monad_required"]) == 5 and len(data["acceptance_interface"]["operator_exit_required"]) == 2, data["acceptance_interface"]),
        check("no closure", result["qa_su3_closed"] is False and cert["closure_claimed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "validator exit code: 2" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 typed monad D_E or rho_E data interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
