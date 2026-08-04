"""Audit the selected Qa/SU3 color-bundle operator packet fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_color_bundle_operator_packet_fill_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Color_Bundle_Operator_Packet_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_fill_selected_qa_su3_color_bundle_operator_packet.py"


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
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    fill = cert["fill_result"]
    gates = cert["gate_results"]
    packet = cert["partial_packet"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_COLOR_BUNDLE_OPERATOR_PACKET_FILL_ATTEMPT_PARTIAL_SOURCE_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["fill_result"] == cert["fill_result"]
            and computed["gate_results"] == cert["gate_results"],
            computed["fill_result"],
        ),
        check(
            "domain constraints imported",
            fill["domain_constraints_imported"] is True
            and gates["domain_compatibility"] == "PARTIAL_IMPORTED_QA_QUOTIENT_DOMAIN",
            gates,
        ),
        check(
            "Strominger templates found but not promoted",
            fill["strominger_hym_templates_found"] is True
            and fill["same_branch_qa_su3_source_found"] is False
            and gates["source_selection"].startswith("FAIL"),
            {"fill": fill, "gates": gates},
        ),
        check(
            "operator and finite-part gates remain blocked",
            gates["operator_data"].startswith("FAIL")
            and gates["finite_part_data"].startswith("FAIL")
            and packet["operator_blocks"]["endomorphism_E"] is None
            and packet["operator_blocks"]["spectrum"] is None,
            packet["operator_blocks"],
        ),
        check(
            "no determinant closure",
            cert["computed_numeric_response"] is None
            and fill["determinant_computable_now"] is False
            and fill["qa_su3_closed"] is False
            and fill["full_sm_closure_achieved"] is False,
            fill,
        ),
        check(
            "no forbidden source used",
            fill["target_fitting_used"] is False
            and fill["retired_hym_matrix_used"] is False
            and packet["connection_or_residual"]["retired_hym_matrix_used"] is False,
            cert["do_not_use"],
        ),
        check(
            "note records next source packet search",
            "Selected_Qa_SU3_Strominger_HYM_Source_Packet_Search_v1" in note
            and "domain constraints imported: yes" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 color-bundle operator packet fill attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
