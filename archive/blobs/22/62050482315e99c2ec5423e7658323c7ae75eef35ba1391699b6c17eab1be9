"""Audit formula-level coefficient extraction for the scale-lifting branch."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "selected_scale_coefficient_extraction_certificate.json"


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


def approx_equal(left: float, right: float, rel: float = 1e-12, abs_tol: float = 1e-12) -> bool:
    return abs(left - right) <= max(abs_tol, rel * max(abs(left), abs(right), 1e-300))


def s_star(c_uv: float, delta: float, kappa: float) -> float:
    return (60.0 * kappa * c_uv**2 / delta) ** (1.0 / 6.0)


def main() -> None:
    cert = load_json(CERT)
    sources = {key: Path(value) for key, value in cert.get("source_paths", {}).items()}
    text = {key: read(path) for key, path in sources.items()}
    coeff = cert["extracted_coefficients"]
    demo = cert["normalized_demonstration_branch"]
    verdict = cert["verdict"]

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "KAPPA_EXTRACTED_CUV_DELTA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "sources present",
            "PASS" if all(path.exists() for path in sources.values()) else "FAIL",
            str([str(path) for path in sources.values() if not path.exists()]),
        ),
        Gate(
            "proof note has extracted formulas",
            "PASS"
            if contains_all(
                text["proof_note"],
                ["p = 4", "A = C_UV^2", "B = delta/(30 kappa)", "s_* = (60 kappa C_UV^2 / delta)^(1/6)"],
            )
            else "FAIL",
            str(sources["proof_note"]),
        ),
        Gate(
            "scale lemma supplies base functional",
            "PASS"
            if contains_all(
                text["scale_lifting_lemma"],
                ["F_scale(s) = A s^{-p} + B s^2", "s_* = (p A / (2 B))^(1/(p+2))"],
            )
            else "FAIL",
            str(sources["scale_lifting_lemma"]),
        ),
        Gate(
            "physical normalization source has lambda0",
            "PASS"
            if contains_all(text["physical_action_normalization"], ["lambda_* = 15", "alpha_int = 1"])
            else "FAIL",
            str(sources["physical_action_normalization"]),
        ),
        Gate(
            "heterotic selection has OU coefficient structure",
            "PASS"
            if contains_all(
                text["heterotic_selection"],
                ["Var}=\\delta/(2\\gamma)", "gamma=\\kappa\\lambda-L-\\Delta", "OU variance and summability"],
            )
            else "FAIL",
            str(sources["heterotic_selection"]),
        ),
        Gate(
            "heterotic flux has alpha-prime control",
            "PASS"
            if contains_all(
                text["heterotic_flux"],
                ["alpha'^2", "curvature-squared", "large volume and small flux"],
            )
            else "FAIL",
            str(sources["heterotic_flux"]),
        ),
        Gate(
            "numeric extraction note reduces kappa",
            "PASS"
            if contains_all(
                text["numeric_extraction_note"],
                ["kappa = 1", "B = delta/30", "s_* = (60 C_UV^2 / delta)^(1/6)"],
            )
            else "FAIL",
            str(sources["numeric_extraction_note"]),
        ),
        Gate(
            "damping source fixes exact branch",
            "PASS"
            if contains_all(text["damping_hessian"], ["alpha = 1", "lambda_* = 15", "E_Schur = 0"])
            else "FAIL",
            str(sources["damping_hessian"]),
        ),
        Gate(
            "white-noise source leaves disturbance power open",
            "PASS"
            if contains_all(
                text["white_noise"],
                ["finite-memory disturbance", "integrated covariance", "not proved here"],
            )
            else "FAIL",
            str(sources["white_noise"]),
        ),
        Gate("p extracted", "PASS" if approx_equal(float(coeff["p"]), 4.0) else "FAIL", str(coeff["p"])),
        Gate("lambda0 extracted", "PASS" if approx_equal(float(coeff["lambda0"]), 15.0) else "FAIL", str(coeff["lambda0"])),
        Gate("kappa extracted", "PASS" if approx_equal(float(coeff["kappa"]), 1.0) else "FAIL", str(coeff["kappa"])),
        Gate("B formula", "PASS" if coeff["B"] == "delta/(2*kappa*lambda0) = delta/(30*kappa)" else "FAIL", coeff["B"]),
        Gate(
            "B after kappa extraction",
            "PASS" if coeff["B_after_kappa_extraction"] == "delta/30" else "FAIL",
            coeff["B_after_kappa_extraction"],
        ),
        Gate(
            "s star after kappa extraction",
            "PASS"
            if coeff["s_star_after_kappa_extraction"] == "(60*C_UV^2/delta)^(1/6)"
            else "FAIL",
            coeff["s_star_after_kappa_extraction"],
        ),
        Gate(
            "demo B",
            "PASS" if approx_equal(float(demo["B"]), 1.0 / 30.0) else "FAIL",
            f"{float(demo['B']):.16g}",
        ),
        Gate(
            "demo s_star",
            "PASS"
            if approx_equal(
                s_star(float(demo["C_UV"]), float(demo["delta"]), float(demo["kappa"])),
                float(demo["s_star"]),
            )
            else "FAIL",
            f"{s_star(float(demo['C_UV']), float(demo['delta']), float(demo['kappa'])):.16g}",
        ),
        Gate(
            "no numeric overclaim",
            "PASS"
            if verdict.get("formula_level_coefficient_gap_fixed") is True
            and verdict.get("kappa_extracted") is True
            and verdict.get("numeric_coefficients_extracted") is False
            and verdict.get("physical_absolute_normalization_closed") is False
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "single remaining gate",
            "PASS"
            if verdict.get("remaining_gate_count") == 1
            and "rho_UV=C_UV^2/delta" in verdict.get("remaining_gate", "")
            else "FAIL",
            str(verdict),
        ),
    ]

    print("Selected scale coefficient extraction audit")
    print("===========================================")
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
