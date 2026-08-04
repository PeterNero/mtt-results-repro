"""Audit the Qa/SU3 gerbe-twist cancellation packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "gerbe_twist_cancellation_packet_certificate.json"
DATA = REPO / "candidate_data" / "gerbe_twist_cancellation_packet.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Gerbe_Twist_Cancellation_Packet_v1.md"
SCRIPT = REPO / "scripts" / "build_gerbe_twist_cancellation_packet.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    pairs = data["pair_results"]
    checks = [
        check("status", cert["status"] == "QA_SU3_GERBE_TWIST_CANCELLATION_SOLUTION_CANDIDATE_BUILT_SOURCE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("five products", len(pairs) == 5, len(pairs)),
        check("all products match P", all(item["product_matches_P"] for item in pairs), pairs),
        check("all c twists cancel", all(item["gerbe_twist_cancels"] for item in pairs), pairs),
        check("P is untwisted", data["P"]["gerbe_c_twist"] == 0, data["P"]),
        check("solution candidate not closure", data["solution_claim"]["solves_literal_c_nonclosed_obstruction_at_product_level"] is True and data["solution_claim"]["operator_exit_supplied"] is False, data["solution_claim"]),
        check("remaining source gates open", cert["what_remains_open"]["selected_gerbe_or_B_field_representative"] is True and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert["what_remains_open"]),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next artifact", "Selected_Qa_SU3_Twisted_Section_Ring_and_Gerbe_Source_Gate_v1" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 gerbe twist cancellation packet audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
