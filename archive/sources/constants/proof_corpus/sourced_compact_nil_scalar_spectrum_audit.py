"""Audit the sourced compact Nil scalar spectrum import."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "sourced_compact_nil_scalar_spectrum_certificate.json"
NOTE = REPO / "proof_corpus" / "Sourced_Compact_Nil_Scalar_Spectrum_v1.md"
SCRIPT = REPO / "scripts" / "compute_sourced_compact_nil_scalar_spectrum.py"


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


def approx(left: float, right: float, tolerance: float = 1e-12) -> bool:
    return math.isclose(left, right, rel_tol=0.0, abs_tol=tolerance)


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
            cert["status"] == "COMPACT_NIL_SCALAR_SPECTRUM_SOURCE_IMPORTED_DETERMINANT_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate geometry",
            approx(
                computed["selected_geometry_map"]["r_central"],
                cert["selected_geometry_map"]["r_central"],
            )
            and approx(
                computed["selected_geometry_map"]["f_struct"],
                cert["selected_geometry_map"]["f_struct"],
            ),
            computed["selected_geometry_map"],
        )
    )
    failures.append(
        not report(
            "first p nonzero mode matches prior eigenvalue schema",
            abs(computed["consistency_checks"]["first_p_nonzero_eigenvalue_matches_prior_schema"]) < 1e-12,
            computed["sample_modes"]["p_nonzero_first_modes"][0],
        )
    )
    failures.append(
        not report(
            "compact scalar multiplicity is 2 abs k",
            computed["spectrum_formula"]["p_nonzero_multiplicity_after_signs_and_l"] == "2*|k|"
            and computed["sample_modes"]["p_nonzero_first_modes"][2]["sign_pair_l_multiplicity"] == 4,
            computed["spectrum_formula"],
        )
    )
    failures.append(
        not report(
            "old unit multiplicity branch retired for compact scalar claims",
            computed["consistency_checks"]["prior_sign_pair_unit_multiplicity_was_not_compact_scalar_spectrum"]
            is True
            and computed["verdict"]["old_unit_multiplicity_proxy_retired_for_compact_scalar_claims"] is True,
            computed["consistency_checks"],
        )
    )
    failures.append(
        not report(
            "determinant closure remains open",
            computed["verdict"]["compact_scalar_eigenvalue_formula_imported"] is True
            and computed["verdict"]["compact_scalar_p_nonzero_multiplicity_imported"] is True
            and computed["verdict"]["selected_Qa_gauge_operator_closed"] is False
            and computed["verdict"]["BRST_ghost_quotient_closed"] is False
            and computed["verdict"]["analytic_zeta_determinant_closed"] is False
            and computed["verdict"]["numeric_electroweak_closure_certified"] is False,
            computed["verdict"],
        )
    )
    failures.append(
        not report(
            "note records source and boundary",
            "arXiv:1806.05156" in note
            and "2|k|" in note
            and "not the selected Qa determinant" in note
            and "Exact_Selected_Nil_Gauge_Threshold_Zeta_Determinant_v1" in note,
            NOTE,
        )
    )

    print("\nSourced compact Nil scalar spectrum audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
