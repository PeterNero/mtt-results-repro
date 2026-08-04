"""Audit the Qa/SU3 color-bundle/global-section determinant gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = (
    REPO
    / "certificates"
    / "selected_qa_su3_color_bundle_connection_or_global_section_determinant_certificate.json"
)
NOTE = (
    REPO
    / "proof_corpus"
    / "Selected_Qa_SU3_Color_Bundle_Connection_or_Global_Section_Determinant_v1.md"
)
SCRIPT = (
    REPO
    / "scripts"
    / "compute_selected_qa_su3_color_bundle_connection_or_global_section_determinant.py"
)


def check(name: str, ok: bool, detail: object) -> None:
    if not ok:
        print(f"FAIL: {name} -- {detail}")
        raise SystemExit(1)
    print(f"PASS: {name} -- {detail}")


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
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
        cert["status"] == "QA_SU3_COLOR_BUNDLE_OR_GLOBAL_SECTION_DETERMINANT_REDUCED_VALUES_OPEN",
        cert["status"],
    )
    check(
        "script agrees with certificate",
        computed["ranking"] == cert["ranking"]
        and computed["input_obstruction"] == cert["input_obstruction"],
        computed["ranking"],
    )
    checks = cert["source_checks"]
    check(
        "source structures present",
        all(item["present"] for item in checks.values()),
        checks,
    )
    exhausted = cert["prior_exhausted_inputs"]
    check(
        "double counts rejected",
        exhausted["canonical_nil_tangent_weitzenbock"]["may_be_added_again"] is False
        and exhausted["local_fp_brs_quotient"]["may_be_reused_as_extra"] is False,
        exhausted,
    )
    routes = cert["determinant_routes"]
    check(
        "best route remains selected connection",
        cert["ranking"]["best_next_computation"] == "selected_su3_color_connection"
        and routes["selected_su3_color_connection"]["status"]
        == "OPEN_SELECTED_CONNECTION_AND_SPECTRUM_REQUIRED",
        routes["selected_su3_color_connection"],
    )
    check(
        "no numeric closure overclaimed",
        cert["verdict"]["new_numeric_closure"] is False
        and cert["verdict"]["target_fitting_used"] is False
        and cert["verdict"]["full_SM_closure_achieved"] is False,
        cert["verdict"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check(
        "note records torsion interface next",
        "Selected_Qa_SU3_Color_Connection_Local_System_Torsion_Interface_v1" in note
        and "D_Qa,color" in note,
        NOTE,
    )
    print("\nSelected Qa/SU3 color-bundle/global-section determinant audit")


if __name__ == "__main__":
    main()
