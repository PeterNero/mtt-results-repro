"""Audit the selected Qa/SU3 color-bundle operator packet interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_color_bundle_operator_packet_interface_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_color_bundle_operator_packet.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Color_Bundle_Operator_Packet_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_color_bundle_operator_packet_interface.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    result = cert["interface_result"]
    packet = template["selected_packet"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_COLOR_BUNDLE_OPERATOR_PACKET_INTERFACE_BUILT_VALUES_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["interface_result"] == cert["interface_result"]
            and computed["remaining_open_fields"] == cert["remaining_open_fields"],
            computed["interface_result"],
        ),
        check(
            "template status open",
            template["status"] == "OPEN_SELECTED_QA_SU3_COLOR_BUNDLE_OPERATOR_PACKET_REQUIRED"
            and packet["branch_id"] is None
            and packet["operator_blocks"]["endomorphism_E"] is None,
            template["status"],
        ),
        check(
            "selected quotient rules imported",
            cert["input_status"]["p0_rule"].startswith("QA_SU3_P0")
            and cert["input_status"]["p_nonzero_rule"].startswith("QA_SU3_PNONZERO"),
            cert["input_status"],
        ),
        check(
            "finite part gate has one-of structure",
            any("requires_one_of" in gate for gate in template["promotion_gates"])
            and "one of: heat_coefficient_table, spectrum, analytic_or_reidemeister_torsion"
            in cert["remaining_open_fields"],
            template["promotion_gates"],
        ),
        check(
            "interface not determinant closure",
            result["interface_built"] is True
            and result["template_filled"] is False
            and result["determinant_computable_now"] is False
            and result["qa_su3_closed"] is False,
            result,
        ),
        check(
            "no target fitting or retired data allowed",
            result["target_fitting_used"] is False
            and "observed Qa/SU3 residual" in cert["do_not_use"]
            and "retired explicit HYM matrix entries" in cert["do_not_use"],
            cert["do_not_use"],
        ),
        check(
            "note records next fill attempt",
            "Selected_Qa_SU3_Color_Bundle_Operator_Packet_Fill_Attempt_v1" in note
            and "determinant computable now: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 color-bundle operator packet interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
