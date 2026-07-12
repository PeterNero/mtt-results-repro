"""Audit Selected_C1_Source_Promotion_Iteration_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_c1_source_promotion_iteration_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_C1_Source_Promotion_Iteration_v1.md"
SCRIPT = REPO / "scripts" / "iterate_selected_c1_source_promotion.py"


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    script_cert = json.loads(proc.stdout)

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "SELECTED_C1_SOURCE_PROMOTION_ITERATED_PHI_FIN_BREAKPOINT_IDENTIFIED",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "no imported proof source",
        cert["usable_selected_source_imports"] == []
        and cert["all_imported_selected_source_candidates_rejected_as_proof_sources"] is True,
        cert["usable_selected_source_imports"],
    )
    ok &= check(
        "cycle exposed",
        cert["cycle_analysis"]["cycle_detected"] is True
        and "selected D_E/Riesz/Green/dotD payload"
        in cert["cycle_analysis"]["source_promotion_needs"],
        cert["cycle_analysis"],
    )
    ok &= check(
        "breakpoint selected",
        cert["solution_direction"]["shortest_non_circular_breakpoint"]
        == "FiniteEmissionMorphism_Phi_fin_with_selected_payload"
        and cert["solution_direction"]["next_artifact_to_construct"]
        == "Selected_PhiFin_C1_Emission_Packet_v1",
        cert["solution_direction"],
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["claims_selected_source_constructed"] is False
        and cert["guardrails"]["claims_A_selected_emitted"] is False
        and cert["guardrails"]["claims_b_selected_emitted"] is False
        and cert["guardrails"]["uses_observed_or_benchmark_inputs"] is False,
        cert["guardrails"],
    )
    ok &= check(
        "note records circularity and next packet",
        "Selected_PhiFin_C1_Emission_Packet_v1" in note
        and "validators are not the missing theorem" in note,
        NOTE,
    )

    print("\nSelected C1 source-promotion iteration audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
