"""Audit the selected hypercharge-normalized threshold interface."""

from __future__ import annotations

import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_hypercharge_normalized_threshold_interface_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_hypercharge_normalized_threshold.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Hypercharge_Normalized_Threshold_Interface_v1.md"
SCRIPT = REPO / "scripts" / "compute_hypercharge_normalized_threshold.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def approx(left: float, right: float, tolerance: float = 1e-12) -> bool:
    return math.isclose(left, right, rel_tol=0.0, abs_tol=tolerance)


def run_script(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(path)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def report(name: str, ok: bool, detail: object = "") -> bool:
    status = "PASS" if ok else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    template_proc = run_script(TEMPLATE)
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "SELECTED_HYPERCHARGE_NORMALIZED_THRESHOLD_INTERFACE_BUILT_VALUES_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "template refuses incomplete data",
            template_proc.returncode != 0
            and "missing selected hypercharge-normalized threshold data" in template_proc.stdout
            and "Qa_SU3_stack" in template_proc.stdout
            and "Qc_circle_stack" in template_proc.stdout
            and "SU2_stack" in template_proc.stdout,
            template_proc.stdout.splitlines(),
        )
    )

    fixture = {
        "selected_hypercharge_normalized_threshold": {
            "selected_values": {"v1_tilde": 0.405623467693425},
            "stack_thresholds": {
                "Qa_SU3_stack": 7.291801913769811,
                "Qc_circle_stack": 2.442340583291322,
                "SU2_stack": -0.5980970589159109,
            },
        }
    }
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as handle:
        json.dump(fixture, handle)
        fixture_path = Path(handle.name)
    try:
        fixture_proc = run_script(fixture_path)
    finally:
        fixture_path.unlink(missing_ok=True)

    computed = json.loads(fixture_proc.stdout)
    failures.append(
        not report(
            "fixture computes hypercharge accounting",
            fixture_proc.returncode == 0
            and approx(computed["hypercharge_threshold"]["p_Y"], 0.813135198983103)
            and approx(computed["weak_split"]["lambda_12"], 1.411232257899014),
            computed,
        )
    )
    failures.append(
        not report(
            "formula recorded",
            cert["source_formula"]["threshold_combination"] == "p_Y = (1/36) p_a + (1/4) p_c"
            and cert["source_formula"]["weak_split"] == "lambda_12 = p_Y - p_SU2",
            cert["source_formula"],
        )
    )
    failures.append(
        not report(
            "source discipline recorded",
            cert["source_alignment"]["ProtoSpinor"].startswith("Supports")
            and "quotient" in cert["source_alignment"]["Finite_Coherent_Projection"]
            and "does not compute" in cert["source_alignment"]["Heterotic_Flux"],
            cert["source_alignment"],
        )
    )
    failures.append(
        not report(
            "note names remaining determinant gate",
            "Selected_Qa_Qc_SU2_Stack_Determinants_v1" in note
            and "calculator refuses the template" in note,
            NOTE,
        )
    )
    failures.append(
        not report(
            "numeric closure not claimed",
            cert["verdict"]["determinant_amplitudes_selected"] is False
            and cert["verdict"]["numeric_electroweak_closure"] is False,
            cert["verdict"],
        )
    )

    print("\nSelected hypercharge-normalized threshold interface audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
