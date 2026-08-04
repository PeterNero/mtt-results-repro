"""Audit direct operator payload fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_directoperatorpayload_fillattempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_directoperatorpayload_fillattempt.candidate.json"
PAYLOAD = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_direct_finite_internal_operator_payload.json"
BOUNDARY = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_direct_operator_payload_physical_boundary.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_directoperatorpayload_fillattempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_DirectOperatorPayload_FillAttempt_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_DIRECT_FINITE_INTERNAL_OPERATOR_PAYLOAD_CLOSED_PHYSICAL_SMOOTH_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_DirectOperatorPayload_PhysicalBoundary_or_SmoothIdentity_v1"


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
    payload = load(PAYLOAD)
    boundary = load(BOUNDARY)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and payload["status"] == "FINITE_INTERNAL_DIRECT_OPERATOR_PAYLOAD_FILLED", (data["status"], cert["status"], payload["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and boundary["next_required_artifact"] == NEXT, decision)
    check("all acceptance fields filled", decision["all_acceptance_fields_filled_at_finite_internal_scope"] is True and all(data["filled_acceptance_fields"].values()), data["filled_acceptance_fields"])
    check("finite payload closed", decision["direct_finite_internal_operator_payload_closed"] is True and cert["direct_finite_internal_operator_payload_closed"] is True, decision)
    check("selected domain", payload["operator_domain_or_finite_quotient_domain"]["labels"] == ["F1", "F2", "F3", "F4", "F5", "G1", "G2", "G3", "G4", "G5", "P"], payload["operator_domain_or_finite_quotient_domain"])
    check("operator tables", len(payload["rho_E_or_D_E_operator_tables"]["D_E_diagonal_matrix_on_labels"]) == 11 and len(payload["rho_E_or_D_E_operator_tables"]["rho_E_central_character"]) == 11, payload["rho_E_or_D_E_operator_tables"])
    check("self adjoint/unitary", all(payload["self_adjoint_or_unitary_structure"].values()), payload["self_adjoint_or_unitary_structure"])
    check("logdet finite part", payload["spectrum_or_logdet_finite_part"]["determinant"] == 2008 and payload["spectrum_or_logdet_finite_part"]["finite_internal_part"] == "log(2008)", payload["spectrum_or_logdet_finite_part"])
    check("trace normalization", payload["trace_normalization"]["chi_Qa"] == "1" and payload["trace_normalization"]["finite_trace"]["finite_trace_tau_squared"] == 8, payload["trace_normalization"])
    check("identity map to packet", payload["map_to_selected_internal_packet"]["identity_on_selected_packet"] is True, payload["map_to_selected_internal_packet"])
    check("no GR double count", payload["proof_no_smooth_GR_double_count"]["GR_smooth_surface_routed_to_GR_sector"] is True and payload["proof_no_smooth_GR_double_count"]["internal_payload_does_not_append_smooth_complement"] is True, payload["proof_no_smooth_GR_double_count"])
    check("boundary open", boundary["closed"]["direct_finite_internal_operator_payload"] is True and all(boundary["not_closed"].values()), boundary)
    check("no smooth/physical overclaim", decision["smooth_operator_identity_closed"] is False and decision["physical_threshold_normalization_closed"] is False and data["closure_claimed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records payload and boundary", str(PAYLOAD.relative_to(ROOT)) in note and str(BOUNDARY.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic projective rho_E direct operator payload fill audit")


if __name__ == "__main__":
    main()
