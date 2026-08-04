"""Audit the selected local determinant computation interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
CERT = REPO / "certificates" / "selected_local_determinant_computation_interface_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_local_determinant_spectrum.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Local_Determinant_Computation_Interface_v1.md"
CALCULATOR = REPO / "scripts" / "compute_selected_local_determinant_response.py"
FINITE_PROJECTION = OBSIDIAN / "5 Dirac Delta" / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"
THETA_NIL = REPO.parent / "mtt-q79-proof-repro" / "proof_corpus" / "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def run_template() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CALCULATOR), str(TEMPLATE)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = load_json(CERT)
    template = load_json(TEMPLATE)
    note = read(NOTE)
    finite_projection = read(FINITE_PROJECTION)
    theta_nil = read(THETA_NIL)
    run = run_template()

    missing = [
        "selected_local_determinant.gauge_factor_spectra.U1",
        "selected_local_determinant.gauge_factor_spectra.SU2",
        "selected_local_determinant.gauge_factor_spectra.SU3",
    ]

    checks = [
        check(
            "certificate status",
            cert["status"] == "LOCAL_DETERMINANT_COMPUTATION_INTERFACE_CLOSED_SPECTRA_OPEN",
            cert["status"],
        ),
        check(
            "calculator exists",
            CALCULATOR.exists(),
            CALCULATOR,
        ),
        check(
            "template refuses absent spectra",
            run.returncode == 2 and all(item in run.stdout for item in missing),
            run.stdout.splitlines(),
        ),
        check(
            "template names all gauge factors",
            set(template["selected_local_determinant"]["gauge_factor_spectra"].keys()) == {"U1", "SU2", "SU3"},
            template["selected_local_determinant"]["gauge_factor_spectra"],
        ),
        check(
            "finite projection supplies spectral heat-kernel home",
            "A corresponding internal heat kernel has spectral form" in finite_projection
            and "A_{\\rm int}\\phi_j=\\mu_j^2\\phi_j" in finite_projection,
            "internal spectral kernel",
        ),
        check(
            "theta nil supplies explicit Laplacian/eigenvalue structure",
            "Scalar Laplacian" in theta_nil
            and "Its eigenvalues are" in theta_nil
            and "magnetic Laplacian" in theta_nil,
            "Nil spectrum structure",
        ),
        check(
            "formula recorded",
            cert["formula"]["weak_split"] == "lambda_12 = p_U1 - p_SU2"
            and "p_a = sum_j" in note,
            cert["formula"],
        ),
        check(
            "numeric closure not claimed",
            cert["verdict"]["determinant_accounting_interface_closed"] is True
            and cert["verdict"]["selected_spectra_computed"] is False
            and cert["verdict"]["numeric_electroweak_closure"] is False,
            cert["verdict"],
        ),
    ]

    print("\nSelected local determinant computation interface audit")
    print("======================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
