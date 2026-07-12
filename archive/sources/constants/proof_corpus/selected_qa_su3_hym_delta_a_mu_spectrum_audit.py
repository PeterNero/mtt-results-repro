"""Audit the Qa/SU3 HYM Delta_A(mu) algebraic block computation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_hym_delta_a_mu_spectrum_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_HYM_Delta_A_Mu_Spectrum_Computation_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_hym_delta_a_mu_spectrum.py"


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
    samples = cert["sample_blocks"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_HYM_DELTA_A_MU_ALGEBRAIC_BLOCK_COMPUTED_FULL_SELECTION_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["sample_blocks"] == cert["sample_blocks"]
            and computed["remaining_required_data"] == cert["remaining_required_data"],
            computed["verdict"],
        ),
        check(
            "sample blocks have one zero and eight positives",
            all(sample["zero_modes"] == 1 and sample["positive_modes"] == 8 for sample in samples),
            samples,
        ),
        check(
            "mu=1 eigenvalues include expected adjoint block values",
            samples[1]["mu"] == 1.0
            and abs(samples[1]["eigenvalues"][3] - 1.2679491924311228) < 1e-12
            and abs(samples[1]["eigenvalues"][-1] - 4.732050807568877) < 1e-12,
            samples[1]["eigenvalues"],
        ),
        check(
            "monotone diagnostic blocks final selection",
            cert["monotonicity_diagnostic"]["strictly_increasing_on_samples"] is True
            and cert["verdict"]["mu_selected"] is False,
            cert["monotonicity_diagnostic"],
        ),
        check(
            "scope excludes missing full Hessian pieces",
            "OU weights gamma_{n,k}^{-1}" in cert["computed_block_scope"]["excluded"]
            and "real unitary u(E) slice and Hermitian metric normalization"
            in cert["computed_block_scope"]["excluded"],
            cert["computed_block_scope"]["excluded"],
        ),
        check(
            "note records next artifact",
            "Selected_Qa_SU3_HYM_Full_Real_Delta_A_Hessian_With_OU_Weights_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 HYM Delta_A(mu) algebraic block audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
