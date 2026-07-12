"""Audit the selected rho_UV response-ratio computation attempt."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "selected_rho_uv_response_ratio_computation_attempt_certificate.json"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def contains_all(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def approx(left: float, right: float, tol: float = 1e-10) -> bool:
    return abs(left - right) <= tol * max(1.0, abs(left), abs(right))


def r3(R: float) -> float:
    return math.sqrt(8.0 * (2.0 * math.pi) ** 2 / (16.0 + 8.0 / R**4))


def v1_tilde(R: float) -> float:
    return 64.0 * (2.0 * math.pi) ** 2 / (16.0 * R**4 + 8.0)


def s_star(rho: float) -> float:
    return (60.0 * rho) ** (1.0 / 6.0)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    sources = {key: Path(value) for key, value in cert["source_paths"].items()}
    text = {key: read(path) for key, path in sources.items()}
    c1_cert = json.loads(Path(cert["source_paths"]["c1_attempt_certificate"]).read_text(encoding="utf-8"))
    demo = cert["demonstration_specialization"]
    verdict = cert["verdict"]

    gates = [
        Gate(
            "certificate status",
            "PASS" if cert.get("status") == "RHO_UV_SYMBOLIC_FORMULA_COMPUTED_NUMERIC_CLOSURE_BLOCKED" else "FAIL",
            str(cert.get("status")),
        ),
        Gate("sources present", "PASS" if all(path.exists() for path in sources.values()) else "FAIL", str([str(path) for path in sources.values() if not path.exists()])),
        Gate(
            "proof note has closed UV row",
            "PASS" if contains_all(text["proof_note"], ["U_raw = (v1_tilde, 0, 0)", "v1_tilde = 8 r3^2/R^4"])
            else "FAIL",
            str(sources["proof_note"]),
        ),
        Gate(
            "proof note has rho formula",
            "PASS"
            if contains_all(text["proof_note"], ["rho_UV =", "G_11", "||D_raw||^2", "64(2pi)^2 / (16 R^4 + 8)"])
            else "FAIL",
            str(sources["proof_note"]),
        ),
        Gate(
            "superset gate asked for U and D",
            "PASS" if contains_all(text["superset_gate"], ["U = selected O(alpha'^2) UV response row", "D = selected finite-memory disturbance covariance row"])
            else "FAIL",
            str(sources["superset_gate"]),
        ),
        Gate(
            "C1 attempt confirms open response data",
            "PASS"
            if c1_cert.get("status") == "C1_RESPONSE_EXTRACTION_BLOCKED_MISSING_SELECTED_OPERATOR_DATA"
            and c1_cert["attempt_result"]["alpha1_driver_row_computed"] is True
            and c1_cert["attempt_result"]["M_C1_alpha1_entries_computed"] is False
            else "FAIL",
            str(c1_cert.get("attempt_result")),
        ),
        Gate(
            "heterotic source supplies alpha1 row",
            "PASS"
            if contains_all(text["heterotic_selection"], ["Tr}_{\\mathrm{grav}}R_{+}^{2}", "alpha_1", "tilde v_1"])
            else "FAIL",
            str(sources["heterotic_selection"]),
        ),
        Gate(
            "white-noise source leaves covariance open",
            "PASS" if contains_all(text["white_noise"], ["finite-memory disturbance", "not proved here", "finite-memory model matters"])
            else "FAIL",
            str(sources["white_noise"]),
        ),
    ]

    for row in demo["values"]:
        R = float(row["R"])
        rho = v1_tilde(R) ** 2
        gates.extend(
            [
                Gate(f"R={R:g} r3", "PASS" if approx(r3(R), float(row["r3"])) else "FAIL", f"{r3(R):.15g}"),
                Gate(f"R={R:g} v1_tilde", "PASS" if approx(v1_tilde(R), float(row["v1_tilde"])) else "FAIL", f"{v1_tilde(R):.15g}"),
                Gate(f"R={R:g} demo rho", "PASS" if approx(rho, float(row["rho_UV"])) else "FAIL", f"{rho:.15g}"),
                Gate(f"R={R:g} demo s_star", "PASS" if approx(s_star(rho), float(row["s_star"])) else "FAIL", f"{s_star(rho):.15g}"),
            ]
        )

    gates.extend(
        [
            Gate(
                "demonstration not certified",
                "PASS"
                if demo.get("certified") is False and verdict.get("demonstration_values_are_predictions") is False
                else "FAIL",
                str(demo.get("assumptions")),
            ),
            Gate(
                "numeric closure blocked",
                "PASS"
                if verdict.get("U_support_closed") is True
                and verdict.get("symbolic_rho_formula_computed") is True
                and verdict.get("numeric_rho_uv_closed") is False
                and "G_11" in verdict.get("remaining_gate", "")
                else "FAIL",
                str(verdict),
            ),
        ]
    )

    print("Selected rho_UV response-ratio computation attempt audit")
    print("========================================================")
    print()
    print(f"status={cert.get('status')}")
    print(f"remaining_gate={verdict.get('remaining_gate')}")
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
