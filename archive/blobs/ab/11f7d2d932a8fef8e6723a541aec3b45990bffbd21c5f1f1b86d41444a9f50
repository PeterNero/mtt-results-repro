"""Audit the typed monad D_E / rho_E data interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_typed_monad_de_or_rhoe_data_interface_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Typed_Monad_DE_or_RhoE_Data_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_typed_monad_de_or_rhoe_data_interface.py"
VALIDATOR = REPO / "scripts" / "validate_selected_qa_su3_typed_monad_packet.py"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_typed_monad_de_or_rhoe_data.template.json"


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
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    validator_proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(TEMPLATE)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    result = cert["interface_result"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_TYPED_MONAD_DE_OR_RHOE_DATA_INTERFACE_BUILT_VALUES_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["interface_result"] == cert["interface_result"]
            and computed["acceptance_interface"] == cert["acceptance_interface"],
            computed["interface_result"],
        ),
        check(
            "template is open and forbids residual fitting",
            template["status"] == "OPEN_SELECTED_QA_SU3_TYPED_MONAD_DE_OR_RHOE_DATA_REQUIRED"
            and template["selected_branch"]["target_residual_used"] is False
            and "observed Qa/SU3 residual" in template["forbidden_inputs"],
            template["status"],
        ),
        check(
            "validator returns open on template",
            validator_proc.returncode == 2 and "OPEN:" in validator_proc.stdout,
            validator_proc.stdout,
        ),
        check(
            "typed monad requirements present",
            "machine-checkable g*f=0" in cert["acceptance_interface"]["typed_monad_required"]
            and "locally-free/stability/HYM source certificate"
            in cert["acceptance_interface"]["typed_monad_required"],
            cert["acceptance_interface"]["typed_monad_required"],
        ),
        check(
            "operator exits require D_E or rhoE",
            any("D_E packet" in item for item in cert["acceptance_interface"]["operator_exit_required"])
            and any("rho_E packet" in item for item in cert["acceptance_interface"]["operator_exit_required"]),
            cert["acceptance_interface"]["operator_exit_required"],
        ),
        check(
            "no closure claimed",
            result["operator_packet_fillable_now"] is False
            and result["determinant_computable_now"] is False
            and result["qa_su3_closed"] is False
            and result["target_fitting_used"] is False,
            result,
        ),
        check(
            "note records fill attempt next",
            "Selected_Qa_SU3_Typed_Monad_Data_Fill_Attempt_v1" in note
            and "Qa/SU3 closed: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 typed monad D_E/rho_E data interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
