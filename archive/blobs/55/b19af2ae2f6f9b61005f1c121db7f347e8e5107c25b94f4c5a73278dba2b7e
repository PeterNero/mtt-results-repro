"""Scan truncated selected spectral-table diagnostics across cutoffs."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

from generate_selected_gauge_factor_spectral_table import build_table


ROOT = Path(__file__).resolve().parents[1]
CALCULATOR = ROOT / "scripts" / "compute_selected_local_determinant_response.py"


def compute(table: dict) -> dict:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as handle:
        json.dump(table, handle)
        path = Path(handle.name)
    try:
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


def main() -> int:
    rows = []
    for cutoff in range(1, 6):
        table = build_table(
            n=79,
            circle_n_max=cutoff,
            sphere_ell_max=cutoff,
            nil_m_max=cutoff,
            nil_p_max=cutoff,
            nil_k_max=cutoff,
        )
        result = compute(table)
        rows.append(
            {
                "cutoff": cutoff,
                "mode_counts": result["mode_counts"],
                "lambda_12": result["lambda_12"],
                "local_determinant_response_per_v1": result["local_determinant_response_per_v1"],
            }
        )

    output = {
        "status": "TRUNCATED_DIAGNOSTIC_SCAN_NOT_REGULARIZED_DETERMINANT",
        "rows": rows,
        "lambda_12_values": [row["lambda_12"] for row in rows],
        "verdict": {
            "finite_cutoff_pipeline_works": True,
            "cutoff_independent_value_obtained": False,
            "next_required_upgrade": "Replace truncation by selected zeta/heat-kernel finite part and exact Nil/gauge-weight spectra.",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
