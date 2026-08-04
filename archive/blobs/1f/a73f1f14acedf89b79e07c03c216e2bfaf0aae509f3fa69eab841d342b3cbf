"""Audit BN27 source-object declaration / connection-value export interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_sourceobject_sqasU3bn27_declaration_or_connectionvalueexport.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceobject_sqasU3bn27_declaration_or_connectionvalueexport.candidate.json"
INTERFACE = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceobject_sqasU3bn27_declaration_interface.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_sourceobject_sqasU3bn27_declaration_or_connectionvalueexport_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SourceObject_SQaSU3BN27_Declaration_or_ConnectionValueExport_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEOBJECT_DECLARATION_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceObject_DeclarationInterface_Fill_or_SelectedConnectionValues_v1"


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
    interface = load(INTERFACE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("interface built", decision["source_object_declaration_interface_built"] is True and INTERFACE.exists(), decision)
    check("bare name rejected", decision["bare_source_name_rejected_as_closure"] is True and interface["source_object"]["bare_name_is_not_sufficient"] is True, interface["source_object"])
    check("required exports open", all(value is None for value in interface["source_object"]["required_exports"].values()), interface["source_object"]["required_exports"])
    check("connection interfaces open", all(value is None for route in ["typed_cech_monad", "direct_hym_or_strominger"] for value in interface["equivalent_connection_value_export"][route].values()), interface["equivalent_connection_value_export"])
    check("finite routec roots open", interface["equivalent_connection_value_export"]["finite_routec_solve"]["selected_trace_equality_to_27mode_operator"] is False and interface["equivalent_connection_value_export"]["finite_routec_solve"]["theorem_derived_selected_source_flags"] is False, interface["equivalent_connection_value_export"]["finite_routec_solve"])
    check("known values retained", interface["known_values_to_consume"]["oriented_abs_sector_product"] == 92160000 and interface["known_values_to_consume"]["oriented_abs_sector_logdet_exact"] == "log(92160000)", interface["known_values_to_consume"])
    check("no source closure", decision["direct_source_object_declaration_closed"] is False and decision["source_object_named_S_QaSU3_BN27"] is False and decision["BN27_source_identity_closed"] is False, decision)
    check("no connection closure", decision["equivalent_connection_value_export_closed"] is False and decision["finite_routec_solve_export_closed"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records interface", NEXT in note and str(INTERFACE.relative_to(ROOT)) in note and "bare_source_name_rejected_as_closure = true" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 source-object declaration/connection-export audit passed")


if __name__ == "__main__":
    main()
