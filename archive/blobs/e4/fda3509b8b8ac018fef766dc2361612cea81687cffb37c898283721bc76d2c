"""Audit the no-go theorem for mu-independent Qa/SU3 completion terms."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_mu_independent_completion_no_go_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Mu_Independent_Completion_No_Go_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_mu_independent_completion_no_go.py"


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
    errors = cert["pencil_identity"]["reconstruction_max_abs_errors"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_MU_INDEPENDENT_TORSION_OU_COMPLETION_NO_GO_PROVED",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["pencil_identity"] == cert["pencil_identity"]
            and computed["monotonicity_certificate"] == cert["monotonicity_certificate"],
            computed["verdict"],
        ),
        check(
            "pencil reconstruction is exact numerically",
            max(errors.values()) < 1e-12,
            errors,
        ),
        check(
            "A and B are positive semidefinite on u3",
            min(cert["pencil_identity"]["A_eigenvalues_u3"]) >= 0.0
            and min(cert["pencil_identity"]["B_eigenvalues_u3"]) >= 0.0,
            {
                "A": cert["pencil_identity"]["A_eigenvalues_u3"],
                "B": cert["pencil_identity"]["B_eigenvalues_u3"],
            },
        ),
        check(
            "logdet derivative positive on samples",
            cert["monotonicity_certificate"]["strictly_positive_on_samples"] is True,
            cert["monotonicity_certificate"]["derivative_samples"],
        ),
        check(
            "mu-independent completion ruled out",
            cert["verdict"]["mu_independent_completion_can_select_mu"] is False
            and "any mu-independent positive semidefinite OU lift C"
            in cert["no_go_scope"]["ruled_out_as_mu_selector"],
            cert["no_go_scope"],
        ),
        check(
            "mu-dependent selector remains open",
            "mu-dependent curvature endomorphism from the non-flat HYM curvature F(mu)"
            in cert["no_go_scope"]["not_ruled_out"]
            and cert["verdict"]["full_mu_selection_closed"] is False,
            cert["verdict"],
        ),
        check(
            "note records next artifact",
            "Selected_Qa_SU3_Mu_Dependent_Curvature_or_OU_Selector_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 mu-independent completion no-go audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
