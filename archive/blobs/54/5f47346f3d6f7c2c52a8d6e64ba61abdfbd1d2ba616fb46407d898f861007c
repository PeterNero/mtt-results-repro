"""Audit the selected Qa/SU3 m=1 rank-two Ext H1 source-data attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_m1_rank2_ext_h1_source_data_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_M1_Rank2_Ext_H1_Source_Data_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_m1_rank2_ext_h1_source_data.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


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


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")

    packet = cert["imported_h1_packet"]
    closes = cert["what_this_closes_conditionally"]
    why_not = cert["why_it_still_does_not_promote"]
    routes = cert["source_selector_options_now"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_M1_RANK2_EXT_H1_CONDITIONAL_PACKET_IMPORTED_SELECTION_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["imported_h1_packet"] == packet
            and computed["why_it_still_does_not_promote"] == why_not
            and computed["source_selector_options_now"] == routes,
            computed["status"],
        ),
        check(
            "finite h1 packet imported",
            packet["candidate_role"] == "UNSELECTED_FIXTURE"
            and packet["source_selected_by_mtt"] is False
            and packet["fixture_only"] is True
            and packet["h1"] == 8
            and packet["d1_d0_zero"] is True
            and packet["nonzero_ext_class"] is True,
            packet,
        ),
        check(
            "conditional closures are exactly finite",
            closes["finite_Cech_Kunneth_H1_packet_exists"] is True
            and closes["d1_d0_zero_and_h1_8_checked"] is True
            and closes["closed_nonexact_ext_vector_exists_in_fixture"] is True
            and closes["ordered_integral_monad_difference_candidate_found"] is True
            and closes["monad_difference_matches_target_L"] is True,
            closes,
        ),
        check(
            "selected promotion still refused",
            packet["promotes_to_non_split_V_alpha_input"] is False
            and why_not["packet_is_unselected_fixture"] is True
            and why_not["validator_refuses_selected_promotion"] is True
            and "source.selected_by_mtt is not true"
            in why_not["ordered_source_gate_open_items"],
            why_not,
        ),
        check(
            "best next handle is monad difference",
            routes[0]["route"] == "monad_difference_L3_minus_K2"
            and routes[0]["status"] == "BEST_LIVE_SELECTION_HANDLE"
            and routes[0]["evidence"]["value"] == [1, -2, 0]
            and routes[0]["evidence"]["double_value"] == [2, -4, 0],
            routes[0],
        ),
        check(
            "guardrails prevent overclaim",
            guardrails["claims_selected_h1_source_data"] is False
            and guardrails["claims_selected_nonzero_Ext_class"] is False
            and guardrails["claims_D_E_dotD_Riesz_Green"] is False
            and guardrails["claims_full_SM_closure"] is False
            and guardrails["uses_observed_flavor_data"] is False,
            guardrails,
        ),
        check(
            "note records next theorem",
            "h1 = 8" in note
            and "UNSELECTED_FIXTURE" in note
            and "L3 - K2 = (1,-2,0)" in note
            and "Selected_Monad_Difference_L2_Source_or_Pic0_Quotient_Theorem_v1"
            in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 m=1 rank-two Ext H1 source-data attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
