"""Audit the visible rank-two L2 ordered-source promotion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "build_visible_rank2_l2_ordered_source_promotion_gate.py"
VALIDATOR = REPO / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"
CERT = REPO / "certificates" / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_l2_ordered_source_promotion_gate.candidate.json"
TEMPLATE = REPO / "certificates" / "visible_rank2_l2_ordered_source.template.json"
ATTEMPT = REPO / "candidate_data" / "visible_rank2_l2_ordered_source.current_attempt.json"
PAPER = ROOT / "Visible_Rank2_L2_Ordered_Source_Promotion_Gate_v1.md"


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
    template = load_json(TEMPLATE)
    attempt = load_json(ATTEMPT)
    paper = read(PAPER)

    validations = cert.get("validation_results", {})
    template_validation = validations.get("template", {})
    attempt_validation = validations.get("current_appell_humbert_attempt", {})
    attempt_open = attempt_validation.get("parsed_report", {}).get("open_items", [])
    blockers = cert.get("blockers", {})
    contract = cert.get("promotion_contract", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    matrix = cert.get("target_ordered_matrix", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("validator exists", "PASS" if VALIDATOR.exists() else "FAIL", str(VALIDATOR)),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("template exists", "PASS" if TEMPLATE.exists() else "FAIL", str(TEMPLATE)),
        Gate("current attempt exists", "PASS" if ATTEMPT.exists() else "FAIL", str(ATTEMPT)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status formulated",
            "PASS"
            if cert.get("status")
            == "VISIBLE_RANK2_L2_ORDERED_SOURCE_PROMOTION_GATE_FORMULATED_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("promotion_contract") == cert.get("promotion_contract")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "template is open",
            "OPEN"
            if template.get("schema") == "VisibleRank2L2OrderedSourcePacket.v1"
            and template.get("status") == "OPEN"
            and template_validation.get("exit_code") == 2
            else "FAIL",
            str(template_validation),
        ),
        Gate(
            "current attempt refused",
            "OPEN"
            if attempt.get("candidate_role") == "UNSELECTED_FIXTURE"
            and attempt_validation.get("exit_code") == 2
            and "source status is not a selected ordered-source status" in attempt_open
            and "Pic0 character not selected or quotiented" in attempt_open
            else "FAIL",
            str(attempt_validation),
        ),
        Gate(
            "ordered matrix fixed",
            "PASS"
            if matrix.get("L") == [1, -2, 0]
            and matrix.get("L2") == [2, -4, 0]
            and matrix.get("E_g1_g2") == 2
            and matrix.get("E_g3_g4") == -4
            and matrix.get("E_g5_g6") == 0
            else "FAIL",
            str(matrix),
        ),
        Gate(
            "blockers identified",
            "PASS"
            if blockers.get("explicit_appell_humbert_formula_exists") is True
            and blockers.get("finite_mod3_qutrit_not_enough") is True
            and blockers.get("equal_radius_import_ruled_out") is True
            and blockers.get("current_appell_humbert_packet_refused_by_validator") is True
            and blockers.get("missing_selected_source_status") is True
            and blockers.get("missing_base_order_selection") is True
            and blockers.get("missing_pic0_resolution") is True
            else "FAIL",
            str(blockers),
        ),
        Gate(
            "promotion contract complete",
            "PASS"
            if contract.get("must_supply_selected_source_status") is True
            and contract.get("must_select_standard_lattice_or_equivalent") is True
            and contract.get("must_break_target_vs_swapped_base_swap") is True
            and contract.get("must_resolve_pic0")
            == [
                "neutral_character_selected",
                "pic0_quotient_rule",
                "specific_flat_character_selected",
            ]
            else "FAIL",
            str(contract),
        ),
        Gate(
            "closes executable gate",
            "PASS"
            if closes.get("ordered_source_packet_schema_and_validator") is True
            and closes.get("current_appell_humbert_packet_correctly_refused_as_unselected_fixture")
            is True
            and closes.get("remaining_ordered_source_gap_made_machine_checkable") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("selected_ordered_integral_source_certificate") is True
            and still_open.get("pic0_selection_or_quotient_rule") is True
            and still_open.get("same_source_D_E_dotD_Riesz_Green") is True
            and still_open.get("full_SM_closure") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "ordered-source promotion gate",
                    "E(g1,g2)=2",
                    "E(g3,g4)=-4",
                    "UNSELECTED_FIXTURE",
                    "Pic0",
                    "not enough that the Appell-Humbert formula exists",
                    "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two L2 ordered-source promotion gate audit")
    print("======================================================")
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
