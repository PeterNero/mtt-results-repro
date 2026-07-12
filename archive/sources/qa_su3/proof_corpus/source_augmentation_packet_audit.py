"""Audit the first Qa/SU3 source-augmentation packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "source_augmentation_packet_certificate.json"
DATA = REPO / "candidate_data" / "source_augmentation_packet.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Source_Augmentation_Packet_v1.md"
SCRIPT = REPO / "scripts" / "build_source_augmentation_packet.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    checks = [
        check("status", cert["status"] == "QA_SU3_SOURCE_AUGMENTATION_PACKET_SYMBOLIC_PRODUCTS_PASS_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("eleven section spaces", len(data["required_section_spaces"]) == 11, len(data["required_section_spaces"])),
        check("five products land in P", all(item["lands_in_P"] for item in data["product_tests"]), data["product_tests"]),
        check("values remain open", cert["what_remains_open"]["operator_exit"] is True and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert["what_remains_open"]),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next solver", "Selected_Qa_SU3_Automorphy_Factor_Ansatz_Constraint_Solver_v1" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 source augmentation packet audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
