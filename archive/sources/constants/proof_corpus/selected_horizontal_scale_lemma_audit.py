"""Audit the selected horizontal-scale lemma for Iwasawa rho_UV."""

from __future__ import annotations

import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Horizontal_Scale_Lemma_for_Iwasawa_Rho_UV_v1.md"
CERT = REPO / "certificates" / "selected_horizontal_scale_lemma_certificate.json"
POLICY = REPO / "proof_corpus" / "Primitive_Constant_Discipline_for_No_Knob_Program_v1.md"
FINAL_RHO = REPO / "proof_corpus" / "Final_Selected_Character_Rho_UV_Theorem_v1.md"
BRIDGE = REPO / "proof_corpus" / "Selected_Iwasawa_Radius_Bridge_Reduction_v1.md"


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
    policy = read(POLICY)
    final_rho = read(FINAL_RHO)
    bridge = read(BRIDGE)
    root = bisect_root()
    vals = cert["candidate_values"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "HORIZONTAL_SCALE_REDUCTION_CLOSED_BIANCHI_SCALE_CHECK_OPEN",
            cert["status"],
        ),
        check(
            "rho theorem imported",
            "rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2" in final_rho,
            "final rho theorem",
        ),
        check(
            "bridge reduction imported",
            "Selected Horizontal-Scale Lemma" in bridge,
            "prior bridge reduction",
        ),
        check(
            "one-dimensional coordinate proved",
            "No second independent scale appears" in note
            and cert["closed"]["one_dimensional_horizontal_coordinate"] is True,
            "R only in coefficient quotient",
        ),
        check(
            "full dilation not overclaimed",
            "does not prove that the full unprojected metric dilation" in note
            and cert["verdict"]["final_numeric_rho_uv_closed"] is False,
            "Bianchi-constrained check remains open",
        ),
        check(
            "primitive fallback disciplined",
            "primitive constant != adjustable fit knob" in policy
            and cert["primitive_constant_fallback"]["allowed_in_principle"] is True,
            "primitive policy imported",
        ),
        check("R root", approx(root, vals["R_star"]), f"{root:.16g}"),
        check("fixed point", approx(root, s_star(root)), f"{s_star(root):.16g}"),
        check("r3", approx(r3(root), vals["r3"]), f"{r3(root):.16g}"),
        check("v1", approx(v1_tilde(root), vals["v1_tilde"]), f"{v1_tilde(root):.16g}"),
        check("rho", approx(rho_uv(root), vals["rho_UV"]), f"{rho_uv(root):.16g}"),
        check(
            "next artifact identified",
            cert["verdict"]["next_required_artifact"]
            == "Bianchi_Constrained_Scale_Lifting_Check_for_Iwasawa_Rho_UV_v1",
            cert["verdict"]["next_required_artifact"],
        ),
    ]

    print("\nSelected horizontal-scale lemma audit")
    print("=====================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
