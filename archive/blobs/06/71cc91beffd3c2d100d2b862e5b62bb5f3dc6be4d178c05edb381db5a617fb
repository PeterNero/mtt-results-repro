"""Audit the Qa/SU3 color-bundle operator packet interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "color_bundle_operator_packet_interface_certificate.json"
DATA = REPO / "candidate_data" / "color_bundle_operator_packet_interface.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Color_Bundle_Operator_Packet_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_color_bundle_operator_packet_interface.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    result = data["interface_result"]
    template = data["packet_template"]
    checks = [
        check("status", cert["status"] == "QA_SU3_COLOR_BUNDLE_OPERATOR_PACKET_INTERFACE_BUILT_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("interface built", result["interface_built"] is True and result["template_filled"] is False, result),
        check("promotion gates", len(template["promotion_gates"]) == 6, template["promotion_gates"]),
        check("forbidden inputs", "observed Qa/SU3 residual" in template["forbidden_inputs"], template["forbidden_inputs"]),
        check("quotient imports", cert["what_closes"]["p0_and_p_nonzero_quotient_status_imported"] is True, data["external_certificates"]),
        check("operator missing", result["selected_qa_su3_operator_packet_available"] is False, result),
        check("no closure", result["qa_su3_closed"] is False and cert["closure_claimed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "endomorphism_E" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 color-bundle operator packet interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
