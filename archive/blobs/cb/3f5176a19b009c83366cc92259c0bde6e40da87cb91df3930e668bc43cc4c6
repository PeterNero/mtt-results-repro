"""Audit the finite cochain packet or D_E response acceptance gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "finite_cochain_packet_or_de_response_gate_certificate.json"
DATA = REPO / "candidate_data" / "finite_cochain_packet_or_de_response_gate.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Finite_Cochain_Packet_or_DE_Response_v1.md"
SCRIPT = REPO / "scripts" / "build_finite_cochain_packet_or_de_response_gate.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    gates = data["gate_results"]
    checks = [
        check("status", cert["status"] == "QA_SU3_FINITE_COCHAIN_PACKET_OR_DE_RESPONSE_GATE_BUILT_SELECTED_SOURCE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("eleven spaces", gates["eleven_spaces_carried_forward"] is True and data["required_space_count"] == 11, data["spaces"]),
        check("five products", gates["five_product_pairs_carried_forward"] is True and data["typed_product_pair_count"] == 5, data["typed_product_pairs"]),
        check("cochain lane", gates["cochain_acceptance_contract_built"] is True and len(data["finite_cochain_lane"]) == 5, data["finite_cochain_lane"]),
        check("operator lane", gates["operator_response_contract_built"] is True and len(data["operator_response_lane"]) == 5, data["operator_response_lane"]),
        check("bridge lane", gates["same_source_bridge_contract_built"] is True and len(data["bridge_checks"]) == 4, data["bridge_checks"]),
        check("response equations", "s_i = Q dotD psi_i" in note and "dotPsi_i = -R Q dotD psi_i" in note, NOTE),
        check("selected source open", gates["selected_source_promoted"] is False and cert["closure_claimed"] is False, gates),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 finite cochain packet or D_E response gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
