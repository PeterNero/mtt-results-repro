"""Audit BN27 validator-export fill / selected-connection solve gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_validatorexport_fill_or_selectedconnectionsolve.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_validatorexport_fill_or_selectedconnectionsolve.candidate.json"
COLLAPSE = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_validator_dependency_collapse.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_validatorexport_fill_or_selectedconnectionsolve_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_ValidatorExport_Fill_or_SelectedConnectionSolve_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_VALIDATOR_EXPORT_FILL_REDUCED_TO_SOURCEBRANCH_OR_CONNECTIONVALUES"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceBranchIdentity_ThreeClause_Fill_or_ConnectionSolve_v1"


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
    collapse = load(COLLAPSE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("collapse built", decision["validator_dependency_collapse_built"] is True and COLLAPSE.exists(), decision)
    check("audit replay closed", decision["audit_replay_validator_closed"] is True and collapse["validator_dependencies"]["audit_replay_validator"]["unconditional_closed"] is True, collapse["validator_dependencies"]["audit_replay_validator"])
    check("operator conditional only", decision["operator_coemission_conditional_closed"] is True and collapse["validator_dependencies"]["operator_coemission_validator"]["unconditional_closed"] is False, collapse["validator_dependencies"]["operator_coemission_validator"])
    check("three clause cutset", decision["sourcebranch_required_clause_count"] == 3 and set(collapse["three_clause_sourcebranch_cutset"].keys()) == {"one_selected_source_names_both_branches", "eleven_label_to_full_BN27_threshold_carrier", "routec_row_not_external_import"}, collapse["three_clause_sourcebranch_cutset"])
    check("no clauses emitted", decision["sourcebranch_emitted_clause_count"] == 0 and all(v["emitted_by_current_source"] is False for v in data["clause_status"].values()), data["clause_status"])
    check("five validators not closed", decision["five_validator_bundle_unconditional_closed"] is False and decision["same_source_export_to_BN27_validators"] is False, decision)
    check("no selected solve closure", decision["selected_connection_solve_closed"] is False and cert["selected_connection_solve_closed"] is False, cert)
    check("no BN27 identity", decision["BN27_source_identity_closed"] is False and decision["source_object_named_S_QaSU3_BN27"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records collapse", NEXT in note and str(COLLAPSE.relative_to(ROOT)) in note and "sourcebranch_emitted_clause_count = 0" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 validator-export fill/connection-solve audit passed")


if __name__ == "__main__":
    main()
