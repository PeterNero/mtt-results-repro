"""Audit the exact scalar-proxy weak split and Nil independence."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "exact_scalar_proxy_weak_split_certificate.json"
NOTE = REPO / "proof_corpus" / "Exact_Scalar_Proxy_Weak_Split_v1.md"
CALCULATOR = REPO / "scripts" / "compute_exact_weak_split_from_circle_sphere.py"
INTERFACE = REPO / "certificates" / "selected_electroweak_c1_response_interface_certificate.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_calculator() -> dict:
    proc = subprocess.run(
        [sys.executable, str(CALCULATOR)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def approx(left: float, right: float, tol: float = 1e-12) -> bool:
    return abs(left - right) <= tol


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    interface = json.loads(read(INTERFACE))
    note = read(NOTE)
    result = run_calculator()
    split = result["weak_split"]

    expected_delta = (
        interface["selected_values"]["v1_tilde"]
        * split["lambda_12"]
        / (4.0 * math.pi)
    )

    checks = [
        check(
            "certificate status",
            cert["status"] == "EXACT_SCALAR_PROXY_WEAK_SPLIT_COMPUTED_NOT_FINAL_CLOSURE",
            cert["status"],
        ),
        check(
            "Nil independence formula inherited",
            interface["formula"]["lambda_12"] == "2*m1-m2=q1-q2=p1-p2"
            and result["nil_independence"]["SU3_nil_enters_lambda_12"] is False,
            result["nil_independence"],
        ),
        check(
            "exact scalar split",
            approx(split["lambda_12"], 3.040437642207233),
            split,
        ),
        check(
            "Delta_G_12 formula",
            approx(split["Delta_G_12"], expected_delta),
            split["Delta_G_12"],
        ),
        check(
            "does not match diagnostic target",
            result["verdict"]["matches_diagnostic_target"] is False
            and split["residual_lambda_12"] > 0.8,
            split,
        ),
        check(
            "note names remaining gate",
            "Selected_U1_SU2_Gauge_Threshold_Operator_and_Weights_v1" in note,
            "remaining gate",
        ),
        check(
            "numeric closure not claimed",
            cert["verdict"]["numeric_electroweak_closure"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        ),
    ]

    print("\nExact scalar-proxy weak split audit")
    print("===================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
