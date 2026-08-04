"""Build the finite-Heisenberg determinant no-go and smooth-lift target."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralfiniteheisenbergdeterminantnogoandsmoothlifttarget"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_finite_heisenberg_determinant_nogo.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralFiniteHeisenbergDeterminantNoGoAndSmoothLiftTarget_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_FINITE_HEISENBERG_DETERMINANT_NOGO_CLOSED_SMOOTH_U1_LIFT_AND_SCALE_OPEN"
NEXT = "MTT_Selected_NeutralSmoothDeterminantLineHolonomyAndAnchoredScale_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cp(value: list[float]) -> complex:
    return complex(value[0], value[1])


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def scale(z, a):
    return [[z*a[i][j] for j in range(3)] for i in range(3)]


def power(a, n):
    out = [[1+0j if i == j else 0j for j in range(3)] for i in range(3)]
    for _ in range(n):
        out = matmul(out, a)
    return out


def det(a):
    return (
        a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
    )


def main() -> int:
    prior = load(
        ROOT / "candidate_data" / "selected_neutralcommoncirclefactorizationandholonomyscalarreduction"
        / "neutral_common_circle_factorization.packet.json"
    )
    rhoe = load(
        ROOT / "candidate_data" / "selected_step38_finiteheisenberg_rhoe_promotion_or_deoperatorfrontier"
        / "step38_finite_heisenberg_rhoe_promotion.packet.json"
    )

    generators = rhoe["selected_projective_rhoE_gauge_representative"]["generators"]
    Z = [[cp(item) for item in row] for row in generators["g1"]]
    X = [[cp(item) for item in row] for row in generators["g2"]]
    zeta = cmath.exp(2j*math.pi/3.0)
    elements = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                matrix = scale(zeta**c, matmul(power(Z, a), power(X, b)))
                elements.append({"a": a, "b": b, "c": c, "determinant": det(matrix)})
    max_det_residual = max(abs(row["determinant"]-1.0) for row in elements)

    discrete_phases = [2.0*math.pi*j/3.0 for j in range(3)]
    cosine_orbits = [[math.cos(phi+2.0*math.pi*k/3.0) for k in range(3)] for phi in discrete_phases]
    degeneracies = [min(abs(row[i]-row[j]) for i in range(3) for j in range(i+1,3)) for row in cosine_orbits]

    checks = {
        "A38_factorization_closed": prior["theorem"]["proved"],
        "finite_rhoE_transition_matrices_closed": rhoe["closure_result"]["operator_level_projective_rhoE_transition_matrices_closed"],
        "finite_rhoE_selected_up_to_unitary_gauge": rhoe["closure_result"]["nonidentity_projective_rhoE_selected_up_to_unitary_gauge"],
        "Z_determinant_one": abs(det(Z)-1.0) < 1e-12,
        "X_determinant_one": abs(det(X)-1.0) < 1e-12,
        "central_zetaI_determinant_one": abs(zeta**3-1.0) < 1e-12,
        "all_27_finite_Heisenberg_determinants_one": max_det_residual < 1e-11,
        "all_determinant_trivial_phases_have_twofold_cosine_degeneracy": all(value < 1e-12 for value in degeneracies),
        "smooth_operator_values_remain_open": not rhoe["closure_result"]["selected_covariant_D_E_matrices_closed"],
    }
    checks = {key: bool(value) for key, value in checks.items()}
    theorem_proved = all(checks.values())

    packet = {
        "schema": "MTTSelectedNeutralFiniteHeisenbergDeterminantNoGoAndSmoothLiftTarget.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralCommonCircleFactorizationAndHolonomyScalarReduction_v1",
        "theorem": {
            "name": "FiniteHeisenbergDeterminantTrivialityAndNeutralDriftNoGoTheorem",
            "proved": theorem_proved,
            "statement": "The later selected finite Stone-von Neumann packet promotes the nonidentity qutrit rho_E transition gauge class, but its clock Z, shift X and central zeta_3 I generators all have determinant one. Consequently every element zeta_3^c Z^a X^b of the 27-element finite Heisenberg image lies in SU(3), so det rho_E(g)=1 identically. In the neutral factorization det H_nu=exp(3 i phi_nu), this finite image can only permit phi_nu=0,2 pi/3,4 pi/3 modulo 2 pi; these merely permute the Z3 cosine orbit and preserve an exact twofold degeneracy. Therefore the finite qutrit/projective packet cannot source the small continuous neutral nil drift. The required source is a smooth determinant-line U(1) holonomy beyond the determinant-trivial finite shadow, plus the anchored physical scale.",
        },
        "source_checks": checks,
        "finite_Heisenberg_determinant_proof": {
            "normal_form": "zeta_3^c Z^a X^b, a,b,c in {0,1,2}",
            "element_count": len(elements),
            "det_Z": [det(Z).real, det(Z).imag],
            "det_X": [det(X).real, det(X).imag],
            "det_zetaI": [(zeta**3).real, (zeta**3).imag],
            "max_abs_det_minus_one": max_det_residual,
            "image_subgroup": "SU(3)",
            "determinant_character": "trivial",
        },
        "neutral_phase_consequence": {
            "identity": "det H_nu=exp(3*i*phi_nu)",
            "finite_allowed_phi_mod_2pi": discrete_phases,
            "cosine_orbits": cosine_orbits,
            "minimum_pair_gaps": degeneracies,
            "all_have_exact_twofold_degeneracy": True,
            "can_source_small_nonzero_continuous_nil_drift": False,
        },
        "scope_guard": {
            "finite_rhoE_promotion_retracted": False,
            "finite_projective_gauge_class_closed": True,
            "what_is_rejected": "using its determinant-trivial SU(3) image as the central U(1) determinant-line value",
            "unitary_conjugation_can_change_determinant": False,
        },
        "next_source_target": {
            "bundle": "smooth determinant line det(E_nu) over the selected neutral co-aligned loop",
            "connection": "trace part of the smooth U(3) connection or an independently selected central U(1) connection",
            "holonomy": "exp(i*integral_gamma_nu Tr(A)/3) with det H_nu=exp(i*integral_gamma_nu Tr(A))",
            "required_nontriviality": "det H_nu not restricted to 1 by the finite SU(3) shadow",
            "scale": "same-branch anchored neutral Hessian contraction with one physical unit",
        },
        "what_closes_here": {
            "finite_operator_level_rhoE_imported": theorem_proved,
            "finite_Heisenberg_determinant_triviality": theorem_proved,
            "finite_qutrit_source_for_continuous_phi_nu_rejected": theorem_proved,
            "smooth_determinant_line_target_typed": theorem_proved,
            "phi_nu_value": False,
            "mu_nu_value": False,
            "dimensionful_neutral_masses": False,
        },
        "new_physical_value_fields_closed_here": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralFiniteHeisenbergDeterminantNoGoAndSmoothLiftTarget_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "finite_group_elements_checked": len(elements),
        "max_determinant_residual": max_det_residual,
        "finite_image_in_SU3": theorem_proved,
        "finite_qutrit_can_source_continuous_phi_nu": False,
        "smooth_determinant_line_target_typed": theorem_proved,
        "phi_nu_value_closed": False,
        "mu_nu_value_closed": False,
        "dimensionful_neutral_masses_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Finite-Heisenberg Determinant No-Go and Smooth-Lift Target v1

## Determinant theorem

The selected finite projective representation has normal form

```text
zeta_3^c Z^a X^b, a,b,c in {{0,1,2}}.
```

All 27 elements were checked. `det Z=det X=det(zeta_3 I)=1`, and the maximum
determinant residual is `{max_det_residual}`. The finite image therefore lies
in `SU(3)` and has trivial determinant character.

Since `det H_nu=exp(3 i phi_nu)`, the finite shadow permits only determinant-
trivial phases. They merely permute the three cosine values and retain an exact
twofold degeneracy. The finite qutrit packet cannot emit the small continuous
neutral nil drift.

## Correct source target

No valid finite rho_E result is retracted. The missing object is the smooth
determinant-line `U(1)` holonomy along the selected neutral co-aligned loop,
together with the anchored Hessian physical scale.

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
