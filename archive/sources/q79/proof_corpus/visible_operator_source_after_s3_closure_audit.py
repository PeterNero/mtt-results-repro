"""Audit the visible operator-source reduction after selected S3 closure."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_visible_operator_source_after_s3_closure.py"
CANDIDATE = REPO / "candidate_data" / "visible_operator_source_after_s3_closure.candidate.json"
CERT = REPO / "certificates" / "visible_operator_source_after_s3_closure_certificate.json"
PAPER = ROOT / "Visible_Operator_Source_After_S3_Closure_v1.md"


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


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)
    retired_s3 = cert.get("retired_by_selected_s3_closure", {})
    retired_curv = cert.get("retired_by_visible_curvature_closure", {})
    cut_set = cert.get("still_open_cut_set", {})
    calc = cert.get("calculation_results", {})
    guardrails = cert.get("guardrails", {})
    target = cert.get("operator_source_target", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status reduced not closed",
            "PASS"
            if cert.get("status")
            == "VISIBLE_OPERATOR_SOURCE_REDUCED_TO_SELECTED_CW_OPERATOR_SOURCE_OPEN"
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
        Gate("S3 blockers retired", "PASS" if all(retired_s3.values()) else "FAIL", str(retired_s3)),
        Gate(
            "curvature blockers retired",
            "PASS" if all(retired_curv.values()) else "FAIL",
            str(retired_curv),
        ),
        Gate(
            "operator cut set remains",
            "OPEN"
            if cut_set.get("selected_visible_bundle_or_sheaf_model") is True
            and cut_set.get("Chern_Weil_row_derived_from_selected_source") is True
            and cut_set.get("selected_D_E_dotD_Riesz_Green") is True
            and cut_set.get("coherent_spectral_zero_mode_projectors") is True
            else "FAIL",
            str(cut_set),
        ),
        Gate(
            "calculation scoped",
            "PASS"
            if calc.get("old_s3_gerbe_fw_projector_blockers_retired") is True
            and calc.get("operator_source_cut_set_still_open") is True
            and calc.get("blocker_reduced_not_closed") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "target lists D_E path",
            "PASS"
            if contains_all(
                " ".join(target.get("must_supply_next", [])),
                ["Chern-Weil", "D_E", "Riesz", "dotD_alpha1", "primitive C1"],
            )
            else "FAIL",
            str(target),
        ),
        Gate("guardrails", "PASS" if all(value is False for value in guardrails.values()) else "FAIL", str(guardrails)),
        Gate(
            "paper records reduction",
            "PASS"
            if contains_all(
                paper,
                [
                    "Retired Blockers",
                    "Remaining Cut Set",
                    "selected visible Chern-Weil operator source",
                    "does not claim",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible operator source after S3 closure audit")
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
