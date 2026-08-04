"""Audit the U1/Y Route-C typed monad/Cech or HYM witness contract."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.candidate.json"
PAYLOAD = REPO / "candidate_data" / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.open.json"
CERT = REPO / "certificates" / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_TypedMonadCech_or_HYMConnectionWitness_v1.md"

STATUS = "U1Y_ROUTEC_TYPED_MONAD_CECH_OR_HYM_CONNECTION_WITNESS_CONTRACT_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_FiniteHYMConnectionSolve_or_TypedCechPayload_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    payload = json.loads(PAYLOAD.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    guardrails = data["guardrails"]
    audit_checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("payload open", payload["status"] == "OPEN_VALUES_REQUIRED" and cert["payload_missing_leaf_count"] > 0, cert),
        check("three routes", decision["accepts_three_equivalent_witness_routes"] is True and set(data["witness_routes"]) == {"typed_monad_cech", "direct_hym", "finite_routec_solve"}, data["witness_routes"]),
        check("current values absent", decision["typed_monad_cech_values_present"] is False and decision["direct_hym_values_present"] is False and decision["finite_routec_solve_values_present"] is False, decision),
        check("finite prefix support only", decision["finite_prefix_may_seed_but_not_fill_payload"] is True and data["finite_prefix_support"]["selected_by_mtt"] is False, data["finite_prefix_support"]),
        check("honest replay blocked", decision["honest_replay_still_blocked"] is True, decision),
        check("no witness closure", decision["selected_connection_witness_constructed"] is False and cert["selected_connection_witness_constructed"] is False, decision),
        check("no downstream closure", data["closure_claimed"] is False and decision["primitive_C1_values_computed"] is False and decision["lambda_12_computable"] is False, decision),
        check("guardrails", guardrails["promotes_finite_prefix_values"] is False and guardrails["promotes_lifted_selected_flags"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note documents routes", "Accepted Witness Routes" in note and "Finite prefix values are support" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C typed monad/Cech or HYM witness audit")
    return 0 if all(audit_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
