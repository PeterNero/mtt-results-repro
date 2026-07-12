"""Audit the Qa/SU3 c-twist source value search."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "ctwist_source_value_search_certificate.json"
DATA = REPO / "candidate_data" / "ctwist_source_value_search.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_CTwist_Source_Value_Search_v1.md"
SCRIPT = REPO / "scripts" / "build_ctwist_source_value_search.py"


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
    candidates = {item["id"]: item for item in data["value_candidates"]}
    scans = data["source_scans"]
    gates = data["gate_results"]
    checks = [
        check("status", cert["status"] == "QA_SU3_CTWIST_SOURCE_VALUE_SEARCH_PARTIAL_VALUES_FOUND_SAME_BRANCH_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("q79 values found", scans["q79_s3_class_closure"]["terms"]["B_i_zero"] and scans["q79_s3_class_closure"]["terms"]["finite_table"], scans["q79_s3_class_closure"]),
        check("strominger source family found", scans["strominger_flux_selection"]["terms"]["fixed_differential_class"] and scans["strominger_flux_selection"]["terms"]["Hhat_global"], scans["strominger_flux_selection"]),
        check("iwasawa gerbe support found", scans["iwasawa_flux_gerbe_quantization"]["terms"]["integral_periods"] and scans["iwasawa_flux_gerbe_quantization"]["terms"]["B_field_gerbe_global"], scans["iwasawa_flux_gerbe_quantization"]),
        check("q79 direct import rejected", candidates["q79_s3_flat_deligne_representative"]["promotion_status"] == "REJECT_AS_DIRECT_IMPORT_GUARDRAIL_ONLY", candidates["q79_s3_flat_deligne_representative"]),
        check("same branch still open", gates["same_branch_Qa_SU3_values_found"] is False and cert["what_remains_open"]["same_branch_Qa_SU3_tau_or_DD_class"] is True, gates),
        check("fallback marked parallel", gates["fallback_A01_DE_should_run_in_parallel"] is True, gates),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next artifact", cert["next_required_artifact"] in note, NOTE),
    ]
    print("\nSelected Qa/SU3 c-twist source value search audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
