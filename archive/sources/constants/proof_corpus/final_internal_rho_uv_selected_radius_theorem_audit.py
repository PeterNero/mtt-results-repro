"""Audit the final internal rho_UV selected-radius theorem."""

from __future__ import annotations

import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Final_Internal_Rho_UV_Selected_Radius_Theorem_v1.md"
CERT = REPO / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"
LAW = REPO / "proof_corpus" / "Selected_Horizontal_Scale_Law_for_Iwasawa_Rho_UV_v1.md"
RHO = REPO / "proof_corpus" / "Final_Selected_Character_Rho_UV_Theorem_v1.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def approx(a: float, b: float, tol: float = 1e-10) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def v1_tilde(R: float) -> float:
    return 64.0 * (2.0 * math.pi) ** 2 / (16.0 * R**4 + 8.0)


def rho_uv(R: float) -> float:
    return v1_tilde(R) ** 2


def s_star_from_rho(R: float) -> float:
    return (60.0 * rho_uv(R)) ** (1.0 / 6.0)


def r3(R: float) -> float:
    return math.sqrt(8.0 * (2.0 * math.pi) ** 2 / (16.0 + 8.0 / R**4))


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    law = read(LAW)
    rho = read(RHO)
    vals = cert["selected_values"]
    R = float(vals["R_star"])

    checks = [
        check("certificate status", cert["status"] == "FINAL_INTERNAL_RHO_UV_BRANCH_CLOSED", cert["status"]),
        check("rho branch imported", "rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2" in rho, "rho theorem"),
        check("H2 law imported", "selected horizontal scale law = H2" in law, "scale law theorem"),
        check("theorem states closure", "rho_UV internal branch is closed" in note, "closure statement"),
        check("R", approx(R, 4.440528182269818), f"{R:.16g}"),
        check("r3", approx(r3(R), vals["r3"]), f"{r3(R):.16g}"),
        check("v1", approx(v1_tilde(R), vals["v1_tilde"]), f"{v1_tilde(R):.16g}"),
        check("rho", approx(rho_uv(R), vals["rho_UV"]), f"{rho_uv(R):.16g}"),
        check("s star", approx(s_star_from_rho(R), vals["s_star_from_rho"]), f"{s_star_from_rho(R):.16g}"),
        check(
            "no overclaim",
            "dimensionful SI constant" in cert["not_claimed"]
            and "electroweak prediction" in cert["not_claimed"]
            and cert["verdict"]["internal_no_knob_branch_closed"] is True,
            cert["not_claimed"],
        ),
    ]

    print("\nFinal internal rho_UV selected-radius theorem audit")
    print("===================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
