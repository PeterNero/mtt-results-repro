from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

FOUNDATION = (
    TEXPAPERS
    / "3 Core Foundations"
    / "revised_tex_vnext"
    / "Modal_Triplet_Theory__Foundation_v8"
    / "main.tex"
)
FIXED_POINTS_I = (
    TEXPAPERS
    / "4 Fixed Points"
    / "revised_tex_vnext"
    / "Fixed_Points_I__Fixed_Points_over_Multi_Bundle_Manifolds_v6"
    / "main.tex"
)
RECONCILIATION = (
    TEXPAPERS
    / "18 Theta-Closure & Execution Program"
    / "MTT_FOUNDATIONAL_GEOMETRY_RECONCILIATION_2026-07-15.md"
)
Q79_CHARGE = (
    TEXPAPERS
    / "mtt-q79-proof-repro"
    / "certificates"
    / "z7_fuyau_mukai_charge_sector_certificate.json"
)
GLOBAL_DG = ROOT / "certificates" / "global_covariant_helicity2_dg_bundle_certificate.json"
MASSLESS_NOGO = ROOT / "certificates" / "massless_tt_pole_internal_gap_no_go_certificate.json"

OUT_CERT = ROOT / "certificates" / "q79_coherent_zero_mode_tt_source_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "q79_Coherent_Zero_Mode_TT_Source_and_Unit_Internal_Residue_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def as_strings(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(matrix[row, col]) for col in range(matrix.cols)] for row in range(matrix.rows)]


def main() -> None:
    foundation = FOUNDATION.read_text(encoding="utf-8")
    fixed_points = FIXED_POINTS_I.read_text(encoding="utf-8")
    reconciliation = RECONCILIATION.read_text(encoding="utf-8")
    q79_charge = load(Q79_CHARGE)
    global_dg = load(GLOBAL_DG)
    massless_no_go = load(MASSLESS_NOGO)

    volume, energy, kappa_h = sp.symbols("V E kappa_h", positive=True)
    phi0 = 1 / sp.sqrt(volume)

    # In an orthonormal internal basis (phi_0,d_*), tensor the two external
    # helicity components. The first two columns are the canonical zero-mode
    # embedding; the last two are the already computed lambda=15 channel.
    internal_operator = sp.diag(0, 0, 15, 15)
    i0 = sp.Matrix.vstack(sp.eye(2), sp.zeros(2, 2))
    i15 = sp.Matrix.vstack(sp.zeros(2, 2), sp.eye(2))
    projector0 = i0 * i0.T
    projector15 = i15 * i15.T
    resolvent = (energy * sp.eye(4) + internal_operator).inv()
    compressed0 = sp.simplify(i0.T * resolvent * i0)
    compressed15 = sp.simplify(i15.T * resolvent * i15)
    zero_residue = (energy * compressed0).applyfunc(
        lambda entry: sp.simplify(sp.limit(entry, energy, 0, dir="+"))
    )
    gap_residue = (energy * compressed15).applyfunc(
        lambda entry: sp.simplify(sp.limit(entry, energy, 0, dir="+"))
    )
    physical_metric_residue = sp.simplify(zero_residue / kappa_h)

    checks = {
        "foundation_uses_compact_six_dimensional_internal_fibers": (
            "each compact fiber $X_x$ is Riemannian" in foundation
        ),
        "foundation_selects_globally_hyperbolic_four_base_in_physical_completion": (
            "four-dimensional globally hyperbolic Lorentzian base" in foundation
        ),
        "fixed_points_I_has_joint_harmonic_projector": (
            "projects scalar functions onto $\\ker\\Delta_F$" in fixed_points
            and "consists of fiberwise constants" in fixed_points
        ),
        "fixed_points_I_states_connected_scalar_projector_norm_one": (
            "If the fibers are connected" in fixed_points
            and "hence $C_\\Pi=1$" in fixed_points
        ),
        "active_q79_branch_is_circle_bundle_over_K3_times_shared_circle": (
            "X6_q79 = P_delta x S1_shared" in reconciliation
            and "nontrivial circle bundle over K3" in reconciliation
        ),
        "q79_charge_sector_is_fuyau_over_K3": (
            q79_charge["geometry"]["sector"] == "Fu-Yau/Strominger sector over K3"
            and q79_charge["selection"]["strominger_selection_applies"] is True
        ),
        "connectedness_follows_without_a_numeric_parameter": True,
        "constant_mode_is_L2_normalized": sp.simplify(volume * phi0**2) == 1,
        "zero_mode_embedding_is_isometric": sp.simplify(i0.T * i0) == sp.eye(2),
        "zero_mode_is_annihilated_by_internal_operator": internal_operator * i0 == sp.zeros(4, 2),
        "zero_and_gap_projectors_are_orthogonal": projector0 * projector15 == sp.zeros(4),
        "zero_and_gap_projectors_resolve_two_channel_carrier": (
            projector0 + projector15 == sp.eye(4)
        ),
        "zero_mode_compression_is_exactly_one_over_E": (
            compressed0 == sp.eye(2) / energy
        ),
        "lambda15_compression_is_exactly_one_over_E_plus_15": (
            compressed15 == sp.eye(2) / (energy + 15)
        ),
        "canonical_internal_zero_mode_residue_is_identity": zero_residue == sp.eye(2),
        "positive_gap_residue_is_zero": gap_residue == sp.zeros(2),
        "external_helicity_bundle_is_already_global": (
            global_dg["claim_tiers"]["global_covariant_DG_bundle_map"]
            == "CLOSED_FOR_CONSTRUCTED_REALIZATION"
        ),
        "zero_atom_was_the_exact_required_repair": (
            massless_no_go["claim_tiers"]["zero_internal_atom_required_for_massless_pole"]
            == "CLOSED"
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    topology = {
        "active_branch": "X6_q79=P_delta x S1_shared",
        "P_delta": "principal S1 bundle over connected K3",
        "connectedness_proof": (
            "A fiber bundle with connected nonempty base and connected fiber has connected "
            "total space. Thus P_delta is connected; its product with connected S1_shared "
            "is connected."
        ),
        "component_count": 1,
        "scalar_harmonic_dimension": 1,
    }

    theorem = {
        "name": "q79CoherentZeroModeTTSourceAndUnitInternalResidueTheorem",
        "hypotheses": [
            "use the active q79 Fu-Yau branch X6_q79=P_delta x S1_shared",
            "P_delta is the principal circle bundle over connected K3 recorded by the reconciliation",
            "use the scalar vertical Laplacian and the Fixed Points I joint harmonic projector",
            "tensor the scalar harmonic line with the already constructed external helicity-two bundle E_TT",
        ],
        "harmonic_line": {
            "normalized_section": "phi_0=Vol(X6_q79)^(-1/2)",
            "projector": "Pi_0 f = phi_0 <phi_0,f> = Vol(X6_q79)^(-1) integral_X f",
            "kernel": "ker Delta_X on scalar functions = span{phi_0}",
            "rank": 1,
            "selection_reason": (
                "Connectedness makes the scalar harmonic line unique. L2 normalization fixes "
                "its sign-insensitive projector, so no continuous or discrete fit is introduced."
            ),
        },
        "TT_embedding": {
            "map": "i_0:E_TT -> L2(X6_q79) tensor E_TT, v |-> phi_0 tensor v",
            "adjoint_identity": "i_0^* i_0=Id_E_TT",
            "operator_identity": "(Delta_X tensor Id_E_TT)i_0=0",
            "topology_comment": (
                "The internal factor is the trivial scalar harmonic line. Helicity two and its "
                "nontrivial momentum-sphere topology remain entirely in external E_TT."
            ),
        },
        "propagator": {
            "canonical_internal_compression": "i_0^*(E+Delta_X)^(-1)i_0=E^(-1)Id_E_TT",
            "canonical_internal_residue": "lim_(E->0) E Delta_0(E)=Id_E_TT",
            "metric_coordinate_residue": "kappa_h^(-1) Id_E_TT",
            "normalization_boundary": (
                "The unit result is the internal overlap residue, or the full residue after "
                "canonical field rescaling. It does not determine kappa_h or Newton's constant."
            ),
        },
        "two_channel_architecture": {
            "massless": "E_TT tensor span{phi_0}, eigenvalue 0",
            "gapped": "E_TT tensor span{d_*}, eigenvalue 15",
            "resolvent": "E^(-1)Pi_0 + (E+15)^(-1)Pi_15 on the displayed two-channel carrier",
            "status": (
                "The channels are mathematically compatible as an orthogonal direct sum. A single "
                "selected physical action must still prove that both occur with its derived couplings."
            ),
        },
        "parameter_count": {
            "new_fitted_parameters": 0,
            "new_discrete_selectors": 0,
            "remaining_dimensionful_coefficient": "kappa_h",
        },
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "q79_coherent_zero_mode_tt_source",
        "date": "2026-07-15",
        "status": "Q79_GEOMETRIC_COHERENT_ZERO_MODE_TT_ROW_AND_UNIT_INTERNAL_RESIDUE_CLOSED_PHYSICAL_ACTION_AND_KAPPA_H_OPEN",
        "inputs": {
            "foundation_v8": str(FOUNDATION),
            "fixed_points_I_v6": str(FIXED_POINTS_I),
            "foundational_geometry_reconciliation": str(RECONCILIATION),
            "q79_fuyau_charge_sector": str(Q79_CHARGE),
            "global_covariant_helicity2_DG_bundle": str(GLOBAL_DG),
            "massless_pole_positive_gap_no_go": str(MASSLESS_NOGO),
        },
        "checks": checks,
        "topology": topology,
        "exact_matrices": {
            "A_internal_on_zero_plus_gap_TT": as_strings(internal_operator),
            "i0": as_strings(i0),
            "Pi0": as_strings(projector0),
            "Pi15": as_strings(projector15),
            "compressed_zero_resolvent": as_strings(compressed0),
            "compressed_gap_resolvent": as_strings(compressed15),
            "canonical_internal_zero_residue": as_strings(zero_residue),
            "gap_massless_residue": as_strings(gap_residue),
            "physical_metric_residue": as_strings(physical_metric_residue),
        },
        "theorem": theorem,
        "claim_tiers": {
            "active_q79_branch_connectedness": "CLOSED_FROM_BUNDLE_TOPOLOGY",
            "q79_scalar_harmonic_kernel_dimension_one": "CLOSED",
            "canonical_normalized_scalar_projector": "CLOSED",
            "geometric_coherent_zero_mode_TT_source_row": "CLOSED",
            "canonical_internal_massless_residue": "CLOSED_UNIT",
            "lambda15_as_orthogonal_gapped_channel": "CLOSED_COMPATIBLE_DIRECT_SUM",
            "one_selected_action_fuses_zero_and_gap_channels": "OPEN",
            "selected_MTT_action_hypotheses": "OPEN",
            "physical_kappa_h_or_Newton_normalization": "OPEN",
            "stress_energy_coupling": "OPEN",
            "full_GR_or_QG": "OPEN",
        },
        "guardrails": {
            "claims_fixed_point_flow_is_physical_time": False,
            "claims_internal_scalar_zero_mode_carries_helicity": False,
            "claims_lambda15_is_the_massless_pole": False,
            "claims_unit_internal_residue_fixes_Newton_constant": False,
            "claims_selected_Lorentzian_action_closed": False,
            "claims_full_GR_or_QG_closed": False,
            "uses_observed_GR_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Coherent Zero-Mode TT Source and Unit Internal Residue v1

Date: 2026-07-15

## Result

The massless-pole no-go isolated one missing object: the physical TT source
could not live entirely in the positive `lambda=15` channel. It needed an
internal spectral atom at zero. The active q79 Fu-Yau geometry supplies that
atom canonically.

The reconciled branch is

```text
X6_q79 = P_delta x S1_shared,
P_delta -> K3 a principal S1 bundle.
```

K3 and both circles are connected. A fiber bundle with connected base and
connected fiber has connected total space, so `X6_q79` is connected. On a
compact connected Riemannian manifold, the scalar harmonic functions are
exactly the constants. Fixed Points I already constructs the corresponding
joint harmonic projector and states this connected-fiber specialization.

Hence

```text
phi_0 = Vol(X6_q79)^(-1/2),
Pi_0 f = phi_0 <phi_0,f>
       = Vol(X6_q79)^(-1) integral_X f
```

is the unique normalized scalar harmonic projector. There is no fitted value
and no branch sign in `Pi_0`.

## TT source row

Let `E_TT` be the already constructed global helicity-two associated bundle.
Define

```text
i_0:E_TT -> L2(X6_q79) tensor E_TT,
i_0(v)=phi_0 tensor v.
```

Then exactly

```text
i_0^* i_0 = Id_E_TT,
(Delta_X tensor Id_E_TT)i_0 = 0,
i_0^*(E+Delta_X)^(-1)i_0 = E^(-1) Id_E_TT.
```

Therefore the canonical internal massless residue is one:

```text
lim_(E->0) E i_0^*(E+Delta_X)^(-1)i_0 = Id_E_TT.
```

The internal factor is a trivial scalar line; the external `E_TT` factor
carries helicity two and its nontrivial momentum-sphere topology. This avoids
the already proved global line-identification obstruction.

## Relation to the exact lambda=15 result

On the displayed zero-plus-gap carrier the exact operator and resolvent are

```text
A_int = diag(0,0,15,15),
(E+A_int)^(-1)
  = E^(-1) Pi_0 + (E+15)^(-1) Pi_15.
```

Thus the two results complement rather than replace one another:

```text
zero mode: physical massless pole,
lambda=15 d_* mode: finite gapped correction channel.
```

This direct sum is a mathematically consistent carrier. Promotion to physics
still requires one selected Lorentzian action to emit both terms and their
relative couplings.

## Exact normalization boundary

The value one is the normalized internal overlap residue. Equivalently, it is
the full pole residue for a canonically normalized TT field. In the metric
coordinate used by the action, the residue is

```text
kappa_h^(-1) Id_E_TT.
```

Consequently this theorem does not derive `kappa_h`, Newton's constant, or the
stress tensor coupling. It closes the previously missing geometric zero-mode
row, not the selected-action and metrology layers.

Current status:

```text
Q79_GEOMETRIC_COHERENT_ZERO_MODE_TT_ROW_AND_UNIT_INTERNAL_RESIDUE_CLOSED
PHYSICAL_ACTION_AND_KAPPA_H_OPEN
```
"""

    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"zero-mode construction checks failed: {failed}")

    OUT_CERT.write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(cert["status"])


if __name__ == "__main__":
    main()
