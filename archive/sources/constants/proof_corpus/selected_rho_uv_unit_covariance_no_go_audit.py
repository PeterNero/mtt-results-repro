"""Audit the selected rho_UV unit-covariance no-go and repair theorem."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Rho_UV_Unit_Covariance_No_Go_and_Repair_Theorem_v1.md"
CERT = REPO / "certificates" / "selected_rho_uv_unit_covariance_no_go_certificate.json"


@dataclass
class Gate:
    name: str
    status: str
    detail: str


def read(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    sources = cert["source_paths"]
    text = {
        "note": NOTE.read_text(encoding="utf-8"),
        "coefficient_route": read(sources["coefficient_route"]),
        "response_attempt": read(sources["response_attempt"]),
        "damping_hessian": read(sources["damping_hessian"]),
        "physical_action": read(sources["physical_action_normalization"]),
        "scale_extraction": read(sources["selected_scale_extraction"]),
        "white_noise": read(sources["white_noise"]),
    }

    gates: list[Gate] = []
    gates.append(
        Gate(
            "certificate status",
            "PASS" if cert.get("status") == "UNIT_COVARIANCE_SHORTCUT_REFUTED_REPAIR_THEOREM_FORMULATED" else "FAIL",
            cert.get("status", "missing"),
        )
    )
    gates.append(
        Gate(
            "note refutes Brownian renaming shortcut",
            "PASS"
            if contains_all(
                text["note"],
                [
                    "setting it to one by calling the Wiener process \"standard\"",
                    "does not determine the physical covariance",
                    "What is not acceptable is selecting `d=1`",
                    "renaming the noise.",
                ],
            )
            else "FAIL",
            "standard-Wiener normalization is not a no-knob covariance value",
        )
    )
    gates.append(
        Gate(
            "white-noise source leaves amplitude D free",
            "PASS"
            if contains_all(text["white_noise"], ["int_{-\\infty}^{\\infty} C_\\tau(t)\\,dt = 2D", "finite-memory model matters", "D\\delta"])
            else "FAIL",
            "finite-memory shape is proved; selected carrier amplitude is not",
        )
    )
    gates.append(
        Gate(
            "coefficient route closed G11 only",
            "PASS" if contains_all(text["coefficient_route"], ["G_11 = 1", "remaining gate = ||D_raw||_coeff^2"]) else "FAIL",
            "prior route reduces but does not close D_raw",
        )
    )
    gates.append(
        Gate(
            "response attempt has fixed UV coordinate",
            "PASS" if contains_all(text["response_attempt"], ["U_raw = (v1_tilde, 0, 0)", "rho_UV = ||U_raw||^2 / ||D_raw||^2"]) else "FAIL",
            "D cannot be absorbed after U coordinate is selected",
        )
    )
    gates.append(
        Gate(
            "damping and action units are closed but insufficient",
            "PASS"
            if contains_all(text["damping_hessian"], ["K_ret,64 = S^-1 = S^63", "lambda_* = 15"])
            and contains_all(text["physical_action"], ["alpha_int = 1", "G10_int = 1"])
            and contains_all(text["scale_extraction"], ["kappa = 1", "delta > 0"])
            else "FAIL",
            "drift/action normalization is not disturbance covariance",
        )
    )

    negative = cert.get("closed_negative_result", {})
    verdict = cert.get("verdict", {})
    gates.append(
        Gate(
            "no numeric overclaim",
            "PASS"
            if negative.get("D_raw_norm_squared_equals_one_from_current_corpus") is False
            and verdict.get("unit_covariance_shortcut_valid") is False
            and verdict.get("numeric_rho_uv_closed") is False
            else "FAIL",
            str(verdict),
        )
    )
    repair = cert.get("remaining_repair_calculation", {})
    gates.append(
        Gate(
            "repair calculation is explicit",
            "PASS"
            if repair.get("needed_object") == "selected unresolved finite-memory carrier covariance Q_tau"
            and "P K_ret Q_tau K_ret^* P^*" in repair.get("formula", "")
            else "FAIL",
            str(repair),
        )
    )

    print("Selected rho_UV unit-covariance no-go audit")
    print("=" * 49)
    failed = False
    for gate in gates:
        print(f"{gate.status}: {gate.name} -- {gate.detail}")
        failed = failed or gate.status != "PASS"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
