"""Audit the selected horizontal scale law for Iwasawa rho_UV."""

from __future__ import annotations

import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Horizontal_Scale_Law_for_Iwasawa_Rho_UV_v1.md"
CERT = REPO / "certificates" / "selected_horizontal_scale_law_certificate.json"
BIANCHI = REPO / "proof_corpus" / "Bianchi_Constrained_Scale_Lifting_Check_for_Iwasawa_Rho_UV_v1.md"
FINAL_RHO = REPO / "proof_corpus" / "Final_Selected_Character_Rho_UV_Theorem_v1.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def approx(a: float, b: float, tol: float = 1e-10) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def v1_tilde(R: float) -> float:
    return 64.0 * (2.0 * math.pi) ** 2 / (16.0 * R**4 + 8.0)


def rho_uv(R: float) -> float:
    return v1_tilde(R) ** 2


def s_star(R: float) -> float:
    return (60.0 * rho_uv(R)) ** (1.0 / 6.0)


def r3(R: float) -> float:
    return math.sqrt(8.0 * (2.0 * math.pi) ** 2 / (16.0 + 8.0 / R**4))


def dF_dx(x: float) -> float:
    a = 64.0 * (2.0 * math.pi) ** 2
    return 1.0 / 30.0 - 64.0 * a * a * x / (16.0 * x * x + 8.0) ** 3


def bisection_x(lo: float, hi: float) -> float:
    flo = dF_dx(lo)
    for _ in range(240):
        mid = (lo + hi) / 2.0
        fmid = dF_dx(mid)
        if flo * fmid <= 0:
            hi = mid
        else:
            lo = mid
            flo = fmid
    return (lo + hi) / 2.0


def stationary_points() -> tuple[float, float]:
    xs = []
    prev_x = 1e-12
    prev = dF_dx(prev_x)
    for i in range(1, 200000):
        x = 10.0 ** (-12.0 + 16.0 * i / 199999.0)
        val = dF_dx(x)
        if val * prev < 0.0:
            xs.append(bisection_x(prev_x, x))
        prev_x = x
        prev = val
    return math.sqrt(xs[0]), math.sqrt(xs[1])


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    bianchi = read(BIANCHI)
    final_rho = read(FINAL_RHO)
    r_max, r_min = stationary_points()
    vals = cert["selected_values"]

    checks = [
        check("certificate status", cert["status"] == "H2_HORIZONTAL_SCALE_LAW_SELECTED", cert["status"]),
        check("prior gate imported", "Selected_Horizontal_Scale_Law_for_Iwasawa_Rho_UV_v1" in bianchi, "Bianchi check next artifact"),
        check("rho theorem imported", "rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2" in final_rho, "rho branch"),
        check("H2 selected", cert["selected_law"]["id"] == "H2" and "F_H2(R)" in note, cert["selected_law"]),
        check("H1 rejected", "double-counts" in note and "R^(-4)" in note, cert["rejected"]["H1"]),
        check("FP rejected as final Euler", "not the selected Euler equation" in note, cert["rejected"]["FP"]),
        check("local max", approx(r_max, cert["stationary_points"]["local_max_R"]), f"{r_max:.16g}"),
        check("global min", approx(r_min, cert["stationary_points"]["global_min_R"]), f"{r_min:.16g}"),
        check("r3", approx(r3(r_min), vals["r3"]), f"{r3(r_min):.16g}"),
        check("v1", approx(v1_tilde(r_min), vals["v1_tilde"]), f"{v1_tilde(r_min):.16g}"),
        check("rho", approx(rho_uv(r_min), vals["rho_UV"]), f"{rho_uv(r_min):.16g}"),
        check("s star", approx(s_star(r_min), vals["s_star_from_rho"]), f"{s_star(r_min):.16g}"),
        check(
            "internal closure not SI overclaim",
            cert["closed"]["rho_UV_selected_internal_dimensionless"] is True
            and "dimensionful SI normalization" in cert["not_closed"],
            cert["not_closed"],
        ),
    ]

    print("\nSelected horizontal scale law audit")
    print("===================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
