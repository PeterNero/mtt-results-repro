"""Audit the final compact-Nil Hodge Qa/SU3 obstruction status."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_final_obstruction_or_projector_resolution_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Final_Obstruction_or_Projector_Jacobian_Resolution_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_final_obstruction_or_projector_resolution.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


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


def report(name: str, ok: bool, detail: object = "") -> bool:
    status = "PASS" if ok else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    computed = run_script()
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"]
            == "QA_SU3_COMPACT_NIL_HODGE_BRANCH_OBSTRUCTED_PROJECTOR_RESOLUTION_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "branch fully computed",
            computed["verdict"]["compact_nil_hodge_branch_fully_computed"] is True,
            computed["computed_branch"],
        )
    )
    failures.append(
        not report(
            "branch does not close",
            computed["verdict"]["compact_nil_hodge_branch_closes_Qa_SU3"] is False
            and computed["verdict"]["branch_status"]
            == "OBSTRUCTED_AS_FINAL_NO_KNOB_QA_SU3_CLOSURE",
            computed["verdict"],
        )
    )
    failures.append(
        not report(
            "no selected projector Jacobian",
            computed["projector_resolution_test"]["current_corpus_selects_this_projector"]
            is False
            and computed["verdict"]["target_fitting_used"] is False,
            computed["projector_resolution_test"],
        )
    )
    failures.append(
        not report(
            "note records next source hunt",
            "fully computed and obstructed" in note
            and "Selected_Qa_SU3_Alternative_Operator_or_Projector_Source_Hunt_v1"
            in note,
            NOTE,
        )
    )

    print("\nSelected Qa/SU3 final obstruction/projector resolution audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
