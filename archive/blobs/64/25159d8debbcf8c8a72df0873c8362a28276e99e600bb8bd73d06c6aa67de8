"""Audit the corpus-backed no-knob upgrade backlog."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "no_knob_upgrade_backlog_certificate.json"
DATA = REPO / "candidate_data" / "no_knob_upgrade_backlog.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_No_Knob_Upgrade_Backlog_v1.md"
SCRIPT = REPO / "scripts" / "build_no_knob_upgrade_backlog.py"

REQUIRED_ROWS = {
    "born_record_no_knob",
    "local_qft_functor",
    "selected_sm_packet",
    "gauge_threshold_no_knob",
    "yukawa_cp_higgs_no_knob",
    "gr_dynamics_and_stress_response",
    "absolute_dimensionful_normalization",
    "actual_empirical_equivalence_run",
}


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
    rows = data["backlog_rows"]
    row_ids = {row["id"] for row in rows}
    p0 = [row["id"] for row in rows if row["priority"] == "P0"]
    rows_have_sources = all(row["supporting_sources"] for row in rows)
    rows_not_closed = all(row["closed_now"] is False for row in rows)
    status_has_present = all(status["present"] for status in data["source_status"].values())
    checks = [
        check("status", cert["status"] == "MTT_NO_KNOB_UPGRADE_BACKLOG_BUILT_FROM_CORPUS_AND_REPOS", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("required rows complete", REQUIRED_ROWS.issubset(row_ids), row_ids),
        check("source registry populated", status_has_present, data["source_status"]),
        check("rows have supporting sources", rows_have_sources and gates["all_backlog_rows_have_sources"] is True, rows),
        check("p0 blockers present", {"born_record_no_knob", "local_qft_functor", "selected_sm_packet", "gr_dynamics_and_stress_response", "absolute_dimensionful_normalization", "actual_empirical_equivalence_run"}.issubset(set(p0)), p0),
        check("open gates preserved", rows_not_closed, rows),
        check("selected SM packet open", gates["selected_sm_packet_still_open"] is True, gates),
        check("absolute normalization open", gates["absolute_normalization_still_open"] is True, gates),
        check("empirical equivalence open", gates["actual_empirical_equivalence_still_open"] is True, gates),
        check("qa su3 internal status imported", gates["qa_su3_internal_reduced_packet_status_imported"] is True and gates["qa_su3_coupling_bridge_still_open"] is True, gates),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no no-knob closure claim", gates["no_knob_closure_claimed"] is False and cert["what_remains_open"]["no_knob_constants"] is True, cert),
        check("no target fitting", gates["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("note records decisive gates", "actual selected SM" in note and "absolute dimensionful normalization" in note and "log(2008)" in note, NOTE),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Actual_Selected_SM_Packet_and_Anomaly_Audit_v1", data["next_required_artifact"]),
    ]
    print("\nMTT no-knob upgrade backlog audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
