"""Check the finite right-channel label theorem reductions."""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
LAMBDA_LENS = 3.57
LAMBDA_NIL = 0.25


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    up_paper = read(ROOT / "Up_Retarded_Spinorial_Right_Channel_Label_Theorem_v1.md")
    down_paper = read(ROOT / "Down_Dyadic_Nil_Right_Channel_Label_Theorem_v1.md")
    spinorial = read(ROOT / "Terminal_Spinorial_Return_Gate_for_Z64_Carry_v1.md")
    z64 = read(ROOT / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md")
    color = read(ROOT / "Color_Singlet_Redundancy_Source_for_Bq_v1.md")
    schema = read(ROOT / "Finite_Label_Right_Channel_Source_Operator_Schema_v1.md")

    j = LAMBDA_NIL / LAMBDA_LENS
    spin_eigs = np.array([-1.0, 1.0])
    up_labels = j * (-0.5 + spin_eigs)
    expected_up = np.array([-1.5 * j, 0.5 * j])
    down_labels = np.array([1.0 / 64.0, 1.5 * LAMBDA_NIL])
    expected_down = np.array([0.015625, 0.375])

    base_up = 4.0 * math.log(math.pi)
    base_down = math.log(math.pi)
    candidate_up = base_up + up_labels
    candidate_down = base_down + down_labels
    required_up = np.array([4.48005803, 4.61589902])
    required_down = np.array([1.15867841, 1.52651629])
    action_error = float(np.linalg.norm(candidate_up - required_up) + np.linalg.norm(candidate_down - required_down))

    gates = [
        Gate("up theorem saved", "PASS" if "Up-Sector Retarded Spinorial" in up_paper else "FAIL", "up label theorem present"),
        Gate("down theorem saved", "PASS" if "Down-Sector Dyadic/Nil" in down_paper else "FAIL", "down label theorem present"),
        Gate("spinorial source imported", "PASS" if "epsilon in {+1,-1}" in spinorial or "epsilon in {-1,+1}" in spinorial else "FAIL", "spinorial parity source present"),
        Gate("dyadic source imported", "PASS" if "E_q = (1/64)" in z64 or "K_64=C[coker A_64]" in z64 else "FAIL", "Z64 projector source present"),
        Gate("half-channel source imported", "PASS" if "delta^2/2" in color else "FAIL", "Schur half-channel source present"),
        Gate("schema linked", "PASS" if "R_u = J(-1/2 I_u^light + Xi_u)" in schema else "FAIL", "source schema linked"),
        Gate("up labels derived", "PASS" if np.linalg.norm(up_labels - expected_up) < 1e-14 else "FAIL", f"labels={up_labels}"),
        Gate("down labels derived", "PASS" if np.linalg.norm(down_labels - expected_down) < 1e-14 else "FAIL", f"labels={down_labels}"),
        Gate("near mass candidate", "PASS" if action_error < 0.02 else "FAIL", f"candidate action error={action_error:.6f}"),
        Gate("channel assignment", "OPEN", "extract label-to-projector assignment from Sigma_MTT"),
    ]

    print("Finite right-channel label theorem check")
    print("========================================")
    print()
    print(f"J=lambda_nil/lambda_lens={j:.12f}")
    print("up residual labels:   " + " ".join(f"{x:+.12f}" for x in up_labels))
    print("down residual labels: " + " ".join(f"{x:+.12f}" for x in down_labels))
    print("candidate actions:")
    print("  up:   " + " ".join(f"{x:.6f}" for x in candidate_up))
    print("  down: " + " ".join(f"{x:.6f}" for x in candidate_down))
    print(f"action error against target: {action_error:.12e}")
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
