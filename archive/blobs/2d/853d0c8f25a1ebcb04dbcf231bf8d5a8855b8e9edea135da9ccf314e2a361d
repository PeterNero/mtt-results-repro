"""Audit the V_alpha extension stability finite-filter attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "attempt_valpha_extension_stability_filter.py"
CERT = ROOT / "certificates" / "valpha_extension_stability_filter_attempt_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "valpha_extension_stability_filter_attempt.candidate.json"
TEMPLATE = (
    ROOT
    / "candidate_data"
    / "valpha_extension_stability_filter"
    / "destabilizer_yoneda_obstruction.template.json"
)
PAPER = CORPUS / "VAlpha_Extension_Stability_Filter_Attempt_v1.md"


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


def vecs(rows: list[dict[str, Any]]) -> list[list[int]]:
    return [row.get("M", []) for row in rows]


def main() -> int:
    proc = run_script()
    cert = load(CERT)
    candidate = load(CANDIDATE)
    template = load(TEMPLATE)
    paper = read(PAPER)

    finite = cert.get("finite_branch_candidate_filter", {})
    closed = cert.get("closed_by_this_attempt", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    selected = cert.get("selected_extension", {})
    chamber = cert.get("selected_chamber", {})
    quotient = finite.get("quotient_destabilizer_result", {})
    displayed = finite.get("displayed_subline_result", {})
    zero = finite.get("residual_zero_slope_candidates", [])
    template_rows = template.get("destabilizer_candidates", [])

    expected_status = (
        "VALPHA_EXTENSION_STABILITY_FILTER_PARTIAL_QUOTIENT_DESTABILIZER_EXCLUDED_YONEDA_OPEN"
    )
    expected_zero = [[-2, 1, 0], [2, -1, 0]]

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1200]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("template exists", "PASS" if TEMPLATE.exists() else "FAIL", TEMPLATE),
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
            "selected extension data",
            "PASS"
            if selected.get("L") == [1, -2, 0]
            and selected.get("L_inverse") == [-1, 2, 0]
            and selected.get("h1") == 8
            and selected.get("selected_ext_closed_not_exact_nonzero") is True
            and selected.get("non_split_extension_proved_by_current_data") is True
            else "FAIL",
            selected,
        ),
        Gate(
            "selected chamber slopes",
            "PASS"
            if chamber.get("p") == [1, 2, 1]
            and chamber.get("mu_L") == -3
            and chamber.get("mu_L_inverse") == 3
            and chamber.get("uses_target_wall_as_filter_not_source_selection") is True
            else "FAIL",
            chamber,
        ),
        Gate(
            "displayed L not destabilizing",
            "PASS"
            if displayed.get("M") == [1, -2, 0]
            and displayed.get("slope_at_selected_p") == -3
            and displayed.get("destabilizing_risk") is False
            else "FAIL",
            displayed,
        ),
        Gate(
            "quotient L inverse excluded",
            "PASS"
            if quotient.get("M") == [-1, 2, 0]
            and quotient.get("status") == "EXCLUDED_BY_NON_SPLIT_EXTENSION"
            and quotient.get("detail", {}).get("closed_by_current_data") is True
            and finite.get("quotient_L_inverse_excluded") is True
            else "FAIL",
            quotient,
        ),
        Gate(
            "only finite zero-slope residuals remain",
            "OPEN"
            if sorted(vecs(zero)) == sorted(expected_zero)
            and finite.get("residual_zero_slope_count") == 2
            and finite.get("residual_positive_slope_count") == 0
            else "FAIL",
            zero,
        ),
        Gate(
            "Yoneda template for residuals",
            "OPEN"
            if template.get("status") == "OPEN_YONEDA_MATRICES_REQUIRED"
            and sorted(vecs(template_rows)) == sorted(expected_zero)
            and all(row.get("pullback_obstruction_matrix") is None for row in template_rows)
            else "FAIL",
            template_rows,
        ),
        Gate(
            "closed subclaims exact",
            "PASS"
            if closed.get("nonzero_ext_implies_non_split") is True
            and closed.get("displayed_L_has_negative_slope") is True
            and closed.get("quotient_L_inverse_subline_excluded_by_non_split") is True
            and closed.get("finite_residual_yoneda_contract_created") is True
            else "FAIL",
            closed,
        ),
        Gate(
            "still open includes full stability blockers",
            "OPEN"
            if still_open.get("complete_destabilizing_subsheaf_enumeration") is True
            and still_open.get("zero_slope_branch_candidate_hom_yoneda_matrices") is True
            and still_open.get("selected_hym_or_strominger_existence_certificate") is True
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
            "paper has required caveats",
            "PASS"
            if contains_all(
                paper,
                [
                    "VAlpha Extension Stability Filter",
                    "quotient `L^-1`",
                    "zero-slope",
                    "Hom/Yoneda",
                    "does not prove full stability",
                    "does not prove HYM existence",
                    "does not prove full SM closure",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("V_alpha extension stability filter attempt audit")
    print("================================================")
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
