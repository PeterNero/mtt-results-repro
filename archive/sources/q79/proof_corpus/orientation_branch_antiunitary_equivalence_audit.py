"""Audit the q79/q369 finite antiunitary branch equivalence proof."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "orientation_branch_antiunitary_equivalence_certificate.json"
CANDIDATE = REPO / "candidate_data" / "orientation_branch_antiunitary_equivalence.candidate.json"
NOTE = REPO / "proof_corpus" / "Orientation_Branch_Antiunitary_Equivalence_v1.md"
SCRIPT = REPO / "scripts" / "prove_orientation_branch_antiunitary_equivalence.py"


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


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")

    summary = cert["summary"]
    comparisons = candidate["comparisons"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "ORIENTATION_BRANCH_ANTIUNITARY_EQUIVALENCE_CLOSED_SOURCE_SELECTION_OPEN",
            cert["status"],
        ),
        check(
            "script recomputes certificate",
            computed["summary"] == summary
            and computed["branch_pair"] == cert["branch_pair"]
            and computed["comparisons"] == comparisons,
            computed["summary"],
        ),
        check(
            "branch labels conjugate",
            cert["branch_pair"]["q79_m"] == 1
            and cert["branch_pair"]["q369_m"] == 2
            and cert["branch_pair"]["q79_global_cp_label"] == 79
            and cert["branch_pair"]["q369_global_cp_label"] == 369
            and cert["branch_pair"]["sector_orientations_are_conjugate"] is True,
            cert["branch_pair"],
        ),
        check(
            "finite entries all conjugate",
            summary["antiunitary_equivalence_closed"] is True
            and summary["difference_count"] == 0
            and summary["total_entries_compared"] == 1629
            and summary["max_abs_conjugation_error"] < 1e-12,
            summary,
        ),
        check(
            "all three finite packets compared",
            comparisons["de_action.candidate.json"]["entries_compared"] == 307
            and comparisons["reduced_green.candidate.json"]["entries_compared"] == 500
            and comparisons["dotd_response.candidate.json"]["entries_compared"] == 822
            and all(item["difference_count"] == 0 for item in comparisons.values()),
            comparisons,
        ),
        check(
            "source flags remain common blocker",
            summary["source_flags_match_and_remain_false"] is True
            and summary["source_flag_counts"] == {
                "mismatched": 0,
                "q369_false": 28,
                "q79_false": 28,
            },
            summary["source_flag_counts"],
        ),
        check(
            "no branch-selection overclaim",
            guardrails["claims_unique_branch_selected"] is False
            and guardrails["claims_selected_source_origin"] is False
            and guardrails["uses_observed_cp_sign"] is False
            and guardrails["claims_full_sm_closure"] is False,
            guardrails,
        ),
        check(
            "note records finite equivalence and remaining theorem",
            "finite antiunitary" in note
            and "1629 finite entries" in note
            and "does not choose" in note
            and "selected source or retarded boundary theorem" in note,
            NOTE,
        ),
        check(
            "candidate matches certificate summary",
            candidate["summary"] == cert["summary"]
            and candidate["verdict"] == cert["verdict"],
            candidate["status"],
        ),
    ]

    print("\nOrientation branch antiunitary equivalence audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
