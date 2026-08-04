"""Audit the Qa/SU3 minimal gerbe-source candidate/no-go gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "minimal_gerbe_source_candidate_or_nogo_certificate.json"
DATA = REPO / "candidate_data" / "minimal_gerbe_source_candidate_or_nogo.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Minimal_Gerbe_Source_Candidate_or_NoGo_v1.md"
SCRIPT = REPO / "scripts" / "build_minimal_gerbe_source_candidate_or_nogo.py"


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
    scans = data["source_scans"]
    gates = data["gate_results"]
    fields = data["source_packet_fields"]
    routes = {item["route_id"]: item for item in data["evaluated_routes"]}
    checks = [
        check(
            "status",
            cert["status"] == "QA_SU3_MINIMAL_GERBE_SOURCE_CANDIDATE_BUILT_SELECTED_SOURCE_OPEN",
            cert["status"],
        ),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("c twists required", data["c_twist_values_required"] == [-1, 1], data["c_twist_values_required"]),
        check(
            "structural gerbe corpus present",
            scans["flux_iwasawa_gerbe"]["terms"]["b_field_gerbe"]
            and scans["strominger_fixed_gerbe_class"]["terms"]["deligne_2_gerbe"],
            scans,
        ),
        check(
            "q79 guardrail present",
            scans["q79_s3_class_closure"]["terms"]["selected_s3_flat_deligne_class"]
            and scans["q79_s3_class_closure"]["terms"]["smooth_freed_witten"],
            scans["q79_s3_class_closure"],
        ),
        check(
            "source still open",
            gates["minimal_gerbe_source_candidate_exists"] is True
            and gates["same_branch_Qa_SU3_selected_source_supplied"] is False
            and all(value is False for value in fields.values()),
            gates,
        ),
        check(
            "no premature no-go",
            gates["no_go_triggered"] is False and cert["what_closes"]["literal_no_go_not_triggered"] is True,
            gates,
        ),
        check(
            "q79 not imported as proof",
            routes["q79_s3_flat_deligne_import"]["status"] == "ADJACENT_GUARDRAIL_NOT_SAME_SOURCE",
            routes["q79_s3_flat_deligne_import"],
        ),
        check("closure not claimed", cert["closure_claimed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next artifact", cert["next_required_artifact"] in note, NOTE),
    ]
    print("\nSelected Qa/SU3 minimal gerbe-source candidate/no-go audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
