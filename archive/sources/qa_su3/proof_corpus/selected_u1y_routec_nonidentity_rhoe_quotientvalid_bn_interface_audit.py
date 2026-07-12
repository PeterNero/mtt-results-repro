"""Audit the non-identity rho_E / quotient-valid B_N interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn_interface.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn_interface.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn_interface_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn.template.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1.md"

STATUS = "U1Y_ROUTEC_NONIDENTITY_RHOE_QUOTIENTVALID_BN_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_FillAttempt_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS and template["status"].startswith("OPEN_"), cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("previous reduction imported", data["interface_checks"]["previous_gate_reduced_to_this_payload"] is True, data["interface_checks"]),
        check("source values open", template["source_evidence"]["selected_by_mtt"] is None and template["source_evidence"]["same_branch_q79_F_m1"] is None, template["source_evidence"]),
        check("rhoE BN values open", template["rho_E"]["nonidentity"] is None and template["B_N"]["quotient_valid"] is None, template),
        check("operator replay open", template["operator_replay"]["D_E"] is None and template["operator_replay"]["no_lifted_flags"] is None, template["operator_replay"]),
        check("correction emission open", template["correction_emission"]["A_selected"] is None and template["correction_emission"]["b_selected_or_homogeneous_zero_theorem"] is None, template["correction_emission"]),
        check("no closure", cert["closure_claimed"] is False and cert["what_remains_open"]["A_selected"] is True, cert),
        check("note records forbidden shortcuts", "diagnostic splitter as source" in note and "identity rho_E smoke payload" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C nonidentity rho_E / quotient-valid B_N interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
