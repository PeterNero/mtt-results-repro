"""Audit oriented Phi_fin source-ownership certificate fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.candidate.json"
FILLED = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.values.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceOwnership_Certificate_FillAttempt_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEOWNERSHIP_CERTIFICATE_FILL_PARTIAL_BRANCHCERT_ONLY"
NEXT = "Selected_Heterotic_OrientedPhiFin_OrientedBN_CarrierEmission_or_EndEQuotientFunctor_v1"


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
    filled = load(FILLED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    fields = filled["filled_certificate_fields"]
    diagnostics = filled["diagnostics"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("branch certificate closed", decision["same_branch_source_certificate_closed"] is True and fields["same_branch_QaSU3_heterotic_source_certificate"]["filled"] is True, fields)
    check("support policy retained", fields["C_tau_orientation_bound_to_same_threshold_complex"]["filled"] is True and fields["kernel_zero_mode_shared_circle_policy_replayed"]["filled"] is True and fields["no_observed_data_or_residual_selector"]["filled"] is True, fields)
    check("carrier/functor still open", fields["oriented_BN_carrier_emitted_by_that_source"]["filled"] is False and fields["quotient_or_functor_EndE_or_rhoE_to_oriented_BN"]["filled"] is False, fields)
    check("rho shadow not promoted", diagnostics["rho_shadow_intertwines"] is True and diagnostics["DE_intertwines"] is False and diagnostics["same_finitepart"] is False, diagnostics)
    check("finitepart not promoted", fields["finitepart_trace_identity_consumes_nonzero_oriented_sector"]["filled"] is False and decision["oriented_logdet_promoted"] is False, fields)
    check("true value blockers open", decision["oriented_BN_carrier_emission_closed"] is False and decision["EndE_or_rhoE_to_oriented_BN_functor_closed"] is False and decision["positive_PhiFin_DE_source_ownership_closed"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records values", str(FILLED.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-ownership certificate fill-attempt audit passed")


if __name__ == "__main__":
    main()
