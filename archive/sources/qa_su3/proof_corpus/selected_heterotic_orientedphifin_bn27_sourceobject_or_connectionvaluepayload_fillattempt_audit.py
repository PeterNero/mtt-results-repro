"""Audit BN27 source-object or connection-value payload fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_sourceobject_or_connectionvaluepayload_fillattempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceobject_or_connectionvaluepayload_fillattempt.candidate.json"
PROBE = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceobject_or_connectionvaluepayload_support_probe.json"
MISSING = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_minimal_missing_source_value_theorem.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_sourceobject_or_connectionvaluepayload_fillattempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SourceObject_or_ConnectionValuePayload_FillAttempt_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEOBJECT_OR_CONNECTIONVALUEPAYLOAD_FILL_SUPPORT_ONLY_SOURCE_VALUES_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_MinimalMissingSourceValueTheorem_or_ConnectionTables_v1"


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
    probe = load(PROBE)
    missing = load(MISSING)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("source probe count", decision["source_support_fields_probed"] == 11 and len(probe["source_support_probe"]) == 11, probe["source_support_probe"])
    check("connection probe count", decision["connection_support_fields_probed"] == 8 and len(probe["connection_support_probe"]) == 8, probe["connection_support_probe"])
    check("no source values filled", decision["source_object_filled_field_count"] == 0 and probe["source_value_filled_count"] == 0, decision)
    check("no connection values filled", decision["connection_values_filled_field_count"] == 0 and probe["connection_value_filled_count"] == 0, decision)
    check("every probed source field support only", all(item["source_value_filled"] is False for item in probe["source_support_probe"].values()), probe["source_support_probe"])
    check("every probed connection field support only", all(item["source_value_filled"] is False for item in probe["connection_support_probe"].values()), probe["connection_support_probe"])
    check("minimal theorem built", decision["minimal_missing_theorem_built"] is True and MISSING.exists(), missing)
    check("minimal direct theorem has 11 fields", len(missing["minimal_direct_theorem"]["would_fill_source_fields"]) == 11, missing["minimal_direct_theorem"])
    check("minimal connection theorem has 8 fields", len(missing["minimal_constructive_alternative"]["would_fill_connection_fields"]) == 8, missing["minimal_constructive_alternative"])
    check("no closure", decision["source_branch_identity_closed"] is False and decision["same_source_export_to_BN27_validators"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records missing theorem", NEXT in note and str(MISSING.relative_to(ROOT)) in note and "source_object_filled_field_count = 0" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 source-object/connection-value fill attempt audit passed")


if __name__ == "__main__":
    main()
