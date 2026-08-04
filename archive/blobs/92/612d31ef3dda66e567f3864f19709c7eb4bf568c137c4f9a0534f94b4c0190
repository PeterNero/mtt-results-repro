"""Audit the partial Strominger/Weitzenbock/OU completion for Qa/SU3."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_hym_strominger_weitzenbock_ou_completion_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_HYM_Strominger_Weitzenbock_OU_Completion_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_hym_strominger_weitzenbock_ou_completion.py"


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
    samples = cert["metric_weighted_real_chern_blocks"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_HYM_STROMINGER_COMPLETION_METRIC_WEIGHTED_CHERN_BLOCK_COMPUTED_TORSION_OU_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["source_backed_completion"] == cert["source_backed_completion"]
            and computed["metric_weighted_real_chern_blocks"] == cert["metric_weighted_real_chern_blocks"]
            and computed["mu_scan"] == cert["mu_scan"],
            computed["verdict"],
        ),
        check(
            "selected Iwasawa radius imported",
            abs(cert["source_backed_completion"]["selected_iwasawa_geometry"]["r1"] - 4.440528182269818)
            < 1e-12
            and abs(cert["source_backed_completion"]["selected_iwasawa_geometry"]["r3"] - 4.440028979122532)
            < 1e-12,
            cert["source_backed_completion"]["selected_iwasawa_geometry"],
        ),
        check(
            "R plus trace coefficient matches selected geometry",
            cert["source_backed_completion"]["r_plus_trace_coefficient_check"][
                "matches_radius_certificate_v1_tilde"
            ]
            is True,
            cert["source_backed_completion"]["r_plus_trace_coefficient_check"],
        ),
        check(
            "metric-weighted samples have one central zero and eight positives",
            all(sample["zero_modes"] == 1 and sample["positive_modes"] == 8 for sample in samples),
            samples,
        ),
        check(
            "metric-weighted determinant scan remains monotone",
            cert["mu_scan"]["strictly_increasing_on_grid"] is True
            and cert["mu_scan"]["grid_min_mu"] == 0.0001,
            cert["mu_scan"],
        ),
        check(
            "full Strominger operator remains open",
            cert["verdict"]["torsional_weitzenbock_endomorphism_computed"] is False
            and cert["verdict"]["ou_weights_computed"] is False
            and cert["verdict"]["mu_selected"] is False,
            cert["verdict"],
        ),
        check(
            "note records the next true gate",
            "Selected_Qa_SU3_Torsional_Endomorphism_or_OU_Mode_Weights_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 HYM Strominger/Weitzenbock/OU completion audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
