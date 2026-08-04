"""Audit the real u(3) Chern/HYM Hessian block for Qa/SU3."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_hym_full_real_delta_a_hessian_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_HYM_Full_Real_Delta_A_Hessian_With_OU_Weights_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_hym_full_real_delta_a_hessian.py"


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
    samples = cert["sample_real_hessian_blocks"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_HYM_REAL_CHERN_HESSIAN_BLOCK_COMPUTED_STROMINGER_OU_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["sample_real_hessian_blocks"] == cert["sample_real_hessian_blocks"]
            and computed["remaining_required_data"] == cert["remaining_required_data"],
            computed["verdict"],
        ),
        check(
            "real u3 basis has one central zero and eight positives",
            all(sample["zero_modes"] == 1 and sample["positive_modes"] == 8 for sample in samples),
            samples,
        ),
        check(
            "mu=1 real Hessian eigenvalues match expected values",
            samples[1]["mu"] == 1.0
            and abs(samples[1]["eigenvalues"][1] - 2.5358983848622456) < 1e-12
            and abs(samples[1]["eigenvalues"][-1] - 9.464101615137755) < 1e-12,
            samples[1]["eigenvalues"],
        ),
        check(
            "real block includes Chern conjugate and u3 slice",
            "real anti-Hermitian u(3) basis" in cert["computed_block_scope"]["included"]
            and "Chern unitary conjugate pieces -B_i^*" in cert["computed_block_scope"]["included"],
            cert["computed_block_scope"]["included"],
        ),
        check(
            "full Strominger pieces still excluded",
            "OU weights gamma_{n,k}^{-1}"
            in cert["computed_block_scope"]["still_excluded_from_full_strominger_hessian"]
            and "torsional Weitzenbock/endomorphism terms from R_+ and Hhat"
            in cert["computed_block_scope"]["still_excluded_from_full_strominger_hessian"],
            cert["computed_block_scope"]["still_excluded_from_full_strominger_hessian"],
        ),
        check(
            "no target fitting or false closure",
            cert["verdict"]["target_fitting_used"] is False
            and cert["verdict"]["full_strominger_hessian_computed"] is False
            and cert["verdict"]["mu_selected"] is False,
            cert["verdict"],
        ),
        check(
            "note records next artifact",
            "Selected_Qa_SU3_HYM_Strominger_Weitzenbock_OU_Completion_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 HYM full-real Delta_A Hessian audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
