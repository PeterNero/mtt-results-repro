"""Audit the Qa/SU3 color-connection/local-system torsion interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = (
    REPO
    / "certificates"
    / "selected_qa_su3_color_connection_local_system_torsion_interface_certificate.json"
)
TEMPLATE = (
    REPO
    / "certificates"
    / "selected_qa_su3_color_connection_local_system_torsion.template.json"
)
NOTE = (
    REPO
    / "proof_corpus"
    / "Selected_Qa_SU3_Color_Connection_Local_System_Torsion_Interface_v1.md"
)
SCRIPT = (
    REPO
    / "scripts"
    / "compute_selected_qa_su3_color_connection_local_system_torsion_interface.py"
)


def check(name: str, ok: bool, detail: object) -> None:
    if not ok:
        print(f"FAIL: {name} -- {detail}")
        raise SystemExit(1)
    print(f"PASS: {name} -- {detail}")


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)

    check(
        "certificate status",
        cert["status"] == "QA_SU3_COLOR_CONNECTION_LOCAL_SYSTEM_TORSION_INTERFACE_BUILT_VALUES_OPEN",
        cert["status"],
    )
    check(
        "script agrees with certificate",
        computed["missing_template_fields"] == cert["missing_template_fields"]
        and computed["allowed_branches"] == cert["allowed_branches"],
        computed["missing_template_fields"],
    )
    check(
        "template remains open",
        template["status"] == "OPEN_SELECTED_QA_SU3_COLOR_CONNECTION_LOCAL_SYSTEM_TORSION_DATA_REQUIRED"
        and template["selected_qa_su3_operator"]["branch"] is None,
        template["selected_qa_su3_operator"],
    )
    check(
        "three legal branches exposed",
        set(cert["allowed_branches"])
        == {
            "selected_su3_color_connection_spectrum",
            "acyclic_local_system_torsion",
            "global_section_measure",
        },
        cert["allowed_branches"],
    )
    check(
        "template refuses incomplete data",
        cert["template_refuses_to_compute"] is True
        and cert["verdict"]["can_compute_numeric_response_now"] is False,
        cert["verdict"],
    )
    check(
        "no target fitting",
        cert["verdict"]["target_fitting_used"] is False
        and any("-0.19453293407759187" in rule for rule in cert["no_knob_rules"]),
        cert["no_knob_rules"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check(
        "note records fill artifact",
        "Fill_Selected_Qa_SU3_Color_Connection_or_Torsion_Template_From_Source_Data" in note
        and "acyclic_local_system_torsion" in note,
        NOTE,
    )
    print("\nSelected Qa/SU3 color-connection local-system torsion interface audit")


if __name__ == "__main__":
    main()
