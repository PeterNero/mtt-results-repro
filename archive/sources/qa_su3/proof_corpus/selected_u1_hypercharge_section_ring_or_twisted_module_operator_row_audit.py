"""Audit the U1/hypercharge section-ring or twisted-module operator-row gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1_hypercharge_section_ring_or_twisted_module_operator_row.py"
DATA = REPO / "candidate_data" / "selected_u1_hypercharge_section_ring_or_twisted_module_operator_row.candidate.json"
CERT = REPO / "certificates" / "selected_u1_hypercharge_section_ring_or_twisted_module_operator_row_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1_Hypercharge_Section_Ring_or_Twisted_Module_Operator_Row_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    lanes = data["lanes"]
    decision = data["decision"]

    check("status exact", data["status"] == "U1_HYPERCHARGE_SECTION_RING_OR_TWISTED_MODULE_ROW_REDUCED_SOURCE_AMENDMENT_REQUIRED", data["status"])
    check("ordinary lane blocked", lanes["ordinary_iwasawa_section_ring"]["status"] == "BLOCKED_CURRENT_SOURCE_NO_AUTOMORPHY_OR_SECTION_BASES", lanes["ordinary_iwasawa_section_ring"])
    check("twisted lane blocked", lanes["projective_gerbe_or_twisted_module"]["status"] == "BLOCKED_CURRENT_SOURCE_NO_LOCAL_SYSTEM_RESPONSE_OR_OPERATOR_ROW", lanes["projective_gerbe_or_twisted_module"])
    check("qutrit lane scoped", lanes["finite_qutrit_projector_lane"]["status"] == "CLOSED_FOR_QUOTIENT_INDEX_ONLY_NOT_OPERATOR_ROW", lanes["finite_qutrit_projector_lane"])
    check("minimal amendment specified", len(lanes["minimal_source_amendment"]["packet_fields"]) == 6, lanes["minimal_source_amendment"])
    check("decision refuses closure", decision["section_ring_or_twisted_module_operator_row_found"] is False and decision["lambda_12_closed"] is False and decision["target_fitting_used"] is False, decision)
    check("certificate agrees", cert["closed"]["minimal_source_amendment_packet_specified"] is True and cert["open"]["u1_y_operator_row"] is True, cert)
    check("note records index-only guardrail", "CLOSED_FOR_QUOTIENT_INDEX_ONLY_NOT_OPERATOR_ROW" in note and "local determinant operator" in note, NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
