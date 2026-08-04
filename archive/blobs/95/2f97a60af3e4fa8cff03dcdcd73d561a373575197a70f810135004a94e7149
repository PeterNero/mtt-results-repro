"""Audit the heterotic typed-map/projective-rhoE source fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_typedmaptables_or_projectiverhoetables_sourcefill.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_typedmaptables_or_projectiverhoetables_sourcefill.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_typedmaptables_or_projectiverhoetables_sourcefill_certificate.json"
MISSING = ROOT / "candidate_data" / "selected_heterotic_typedmaptables_or_projectiverhoetables_missing_leaves.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_TypedMapTables_or_ProjectiveRhoETables_SourceFill_v1.md"

STATUS = "HETEROTIC_TYPEDMAPTABLES_OR_PROJECTIVERHOETABLES_SOURCEFILL_NOGO_VALUES_OPEN"
NEXT = "Selected_Heterotic_SourceAmendment_or_ProjectiveRhoE_RepresentativeTables_v1"


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
    missing = load(MISSING)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("source fill attempted", data["decision"]["source_fill_attempt_executed"] is True and cert["source_fill_attempt_executed"] is True, data["decision"])
    check("no values emitted", data["decision"]["typed_map_tables_emitted"] is False and data["decision"]["projective_rhoE_tables_emitted"] is False and data["decision"]["direct_operator_exit_emitted"] is False, data["decision"])

    typed = data["lane_a_typed"]
    projective = data["lane_b_projective"]
    check("typed lane no-go", typed["verdict"] == "NO_SELECTED_TYPED_TABLES_EMITTED" and typed["value_packet_emitted"] is False, typed)
    check("projective lane no-go", projective["verdict"] == "NO_SELECTED_PROJECTIVE_RHOE_TABLES_EMITTED" and projective["value_packet_emitted"] is False, projective)
    check("typed support not value", typed["support_imported"]["monad_topology"] == "PASS_SOURCE_PRINTED" and typed["rejections"]["typed_f_g_maps"].startswith("FAIL"), typed)
    check("projective support not value", projective["support_imported"]["projective_validator_pattern_available"] is True and projective["rejections"]["projective_rhoE_tables"] is False, projective)
    check("missing packet complete", missing["status"] == "CURRENT_SOURCE_VALUES_OPEN" and len(missing["legal_minimal_repairs"]) == 3, missing)
    check("downstream blocked", cert["EndE_to_BN_functor_filled"] is False and cert["E_Qa_computed"] is False and cert["threshold_value_computed"] is False, cert)
    check("guardrails true", all(data["guardrails"].values()) and data["target_fitting_used"] is False, data["guardrails"])
    check("note records repairs", NEXT in note and "Legal Next Repairs" in note, NOTE)

    print("\nSelected heterotic typed-map/projective-rhoE source-fill audit")


if __name__ == "__main__":
    main()
