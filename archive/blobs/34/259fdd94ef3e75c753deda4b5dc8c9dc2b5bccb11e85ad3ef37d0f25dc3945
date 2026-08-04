"""Audit the physical action-normalization gate closure."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "physical_action_normalization_gate_certificate.json"


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


def r1(n: int) -> float:
    return math.sqrt(math.log(n) / 15.0)


def vol_int(n: int) -> float:
    radius = r1(n)
    return 31.8 * radius**3


def main() -> None:
    cert = load_json(CERT)
    sources = {key: Path(value) for key, value in cert.get("source_paths", {}).items()}
    text = {key: read(path) for key, path in sources.items()}
    internal = cert["canonical_internal_normalization"]
    verdict = cert["verdict"]

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "INTERNAL_ACTION_NORMALIZATION_CERTIFIED_PHYSICAL_ABSOLUTE_NO_GO"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "sources present",
            "PASS" if all(path.exists() for path in sources.values()) else "FAIL",
            str([str(path) for path in sources.values() if not path.exists()]),
        ),
        Gate(
            "proof note separates unit and physical claims",
            "PASS"
            if contains_all(
                text["proof_note"],
                [
                    "canonical internal action normalization: CLOSED",
                    "physical absolute action normalization: NO-GO",
                    "not measured si",
                ],
            )
            else "FAIL",
            str(sources["proof_note"]),
        ),
        Gate(
            "damping source fixes alpha internally",
            "PASS"
            if contains_all(
                text["damping_hessian"],
                ["alpha = 1", "lambda_* = 15", "Do not choose `alpha`, `G10`"],
            )
            else "FAIL",
            str(sources["damping_hessian"]),
        ),
        Gate(
            "GR source supplies action dictionary",
            "PASS"
            if contains_all(
                text["mtt_to_gr"],
                ["where $\\mathcal G$ is the $10$D gravitational coupling", "G_{\\rm eff} := \\frac{\\mathcal G}{\\mathcal V_{\\rm int}}"],
            )
            else "FAIL",
            str(sources["mtt_to_gr"]),
        ),
        Gate(
            "Theta IV refuses G10 computation",
            "PASS"
            if contains_all(
                text["theta_iv_gravity"],
                ["31.8", "G_{10}", "does not attempt to compute $G_{10}$"],
            )
            else "FAIL",
            str(sources["theta_iv_gravity"]),
        ),
        Gate(
            "string bridge is scale-structural only",
            "PASS"
            if contains_all(
                text["gr_string_admissibility"],
                ["alpha'\\sim\\lambda_\\ast^{-1}", "not a conjecture"],
            )
            else "FAIL",
            str(sources["gr_string_admissibility"]),
        ),
        Gate(
            "dimensionful obstruction retained",
            "PASS"
            if contains_all(
                text["dimensionful_obstruction"],
                ["selected absolute normalization", "target constant", "G_10 / R1^3"],
            )
            else "FAIL",
            str(sources["dimensionful_obstruction"]),
        ),
        Gate(
            "internal alpha",
            "PASS" if approx_equal(float(internal["alpha_int"]), 1.0) else "FAIL",
            str(internal["alpha_int"]),
        ),
        Gate(
            "internal G10",
            "PASS" if approx_equal(float(internal["G10_int"]), 1.0) else "FAIL",
            str(internal["G10_int"]),
        ),
        Gate(
            "internal lambda",
            "PASS" if approx_equal(float(internal["lambda_star"]), 15.0) else "FAIL",
            str(internal["lambda_star"]),
        ),
    ]

    for item in cert["tested_cases"]:
        n = int(item["N"])
        actual_r1 = r1(n)
        actual_vol = vol_int(n)
        actual_geff = 1.0 / actual_vol
        gates.extend(
            [
                Gate(
                    f"N={n} R1",
                    "PASS" if approx_equal(actual_r1, float(item["R1"])) else "FAIL",
                    f"{actual_r1:.16g}",
                ),
                Gate(
                    f"N={n} Vol_int",
                    "PASS" if approx_equal(actual_vol, float(item["Vol_int"])) else "FAIL",
                    f"{actual_vol:.16g}",
                ),
                Gate(
                    f"N={n} G_eff_int",
                    "PASS" if approx_equal(actual_geff, float(item["G_eff_int"])) else "FAIL",
                    f"{actual_geff:.16g}",
                ),
            ]
        )

    gates.extend(
        [
            Gate(
                "internal gate closed",
                "PASS"
                if verdict.get("canonical_internal_action_normalization_closed") is True
                and verdict.get("alpha_closed_in_internal_units") is True
                and verdict.get("G10_closed_as_internal_unit_convention") is True
                else "FAIL",
                str(verdict),
            ),
            Gate(
                "physical overclaim blocked",
                "PASS"
                if verdict.get("physical_absolute_dimensionful_predictions_closed") is False
                and verdict.get("no_go_without_external_dimensional_anchor") is True
                else "FAIL",
                str(verdict),
            ),
        ]
    )

    print("Physical action-normalization gate audit")
    print("========================================")
    print()
    print(f"tested_cases={len(cert['tested_cases'])}")
    print(f"status={cert.get('status')}")
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
