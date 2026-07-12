"""Audit the final selected-character rho_UV theorem."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Final_Selected_Character_Rho_UV_Theorem_v1.md"
CERT = REPO / "certificates" / "final_selected_character_rho_uv_theorem_certificate.json"


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


def compute(R: float) -> tuple[float, float, float]:
    r3_sq = 8.0 * (2.0 * math.pi) ** 2 / (16.0 + 8.0 / R**4)
    r3 = math.sqrt(r3_sq)
    v1 = 64.0 * (2.0 * math.pi) ** 2 / (16.0 * R**4 + 8.0)
    rho = v1**2
    s_star = (60.0 * rho) ** (1.0 / 6.0)
    return r3, rho, s_star


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    sources = cert["source_paths"]
    text = {
        "note": NOTE.read_text(encoding="utf-8"),
        "response": read(sources["response_attempt"]),
        "coefficient": read(sources["coefficient_route"]),
        "character": read(sources["character_channel_closure"]),
        "scale": read(sources["scale_extraction"]),
    }

    gates: list[Gate] = []
    gates.append(
        Gate(
            "certificate status",
            "PASS" if cert.get("status") == "RHO_UV_BRANCH_FUNCTION_CLOSED_R_SELECTION_OPEN" else "FAIL",
            cert.get("status", "missing"),
        )
    )
    gates.append(
        Gate(
            "final theorem states closed formula",
            "PASS" if contains_all(text["note"], ["rho_UV(R) = [64(2pi)^2/(16 R^4 + 8)]^2", "s_*(R) = (60 rho_UV(R))^(1/6)"]) else "FAIL",
            "rho_UV and s_star as functions of R",
        )
    )
    gates.append(
        Gate(
            "UV row source imported",
            "PASS" if contains_all(text["response"], ["U_raw = (v1_tilde, 0, 0)", "v1_tilde(R) = 64(2pi)^2 / (16 R^4 + 8)"]) else "FAIL",
            "heterotic alpha1 row",
        )
    )
    gates.append(
        Gate(
            "coefficient metric closed",
            "PASS" if contains_all(text["coefficient"], ["G_11 = 1", "||U_raw||_coeff^2 = v1_tilde(R)^2"]) else "FAIL",
            "G11=1 in finite coefficient quotient",
        )
    )
    gates.append(
        Gate(
            "character channel closes D",
            "PASS" if contains_all(text["character"], ["||D_raw||_coeff^2 = 1", "q_64=15", "Q_char = E_15"]) else "FAIL",
            "selected character covariance",
        )
    )
    gates.append(
        Gate(
            "scale extraction imported",
            "PASS" if contains_all(text["scale"], ["s_* = (60 rho_UV)^(1/6)", "kappa = 1"]) else "FAIL",
            "scale-lifting formula",
        )
    )

    verdict = cert.get("verdict", {})
    gates.append(
        Gate(
            "R selection remains open",
            "PASS"
            if verdict.get("rho_uv_branch_function_closed") is True
            and verdict.get("single_numeric_rho_uv_closed") is False
            and "Iwasawa radius R" in verdict.get("remaining_gate", "")
            else "FAIL",
            str(verdict),
        )
    )

    for row in cert.get("evaluations", []):
        R = float(row["R"])
        r3, rho, s_star = compute(R)
        gates.append(Gate(f"R={R:g} r3", "PASS" if approx(r3, float(row["r3"])) else "FAIL", f"{r3:.15g}"))
        gates.append(Gate(f"R={R:g} rho", "PASS" if approx(rho, float(row["rho_UV"])) else "FAIL", f"{rho:.15g}"))
        gates.append(Gate(f"R={R:g} s*", "PASS" if approx(s_star, float(row["s_star"])) else "FAIL", f"{s_star:.15g}"))

    print("Final selected-character rho_UV theorem audit")
    print("=" * 46)
    failed = False
    for gate in gates:
        print(f"{gate.status}: {gate.name} -- {gate.detail}")
        failed = failed or gate.status != "PASS"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
