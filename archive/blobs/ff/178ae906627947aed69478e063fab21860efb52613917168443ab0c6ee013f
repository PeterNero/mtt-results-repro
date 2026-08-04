"""Audit the visible twisted Chan-Paton rescue calculation."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_visible_twisted_chan_paton_rescue.py"
CANDIDATE = REPO / "candidate_data" / "visible_twisted_chan_paton_rescue.candidate.json"
CERT = REPO / "certificates" / "visible_twisted_chan_paton_rescue_certificate.json"
PAPER = ROOT / "Visible_Twisted_Chan_Paton_Rescue_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def run_constructor() -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def main() -> None:
    code, output = run_constructor()
    cert = load_json(CERT)
    paper = read(PAPER)
    projective = cert.get("projective_module_check", {})
    enumeration = cert.get("coordinate_rescue_enumeration", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    assignments = enumeration.get("minimal_rescue_assignments", [])
    one_twisted_stack_each = (
        isinstance(assignments, list)
        and len(assignments) == 6
        and all(item.get("exactly_one_twisted_D7") is True for item in assignments)
        and all(item.get("rank_two_curve_count") == 0 for item in assignments)
    )

    gates = [
        Gate("constructor exits 0", "PASS" if code == 0 else "FAIL", output[:900]),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status rescue reduced selection open",
            "PASS"
            if cert.get("status")
            == "VISIBLE_TWISTED_CP_MINIMAL_COORDINATE_RESCUE_REDUCED_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "projective module matches m1",
            "PASS"
            if projective.get("finite_projective_module_matches_m1_twist") is True
            and projective.get("validator", {}).get("exit") == 0
            and projective.get("carrier_projective_gluing_passes") is True
            and projective.get("carrier_strict_vector_bundle_gluing_passes") is False
            else "FAIL",
            str(projective),
        ),
        Gate(
            "six minimal split assignments",
            "PASS"
            if enumeration.get("split_active_direction_assignments") == 6
            and enumeration.get("minimal_rescue_assignment_count") == 6
            else "FAIL",
            str(enumeration),
        ),
        Gate(
            "one twisted D7, curves ordinary",
            "PASS" if one_twisted_stack_each else "FAIL",
            str(assignments),
        ),
        Gate(
            "all three D7 choices remain",
            "PASS" if enumeration.get("twisted_D7_stack_choices") == ["S1", "S2", "S3"] else "FAIL",
            str(enumeration.get("twisted_D7_stack_choices")),
        ),
        Gate(
            "finite closure and open selection separated",
            "PASS"
            if closes.get("finite_algebraic_twisted_CP_rescue_family_exists") is True
            and still_open.get("selected_choice_of_twisted_D7_stack_S1_or_S2_or_S3") is True
            and still_open.get("physical_worldvolume_flux_or_twisted_Chan_Paton_source_certificate")
            is True
            else "FAIL",
            str({"closes": closes, "still_open": still_open}),
        ),
        Gate(
            "guardrails prevent overclaim",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records conditional nature",
            "PASS"
            if all(
                needle in paper
                for needle in [
                    "conditional projective/twisted route",
                    "one twisted/projective D7 stack",
                    "does not prove full Freed-Witten closure",
                ]
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible twisted Chan-Paton rescue audit")
    print("========================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
