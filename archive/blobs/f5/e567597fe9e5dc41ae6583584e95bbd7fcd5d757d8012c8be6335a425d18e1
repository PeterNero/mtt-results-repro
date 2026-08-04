"""Audit the Qa/SU3 projector and endomorphism pathway gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_projector_endomorphism_pathways_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Projector_Endomorphism_Pathways_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_projector_endomorphism_pathways.py"


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
            cert["status"] == "QA_SU3_PROJECTOR_ENDOMORPHISM_PATHS_EVALUATED_CLOSURE_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate required gap",
            abs(
                computed["inputs"]["required_unweighted_Qa_gap"]
                - cert["inputs"]["required_unweighted_Qa_gap"]
            )
            < 1e-12,
            computed["inputs"],
        )
    )
    failures.append(
        not report(
            "projector path remains open without selected Jacobian",
            computed["projector_path"]["unit_L2_harmonic_projector_logdet_gap"] == 0.0
            and computed["verdict"]["projector_path_requires_new_selected_norm_or_jacobian"]
            is True,
            computed["projector_path"],
        )
    )
    failures.append(
        not report(
            "endomorphism path remains open without selected Weitzenbock term",
            computed["endomorphism_path"]["selected_constant_shift_available"] is False
            and computed["verdict"]["endomorphism_path_requires_selected_weitzenbock_term"]
            is True,
            computed["endomorphism_path"],
        )
    )
    failures.append(
        not report(
            "diagnostic scan is not treated as closure",
            computed["structural_factor_scan"]["purpose"].startswith("diagnostic only")
            and computed["verdict"]["tempting_nil_volume_factor_is_not_selected"] is True
            and computed["verdict"]["selected_Qa_SU3_operator_closed"] is False,
            computed["structural_factor_scan"]["closest_candidate"],
        )
    )
    failures.append(
        not report(
            "note records both paths and next gate",
            "Path A" in note
            and "Path B" in note
            and "Selected_Qa_SU3_Canonical_Twistor_Bundle_Projector_or_Weitzenbock_E_Term_v1"
            in note,
            NOTE,
        )
    )

    print("\nSelected Qa/SU3 projector/endomorphism pathway audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
