"""Audit BN27 selected-source-emission or connection-tables constructive attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_selectedsourceemission_or_connectiontables_constructiveattempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_selectedsourceemission_or_connectiontables_constructiveattempt.candidate.json"
MATRIX = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_selectedsourceemission_or_connectiontables_attempt_matrix.json"
REPLAY = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_if_sourceemission_then_validator_replay_dag.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_selectedsourceemission_or_connectiontables_constructiveattempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SelectedSourceEmission_or_ConnectionTables_ConstructiveAttempt_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SELECTEDSOURCEEMISSION_OR_CONNECTIONTABLES_ATTEMPT_DIRECT_THEOREM_SHORTEST_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SelectedSourceEmission_TheoremPacket_Fill_or_NoGo_v1"


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
    matrix = load(MATRIX)
    replay = load(REPLAY)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("matrix built", decision["route_matrix_built"] is True and MATRIX.exists(), decision)
    check("replay dag built", decision["conditional_replay_dag_built"] is True and REPLAY.exists(), decision)
    check("primary direct route", decision["primary_route"] == "direct_selected_source_emission_theorem" and cert["primary_route"] == decision["primary_route"], decision)
    check("direct counts", decision["direct_open_statement_count"] == 6 and matrix["direct_source_emission_route"]["open_statement_count"] == 6, matrix["direct_source_emission_route"])
    check("connection counts", decision["connection_open_table_count"] == 8 and matrix["connection_tables_route"]["open_table_count"] == 8, matrix["connection_tables_route"])
    check("conditional replay ready only", decision["conditional_replay_ready"] is True and decision["unconditional_replay_allowed"] is False, decision)
    check("replay promotes only conditionally", replay["current_status"]["conditional_replay_ready"] is True and replay["current_status"]["unconditional_replay_allowed"] is False and replay["current_status"]["oriented_logdet_promoted"] is False, replay["current_status"])
    check("replay has validators", set(replay["then_validators_close"].keys()) == {"source_identity", "BN27_deck_action", "operator_coemission", "kernel_policy", "trace_policy", "audit_replay", "not_external_import"}, replay["then_validators_close"])
    check("no closure", decision["source_branch_identity_closed"] is False and decision["same_source_export_to_BN27_validators"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records outputs", NEXT in note and str(MATRIX.relative_to(ROOT)) in note and str(REPLAY.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 selected-source-emission/connection-tables constructive attempt audit passed")


if __name__ == "__main__":
    main()
