"""Audit the selected rho_UV coefficient-normalization route."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Rho_UV_Coefficient_Normalization_and_Unit_Covariance_Route_v1.md"
CERT = REPO / "certificates" / "selected_rho_uv_coefficient_normalization_route_certificate.json"


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


def compute_row(R: float) -> tuple[float, float, float, float]:
    r3_sq = 8.0 * (2.0 * math.pi) ** 2 / (16.0 + 8.0 / R**4)
    r3 = math.sqrt(r3_sq)
    v1 = 64.0 * (2.0 * math.pi) ** 2 / (16.0 * R**4 + 8.0)
    rho = v1**2
    s_star = (60.0 * rho) ** (1.0 / 6.0)
    return r3, v1, rho, s_star


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    sources = cert["source_paths"]
    text = {
        "note": NOTE.read_text(encoding="utf-8"),
        "response_attempt": read(sources["response_attempt"]),
        "superset_gate": read(sources["superset_gate"]),
        "heterotic_selection": read(sources["heterotic_selection"]),
        "heterotic_flux": read(sources["heterotic_flux"]),
        "white_noise": read(sources["white_noise"]),
    }

    gates: list[Gate] = []

    gates.append(
        Gate(
            "certificate status",
            "PASS" if cert.get("status") == "G11_CLOSED_UNIT_COVARIANCE_ROUTE_CONDITIONAL" else "FAIL",
            cert.get("status", "missing"),
        )
    )
    gates.append(
        Gate(
            "proof note states reduced formula",
            "PASS"
            if contains_all(
                text["note"],
                [
                    "G_11 = 1",
                    "rho_UV(R) =",
                    "||D_raw||_coeff^2",
                    "remaining gate = ||D_raw||_coeff^2",
                ],
            )
            else "FAIL",
            "G11 closure and one-factor disturbance gate",
        )
    )
    gates.append(
        Gate(
            "UV source row remains source-certified",
            "PASS"
            if contains_all(text["response_attempt"], ["U_raw = (v1_tilde, 0, 0)", "v1_tilde(R) = 64(2pi)^2 / (16 R^4 + 8)"])
            else "FAIL",
            "prior computation supplies row support and coefficient",
        )
    )
    gates.append(
        Gate(
            "heterotic source has invariant coefficient basis",
            "PASS"
            if contains_all(text["heterotic_selection"], ["alpha_1", "alpha_2", "alpha_3", "a\\wedge b\\wedge c"])
            else "FAIL",
            "basis and volume normalization are present",
        )
    )
    gates.append(
        Gate(
            "flux source confirms coefficient normalization context",
            "PASS"
            if contains_all(text["heterotic_flux"], ["\\int_X a\\wedge b\\wedge c=1", "\\alpha_1:=a\\wedge b", "\\mathrm{Tr}_{\\mathrm{grav}} R_+^2"])
            else "FAIL",
            "independent flux note records same invariant basis and curvature row",
        )
    )
    gates.append(
        Gate(
            "white-noise source does not overclose covariance",
            "PASS"
            if contains_all(text["white_noise"], ["finite-memory disturbance", "computed here from a specific carrier geometry", "finite-memory model matters"])
            else "FAIL",
            "finite-memory covariance exists but is not selected numerically",
        )
    )

    closed = cert.get("closed", {})
    gates.append(
        Gate(
            "G11 is closed only for coefficient response norm",
            "PASS"
            if closed.get("G_11") == 1.0 and closed.get("selected_response_norm") == "componentwise coefficient Hilbert norm"
            else "FAIL",
            str(closed),
        )
    )

    verdict = cert.get("verdict", {})
    gates.append(
        Gate(
            "no unconditional rho overclaim",
            "PASS"
            if verdict.get("G11_closed_for_coefficient_response_problem") is True
            and verdict.get("D_raw_norm_closed") is False
            and verdict.get("numeric_rho_uv_unconditional") is False
            else "FAIL",
            str(verdict),
        )
    )

    values = cert.get("conditional_values_if_D_raw_norm_squared_is_one", [])
    for row in values:
        R = float(row["R"])
        r3, v1, rho, s_star = compute_row(R)
        gates.extend(
            [
                Gate(f"R={R:g} conditional r3", "PASS" if approx(r3, float(row["r3"])) else "FAIL", f"{r3:.15g}"),
                Gate(f"R={R:g} conditional v1", "PASS" if approx(v1, float(row["v1_tilde"])) else "FAIL", f"{v1:.15g}"),
                Gate(f"R={R:g} conditional rho", "PASS" if approx(rho, float(row["rho_UV"])) else "FAIL", f"{rho:.15g}"),
                Gate(f"R={R:g} conditional s*", "PASS" if approx(s_star, float(row["s_star"])) else "FAIL", f"{s_star:.15g}"),
            ]
        )

    print("Selected rho_UV coefficient-normalization route audit")
    print("=" * 59)
    failed = False
    for gate in gates:
        print(f"{gate.status}: {gate.name} -- {gate.detail}")
        failed = failed or gate.status != "PASS"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
