"""Audit the selected normalization minimization functional gate."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "selected_normalization_minimization_functional_certificate.json"


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


def r3_iwasawa(r_value: float, alpha_prime: float = 1.0) -> float:
    r3_squared = 8.0 * (2.0 * math.pi) ** 2 / (16.0 / alpha_prime + 8.0 / r_value**4)
    return math.sqrt(r3_squared)


def r1_exact(n: int) -> float:
    return math.sqrt(math.log(n) / 15.0)


def main() -> None:
    cert = load_json(CERT)
    sources = {key: Path(value) for key, value in cert.get("source_paths", {}).items()}
    text = {key: read(path) for key, path in sources.items()}
    checks = cert["executable_checks"]
    verdict = cert["verdict"]

    gates = [
        Gate(
            "certificate status",
            "PASS" if cert.get("status") == "FUNCTIONAL_FORMULATED_SCALE_LIFTING_LEMMA_OPEN" else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "sources present",
            "PASS" if all(path.exists() for path in sources.values()) else "FAIL",
            str([str(path) for path in sources.values() if not path.exists()]),
        ),
        Gate(
            "proof note states functional",
            "PASS"
            if contains_all(
                text["proof_note"],
                ["F_norm(s; T,m,N)", "Scale-Lifting Lemma", "does not yet"],
            )
            else "FAIL",
            str(sources["proof_note"]),
        ),
        Gate(
            "Strominger source has Xi selection",
            "PASS"
            if contains_all(
                text["strominger_selection"],
                ["selection potential", "\\Xi", "unique local minimizer", "fixed topological sector"],
            )
            else "FAIL",
            str(sources["strominger_selection"]),
        ),
        Gate(
            "Strominger source has positive Hessian",
            "PASS"
            if contains_all(
                text["strominger_selection"],
                ["Positive Hessian", "strict convexity", "OU term", "lifting residual moduli"],
            )
            else "FAIL",
            str(sources["strominger_selection"]),
        ),
        Gate(
            "flux source has Bianchi and quantization",
            "PASS"
            if contains_all(
                text["heterotic_flux"],
                ["dH", "alpha'/4", "Flux quantization", "integral periods"],
            )
            else "FAIL",
            str(sources["heterotic_flux"]),
        ),
        Gate(
            "flux source records scale obstruction",
            "PASS"
            if contains_all(
                text["heterotic_flux"],
                ["overall volume/shape modulus remains", "fix the *ratio* $R_1/R$", "overall scale modulus"],
            )
            else "FAIL",
            str(sources["heterotic_flux"]),
        ),
        Gate(
            "selection source has no invariant moduli clue",
            "PASS"
            if contains_all(
                text["heterotic_selection"],
                ["no invariant moduli remain in the invariant sector", "functional $\\Xi"],
            )
            else "FAIL",
            str(sources["heterotic_selection"]),
        ),
        Gate(
            "central circle source has internal units",
            "PASS"
            if contains_all(
                text["central_circle"],
                ["alpha_int = 1", "G10_int = 1", "not measured SI"],
            )
            else "FAIL",
            str(sources["central_circle"]),
        ),
    ]

    iwasawa = checks["iwasawa_alpha_prime_internal_units"]
    for r_value, expected in zip(iwasawa["sample_R_values"], iwasawa["r3_values"]):
        actual = r3_iwasawa(float(r_value))
        gates.append(
            Gate(
                f"Iwasawa R={r_value} r3",
                "PASS" if approx_equal(actual, float(expected)) else "FAIL",
                f"{actual:.16g}",
            )
        )

    central = checks["central_circle"]
    for n in (64, 79, 448):
        actual = r1_exact(n)
        expected = float(central[f"R1_{n}"])
        gates.append(
            Gate(
                f"central circle R1({n})",
                "PASS" if approx_equal(actual, expected) else "FAIL",
                f"{actual:.16g}",
            )
        )

    gates.extend(
        [
            Gate(
                "functional terms complete",
                "PASS"
                if set(cert["functional"]["terms"])
                == {
                    "Xi_reduced(s; T,m)",
                    "B_Bianchi(s; T,m)",
                    "B_quant(s; T,m)",
                    "B_circle(s; N)",
                    "B_control(s; T,m)",
                }
                else "FAIL",
                str(cert["functional"]["terms"]),
            ),
            Gate(
                "no forbidden closure",
                "PASS"
                if verdict.get("normalization_functional_formulated") is True
                and verdict.get("unique_positive_scale_minimizer_proved") is False
                and verdict.get("physical_absolute_normalization_closed") is False
                else "FAIL",
                str(verdict),
            ),
            Gate(
                "single next lemma identified",
                "PASS"
                if verdict.get("remaining_lemma_count") == 1
                and verdict.get("remaining_lemma") == "Scale-Lifting Lemma for the Selected Flux/Strominger Functional"
                else "FAIL",
                str(verdict),
            ),
        ]
    )

    print("Selected normalization minimization functional audit")
    print("====================================================")
    print()
    print(f"status={cert.get('status')}")
    print(f"remaining_lemma={verdict.get('remaining_lemma')}")
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
