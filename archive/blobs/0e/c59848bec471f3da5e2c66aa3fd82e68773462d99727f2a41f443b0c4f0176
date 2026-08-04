"""Audit the selected gauge-factor spectral table candidate pipeline."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_gauge_factor_spectral_table_candidate_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Gauge_Factor_Spectral_Table_Candidate_v1.md"
GENERATOR = REPO / "scripts" / "generate_selected_gauge_factor_spectral_table.py"
SCAN = REPO / "scripts" / "scan_selected_spectral_table_cutoffs.py"
CALCULATOR = REPO / "scripts" / "compute_selected_local_determinant_response.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def run_json(args: list[str]) -> dict:
    proc = subprocess.run(
        [sys.executable, *args],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def compute_table(table: dict) -> dict:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as handle:
        json.dump(table, handle)
        path = Path(handle.name)
    try:
        return run_json([str(CALCULATOR), str(path)])
    finally:
        path.unlink(missing_ok=True)


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = load_json(CERT)
    note = read(NOTE)
    table = run_json(
        [
            str(GENERATOR),
            "--circle-n-max",
            "2",
            "--sphere-ell-max",
            "2",
            "--nil-m-max",
            "1",
            "--nil-p-max",
            "1",
            "--nil-k-max",
            "1",
        ]
    )
    determinant = compute_table(table)
    scan = run_json([str(SCAN)])

    spectra = table["selected_local_determinant"]["gauge_factor_spectra"]
    checks = [
        check(
            "certificate status",
            cert["status"] == "DIAGNOSTIC_SPECTRAL_TABLE_PIPELINE_BUILT_FINAL_SPECTRA_OPEN",
            cert["status"],
        ),
        check(
            "generator emits all gauge sectors",
            set(spectra.keys()) == {"U1", "SU2", "SU3"} and all(spectra[key] for key in spectra),
            {key: len(value) for key, value in spectra.items()},
        ),
        check(
            "selected scaffold uses q79 R1",
            abs(table["selected_scaffold"]["R1_z64_normalized"] - 0.5397189300902845) < 1e-15,
            table["selected_scaffold"],
        ),
        check(
            "determinant calculator accepts generated table",
            "lambda_12" in determinant and set(determinant["mode_counts"].keys()) == {"U1", "SU2", "SU3"},
            determinant,
        ),
        check(
            "cutoff scan is nonconstant",
            len(scan["rows"]) == 5
            and max(scan["lambda_12_values"]) - min(scan["lambda_12_values"]) > 1.0
            and scan["verdict"]["cutoff_independent_value_obtained"] is False,
            scan["lambda_12_values"],
        ),
        check(
            "note names zeta determinant upgrade",
            "Selected_Gauge_Factor_Zeta_Determinant_v1" in note,
            "zeta determinant",
        ),
        check(
            "numeric closure not claimed",
            cert["verdict"]["spectral_table_pipeline_built"] is True
            and cert["verdict"]["final_selected_spectral_table_certified"] is False
            and cert["verdict"]["numeric_electroweak_closure"] is False,
            cert["verdict"],
        ),
    ]

    print("\nSelected gauge-factor spectral table candidate audit")
    print("====================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
