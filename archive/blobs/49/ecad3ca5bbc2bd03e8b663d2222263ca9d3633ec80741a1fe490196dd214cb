"""Audit the consolidated non-SM constants status matrix."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERTIFICATES = REPO / "certificates"
CERT = CERTIFICATES / "nonsm_constants_status_matrix_certificate.json"
PAPER = ROOT / "NonSM_Constants_Status_Matrix_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def contains_all(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def row(rows: list[dict], row_id: str) -> dict:
    for item in rows:
        if item.get("id") == row_id:
            return item
    return {}


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    rows = cert.get("rows", [])
    statuses = {item.get("status") for item in rows}
    frontier = cert.get("frontier", {})
    verdict = cert.get("verdict", {})
    referenced = [CERTIFICATES / item.get("certificate", "") for item in rows]

    gates = [
        Gate(
            "certificate status",
            "PASS" if cert.get("status") == "STATUS_MATRIX_CERTIFIED" else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "all referenced certificates present",
            "PASS" if all(path.exists() for path in referenced) else "FAIL",
            str([str(path) for path in referenced if not path.exists()]),
        ),
        Gate(
            "status taxonomy used",
            "PASS"
            if statuses
            == {
                "CONDITIONAL_NO_KNOB",
                "RATIO_NO_KNOB",
                "STRUCTURAL_CONSISTENCY",
                "REPAIR_CERTIFIED",
                "OPEN_NORMALIZATION",
                "FORBIDDEN_UNIT_CONVENTION",
            }
            else "FAIL",
            str(sorted(statuses)),
        ),
        Gate(
            "tensor row",
            "PASS"
            if row(rows, "theta_tensor_bound").get("status") == "CONDITIONAL_NO_KNOB"
            and "1.56e-30" in row(rows, "theta_tensor_bound").get("current_result", "")
            else "FAIL",
            str(row(rows, "theta_tensor_bound")),
        ),
        Gate(
            "axion row",
            "PASS"
            if row(rows, "execution_i_axion_ratios").get("status") == "RATIO_NO_KNOB"
            and "4.366812227074235" in row(rows, "execution_i_axion_ratios").get("current_result", "")
            else "FAIL",
            str(row(rows, "execution_i_axion_ratios")),
        ),
        Gate(
            "threshold row not overclaimed",
            "PASS"
            if row(rows, "execution_i_threshold_profile").get("status") == "STRUCTURAL_CONSISTENCY"
            and "derive exceptional coefficients" in row(rows, "execution_i_threshold_profile").get("next_gate", "")
            else "FAIL",
            str(row(rows, "execution_i_threshold_profile")),
        ),
        Gate(
            "large-volume repair row",
            "PASS"
            if row(rows, "execution_i_large_volume_repair").get("status") == "REPAIR_CERTIFIED"
            and "s=5" in row(rows, "execution_i_large_volume_repair").get("current_result", "")
            else "FAIL",
            str(row(rows, "execution_i_large_volume_repair")),
        ),
        Gate(
            "normalization blockers remain open",
            "PASS"
            if row(rows, "newton_planck_normalization").get("status") == "OPEN_NORMALIZATION"
            and row(rows, "execution_i_eft_status").get("status") == "OPEN_NORMALIZATION"
            else "FAIL",
            str([row(rows, "newton_planck_normalization"), row(rows, "execution_i_eft_status")]),
        ),
        Gate(
            "unit conventions protected",
            "PASS"
            if row(rows, "unit_conventions").get("status") == "FORBIDDEN_UNIT_CONVENTION"
            else "FAIL",
            str(row(rows, "unit_conventions")),
        ),
        Gate(
            "frontier records blocker",
            "PASS"
            if "selected absolute normalization" in frontier.get("main_blocker", "")
            and "observed target value" in frontier.get("forbidden_upgrade", "")
            else "FAIL",
            str(frontier),
        ),
        Gate(
            "paper records next step",
            "PASS"
            if contains_all(
                paper,
                [
                    "absolute-normalization candidate gate",
                    "observed target constant",
                    "selected normalization anchor",
                    "FORBIDDEN_UNIT_CONVENTION",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("matrix_certified") is True
            and verdict.get("absolute_dimensionful_constants_closed") is False
            and "absolute-normalization candidate gate" in verdict.get("next_recommended_step", "")
            else "FAIL",
            str(verdict),
        ),
    ]

    print("Non-SM constants status matrix audit")
    print("====================================")
    print()
    print(f"rows={len(rows)}")
    print(f"statuses={sorted(statuses)}")
    print()

    width = max(len(gate.label) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
