"""Check source candidates for the weighted right-eigenchannel mass actions."""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    paper = read(ROOT / "Weighted_Right_Eigenchannel_Action_Source_Candidates_v1.md")
    right = read(ROOT / "Right_Eigenchannel_Mass_Layer_Theorem_Target_v1.md")
    mass_req = read(ROOT / "Selected_Mass_Layer_Requirements_after_Bq_v1.md")

    a_up = np.array([4.48005803, 4.61589902], dtype=float)
    a_down = np.array([1.15867841, 1.52651629], dtype=float)
    q_up = 2.0
    q_down = 1.0

    structural_primitives = {
        "log(pi)": math.log(math.pi),
        "log(2*pi)": math.log(2.0 * math.pi),
        "log(4)": math.log(4.0),
        "log(e*pi/2)": math.log(math.e * math.pi / 2.0),
        "lambda_nil/lambda_lens": 0.25 / 3.57,
    }

    rows: list[tuple[str, float, float, float, float]] = []
    for label, primitive in structural_primitives.items():
        predicted_up = q_up * q_up * primitive
        predicted_down = q_down * q_down * primitive
        residual = float(
            np.linalg.norm(a_up - predicted_up) + np.linalg.norm(a_down - predicted_down)
        )
        rows.append((label, primitive, predicted_up, predicted_down, residual))
    rows.sort(key=lambda row: row[4])

    log_pi = math.log(math.pi)
    base_up = q_up * q_up * log_pi
    base_down = q_down * q_down * log_pi
    residual_up = a_up - base_up
    residual_down = a_down - base_down
    split_up = a_up - float(np.mean(a_up))
    split_down = a_down - float(np.mean(a_down))

    gates = [
        Gate(
            "paper saved",
            "PASS" if "Weighted Right-Eigenchannel Action Source Candidates" in paper else "FAIL",
            "candidate-source paper present",
        ),
        Gate(
            "right theorem synchronized",
            "PASS" if "A_u ~= (4.480058, 4.615899, 0)" in right else "FAIL",
            "right-eigenchannel theorem carries corrected actions",
        ),
        Gate(
            "requirements imported",
            "PASS" if "A_u ~= 4.55" in mass_req and "A_d ~= 1.34" in mass_req else "FAIL",
            "mass-action requirements imported",
        ),
        Gate(
            "corpus source classes",
            "PASS" if "localized zero-mode overlap actions" in paper and "finite allowed instanton" in paper else "FAIL",
            "allowed mechanisms listed",
        ),
        Gate(
            "no-proxy guard",
            "PASS" if "observed quark masses" in paper and "entry-wise Yukawa fits" in paper else "FAIL",
            "proxy sources excluded",
        ),
        Gate(
            "log(pi) primitive",
            "DIAGNOSTIC" if rows[0][0] == "log(pi)" else "OPEN",
            f"best simple primitive={rows[0][0]}, residual={rows[0][4]:.6f}",
        ),
        Gate(
            "family splitting",
            "OPEN",
            "derive residuals from widths/instanton/Higgs/nil finite-width data",
        ),
    ]

    print("Weighted right-eigenchannel action source candidate check")
    print("=========================================================")
    print()
    print("Required actions:")
    print("  A_u: " + " ".join(f"{x:.6f}" for x in a_up))
    print("  A_d: " + " ".join(f"{x:.6f}" for x in a_down))
    print("Means and splits:")
    print(f"  mean(A_u)={np.mean(a_up):.6f}, split={split_up[0]:+.6f} {split_up[1]:+.6f}")
    print(f"  mean(A_d)={np.mean(a_down):.6f}, split={split_down[0]:+.6f} {split_down[1]:+.6f}")
    print()
    print("Simple structural primitives, using q_u=2 and q_d=1:")
    for label, primitive, predicted_up, predicted_down, residual in rows:
        print(
            f"  {label:18s} primitive={primitive:.6f} "
            f"up={predicted_up:.6f} down={predicted_down:.6f} residual={residual:.6f}"
        )
    print()
    print("log(pi) base residuals:")
    print("  A_u - 4log(pi): " + " ".join(f"{x:+.6f}" for x in residual_up))
    print("  A_d -  log(pi): " + " ".join(f"{x:+.6f}" for x in residual_down))
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
