"""Audit the Qa/SU3 twisted section-ring and gerbe-source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_twisted_section_ring_gerbe_source_gate_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Twisted_Section_Ring_and_Gerbe_Source_Gate_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_twisted_section_ring_gerbe_source_gate.py"


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
    closes = cert["what_closes_now"]
    remains = cert["what_remains_open"]
    gate = cert["gate_result"]
    products = cert["twist_table"]["pair_products"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_TWISTED_SECTION_RING_GERBE_SOURCE_GATE_BUILT_VALUES_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["what_closes_now"] == cert["what_closes_now"]
            and computed["gate_result"] == cert["gate_result"]
            and computed["twist_table"] == cert["twist_table"],
            computed["gate_result"],
        ),
        check(
            "all twist products cancel",
            closes["all_Fi_Gi_twists_cancel_to_P"] is True
            and all(product["gerbe_twist_sum"] == 0 for product in products.values())
            and all(product["ordinary_ab_sum"] == [-1, 1] for product in products.values()),
            products,
        ),
        check(
            "literal c remains forbidden as ordinary c1",
            closes["literal_c_not_used_as_ordinary_c1"] is True,
            closes,
        ),
        check(
            "open template refuses to compute",
            cert["template_validator_result"]["exit_code"] == 2
            and "OPEN:" in cert["template_validator_result"]["output"],
            cert["template_validator_result"],
        ),
        check(
            "remaining gates are explicit",
            remains["selected_gerbe_representative"] is True
            and remains["twisted_section_bases"] is True
            and remains["operator_exit"] is True
            and remains["qa_su3_closed"] is False,
            remains,
        ),
        check(
            "no closure or fitting claimed",
            gate["typing_level_solution_preserved"] is True
            and gate["selected_packet_available"] is False
            and gate["qa_su3_closed"] is False
            and gate["target_fitting_used"] is False,
            gate,
        ),
        check(
            "note records next fill attempt",
            "Selected_Qa_SU3_Twisted_Gerbe_Source_Packet_Fill_Attempt_v1" in note
            and "Qa/SU3 closed: no" in note
            and "target fitting used: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 twisted section-ring and gerbe-source gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
