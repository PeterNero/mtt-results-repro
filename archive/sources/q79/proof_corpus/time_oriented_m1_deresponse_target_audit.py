"""Audit the time-oriented m=1 de_response target."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "time_oriented_m1_deresponse_target_certificate.json"
CANDIDATE = REPO / "candidate_data" / "time_oriented_m1_deresponse_target.candidate.json"
PAPER = REPO / "proof_corpus" / "Time_Oriented_m1_DeResponse_Target_v1.md"
SCRIPT = REPO / "scripts" / "attempt_time_oriented_m1_deresponse_target.py"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: str) -> tuple[str, bool, str]:
    return name, condition, detail


def run_script() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def main() -> int:
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    rerun = run_script()
    paper = PAPER.read_text(encoding="utf-8")
    results = cert.get("calculation_results", {})
    guardrails = cert.get("guardrails", {})
    still_open = cert.get("still_open", {})

    checks = [
        check(
            "certificate status",
            cert.get("status")
            == "TIME_ORIENTED_M1_DERESPONSE_TARGET_COHERENT_SELECTED_SOURCE_OPEN",
            str(cert.get("status")),
        ),
        check(
            "candidate status",
            candidate.get("status") == cert.get("status"),
            str(candidate.get("status")),
        ),
        check(
            "rerun agrees",
            rerun.get("status") == cert.get("status")
            and rerun.get("calculation_results") == results,
            str(rerun.get("status")),
        ),
        check(
            "m1 fixed",
            results.get("m1_representative_fixed") is True
            and cert.get("fixed_representative_input", {}).get("torsion_label_m") == 1,
            str(cert.get("fixed_representative_input")),
        ),
        check(
            "honest current fails",
            results.get("honest_current_promotion_fails") is True
            and results.get("honest_current_hym_source_fails") is True,
            str(results),
        ),
        check(
            "conditional lifted passes",
            results.get("conditional_lifted_promotion_passes") is True
            and results.get("conditional_lifted_hym_gate_passes") is True
            and results.get("finite_deresponse_stack_coherent") is True,
            str(results),
        ),
        check(
            "remaining source absent",
            results.get("selected_source_still_absent") is True
            and still_open.get("actual_selected_visible_SM_bundle_or_twisted_source") is True
            and still_open.get("repo_level_selected_D_E_dotD_data") is True,
            str(still_open),
        ),
        check(
            "guardrails",
            guardrails.get("claims_selected_source_constructed") is False
            and guardrails.get("claims_lifted_flags_are_physical_proof") is False
            and guardrails.get("claims_selected_D_E_constructed_in_repo") is False
            and guardrails.get("claims_full_SM_closure") is False,
            str(guardrails),
        ),
        check(
            "paper records conditional scope",
            "yes, conditionally" in paper
            and "The lifted packet is not written as proof data" in paper
            and "selected source origin: still missing" in paper,
            "paper scope present",
        ),
    ]

    print("Time-oriented m=1 de_response target audit")
    print("==========================================")
    failures = 0
    for name, ok, detail in checks:
        print(f"{name:42} {'PASS' if ok else 'FAIL'}  {detail}")
        if not ok:
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
