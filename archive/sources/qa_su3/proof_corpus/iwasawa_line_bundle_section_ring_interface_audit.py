"""Audit the Iwasawa line-bundle section-ring interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "iwasawa_line_bundle_section_ring_interface_certificate.json"
TEMPLATE = REPO / "certificates" / "iwasawa_line_bundle_section_ring.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Iwasawa_Line_Bundle_Section_Ring_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_iwasawa_line_bundle_section_ring_interface.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    result = cert["interface_result"]
    constant_test = cert["constant_scalar_test"]
    terms = cert["selected_source_scan"]["terms"]
    checks = [
        check("status", cert["status"] == "QA_SU3_IWASAWA_LINE_BUNDLE_SECTION_RING_INTERFACE_BUILT_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["interface_result"] == cert["interface_result"] and computed["gate_results"] == cert["gate_results"], computed["interface_result"]),
        check("template remains open", template["status"] == "OPEN_SELECTED_QA_SU3_IWASAWA_LINE_BUNDLE_SECTION_RING_REQUIRED" and template["multiplication_table"] is None, template["status"]),
        check("eleven spaces", result["required_spaces_count"] == 11 and len(cert["required_section_spaces"]) == 11, cert["required_section_spaces"]),
        check("literal constants blocked", constant_test["literal_constant_entries_can_fill_all_required_spaces"] is False and constant_test["zero_charge_spaces"] == [] and len(constant_test["nonzero_charge_spaces"]) == 11, constant_test),
        check("source lacks construction data", terms["constant_matrices"] is True and terms["generic_holomorphic_maps"] is True and terms["section_ring"] is False and terms["automorphy"] is False and terms["factor_of_automorphy"] is False and terms["rho_E"] is False, terms),
        check("no closure", result["interface_built"] is True and result["explicit_maps_constructed"] is False and result["qa_su3_closed"] is False and cert["closure_claimed"] is False, result),
        check("note records next", cert["next_required_artifact"]["name"] in note and "literal constant map route blocked: yes" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 Iwasawa line-bundle section-ring interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
