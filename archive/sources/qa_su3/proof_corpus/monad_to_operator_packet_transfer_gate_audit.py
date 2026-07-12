"""Audit the monad-to-operator packet transfer gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "monad_to_operator_packet_transfer_gate_certificate.json"
DATA = REPO / "candidate_data" / "monad_to_operator_packet_transfer_gate.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Monad_to_Operator_Packet_Transfer_Gate_v1.md"
SCRIPT = REPO / "scripts" / "build_monad_to_operator_packet_transfer_gate.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    result = data["result"]
    transfer = data["packet_transfer"]
    checks = [
        check("status", cert["status"] == "QA_SU3_MONAD_TO_OPERATOR_PACKET_TRANSFER_PARTIAL_SOURCE_FOUND_OPERATOR_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("source partial pass", transfer["selected_branch_and_source_certificate"]["status"] == "PARTIAL_PASS", transfer["selected_branch_and_source_certificate"]),
        check("bundle not threshold-selected", transfer["selected_color_bundle_sheaf_or_twist"]["status"] == "CANDIDATE_PASS_NOT_SELECTED_FOR_THRESHOLD", transfer["selected_color_bundle_sheaf_or_twist"]),
        check("operator blocks open", transfer["endomorphism_E_or_heat_zero_order_block"]["status"] == "OPEN" and transfer["spectrum_heat_torsion_finite_part"]["status"] == "OPEN", transfer),
        check("result open", result["selected_source_slot_partially_filled"] is True and result["selected_threshold_representation_found"] is False, result),
        check("no determinant", result["determinant_computable_now"] is False and result["qa_su3_closed"] is False, result),
        check("guardrails", "Chern classes as substitute for endomorphism_E or determinant finite part" in data["do_not_use"], data["do_not_use"]),
        check("note records next", cert["next_required_artifact"] in note and "representation map" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 monad to operator packet transfer gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
