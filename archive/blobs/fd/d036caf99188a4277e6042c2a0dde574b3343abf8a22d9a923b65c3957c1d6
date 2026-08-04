"""Audit the Iwasawa line-bundle section-ring interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_iwasawa_line_bundle_section_ring_interface_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_iwasawa_line_bundle_section_ring.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Iwasawa_Line_Bundle_Section_Ring_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_iwasawa_line_bundle_section_ring_interface.py"


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
    constant_test = cert["constant_scalar_test"]
    terms = cert["selected_source_scan"]["terms"]
    gates = cert["gate_results"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_IWASAWA_LINE_BUNDLE_SECTION_RING_INTERFACE_BUILT_VALUES_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["interface_result"] == cert["interface_result"]
            and computed["constant_scalar_test"] == cert["constant_scalar_test"]
            and computed["gate_results"] == cert["gate_results"],
            computed["interface_result"],
        ),
        check(
            "template remains open",
            template["status"] == "OPEN_SELECTED_QA_SU3_IWASAWA_LINE_BUNDLE_SECTION_RING_REQUIRED"
            and template["multiplication_table"] is None
            and template["constant_frame_rule"] is None,
            template["status"],
        ),
        check(
            "eleven required spaces",
            result["required_spaces_count"] == 11
            and len(cert["required_section_spaces"]) == 11
            and constant_test["required_spaces"] == 11,
            cert["required_section_spaces"],
        ),
        check(
            "literal constants blocked by nonzero charges",
            constant_test["literal_constant_entries_can_fill_all_required_spaces"] is False
            and constant_test["zero_charge_spaces"] == []
            and len(constant_test["nonzero_charge_spaces"]) == 11
            and gates["literal_constant_scalar_interpretation"] == "FAIL_LITERAL_CONSTANT_ENTRIES_HAVE_WRONG_CHARGE",
            constant_test,
        ),
        check(
            "source has generic constants but no construction data",
            terms["constant_matrices"] is True
            and terms["generic_holomorphic_maps"] is True
            and terms["section_ring"] is False
            and terms["automorphy"] is False
            and terms["factor_of_automorphy"] is False
            and terms["rho_E"] is False,
            terms,
        ),
        check(
            "no closure claimed",
            result["interface_built"] is True
            and result["literal_constant_map_route_blocked"] is True
            and result["selected_source_has_section_construction_data"] is False
            and result["explicit_maps_constructed"] is False
            and result["qa_su3_closed"] is False
            and result["target_fitting_used"] is False,
            result,
        ),
        check(
            "note records automorphy next",
            "Selected_Qa_SU3_Iwasawa_Automorphy_or_Section_Ring_Construction_v1" in note
            and "literal constant map route blocked: yes" in note
            and "selected source has section construction data: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 Iwasawa line-bundle section-ring interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
