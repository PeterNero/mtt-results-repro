"""Audit the compact Nil scalar Hurwitz-zeta determinant candidate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "compact_nil_scalar_hurwitz_zeta_candidate_certificate.json"
NOTE = REPO / "proof_corpus" / "Compact_Nil_Scalar_Hurwitz_Zeta_Candidate_v1.md"
SCRIPT = REPO / "scripts" / "compute_compact_nil_scalar_hurwitz_zeta_candidate.py"


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

    central = computed["central_window_result"]
    hyper = central["hypercharge_if_used_for_Qa"]

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "COMPACT_NIL_SCALAR_HURWITZ_ZETA_CANDIDATE_COMPUTED_NOT_QA_CLOSURE",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate central scalar value",
            abs(
                central["total_scalar_finite_logdet_candidate"]
                - cert["central_window_result"]["total_scalar_finite_logdet_candidate"]
            )
            < 1e-9,
            central,
        )
    )
    failures.append(
        not report(
            "central scalar candidate is a stable near miss",
            3.8 < central["total_scalar_finite_logdet_candidate"] < 3.9
            and 0.05 < hyper["absolute_residual_lambda_12"] < 0.08,
            hyper,
        )
    )
    failures.append(
        not report(
            "window stability supports diagnostic scalar value",
            computed["stability_diagnostics"]["stable_enough_for_selected_determinant"] is True
            and computed["stability_diagnostics"]["window_scalar_value_spread"] < 0.05,
            computed["stability_diagnostics"],
        )
    )
    failures.append(
        not report(
            "scalar candidate does not close Qa",
            computed["verdict"]["compact_scalar_hurwitz_candidate_computed"] is True
            and computed["verdict"]["compact_scalar_candidate_near_required_Qa"] is False
            and computed["verdict"]["scalar_candidate_refutes_direct_scalar_Qa_closure"] is True
            and computed["verdict"]["asymptotic_fit_stable_enough_for_selection"] is True
            and computed["verdict"]["selected_Qa_gauge_operator_closed"] is False
            and computed["verdict"]["numeric_electroweak_closure_certified"] is False,
            computed["verdict"],
        )
    )
    failures.append(
        not report(
            "note records scalar/gauge boundary",
            "Hurwitz" in note
            and "not the selected Qa/SU3 gauge determinant" in note
            and "Selected_Qa_SU3_Gauge_Block_Quotient_Operator_v1" in note,
            NOTE,
        )
    )

    print("\nCompact Nil scalar Hurwitz-zeta candidate audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
