"""Audit the Qa/SU3 HYM color-connection spectrum/torsion computation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = (
    REPO
    / "certificates"
    / "selected_qa_su3_hym_color_connection_spectrum_or_torsion_certificate.json"
)
NOTE = (
    REPO
    / "proof_corpus"
    / "Selected_Qa_SU3_HYM_Color_Connection_Spectrum_or_Torsion_Computation_v1.md"
)
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_hym_color_connection_spectrum_or_torsion.py"


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
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    invariants = cert["computed_algebraic_invariants"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_HYM_CONNECTION_MATRIX_EXTRACTED_SPECTRUM_TORSION_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["selected_connection_matrix_data"]
            == cert["selected_connection_matrix_data"]
            and computed["remaining_blockers"] == cert["remaining_blockers"],
            computed["verdict"],
        ),
        check(
            "source matrix terms found",
            r"\mu\,\bar\omega^3" in cert["source_check"]["terms_found"]
            and r"\sqrt{\mu}\,\bar\omega^1" in cert["source_check"]["terms_found"]
            and r"-\sqrt{\mu}\,\bar\omega^2" in cert["source_check"]["terms_found"],
            cert["source_check"],
        ),
        check(
            "matrix invariants computed",
            invariants["sum_frobenius_squared_of_A01_coefficients"] == "2*mu + mu^2"
            and invariants["mu_dependence_detected"] is True,
            invariants,
        ),
        check(
            "not misread as Laplacian spectrum",
            "this is not the spectrum of the connection Laplacian" in note
            and cert["computed_numeric_response"] is None,
            NOTE,
        ),
        check(
            "no target fitting or SM closure overclaim",
            cert["verdict"]["target_fitting_used"] is False
            and cert["verdict"]["can_close_Qa_SU3_now"] is False
            and cert["verdict"]["full_SM_closure_achieved"] is False,
            cert["verdict"],
        ),
        check(
            "next gate named",
            cert["verdict"]["next_required_artifact"]
            == "Selected_Qa_SU3_HYM_Mu_and_Operator_Domain_Selection_v1",
            cert["verdict"]["next_required_artifact"],
        ),
    ]

    print("\nSelected Qa/SU3 HYM color-connection spectrum/torsion audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
