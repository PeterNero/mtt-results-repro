"""Audit the unconditional selected monad-difference L^2 source attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "attempt_unconditional_selected_monad_difference_l2_source.py"
CERT = REPO / "certificates" / "unconditional_selected_monad_difference_l2_source_attempt_certificate.json"
CANDIDATE = REPO / "candidate_data" / "unconditional_selected_monad_difference_l2_source_attempt.candidate.json"
PAPER = ROOT / "Unconditional_Selected_Monad_Difference_L2_Source_Attempt_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def route(cert: dict[str, Any], key: str) -> dict[str, Any]:
    return cert.get("route_results", {}).get(key, {})


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)

    already = cert.get("already_closed", {})
    attempt = cert.get("unconditional_theorem_attempt", {})
    closes = cert.get("what_this_closes", {})
    does_not_close = cert.get("what_this_does_not_close", {})
    minimal = cert.get("minimal_new_statement_that_would_close", {})
    guardrails = cert.get("guardrails", {})

    r1 = route(cert, "R1_direct_corpus_selector")
    r2 = route(cert, "R2_flux_monad_table")
    r3 = route(cert, "R3_core_cech_overlap_principle")
    r4 = route(cert, "R4_minimality_or_reuse_principle")
    r5 = route(cert, "R5_pic0_selection_or_quotient")
    r6 = route(cert, "R6_same_source_operator_or_hessian")
    r7 = route(cert, "R7_constants_terminal_lane_attempt")

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status blocked honestly",
            "PASS"
            if cert.get("status")
            == "UNCONDITIONAL_SELECTED_MONAD_DIFFERENCE_L2_SOURCE_ATTEMPT_BLOCKED_NO_SELECTOR_OR_PIC0_RULE"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("unconditional_theorem_attempt")
            == cert.get("unconditional_theorem_attempt")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "imports closed conditional pieces",
            "PASS"
            if already.get("conditional_uniqueness_of_L3_minus_K2_inside_terminal_lane")
            is True
            and already.get("selected_monad_difference_would_pass_validator") is True
            and already.get("current_closed_invariants_have_no_hidden_selector") is True
            else "FAIL",
            str(already),
        ),
        Gate(
            "direct selector absent",
            "PASS"
            if r1.get("status") == "FAIL_ABSENT"
            and r1.get("passes") is False
            and r1.get("hits") == []
            else "FAIL",
            str(r1),
        ),
        Gate(
            "flux table candidate only",
            "PASS"
            if r2.get("status") == "CANDIDATE_ONLY"
            and r2.get("passes") is False
            and r2.get("evidence", {}).get("monad_table_present") is True
            and r2.get("evidence", {}).get("selection_language_present") is False
            else "FAIL",
            str(r2),
        ),
        Gate(
            "cech language not selector",
            "PASS"
            if r3.get("status") == "LANGUAGE_ONLY"
            and r3.get("passes") is False
            and r3.get("evidence", {}).get("core_supplies_cech_language") is True
            and r3.get("evidence", {}).get("core_selects_specific_L3_minus_K2_or_Pic0")
            is False
            else "FAIL",
            str(r3),
        ),
        Gate(
            "minimality insufficient",
            "PASS"
            if r4.get("status") == "INSUFFICIENT_WITHOUT_FORMAL_SELECTOR"
            and r4.get("passes") is False
            and r4.get("evidence", {}).get("primary_rank2_route_identified") is True
            else "FAIL",
            str(r4),
        ),
        Gate(
            "pic0 absent",
            "PASS"
            if r5.get("status") == "FAIL_ABSENT"
            and r5.get("passes") is False
            and r5.get("evidence", {}).get("no_hidden_pic0_selector_theorem") is True
            and r5.get("evidence", {}).get("sufficiency_still_requires_pic0") is True
            else "FAIL",
            str(r5),
        ),
        Gate(
            "operator selector absent",
            "PASS"
            if r6.get("status") == "FAIL_ABSENT"
            and r6.get("passes") is False
            and r6.get("evidence", {}).get("selected_D_E_source_absent") is True
            and r6.get("evidence", {}).get("same_source_D_E_constructed") is False
            else "FAIL",
            str(r6),
        ),
        Gate(
            "constants attempt corroborates blocker",
            "PASS"
            if r7.get("status") == "CORROBORATES_BLOCKER"
            and r7.get("passes") is False
            and r7.get("evidence", {}).get("conditional_uniqueness_closed") is True
            and r7.get("evidence", {}).get("terminal_lane_selector_closed") is False
            and r7.get("evidence", {}).get("pic0_still_open") is True
            else "FAIL",
            str(r7),
        ),
        Gate(
            "unconditional theorem blocked",
            "OPEN"
            if attempt.get("proved") is False
            and attempt.get("source_lane_selected") is False
            and attempt.get("pic0_resolved") is False
            else "FAIL",
            str(attempt),
        ),
        Gate(
            "closes route audit",
            "PASS"
            if closes.get("exhaustive_current_route_audit_for_unconditional_selection")
            is True
            and closes.get("direct_corpus_selector_absence_checked") is True
            and closes.get("cross_repo_terminal_lane_attempt_agrees_blocked") is True
            and closes.get("proof_blocker_is_source_selector_plus_pic0") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "does not overclose",
            "PASS"
            if does_not_close.get("unconditional_Selected_Monad_Difference_L2_Source_v1")
            is False
            and does_not_close.get("actual_MTT_selection_of_terminal_monad_difference_lane")
            is False
            and does_not_close.get("neutral_Pic0_selection_or_quotient") is False
            and does_not_close.get("full_SM_closure") is False
            else "FAIL",
            str(does_not_close),
        ),
        Gate(
            "minimal new statement exact",
            "PASS"
            if "terminal monad differences L_i-K2" in minimal.get("source_lane_selector", "")
            and "Pic0" in minimal.get("pic0_rule", "")
            and "previous conditional uniqueness theorem forces L3-K2"
            in minimal.get("why_enough", "")
            else "FAIL",
            str(minimal),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records all routes",
            "PASS"
            if contains_all(
                paper,
                [
                    "R1: Direct Corpus Selector",
                    "R2: Flux Monad Table",
                    "R3: Core Cech Principle",
                    "R4: Minimality and Reuse",
                    "R5: Pic0",
                    "R6: Same-Source Operator or Hessian",
                    "R7: Constants Terminal-Lane Attempt",
                    "The unconditional theorem is not proved from the current corpus.",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Unconditional selected monad-difference L2 source attempt audit")
    print("================================================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
