"""Audit the invariant scalar Dolbeault attempt for the visible L^2 packet."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "attempt_visible_rank2_l2_invariant_dolbeault.py"
VALIDATOR = REPO / "scripts" / "validate_visible_rank2_l2_cohomology.py"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_l2_invariant_dolbeault_attempt.candidate.json"
CERT = REPO / "certificates" / "visible_rank2_l2_invariant_dolbeault_attempt_certificate.json"
PAPER = ROOT / "Visible_Rank2_L2_Invariant_Dolbeault_Attempt_v1.md"


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


def run_fixture(packet: dict[str, Any]) -> tuple[int, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "visible_l2_invariant_fixture.json"
        path.write_text(json.dumps(packet, indent=2), encoding="utf-8")
        proc = run([sys.executable, str(VALIDATOR), str(path)])
        return proc.returncode, proc.stdout


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)

    scan = cert.get("scan_summary", {})
    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    open_items = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    fixture = cert.get("validator_fixture", {}).get("packet", {})
    fixture_code, fixture_output = run_fixture(fixture)

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status blocked needs transitions",
            "PASS"
            if cert.get("status")
            == "VISIBLE_RANK2_L2_INVARIANT_DOLBEAULT_ATTEMPT_BLOCKED_NEEDS_TRANSITIONS"
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
        Gate(
            "scan counts",
            "PASS"
            if scan.get("candidate_count") == 27
            and scan.get("integrable_count") == 9
            and scan.get("positive_h1_count") == 1
            and scan.get("nontrivial_positive_h1_count") == 0
            else "FAIL",
            str(scan),
        ),
        Gate(
            "trivial fixture h1 only",
            "PASS"
            if scan.get("trivial_A_h1") == 2
            and all(value == 0 for value in scan.get("nonzero_integrable_h1_values", {}).values())
            else "FAIL",
            str(scan.get("nonzero_integrable_h1_values")),
        ),
        Gate(
            "target c1 not hit",
            "PASS"
            if scan.get("all_global_scalar_c1_vectors") == [[0, 0, 0]]
            and scan.get("target_c1_L_squared_hit") is False
            and calc.get("invariant_global_scalar_ansatz_hits_target_c1_L_squared") is False
            else "FAIL",
            str({"scan": scan, "calc": calc}),
        ),
        Gate(
            "validator fixture passes as unselected",
            "PASS"
            if fixture_code == 0
            and "validation PASS" in fixture_output
            and "does not promote selected MTT data" in fixture_output
            else "FAIL",
            fixture_output.strip(),
        ),
        Gate(
            "calculation scoped",
            "PASS"
            if calc.get("invariant_scalar_integrability_classified") is True
            and calc.get("trivial_invariant_complex_has_h1_positive") is True
            and calc.get("nontrivial_integrable_invariant_complex_has_h1_positive")
            is False
            and calc.get("selected_L2_packet_constructed") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closes invariant route",
            "PASS"
            if closes.get("simplest_global_invariant_scalar_dolbeault_route_tested")
            is True
            and closes.get("global_scalar_ansatz_cannot_realize_nonzero_c1_L_squared")
            is True
            and closes.get("transition_or_automorphy_data_required") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if open_items.get("construct_selected_L2_transition_or_automorphy_data")
            is True
            and open_items.get("compute_actual_h1_for_nontrivial_L_squared") is True
            and open_items.get("full_SM_closure") is True
            else "FAIL",
            str(open_items),
        ),
        Gate("guardrails", "PASS" if all(value is False for value in guardrails.values()) else "FAIL", str(guardrails)),
        Gate(
            "paper records attempt",
            "PASS"
            if contains_all(
                paper,
                [
                    "global scalar invariant ansatz",
                    "D_A^2=0 iff a3=0",
                    "A=0 has h1=2",
                    "nonzero integrable candidates have h1=0",
                    "c1(L^2)=(2,-4,0)",
                    "transition or automorphy data",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two L2 invariant Dolbeault attempt audit")
    print("=====================================================")
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
