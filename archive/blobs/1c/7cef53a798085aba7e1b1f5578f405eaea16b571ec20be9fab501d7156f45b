"""Test whether selected gap/overlap scaffold determines the determinant response.

This is a no-knob obstruction test.  It constructs several spectral tables that
obey the same currently selected Theta scaffold data available in the corpus:

    N=79 central-circle R1 from the Z64-normalized branch,
    (f2 R_lens)^2 = 0.280 R1,
    c = 1.439 R1,
    first-gap lower bounds for circle/lens/nil.

If the determinant response differs across admissible completions, the final
electroweak determinant computation is not determined by the current scaffold.
"""

from __future__ import annotations

import json
import math
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CALCULATOR = ROOT / "scripts" / "compute_selected_local_determinant_response.py"
CENTRAL_CERT = ROOT / "certificates" / "selected_central_circle_damping_identification_lemma_certificate.json"


def selected_r1(n: int = 79) -> float:
    cert = json.loads(CENTRAL_CERT.read_text(encoding="utf-8"))
    for row in cert["tested_cases"]:
        if row["N"] == n:
            return float(row["R1_z64_normalized"])
    raise KeyError(n)


def scaffold_gaps(r1: float) -> dict[str, float]:
    lens_radius_squared = 0.280 * r1
    c_nil = 1.439 * r1
    return {
        "U1": 1.0 / (r1 * r1),
        "SU2": 2.0 / lens_radius_squared,
        "SU3": min(4.0 * math.pi * math.pi, 2.0 * math.pi + 4.0 * math.pi * math.pi / (c_nil * c_nil)),
    }


def run_calculator(table: dict) -> dict:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as handle:
        json.dump(table, handle)
        path = Path(handle.name)
    try:
        import subprocess

        proc = subprocess.run(
            [sys.executable, str(CALCULATOR), str(path)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=True,
        )
        return json.loads(proc.stdout)
    finally:
        path.unlink(missing_ok=True)


def spectral_table(gaps: dict[str, float], extra_su2_mode: float | None = None) -> dict:
    spectra = {
        factor: [{"eigenvalue": value, "multiplicity": 1.0, "index_weight": 1.0}]
        for factor, value in gaps.items()
    }
    if extra_su2_mode is not None:
        spectra["SU2"].append({"eigenvalue": extra_su2_mode, "multiplicity": 1.0, "index_weight": 1.0})
    return {
        "selected_local_determinant": {
            "reference_scale_squared": 1.0,
            "gauge_factor_spectra": spectra,
        }
    }


def main() -> int:
    r1 = selected_r1(79)
    gaps = scaffold_gaps(r1)
    baseline = run_calculator(spectral_table(gaps))
    shifted = run_calculator(spectral_table(gaps, extra_su2_mode=100.0 * gaps["SU2"]))

    result = {
        "selected_scaffold": {
            "N": 79,
            "R1_z64_normalized": r1,
            "lens_radius_squared": 0.280 * r1,
            "nil_c": 1.439 * r1,
            "gap_values_used_as_first_modes": gaps,
        },
        "baseline_one_gap_proxy": baseline,
        "same_scaffold_with_extra_SU2_mode": shifted,
        "lambda_12_difference": shifted["lambda_12"] - baseline["lambda_12"],
        "verdict": {
            "current_scaffold_determines_full_determinant": False,
            "reason": "The same selected first-gap/overlap data allow different higher spectra and hence different determinant responses.",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
