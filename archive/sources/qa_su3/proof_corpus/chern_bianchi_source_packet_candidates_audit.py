"""Audit the Chern/Bianchi source packet candidate table."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "chern_bianchi_source_packet_candidates_certificate.json"
DATA = REPO / "candidate_data" / "chern_bianchi_source_packet_candidates.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Chern_Bianchi_Source_Packet_Candidates_v1.md"
SCRIPT = REPO / "scripts" / "build_chern_bianchi_source_packet_candidates.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def by_id(data: dict[str, object], candidate_id: str) -> dict[str, object]:
    return next(row for row in data["candidate_packets"] if row["id"] == candidate_id)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    result = data["result"]
    abelian = by_id(data, "iwasawa_abelian_two_line_flux_row")
    checks = [
        check("status", cert["status"] == "QA_SU3_CHERN_BIANCHI_SOURCE_PACKET_CANDIDATES_BUILT_NO_SELECTED_SOURCE", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("four candidates", len(data["candidate_packets"]) == 4, [row["id"] for row in data["candidate_packets"]]),
        check("abelian row numeric", math.isclose(abelian["data"]["u"][0], 8.0 * (2.0 * math.pi) ** 2), abelian["data"]),
        check("abelian not closure", abelian["passes"]["integer_flux_row"] is True and abelian["passes"]["selected_su3_color_bundle"] is False, abelian),
        check("candidate table result", result["candidate_table_built"] is True and result["chern_bianchi_row_found"] is True, result),
        check("selected source open", result["selected_qa_su3_source_found"] is False and result["selected_endomorphism_E_found"] is False, result),
        check("no closure", result["qa_su3_closed"] is False and cert["closure_claimed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "Iwasawa abelian" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 Chern-Bianchi source packet candidates audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
