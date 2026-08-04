"""Audit physical quotient scheme candidates."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "physical_quotient_scheme_candidates_certificate.json"
NOTE = REPO / "proof_corpus" / "Physical_Quotient_Scheme_Candidates_v1.md"
SCRIPT = REPO / "scripts" / "compute_physical_quotient_scheme_candidates.py"


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
    by_name = {row["name"]: row for row in computed["candidate_results"]}
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "PHYSICAL_QUOTIENT_SCHEME_CANDIDATES_COMPUTED_NOT_SELECTED",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate best clue",
            computed["best_structural_candidate"]["name"] == "adjoint_casimir_weights"
            and approx(
                computed["best_structural_candidate"]["lambda_12"],
                2.41442942313547,
            ),
            computed["best_structural_candidate"],
        )
    )
    failures.append(
        not report(
            "universal half prefactor ruled out",
            by_name["uniform_half_determinant_prefactor"]["lambda_12"] < 1.0
            and by_name["uniform_half_determinant_prefactor"]["status"] == "RULED_OUT_AS_UNIVERSAL_PREFAC",
            by_name["uniform_half_determinant_prefactor"],
        )
    )
    failures.append(
        not report(
            "adjoint dimension overshoots",
            by_name["adjoint_dimension_weights"]["lambda_12"] > 4.0,
            by_name["adjoint_dimension_weights"],
        )
    )
    failures.append(
        not report(
            "de Rham branch ruled out",
            by_name["formal_de_rham_vector_ghost_on_qc_su2"]["lambda_12"] < 0.0
            and by_name["formal_de_rham_vector_ghost_on_qc_su2"]["status"]
            == "RULED_OUT_FOR_THIS_PROXY_BRANCH",
            by_name["formal_de_rham_vector_ghost_on_qc_su2"],
        )
    )
    failures.append(
        not report(
            "best clue remains unselected",
            computed["verdict"]["best_candidate_selected_by_corpus"] is False
            and "Selected_Physical_Quotient_Heat_Coefficients_v1" in note,
            computed["verdict"],
        )
    )
    failures.append(
        not report(
            "numeric closure not claimed",
            cert["verdict"]["numeric_electroweak_closure"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        )
    )

    print("\nPhysical quotient scheme candidates audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
