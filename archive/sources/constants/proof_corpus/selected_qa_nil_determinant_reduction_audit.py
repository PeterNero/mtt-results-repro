"""Audit the selected Qa/SU3-Nil determinant reduction attempt."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_nil_determinant_reduction_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_Nil_Determinant_Reduction_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_nil_determinant_reduction.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def approx(left: float, right: float, tolerance: float = 1e-12) -> bool:
    return math.isclose(left, right, rel_tol=0.0, abs_tol=tolerance)


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

    required = computed["exact_required_Qa_after_Qc_SU2_closure"]
    old_proxy = computed["old_proxy_comparison"]
    summaries = {item["name"]: item for item in computed["diagnostic_branch_summaries"]}

    failures.append(
        not report(
            "certificate status",
            cert["status"]
            == "QA_NIL_DETERMINANT_REDUCED_TO_EXACT_TARGET_AND_DIAGNOSTIC_OSCILLATOR_BRANCHES_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate required Qa",
            approx(
                required["heat_weighted_p_a_required"],
                cert["exact_required_Qa_after_Qc_SU2_closure"]["heat_weighted_p_a_required"],
            )
            and approx(
                required["unweighted_p_a_required_if_CA_SU3_is_3"],
                cert["exact_required_Qa_after_Qc_SU2_closure"]["unweighted_p_a_required_if_CA_SU3_is_3"],
            ),
            required,
        )
    )
    failures.append(
        not report(
            "required Qa numerical target is fixed by selected Qc/SU2",
            approx(required["heat_weighted_p_a_required"], 13.945459078292526)
            and approx(required["unweighted_p_a_required_if_CA_SU3_is_3"], 4.648486359430842),
            required,
        )
    )
    failures.append(
        not report(
            "old proxy overshoots required Qa",
            old_proxy["status"] == "OLD_PROXY_OVERSHOOTS_REQUIRED_QA"
            and old_proxy["heat_weighted_excess_over_required"] > 7.0
            and old_proxy["residual_lambda_12_from_old_proxy"] > 0.2,
            old_proxy,
        )
    )
    failures.append(
        not report(
            "three diagnostic branches computed and unselected",
            set(summaries) == {
                "sign_pair_unit_multiplicity",
                "single_abs_p_multiplicity",
                "sign_pair_abs_p_multiplicity",
            }
            and all(item["selected"] is False for item in summaries.values()),
            summaries,
        )
    )
    failures.append(
        not report(
            "no diagnostic oscillator branch is claimed as closure",
            computed["verdict"]["oscillator_completion_calculated"] is True
            and computed["verdict"]["oscillator_completion_selected"] is False
            and computed["verdict"]["qa_nil_selected_determinant_closed"] is False
            and computed["verdict"]["numeric_electroweak_closure_certified"] is False,
            computed["verdict"],
        )
    )
    failures.append(
        not report(
            "note preserves the missing-input boundary",
            "compact Nil p != 0 multiplicities" in note
            and "selected Qa/SU3 gauge-threshold operator" in note
            and "not a selected proof value" in note
            and "Exact_Selected_Nil_Gauge_Threshold_Zeta_Determinant_v1" in note,
            NOTE,
        )
    )

    print("\nSelected Qa/SU3-Nil determinant reduction audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
