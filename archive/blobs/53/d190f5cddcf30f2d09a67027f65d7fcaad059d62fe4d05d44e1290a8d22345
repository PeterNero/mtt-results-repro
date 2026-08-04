"""Audit the Qa/Qc/SU2 spectrum-or-heat-coefficient candidate gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qaqcsu2_operator_spectra_or_heat_coefficients_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_Qc_SU2_Operator_Spectra_or_Heat_Coefficients_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qaqcsu2_operator_spectra_or_heat_coefficients.py"


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

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "QA_QC_SU2_SPECTRA_HEAT_CANDIDATE_TABLE_BUILT_SELECTION_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate lambda",
            approx(
                computed["candidate_hypercharge_accounting"]["lambda_12_candidate"],
                cert["candidate_hypercharge_accounting"]["lambda_12_candidate"],
            )
            and approx(
                computed["candidate_hypercharge_accounting"]["p_Y_candidate"],
                cert["candidate_hypercharge_accounting"]["p_Y_candidate"],
            ),
            computed["candidate_hypercharge_accounting"],
        )
    )
    failures.append(
        not report(
            "Qc and SU2 selected weak-split statuses carried",
            computed["block_status"]["D_Qc"]["spectrum_or_heat_data_status"]
            == "SELECTED_QC_CIRCLE_GAUGE_BLOCK_ZETA_CLOSED_FOR_WEAK_SPLIT"
            and computed["block_status"]["D_SU2"]["spectrum_or_heat_data_status"]
            == "SELECTED_SU2_SPHERE_GAUGE_BLOCK_ZETA_CLOSED_FOR_WEAK_SPLIT",
            {
                "D_Qc": computed["block_status"]["D_Qc"]["spectrum_or_heat_data_status"],
                "D_SU2": computed["block_status"]["D_SU2"]["spectrum_or_heat_data_status"],
            },
        )
    )
    failures.append(
        not report(
            "Qa remains diagnostic proxy",
            computed["block_status"]["D_Qa"]["spectrum_or_heat_data_status"]
            == "DIAGNOSTIC_SU3_NIL_PROXY_NOT_SELECTED"
            and computed["verdict"]["su3_nil_selected_spectrum_closed"] is False,
            computed["block_status"]["D_Qa"],
        )
    )
    failures.append(
        not report(
            "candidate heat-weighted values match prior branch",
            approx(computed["block_status"]["D_Qa"]["heat_weighted_finite_part_candidate"], 21.875405741309436)
            and approx(computed["block_status"]["D_Qc"]["heat_weighted_finite_part_candidate"], 2.442340583291322)
            and approx(computed["block_status"]["D_SU2"]["heat_weighted_finite_part_candidate"], -1.1961941178318218),
            computed["candidate_hypercharge_accounting"],
        )
    )
    failures.append(
        not report(
            "selected gauge spectra remain partly open",
            computed["selection_status_summary"]["all_three_selected_for_physical_quotient"] is False
            and computed["selection_status_summary"]["D_Qc_selected_gauge_block"] is True
            and computed["selection_status_summary"]["D_SU2_selected_gauge_block"] is True
            and computed["verdict"]["selected_gauge_operator_spectra_closed"] is False
            and computed["verdict"]["su2_gauge_block_closed_for_weak_split"] is True
            and computed["verdict"]["new_no_knob_prediction_certified"] is False,
            computed["selection_status_summary"],
        )
    )
    failures.append(
        not report(
            "note names exact Nil/gauge heat gate",
            "Exact_Selected_Nil_or_Gauge_Threshold_Heat_Coefficients_v1" in note
            and "It is not electroweak closure." in note
            and "DIAGNOSTIC_SU3_NIL_PROXY_NOT_SELECTED" in note
            and "D_Qc is now selected for weak-split accounting" in note,
            NOTE,
        )
    )

    print("\nSelected Qa/Qc/SU2 spectra-or-heat-coefficients audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
