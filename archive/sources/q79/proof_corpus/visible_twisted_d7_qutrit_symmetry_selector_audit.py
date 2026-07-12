"""Audit the qutrit-symmetry reduction of the visible twisted D7 selector."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "derive_s3_selector_from_qutrit_symmetry.py"
CANDIDATE = REPO / "candidate_data" / "visible_twisted_d7_qutrit_symmetry_selector.candidate.json"
CERT = REPO / "certificates" / "visible_twisted_d7_qutrit_symmetry_selector_certificate.json"
PAPER = ROOT / "Visible_Twisted_D7_Qutrit_Symmetry_Selector_v1.md"


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
    source_hits = cert.get("source_hits", {})
    equal_pairs = cert.get("equal_scale_pairs", [])
    allowed = cert.get("allowed_generator_factor_assignments_under_symmetry", [])
    guardrails = cert.get("guardrails", {})
    still_open = cert.get("still_open", {})
    notation = cert.get("notation_guard", {})
    closes = cert.get("what_this_closes", {})

    gates = [
        Gate("constructor exits 0", "PASS" if code == 0 else "FAIL", output[:900]),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status reduces to S3 embedding rule",
            "PASS"
            if cert.get("status")
            == "VISIBLE_TWISTED_D7_QUTRIT_SYMMETRY_SELECTOR_REDUCES_TO_S3_EMBEDDING_RULE_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "all source inputs present",
            "PASS" if all(source_hits.values()) else "FAIL",
            str(source_hits),
        ),
        Gate(
            "only equal-scale pair is T1,T2",
            "PASS" if equal_pairs == [{"delta": 0.0, "pair": ["T1", "T2"]}] else "FAIL",
            str(equal_pairs),
        ),
        Gate(
            "symmetry-allowed assignments force S3",
            "PASS"
            if len(allowed) == 2
            and {item.get("twisted_projective_D7_stack_required") for item in allowed} == {"S3"}
            and cert.get("forced_twisted_stack_if_embedding_rule_is_proved") == "S3"
            else "FAIL",
            str(allowed),
        ),
        Gate(
            "guardrails prevent overclaim",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "embedding theorem still open",
            "PASS"
            if still_open.get(
                "prove_symmetry_preserving_F3_squared_to_CY_coordinate_embedding_from_MTT_source"
            )
            is True
            and closes.get("unconditional_selected_geometric_source_for_S3") is False
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "notation collision disallowed",
            "PASS"
            if notation.get("central_phase_zeta3_root_and_tier3_zeta_ratio_are_distinct_data")
            is True
            and notation.get("uses_symbol_collision_as_proof") is False
            else "FAIL",
            str(notation),
        ),
        Gate(
            "paper states open theorem",
            "PASS"
            if all(
                needle in paper
                for needle in [
                    "provided the symmetry-preserving embedding rule is proved",
                    "This is not yet the selected S3 source theorem",
                    "does not use a symbol collision",
                ]
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible twisted D7 qutrit-symmetry selector audit")
    print("=================================================")
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
