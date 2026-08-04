"""Audit the visible twisted D7 volume-selector attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "attempt_select_visible_twisted_d7_by_volume.py"
CANDIDATE = REPO / "candidate_data" / "visible_twisted_d7_volume_selector_attempt.candidate.json"
CERT = REPO / "certificates" / "visible_twisted_d7_volume_selector_attempt_certificate.json"
PAPER = ROOT / "Visible_Twisted_D7_Volume_Selector_Attempt_v1.md"


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
    data = cert.get("executed_volume_data", {})
    computed = data.get("computed_from_tier3", {})
    tau = computed.get("tau", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    selector = cert.get("conditional_selector", {})

    gates = [
        Gate("constructor exits 0", "PASS" if code == 0 else "FAIL", output[:900]),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status conditional S3",
            "PASS"
            if cert.get("status")
            == "VISIBLE_TWISTED_D7_VOLUME_SELECTOR_ATTEMPT_S3_CONDITIONAL_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source hits present",
            "PASS" if all(data.get("source_hits", {}).values()) else "FAIL",
            str(data.get("source_hits", {})),
        ),
        Gate(
            "tau ordering singles out S3",
            "PASS"
            if tau.get("S3", 99) < tau.get("S1", 0)
            and abs(tau.get("S1", 0) - tau.get("S2", 1)) < 1e-12
            and cert.get("volume_ordering", [{}])[0].get("stack") == "S3"
            else "FAIL",
            str(tau),
        ),
        Gate(
            "conditional selector does not overclaim",
            "PASS"
            if selector.get("selected_if_rule_is_added") == "S3"
            and "rule_not_yet_proved" in selector
            and closes.get("unconditional_MTT_selection_of_S3") is False
            and still_open.get("prove_MTT_volume_or_anisotropy_rule_for_twisted_stack") is True
            else "FAIL",
            str({"selector": selector, "closes": closes, "still_open": still_open}),
        ),
        Gate(
            "guardrails prevent overclaim",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper states conditional nature",
            "PASS"
            if all(
                needle in paper
                for needle in [
                    "conditional selector attempt",
                    "unique volume-distinguished candidate",
                    "This is not a proof that MTT selects S3",
                ]
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible twisted D7 volume-selector attempt audit")
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
