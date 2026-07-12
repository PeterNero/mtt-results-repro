"""Audit the Qa/SU3 HYM mu/operator-domain selection gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = (
    REPO
    / "certificates"
    / "selected_qa_su3_hym_mu_and_operator_domain_selection_certificate.json"
)
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_HYM_Mu_and_Operator_Domain_Selection_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_hym_mu_and_operator_domain_selection.py"


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
    routes = cert["candidate_routes"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_HYM_OPERATOR_DOMAIN_REDUCED_MU_SELECTION_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["selected_next_operator_gate"] == cert["selected_next_operator_gate"]
            and computed["remaining_required_data"] == cert["remaining_required_data"],
            computed["verdict"],
        ),
        check(
            "continuous mu/moduli source found",
            r"\mu>0" in cert["source_checks"]["explicit_iwasawa_hym_family"]["terms_found"]
            and "bundle moduli enter continuously"
            in cert["source_checks"]["explicit_iwasawa_hym_family"]["terms_found"],
            cert["source_checks"]["explicit_iwasawa_hym_family"],
        ),
        check(
            "strominger hessian domain sourced",
            "bundle via the Yang--Mills Laplacian"
            in cert["source_checks"]["strominger_selection_hessian"]["terms_found"]
            and r"\Delta_A"
            in cert["source_checks"]["strominger_selection_hessian"]["terms_found"],
            cert["source_checks"]["strominger_selection_hessian"],
        ),
        check(
            "bad shortcuts rejected",
            routes["chern_classes_and_bianchi"]["status"] == "REJECTED_FOR_MU_SELECTION"
            and routes["unit_frobenius_or_mu_equals_one"]["status"]
            == "FORBIDDEN_UNSOURCED_NORMALIZATION",
            routes,
        ),
        check(
            "operator domain reduced but mu open",
            cert["verdict"]["operator_domain_selected_for_next_gate"] is True
            and cert["verdict"]["mu_selected"] is False
            and cert["verdict"]["can_close_Qa_SU3_now"] is False,
            cert["verdict"],
        ),
        check(
            "note records next artifact",
            "Selected_Qa_SU3_HYM_Delta_A_Mu_Spectrum_Computation_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 HYM mu/operator-domain selection audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
