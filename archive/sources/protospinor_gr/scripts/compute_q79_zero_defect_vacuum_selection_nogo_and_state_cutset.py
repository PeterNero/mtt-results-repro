from __future__ import annotations

import json
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

FLAT_ENDPOINT = (
    ROOT
    / "certificates"
    / "q79_shared_circle_double_return_cln_nil_flat_endpoint_certificate.json"
)
TEGR_BRIDGE = (
    ROOT
    / "certificates"
    / "closure_anholonomy_teleparallel_einstein_bridge_certificate.json"
)
STRICT_SOURCE = (
    ROOT
    / "certificates"
    / "strict_same_source_teleparallel_selection_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_zero_defect_vacuum_selection_nogo_and_state_cutset_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Zero_Defect_Vacuum_Selection_NoGo_and_State_Boundary_Cutset_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_rows(matrix: sp.Matrix) -> list[list[int | str]]:
    rows: list[list[int | str]] = []
    for row in matrix.tolist():
        converted: list[int | str] = []
        for value in row:
            value = sp.simplify(value)
            if value.is_Integer:
                converted.append(int(value))
            elif value.is_Rational:
                converted.append(str(value))
            else:
                converted.append(str(value))
        rows.append(converted)
    return rows


def nonzero_components(tensor: sp.MutableDenseNDimArray) -> list[dict]:
    components: list[dict] = []
    for index in product(*(range(size) for size in tensor.shape)):
        value = sp.simplify(tensor[index])
        if value != 0:
            components.append({"index": list(index), "value": str(value)})
    return components


def main() -> None:
    flat_endpoint = load(FLAT_ENDPOINT)
    tegr_bridge = load(TEGR_BRIDGE)
    strict_source = load(STRICT_SOURCE)

    u, v, x, y = sp.symbols("u v x y", real=True)
    coordinates = (u, v, x, y)
    dimension = len(coordinates)
    profile = x**2 - y**2

    # Brinkmann plus-polarized plane wave:
    # ds^2 = H du^2 - 2 du dv + dx^2 + dy^2.
    metric = sp.Matrix(
        [
            [profile, -1, 0, 0],
            [-1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )
    inverse_metric = sp.simplify(metric.inv())

    christoffel = sp.MutableDenseNDimArray.zeros(dimension, dimension, dimension)
    for rho, mu, nu in product(range(dimension), repeat=3):
        christoffel[rho, mu, nu] = sp.simplify(
            sp.Rational(1, 2)
            * sum(
                inverse_metric[rho, sigma]
                * (
                    sp.diff(metric[sigma, nu], coordinates[mu])
                    + sp.diff(metric[sigma, mu], coordinates[nu])
                    - sp.diff(metric[mu, nu], coordinates[sigma])
                )
                for sigma in range(dimension)
            )
        )

    riemann_mixed = sp.MutableDenseNDimArray.zeros(
        dimension, dimension, dimension, dimension
    )
    for rho, sigma, mu, nu in product(range(dimension), repeat=4):
        riemann_mixed[rho, sigma, mu, nu] = sp.simplify(
            sp.diff(christoffel[rho, nu, sigma], coordinates[mu])
            - sp.diff(christoffel[rho, mu, sigma], coordinates[nu])
            + sum(
                christoffel[rho, mu, lam] * christoffel[lam, nu, sigma]
                - christoffel[rho, nu, lam] * christoffel[lam, mu, sigma]
                for lam in range(dimension)
            )
        )

    riemann_lower = sp.MutableDenseNDimArray.zeros(
        dimension, dimension, dimension, dimension
    )
    for alpha, sigma, mu, nu in product(range(dimension), repeat=4):
        riemann_lower[alpha, sigma, mu, nu] = sp.simplify(
            sum(
                metric[alpha, rho] * riemann_mixed[rho, sigma, mu, nu]
                for rho in range(dimension)
            )
        )

    ricci = sp.zeros(dimension)
    for sigma, nu in product(range(dimension), repeat=2):
        ricci[sigma, nu] = sp.simplify(
            sum(riemann_mixed[rho, sigma, rho, nu] for rho in range(dimension))
        )
    scalar_curvature = sp.simplify(
        sum(
            inverse_metric[mu, nu] * ricci[mu, nu]
            for mu, nu in product(range(dimension), repeat=2)
        )
    )
    einstein = sp.simplify(ricci - sp.Rational(1, 2) * metric * scalar_curvature)

    christoffel_nonzero = nonzero_components(christoffel)
    riemann_nonzero = nonzero_components(riemann_lower)

    # A null coframe for the same metric is ell=du,
    # n=dv-(H/2)du, with g=-2 ell n+dx^2+dy^2.
    # In Weitzenbock gauge d n=-(1/2)dH wedge du is nonzero.
    dprofile_dx = sp.diff(profile, x)
    dprofile_dy = sp.diff(profile, y)
    dn_dx_wedge_du = -sp.Rational(1, 2) * dprofile_dx
    dn_dy_wedge_du = -sp.Rational(1, 2) * dprofile_dy

    state_boundary_contract = {
        "select_global_solution_domain_and_boundary_class": False,
        "exclude_nonflat_Ricci_flat_helicity_two_waves": False,
        "select_zero_defect_initial_or_asymptotic_state": False,
        "derive_zero_effective_cosmological_term": False,
        "prove_QWW_zero_source_is_the_selected_ground_state": False,
    }

    checks = {
        "flat_endpoint_is_available_but_not_dynamically_selected": (
            flat_endpoint["claim_tiers"]["canonical_zero_defect_Minkowski_coframe"]
            == "CLOSED_EXACT"
            and flat_endpoint["claim_tiers"][
                "double_return_dynamically_selects_zero_defect"
            ]
            == "OPEN"
        ),
        "strict_candidate_equations_are_Einstein_at_leading_order": (
            strict_source["claim_tiers"][
                "leading_two_derivative_classical_GR_on_candidate_branch"
            ]
            == "CLOSED_EXACT_UP_TO_KAPPA_LAMBDA_BOUNDARY"
            and tegr_bridge["claim_tiers"][
                "TEGR_bulk_field_equations_equal_Einstein_equations"
            ]
            == "CLOSED_EXACT"
        ),
        "pp_wave_metric_is_non_degenerate_Lorentzian": (
            metric.det() == -1
            and metric[:2, :2].det() == -1
        ),
        "profile_is_transversely_harmonic": (
            sp.diff(profile, x, 2) + sp.diff(profile, y, 2) == 0
        ),
        "pp_wave_Ricci_tensor_vanishes": ricci == sp.zeros(4),
        "pp_wave_scalar_curvature_vanishes": scalar_curvature == 0,
        "pp_wave_Einstein_tensor_vanishes": einstein == sp.zeros(4),
        "pp_wave_Riemann_tensor_is_nonzero": len(riemann_nonzero) > 0,
        "plus_polarized_curvature_components_are_nonzero_and_opposite": (
            riemann_lower[0, 2, 0, 2] == -1
            and riemann_lower[0, 3, 0, 3] == 1
        ),
        "pp_wave_null_coframe_has_nonzero_anholonomy": (
            dn_dx_wedge_du == -x
            and dn_dy_wedge_du == y
            and (dn_dx_wedge_du != 0 or dn_dy_wedge_du != 0)
        ),
        "Lambda_zero_and_zero_stress_do_not_force_flatness": (
            einstein == sp.zeros(4) and len(riemann_nonzero) > 0
        ),
        "double_return_plus_Lambda_zero_do_not_force_flatness": (
            flat_endpoint["claim_tiers"][
                "double_return_alone_forces_zero_metric_strain"
            ]
            == "CLOSED_NO_GO"
            and einstein == sp.zeros(4)
            and len(riemann_nonzero) > 0
        ),
        "state_boundary_cutset_has_no_silent_completed_rows": not any(
            state_boundary_contract.values()
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    certificate = {
        "certificate": "q79_zero_defect_vacuum_selection_nogo_and_state_cutset",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": (
            "EINSTEIN_TEGR_VACUUM_DOES_NOT_SELECT_FLAT_ENDPOINT_CLOSED_NOGO_"
            "STATE_BOUNDARY_OR_POSITIVE_DEFECT_SELECTION_REQUIRED"
        ),
        "inputs": {
            "double_return_and_flat_endpoint": str(FLAT_ENDPOINT),
            "teleparallel_Einstein_bridge": str(TEGR_BRIDGE),
            "strict_same_source_TEGR": str(STRICT_SOURCE),
        },
        "checks": checks,
        "finite_data": {
            "coordinate_order": ["u", "v", "x", "y"],
            "profile_H": "x^2-y^2",
            "metric": matrix_rows(metric),
            "inverse_metric": matrix_rows(inverse_metric),
            "metric_determinant": int(metric.det()),
            "transverse_profile_laplacian": 0,
            "nonzero_Christoffel_components": christoffel_nonzero,
            "nonzero_Riemann_component_count": len(riemann_nonzero),
            "nonzero_Riemann_components": riemann_nonzero,
            "Ricci_tensor": matrix_rows(ricci),
            "Ricci_scalar": int(scalar_curvature),
            "Einstein_tensor": matrix_rows(einstein),
            "representative_plus_curvature": {
                "R_uxux": int(riemann_lower[0, 2, 0, 2]),
                "R_uyuy": int(riemann_lower[0, 3, 0, 3]),
            },
            "null_coframe_anholonomy": {
                "d_n_coefficient_dx_wedge_du": str(dn_dx_wedge_du),
                "d_n_coefficient_dy_wedge_du": str(dn_dy_wedge_du),
            },
            "state_boundary_selection_contract": state_boundary_contract,
            "state_boundary_rows_available": sum(state_boundary_contract.values()),
            "state_boundary_rows_required": len(state_boundary_contract),
            "new_continuous_parameters": 0,
            "new_discrete_parameters": 0,
        },
        "theorem": {
            "name": "VacuumEinsteinTEGRFlatEndpointSelectionNoGo",
            "part_A_counterexample": (
                "The exact Brinkmann metric ds^2=(x^2-y^2)du^2-2du dv+dx^2+dy^2 "
                "has Lorentzian determinant -1, zero Ricci and Einstein tensors, "
                "but nonzero plus-polarized Riemann components R_uxux=-1 and R_uyuy=1."
            ),
            "part_B_action_consequence": (
                "Because the strict candidate leading equations are Einstein and the "
                "TEGR bulk equations are exactly equivalent, zero stress and Lambda_eff=0 "
                "do not select the Minkowski endpoint from the current action class."
            ),
            "part_C_closure_consequence": (
                "The null coframe has nonzero anholonomy dn=-(1/2)dH wedge du, so the "
                "same vacuum equation class contains propagating closure/torsion defect."
            ),
            "part_D_remaining_selector": (
                "Selecting flat spacetime requires independent state or boundary data, "
                "a derived zero-defect ground-state principle, or a stronger positive "
                "defect functional with a proved unique minimizer. It is not another "
                "TEGR constitutive coefficient."
            ),
        },
        "claim_tiers": {
            "exact_curved_Ricci_flat_helicity_two_wave": "CLOSED_CONSTRUCTED",
            "zero_stress_Lambda_zero_Einstein_equations_force_flatness": "CLOSED_NO_GO",
            "zero_stress_Lambda_zero_TEGR_equations_force_zero_torsion": "CLOSED_NO_GO",
            "double_return_plus_Lambda_zero_force_flatness": "CLOSED_NO_GO",
            "Minkowski_zero_defect_endpoint_exists": "CLOSED_EXACT",
            "Minkowski_zero_defect_endpoint_is_unique_vacuum": "CLOSED_NO_GO_WITHOUT_STATE_OR_BOUNDARY_SELECTOR",
            "selected_zero_defect_state_or_boundary_rule": "OPEN_5_ROW_CONTRACT_0_AVAILABLE",
            "selected_positive_defect_ground_state_functional": "OPEN",
            "pregeometric_perfect_closure_selects_physical_Minkowski_state": "OPEN",
        },
        "guardrails": {
            "claims_vacuum_Einstein_equations_imply_zero_curvature": False,
            "claims_vacuum_TEGR_equations_imply_zero_torsion": False,
            "claims_Lambda_eff_zero_selects_Minkowski": False,
            "claims_double_return_excludes_gravitational_waves": False,
            "claims_flat_endpoint_is_selected_without_state_boundary_data": False,
            "uses_observed_physics_data": False,
            "adds_fitted_numeric_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Zero-Defect Vacuum Selection No-Go and State/Boundary Cutset v1

Status:
`EINSTEIN_TEGR_VACUUM_DOES_NOT_SELECT_FLAT_ENDPOINT_CLOSED_NOGO_STATE_BOUNDARY_OR_POSITIVE_DEFECT_SELECTION_REQUIRED`

## Question

The previous theorem proves that the displayed `Q_WW=I` endpoint is exactly
Minkowski and that a zero-stress Minkowski vacuum requires `Lambda_eff=0`.
Could the already selected leading Einstein/TEGR equations then force that
flat endpoint?

No.

## Exact curved vacuum witness

In coordinates `(u,v,x,y)`, take

```text
H=x^2-y^2,
ds^2=H du^2-2 du dv+dx^2+dy^2.
```

The metric determinant is exactly `-1`, so it is nondegenerate and Lorentzian.
The transverse profile is harmonic:

```text
partial_x^2 H+partial_y^2 H=2-2=0.
```

Direct symbolic calculation of the Levi-Civita connection gives

```text
Ricci=0,
R=0,
Einstein=0,
```

while the Riemann tensor is not zero. Representative plus-polarized components
are

```text
R_uxux=-1,
R_uyuy=+1.
```

This is therefore an exact curved, zero-stress, `Lambda_eff=0` solution of the
same Einstein bulk equation class selected at leading order.

## Teleparallel reading

A null coframe is

```text
ell=du,
n=dv-(H/2)du,
g=-2 ell n+dx^2+dy^2.
```

In Weitzenbock gauge,

```text
d n=-(1/2)dH wedge du
   =-x dx wedge du+y dy wedge du,
```

which is nonzero. The exact TEGR/Einstein boundary identity therefore does not
mean that vacuum TEGR sets torsion or closure anholonomy to zero. It means the
bulk field equations are equivalent.

## Consequence

Neither of these implications is valid:

```text
zero stress + Lambda_eff=0 => flat spacetime,
double return + zero stress + Lambda_eff=0 => flat spacetime.
```

The action form is no longer the missing object for this question. Flat-vacuum
selection requires an additional state principle or boundary theorem. A strict
five-row contract is now exposed:

```text
select the global solution domain and boundary class,
exclude nonflat Ricci-flat helicity-two waves when perfect closure is intended,
select zero-defect initial or asymptotic data,
derive Lambda_eff=0,
prove the Q_WW zero source is the selected ground state.
```

No row is supplied by the current corpus. A different valid route would derive
a positive defect functional whose unique physical minimizer is the zero source.
That functional must come from MTT; defining it ad hoc would not be a selection
theorem.

No observed value and no fitted parameter is used.
"""

    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {certificate['status']}")


if __name__ == "__main__":
    main()
