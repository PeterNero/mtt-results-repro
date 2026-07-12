"""Audit the selected Qa/SU3 p=0 ghost-measure normalization theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_p0_ghost_measure_normalization_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_P0_Ghost_Measure_Normalization_Theorem_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_p0_ghost_measure_normalization.py"


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
            cert["status"] == "QA_SU3_P0_GHOST_MEASURE_NORMALIZATION_SELECTED_FULL_QA_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "p0 extra correction is zero",
            computed["selected_p0_measure_rule"]["selected_extra_p0_logdet_correction"]
            == 0.0,
            computed["selected_p0_measure_rule"],
        )
    )
    failures.append(
        not report(
            "ghost and zero-mode rules selected",
            computed["selected_p0_measure_rule"][
                "longitudinal_exact_modes_cancelled_by_ghost_jacobian"
            ]
            is True
            and computed["selected_p0_measure_rule"][
                "harmonic_zero_modes_excluded_from_threshold_det_prime"
            ]
            is True,
            computed["selected_p0_measure_rule"],
        )
    )
    failures.append(
        not report(
            "p0 ambiguity closed but full Qa remains open",
            computed["verdict"]["p0_ambiguity_closed"] is True
            and computed["verdict"]["selected_Qa_SU3_operator_closed"] is False,
            computed["verdict"],
        )
    )
    failures.append(
        not report(
            "note records p nonzero next gate",
            "selected extra p=0 logdet correction = 0" in note
            and "Selected_Qa_SU3_PNonzero_Physical_Quotient_Determinant_Theorem_v1"
            in note,
            NOTE,
        )
    )

    print("\nSelected Qa/SU3 p0 ghost-measure normalization audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
