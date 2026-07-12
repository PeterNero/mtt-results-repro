"""Audit the selected Iwasawa radius bridge reduction."""

from __future__ import annotations

import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Iwasawa_Radius_Bridge_Reduction_v1.md"
CERT = REPO / "certificates" / "selected_iwasawa_radius_bridge_reduction_certificate.json"
FINAL_RHO = REPO / "proof_corpus" / "Final_Selected_Character_Rho_UV_Theorem_v1.md"
SCALE = REPO / "proof_corpus" / "Scale_Lifting_Lemma_for_Selected_Flux_Strominger_Functional_v1.md"
MINIMIZATION = REPO / "proof_corpus" / "Selected_Normalization_Minimization_Functional_v1.md"


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


def r1_exact(n: int) -> float:
    return math.sqrt(math.log(n) / 15.0)


def bisect_root() -> float:
    lo, hi = 1e-6, 100.0

    def f(x: float) -> float:
        return x - s_star(x)

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
    minimization = read(MINIMIZATION)
    root = bisect_root()
    cond = cert["conditional_theorem"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "BRIDGE_REDUCED_TO_SINGLE_HORIZONTAL_SCALE_LEMMA",
            cert["status"],
        ),
        check(
            "rho branch imported",
            "rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2" in final_rho,
            "final selected-character rho theorem",
        ),
        check(
            "scale variable caveat recorded",
            "common dilation" in note and "horizontal radius" in note,
            "bridge cannot be silently assumed",
        ),
        check(
            "minimization source has s definition",
            "s              = remaining positive dilation / string-unit scale" in minimization,
            "s definition",
        ),
        check(
            "scale source has dilation premise",
            "For a dilation of the internal metric" in scale,
            "scale-lifting premise",
        ),
        check(
            "bridge lemma not overclosed",
            cert["bridge_lemma"]["closed"] is False
            and cert["verdict"]["final_rho_uv_numeric_closed"] is False,
            cert["bridge_lemma"],
        ),
        check("R root", approx(root, cond["R_star"]), f"{root:.16g}"),
        check("fixed point", approx(root, s_star(root)), f"s_star={s_star(root):.16g}"),
        check("r3", approx(r3(root), cond["r3"]), f"{r3(root):.16g}"),
        check("v1", approx(v1_tilde(root), cond["v1_tilde"]), f"{v1_tilde(root):.16g}"),
        check("rho", approx(rho_uv(root), cond["rho_UV"]), f"{rho_uv(root):.16g}"),
    ]

    for row in cert["shared_circle_compatibility"]:
        n = int(row["N"])
        r1 = r1_exact(n)
        checks.append(check(f"N={n} R1", approx(r1, float(row["R1"])), f"{r1:.16g}"))
        checks.append(
            check(
                f"N={n} R1/R_star",
                approx(r1 / root, float(row["R1_over_R_star"])),
                f"{r1 / root:.16g}",
            )
        )
        checks.append(check(f"N={n} R1<=2", r1 <= 2.0 and row["central_circle_bound_R1_le_2"], r1))

    checks.extend(
        [
            check(
                "no shared-circle contradiction",
                cert["verdict"]["shared_circle_contradiction_found"] is False
                and "R_* is not the central-circle radius" in note,
                cert["verdict"],
            ),
            check(
                "next artifact identified",
                cert["verdict"]["next_required_artifact"]
                == "Selected_Horizontal_Scale_Lemma_for_Iwasawa_Rho_UV_v1",
                cert["verdict"]["next_required_artifact"],
            ),
        ]
    )

    print("\nSelected Iwasawa radius bridge reduction audit")
    print("==============================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
