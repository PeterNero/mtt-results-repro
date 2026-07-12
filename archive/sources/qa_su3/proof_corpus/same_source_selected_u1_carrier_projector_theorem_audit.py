"""Audit the same-source selected U1 carrier/projector theorem attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "same_source_selected_u1_carrier_projector_theorem_certificate.json"
DATA = REPO / "candidate_data" / "same_source_selected_u1_carrier_projector_theorem.candidate.json"
NOTE = REPO / "proof_corpus" / "Same_Source_Selected_U1_Carrier_Projector_Theorem_v1.md"
SCRIPT = REPO / "scripts" / "build_same_source_selected_u1_carrier_projector_theorem.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def test_by_id(items: list[dict[str, object]], tid: str) -> dict[str, object]:
    return next(item for item in items if item["id"] == tid)


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
    tests = data["theorem_attempt"]["tests"]
    decision = data["decision"]
    checks = [
        check("status", cert["status"] == "SAME_SOURCE_U1_CARRIER_SOURCE_LEVEL_SELECTED_PROJECTOR_OPERATOR_TRACE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("source-level carrier support closed", test_by_id(tests, "selected_s3_qutrit_source_level_carrier")["closed"] is True, tests),
        check("rank-three shape available", test_by_id(tests, "rank_three_shape_available")["closed"] is True, tests),
        check("projector not emitted", test_by_id(tests, "u1_specific_shared_circle_projector_P_perp")["closed"] is False and decision["u1_projector_P_perp_emitted"] is False, decision),
        check("operator trace policy not emitted", test_by_id(tests, "operator_trace_uses_P_perp")["closed"] is False and decision["u1_operator_trace_policy_emitted"] is False, decision),
        check("no promotion", decision["promoted_to_selected_threshold_index"] is False and decision["measured_electroweak_closure"] is False, decision),
        check("target not used", decision["target_fitting_used"] is False and data["target_fitting_used"] is False, decision),
        check("note names minimal packet", "Minimal Projector Packet" in note and "P_perp" in note, NOTE),
    ]
    print("\nSame-source selected U1 carrier/projector theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
