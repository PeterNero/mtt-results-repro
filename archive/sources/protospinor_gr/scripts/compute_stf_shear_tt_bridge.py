from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LENS_SEARCH_CERT = ROOT / "certificates" / "lens_shear_projection_source_search_certificate.json"
OUT_CERT = ROOT / "certificates" / "stf_shear_tt_bridge_certificate.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rank(matrix: list[list[float]], tol: float = 1e-12) -> int:
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = None
        for i in range(r, rows):
            if abs(a[i][c]) > tol:
                pivot = i
                break
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(rows):
            if i != r and abs(a[i][c]) > tol:
                factor = a[i][c]
                a[i] = [a[i][j] - factor * a[r][j] for j in range(cols)]
        r += 1
    return r


def matvec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def main() -> None:
    lens_search = load_json(LENS_SEARCH_CERT)

    # Symmetric spatial perturbation basis:
    # [h_xx, h_yy, h_zz, h_xy, h_xz, h_yz].
    spatial_symmetric_components = 6
    constraints = {
        "trace_free": [1.0, 1.0, 1.0, 0.0, 0.0, 0.0],
        "transverse_xz": [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
        "transverse_yz": [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
        "longitudinal_zz": [0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
    }
    constraint_matrix = list(constraints.values())
    constraint_rank = rank(constraint_matrix)
    tt_dimension = spatial_symmetric_components - constraint_rank

    plus = [1.0, -1.0, 0.0, 0.0, 0.0, 0.0]
    cross = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
    plus_satisfies = all(abs(v) < 1e-12 for v in matvec(constraint_matrix, plus))
    cross_satisfies = all(abs(v) < 1e-12 for v in matvec(constraint_matrix, cross))
    plus_cross_independent = rank([plus, cross]) == 2

    bridge_closed = (
        tt_dimension == 2
        and plus_satisfies
        and cross_satisfies
        and plus_cross_independent
    )

    cert = {
        "certificate": "STFShearTTBridgeCertificate",
        "status": "STF_SHEAR_TO_TT_PLUS_CROSS_BRIDGE_CLOSED_LENS_SOURCE_OPEN",
        "purpose": "Prove the mathematical bridge from transverse symmetric trace-free spatial shear to the two TT plus/cross metric response directions.",
        "input_lens_source_search": str(LENS_SEARCH_CERT),
        "spatial_symmetric_basis": [
            "h_xx",
            "h_yy",
            "h_zz",
            "h_xy",
            "h_xz",
            "h_yz",
        ],
        "constraints_for_wavevector_z": constraints,
        "linear_algebra": {
            "spatial_symmetric_components": spatial_symmetric_components,
            "constraint_rank": constraint_rank,
            "tt_dimension": tt_dimension,
            "plus_vector": plus,
            "cross_vector": cross,
            "plus_satisfies_constraints": plus_satisfies,
            "cross_satisfies_constraints": cross_satisfies,
            "plus_cross_independent": plus_cross_independent,
        },
        "bridge_closed": bridge_closed,
        "what_this_closes": "If lens shear is independently identified with transverse symmetric trace-free spatial shear, then the plus/cross TT projection is fixed and two-dimensional.",
        "what_remains_open": "The MTT source identification from lens transport/shear to this STF transverse shear basis.",
        "remaining_blocker": {
            "name": "Lens_to_STF_Source_Identification",
            "blocked_by": lens_search["blocked_claim"]["reason"],
        },
        "guardrails": {
            "claims_lens_selected_as_STF": False,
            "claims_selected_P_GR": False,
            "claims_full_GR_closure": False,
            "uses_observed_GR_data": False,
        },
    }
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(json.dumps({"wrote": str(OUT_CERT), "status": cert["status"]}, indent=2))


if __name__ == "__main__":
    main()

