"""Audit the MTT core axioms and measured-parameter interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "core_axioms_measured_parameter_interface_certificate.json"
DATA = REPO / "candidate_data" / "core_axioms_measured_parameter_interface.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Core_Axioms_and_Measured_Parameter_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_core_axioms_measured_parameter_interface.py"

REQUIRED_CLASSES = {
    "MEASURED_PARITY_INPUT",
    "SELECTED_SOURCE_DATA",
    "DIAGNOSTIC_FIXTURE",
    "NO_KNOB_TARGET",
}
REQUIRED_SCHEMA_FIELDS = {
    "name",
    "sector",
    "kind",
    "value_domain",
    "units",
    "convention",
    "uncertainty",
    "provenance",
    "allowed_use",
    "forbidden_use",
    "no_knob_target",
    "downstream_artifacts",
}


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    gates = data["gate_results"]
    shortcut_text = " ".join(data["forbidden_shortcuts"]).lower()
    checks = [
        check("status", cert["status"] == "MTT_CORE_AXIOMS_MEASURED_PARAMETER_INTERFACE_BUILT_SM_PARITY_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("core axioms stated", gates["core_axioms_stated"] is True and len(data["axioms"]) >= 6, data["axioms"]),
        check("measured interface defined", gates["measured_parameter_interface_defined"] is True, gates),
        check("source non-selection", gates["measured_inputs_do_not_select_sources"] is True, gates),
        check("no-knob obligation", gates["no_knob_upgrade_targets_required"] is True, gates),
        check("diagnostics excluded", gates["diagnostic_fixtures_excluded"] is True, gates),
        check("classes complete", REQUIRED_CLASSES.issubset(data["parameter_classes"].keys()), data["parameter_classes"].keys()),
        check("schema complete", REQUIRED_SCHEMA_FIELDS.issubset(set(data["slot_schema_required_fields"])), data["slot_schema_required_fields"]),
        check("forbidden source selection", "source selection" in shortcut_text and "measured" in shortcut_text, data["forbidden_shortcuts"]),
        check("forbidden target fitting", "post-hoc fitting" in shortcut_text or "target residual" in shortcut_text, data["forbidden_shortcuts"]),
        check("forbidden diagnostic fixture", "diagnostic" in shortcut_text and "physical data" in shortcut_text, data["forbidden_shortcuts"]),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", gates["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("note records policy", "SM-parity" in note and "no-knob" in note and "not\nused to select" in note, NOTE),
        check("next artifact selected", data["next_required_artifact"] == "MTT_SM_Sector_Embedding_Interface_v1", data["next_required_artifact"]),
    ]
    print("\nMTT core axioms and measured-parameter interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
