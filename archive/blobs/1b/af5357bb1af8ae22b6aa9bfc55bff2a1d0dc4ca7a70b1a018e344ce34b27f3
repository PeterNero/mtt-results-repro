"""Audit the visible rank-two L2 selector obstruction theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_visible_rank2_l2_selector_obstruction.py"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_l2_selector_obstruction.candidate.json"
CERT = REPO / "certificates" / "visible_rank2_l2_selector_obstruction_certificate.json"
PAPER = ROOT / "Visible_Rank2_L2_Selector_Obstruction_Theorem_v1.md"


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

    equality = cert.get("equality_table", {})
    pic0 = cert.get("pic0_invariance", {})
    breaking = cert.get("current_breaking_sources", {})
    obstruction = cert.get("obstruction_theorem", {})
    attempt = cert.get("attempt_to_prove_target_selector", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status source required",
            "PASS"
            if cert.get("status") == "VISIBLE_RANK2_L2_SELECTOR_OBSTRUCTION_PROVED_SOURCE_REQUIRED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("equality_table") == cert.get("equality_table")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "target-swapped degeneracy",
            "PASS"
            if equality.get("target_swapped_by_base_swap") is True
            and equality.get("branch_orbit_under_swap_and_dual") is True
            and equality.get("L_mod3_equal") is True
            and equality.get("L2_mod3_equal") is True
            and equality.get("c2_equal") is True
            and equality.get("h1_equal") is True
            else "FAIL",
            str(equality),
        ),
        Gate(
            "Pic0 degeneracy",
            "PASS"
            if pic0.get("flat_pic0_changes_c1") is False
            and pic0.get("flat_pic0_changes_c2") is False
            and pic0.get("flat_pic0_changes_h1_for_nonzero_elliptic_degrees")
            is False
            and pic0.get("curvature_and_bianchi_terms_can_select_neutral_character")
            is False
            and pic0.get("needs_holonomy_sensitive_source_or_gauge_fixing") is True
            else "FAIL",
            str(pic0),
        ),
        Gate(
            "no current breaking source",
            "PASS"
            if cert.get("no_breaking_source_available") is True
            and breaking.get("selected_target_wall_r1_over_r2_sqrt2") is False
            and breaking.get("selected_ordered_integral_source_for_L2") is False
            and breaking.get("appell_humbert_selected_by_mtt") is False
            and breaking.get("target_branch_selected_by_mtt") is False
            and breaking.get("neutral_pic0_selected_by_mtt") is False
            and breaking.get("time_orientation_maps_to_visible_base_order") is False
            else "FAIL",
            str(breaking),
        ),
        Gate(
            "obstruction theorem scoped",
            "PASS"
            if "No current closed selector" in obstruction.get("theorem", "")
            and "selected target Gauduchon wall r1:r2=sqrt(2):1"
            in obstruction.get("does_not_apply_if_new_source_supplies", [])
            and "same-source D_E/dotD/Hessian term ordering the base factors"
            in obstruction.get("does_not_apply_if_new_source_supplies", [])
            else "FAIL",
            str(obstruction),
        ),
        Gate(
            "target proof honestly failed",
            "PASS"
            if attempt.get("proved_unique_target_selection") is False
            and "do not select" in attempt.get("reason_not_proved", "")
            else "FAIL",
            str(attempt),
        ),
        Gate(
            "closes no-hidden-selector",
            "PASS"
            if closes.get("no_hidden_selector_in_current_topology_h1_qutrit_or_appell_humbert_data")
            is True
            and closes.get("pic0_neutrality_not_selected_by_current_curvature_topology_data")
            is True
            and closes.get("proof_target_reduced_to_new_symmetry_breaking_source") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("selected_target_wall_r1_over_r2_sqrt2") is True
            and still_open.get("selected_ordered_integral_Cech_automorphy_D_E_source")
            is True
            and still_open.get("selected_or_quotiented_Pic0_character") is True
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
                    "Base-Swap Degeneracy",
                    "Pic0 Degeneracy",
                    "cannot uniquely select",
                    "selected target Gauduchon wall",
                    "same-source D_E/dotD/Hessian",
                    "no-hidden-selector theorem",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two L2 selector obstruction audit")
    print("==============================================")
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
