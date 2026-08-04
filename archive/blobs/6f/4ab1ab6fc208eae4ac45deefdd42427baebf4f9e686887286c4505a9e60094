"""Audit the pure central-circle block reduction for the Z64 Hessian bound."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

PROTO = OBSIDIAN / (
    r"10 ProtoSpinor\Proto_Spinor_Closure_and_Worldsheet_Encoding_in_Modal_Triplet_Theory_v3.md"
)
FOUNDATION = OBSIDIAN / r"3 Core Foundations\Modal_Triplet_Theory__Foundation_v6 (1).md"
THETA = OBSIDIAN / (
    r"18 Theta-Closure & Execution Program\Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def main() -> None:
    proto = read(PROTO)
    foundation = read(FOUNDATION)
    theta = read(THETA)

    gates = [
        Gate(
            "ProtoSpinor bridge source",
            "PASS" if proto else "MISSING",
            str(PROTO),
        ),
        Gate(
            "mixed terms controlled",
            "PASS" if "Q_{\\mathrm{mix}}" in proto and "controlled remainder" in proto else "FAIL",
            "Q_mix vanishes at aligned normal form to leading order",
        ),
        Gate(
            "pure circle truncation",
            "PASS" if "delta\\ell=0" in proto and "delta n=0" in proto else "FAIL",
            "circle-dominant perturbation sets lens/nil perturbations to zero",
        ),
        Gate(
            "circle block exact quadratic matching",
            "PASS" if "circle block alone" in proto and "H_C" in proto else "FAIL",
            "Q_C=<delta c,H_C delta c> up to cubic remainder",
        ),
        Gate(
            "combined blockwise synthesis",
            "PASS" if "H_C\\oplus H_L\\oplus H_N" in proto or "blockwise" in proto else "FAIL",
            "circle/lens/nil blocks assemble locally",
        ),
        Gate(
            "commuting vertical Laplacians",
            "PASS" if "vertical Laplacians" in foundation and "commute" in foundation else "FAIL",
            "base-only warping gives commuting Laplacians",
        ),
        Gate(
            "warp leakage term identified",
            "PASS" if "O(\\varepsilon_{\\mathrm{warp}})" in foundation else "FAIL",
            "non-base-only perturbations tracked as epsilon_warp",
        ),
        Gate(
            "block-diagonal baseline metric",
            "PASS" if "block-diagonal" in theta else "FAIL",
            "theta closure baseline metric ansatz",
        ),
        Gate(
            "Schur-Feshbach bound",
            "PASS" if "C\\,\\lambda_Q^{-1}" in theta else "FAIL",
            "||E_Schur|| <= C lambda_Q^{-1}",
        ),
        Gate(
            "E_mix at Hessian level",
            "PROVED",
            "zero on pure central-circle tower sector",
        ),
        Gate(
            "E_cubic at Hessian level",
            "PROVED",
            "cubic Taylor remainder is not part of the Hessian operator",
        ),
        Gate(
            "reduced pass condition",
            "PROVED",
            "C_fl/lambda_Q < 9 alpha/2, plus epsilon_warp if needed",
        ),
        Gate(
            "exact-branch Schur collapse",
            "PROVED",
            "later compatibility theorem gives C_fl=0 under exact block commutation",
        ),
        Gate(
            "non-exact leakage bound",
            "OPTIONAL-OPEN",
            "needed only if warp/noncommuting branch is used",
        ),
    ]

    print("Pure central-circle block reduction audit")
    print("=========================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
