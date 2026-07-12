"""Audit the selected S3 class/restriction closure."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_visible_twisted_s3_class_restriction_closure.py"
VALIDATOR = REPO / "scripts" / "validate_visible_twisted_s3_class_restriction_packet.py"
SELECTED = REPO / "certificates" / "visible_twisted_s3_class_restriction_packet.selected.json"
CANDIDATE = (
    REPO / "candidate_data" / "visible_twisted_s3_class_restriction_closure.candidate.json"
)
CERT = REPO / "certificates" / "visible_twisted_s3_class_restriction_closure_certificate.json"
PAPER = ROOT / "Visible_Twisted_S3_Class_Restriction_Closure_v1.md"


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


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    validator_proc = run([sys.executable, str(VALIDATOR), str(SELECTED)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    selected = load_json(SELECTED)
    paper = read(PAPER)

    table = selected.get("explicit_S3_pullback_table", {})
    orientation = table.get("orientation_checks", {})
    closes = cert.get("what_this_closes", {})
    calc = cert.get("calculation_results", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    retention = cert.get("block_projector_retention", {})

    gates = [
        Gate("constructor exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("selected packet exists", "PASS" if SELECTED.exists() else "FAIL", str(SELECTED)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "closure status",
            "PASS"
            if cert.get("status")
            == "VISIBLE_TWISTED_S3_CLASS_RESTRICTION_CLOSED_OPERATOR_SOURCE_OPEN"
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
            "selected packet validates",
            "PASS"
            if validator_proc.returncode == 0
            and "class/restriction PASS" in validator_proc.stdout
            else "FAIL",
            validator_proc.stdout.strip(),
        ),
        Gate(
            "selected packet exact branch",
            "PASS"
            if selected.get("selected_stack") == "S3"
            and selected.get("branch", {}).get("q") == 79
            and selected.get("branch", {}).get("orientation") == "F"
            and selected.get("branch", {}).get("torsion_label_m") == 1
            else "FAIL",
            str(selected.get("branch", {})),
        ),
        Gate(
            "flat table supplied",
            "PASS"
            if table.get("active_quotient") == "F_3^2"
            and table.get("formula") == "B((a,b),(c,d)) = -c*b/3 mod Z"
            and table.get("curvature_H_form") == "0"
            and len(table.get("entries", [])) == 81
            else "FAIL",
            str({"entries": len(table.get("entries", [])), "formula": table.get("formula")}),
        ),
        Gate(
            "orientation check",
            "PASS"
            if orientation.get("B_e1_e2") == "0/3"
            and orientation.get("B_e2_e1") == "2/3"
            and orientation.get("commutator_e1_e2") == "1/3"
            and orientation.get("q79_F_orientation") is True
            else "FAIL",
            str(orientation),
        ),
        Gate(
            "restriction and FW closed",
            "PASS"
            if calc.get("S3_pullback_table_supplied") is True
            and calc.get("smooth_Freed_Witten_cancellation_closed") is True
            and cert.get("S3_restriction_and_Freed_Witten", {}).get(
                "twisted_CP_DD_matches_B_restriction"
            )
            is True
            else "FAIL",
            str(cert.get("S3_restriction_and_Freed_Witten", {})),
        ),
        Gate(
            "block projector retention scoped",
            "PASS"
            if retention.get("retention_closed") is True
            and "D_E/dotD spectral zero-mode projectors remain separate"
            in retention.get("retention_scope", "")
            else "FAIL",
            str(retention),
        ),
        Gate(
            "what closes",
            "PASS"
            if all(closes.values())
            and closes.get("selected_S3_flat_Deligne_class") is True
            and closes.get("selected_S3_pullback_restriction_table") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "remaining frontier recorded",
            "OPEN"
            if still_open.get("selected_visible_Green_Schwarz_operator_source") is True
            and still_open.get("selected_D_E_dotD_Riesz_Green") is True
            and still_open.get("coherent_spectral_zero_mode_projector_retention") is True
            and still_open.get("full_SM_closure") is True
            else "FAIL",
            str(still_open),
        ),
        Gate("guardrails", "PASS" if all(value is False for value in guardrails.values()) else "FAIL", str(guardrails)),
        Gate(
            "paper records scope",
            "PASS"
            if contains_all(
                paper,
                [
                    "Visible Twisted S3 Class Restriction Closure",
                    "B((a,b),(c,d)) = -c*b/3 mod Z",
                    "block-factorized sector projectors are retained",
                    "not the spectral zero-mode projector theorem",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible twisted S3 class/restriction closure audit")
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
