"""Audit the V_alpha zero-slope Yoneda reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "attempt_valpha_zero_slope_yoneda_reduction.py"
CERT = ROOT / "certificates" / "valpha_zero_slope_yoneda_reduction_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "valpha_zero_slope_yoneda_reduction.candidate.json"
PARTIAL = (
    ROOT
    / "candidate_data"
    / "valpha_zero_slope_yoneda"
    / "zero_slope_yoneda_reduction.partial.json"
)
SCALAR = (
    ROOT
    / "candidate_data"
    / "valpha_zero_slope_yoneda"
    / "remaining_yoneda_scalar.template.json"
)
PAPER = CORPUS / "VAlpha_Zero_Slope_Yoneda_Reduction_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: object


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run_script() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def row_for(rows: list[dict[str, Any]], vector: list[int]) -> dict[str, Any]:
    for row in rows:
        if row.get("M") == vector:
            return row
    return {}


def main() -> int:
    proc = run_script()
    cert = load(CERT)
    candidate = load(CANDIDATE)
    partial = load(PARTIAL)
    scalar = load(SCALAR)
    paper = read(PAPER)

    reduction = cert.get("zero_slope_reduction", {})
    rows = reduction.get("candidate_rows", [])
    m_left = row_for(rows, [-2, 1, 0])
    m_right = row_for(rows, [2, -1, 0])
    closed = cert.get("closed_by_this_attempt", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    method = cert.get("method", {})

    expected_status = "VALPHA_ZERO_SLOPE_YONEDA_REDUCED_TO_ONE_SCALAR_OPEN"

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1200]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("partial packet exists", "PASS" if PARTIAL.exists() else "FAIL", PARTIAL),
        Gate("scalar template exists", "PASS" if SCALAR.exists() else "FAIL", SCALAR),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status expected",
            "PASS" if cert.get("status") == expected_status else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors cert",
            "PASS" if candidate == cert else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "partial mirrors reduction",
            "PASS"
            if partial.get("status") == "ONE_ZERO_SLOPE_CANDIDATE_MODEL_EXCLUDED_ONE_YONEDA_SCALAR_OPEN"
            and partial.get("candidate_rows") == rows
            else "FAIL",
            partial.get("status"),
        ),
        Gate(
            "exact-sequence method recorded",
            "PASS"
            if "Hom(M,V_alpha)" in method.get("exact_sequence", "")
            and method.get("Q") == [-1, 2, 0]
            and method.get("L") == [1, -2, 0]
            and method.get("slope_chamber_p") == [1, 2, 1]
            else "FAIL",
            method,
        ),
        Gate(
            "M=(2,-1,0) Hom vanishes",
            "PASS"
            if m_right.get("status") == "EXCLUDED_BY_HOM_VANISHING_IN_REDUCED_PULLBACK_MODEL"
            and m_right.get("hom_M_to_L", {}).get("dimension") == 0
            and m_right.get("hom_M_to_Q_L_inverse", {}).get("dimension") == 0
            and m_right.get("closed_in_reduced_pullback_model") is True
            else "FAIL",
            m_right,
        ),
        Gate(
            "M=(-2,1,0) one scalar",
            "OPEN"
            if m_left.get("status") == "REDUCED_TO_SINGLE_YONEDA_SCALAR"
            and m_left.get("hom_M_to_L", {}).get("dimension") == 0
            and m_left.get("hom_M_to_Q_L_inverse", {}).get("dimension") == 1
            and m_left.get("ext1_M_to_L", {}).get("dimension_reduced") == 9
            and m_left.get("closed_in_reduced_pullback_model") is False
            else "FAIL",
            m_left,
        ),
        Gate(
            "scalar template exact",
            "OPEN"
            if scalar.get("status") == "OPEN"
            and scalar.get("M") == [-2, 1, 0]
            and scalar.get("hom_dimension") == 1
            and scalar.get("target_ext_dimension_reduced") == 9
            and scalar.get("current_value") is None
            and scalar.get("required_nonzero_scalar") == "delta_e(sigma_11) != 0"
            else "FAIL",
            scalar,
        ),
        Gate(
            "closed subclaims exact",
            "PASS"
            if closed.get("M_2_minus1_0_has_no_morphism_to_V_in_reduced_model") is True
            and closed.get("M_minus2_1_0_reduced_to_single_yoneda_scalar") is True
            and closed.get("matrix_search_reduced_to_one_scalar_for_finite_branch_candidates") is True
            else "FAIL",
            closed,
        ),
        Gate(
            "still open guarded",
            "OPEN"
            if still_open.get("compute_remaining_yoneda_scalar") is True
            and still_open.get("complete_destabilizing_subsheaf_enumeration") is True
            and still_open.get("promote_reduced_model_to_selected_full_Hom_functor") is True
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
            "paper records reduction and caveats",
            "PASS"
            if contains_all(
                paper,
                [
                    "VAlpha Zero-Slope Yoneda Reduction",
                    "Hom(M,L)=0",
                    "Hom(M,L^-1)",
                    "one Yoneda boundary scalar",
                    "delta_e != 0",
                    "does not by itself prove full stability",
                    "does not prove HYM existence",
                    "does not prove HYM existence or full SM closure",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("V_alpha zero-slope Yoneda reduction audit")
    print("=========================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:<{width}}  {gate.status:<{status_width}}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        print("\nFailures")
        print("--------")
        for failure in failures:
            print(f"- {failure.label}: {failure.detail}")
        return 1

    print("\nResult: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
