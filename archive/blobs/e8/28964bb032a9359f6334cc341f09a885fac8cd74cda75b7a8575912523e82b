"""Audit the terminal admissible-section source principle packet."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "prove_terminal_admissible_section_source_principle.py"
CERT = ROOT / "certificates" / "terminal_admissible_section_source_principle_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "terminal_admissible_section_source_principle.candidate.json"
ORDERED_PACKET = (
    ROOT
    / "candidate_data"
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_ordered_source.selected_under_section_principle.json"
)
COHOMOLOGY_PACKET = (
    ROOT
    / "candidate_data"
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_cohomology.selected_under_section_principle.json"
)
PAPER = CORPUS / "Terminal_Admissible_Section_Source_Principle_for_VAlpha_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: object


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    ordered_proc = run(
        [
            sys.executable,
            str(ROOT / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"),
            str(ORDERED_PACKET),
        ]
    )
    cohomology_proc = run(
        [
            sys.executable,
            str(ROOT / "scripts" / "validate_visible_rank2_l2_cohomology.py"),
            str(COHOMOLOGY_PACKET),
        ]
    )

    cert = load(CERT)
    candidate = load(CANDIDATE)
    ordered_packet = load(ORDERED_PACKET)
    cohomology_packet = load(COHOMOLOGY_PACKET)
    paper = read(PAPER)

    support = cert.get("corpus_support", {})
    checks = cert.get("input_closure_checks", {})
    scan = cert.get("terminal_lane_scan", {})
    selection = cert.get("selection_derivation", {})
    validators = cert.get("validator_results", {})
    closes = cert.get("what_this_closes_under_principle", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1200]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("ordered packet exists", "PASS" if ORDERED_PACKET.exists() else "FAIL", ORDERED_PACKET),
        Gate("cohomology packet exists", "PASS" if COHOMOLOGY_PACKET.exists() else "FAIL", COHOMOLOGY_PACKET),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status under explicit principle",
            "PASS"
            if cert.get("status")
            == "TERMINAL_ADMISSIBLE_SECTION_SOURCE_DERIVED_UNDER_EXPLICIT_PRINCIPLE_STABILITY_OPEN"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors cert",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("selection_derivation") == cert.get("selection_derivation")
            else "FAIL",
            CANDIDATE,
        ),
        Gate("corpus support", "PASS" if support.get("supported") is True else "FAIL", support),
        Gate("input closure checks", "PASS" if checks and all(checks.values()) else "FAIL", checks),
        Gate(
            "terminal lane unique",
            "PASS"
            if scan.get("unique_zero_central") is True
            and scan.get("unique_visible_c2_in_terminal_lane") is True
            and scan.get("zero_central_labels") == ["L3-K2"]
            and scan.get("visible_c2_labels") == ["L3-K2"]
            else "FAIL",
            scan,
        ),
        Gate(
            "selection target",
            "PASS"
            if selection.get("selected_source_label") == "g3 / L3-K2"
            and selection.get("selected_L") == [1, -2, 0]
            and selection.get("selected_L2") == [2, -4, 0]
            and selection.get("selected_c2") == [4, 0, 0]
            else "FAIL",
            selection,
        ),
        Gate(
            "ordered packet selected role",
            "PASS"
            if ordered_packet.get("candidate_role") == "SELECTED_DATA"
            and ordered_packet.get("source", {}).get("selected_by_mtt") is True
            and ordered_packet.get("source", {}).get("source_certificate")
            == "terminal_admissible_section_source_principle_certificate.json"
            else "FAIL",
            ordered_packet.get("source"),
        ),
        Gate(
            "cohomology packet selected role",
            "PASS"
            if cohomology_packet.get("candidate_role") == "SELECTED_DATA"
            and cohomology_packet.get("source", {}).get("selected_by_mtt") is True
            and cohomology_packet.get("reported_cohomology", {}).get("h1") == 8
            else "FAIL",
            cohomology_packet.get("source"),
        ),
        Gate(
            "ordered validator passes",
            "PASS"
            if ordered_proc.returncode == 0
            and validators.get("ordered_source", {}).get("exit_code") == 0
            else "FAIL",
            ordered_proc.stdout,
        ),
        Gate(
            "cohomology validator promotes",
            "PASS"
            if cohomology_proc.returncode == 0
            and "packet promotes the rank-two route" in cohomology_proc.stdout
            and validators.get("cohomology", {}).get("promotes_rank_two_route") is True
            else "FAIL",
            cohomology_proc.stdout,
        ),
        Gate(
            "closes only under principle",
            "PASS"
            if closes.get("terminal_g3_source_selector") is True
            and closes.get("selected_h1_8_L2_cohomology_packet") is True
            and closes.get("selected_nonzero_closed_nonexact_Ext_vector") is True
            else "FAIL",
            closes,
        ),
        Gate(
            "still open is honest",
            "OPEN"
            if still_open.get(
                "promote_principle_to_unconditional_MTT_axiom_or_prove_from_projection_admissibility"
            )
            is True
            and still_open.get("non_split_extension_stability_or_HYM") is True
            and still_open.get("full_SM_closure") is True
            else "FAIL",
            still_open,
        ),
        Gate(
            "guardrails",
            "PASS" if guardrails and all(value is False for value in guardrails.values()) else "FAIL",
            guardrails,
        ),
        Gate(
            "paper records conditional theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "TerminalAdmissibleSectionSourcePrinciple.v1",
                    "Under this principle",
                    "g3 / L3-K2",
                    "h1=8",
                    "nonzero closed non-exact Ext vector",
                    "not full SM closure",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Terminal admissible-section source principle audit")
    print("==================================================")
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
