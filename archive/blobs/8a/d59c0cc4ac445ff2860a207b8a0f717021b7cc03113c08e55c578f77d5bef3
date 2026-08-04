"""Audit the finite qutrit coupling invariant selection rule."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "iwasawa_block_coupling_invariant_selection_rule_certificate.json"
PAPER = ROOT / "Iwasawa_Block_Coupling_Invariant_Selection_Rule_v1.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_block_coupling_invariants.py"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def run_analysis() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    analysis = run_analysis()
    calc = cert.get("calculation_results", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    pair_dims = analysis.get("pair_fixed_dimensions", {})
    same = analysis.get("same_twist_all_family", {})
    conjugate_right = analysis.get("conjugate_right_family", {})
    conjugate_left = analysis.get("conjugate_left_family", {})
    e6_like = analysis.get("e6_like_three_same_twists", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "IWASAWA_BLOCK_COUPLING_INVARIANT_SELECTION_RULE_FORMULATED_ORIENTATION_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "pair invariant table",
            "PASS"
            if pair_dims == calc.get("pair_fixed_dimensions")
            and pair_dims.get("1+2") == 1
            and pair_dims.get("2+1") == 1
            and pair_dims.get("1+1") == 0
            and pair_dims.get("2+2") == 0
            else "FAIL",
            str(pair_dims),
        ),
        Gate(
            "allowed orientations",
            "PASS"
            if analysis.get("allowed_nontrivial_pair_orientations") == ["1+2", "2+1"]
            else "FAIL",
            str(analysis.get("allowed_nontrivial_pair_orientations")),
        ),
        Gate(
            "same twist blocked",
            "PASS"
            if same.get("all_four_sm_pairs_allowed") is False
            and all(value == 0 for value in same.get("sm_yukawa_pair_fixed_dimensions", {}).values())
            else "FAIL",
            str(same),
        ),
        Gate(
            "conjugate right allowed",
            "PASS"
            if conjugate_right.get("all_four_sm_pairs_allowed") is True
            and all(
                value == 1
                for value in conjugate_right.get("sm_yukawa_pair_fixed_dimensions", {}).values()
            )
            else "FAIL",
            str(conjugate_right),
        ),
        Gate(
            "conjugate left allowed",
            "PASS"
            if conjugate_left.get("all_four_sm_pairs_allowed") is True
            and all(
                value == 1
                for value in conjugate_left.get("sm_yukawa_pair_fixed_dimensions", {}).values()
            )
            else "FAIL",
            str(conjugate_left),
        ),
        Gate(
            "E6 cubic comparison",
            "PASS"
            if e6_like.get("fixed_dimension") == 3
            and e6_like.get("central_orientation_sum_mod3") == 0
            else "FAIL",
            str(e6_like),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("same_twist_all_family_all_four_SM_pairs_allowed") is False
            and calc.get("conjugate_right_family_all_four_SM_pairs_allowed") is True
            and calc.get("conjugate_left_family_all_four_SM_pairs_allowed") is True
            and calc.get("e6_like_three_same_twists_fixed_dimension") == 3
            and calc.get("trivial_Higgs_line_requires_pair_sum_zero_mod3") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("finite_coupling_rule_formulated") is True
            and verdict.get("same_twist_all_family_rejected_for_SM_Higgs_line") is True
            and verdict.get("conjugate_orientation_pairing_needed") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records rule",
            "PASS"
            if contains_all(
                paper,
                [
                    "s_left + s_right = 0 mod 3",
                    "1+2, 2+1",
                    "fixed_dimension = 3",
                    "MTT-selected sector orientation assignment",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa block coupling invariant selection-rule audit")
    print("=====================================================")
    print()
    print(f"allowed_nontrivial_pair_orientations={analysis.get('allowed_nontrivial_pair_orientations')}")
    print(
        "same_twist_all_family_allowed="
        f"{same.get('all_four_sm_pairs_allowed')}"
    )
    print(
        "conjugate_right_family_allowed="
        f"{conjugate_right.get('all_four_sm_pairs_allowed')}"
    )
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
