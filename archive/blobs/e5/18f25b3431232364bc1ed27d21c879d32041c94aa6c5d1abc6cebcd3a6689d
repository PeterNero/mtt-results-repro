"""Audit the selected SU2 threshold-background flatness theorem."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\proof_corpus")
CERT = REPO / "certificates" / "selected_su2_threshold_background_flatness_or_fp_spectrum_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_SU2_Threshold_Background_Flatness_or_FP_Spectrum_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_su2_threshold_background_flatness_or_fp_spectrum.py"
THETA_II = Q79 / "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md"
THETA_III = Q79 / "Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization.md"


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
    theta_ii = read(THETA_II)
    theta_iii = read(THETA_III)
    computed = run_script()
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "SU2_THRESHOLD_BACKGROUND_FLATNESS_CLOSED_FP_POLICY_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "Theta II supplies constant gauge harmonic after fixing",
            "massless gauge harmonic is taken to be constant on" in theta_ii
            and "after gauge fixing" in theta_ii
            and "constant-curvature" in theta_ii,
            THETA_II,
        )
    )
    failures.append(
        not report(
            "Theta III supplies trivial-bundle linearization and constant harmonic",
            "Linearizing Equation" in theta_iii
            and "about the trivial bundle" in theta_iii
            and "massless twistor harmonic" in theta_iii
            and "is constant" in theta_iii,
            THETA_III,
        )
    )
    failures.append(
        not report(
            "script agrees with flat FP arithmetic",
            approx(computed["computed_flat_fp_data"]["p_SU2_no_extra_ghost_term"], -1.1961941178318218)
            and approx(computed["computed_flat_fp_data"]["flat_adjoint_fp_logdet"], -1.7942911767477328)
            and computed["proved_flatness_statement"]["closed"] is True,
            computed["computed_flat_fp_data"],
        )
    )
    failures.append(
        not report(
            "flatness closed but policy remains open",
            cert["verdict"]["selected_su2_threshold_background_flat"] is True
            and cert["verdict"]["selected_nonflat_fp_spectrum_required"] is False
            and cert["verdict"]["quotient_normalization_policy_closed"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        )
    )
    failures.append(
        not report(
            "note names next quotient policy gate",
            "Selected_Flat_FP_Quotient_Normalization_Policy_v1" in note
            and "flatness is closed" in note
            and "policy is still open" in note,
            NOTE,
        )
    )

    print("\nSelected SU2 threshold background flatness or FP spectrum audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
