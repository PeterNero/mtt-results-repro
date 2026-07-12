"""Audit BN27 same-source export to validators / selected connection values gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_samesourceexport_to_bn27validators_or_selectedconnectionvalues.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_samesourceexport_to_bn27validators_or_selectedconnectionvalues.candidate.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_validator_export_acceptance_contract.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_samesourceexport_to_bn27validators_or_selectedconnectionvalues_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SameSourceExport_To_BN27Validators_or_SelectedConnectionValues_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_VALIDATOR_EXPORT_CONTRACT_BUILT_SOURCE_VALUES_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_ValidatorExport_Fill_or_SelectedConnectionSolve_v1"


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
    contract = load(CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    summary = data["validator_summary"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("contract built", decision["validator_export_acceptance_contract_built"] is True and CONTRACT.exists(), decision)
    check("support ready", decision["support_ready_count"] == 6 and all(summary["support_ready"].values()), summary["support_ready"])
    check("only audit replay owned", decision["selected_export_owned_count"] == 1 and summary["currently_export_owned"]["audit_replay"] is True, summary["currently_export_owned"])
    check("five validators open", decision["open_validator_count"] == 5 and "audit_replay_validator" not in decision["open_validators"], decision["open_validators"])
    check("contract acceptance values open", all(v["acceptance_value"] is None for k, v in contract["validators"].items() if k != "audit_replay_validator"), contract["validators"])
    check("acceptable families present", set(contract["acceptable_value_families"].keys()) == {"source_identity_transport", "typed_connection_values", "direct_connection_values"}, contract["acceptable_value_families"])
    check("no export closure", decision["same_source_export_to_BN27_validators"] is False and cert["same_source_export_to_BN27_validators"] is False, decision)
    check("no selected values closure", decision["selected_connection_values_closed"] is False and cert["selected_connection_values_closed"] is False, decision)
    check("no BN27 identity", decision["BN27_source_identity_closed"] is False and decision["source_object_named_S_QaSU3_BN27"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records contract", NEXT in note and str(CONTRACT.relative_to(ROOT)) in note and "selected_export_owned_count = 1" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 same-source export/connection-values audit passed")


if __name__ == "__main__":
    main()
