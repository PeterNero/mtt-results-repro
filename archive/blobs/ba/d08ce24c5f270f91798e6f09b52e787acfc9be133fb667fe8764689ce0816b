"""Audit the obstruction to no-knob absolute dimensionful predictions."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "dimensionful_constant_obstruction_certificate.json"
PAPER = ROOT / "Dimensionful_Constant_Normalization_Obstruction_v1.md"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
THETA_IV = Q79 / "proof_corpus" / "Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale.md"


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


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    theta_iv = read(THETA_IV)
    verdict = cert["verdict"]

    gates = [
        Gate(
            "certificate status",
            "PASS" if cert.get("status") == "OBSTRUCTION_CERTIFIED" else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "target set includes core constants",
            "PASS"
            if all(target in cert.get("targets", []) for target in ["Newton constant G_N", "late-time Hubble constant H0"])
            else "FAIL",
            str(cert.get("targets", [])),
        ),
        Gate(
            "theta IV source has structure not closure",
            "PASS"
            if contains_all(
                theta_iv,
                [
                    "31.8",
                    "G_{10}",
                    "R_1^3",
                    "does not attempt to compute",
                ],
            )
            else "FAIL",
            str(THETA_IV),
        ),
        Gate(
            "paper forbids backsolve",
            "PASS"
            if contains_all(
                paper,
                [
                    "not yet a numerical prediction",
                    "has not been selected independently",
                    "forbidden claims",
                    "without using the target constant",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
        Gate(
            "required absolute-normalization gate",
            "PASS"
            if contains_all(
                " ".join(cert.get("required_for_absolute_prediction", [])),
                [
                    "selected absolute normalization",
                    "not target-value backsolved",
                    "unit convention separated",
                ],
            )
            else "FAIL",
            str(cert.get("required_for_absolute_prediction", [])),
        ),
        Gate(
            "no absolute overclaim",
            "PASS"
            if verdict.get("absolute_dimensionful_predictions_closed") is False
            and verdict.get("structural_dimensionful_constraints_available") is True
            else "FAIL",
            str(verdict),
        ),
    ]

    print("Dimensionful constant obstruction audit")
    print("=======================================")
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
