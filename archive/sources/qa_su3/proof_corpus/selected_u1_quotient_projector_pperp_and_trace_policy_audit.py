"""Audit the selected U1 quotient projector and trace-policy theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_u1_quotient_projector_pperp_and_trace_policy_certificate.json"
DATA = REPO / "candidate_data" / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1_Quotient_Projector_Pperp_and_Trace_Policy_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_u1_quotient_projector_pperp_and_trace_policy.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    theorem = data["projector_theorem"]
    checks_data = theorem["checks"]
    decision = data["decision"]
    support = data["source_support"]
    checks = [
        check("status", cert["status"] == "SELECTED_U1_QUOTIENT_PROJECTOR_PPERP_TRACE_POLICY_CLOSED_INDEX_ONLY", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("source support imported", support["previous_source_level_support"]["source_level_rank3_carrier_support_closed"] is True and support["previous_source_level_support"]["su2_weak_split_closed"] is True, support["previous_source_level_support"]),
        check("projector explicit", theorem["P_perp"] == [["2/3", "-1/3", "-1/3"], ["-1/3", "2/3", "-1/3"], ["-1/3", "-1/3", "2/3"]], theorem["P_perp"]),
        check("projector idempotent", checks_data["idempotent"] is True, checks_data),
        check("annihilates shared vector", checks_data["annihilates_shared_vector"] is True, checks_data),
        check("rank and trace", checks_data["rank"] == 2 and checks_data["trace_P_perp"] == "2/1" and checks_data["trace_identity"] == "3/1", checks_data),
        check("normalized trace 2/3", checks_data["normalized_trace"] == "2/3" and checks_data["same_as_source_theorem_weight"] is True, checks_data),
        check("trace policy emitted", decision["U1_operator_trace_uses_P_perp"] is True and "Tr(P_perp)/Tr(I_3) = 2/3" in data["trace_policy"]["formula"], data["trace_policy"]),
        check("index pair closed only", decision["selected_U1_SU2_threshold_index_pair_closed"] is True and decision["measured_electroweak_closure"] is False and decision["K_gauge_anchor_closed"] is False, decision),
        check("target not used", decision["target_fitting_used"] is False and data["target_fitting_used"] is False, decision),
        check("note records guardrails", "does not close measured electroweak" in note and "Do not use this theorem to set K_gauge" in note, NOTE),
    ]
    print("\nSelected U1 quotient projector Pperp and trace-policy audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
