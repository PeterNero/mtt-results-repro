"""Audit Selected_PhiFin_S2_Full_Operator_Error_Bound_or_Source_Theorem_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = (
    REPO
    / "certificates"
    / "selected_phifin_s2_full_operator_error_bound_or_source_theorem_certificate.json"
)
PACKET = (
    REPO
    / "candidate_data"
    / "selected_phifin_s2_full_operator_error_bound_or_source_theorem.candidate.json"
)
NOTE = (
    REPO
    / "proof_corpus"
    / "Selected_PhiFin_S2_Full_Operator_Error_Bound_or_Source_Theorem_v1.md"
)
SCRIPT = (
    REPO
    / "scripts"
    / "build_selected_phifin_s2_full_operator_error_bound_or_source_theorem.py"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = load(CERT)
    packet = load(PACKET)
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
    gap = packet["model_gap_data"]
    routes = packet["two_sufficient_closure_routes"]
    evals = packet["current_closure_evaluation"]
    eta_gate = packet["minimal_new_payload_to_close"]["eta_N_operator_norm_bound"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "CONDITIONAL_OPERATOR_BRIDGE_PROVED_NUMERIC_ETA_SOURCE_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "gap budget computed",
        gap["gamma_model"] > 0
        and gap["epsilon_model"] == 0.0
        and gap["strict_half_gap_budget"] == gap["gamma_model"] / 2.0
        and gap["strict_eta_budget_after_epsilon"] == gap["strict_half_gap_budget"],
        gap,
    )
    ok &= check(
        "conditional bridge only",
        packet["conditional_bridge_theorem"]["proved"] is True
        and evals["conditional_bridge_closed"] is True
        and evals["selected_S2_gap_error_closed"] is False
        and evals["selected_value_emission_closed"] is False,
        evals,
    )
    ok &= check(
        "two routes typed",
        routes["route_A_source_theorem"]["proved"] is False
        and routes["route_B_operator_error_bound"]["proved"] is False
        and routes["route_B_operator_error_bound"]["current_eta_N"] is None,
        routes,
    )
    ok &= check(
        "eta threshold matches packet",
        eta_gate["threshold"] == gap["strict_eta_budget_after_epsilon"]
        and "eta_N" in eta_gate["accepted_if"],
        eta_gate,
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["does_not_claim_eta_N_emitted"] is True
        and cert["guardrails"]["does_not_claim_selected_gap_error_closed"] is True
        and cert["guardrails"]["does_not_promote_source_flags"] is True,
        cert["guardrails"],
    )
    ok &= check(
        "note records threshold and open status",
        "eta_N <" in note and "No such `eta_N` has been emitted yet" in note,
        NOTE,
    )

    print("\nSelected PhiFin S2 full-operator error-bound/source theorem audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
