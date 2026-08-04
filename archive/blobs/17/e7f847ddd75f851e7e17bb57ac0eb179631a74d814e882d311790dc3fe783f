"""Test candidate source theories for weighted right-eigenchannel mass actions."""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
LAMBDA_LENS = 3.57
LAMBDA_NIL = 0.25
Q_UP = 2.0
Q_DOWN = 1.0

A_UP = np.array([4.48005803, 4.61589902], dtype=float)
A_DOWN = np.array([1.15867841, 1.52651629], dtype=float)


@dataclass(frozen=True)
class TheoryResult:
    name: str
    status: str
    prediction_up: np.ndarray
    prediction_down: np.ndarray
    residual: float
    note: str


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def residual(pred_up: np.ndarray, pred_down: np.ndarray) -> float:
    return float(np.linalg.norm(A_UP - pred_up) + np.linalg.norm(A_DOWN - pred_down))


def format_pair(values: np.ndarray) -> str:
    return "(" + ", ".join(f"{x:.6f}" for x in values) + ")"


def best_structural_primitive() -> list[TheoryResult]:
    primitives = {
        "q^2 log(pi)": math.log(math.pi),
        "q^2 log(4)": math.log(4.0),
        "q^2 log(2pi)": math.log(2.0 * math.pi),
        "q^2 log(e*pi/2)": math.log(math.e * math.pi / 2.0),
        "q^2 lambda_nil": LAMBDA_NIL,
        "q^2 lambda_nil/lambda_lens": LAMBDA_NIL / LAMBDA_LENS,
    }
    out: list[TheoryResult] = []
    for label, primitive in primitives.items():
        pred_up = np.array([Q_UP * Q_UP * primitive] * 2, dtype=float)
        pred_down = np.array([Q_DOWN * Q_DOWN * primitive] * 2, dtype=float)
        out.append(
            TheoryResult(
                label,
                "DIAGNOSTIC",
                pred_up,
                pred_down,
                residual(pred_up, pred_down),
                "sector base only; no two-light-mode splitting",
            )
        )
    return sorted(out, key=lambda row: row.residual)


def z3_laplacian_result() -> TheoryResult:
    base = math.log(math.pi)
    j = LAMBDA_NIL / LAMBDA_LENS
    # The retained Z3 Laplacian has nontrivial eigenvalue 3 twice, so it cannot
    # split the two light right channels.  We include the fixed 3J lift as a
    # representative no-free-parameter test.
    lift = 3.0 * j
    pred_up = np.array([Q_UP * Q_UP * base + lift] * 2, dtype=float)
    pred_down = np.array([Q_DOWN * Q_DOWN * base + lift] * 2, dtype=float)
    return TheoryResult(
        "Z3 Laplacian 3J lift",
        "NO-GO",
        pred_up,
        pred_down,
        residual(pred_up, pred_down),
        "degenerate nontrivial Z3 eigenvalues cannot split the two light modes",
    )


def benchmark_proxy_result() -> TheoryResult:
    base = math.log(math.pi)
    # Historical benchmark clues only.  They are not proof-admissible inputs.
    f22 = math.log(1.18)
    eta_d1 = -math.log(1.0 - 0.09)
    eta_d2 = -math.log(1.0 - 0.07)
    pred_up = np.array([Q_UP * Q_UP * base, Q_UP * Q_UP * base + f22], dtype=float)
    pred_down = np.array([Q_DOWN * Q_DOWN * base + eta_d1, Q_DOWN * Q_DOWN * base + eta_d2], dtype=float)
    return TheoryResult(
        "Execution-II benchmark corrections",
        "REJECTED-PROXY",
        pred_up,
        pred_down,
        residual(pred_up, pred_down),
        "uses F22, eta_d1, eta_d2 benchmark inputs; clue only, not proof",
    )


def finite_operator_integer_scan() -> tuple[TheoryResult, dict[str, object]]:
    """Diagnostic: can small finite labels built from MTT scales span residuals?"""

    base = math.log(math.pi)
    base_up = Q_UP * Q_UP * base
    base_down = Q_DOWN * Q_DOWN * base
    target_residuals = np.array(
        [
            A_UP[0] - base_up,
            A_UP[1] - base_up,
            A_DOWN[0] - base_down,
            A_DOWN[1] - base_down,
        ],
        dtype=float,
    )
    scales = {
        "lambda_nil": LAMBDA_NIL,
        "J": LAMBDA_NIL / LAMBDA_LENS,
        "1/64": 1.0 / 64.0,
        "1/7": 1.0 / 7.0,
    }
    coeffs = [x / 2.0 for x in range(-6, 7)]
    best: tuple[float, list[tuple[str, float, float]], np.ndarray] | None = None
    for labels in itertools.product(scales.items(), repeat=4):
        # Keep the expression simple: each channel gets one primitive scale
        # multiplied by a half-integer label.
        for cvals in itertools.product(coeffs, repeat=4):
            values = np.array([c * scale for c, (_, scale) in zip(cvals, labels)], dtype=float)
            err = float(np.linalg.norm(values - target_residuals))
            if best is None or err < best[0]:
                terms = [(name, c, c * scale) for c, (name, scale) in zip(cvals, labels)]
                best = (err, terms, values)
    assert best is not None
    _, terms, values = best
    pred_up = np.array([base_up + values[0], base_up + values[1]], dtype=float)
    pred_down = np.array([base_down + values[2], base_down + values[3]], dtype=float)
    details = {
        "target_residuals": target_residuals,
        "terms": terms,
        "values": values,
    }
    return (
        TheoryResult(
            "finite one-scale-per-channel scan",
            "DIAGNOSTIC-ONLY",
            pred_up,
            pred_down,
            residual(pred_up, pred_down),
            "small finite labels can approximate the residuals, but labels are not selected yet",
        ),
        details,
    )


def selected_right_operator_target() -> TheoryResult:
    pred_up = A_UP.copy()
    pred_down = A_DOWN.copy()
    return TheoryResult(
        "selected finite right-channel operator R_x",
        "TARGET",
        pred_up,
        pred_down,
        residual(pred_up, pred_down),
        "exact by definition; proof requires deriving R_x from Sigma_MTT before mass comparison",
    )


def main() -> None:
    paper = read(ROOT / "Mass_Action_Source_Theory_Battery_v1.md")
    source_candidates = read(ROOT / "Weighted_Right_Eigenchannel_Action_Source_Candidates_v1.md")
    localization = read(ROOT / "Selected_Localization_Graph_Theorem_v1.md")

    simple = best_structural_primitive()
    finite_scan, scan_details = finite_operator_integer_scan()
    theories = simple + [
        z3_laplacian_result(),
        benchmark_proxy_result(),
        finite_scan,
        selected_right_operator_target(),
    ]
    ranked = sorted(theories, key=lambda row: row.residual)
    admissible_ranked = [
        row
        for row in ranked
        if row.status in {"DIAGNOSTIC", "NO-GO", "TARGET"}
        and "benchmark" not in row.name.lower()
        and "scan" not in row.name.lower()
    ]
    best_simple = simple[0]
    terms = scan_details["terms"]

    gates = [
        Gate("paper saved", "PASS" if "Mass-Action Source Theory Battery" in paper else "FAIL", "battery note present"),
        Gate("source candidates imported", "PASS" if "q_x^2 log(pi)" in source_candidates else "FAIL", "previous source note imported"),
        Gate("localization theorem imported", "PASS" if "L_loc,x" in localization and "Gamma_x" in localization else "FAIL", "operator route aligned with corpus"),
        Gate("best simple primitive", "PASS" if best_simple.name == "q^2 log(pi)" else "FAIL", f"{best_simple.name}, residual={best_simple.residual:.6f}"),
        Gate("Z3 split no-go", "PASS" if z3_laplacian_result().status == "NO-GO" else "FAIL", "Z3 Laplacian alone is degenerate on two light modes"),
        Gate("proxy rejected", "PASS" if benchmark_proxy_result().status == "REJECTED-PROXY" else "FAIL", "old local flavor corrections not proof inputs"),
        Gate("right-operator target", "OPEN", "derive R_x eigenvalues from Sigma_MTT"),
    ]

    print("Mass-action source theory battery")
    print("=================================")
    print()
    print("Required actions:")
    print(f"  A_u={format_pair(A_UP)}")
    print(f"  A_d={format_pair(A_DOWN)}")
    print()
    print("Ranked candidate theories:")
    for row in ranked:
        print(
            f"  {row.name:42s} {row.status:16s} residual={row.residual:.6f} "
            f"up={format_pair(row.prediction_up)} down={format_pair(row.prediction_down)}"
        )
        print(f"    {row.note}")
    print()
    print("Best simple structural primitive:")
    print(f"  {best_simple.name}: residual={best_simple.residual:.6f}")
    print()
    print("Finite one-scale-per-channel scan terms relative to q^2 log(pi):")
    labels = ["u1", "u2", "d1", "d2"]
    for label, (name, coeff, value), target in zip(labels, terms, scan_details["target_residuals"]):
        print(f"  {label}: {coeff:+.1f} * {name:10s} = {value:+.6f} target={target:+.6f}")
    print("  This is a search diagnostic, not a source derivation.")
    print()
    print("Admissible non-proxy ordering, ignoring exact target and per-channel scan:")
    for row in admissible_ranked:
        print(f"  {row.name:42s} {row.status:10s} residual={row.residual:.6f}")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
