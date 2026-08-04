"""Audit the selected monad-difference L^2 source proof attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_selected_monad_difference_l2_source_attempt.py"
CERT = REPO / "certificates" / "selected_monad_difference_l2_source_proof_attempt_certificate.json"
CANDIDATE = REPO / "candidate_data" / "selected_monad_difference_l2_source_proof_attempt.candidate.json"
PAPER = ROOT / "Selected_Monad_Difference_L2_Source_Proof_Attempt_v1.md"


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


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)

    scan = cert.get("terminal_monad_difference_scan", {})
    theorem = cert.get("conditional_uniqueness_theorem", {})
    sufficiency = cert.get("sufficiency_import", {})
    attempt = cert.get("unconditional_selection_attempt", {})
    blockers = attempt.get("open_blockers", {})
    cross_repo = cert.get("cross_repo_consistency", {})
    closes = cert.get("what_this_closes", {})
    does_not_close = cert.get("what_this_does_not_close", {})
    contract = cert.get("minimal_success_contract", {})
    guardrails = cert.get("guardrails", {})

    selected_candidate = scan.get("selected_candidate_inside_lane", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status conditional uniqueness",
            "PASS"
            if cert.get("status")
            == "SELECTED_MONAD_DIFFERENCE_L2_SOURCE_CONDITIONAL_UNIQUENESS_PROVED_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("conditional_uniqueness_theorem")
            == cert.get("conditional_uniqueness_theorem")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "unique target in terminal lane",
            "PASS"
            if scan.get("zero_central_terminal_differences") == ["L3-K2"]
            and scan.get("target_matches") == ["L3-K2"]
            and scan.get("double_target_matches") == ["L3-K2"]
            and selected_candidate.get("value") == [1, -2, 0]
            and selected_candidate.get("double_value") == [2, -4, 0]
            else "FAIL",
            str(scan),
        ),
        Gate(
            "conditional theorem proved",
            "PASS"
            if theorem.get("proved") is True
            and "terminal monad differences L_i-K2" in " ".join(theorem.get("hypotheses", []))
            and "L3-K2=(1,-2,0)" in theorem.get("conclusion", "")
            else "FAIL",
            str(theorem),
        ),
        Gate(
            "dual g3 checked",
            "PASS"
            if theorem.get("dual_g3_check", {}).get("printed_g3_type") == [-1, 2, 0]
            and theorem.get("dual_g3_check", {}).get("is_dual_to_selected_L3_minus_K2")
            is True
            else "FAIL",
            str(theorem.get("dual_g3_check", {})),
        ),
        Gate(
            "sufficiency imported",
            "PASS"
            if sufficiency.get("proved") is True
            and sufficiency.get("hypothetical_selected_packet_passes") is True
            and sufficiency.get("unselected_packet_refused") is True
            else "FAIL",
            str(sufficiency),
        ),
        Gate(
            "unconditional proof honestly blocked",
            "OPEN"
            if attempt.get("proved") is False
            and blockers.get("actual_MTT_selection_of_terminal_monad_difference_lane") is True
            and blockers.get("neutral_Pic0_selection_or_quotient") is True
            and blockers.get("typed_monad_sections_or_equivalent_transition_data") is True
            else "FAIL",
            str(attempt),
        ),
        Gate(
            "cross repo agrees",
            "PASS"
            if cross_repo.get("constants_repo_present") is True
            and cross_repo.get("constants_monad_attempt_agrees_selection_open") is True
            and cross_repo.get("constants_map_attempt_agrees_sections_missing") is True
            else "FAIL",
            str(cross_repo),
        ),
        Gate(
            "closes conditional lane",
            "PASS"
            if closes.get("unique_L3_minus_K2_inside_ordered_terminal_monad_difference_lane")
            is True
            and closes.get("sufficiency_of_selected_monad_difference_imported") is True
            and closes.get("proof_frontier_no_longer_arithmetic") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "does not overclose",
            "PASS"
            if does_not_close.get("unconditional_Selected_Monad_Difference_L2_Source_v1")
            is False
            and does_not_close.get("actual_MTT_selection_of_L3_minus_K2") is False
            and does_not_close.get("Pic0_selection_or_quotient") is False
            and does_not_close.get("full_SM_closure") is False
            else "FAIL",
            str(does_not_close),
        ),
        Gate(
            "success contract exact",
            "PASS"
            if contract.get("name") == "Selected_Monad_Difference_L2_Source.v1"
            and "neutral Pic0 selection, or a theorem quotienting Pic0 from the physical source"
            in contract.get("must_supply", [])
            else "FAIL",
            str(contract),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_unconditional_selected_source_proved") is False
            and all(
                value is False
                for key, value in guardrails.items()
                if key != "claims_unconditional_selected_source_proved"
            )
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records theorem and blocker",
            "PASS"
            if contains_all(
                paper,
                [
                    "Conditional on the source being an ordered terminal monad difference",
                    "L3-K2=(1,-2,0)",
                    "2(L3-K2)=(2,-4,0)",
                    "MTT selection of the terminal monad-difference lane",
                    "is not proved yet from the current corpus",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected monad-difference L2 source proof attempt audit")
    print("=======================================================")
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
