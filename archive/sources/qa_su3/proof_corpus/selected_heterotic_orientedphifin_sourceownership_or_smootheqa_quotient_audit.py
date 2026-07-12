"""Audit oriented Phi_fin source-ownership / smooth-EQa quotient attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourceownership_or_smootheqa_quotient.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceownership_or_smootheqa_quotient.candidate.json"
REQUEST = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceownership_minimal_certificate_request.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourceownership_or_smootheqa_quotient_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceOwnership_Theorem_or_SmoothEQa_Quotient_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEOWNERSHIP_ATTEMPT_CURRENT_SOURCE_NOGO_CERTIFICATE_REQUEST_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceOwnership_Certificate_FillAttempt_v1"


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
    request = load(REQUEST)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    lane_a = data["lanes"]["source_ownership_theorem"]
    lane_b = data["lanes"]["smooth_EQa_quotient_theorem"]
    fields = request["required_certificate_fields"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("payload readiness retained", decision["operator_payload_ready_retained"] is True and cert["operator_payload_ready_retained"] is True, decision)
    check("lane A attempted but open", lane_a["attempted"] is True and lane_a["closes_now"] is False and lane_a["blocking_facts"]["dimension_mismatch_11_to_27_without_functor"] is True, lane_a)
    check("lane B attempted but open", lane_b["attempted"] is True and lane_b["closes_now"] is False and lane_b["blocking_facts"]["smooth_EQa_or_heat_zeta_torsion_finite_part"] is False, lane_b)
    check("certificate request built", decision["minimal_certificate_request_built"] is True and request["status"] == "VALUES_REQUIRED", request)
    check("critical fields open", fields["same_branch_QaSU3_heterotic_source_certificate"] is False and fields["quotient_or_functor_EndE_or_rhoE_to_oriented_BN"] is False and fields["finitepart_trace_identity_consumes_nonzero_oriented_sector"] is False, fields)
    check("support fields retained", fields["C_tau_orientation_bound_to_same_threshold_complex"] is True and fields["kernel_zero_mode_shared_circle_policy_replayed"] is True and fields["no_observed_data_or_residual_selector"] is True, fields)
    check("no promotion", decision["source_ownership_closed"] is False and decision["smooth_EQa_quotient_closed"] is False and decision["oriented_logdet_promoted"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records request", str(REQUEST.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-ownership/smooth-EQa quotient audit passed")


if __name__ == "__main__":
    main()
