"""Audit the time-oriented fixed gerbe representative theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "time_oriented_fixed_gerbe_representative_certificate.json"
CANDIDATE = REPO / "candidate_data" / "time_oriented_fixed_gerbe_representative.candidate.json"
PAPER = REPO / "proof_corpus" / "Time_Oriented_Fixed_Gerbe_Representative_v1.md"
SCRIPT = REPO / "scripts" / "prove_time_oriented_fixed_gerbe_representative.py"


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
    branches = cert.get("branch_representatives", {})
    guardrails = cert.get("guardrails", {})
    still_open = cert.get("still_open", {})

    checks = [
        check(
            "certificate status",
            cert.get("status")
            == "TIME_ORIENTED_FIXED_GERBE_REPRESENTATIVE_CLOSED_SOURCE_PACKET_OPEN",
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
            "finite map closed",
            results.get("finite_gerbe_holonomy_map_closed") is True
            and results.get("trivial_m0_rejected") is True
            and results.get("four_route_nontrivial_pair_closed") is True,
            str(results),
        ),
        check(
            "q79 fixes m1",
            branches.get("time_oriented_q79", {}).get("q") == 79
            and branches.get("time_oriented_q79", {}).get("orientation") == "F"
            and branches.get("time_oriented_q79", {}).get("torsion_label_m") == 1,
            str(branches.get("time_oriented_q79")),
        ),
        check(
            "q369 keeps m2 conjugate",
            branches.get("antiunitary_conjugate_q369", {}).get("q") == 369
            and branches.get("antiunitary_conjugate_q369", {}).get("orientation") == "F*"
            and branches.get("antiunitary_conjugate_q369", {}).get("torsion_label_m") == 2,
            str(branches.get("antiunitary_conjugate_q369")),
        ),
        check(
            "representative closed not source packet",
            results.get("time_oriented_finite_representative_closed") is True
            and results.get("full_twisted_source_promotion_closed") is False
            and results.get("selected_D_E_dotD_constructed") is False,
            str(results),
        ),
        check(
            "still open retains hard source data",
            still_open.get("selected_D_E_dotD") is True
            and still_open.get("twisted_projector_retention") is True
            and still_open.get("full_SM_closure") is True,
            str(still_open),
        ),
        check(
            "guardrails",
            guardrails.get("claims_selected_twist_promotion_packet_passes") is False
            and guardrails.get("claims_full_differential_cohomology_representative") is False
            and guardrails.get("claims_selected_D_E_constructed") is False
            and guardrails.get("claims_full_SM_closure") is False
            and guardrails.get("uses_observed_flavor_data") is False,
            str(guardrails),
        ),
        check(
            "paper records scope",
            "q79/F  -> m = 1" in paper
            and "selected de_response packet on q79/F with m=1" in paper
            and "full Deligne/Cech gerbe period table" in paper,
            "paper scope present",
        ),
    ]

    print("Time-oriented fixed gerbe representative audit")
    print("==============================================")
    failures = 0
    for name, ok, detail in checks:
        print(f"{name:42} {'PASS' if ok else 'FAIL'}  {detail}")
        if not ok:
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
