"""Audit the Qa/SU3 Chern-Bianchi source-packet candidate table."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_chern_bianchi_source_packet_candidates_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Chern_Bianchi_Source_Packet_Candidates_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_chern_bianchi_source_packet_candidates.py"


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


def by_id(cert: dict, candidate_id: str) -> dict:
    for item in cert["candidate_packets"]:
        if item["id"] == candidate_id:
            return item
    raise AssertionError(candidate_id)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    result = cert["result"]
    best = by_id(cert, "iwasawa_abelian_two_line_flux_row")
    rhoe = by_id(cert, "iwasawa_rhoE_validator_route")

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_CHERN_BIANCHI_SOURCE_PACKET_CANDIDATES_BUILT_NO_SELECTED_SOURCE",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["result"] == cert["result"]
            and computed["best_current_candidate"] == cert["best_current_candidate"],
            computed["result"],
        ),
        check(
            "candidate table built with Chern/Bianchi row",
            result["candidate_table_built"] is True
            and result["chern_bianchi_row_found"] is True
            and best["passes"]["invariant_componentwise_bianchi_shape"] is True,
            best,
        ),
        check(
            "best row not overpromoted",
            best["source_selected_for_qa_su3_color_threshold"] is False
            and best["passes"]["selected_su3_color_bundle"] is False
            and best["passes"]["endomorphism_E"] is False,
            best["passes"],
        ),
        check(
            "rhoE route is validator not source",
            rhoe["status"] == "VALIDATOR_AVAILABLE_CANDIDATE_UNSELECTED"
            and rhoe["passes"]["validator_exists"] is True
            and rhoe["passes"]["candidate_transition_data"] is False,
            rhoe,
        ),
        check(
            "no determinant closure",
            result["selected_qa_su3_source_found"] is False
            and result["selected_endomorphism_E_found"] is False
            and result["determinant_computable_now"] is False
            and result["qa_su3_closed"] is False,
            result,
        ),
        check(
            "guardrails recorded",
            "Iwasawa abelian commutant flux row as selected SU3 color determinant" in cert["do_not_use"]
            and "target residual to choose Chern/Bianchi candidate" in cert["do_not_use"],
            cert["do_not_use"],
        ),
        check(
            "note records next promotion gate",
            "Selected_Qa_SU3_Iwasawa_Abelian_Row_to_Nonabelian_Source_Gate_v1" in note
            and "selected Qa/SU3 source found: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 Chern-Bianchi source-packet candidates audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
