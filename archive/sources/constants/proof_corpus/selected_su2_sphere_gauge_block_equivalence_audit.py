"""Audit the SU2 sphere gauge-block equivalence reduction."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
CERT = REPO / "certificates" / "selected_su2_sphere_gauge_block_equivalence_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_SU2_Sphere_Gauge_Block_Equivalence_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_su2_sphere_gauge_block_equivalence.py"
GAUGE_FIXING = OBSIDIAN / "5 Dirac Delta" / "Gauge_Fixing_as_Admissible_Section_Selection_in_Modal_Triplet_Theory.md"


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
    computed = run_script()
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "SU2_SPHERE_GAUGE_BLOCK_EQUIVALENCE_REDUCED_NOT_CLOSED",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate values",
            approx(
                computed["available_exact_data"]["heat_weighted_candidate"],
                cert["available_exact_data"]["heat_weighted_candidate"],
            )
            and approx(computed["available_exact_data"]["casimir_heat_weight_candidate"], 2.0),
            computed["available_exact_data"],
        )
    )
    failures.append(
        not report(
            "source supports nonabelian ghost field dependence",
            "The Faddeev--Popov determinant is now" in gauge_fixing
            and "depends on the gauge field" in gauge_fixing
            and "ghost representation produces interacting ghost terms" in gauge_fixing,
            GAUGE_FIXING,
        )
    )
    failures.append(
        not report(
            "naive de Rham branch remains rejected",
            computed["negative_checks"]["naive_de_rham_vector_ghost_status"]
            == "EXPLORATORY_OPERATOR_LOGIC_NOT_SELECTED"
            and computed["negative_checks"]["naive_de_rham_vector_ghost_lambda_12"] < 0.0,
            computed["negative_checks"],
        )
    )
    failures.append(
        not report(
            "SU2 closure not overclaimed",
            cert["verdict"]["su2_scalar_sphere_zeta_exact"] is True
            and cert["verdict"]["nonabelian_ghosts_decouple"] is False
            and cert["verdict"]["su2_selected_for_lambda_12_accounting"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        )
    )
    failures.append(
        not report(
            "note names nonabelian ghost determinant gate",
            "Selected_SU2_Nonabelian_Ghost_Quotient_Determinant_v1" in note
            and "not closure" in note
            and "M_G[A]" in note,
            NOTE,
        )
    )

    print("\nSelected SU2 sphere gauge-block equivalence audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
