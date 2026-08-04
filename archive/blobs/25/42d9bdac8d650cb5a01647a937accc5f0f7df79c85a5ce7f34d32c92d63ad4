"""Audit BN27 source-object declaration-interface fill / selected-connection values gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_sourceobject_declarationinterface_fill_or_selectedconnectionvalues.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceobject_declarationinterface_fill_or_selectedconnectionvalues.candidate.json"
EXPORT_TEST = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_u1y_routec_export_compatibility_test.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_sourceobject_declarationinterface_fill_or_selectedconnectionvalues_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SourceObject_DeclarationInterface_Fill_or_SelectedConnectionValues_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEOBJECT_INTERFACE_FILL_U1Y_SUPPORT_IMPORTED_VALUES_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SameSourceExport_To_BN27Validators_or_SelectedConnectionValues_v1"


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
    export_test = load(EXPORT_TEST)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("u1y support imported", decision["u1y_routec_support_imported_for_compatibility"] is True and export_test["compatibility_support"]["selected_trace_equality_to_27mode_operator_support"] is True and export_test["compatibility_support"]["DE_gap_Riesz_Green_layer_support"] is True, export_test["compatibility_support"])
    check("full formula still open", export_test["compatibility_support"]["full_selected_iwasawa_strominger_operator_formula_support"] is False, export_test["compatibility_support"])
    check("selected connection still open", export_test["compatibility_support"]["selected_connection_witness_constructed"] is False and decision["selected_connection_values_closed"] is False, export_test["compatibility_support"])
    check("not exported to BN27", all(value is False for value in export_test["not_exported_to_BN27"].values()), export_test["not_exported_to_BN27"])
    check("finite routec export open", decision["finite_routec_solve_export_to_BN27_closed"] is False and data["route_evaluation"]["finite_routec_solve_export_to_BN27"]["closed_now"] is False, data["route_evaluation"]["finite_routec_solve_export_to_BN27"])
    check("same-source export open", decision["same_source_export_to_BN27_validators"] is False and cert["same_source_export_to_BN27_validators"] is False, decision)
    check("source object open", decision["source_object_named_S_QaSU3_BN27"] is False and cert["source_object_named_S_QaSU3_BN27"] is False, decision)
    check("no BN27 identity closure", decision["BN27_source_identity_closed"] is False and data["closure_claimed"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records export test", NEXT in note and str(EXPORT_TEST.relative_to(ROOT)) in note and "same_source_export_to_BN27_validators = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 declaration-interface fill/connection-values audit passed")


if __name__ == "__main__":
    main()
