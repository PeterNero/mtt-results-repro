"""Audit the exact U1 circle and SU2 sphere zeta pieces."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "exact_circle_sphere_zeta_pieces_certificate.json"
NOTE = REPO / "proof_corpus" / "Exact_Circle_Sphere_Zeta_Pieces_v1.md"
CALCULATOR = REPO / "scripts" / "compute_exact_circle_sphere_zeta.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_calculator() -> dict:
    proc = subprocess.run(
        [sys.executable, str(CALCULATOR)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def approx(left: float, right: float, tol: float = 1e-12) -> bool:
    return abs(left - right) <= tol


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    result = run_calculator()
    r1 = result["selected_scaffold"]["R1_z64_normalized"]
    lens = result["selected_scaffold"]["lens_radius_squared"]
    zeta_prime = result["constants"]["zeta_R_prime_minus_one"]
    expected_u1 = 2.0 * math.log(2.0 * math.pi * r1)
    expected_su2 = -4.0 * zeta_prime + (2.0 / 3.0) * math.log(lens)

    checks = [
        check(
            "certificate status",
            cert["status"] == "EXACT_U1_SU2_ZETA_PIECES_CLOSED_SU3_NIL_OPEN",
            cert["status"],
        ),
        check(
            "selected q79 scaffold",
            approx(r1, 0.5397189300902845) and approx(lens, 0.280 * r1),
            result["selected_scaffold"],
        ),
        check(
            "U1 formula",
            approx(result["finite_parts"]["U1_circle"], expected_u1),
            result["finite_parts"]["U1_circle"],
        ),
        check(
            "SU2 formula",
            approx(result["finite_parts"]["SU2_effective_sphere"], expected_su2),
            result["finite_parts"]["SU2_effective_sphere"],
        ),
        check(
            "SU3 remains open",
            result["finite_parts"]["SU3_nil"] is None
            and result["verdict"]["su3_nil_zeta_closed"] is False,
            result["verdict"],
        ),
        check(
            "note names exact Nil upgrade",
            "Exact_Selected_Nil_Gauge_Threshold_Zeta_Determinant_v1" in note,
            "Nil upgrade",
        ),
        check(
            "numeric closure not claimed",
            cert["verdict"]["numeric_electroweak_closure"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        ),
    ]

    print("\nExact circle/sphere zeta pieces audit")
    print("=====================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
