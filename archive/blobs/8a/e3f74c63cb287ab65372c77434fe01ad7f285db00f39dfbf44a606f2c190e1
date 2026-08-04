"""Audit the central-twist orbit-democracy source / determinant operator gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "central_twist_orbit_democracy_source_or_determinant_operator_certificate.json"
DATA = REPO / "candidate_data" / "central_twist_orbit_democracy_source_or_determinant_operator.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Central_Twist_Orbit_Democracy_Source_or_Determinant_Operator_v1.md"
SCRIPT = REPO / "scripts" / "build_central_twist_orbit_democracy_source_or_determinant_operator.py"


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
    finite = data["finite_orbit_democracy_source"]
    det = data["determinant_operator_branch"]["finite_probe"]
    decision = data["decision"]
    checks = [
        check("status", cert["status"] == "QA_SU3_ORBIT_DEMOCRACY_SOURCE_SELECTED_FINITE_TRACE_SMOOTH_DETERMINANT_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("finite orbit democracy selected", finite["source_selected"] is True and finite["theorem"]["selected_weights"] == {"a": 1, "b": 1, "p": 1}, finite),
        check("finite trace source named", "ordinary finite trace" in finite["source"], finite["source"]),
        check("finite response checked", det["finite_trace_tau_squared_computed"] == 8 and det["finite_nonzero_tau_label_count_computed"] == 8 and det["finite_trace_projector_packet"] == 1, det),
        check("projector convention separated", "finite central projector trace" in det["what_this_determines"] and "finite nonzero tau label count" in det["what_this_determines"] and det["finite_trace_projector_packet"] == 1, det),
        check("finite logdet not promoted", det["nonzero_central_character_abs_logdet"] == 0 and det["status"] == "FINITE_RESPONSE_CLOSED_SMOOTH_DETERMINANT_OPEN", det),
        check("determinant no-go retained", data["determinant_operator_branch"]["smooth_exit_closed"] is False and data["determinant_operator_branch"]["no_go"]["verdict"] == "DETERMINANT_OPERATOR_EXIT_NOT_CLOSED_BY_CURRENT_SOURCE", data["determinant_operator_branch"]["no_go"]),
        check("previous promotion gate respected", data["cross_check_against_previous_promotion_gate"]["determinant_finite_part"] == "OPEN" and data["cross_check_against_previous_promotion_gate"]["promotes_now"] is False, data["cross_check_against_previous_promotion_gate"]),
        check("decision split is exact", decision["finite_caxis_orthogonality"] == "CLOSED" and decision["smooth_threshold_determinant_operator"] == "OPEN" and decision["full_Qa_SU3_threshold_closure_now"] is False, decision),
        check("not full closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "finite orbit-democracy" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 central-twist orbit-democracy source or determinant operator audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
