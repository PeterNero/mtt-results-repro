"""Audit the Ext/stability source search."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "ext_stability_source_search_certificate.json"
DATA = REPO / "candidate_data" / "ext_stability_source_search.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Ext_Stability_Source_Search_v1.md"
SCRIPT = REPO / "scripts" / "build_ext_stability_source_search.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    monad = data["monad_computation"]
    closes = data["what_closes"]
    remains = data["what_remains_open"]
    checks = [
        check("status", cert["status"] == "QA_SU3_EXT_STABILITY_SOURCE_SEARCH_FOUND_IWASAWA_MONAD_OPERATOR_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("source found", data["source_scan"]["present"] is True and data["source_scan"]["missing_terms"] == [], data["source_scan"]),
        check("chern recomputed", monad["c1_zero"] is True and monad["c2_zero"] is True and monad["c3_integral_equals_6"] is True, monad),
        check("monad closes source blank", closes["explicit_iwasawa_su3_monad_found"] is True and closes["hym_existence_claim_present"] is True, closes),
        check("same paper row", closes["same_paper_contains_abelian_bianchi_row"] is True, closes),
        check("operator remains open", remains["qa_su3_threshold_representation"] is True and remains["operator_packet_filled"] is False, remains),
        check("no closure", remains["qa_su3_closed"] is False and cert["closure_claimed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "c2(E)=0" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 Ext stability source search audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
