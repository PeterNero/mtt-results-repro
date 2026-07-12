"""Audit Selected_Terminal_Monad_Lane_Source_Selector_v1 attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_terminal_monad_lane_source_selector_attempt_certificate.json"
PACKET = REPO / "certificates" / "selected_terminal_monad_lane_source_selector.if_axiom_packet.json"
SCRIPT = REPO / "scripts" / "attempt_selected_terminal_monad_lane_source_selector.py"
NOTE = REPO / "proof_corpus" / "Selected_Terminal_Monad_Lane_Source_Selector_Attempt_v1.md"


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

    closed = cert["closed_now"]
    not_closed = cert["not_closed"]
    routes = cert["candidate_routes"]
    guards = cert["guardrails"]
    validators = cert["validator_tests"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "TERMINAL_MONAD_LANE_SOURCE_SELECTOR_REDUCED_TO_BASE_ORDER_BREAKING_SOURCE_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "Pic0 local blocker removed",
        closed["pic0_removed_as_local_ordered_gate_blocker"] is True,
        closed,
    )
    ok &= check(
        "terminal lane conditional uniqueness imported",
        closed["terminal_lane_conditional_uniqueness_imported"] is True
        and closed["L3_minus_K2_forced_if_terminal_lane_selected"] is True,
        cert["selected_candidate_if_terminal_lane_selected"],
    )
    ok &= check(
        "strict validator passes with exact selector",
        validators["pic0_quotient_plus_terminal_source_axiom"]["exit_code"] == 0
        and validators["pic0_quotient_plus_terminal_source_axiom"]["status"] == "PASS"
        and closed["validator_passes_if_exact_source_axiom_added"] is True,
        validators,
    )
    ok &= check(
        "without selector remains open only on source evidence",
        validators["pic0_quotient_without_source_axiom"]["exit_code"] == 2
        and "source.selected_by_mtt is not true"
        in validators["pic0_quotient_without_source_axiom"]["open_items"]
        and "Pic0 resolution rule missing" not in validators["pic0_quotient_without_source_axiom"]["open_items"],
        validators["pic0_quotient_without_source_axiom"],
    )
    ok &= check(
        "current invariants refuted as selector",
        routes["R1_current_closed_invariants"]["status"] == "REFUTED_BY_BASE_SWAP_OBSTRUCTION"
        and routes["R1_current_closed_invariants"]["can_select_terminal_lane"] is False,
        routes["R1_current_closed_invariants"],
    )
    ok &= check(
        "remaining theorem is base-order-breaking source",
        cert["minimal_remaining_source_theorem"]["name"] == "Base_Order_Breaking_Terminal_Lane_Source_v1"
        and not_closed["base_order_breaking_source"] is True
        and not_closed["derived_terminal_monad_lane_selector"] is True,
        cert["minimal_remaining_source_theorem"],
    )
    ok &= check(
        "guardrails prevent overclaim",
        guards["claims_terminal_lane_selector_proved"] is False
        and guards["claims_base_order_source_proved"] is False
        and guards["claims_same_source_operator_packet_constructed"] is False
        and guards["claims_full_SM_closure"] is False
        and guards["uses_observed_flavor_data"] is False
        and guards["uses_benchmark_flavor_entries"] is False,
        guards,
    )
    ok &= check(
        "if-axiom packet marked selected only as test",
        packet["source"]["selected_by_mtt"] is True
        and packet["source"]["source_certificate"] == "Selected_Terminal_Monad_Lane_Source_Selector.v1"
        and packet["pic0_resolution"]["resolution"] == "pic0_quotient_rule",
        packet["source"],
    )
    ok &= check(
        "note records open boundary",
        "derived terminal monad lane selector: open" in note
        and "strict validator pass if exact selector is supplied: yes" in note,
        NOTE,
    )

    print("\nSelected terminal monad lane source selector attempt audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
