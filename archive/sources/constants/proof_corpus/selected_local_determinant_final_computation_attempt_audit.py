"""Audit the final local determinant computation attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_local_determinant_final_computation_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Local_Determinant_Final_Computation_Attempt_v1.md"
ATTEMPT = REPO / "scripts" / "test_local_determinant_identifiability.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def run_attempt() -> dict:
    proc = subprocess.run(
        [sys.executable, str(ATTEMPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = load_json(CERT)
    note = read(NOTE)
    result = run_attempt()

    baseline = result["baseline_one_gap_proxy"]["lambda_12"]
    shifted = result["same_scaffold_with_extra_SU2_mode"]["lambda_12"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "FINAL_DETERMINANT_COMPUTATION_BLOCKED_BY_SPECTRAL_UNDERDETERMINATION",
            cert["status"],
        ),
        check(
            "attempt uses selected N=79 scaffold",
            result["selected_scaffold"]["N"] == 79
            and abs(result["selected_scaffold"]["R1_z64_normalized"] - 0.5397189300902845) < 1e-15,
            result["selected_scaffold"],
        ),
        check(
            "same scaffold gives different determinant responses",
            abs(shifted - baseline) > 1.0
            and result["verdict"]["current_scaffold_determines_full_determinant"] is False,
            {"baseline": baseline, "shifted": shifted, "difference": result["lambda_12_difference"]},
        ),
        check(
            "note names exact remaining artifact",
            "Selected_Gauge_Factor_Spectral_Table_v1" in note,
            "spectral table",
        ),
        check(
            "numeric electroweak closure not claimed",
            cert["verdict"]["numeric_electroweak_closure"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False
            and cert["verdict"]["blocker_is_exact"] is True,
            cert["verdict"],
        ),
    ]

    print("\nSelected local determinant final computation attempt audit")
    print("==========================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
