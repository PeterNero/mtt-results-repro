"""Audit BN27 minimal missing source-value theorem / connection-tables gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_minimalmissingsourcevaluetheorem_or_connectiontables.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_minimalmissingsourcevaluetheorem_or_connectiontables.candidate.json"
DIRECT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_selectedsourceemission_theorem_skeleton.json"
TABLES = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_selectedconnectiontables_schema.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_minimalmissingsourcevaluetheorem_or_connectiontables_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_MinimalMissingSourceValueTheorem_or_ConnectionTables_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_MINIMAL_MISSING_THEOREM_OR_TABLES_BUILT_VALUES_STILL_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SelectedSourceEmission_or_ConnectionTables_ConstructiveAttempt_v1"


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
    direct = load(DIRECT)
    tables = load(TABLES)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("direct skeleton built", decision["direct_theorem_skeleton_built"] is True and DIRECT.exists(), decision)
    check("connection schema built", decision["connection_tables_schema_built"] is True and TABLES.exists(), decision)
    check("six direct statements", len(direct["statements"]) == 6 and decision["direct_open_statement_count"] == 6, direct["statements"])
    check("eight connection tables", len(tables["required_tables"]) == 8 and decision["connection_open_table_count"] == 8, tables["required_tables"])
    check("direct theorem open", direct["closed_now"] is False and decision["direct_theorem_closed"] is False, direct)
    check("connection tables open", tables["closed_now"] is False and decision["connection_tables_closed"] is False, tables)
    check("no source branch closure", decision["source_branch_identity_closed"] is False and decision["same_source_export_to_BN27_validators"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records schemas", NEXT in note and str(DIRECT.relative_to(ROOT)) in note and str(TABLES.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 minimal missing theorem/connection-tables audit passed")


if __name__ == "__main__":
    main()
