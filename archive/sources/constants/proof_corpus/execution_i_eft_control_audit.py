"""Audit the Execution I EFT-control status."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "execution_i_eft_control_certificate.json"
PAPER = ROOT / "Execution_I_EFT_Control_Status_v1.md"


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


def approx_equal(left: float, right: float, rel: float = 1e-6, abs_tol: float = 1e-9) -> bool:
    return abs(left - right) <= max(abs_tol, rel * max(abs(left), abs(right), 1e-300))


def main() -> None:
    cert = load_json(CERT)
    source_path = Path(cert["source"])
    source = read(source_path)
    paper = read(PAPER)
    selected = cert["selected_inputs"]
    computed = cert["computed_checks"]
    verdict = cert["verdict"]

    t1 = float(selected["t1"])
    t2 = float(selected["t2"])
    t3 = float(selected["t3"])
    tau1 = t2 * t3
    tau2 = t1 * t3
    tau3 = t1 * t2
    volume = t1 * t2 * t3
    checks = {
        "volume_from_t": volume,
        "tau1_from_t": tau1,
        "tau2_from_t": tau2,
        "tau3_from_t": tau3,
        "tau3_over_tau1": tau3 / tau1,
        "t3_over_t1": t3 / t1,
        "min_t": min(t1, t2, t3),
        "min_tau": min(tau1, tau2, tau3),
    }

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "RATIO_GEOMETRY_CERTIFIED_FULL_EFT_CONTROL_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source present",
            "PASS" if source_path.exists() else "FAIL",
            str(source_path),
        ),
        Gate(
            "source has executed values",
            "PASS"
            if contains_all(
                source,
                [
                    "t_1 = t_2 \\simeq 0.94",
                    "t_3 \\simeq 4.11",
                    "\\tau_1 &= t_2 t_3 \\simeq 3.86",
                    "\\tau_3 &= t_1 t_2 \\simeq 0.88",
                    "t_a \\gg 1",
                ],
            )
            else "FAIL",
            "Execution I Kähler/EFT sections",
        ),
        Gate(
            "tau1 recomputed",
            "PASS" if approx_equal(checks["tau1_from_t"], computed["tau1_from_t"]) else "FAIL",
            f"{checks['tau1_from_t']:.16g}",
        ),
        Gate(
            "tau2 recomputed",
            "PASS" if approx_equal(checks["tau2_from_t"], computed["tau2_from_t"]) else "FAIL",
            f"{checks['tau2_from_t']:.16g}",
        ),
        Gate(
            "tau3 recomputed",
            "PASS" if approx_equal(checks["tau3_from_t"], computed["tau3_from_t"]) else "FAIL",
            f"{checks['tau3_from_t']:.16g}",
        ),
        Gate(
            "ratio target reproduced",
            "PASS"
            if approx_equal(checks["tau3_over_tau1"], computed["tau3_over_tau1"], rel=1e-12)
            and abs(checks["tau3_over_tau1"] - float(selected["zeta3_over_zeta1_target"])) < 0.001
            else "FAIL",
            f"{checks['tau3_over_tau1']:.16g}",
        ),
        Gate(
            "large-volume failure detected",
            "PASS" if checks["min_t"] < 1.0 and checks["min_tau"] < 1.0 else "FAIL",
            f"min_t={checks['min_t']:.4g}, min_tau={checks['min_tau']:.4g}",
        ),
        Gate(
            "no full-EFT overclaim",
            "PASS"
            if verdict.get("ratio_geometry_certified") is True
            and verdict.get("full_eft_control_certified") is False
            and verdict.get("absolute_volume_certified") is False
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "repair options recorded",
            "PASS"
            if {item.get("id") for item in cert.get("repair_options", [])}
            == {"large_volume_rescaling", "finite_volume_control", "alternative_selected_corner"}
            else "FAIL",
            str(cert.get("repair_options", [])),
        ),
        Gate(
            "paper states status",
            "PASS"
            if contains_all(
                paper,
                [
                    "ratio geometry is consistent",
                    "full large-volume control is open",
                    "min(t_a) = 0.94",
                    "not target fitting",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Execution I EFT-control audit")
    print("=============================")
    print()
    for key, value in checks.items():
        print(f"{key}={value:.16g}")
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
