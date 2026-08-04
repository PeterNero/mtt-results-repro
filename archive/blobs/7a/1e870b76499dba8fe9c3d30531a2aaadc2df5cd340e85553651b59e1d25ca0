"""Audit the visible rank-two L2 Appell-Humbert automorphy packet."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "construct_visible_rank2_l2_appell_humbert_automorphy.py"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_l2_appell_humbert_automorphy.candidate.json"
CERT = REPO / "certificates" / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"
PAPER = ROOT / "Visible_Rank2_L2_Appell_Humbert_Automorphy_Source_Attempt_v1.md"


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

    checks = cert.get("construction_checks", {})
    model = cert.get("model", {})
    selection = cert.get("selection_analysis", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    source_scan = cert.get("source_scan", {})
    matrix = model.get("c1_deck_alternating_matrix_order_g1_to_g6", [])

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status selection open",
            "PASS"
            if cert.get("status")
            == "VISIBLE_RANK2_L2_APPELL_HUMBERT_AUTOMORPHY_CONSTRUCTED_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("construction_checks") == cert.get("construction_checks")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "target c1 matrix",
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
            "cocycle and semicharacter",
            "PASS"
            if checks.get("cocycle_law_holds_on_generators_mod_2pi_i") is True
            and checks.get("cocycle_law_holds_on_small_lattice_box_mod_2pi_i") is True
            and checks.get("trivial_semicharacter_allowed_because_c1_pairing_even") is True
            else "FAIL",
            str(checks),
        ),
        Gate(
            "central/shared circle retained",
            "PASS"
            if checks.get("c1_pairing_g5_g6") == 0
            and checks.get("central_shared_circle_trivial") is True
            and closes.get("shared_circle_degree_zero_retained") is True
            else "FAIL",
            str(checks),
        ),
        Gate(
            "ordinary c1 realized",
            "PASS"
            if checks.get("c1_matrix_matches_required_order") is True
            and checks.get("c1_pairing_g1_g2") == 2
            and checks.get("c1_pairing_g3_g4") == -4
            and closes.get("ordinary_integral_c1_matrix_realized") is True
            else "FAIL",
            str(checks),
        ),
        Gate(
            "source scan imported",
            "PASS"
            if source_scan.get("integral_lift_gap_status")
            == "VISIBLE_RANK2_L2_INTEGRAL_LIFT_REDUCED_TO_SOURCE_CERTIFICATE"
            and source_scan.get("constants_automorphy_nogo_present") is True
            else "FAIL",
            str(source_scan),
        ),
        Gate(
            "selection not overclaimed",
            "PASS"
            if selection.get("mathematical_automorphy_representative_constructed") is True
            and selection.get("selected_by_mtt") is False
            and selection.get("target_branch_L_selected_by_mtt") is False
            and selection.get("neutral_pic0_character_selected_by_mtt") is False
            else "FAIL",
            str(selection),
        ),
        Gate(
            "closes formula not selection",
            "PASS"
            if closes.get("explicit_nonflat_factor_of_automorphy_for_L2_2_minus4_0")
            is True
            and closes.get("automorphy_formula_gap_reduced_to_selection_not_existence")
            is True
            and closes.get("finite_torsion_gerbe_not_used_as_ordinary_c1") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("MTT_branch_orientation_selecting_L_1_minus2_0_over_swapped")
            is True
            and still_open.get("MTT_selection_or_elimination_of_flat_Pic0_characters")
            is True
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
                    "Appell-Humbert",
                    "E(g1,g2)= 2",
                    "E(g3,g4)=-4",
                    "E(g5,g6)= 0",
                    "trivial semicharacter",
                    "does not yet have an MTT selection proof",
                    "not an automorphy-existence gap",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two L2 Appell-Humbert automorphy audit")
    print("====================================================")
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
