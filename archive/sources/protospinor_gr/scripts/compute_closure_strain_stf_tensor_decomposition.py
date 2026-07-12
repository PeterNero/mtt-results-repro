from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LENS_TO_STF_CERT = ROOT / "certificates" / "lens_to_stf_source_identification_attempt_certificate.json"
OUT_CERT = ROOT / "certificates" / "closure_strain_stf_tensor_decomposition_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rank(matrix: list[list[Fraction]]) -> int:
    rows = [row[:] for row in matrix]
    m = len(rows)
    n = len(rows[0]) if rows else 0
    r = 0
    for c in range(n):
        pivot = None
        for i in range(r, m):
            if rows[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        p = rows[r][c]
        rows[r] = [x / p for x in rows[r]]
        for i in range(m):
            if i != r and rows[i][c] != 0:
                factor = rows[i][c]
                rows[i] = [rows[i][j] - factor * rows[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def mat_vec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum(row[i] * vector[i] for i in range(len(vector))) for row in matrix]


def zero_vector(size: int) -> list[Fraction]:
    return [Fraction(0) for _ in range(size)]


def main() -> None:
    upstream = load_json(LENS_TO_STF_CERT)

    # General local bookkeeping/closure strain as a 3x3 linear map d_i s_j.
    # Basis: xx, xy, xz, yx, yy, yz, zx, zy, zz.
    basis9 = ["xx", "xy", "xz", "yx", "yy", "yz", "zx", "zy", "zz"]

    antisymmetric_generators = {
        "rot_xy": [0, 1, 0, -1, 0, 0, 0, 0, 0],
        "rot_xz": [0, 0, 1, 0, 0, 0, -1, 0, 0],
        "rot_yz": [0, 0, 0, 0, 0, 1, 0, -1, 0],
    }
    trace_generator = {"radial_trace": [1, 0, 0, 0, 1, 0, 0, 0, 1]}
    stf_generators = {
        "stf_plus": [1, 0, 0, 0, -1, 0, 0, 0, 0],
        "stf_longitudinal": [1, 0, 0, 0, 1, 0, 0, 0, -2],
        "stf_xy": [0, 1, 0, 1, 0, 0, 0, 0, 0],
        "stf_xz": [0, 0, 1, 0, 0, 0, 1, 0, 0],
        "stf_yz": [0, 0, 0, 0, 0, 1, 0, 1, 0],
    }

    all_generators = {
        **antisymmetric_generators,
        **trace_generator,
        **stf_generators,
    }
    generator_matrix = [[Fraction(x) for x in row] for row in all_generators.values()]

    full_rank = rank(generator_matrix)
    decomposition_closed = full_rank == 9

    symmetric_projection_constraints = [
        # E_xy - E_yx = 0, E_xz - E_zx = 0, E_yz - E_zy = 0.
        [0, 1, 0, -1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, -1, 0],
    ]
    trace_free_constraint = [[1, 0, 0, 0, 1, 0, 0, 0, 1]]
    transverse_z_constraints = [
        # For wave covector k along z, transversality k^i E_ij = 0 removes zj.
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    physical_constraints = [
        *symmetric_projection_constraints,
        *trace_free_constraint,
        *transverse_z_constraints,
    ]
    constraint_rank = rank([[Fraction(x) for x in row] for row in physical_constraints])
    physical_dimension = 9 - constraint_rank

    plus = [Fraction(x) for x in stf_generators["stf_plus"]]
    cross = [Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
    plus_satisfies = mat_vec([[Fraction(x) for x in row] for row in physical_constraints], plus) == zero_vector(
        len(physical_constraints)
    )
    cross_satisfies = mat_vec([[Fraction(x) for x in row] for row in physical_constraints], cross) == zero_vector(
        len(physical_constraints)
    )
    plus_cross_independent = rank([plus, cross]) == 2
    tt_basis_closed = physical_dimension == 2 and plus_satisfies and cross_satisfies and plus_cross_independent

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "closure_strain_stf_tensor_decomposition",
        "status": "CLOSURE_STRAIN_STF_TENSOR_DECOMPOSITION_CLOSED_SELECTED_HESSIAN_OPEN",
        "input_certificate": {
            "lens_to_stf_status": upstream["status"],
            "lens_to_stf_closed": upstream["source_tests"]["direct_lens_to_stf_closed"],
            "preferred_forward_route": upstream["interpretation"]["preferred_forward_route"],
        },
        "strain_basis": basis9,
        "decomposition": {
            "antisymmetric_gauge_rotation_generators": antisymmetric_generators,
            "scalar_radial_trace_generator": trace_generator,
            "symmetric_trace_free_generators": stf_generators,
            "full_decomposition_rank": full_rank,
            "ambient_dimension": 9,
            "decomposition_closed": decomposition_closed,
        },
        "tt_reduction": {
            "constraints": {
                "symmetry": symmetric_projection_constraints,
                "trace_free": trace_free_constraint,
                "transverse_to_z": transverse_z_constraints,
            },
            "constraint_rank": constraint_rank,
            "physical_dimension": physical_dimension,
            "plus_vector": [str(x) for x in plus],
            "cross_vector": [str(x) for x in cross],
            "plus_satisfies_constraints": plus_satisfies,
            "cross_satisfies_constraints": cross_satisfies,
            "plus_cross_independent": plus_cross_independent,
            "tt_basis_closed": tt_basis_closed,
        },
        "interpretation": {
            "closed": (
                "If bookkeeping/closure strain is represented as a local 3x3 strain tensor, "
                "ordinary linear algebra decomposes it into gauge rotations, scalar trace, "
                "and five STF tensor directions; transversality leaves the two TT modes."
            ),
            "not_closed": (
                "This does not yet prove that MTT selects this strain tensor as the GR source, "
                "nor does it compute the selected Hessian eigenvalues or Newton normalization."
            ),
            "next_gate": "selected_closure_strain_hessian_on_stf_tensor_sector",
        },
        "guardrails": {
            "claims_selected_MTT_Hessian": False,
            "claims_Newton_normalization": False,
            "claims_full_GR_closed": False,
            "claims_tensor_decomposition_closed": True,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
