"""Audit the Qa/SU3 BRST determinant table with Weitzenbock E included."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_brst_determinant_with_weitzenbock_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_BRST_Determinant_With_Weitzenbock_E_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_brst_determinant_with_weitzenbock.py"


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
            cert["status"] == "QA_SU3_BRST_DETERMINANT_WITH_WEITZENBOCK_E_EVALUATED_CLOSURE_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate required value",
            abs(
                computed["finite_parts_used"]["required_unweighted_Qa"]
                - cert["finite_parts_used"]["required_unweighted_Qa"]
            )
            < 1e-12,
            computed["finite_parts_used"],
        )
    )
    failures.append(
        not report(
            "E included without double counting",
            computed["selected_weitzenbock_inclusion"][
                "E_is_already_in_sourced_hodge_oneform_spectrum"
            ]
            is True
            and computed["selected_weitzenbock_inclusion"]["do_not_add_E_again_as_shift"]
            is True,
            computed["selected_weitzenbock_inclusion"],
        )
    )
    failures.append(
        not report(
            "candidate table built but not closure",
            computed["verdict"]["full_BRST_candidate_table_built"] is True
            and computed["verdict"]["selected_Qa_SU3_operator_closed"] is False,
            computed["closest_unforbidden_candidate"],
        )
    )
    failures.append(
        not report(
            "p0 and ghost rules remain open",
            computed["verdict"]["selected_p0_measure_rule_available"] is False
            and computed["verdict"]["selected_ghost_normalization_available"] is False,
            computed["verdict"],
        )
    )
    failures.append(
        not report(
            "note records p0 ghost measure next gate",
            "already contains the curvature endomorphism" in note
            and "Selected_Qa_SU3_P0_Ghost_Measure_Normalization_Theorem_v1" in note,
            NOTE,
        )
    )

    print("\nSelected Qa/SU3 BRST determinant with Weitzenbock audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
