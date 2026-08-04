"""Audit the selected Iwasawa radius self-consistency candidate."""

from __future__ import annotations

import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Iwasawa_Radius_Self_Consistency_Candidate_v1.md"
CERT = REPO / "certificates" / "selected_iwasawa_radius_self_consistency_candidate_certificate.json"
FINAL_RHO = REPO / "proof_corpus" / "Final_Selected_Character_Rho_UV_Theorem_v1.md"
SCALE = REPO / "proof_corpus" / "Scale_Lifting_Lemma_for_Selected_Flux_Strominger_Functional_v1.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def approx(a: float, b: float, tol: float = 1e-11) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def v1_tilde(R: float) -> float:
    return 64.0 * (2.0 * math.pi) ** 2 / (16.0 * R**4 + 8.0)


def rho_uv(R: float) -> float:
    return v1_tilde(R) ** 2


def s_star(R: float) -> float:
    return (60.0 * rho_uv(R)) ** (1.0 / 6.0)


def r3(R: float) -> float:
    return math.sqrt(8.0 * (2.0 * math.pi) ** 2 / (16.0 + 8.0 / R**4))


def bisect_root() -> float:
    lo, hi = 1e-6, 100.0

    def f(x: float) -> float:
        return x - s_star(x)

    if f(lo) >= 0 or f(hi) <= 0:
        raise AssertionError("bad bracket")
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if f(mid) <= 0:
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
    final_rho = read(FINAL_RHO)
    scale = read(SCALE)
    root = bisect_root()
    expected = cert["numeric_candidate"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "CANDIDATE_RADIUS_CLOSURE_BRIDGE_PREMISE_OPEN",
            cert["status"],
        ),
        check(
            "final rho theorem imported",
            "rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2" in final_rho,
            "rho_UV(R) branch function",
        ),
        check(
            "scale extraction imported",
            "s_* = (60 rho_UV)^(1/6)" in final_rho
            and "s_* = (p A / (2 B))^(1/(p+2))" in scale,
            "scale-lifting formula",
        ),
        check(
            "candidate bridge premise explicit",
            "R = s_*(R)" in note and "bridge premise" in note.lower(),
            "R equals selected dilation premise",
        ),
        check(
            "uniqueness argument explicit",
            "strictly increasing" in note and "strictly decreasing" in note,
            "monotonic fixed-point proof",
        ),
        check("R root", approx(root, expected["R_star"]), f"{root:.16g}"),
        check("fixed point", approx(root, s_star(root)), f"s_star={s_star(root):.16g}"),
        check("r3", approx(r3(root), expected["r3"]), f"{r3(root):.16g}"),
        check("v1", approx(v1_tilde(root), expected["v1_tilde"]), f"{v1_tilde(root):.16g}"),
        check("rho", approx(rho_uv(root), expected["rho_UV"]), f"{rho_uv(root):.16g}"),
        check(
            "not overclaimed",
            cert["verdict"]["final_radius_theorem_closed"] is False
            and "candidate closure" in note,
            cert["verdict"],
        ),
    ]

    print("\nSelected Iwasawa radius self-consistency candidate audit")
    print("========================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
