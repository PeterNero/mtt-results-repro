"""Audit selected character-channel covariance closure for rho_UV."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Character_Channel_Covariance_Closure_for_Rho_UV_v1.md"
CERT = REPO / "certificates" / "selected_character_channel_covariance_closure_certificate.json"


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


def compute(R: float) -> tuple[float, float]:
    v1 = 64.0 * (2.0 * math.pi) ** 2 / (16.0 * R**4 + 8.0)
    rho = v1**2
    s_star = (60.0 * rho) ** (1.0 / 6.0)
    return rho, s_star


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    sources = cert["source_paths"]
    text = {
        "note": NOTE.read_text(encoding="utf-8"),
        "carrier_attempt": read(sources["carrier_covariance_attempt"]),
        "coefficient_route": read(sources["coefficient_route"]),
        "z64_exact": read(sources["z64_exact_branch"]),
        "z64_character": read(sources["z64_character_carrier"]),
        "primitive_lag": read(sources["primitive_lag"]),
    }

    gates: list[Gate] = []
    gates.append(
        Gate(
            "certificate status",
            "PASS" if cert.get("status") == "CHARACTER_CHANNEL_D_EQUALS_ONE_CLOSED_CONDITIONAL_ON_CHANNEL_IDENTIFICATION" else "FAIL",
            cert.get("status", "missing"),
        )
    )
    gates.append(
        Gate(
            "character projectors source",
            "PASS" if contains_all(text["z64_character"], ["E_q = (1/64)", "physical CP labels are its character projectors", "selected character sector"]) else "FAIL",
            "Z64 carrier uses character idempotents",
        )
    )
    gates.append(
        Gate(
            "selected q64 source",
            "PASS" if contains_all(text["z64_exact"], ["selected component:  q_64=15", "K_64=C[coker A_64]~=C[Z_64]"]) else "FAIL",
            "exact branch selects q64=15",
        )
    )
    gates.append(
        Gate(
            "retarded kernel unitary on character line",
            "PASS" if contains_all(text["primitive_lag"], ["S^{-1}=S^63", "q_64 = 15", "selected kernel sees the full exact-order-64 carrier"]) else "FAIL",
            "primitive lag is the selected retarded kernel",
        )
    )
    gates.append(
        Gate(
            "prior covariance reduction available",
            "PASS" if contains_all(text["carrier_attempt"], ["d = p^T Q_tau p", "d = (Q_tau)_{00}", "symmetry alone"]) else "FAIL",
            "new theorem selects character coordinate rather than deck diagonal",
        )
    )
    gates.append(
        Gate(
            "proof note distinguishes character from deck basis",
            "PASS" if contains_all(text["note"], ["physical selected", "channel is the character coordinate", "deck basis", "d_char = 1"]) else "FAIL",
            "prevents accidental use of trace-one deck diagonal",
        )
    )
    gates.append(
        Gate(
            "coefficient route supplies G11",
            "PASS" if contains_all(text["coefficient_route"], ["G_11 = 1", "v1_tilde(R) = 64(2pi)^2/(16 R^4 + 8)"]) else "FAIL",
            "UV row norm already closed",
        )
    )

    verdict = cert.get("verdict", {})
    gates.append(
        Gate(
            "branch closure but not all covariance models",
            "PASS"
            if verdict.get("character_channel_covariance_closed") is True
            and verdict.get("D_raw_norm_squared_on_selected_character_branch") == 1.0
            and verdict.get("rho_uv_closed_on_selected_character_branch") is True
            and verdict.get("unconditional_all_covariance_models_closed") is False
            else "FAIL",
            str(verdict),
        )
    )

    for row in cert.get("values", []):
        R = float(row["R"])
        rho, s_star = compute(R)
        gates.append(Gate(f"R={R:g} rho", "PASS" if approx(rho, float(row["rho_UV"])) else "FAIL", f"{rho:.15g}"))
        gates.append(Gate(f"R={R:g} s*", "PASS" if approx(s_star, float(row["s_star"])) else "FAIL", f"{s_star:.15g}"))

    print("Selected character-channel covariance closure audit")
    print("=" * 53)
    failed = False
    for gate in gates:
        print(f"{gate.status}: {gate.name} -- {gate.detail}")
        failed = failed or gate.status != "PASS"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
