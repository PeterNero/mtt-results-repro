"""Audit the heterotic projective rho_E finite physical quotient theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_finitephysicalquotient_sourcetheorem.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_finitephysicalquotient_sourcetheorem.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_finitephysicalquotient_sourcetheorem_certificate.json"
OBLIGATIONS = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_finitephysicalquotient_remaining_obligations.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_FinitePhysicalQuotient_SourceTheorem_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_FINITE_PHYSICAL_QUOTIENT_DOMAIN_CLOSED_RHOE_SOURCE_EMISSION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SelectedPacketEmission_or_OperatorIdentity_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    cert = load(CERT)
    obligations = load(OBLIGATIONS)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("domain closed", data["decision"]["finite_physical_quotient_domain_closed"] is True and cert["finite_physical_quotient_domain_closed"] is True, data["domain_evidence"])
    check("all domain checks true", all(data["domain_evidence"]["checks"].values()), data["domain_evidence"]["checks"])
    check("expected labels exact", data["expected_labels"] == data["domain_evidence"]["source_labels"] == data["domain_evidence"]["finite_galerkin_basis"] == data["domain_evidence"]["locked_tau_labels"], data["domain_evidence"])
    check("trace closed", data["decision"]["finite_trace_admissibility_closed"] is True and cert["finite_trace_admissibility_closed"] is True, data["trace_admissibility_evidence"])
    check("rhoE emission still open", data["decision"]["finite_rhoE_selected_packet_emission_closed"] is False and cert["finite_rhoE_selected_packet_emission_closed"] is False, data["finite_contract_flags"])
    check("only selected packet emission missing", obligations["missing"] == ["finite_rhoE_packet_selected_not_validator_only"], obligations)
    check("no closure promoted", data["closure_claimed"] is False and cert["closure_claimed"] is False, cert)
    check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert)
    check("guardrails true", all(data["guardrails"].values()), data["guardrails"])
    check("note records emission frontier", NEXT in note and "selected packet" in note, NOTE)

    print("\nSelected heterotic projective rho_E finite physical quotient source theorem audit")


if __name__ == "__main__":
    main()
