"""Audit the selected electroweak C1 response interface."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_C1_Response_Interface_v1.md"
CERT = REPO / "certificates" / "selected_electroweak_c1_response_interface_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_electroweak_c1_response.template.json"
FIXTURE = REPO / "certificates" / "selected_electroweak_c1_response_diagnostic_fixture.json"
CALCULATOR = REPO / "scripts" / "compute_electroweak_c1_response.py"
BRIDGE_CERT = REPO / "certificates" / "selected_electroweak_c1_coefficient_bridge_attempt_certificate.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def approx(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def run_calculator(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CALCULATOR), str(path)],
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
    bridge = load_json(BRIDGE_CERT)
    template = load_json(TEMPLATE)
    note = read(NOTE)
    open_run = run_calculator(TEMPLATE)
    fixture_run = run_calculator(FIXTURE)
    fixture_output = json.loads(fixture_run.stdout) if fixture_run.returncode == 0 else {}
    expected = cert["diagnostic_expected"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "PEW_ALPHA1_RESPONSE_INTERFACE_BUILT_VALUES_OPEN",
            cert["status"],
        ),
        check("calculator exists", CALCULATOR.exists(), CALCULATOR),
        check(
            "template refuses incomplete data",
            open_run.returncode == 2 and "missing electroweak C1 primitive response data" in open_run.stdout,
            open_run.stdout.splitlines()[:3],
        ),
        check(
            "all required terms missing in template",
            all(template["raw_response_per_v1"]["terms"][term] is None for term in cert["required_terms"]),
            template["raw_response_per_v1"]["terms"],
        ),
        check(
            "diagnostic fixture computes",
            fixture_run.returncode == 0
            and approx(fixture_output["P_EW_alpha1"]["m1"], expected["P_EW_alpha1"]["m1"])
            and approx(fixture_output["P_EW_alpha1"]["m2"], expected["P_EW_alpha1"]["m2"])
            and approx(fixture_output["lambda_12"], expected["lambda_12"])
            and approx(fixture_output["c_coefficients"]["c1"], expected["c1"])
            and approx(fixture_output["c_coefficients"]["c2"], expected["c2"])
            and approx(fixture_output["Delta_G_12"], expected["Delta_G_12"]),
            fixture_output,
        ),
        check(
            "trace cancels in lambda",
            approx(fixture_output["checks"]["trace_free_sum"], 0.0)
            and approx(fixture_output["checks"]["lambda_12_equals_raw_U1_minus_SU2"], 0.0),
            fixture_output.get("checks"),
        ),
        check(
            "bridge remains open",
            bridge["verdict"]["numeric_electroweak_closure"] is False
            and cert["verdict"]["numeric_electroweak_closure"] is False,
            bridge["verdict"],
        ),
        check(
            "note states exact interface",
            "scripts/compute_electroweak_c1_response.py" in note
            and "PEW_ALPHA1_RESPONSE_INTERFACE_BUILT_VALUES_OPEN" in note,
            "calculator and status",
        ),
        check(
            "closed formula agrees with bridge",
            cert["formula"]["Delta_G_12"] == "v1_tilde*lambda_12/(4*pi)"
            and bridge["reduction"]["Delta_G_12"] == "v1_tilde*(2*m1-m2)/(4*pi)",
            cert["formula"],
        ),
    ]

    print("\nSelected electroweak C1 response interface audit")
    print("================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())

