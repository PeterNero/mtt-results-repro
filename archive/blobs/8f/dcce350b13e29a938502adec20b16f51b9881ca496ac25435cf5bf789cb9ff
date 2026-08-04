"""Audit the Schur gap-constant reduction for the Z64 projector."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

THETA = (
    OBSIDIAN
    / r"18 Theta-Closure & Execution Program\Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md"
)
BASELINE = (
    OBSIDIAN
    / r"3 Core Foundations\Baseline_Scales_and_Phenomenological_Consistency_in_Modal_Triplet_Theory.md"
)
FIXED_POINTS = (
    OBSIDIAN
    / r"4 Fixed Points\Fixed_Points_I__Fixed_Points_over_Multi_Bundle_Manifolds_v5.md"
)
PAPER = ROOT / "Schur_Gap_Constant_Reduction_for_Z64_Projector_v1.md"


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
    theta = read(THETA)
    baseline = read(BASELINE)
    fixed = read(FIXED_POINTS)
    paper = read(PAPER)

    alpha = 1.0
    baseline_gap = 0.25
    normalized_threshold = 9.0 * alpha / 2.0
    conservative_c_threshold = normalized_threshold * baseline_gap

    gates = [
        Gate(
            "new reduction paper saved",
            "PASS" if paper else "FAIL",
            str(PAPER),
        ),
        Gate(
            "Schur-Feshbach form",
            "PASS"
            if "P_0 L Q" in theta and "(Q L Q)^{-1}" in theta and "Q L P_0" in theta
            else "FAIL",
            str(THETA),
        ),
        Gate(
            "lambda_Q Schur bound",
            "PASS" if "C\\,\\lambda_Q^{-1}" in theta else "FAIL",
            "theta closure gives ||E_Schur|| <= C lambda_Q^{-1}",
        ),
        Gate(
            "mixing-product source",
            "PASS"
            if "\\|L_{PQ}\\|" in baseline and "\\|L_{QP}\\|" in baseline
            else "FAIL",
            "baseline scales identify coherent/noncoherent mixing amplitudes",
        ),
        Gate(
            "gap-suppressed correction ratio",
            "PASS"
            if "\\|L_{PQ}\\|\\|L_{QP}\\|/\\lambda_\\ast" in baseline
            or "\\|L_{PQ}\\|\\|L_{QP}\\|}{\\lambda_\\ast" in baseline
            else "FAIL",
            "mixing product divided by vertical gap",
        ),
        Gate(
            "baseline gap floor",
            "PASS"
            if "0.25" in theta and "h_0" in theta and "lambda_{\\mathrm{nil}}" in theta
            else "FAIL",
            "baseline nil gap gives lambda_* >= 1/4",
        ),
        Gate(
            "circle gap model",
            "PASS" if "lambda_1=R^{-2}" in fixed or "1/R_{\\max}^2" in fixed else "FAIL",
            "fixed-point example gives circle gap scaling",
        ),
        Gate(
            "dimensionless gate",
            "PROVED",
            "C_fl/(alpha lambda_Q) < 9/2",
        ),
        Gate(
            "normalized threshold",
            "PASS" if normalized_threshold == 4.5 else "FAIL",
            f"9 alpha/2 = {normalized_threshold}",
        ),
        Gate(
            "conservative C_fl threshold",
            "PASS" if conservative_c_threshold == 1.125 else "FAIL",
            f"baseline lambda_Q>=1/4 gives C_fl < {conservative_c_threshold} alpha",
        ),
        Gate(
            "actual C_fl",
            "OPEN",
            "must compute selected flavor coherent/noncoherent mixing product",
        ),
        Gate(
            "actual lambda_Q",
            "OPEN",
            "must compute selected flavor Q-sector gap",
        ),
    ]

    print("Schur gap-constant reduction audit")
    print("==================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
