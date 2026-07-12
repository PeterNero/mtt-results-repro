"""Audit the selected SU2 nonabelian ghost quotient determinant gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\proof_corpus")
CERT = REPO / "certificates" / "selected_su2_nonabelian_ghost_quotient_determinant_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_SU2_Nonabelian_Ghost_Quotient_Determinant_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_su2_nonabelian_ghost_quotient_determinant.py"
GAUGE_FIXING = OBSIDIAN / "5 Dirac Delta" / "Gauge_Fixing_as_Admissible_Section_Selection_in_Modal_Triplet_Theory.md"
THETA_II = Q79 / "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md"
QG_II = OBSIDIAN / "12 Quantum Gravity" / "Constructive_MTT_Quantum_Gravity_II__BRST_Lifting__Gauge_Invariant_Observables__and_the_Physical_Hilbert_Space_under_SPT_Damping.md"


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
    gauge_fixing = read(GAUGE_FIXING)
    theta_ii = read(THETA_II)
    qg_ii = read(QG_II)
    computed = run_script()
    failures = []

    by_name = {row["name"]: row for row in computed["computed_branches"]}

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "SU2_NONABELIAN_GHOST_QUOTIENT_REDUCED_NOT_CLOSED",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate scalar and flat FP values",
            approx(
                computed["selected_inputs"]["p_SU2_scalar_exact"],
                cert["selected_inputs"]["p_SU2_scalar_exact"],
            )
            and approx(
                computed["selected_inputs"]["flat_adjoint_fp_logdet_candidate"],
                3.0 * computed["selected_inputs"]["p_SU2_scalar_exact"],
            ),
            computed["selected_inputs"],
        )
    )
    failures.append(
        not report(
            "source supports nonabelian FP field dependence",
            "M_G[A]=\\partial^\\mu D_\\mu[A]" in gauge_fixing
            and "depends on the gauge field" in gauge_fixing
            and "ghost representation produces interacting ghost terms" in gauge_fixing,
            GAUGE_FIXING,
        )
    )
    failures.append(
        not report(
            "Theta II supports constant harmonic but not full FP quotient closure",
            "massless gauge harmonic is taken to be constant on" in theta_ii
            and "after gauge fixing" in theta_ii
            and "constant-curvature" in theta_ii,
            THETA_II,
        )
    )
    failures.append(
        not report(
            "BRST discipline present",
            "BRST" in qg_ii
            and "ghost" in qg_ii
            and "physical" in qg_ii,
            QG_II,
        )
    )
    failures.append(
        not report(
            "conditional zero-extra branch is identified but not selected",
            by_name["flat_background_universal_or_absorbed_ghost"]["status"]
            == "CONDITIONAL_CLOSURE_BRANCH"
            and by_name["flat_background_universal_or_absorbed_ghost"]["selection"]["selectable_now"]
            is False
            and approx(
                by_name["flat_background_universal_or_absorbed_ghost"]["values"]["p_SU2_selected"],
                -1.1961941178318218,
            ),
            by_name["flat_background_universal_or_absorbed_ghost"],
        )
    )
    failures.append(
        not report(
            "diagnostic sign branches remain unselected",
            by_name["explicit_flat_adjoint_ghost_subtraction"]["status"]
            == "DIAGNOSTIC_SIGN_BRANCH_NOT_SELECTED"
            and by_name["explicit_flat_adjoint_ghost_addition"]["status"]
            == "DIAGNOSTIC_SIGN_BRANCH_NOT_SELECTED",
            [
                by_name["explicit_flat_adjoint_ghost_subtraction"]["values"],
                by_name["explicit_flat_adjoint_ghost_addition"]["values"],
            ],
        )
    )
    failures.append(
        not report(
            "closure not overclaimed",
            cert["verdict"]["flat_zero_extra_branch_identified"] is True
            and cert["verdict"]["su2_ghost_quotient_closed"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        )
    )
    failures.append(
        not report(
            "note records exact next missing statement",
            "Selected_SU2_Threshold_Background_is_Flat_and_FP_Determinant_is_Universal_or_Casimir_Absorbed"
            in note
            and "not selected yet" in note
            and "not a fitted sign choice" in note,
            NOTE,
        )
    )

    print("\nSelected SU2 nonabelian ghost quotient determinant audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
