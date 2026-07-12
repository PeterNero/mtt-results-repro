"""Audit the Qa/SU3 co-closed one-form quotient test."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_gauge_block_quotient_operator_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Gauge_Block_Quotient_Operator_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_gauge_block_quotient_operator.py"


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
            cert["status"] == "QA_SU3_COCLOSED_ONEFORM_QUOTIENT_TESTED_NOT_CLOSED",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate finite parts",
            abs(
                computed["finite_parts"]["p_nonzero_co_closed_oneform_logdet"]
                - cert["finite_parts"]["p_nonzero_co_closed_oneform_logdet"]
            )
            < 1e-12,
            computed["finite_parts"],
        )
    )
    failures.append(
        not report(
            "analytic shift identity recorded",
            "Y_+" in computed["source_data"]["identity"]
            and "M_{k,n+1}" in computed["source_data"]["identity"],
            computed["source_data"],
        )
    )
    failures.append(
        not report(
            "no natural quotient candidate closes the gap",
            computed["verdict"]["natural_quotient_candidates_computed"] is True
            and computed["verdict"]["any_natural_candidate_matches_gap"] is False
            and computed["verdict"]["selected_Qa_SU3_operator_closed"] is False,
            computed["best_natural_candidate"],
        )
    )
    failures.append(
        not report(
            "regulator warning preserved",
            "different regulator" in computed["regulator_warning"]["reason_rejected"]
            and "not stable" in computed["regulator_warning"]["reason_rejected"],
            computed["regulator_warning"],
        )
    )
    failures.append(
        not report(
            "note records next projector or endomorphism gate",
            "Y_+ Y_-" in note
            and "does not close the gap" in note
            and "Selected_Qa_SU3_Physical_Coherent_Projector_or_Endomorphism_Term_v1" in note,
            NOTE,
        )
    )

    print("\nSelected Qa/SU3 gauge-block quotient operator audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
