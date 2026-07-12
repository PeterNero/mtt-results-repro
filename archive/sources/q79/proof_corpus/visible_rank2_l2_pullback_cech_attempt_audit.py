"""Audit the visible L^2 pullback-Cech construction attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "construct_visible_rank2_l2_pullback_cech_attempt.py"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_l2_pullback_cech_attempt.candidate.json"
CERT = REPO / "certificates" / "visible_rank2_l2_pullback_cech_attempt_certificate.json"
PACKET = REPO / "candidate_data" / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"
VALIDATOR = REPO / "scripts" / "validate_visible_rank2_l2_cohomology.py"
PAPER = ROOT / "Visible_Rank2_L2_Pullback_Cech_Attempt_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


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
    validator_proc = run([sys.executable, str(VALIDATOR), str(PACKET)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    packet = load_json(PACKET)
    paper = read(PAPER)

    input_gates = cert.get("input_gates", {})
    automorphy = cert.get("automorphy_checks", {})
    cohomology = cert.get("cohomology_model", {})
    validator = cert.get("validator_packet", {}).get("validation", {})
    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    pullback = cert.get("pullback_model", {})
    matrix = pullback.get("c1_deck_alternating_matrix_order_g1_to_g6", [])

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("packet exists", "PASS" if PACKET.exists() else "FAIL", str(PACKET)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status conditional h1 positive",
            "PASS"
            if cert.get("status")
            == "VISIBLE_RANK2_L2_PULLBACK_CECH_ATTEMPT_CONDITIONAL_H1_POSITIVE_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("calculation_results") == cert.get("calculation_results")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate("input gates", "PASS" if all(input_gates.values()) else "FAIL", str(input_gates)),
        Gate(
            "deck c1 matrix",
            "PASS"
            if matrix
            and matrix[0][1] == 2
            and matrix[1][0] == -2
            and matrix[2][3] == -4
            and matrix[3][2] == 4
            and matrix[4][5] == 0
            and matrix[5][4] == 0
            else "FAIL",
            str(matrix),
        ),
        Gate(
            "automorphy checks",
            "PASS"
            if automorphy.get("integral_alternating_c1_cocycle") is True
            and automorphy.get("factors_through_base_torus") is True
            and automorphy.get("heisenberg_commutator_kernel_compatible") is True
            and automorphy.get("c1_L_squared_square_is_minus_16_alpha1") is True
            and automorphy.get("c2_extension_target_is_plus_4_alpha1") is True
            else "FAIL",
            str(automorphy),
        ),
        Gate(
            "cohomology h1=8",
            "PASS"
            if cohomology.get("base_hodge", {}).get("h0") == 0
            and cohomology.get("base_hodge", {}).get("h1") == 8
            and cohomology.get("conditional_total_h1") == 8
            else "FAIL",
            str(cohomology),
        ),
        Gate(
            "validator packet passes unselected",
            "PASS"
            if validator_proc.returncode == 0
            and validator.get("passes") is True
            and validator.get("promotes_selected_data") is False
            and "does not promote selected MTT data" in validator_proc.stdout
            else "FAIL",
            validator_proc.stdout.strip(),
        ),
        Gate(
            "packet role and target",
            "PASS"
            if packet.get("candidate_role") == "UNSELECTED_FIXTURE"
            and packet.get("target", {}).get("c1_L_squared_vector_abc") == [2, -4, 0]
            and packet.get("reported_cohomology", {}).get("h1") == 8
            else "FAIL",
            str(packet.get("target")),
        ),
        Gate(
            "calculation scoped",
            "PASS"
            if calc.get("pullback_c1_cocycle_constructed") is True
            and calc.get("base_pullback_h1_computed") == 8
            and calc.get("validator_packet_passes") is True
            and calc.get("selected_L2_packet_constructed") is False
            and calc.get("nonzero_Ext_class_selected") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closes conditional route only",
            "PASS"
            if closes.get("integral_deck_c1_cocycle_for_c1_L_squared") is True
            and closes.get("conditional_h1_positive_for_base_pullback_model") is True
            and closes.get("actual_MTT_selection_of_pullback_representative") is False
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("prove_MTT_selects_this_pullback_line_bundle_representative")
            is True
            and still_open.get("prove_non_split_extension_stability") is True
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
            "paper records attempt",
            "PASS"
            if contains_all(
                paper,
                [
                    "pullback from the holomorphic base torus",
                    "c1(L^2)=(2,-4,0)",
                    "h1=8",
                    "UNSELECTED_FIXTURE",
                    "not a raw good-cover transition table",
                    "MTT selects this pullback representative",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two L2 pullback-Cech attempt audit")
    print("===============================================")
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
