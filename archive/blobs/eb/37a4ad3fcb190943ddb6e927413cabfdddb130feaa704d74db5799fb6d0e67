"""Audit heterotic Phi_fin source-identity / bundle solve gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_phifin_sourceidentity_or_bundleconnection_solve_gate.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_phifin_sourceidentity_or_bundleconnection_solve_gate.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_phifin_sourceidentity_or_bundleconnection_solve_gate_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_PhiFin_SourceIdentity_or_BundleConnection_Solve_Gate_v1.md"

STATUS = "HETEROTIC_PHIFIN_SOURCEIDENTITY_OR_BUNDLECONNECTION_SOLVE_GATE_BUILT_VALUES_OPEN"


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
    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("both gates built", data["decision"]["source_identity_gate_built"] and data["decision"]["explicit_bundle_solve_gate_built"], data["decision"])

    lane_a = data["lanes"]["A_source_identity"]
    lane_b = data["lanes"]["B_explicit_bundle_solve"]
    check("lane A open", lane_a["closes_now"] is False and data["decision"]["same_source_identity_proved"] is False, lane_a)
    check("lane A has required subclaims", "monad_EndE_to_BN_functor" in lane_a["required_subclaims"] and "D_E_trace_equality_on_QaSU3_domain" in lane_a["required_subclaims"], lane_a["required_subclaims"])
    check("lane B open", lane_b["closes_now"] is False and data["decision"]["explicit_bundle_connection_solved"] is False, lane_b)
    check("lane B has operator payload", "Weitzenbock_E_Qa_matrix" in lane_b["required_payload"] and "heat_zeta_torsion_finite_part" in lane_b["required_payload"], lane_b["required_payload"])
    check("known geometry retained", lane_b["known_geometric_inputs"]["R_plus_summary"]["nonzero_components"] > 0, lane_b["known_geometric_inputs"])

    forbidden = set(data["acceptance_kernel"]["forbidden"])
    check("forbidden shortcuts named", {"identity rho_E smoke", "standard embedding A=GammaPlus without a selector", "Chern classes alone as operator data"} <= forbidden, data["acceptance_kernel"])
    check("no closure", not data["decision"]["direct_finite_operator_emitted"] and not data["decision"]["E_Qa_computed"], data["decision"])
    check("guardrails", not any(data["guardrails"].values()), data["guardrails"])
    check("note records lanes", "Lane A" in NOTE.read_text(encoding="utf-8") and "Lane B" in NOTE.read_text(encoding="utf-8"), NOTE)
    print("\nSelected heterotic Phi_fin source-identity / bundle solve gate audit")


if __name__ == "__main__":
    main()
