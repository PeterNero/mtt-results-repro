"""Audit the visible rank-two L^2 source ambiguity classification."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "classify_visible_rank2_l2_source_ambiguity.py"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_l2_source_ambiguity_classification.candidate.json"
CERT = REPO / "certificates" / "visible_rank2_l2_source_ambiguity_classification_certificate.json"
PAPER = ROOT / "Visible_Rank2_L2_Source_Ambiguity_Classification_v1.md"


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

    solutions = cert.get("classified_integral_pullback_solutions", [])
    tests = cert.get("selection_tests", {})
    proves = cert.get("what_this_proves", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    l_vectors = [entry.get("l_vector_abc") for entry in solutions]
    h1_values = sorted({entry.get("reduced_pullback_h1") for entry in solutions})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status classified",
            "PASS"
            if cert.get("status")
            == "VISIBLE_RANK2_L2_SOURCE_AMBIGUITY_CLASSIFIED_SELECTION_DATA_REQUIRED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("selection_tests") == cert.get("selection_tests")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "four integral branches",
            "PASS"
            if l_vectors == [[-2, 1, 0], [-1, 2, 0], [1, -2, 0], [2, -1, 0]]
            else "FAIL",
            str(l_vectors),
        ),
        Gate(
            "all branches h1=8",
            "PASS" if h1_values == [8] else "FAIL",
            str(h1_values),
        ),
        Gate(
            "target branch included",
            "PASS"
            if tests.get("target_L_1_minus2_0_is_one_valid_branch") is True
            else "FAIL",
            str(tests),
        ),
        Gate(
            "c2 and h1 do not select unique source",
            "OPEN"
            if tests.get("topological_c2_data_selects_unique_L") is False
            and tests.get("cohomology_dimension_selects_unique_L") is False
            else "FAIL",
            str(tests),
        ),
        Gate(
            "flat ambiguity visible",
            "OPEN"
            if tests.get("flat_Pic0_characters_preserve_c1") is True
            and tests.get("nonzero_elliptic_degrees_make_hodge_dimensions_flat_twist_invariant")
            is True
            and tests.get("hidden_flat_or_torsion_twist_ruled_out_by_current_data") is False
            else "FAIL",
            str(tests),
        ),
        Gate(
            "proved exact obligation",
            "PASS"
            if proves.get("c2_target_forces_base_pullback_no_central_degree") is True
            and proves.get("selected_source_certificate_must_choose_branch_and_twist")
            is True
            else "FAIL",
            str(proves),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("select_L_equals_1_minus2_0_over_the_other_three_c2_branches")
            is True
            and still_open.get("rule_out_or_select_flat_Pic0_character") is True
            and still_open.get("promote_pullback_packet_to_SELECTED_DATA") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_unconditional_selection") is False
            and guardrails.get("claims_c2_or_h1_selects_unique_source") is False
            and guardrails.get("claims_flat_twist_eliminated") is False
            and guardrails.get("uses_observed_flavor_data") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records classification",
            "PASS"
            if contains_all(
                paper,
                [
                    "xy=-2",
                    "four integral branches",
                    "h1=8",
                    "Pic0",
                    "hidden knob",
                    "selected-source certificate",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two L2 source ambiguity classification audit")
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
