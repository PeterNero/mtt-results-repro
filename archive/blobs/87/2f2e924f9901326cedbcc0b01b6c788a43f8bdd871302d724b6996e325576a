"""Audit the selected finite-memory carrier covariance computation attempt."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Finite_Memory_Carrier_Covariance_Computation_Attempt_v1.md"
CERT = REPO / "certificates" / "selected_finite_memory_carrier_covariance_computation_attempt_certificate.json"


@dataclass
class Gate:
    name: str
    status: str
    detail: str


def read(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def approx(a: float, b: float, tol: float = 1e-9) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def values(R: float, d: float) -> tuple[float, float]:
    v1 = 64.0 * (2.0 * math.pi) ** 2 / (16.0 * R**4 + 8.0)
    rho = v1**2 / d
    s_star = (60.0 * rho) ** (1.0 / 6.0)
    return rho, s_star


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    sources = cert["source_paths"]
    text = {
        "note": NOTE.read_text(encoding="utf-8"),
        "unit_no_go": read(sources["unit_covariance_no_go"]),
        "damping_hessian": read(sources["damping_hessian"]),
        "fixed_points": read(sources["fixed_points_disturbance"]),
        "measurement": read(sources["measurement_disturbance"]),
        "white_noise": read(sources["white_noise"]),
    }

    gates: list[Gate] = []
    gates.append(
        Gate(
            "certificate status",
            "PASS" if cert.get("status") == "Q_TAU_ALGEBRAIC_REDUCTION_COMPUTED_NUMERIC_VALUE_OPEN" else "FAIL",
            cert.get("status", "missing"),
        )
    )
    gates.append(
        Gate(
            "Green-Kubo source present",
            "PASS"
            if contains_all(text["fixed_points"], ["Green--Kubo formula", "R_x(s)", "sigma(x)\\sigma(x)^\\ast"])
            else "FAIL",
            "fixed-point disturbance paper supplies covariance formula",
        )
    )
    gates.append(
        Gate(
            "disturbance power source remains parameterized",
            "PASS"
            if contains_all(text["measurement"], ["quadratic variation", "\\langle M\\rangle_t = \\delta\\,t", "disturbance power"])
            else "FAIL",
            "measurement paper defines delta but does not select numeric value",
        )
    )
    gates.append(
        Gate(
            "Z64 retarded kernel source present",
            "PASS" if contains_all(text["damping_hessian"], ["K_ret,64 = S^-1 = S^63", "S e_j = e_{j+1 mod 64}"]) else "FAIL",
            "exact branch retarded kernel is certified",
        )
    )
    gates.append(
        Gate(
            "proof note computes algebraic reduction",
            "PASS"
            if contains_all(text["note"], ["||D_raw||_coeff^2 = p^T S^-1 Q_tau S p", "d := (Q_tau)_{00}", "rho_UV(R) ="])
            else "FAIL",
            "D_raw reduced to selected covariance diagonal under equivariance",
        )
    )
    gates.append(
        Gate(
            "white-noise warning prevents overclaim",
            "PASS"
            if contains_all(text["white_noise"], ["finite-memory model matters", "admissible replacement must preserve", "fluctuation--dissipation"])
            else "FAIL",
            "finite-memory amplitude cannot be guessed",
        )
    )
    verdict = cert.get("verdict", {})
    gates.append(
        Gate(
            "numeric closure remains blocked",
            "PASS"
            if verdict.get("Q_tau_formula_computed") is True
            and verdict.get("Z64_retarded_reduction_computed") is True
            and verdict.get("numeric_d_closed") is False
            and verdict.get("numeric_rho_uv_closed") is False
            else "FAIL",
            str(verdict),
        )
    )

    for row in cert.get("conditional_values", []):
        R = float(row["R"])
        checks = [
            ("d_1", 1.0, "d_1_rho_UV", "d_1_s_star"),
            ("d_1_over_64", 1.0 / 64.0, "d_1_over_64_rho_UV", "d_1_over_64_s_star"),
            ("d_63_over_64", 63.0 / 64.0, "d_63_over_64_rho_UV", "d_63_over_64_s_star"),
        ]
        for label, d, rho_key, s_key in checks:
            rho, s_star = values(R, d)
            gates.append(Gate(f"R={R:g} {label} rho", "PASS" if approx(rho, float(row[rho_key])) else "FAIL", f"{rho:.15g}"))
            gates.append(Gate(f"R={R:g} {label} s*", "PASS" if approx(s_star, float(row[s_key])) else "FAIL", f"{s_star:.15g}"))

    print("Selected finite-memory carrier covariance computation attempt audit")
    print("=" * 69)
    failed = False
    for gate in gates:
        print(f"{gate.status}: {gate.name} -- {gate.detail}")
        failed = failed or gate.status != "PASS"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
