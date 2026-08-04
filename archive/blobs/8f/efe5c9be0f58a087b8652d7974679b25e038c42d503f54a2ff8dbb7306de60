"""Check formal Route-B finite-trace rows as right-label value support."""

from __future__ import annotations

import cmath
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
SMP = TEXPAPERS / "mtt-sm-parity-closure"
FORMAL_ROWS = (
    SMP
    / "candidate_data"
    / "selected_routeaemission_or_routebgalerkinrows_execution"
    / "formal_110_row_execution.packet.json"
)
ROUTING = SMP / "candidate_data" / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json"
PAYLOAD = ROOT / "selected_primitive_kernel_source_payload.formal_routeb_attempt.json"

Q = 79
N = 448
LAMBDA_LENS = 3.57
LAMBDA_NIL = 0.25
TOL = 1e-12


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def to_complex(value: Any) -> complex:
    if isinstance(value, (int, float)):
        return complex(value)
    if isinstance(value, list) and len(value) == 2:
        return complex(float(value[0]), float(value[1]))
    raise TypeError(f"unsupported value {value!r}")


def row_matrix(rows: list[dict[str, Any]], sector: str, response: str) -> np.ndarray:
    matrix = np.zeros((3, 3), dtype=complex)
    for row in rows:
        if row.get("sector") == sector and row.get("response") == response:
            coordinate = row["coordinate"]
            i = int(coordinate[1])
            j = int(coordinate[3])
            matrix[i, j] = to_complex(row["finite_trace_quadrature_value"])
    return (matrix + matrix.conj().T) / 2.0


def y_selected(mu: float, phase_shift: int, j_profile: np.ndarray, tau: complex) -> np.ndarray:
    lambda_q = LAMBDA_LENS - LAMBDA_NIL
    weights = np.exp(-mu * j_profile) * np.array([tau ** (phase_shift * b) for b in range(3)], dtype=complex)
    y = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            b = (-(i + j)) % 3
            cost = (j_profile[i] - j_profile[b]) ** 2
            cost += 0.5 * (j_profile[j] - j_profile[(b - 1) % 3]) ** 2
            y[i, j] = weights[b] * math.exp(-lambda_q * float(cost))
    return y


def right_projectors(mu: float, phase_shift: int) -> list[np.ndarray]:
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    tau = cmath.exp(2j * math.pi * Q / N)
    g_inv_sqrt = np.diag(np.exp(-1.0 * j_profile))
    z = y_selected(mu, phase_shift, j_profile, tau) @ g_inv_sqrt
    values, vectors = np.linalg.eigh(z.conj().T @ z)
    idx = np.argsort(values)
    vectors = vectors[:, idx]
    return [np.outer(vectors[:, i], vectors[:, i].conj()) for i in range(3)]


def projected_traces(projectors: list[np.ndarray], matrix: np.ndarray) -> np.ndarray:
    return np.array([float(np.real_if_close(np.trace(p @ matrix))) for p in projectors], dtype=float)


def best_affine_fit(values: np.ndarray, target: np.ndarray) -> tuple[float, float, float]:
    design = np.column_stack([values[:2], np.ones(2)])
    scale, offset = np.linalg.lstsq(design, target, rcond=None)[0]
    residual = float(np.linalg.norm(scale * values[:2] + offset - target))
    return float(scale), float(offset), residual


def main() -> None:
    note = read_text(ROOT / "Formal_RouteB_Right_Label_Value_Import_v1.md")
    formal = load_json(FORMAL_ROWS)
    routing = load_json(ROUTING)
    payload = load_json(PAYLOAD)

    primitive_rows = formal["primitive_kernel_values"]
    u_phase = row_matrix(primitive_rows, "u", "phase")
    d_shift = row_matrix(primitive_rows, "d", "shift")
    pu = right_projectors(8.0, 1)
    pd = right_projectors(2.0, 2)

    u_traces = projected_traces(pu, u_phase)
    d_traces = projected_traces(pd, d_shift)
    u_scale, u_offset, u_residual = best_affine_fit(u_traces, np.array([-1.0, 1.0]))
    dyad_scale, dyad_offset, dyad_residual = best_affine_fit(d_traces, np.array([1.0, 0.0]))
    nil_scale, nil_offset, nil_residual = best_affine_fit(d_traces, np.array([0.0, 1.0]))

    routed = routing["static_routing_source_emission"]["retired_sector_routing"]
    physical_promoted = any(bool(row.get("physical_source_promoted")) for row in primitive_rows)
    formal_emitted = all(bool(row.get("independent_formal_quadrature_emitted")) for row in primitive_rows)

    gates = [
        Gate("import note saved", "PASS" if "Formal Route-B Right-Label Value Import" in note else "FAIL", "formal import note present"),
        Gate("formal row packet", "PASS" if formal.get("schema") == "MTTFormal110RowExecution.v1" else "FAIL", formal.get("status", "missing")),
        Gate("row counts", "PASS" if formal.get("row_counts", {}).get("total_rows") == 110 else "FAIL", str(formal.get("row_counts"))),
        Gate("selected route", "PASS" if routed.get("phase_route") == ["u", "e"] and routed.get("shift_route") == ["d", "nuD"] else "FAIL", "Z->u,e and X->d,nuD"),
        Gate("formal quadrature rows", "PASS" if formal_emitted else "FAIL", "all primitive rows have independent_formal_quadrature_emitted=true"),
        Gate("physical source promotion", "OPEN" if not physical_promoted else "PASS", "formal rows are not yet physical-source promoted"),
        Gate("u:phase affine label", "FORMAL-PASS" if u_residual < TOL else "FAIL", f"scale={u_scale:+.12g}, offset={u_offset:+.12g}, residual={u_residual:.3e}"),
        Gate("d:shift dyad label", "FORMAL-PASS" if dyad_residual < TOL else "FAIL", f"scale={dyad_scale:+.12g}, offset={dyad_offset:+.12g}, residual={dyad_residual:.3e}"),
        Gate("d:shift nil label", "FORMAL-PASS" if nil_residual < TOL else "FAIL", f"scale={nil_scale:+.12g}, offset={nil_offset:+.12g}, residual={nil_residual:.3e}"),
        Gate("payload saved", "PASS" if payload.get("status") == "FORMAL_ROUTE_B_ROWS_EXECUTED_PHYSICAL_PROMOTION_OPEN" else "FAIL", str(PAYLOAD)),
        Gate("strict source closure", "OPEN", "needs finite trace quadrature = physical Phi_fin^C1 action theorem"),
    ]

    print("Formal Route-B right-label value import check")
    print("=============================================")
    print()
    print(f"u:phase eig={tuple(float(x) for x in np.linalg.eigvalsh(u_phase))}")
    print(f"u:phase projected traces={tuple(float(x) for x in u_traces)}")
    print(f"d:shift eig={tuple(float(x) for x in np.linalg.eigvalsh(d_shift))}")
    print(f"d:shift projected traces={tuple(float(x) for x in d_traces)}")
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
