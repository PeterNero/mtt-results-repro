"""Audit the Bianchi-constrained scale-lifting check for Iwasawa rho_UV."""

from __future__ import annotations

import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Bianchi_Constrained_Scale_Lifting_Check_for_Iwasawa_Rho_UV_v1.md"
CERT = REPO / "certificates" / "bianchi_constrained_scale_lifting_check_certificate.json"
HORIZONTAL = REPO / "proof_corpus" / "Selected_Horizontal_Scale_Lemma_for_Iwasawa_Rho_UV_v1.md"


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


def f_h1(R: float) -> float:
    return rho_uv(R) * R**-4 + (1.0 / 30.0) * R**2


def f_h2(R: float) -> float:
    return rho_uv(R) + (1.0 / 30.0) * R**2


def minimize(func) -> float:
    lo, hi = 1e-4, 50.0
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    c = hi - gr * (hi - lo)
    d = lo + gr * (hi - lo)
    for _ in range(300):
        if func(c) < func(d):
            hi = d
            d = c
            c = hi - gr * (hi - lo)
        else:
            lo = c
            c = d
            d = lo + gr * (hi - lo)
    return (lo + hi) / 2.0


def fixed_root() -> float:
    lo, hi = 1e-6, 100.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if mid - s_star(mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    horizontal = read(HORIZONTAL)
    root_fp = fixed_root()
    root_h1 = minimize(f_h1)
    root_h2 = minimize(f_h2)
    h1 = cert["branch_H1_extra_horizontal_residual_scaling"]
    h2 = cert["branch_H2_rho_already_full_uv_response"]

    checks = [
        check("certificate status", cert["status"] == "SCALE_LAW_SELECTION_OPEN_FIXED_POINT_NOT_YET_FINAL", cert["status"]),
        check("horizontal lemma imported", "Bianchi-Constrained Scale-Lifting Check" in horizontal, "previous next gate"),
        check("overclaim warning stated", "not automatically" in note and "fixed-point candidate" in note, "R=s*(R) not final"),
        check("FP root", approx(root_fp, cert["old_fixed_point_candidate"]["R"]), f"{root_fp:.16g}"),
        check("H1 root", approx(root_h1, h1["R_min"]), f"{root_h1:.16g}"),
        check("H1 rho", approx(rho_uv(root_h1), h1["rho_UV"]), f"{rho_uv(root_h1):.16g}"),
        check("H1 s", approx(s_star(root_h1), h1["s_star"]), f"{s_star(root_h1):.16g}"),
        check("H1 r3", approx(r3(root_h1), h1["r3"]), f"{r3(root_h1):.16g}"),
        check("H2 root", approx(root_h2, h2["R_min"]), f"{root_h2:.16g}"),
        check("H2 rho", approx(rho_uv(root_h2), h2["rho_UV"]), f"{rho_uv(root_h2):.16g}"),
        check("H2 s", approx(s_star(root_h2), h2["s_star"]), f"{s_star(root_h2):.16g}"),
        check("H2 r3", approx(r3(root_h2), h2["r3"]), f"{r3(root_h2):.16g}"),
        check(
            "final not closed",
            cert["verdict"]["final_numeric_rho_uv_closed"] is False
            and cert["closed"]["overclaim_prevented"] is True,
            cert["verdict"],
        ),
        check(
            "next artifact identified",
            cert["verdict"]["next_required_artifact"]
            == "Selected_Horizontal_Scale_Law_for_Iwasawa_Rho_UV_v1",
            cert["verdict"]["next_required_artifact"],
        ),
    ]

    print("\nBianchi-constrained scale-lifting check audit")
    print("============================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
