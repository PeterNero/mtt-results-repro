"""Audit the Hessian/kernel central-cocycle derivation interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "hessian_kernel_central_cocycle_derivation_interface_certificate.json"
DATA = REPO / "candidate_data" / "hessian_kernel_central_cocycle_derivation_interface.candidate.json"
TEMPLATE = REPO / "certificates" / "hessian_kernel_central_cocycle_derivation.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Hessian_Kernel_Central_Cocycle_Derivation_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_hessian_kernel_central_cocycle_derivation_interface.py"
VALIDATOR = REPO / "scripts" / "validate_hessian_kernel_central_cocycle_derivation.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
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
    val = subprocess.run(
        [sys.executable, str(VALIDATOR), str(TEMPLATE)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    checks = [
        check("status", cert["status"] == "QA_SU3_HESSIAN_KERNEL_CENTRAL_COCYCLE_DERIVATION_INTERFACE_BUILT_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("validator refuses open template", val.returncode == 2 and cert["template_validator_result"]["exit_code"] == 2, val.stdout),
        check("template schema", template["schema"] == "SelectedQaSU3HessianKernelCentralCocycleDerivation.v1", template["schema"]),
        check("required objects", set(data["required_objects"]) == {"H_sel", "G_ret", "Pi_tw", "tau", "response"}, data["required_objects"]),
        check("template has required top-level groups", {"source_identity", "hessian_block", "retarded_kernel", "twist_projection", "tau_extraction", "admissibility", "response_payload", "guardrails"}.issubset(template), template.keys()),
        check("charge table includes all modules", len(template["twist_projection"]["charge_table"]) == 11, template["twist_projection"]["charge_table"]),
        check("acceptance equations carried", any("rho_E" in item for item in data["acceptance_equations"]) and any("tau(F_i)" in item for item in data["acceptance_equations"]), data["acceptance_equations"]),
        check("values open", cert["what_remains_open"]["H_sel_values"] is True and cert["what_remains_open"]["response_payload"] is True, cert["what_remains_open"]),
        check("no closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, data),
        check("note records next", data["next_required_artifact"] in note and "open template refuses to compute" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 Hessian/kernel central-cocycle derivation interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
