"""Audit the hypercharge embedding gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "hypercharge_embedding_gate_certificate.json"
NOTE = REPO / "proof_corpus" / "Hypercharge_Embedding_Gate_v1.md"
SCRIPT = REPO / "scripts" / "compute_hypercharge_embedding_gate.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def approx(left: float, right: float, tolerance: float = 1e-12) -> bool:
    return math.isclose(left, right, rel_tol=0.0, abs_tol=tolerance)


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


def report(name: str, ok: bool, detail: object = "") -> bool:
    status = "PASS" if ok else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    computed = run_script()
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "HYPERCHARGE_EMBEDDING_GATE_BUILT_NIL_RELEVANCE_REOPENED_FOR_U1_SELECTION",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate",
            approx(
                computed["computed_branches"]["hypercharge_with_proxy_SU3_finite_part"]["lambda_12"],
                cert["computed_branches"]["hypercharge_with_proxy_SU3_finite_part"]["lambda_12"],
            ),
            computed["computed_branches"],
        )
    )
    failures.append(
        not report(
            "hypercharge formula recorded",
            computed["source_formula"]["hypercharge_embedding"] == "Y = (1/6) Q_a - (1/2) Q_c"
            and computed["source_formula"]["threshold_combination"] == "p_Y = (1/36) p_a + (1/4) p_c",
            computed["source_formula"],
        )
    )
    failures.append(
        not report(
            "proxy SU3 does not close",
            computed["computed_branches"]["hypercharge_with_proxy_SU3_finite_part"]["residual_lambda_12"] < -0.7
            and computed["verdict"]["proxy_SU3_does_not_close"] is True,
            computed["computed_branches"]["hypercharge_with_proxy_SU3_finite_part"],
        )
    )
    failures.append(
        not report(
            "required Qa is diagnostic only",
            computed["computed_branches"]["required_Qa_threshold_for_target_if_embedding_is_correct"][
                "p_a_required"
            ]
            > 30
            and "diagnostic" in computed["computed_branches"][
                "required_Qa_threshold_for_target_if_embedding_is_correct"
            ]["role"],
            computed["computed_branches"]["required_Qa_threshold_for_target_if_embedding_is_correct"],
        )
    )
    failures.append(
        not report(
            "note states Nil relevance nuance",
            "Nil/SU3 does not enter after the selected U1 threshold" in note
            and "back in play for selecting physical p_U1 = p_Y" in note,
            NOTE,
        )
    )
    failures.append(
        not report(
            "numeric closure not claimed",
            cert["verdict"]["numeric_electroweak_closure"] is False
            and computed["verdict"]["numeric_electroweak_closure"] is False,
            cert["verdict"],
        )
    )

    print("\nHypercharge embedding gate audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
