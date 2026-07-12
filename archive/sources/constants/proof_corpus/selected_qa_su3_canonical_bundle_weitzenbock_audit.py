"""Audit the selected Qa/SU3 canonical bundle and Weitzenbock data."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_canonical_bundle_weitzenbock_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Canonical_Bundle_Weitzenbock_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_canonical_bundle_weitzenbock.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


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
            cert["status"] == "QA_SU3_CANONICAL_BUNDLE_WEITZENBOCK_DATA_COMPUTED_CLOSURE_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate c_nil",
            abs(computed["selected_geometry"]["c_nil"] - cert["selected_geometry"]["c_nil"])
            < 1e-12,
            computed["selected_geometry"],
        )
    )
    failures.append(
        not report(
            "selected overlap is c_nil and not determinant closure",
            computed["canonical_projector_path"]["projector_closes_gap_from_selected_overlap"]
            is False
            and computed["selected_geometry"]["leading_su3_overlap_I3_0"]
            == computed["selected_geometry"]["c_nil"],
            computed["canonical_projector_path"],
        )
    )
    failures.append(
        not report(
            "Weitzenbock one-form Ricci data identified",
            computed["canonical_weitzenbock_path"]["selected_E_term_computed"] is True
            and computed["canonical_weitzenbock_path"]["bochner_identity_check_zero_mode"]
            is True,
            computed["canonical_weitzenbock_path"],
        )
    )
    failures.append(
        not report(
            "determinant response still open",
            computed["canonical_weitzenbock_path"]["determinant_response_computed"] is False
            and computed["verdict"]["selected_Qa_SU3_operator_closed"] is False,
            computed["verdict"],
        )
    )
    failures.append(
        not report(
            "note records BRST determinant next gate",
            "Ric(e1)" in note
            and "Selected_Qa_SU3_BRST_Physical_Determinant_With_Computed_Weitzenbock_E_v1"
            in note,
            NOTE,
        )
    )

    print("\nSelected Qa/SU3 canonical bundle Weitzenbock audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
