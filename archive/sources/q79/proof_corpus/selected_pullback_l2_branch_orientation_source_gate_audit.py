"""Audit the pullback L^2 branch-orientation source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "build_selected_pullback_l2_branch_orientation_source_gate.py"
CANDIDATE = REPO / "candidate_data" / "selected_pullback_l2_branch_orientation_source_gate.candidate.json"
CERT = REPO / "certificates" / "selected_pullback_l2_branch_orientation_source_gate_certificate.json"
PAPER = ROOT / "Selected_Pullback_L2_Branch_Orientation_Source_Gate_v1.md"


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

    finite = cert.get("finite_qutrit_gate", {})
    chamber = cert.get("gauduchon_chamber_gate", {})
    chambers = chamber.get("chambers", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    routes = {route.get("id"): route for route in cert.get("source_routes", [])}

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status reduced",
            "PASS"
            if cert.get("status")
            == "PULLBACK_L2_BRANCH_ORIENTATION_GATE_REDUCED_TO_WALL_OR_INTEGRAL_LIFT"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("finite_qutrit_gate") == cert.get("finite_qutrit_gate")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "finite qutrit cannot distinguish target and swap",
            "OPEN"
            if finite.get("target_and_swapped_same_finite_signature") is True
            and finite.get("distinguishes_target_from_swapped") is False
            and finite.get("target_signature", {}).get("active_F3_2_image") == [1, 1]
            and finite.get("swapped_signature", {}).get("active_F3_2_image") == [1, 1]
            and finite.get("target_signature", {}).get("m1_self_period_B1_v_v") == "2/3"
            else "FAIL",
            str(finite),
        ),
        Gate(
            "target wall is identified",
            "OPEN"
            if chamber.get("target_wall_would_select_L_1_minus2_0") is True
            and chamber.get("current_selected_wall_source_present") is False
            and chambers.get("target_wall", {}).get("negative_branches") == [[1, -2, 0]]
            else "FAIL",
            str(chamber),
        ),
        Gate(
            "conjugate wall recorded",
            "OPEN"
            if chamber.get("swapped_wall_would_select_L_minus2_1_0") is True
            and chambers.get("swapped_wall", {}).get("negative_branches") == [[-2, 1, 0]]
            else "FAIL",
            str(chamber),
        ),
        Gate(
            "equal radius does not select target",
            "OPEN"
            if chamber.get("equal_radius_sources", {}).get("supports_symmetric_not_wall_chamber")
            is True
            and chamber.get("equal_radius_sources", {}).get("selects_target_branch") is False
            and chamber.get("symmetric_shared_base_selects_unique_branch") is False
            else "FAIL",
            str(chamber.get("equal_radius_sources", {})),
        ),
        Gate(
            "live routes are honest",
            "OPEN"
            if routes.get("selected_gauduchon_wall_p1_p2_1_2", {}).get("status")
            == "LIVE_NOT_SOURCE_CERTIFIED"
            and routes.get("integral_deck_or_cech_lift_ordering_base_factors", {}).get(
                "status"
            )
            == "LIVE_NOT_SOURCE_CERTIFIED"
            else "FAIL",
            str(routes),
        ),
        Gate(
            "closes finite no-go",
            "PASS"
            if closes.get("finite_qutrit_orientation_cannot_select_between_target_and_swapped")
            is True
            and closes.get("selected_orientation_source_must_be_stronger_than_F3_quotient")
            is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("source_certified_p1_p2_1_2_wall_or_near_wall_chamber")
            is True
            and still_open.get("integral_lift_from_finite_qutrit_image_to_integer_branch")
            is True
            and still_open.get("flat_pic0_or_torsion_character_selection") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_L_branch_selected") is False
            and guardrails.get("claims_q79_F_finite_data_selects_L_branch") is False
            and guardrails.get("claims_p1_p2_1_2_wall_selected") is False
            and guardrails.get("uses_observed_flavor_data") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "finite qutrit",
                    "cannot distinguish",
                    "p1:p2 = 1:2",
                    "integral lift",
                    "Selected_Pullback_L2_Branch_Orientation_Source",
                    "full SM closure",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected pullback L2 branch-orientation source gate audit")
    print("=========================================================")
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
