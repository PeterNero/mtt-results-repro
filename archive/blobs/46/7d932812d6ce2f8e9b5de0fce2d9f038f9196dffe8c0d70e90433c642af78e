"""Audit the Qa/SU3 color-connection template fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = (
    REPO
    / "certificates"
    / "selected_qa_su3_color_connection_template_fill_attempt_certificate.json"
)
TEMPLATE = (
    REPO
    / "certificates"
    / "selected_qa_su3_color_connection_local_system_torsion.template.json"
)
NOTE = (
    REPO
    / "proof_corpus"
    / "Selected_Qa_SU3_Color_Connection_Template_Fill_Attempt_v1.md"
)
SCRIPT = REPO / "scripts" / "attempt_fill_selected_qa_su3_color_connection_or_torsion_template.py"


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
        cert["status"] == "QA_SU3_COLOR_CONNECTION_TEMPLATE_FILL_ATTEMPT_BLOCKED_SPECTRUM_OPEN",
        cert["status"],
    )
    check(
        "script agrees with certificate",
        computed["remaining_blockers"] == cert["remaining_blockers"]
        and computed["partial_fill"]["branch"] == cert["partial_fill"]["branch"],
        computed["remaining_blockers"],
    )
    check(
        "template intentionally remains open",
        template["selected_qa_su3_operator"]["branch"] is None
        and cert["template_filled"] is False,
        template["selected_qa_su3_operator"],
    )
    check(
        "partial color connection candidate found",
        cert["verdict"]["source_selected_color_connection_candidate_found"] is True
        and cert["partial_fill"]["color_bundle"]["bundle_or_local_system"]["selected_candidate"]
        == "indecomposable rank-3 SU(3) HYM bundle E on Iwasawa",
        cert["partial_fill"]["color_bundle"]["bundle_or_local_system"],
    )
    check(
        "no determinant values overclaimed",
        cert["computed_numeric_response"] is None
        and cert["verdict"]["selected_numeric_determinant_available"] is False
        and cert["verdict"]["can_close_Qa_SU3_now"] is False,
        cert["verdict"],
    )
    check(
        "no target fitting",
        cert["verdict"]["target_fitting_used"] is False,
        cert["verdict"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check(
        "note records next computation",
        "Selected_Qa_SU3_HYM_Color_Connection_Spectrum_or_Torsion_Computation_v1" in note
        and "spectrum_modes = null" in note,
        NOTE,
    )
    print("\nSelected Qa/SU3 color-connection template fill attempt audit")


if __name__ == "__main__":
    main()
