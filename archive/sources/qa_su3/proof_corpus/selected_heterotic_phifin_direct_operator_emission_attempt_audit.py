"""Audit heterotic Phi_fin direct operator emission attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_phifin_direct_operator_emission_attempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_phifin_direct_operator_emission_attempt.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_phifin_direct_operator_emission_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_PhiFin_DirectOperatorEmission_Attempt_v1.md"

STATUS = "HETEROTIC_PHIFIN_DIRECT_OPERATOR_EMISSION_ATTEMPT_PARTIAL_GAP_IMPORT_SOURCE_IDENTITY_OPEN"


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
    check("shape scaffold imported", data["decision"]["operator_shape_scaffold_imported"] is True and cert["operator_shape_scaffold_imported"] is True, data["decision"])
    check("gap support imported", data["decision"]["D_E_Riesz_Green_gap_support_imported"] is True and cert["D_E_Riesz_Green_gap_support_imported"] is True, data["decision"])

    compat = data["branch_compatibility"]
    check("source identity open", compat["same_source_identity_proved"] is False and data["decision"]["heterotic_QaSU3_source_identity_proved"] is False, compat)
    check("heterotic source named", "rank-three Iwasawa" in compat["heterotic_selected_source"], compat)
    check("import source named", "U1/Y Route-C" in compat["imported_gap_source"], compat)

    payload = data["attempted_payload"]
    check("DE support not promoted", payload["D_E_action"]["filled_for_imported_gap_layer"] is True and payload["D_E_action"]["promoted_to_heterotic_QaSU3"] is False, payload["D_E_action"])
    check("Riesz/Green support not promoted", payload["Riesz_projectors_and_gap"]["filled_for_imported_gap_layer"] is True and payload["reduced_Green"]["promoted_to_heterotic_QaSU3"] is False, payload)
    check("zero order open", payload["Weitzenbock_E_Qa_or_finite_zero_order_block"]["filled"] is False, payload["Weitzenbock_E_Qa_or_finite_zero_order_block"])
    check("finite part open", payload["finite_heat_zeta_torsion_determinant"]["filled"] is False, payload["finite_heat_zeta_torsion_determinant"])

    fields = data["field_status"]
    check("field status honest", fields["D_E_action_shape_support"] and not fields["D_E_action_promoted_to_heterotic"] and not fields["source_identity"], fields)
    check("no closure", data["decision"]["direct_finite_operator_emitted"] is False and data["decision"]["E_Qa_computed"] is False, data["decision"])
    check("guardrails", not any(data["guardrails"].values()), data["guardrails"])
    check("note records next proof object", "same-source identity" in NOTE.read_text(encoding="utf-8"), NOTE)

    print("\nSelected heterotic Phi_fin direct operator emission attempt audit")


if __name__ == "__main__":
    main()
