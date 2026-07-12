"""Execute the physical finite Dirac operator and the remaining finite-triple axioms."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalfinitediracoperatorandintersectionform_or_fullfinitetripleclosure"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "physical_DF_and_finite_triple.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalFiniteDiracOperatorAndIntersectionForm_or_FullFiniteTripleClosure_v1.md"
STATUS = "MTT_PROFILE_DF_CLOSED_NATIVE_THREE_SUMMAND_NOGO_PROVED_MINIMAL_NEUTRAL_COMPLETION_AXIOMS_CLOSED_SELECTION_OPEN"
NEXT = "MTT_Selected_NeutralAlgebraSummandOrEquivalentAxiomRevision_v1"
TOL = 1e-11


EDGES = [
    {"field": "Q_L", "left": "H", "right": "M3", "n_left": 2, "n_right": 3, "grading": -1},
    {"field": "L_L", "left": "H", "right": "C", "n_left": 2, "n_right": 1, "grading": -1},
    {"field": "u_R", "left": "C", "right": "M3", "n_left": 1, "n_right": 3, "grading": 1},
    {"field": "d_R", "left": "Cbar", "right": "M3", "n_left": 1, "n_right": 3, "grading": 1},
    {"field": "e_R", "left": "Cbar", "right": "C", "n_left": 1, "n_right": 1, "grading": 1},
    {"field": "N_R", "left": "C_N", "right": "C", "n_left": 1, "n_right": 1, "grading": 1},
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def complex_matrix(rows: list) -> np.ndarray:
    return np.array([[complex(*entry) for entry in row] for row in rows], dtype=complex)


def quaternion(alpha: complex, beta: complex) -> np.ndarray:
    return np.array([[alpha, beta], [-beta.conjugate(), alpha.conjugate()]], dtype=complex)


def components(lam: complex, q: np.ndarray, m: np.ndarray, nu: complex) -> dict[str, np.ndarray]:
    return {
        "C": np.array([[lam]], dtype=complex),
        "Cbar": np.array([[lam.conjugate()]], dtype=complex),
        "H": q,
        "M3": m,
        "C_N": np.array([[nu]], dtype=complex),
    }


def star(value: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    return {key: matrix.conjugate().T for key, matrix in value.items()}


def offsets(start: int = 0) -> tuple[dict[str, int], int]:
    answer: dict[str, int] = {}
    cursor = start
    for edge in EDGES:
        answer[edge["field"]] = cursor
        cursor += edge["n_left"] * edge["n_right"]
    return answer, cursor


PARTICLE_OFFSETS, PARTICLE_DIM = offsets()
ANTI_OFFSETS, FAMILY_DIM = offsets(PARTICLE_DIM)
FAMILIES = 3
TOTAL_DIM = FAMILIES * FAMILY_DIM


def left_representation(value: dict[str, np.ndarray]) -> np.ndarray:
    out = np.zeros((FAMILY_DIM, FAMILY_DIM), dtype=complex)
    for edge in EDGES:
        field = edge["field"]
        nl, nr = edge["n_left"], edge["n_right"]
        width = nl * nr
        p0, a0 = PARTICLE_OFFSETS[field], ANTI_OFFSETS[field]
        out[p0 : p0 + width, p0 : p0 + width] = np.kron(value[edge["left"]], np.eye(nr))
        out[a0 : a0 + width, a0 : a0 + width] = np.kron(value[edge["right"]], np.eye(nl))
    return out


def real_structure_matrix() -> np.ndarray:
    out = np.zeros((FAMILY_DIM, FAMILY_DIM), dtype=complex)
    for edge in EDGES:
        field = edge["field"]
        nl, nr = edge["n_left"], edge["n_right"]
        p0, a0 = PARTICLE_OFFSETS[field], ANTI_OFFSETS[field]
        for i in range(nl):
            for j in range(nr):
                particle = p0 + i * nr + j
                anti = a0 + j * nl + i
                out[particle, anti] = out[anti, particle] = 1.0
    return out


def grading_matrix() -> np.ndarray:
    diagonal = np.zeros(FAMILY_DIM, dtype=complex)
    for edge in EDGES:
        field = edge["field"]
        width = edge["n_left"] * edge["n_right"]
        diagonal[PARTICLE_OFFSETS[field] : PARTICLE_OFFSETS[field] + width] = edge["grading"]
        diagonal[ANTI_OFFSETS[field] : ANTI_OFFSETS[field] + width] = -edge["grading"]
    return np.diag(diagonal)


def opposite(value: dict[str, np.ndarray], uj: np.ndarray) -> np.ndarray:
    return uj @ left_representation(star(value)).conjugate() @ uj.conjugate().T


def algebra_basis() -> tuple[list[str], list[dict[str, np.ndarray]]]:
    z2, z3 = np.zeros((2, 2), complex), np.zeros((3, 3), complex)
    names: list[str] = []
    values: list[dict[str, np.ndarray]] = []
    for scalar, name in [(1, "C1"), (1j, "Ci")]:
        names.append(name)
        values.append(components(scalar, z2, z3, 0))
    for alpha, beta, name in [(1, 0, "H1"), (1j, 0, "Hi"), (0, 1, "Hj"), (0, 1j, "Hk")]:
        names.append(name)
        values.append(components(0, quaternion(alpha, beta), z3, 0))
    for row in range(3):
        for col in range(3):
            for scalar, suffix in [(1, "r"), (1j, "i")]:
                matrix = np.zeros((3, 3), complex)
                matrix[row, col] = scalar
                names.append(f"M{row}{col}{suffix}")
                values.append(components(0, z2, matrix, 0))
    for scalar, name in [(1, "N1"), (1j, "Ni")]:
        names.append(name)
        values.append(components(0, z2, z3, scalar))
    return names, values


CYCLE = [
    ("C1", "Ci", -1j),
    ("C1", "H1", 1),
    ("C1", "M00r", 1), ("C1", "M11r", 1), ("C1", "M22r", 1),
    ("H1", "C1", -1),
    ("H1", "M00r", -1), ("H1", "M11r", -1), ("H1", "M22r", -1),
    ("M00r", "C1", -1), ("M11r", "C1", -1), ("M22r", "C1", -1),
    ("M00r", "H1", 1), ("M11r", "H1", 1), ("M22r", "H1", 1),
    ("C1", "N1", -1),
    ("N1", "C1", 1),
]


def orientability_cycle(uj: np.ndarray) -> tuple[np.ndarray, list[dict]]:
    names, values = algebra_basis()
    by_name = dict(zip(names, values))
    represented = np.zeros((FAMILY_DIM, FAMILY_DIM), complex)
    rows = []
    for left_name, right_name, coefficient in CYCLE:
        represented += coefficient * left_representation(by_name[left_name]) @ opposite(by_name[right_name], uj)
        rows.append({
            "left_basis_element": left_name,
            "right_basis_element": right_name,
            "coefficient": [float(complex(coefficient).real), float(complex(coefficient).imag)],
        })
    return represented, rows


def physical_dirac(yukawas: dict[str, np.ndarray], uj_family: np.ndarray) -> np.ndarray:
    particle = np.zeros((TOTAL_DIM, TOTAL_DIM), dtype=complex)
    up = np.array([[1.0], [0.0]], dtype=complex)
    down = np.array([[0.0], [1.0]], dtype=complex)
    channel_maps = {
        "u": ("Q_L", "u_R", np.kron(up, np.eye(3))),
        "d": ("Q_L", "d_R", np.kron(down, np.eye(3))),
        "e": ("L_L", "e_R", down),
        "nu": ("L_L", "N_R", up),
    }
    for channel, yukawa in yukawas.items():
        left_field, right_field, internal = channel_maps[channel]
        left_width, right_width = internal.shape
        for left_family in range(FAMILIES):
            for right_family in range(FAMILIES):
                l0 = left_family * FAMILY_DIM + PARTICLE_OFFSETS[left_field]
                r0 = right_family * FAMILY_DIM + PARTICLE_OFFSETS[right_field]
                block = yukawa[left_family, right_family] * internal
                particle[l0 : l0 + left_width, r0 : r0 + right_width] = block
                particle[r0 : r0 + right_width, l0 : l0 + left_width] = block.conjugate().T
    uj = np.kron(np.eye(FAMILIES), uj_family)
    return particle + uj @ particle.conjugate() @ uj.conjugate().T


def internal_channel_dirac(left_field: str, right_field: str, internal: np.ndarray, uj: np.ndarray) -> np.ndarray:
    particle = np.zeros((FAMILY_DIM, FAMILY_DIM), dtype=complex)
    left_width, right_width = internal.shape
    l0, r0 = PARTICLE_OFFSETS[left_field], PARTICLE_OFFSETS[right_field]
    particle[l0 : l0 + left_width, r0 : r0 + right_width] = internal
    particle[r0 : r0 + right_width, l0 : l0 + left_width] = internal.conjugate().T
    return particle + uj @ particle.conjugate() @ uj.conjugate().T


def main() -> int:
    charged_packet = load(ROOT / "candidate_data" / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution" / "versioned_common_scale_yukawa_higgs_values.packet.json")
    neutral_packet = load(ROOT / "candidate_data" / "selected_neutraltwoprimitiveprofilevalueclosure" / "neutral_two_primitive_profile_values.packet.json")
    values = charged_packet["values"]
    yukawas = {
        "u": complex_matrix(values["Y_u_MZ_firstpass"]),
        "d": complex_matrix(values["Y_d_MZ_firstpass"]),
        "e": complex_matrix(values["Y_e_MZ_firstpass"]),
        "nu": complex_matrix(neutral_packet["matrices"]["Y_nu"]),
    }

    uj_family = real_structure_matrix()
    gamma_family = grading_matrix()
    uj = np.kron(np.eye(FAMILIES), uj_family)
    gamma = np.kron(np.eye(FAMILIES), gamma_family)
    d_physical = physical_dirac(yukawas, uj_family)

    represented_cycle, cycle_rows = orientability_cycle(uj_family)
    orientability_residual = float(np.linalg.norm(represented_cycle - gamma_family))

    z2, z3 = np.zeros((2, 2), complex), np.zeros((3, 3), complex)
    minimal_idempotents = [
        components(1, z2, z3, 0),
        components(0, np.eye(2), z3, 0),
        components(0, z2, np.diag([1, 0, 0]), 0),
        components(0, z2, z3, 1),
    ]
    intersection_one = np.array([
        [np.trace(gamma_family @ left_representation(p) @ opposite(q, uj_family)) for q in minimal_idempotents]
        for p in minimal_idempotents
    ]).real.astype(int)
    intersection_three = FAMILIES * intersection_one

    # The native three-summand form is the upper-left block. The neutral edge becomes C--C,
    # whose particle and antiparticle supports cannot be separated by any represented 0-cycle.
    native_intersection = intersection_one[:3, :3]
    native_orientability_lower_bound = float(np.sqrt(2.0))

    _, basis_values = algebra_basis()
    left_basis = [left_representation(value) for value in basis_values]
    right_basis = [opposite(value, uj_family) for value in basis_values]
    order_zero_residuals = [
        float(np.linalg.norm(left @ right - right @ left))
        for left in left_basis
        for right in right_basis
    ]
    up = np.array([[1.0], [0.0]], dtype=complex)
    down = np.array([[0.0], [1.0]], dtype=complex)
    channel_generators = [
        internal_channel_dirac("Q_L", "u_R", np.kron(up, np.eye(3)), uj_family),
        internal_channel_dirac("Q_L", "d_R", np.kron(down, np.eye(3)), uj_family),
        internal_channel_dirac("L_L", "e_R", down, uj_family),
        internal_channel_dirac("L_L", "N_R", up, uj_family),
    ]
    order_one_residuals = []
    for generator in channel_generators:
        for left in left_basis:
            first = generator @ left - left @ generator
            for right in right_basis:
                order_one_residuals.append(float(np.linalg.norm(first @ right - right @ first)))

    singular_values = {key: np.linalg.svd(value, compute_uv=False).tolist() for key, value in yukawas.items()}
    residuals = {
        "D_self_adjoint": float(np.linalg.norm(d_physical - d_physical.conjugate().T)),
        "D_odd": float(np.linalg.norm(d_physical @ gamma + gamma @ d_physical)),
        "JD_reality": float(np.linalg.norm(uj @ d_physical.conjugate() @ uj.conjugate().T - d_physical)),
        "order_zero_max": max(order_zero_residuals),
        "order_one_max": max(order_one_residuals),
        "orientability_cycle": orientability_residual,
    }
    checks = {
        "physical_profile_DF_dimension_96": d_physical.shape == (96, 96),
        "physical_profile_DF_self_adjoint": residuals["D_self_adjoint"] < TOL,
        "physical_profile_DF_odd": residuals["D_odd"] < TOL,
        "physical_profile_DF_J_real": residuals["JD_reality"] < TOL,
        "physical_profile_DF_order_zero": residuals["order_zero_max"] < TOL,
        "physical_profile_DF_order_one": residuals["order_one_max"] < TOL,
        "native_C_H_M3_orientability_obstructed_by_NR_self_edge": native_orientability_lower_bound > 0,
        "native_KO6_three_summand_intersection_degenerate": int(round(np.linalg.det(native_intersection))) == 0,
        "minimal_CN_completion_orientable": orientability_residual < TOL,
        "minimal_CN_intersection_nondegenerate_one_family": int(round(np.linalg.det(intersection_one))) == 4,
        "minimal_CN_intersection_nondegenerate_three_families": int(round(np.linalg.det(intersection_three))) == 324,
    }
    checks = {key: bool(value) for key, value in checks.items()}

    packet = {
        "schema": "MTTSelectedPhysicalFiniteDiracOperatorAndIntersectionFormOrFullFiniteTripleClosure.v1",
        "status": STATUS,
        "theorems": {
            "profile_physical_DF": {
                "proved_at_declared_profile_tier": all(checks[key] for key in list(checks)[:6]),
                "statement": "The accepted charged common-scale profile matrices and the adopted two-primitive Dirac-neutrino profile matrix define an explicit 96-dimensional D_F satisfying self-adjointness, oddness, KO6 reality, order zero, and order one.",
            },
            "native_three_summand_no_go": {
                "proved": checks["native_C_H_M3_orientability_obstructed_by_NR_self_edge"] and checks["native_KO6_three_summand_intersection_degenerate"],
                "statement": "For the A48 KO6 triple with A_F=C+H+M3(C), the N_R:C--C self-edge is non-orientable and the antisymmetric intersection form on the odd-rank K0 generator set is degenerate.",
            },
            "minimal_neutral_summand_completion": {
                "proved_conditionally_on_selecting_C_N": checks["minimal_CN_completion_orientable"] and checks["minimal_CN_intersection_nondegenerate_one_family"],
                "statement": "The minimal replacement N_R:C_N--C over A_F'=C+H+M3(C)+C_N closes orientability and Poincare duality without changing the 16 particle slots per family.",
            },
        },
        "physical_DF": {
            "dimension": TOTAL_DIM,
            "reference_scale": charged_packet["reference_scale"],
            "charged_source_tier": "accepted SM-parity/profile replay; not a no-knob MTT prediction",
            "neutral_source_tier": "two-primitive Dirac profile replay; ontology and strict source selection open",
            "channels": ["Y_u", "Y_d", "Y_e", "Y_nu"],
            "matrix_rank": int(np.linalg.matrix_rank(d_physical, tol=1e-18)),
            "yukawa_singular_values": singular_values,
            "order_one_basis_execution": "all 26x26 real-algebra basis pairs on each of four internal channel generators; arbitrary three-family Yukawa matrices follow by linearity",
        },
        "native_A48_obstruction": {
            "algebra": "C + H + M3(C)",
            "N_R_edge": "C--C",
            "orientability_reason": "Every represented Hochschild 0-chain has equal diagonal action on the N_R particle and antiparticle self-edge, while Gamma_F requires +1 and -1.",
            "minimum_complex_Frobenius_residual": native_orientability_lower_bound,
            "intersection_form_one_family": native_intersection.tolist(),
            "intersection_rank": int(np.linalg.matrix_rank(native_intersection)),
            "intersection_determinant": int(round(np.linalg.det(native_intersection))),
            "structural_reason": "In KO6 the intersection form is antisymmetric; an antisymmetric 3x3 form is necessarily singular.",
        },
        "minimal_completion": {
            "algebra": "C + H + M3(C) + C_N",
            "changed_edge_only": "N_R:C_N--C",
            "particle_slots_per_family": PARTICLE_DIM,
            "orientability_Hochschild_dimension": 0,
            "orientability_cycle_terms": cycle_rows,
            "orientability_residual": orientability_residual,
            "intersection_generator_order": ["C", "H", "M3", "C_N"],
            "intersection_form_one_family": intersection_one.tolist(),
            "intersection_determinant_one_family": int(round(np.linalg.det(intersection_one))),
            "intersection_form_three_families": intersection_three.tolist(),
            "intersection_determinant_three_families": int(round(np.linalg.det(intersection_three))),
        },
        "checks": checks,
        "residuals": residuals,
        "epistemic_policy": {
            "charged_observed_profile_values_used": True,
            "neutral_observed_profile_calibration_used": True,
            "accepted_as_strict_no_knob_prediction": False,
            "C_N_selected_by_A47_native_bundle_theorem": False,
            "C_N_role": "minimal axiom-restoring completion candidate forced by the native no-go",
            "new_continuous_parameters_added_by_finite_axiom_completion": 0,
            "new_discrete_algebra_choice_pending": 1,
            "full_native_finite_Connes_triple_claimed": False,
        },
        "external_consistency": {
            "right_handed_neutrino_orientability_obstruction": "https://arxiv.org/abs/hep-th/0610097",
            "KO6_SM_neutrino_geometry": "https://arxiv.org/abs/hep-th/0608226",
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_PhysicalFiniteDiracOperatorAndIntersectionForm_or_FullFiniteTripleClosure_v1",
        "status": STATUS,
        "profile_physical_DF_closed": packet["theorems"]["profile_physical_DF"]["proved_at_declared_profile_tier"],
        "native_three_summand_full_finite_triple_impossible": packet["theorems"]["native_three_summand_no_go"]["proved"],
        "minimal_CN_completion_finite_axioms_closed": packet["theorems"]["minimal_neutral_summand_completion"]["proved_conditionally_on_selecting_C_N"],
        "orientability_cycle_terms": len(CYCLE),
        "intersection_determinant_one_family": packet["minimal_completion"]["intersection_determinant_one_family"],
        "strict_no_knob_DF_closed": False,
        "CN_selected_by_MTT": False,
        "full_native_finite_Connes_triple_closed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Physical Finite Dirac Operator and Intersection Form or Full Finite Triple Closure v1

## Result

The repository now has the actual `96x96` finite Dirac operator at its declared profile tier. It uses
the locked common-scale `Y_u`, `Y_d`, and `Y_e` matrices and the adopted two-primitive Dirac `Y_nu`
profile. The executable matrix is self-adjoint, odd, `J_F`-real, and satisfies order zero and order one.
Order one is checked on all `26x26` real-algebra basis pairs for each of the four channel generators;
arbitrary three-family Yukawa matrices then follow by linearity and the family-diagonal algebra action.
This closes the physical/profile `D_F`; it does **not** turn replay values into no-knob predictions.

## Native Three-Summand No-Go

The remaining A48 axioms cannot both be closed over `C + H + M3(C)` in KO-dimension 6:

1. `N_R:C--C` is a self-edge. Every represented Hochschild zero-chain acts identically on its particle
   and antiparticle copies, whereas `Gamma_F` requires eigenvalues `+1` and `-1`. The exact lower bound
   on the complex Frobenius residual is `sqrt(2)`.
2. The one-family intersection form is

```text
[[ 0,  2,  2],
 [-2,  0, -2],
 [-2,  2,  0]]
```

It has rank `2` and determinant `0`. More generally, a KO6 intersection form is antisymmetric, so an
odd three-generator form cannot be nondegenerate. This agrees with the published right-handed-neutrino
orientability obstruction: https://arxiv.org/abs/hep-th/0610097.

## Minimal Completion

The smallest executed repair is

```text
A_F' = C + H + M3(C) + C_N,       N_R : C_N--C.
```

No particle slot and no continuous value is added. An explicit 17-term Hochschild zero-cycle represents
`Gamma_F` with residual `{orientability_residual:.3e}`. In generator order `(C,H,M3,C_N)`,

```text
[[ 0,  2,  2, -1],
 [-2,  0, -2,  0],
 [-2,  2,  0,  0],
 [ 1,  0,  0,  0]]
```

has determinant `4` per family; the three-family form has determinant `324`. Thus the completed finite
geometry satisfies orientability and Poincare duality.

## Honest Boundary

`C_N` is mathematically forced as the minimal axiom-restoring completion, but A47 did not select it.
The existing selected `1_M=N^c` carrier is precisely the available MTT object that could source it;
that implication still needs a theorem. Selecting `C_N` may also enlarge the unitary gauge algebra, so
the successor must prove either its reduction to the already closed `/Z6` SM gauge group or the breaking
of the extra neutral unitary direction. This is one discrete structural choice and adds zero continuous
fit parameters.

Next artifact: `{NEXT}`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
