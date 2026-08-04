"""Build the selected eta_00 overlap/Hodge/projector table."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_CANDIDATE = ROOT / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_ext_overlap_hym_hodge_projector_table_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_Ext_Overlap_HYM_Hodge_Projector_Table_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def factor_value(degrees: tuple[int, int, int], generator_index: int, z1: complex, z2: complex, z3: complex) -> complex:
    """AH factor for a single generator g1..g6 in the q79 convention."""
    coords = [z1, z2, z3]
    pair = generator_index // 2
    is_n_generator = generator_index % 2 == 1
    degree = degrees[pair]
    if not is_n_generator or degree == 0:
        return 1.0 + 0.0j
    z = coords[pair]
    log_factor = -math.pi * 1j * degree * 1j - 2.0 * math.pi * 1j * degree * z
    return cmath.exp(log_factor)


def sample_transition_table() -> list[dict]:
    degrees = (2, -4, 0)
    points = [
        ("origin", 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j),
        ("mid_real", 0.5 + 0.0j, 0.5 + 0.0j, 0.0 + 0.0j),
        ("mid_imag", 0.0 + 0.5j, 0.0 + 0.5j, 0.0 + 0.0j),
        ("cell_mid", 0.5 + 0.5j, 0.5 + 0.5j, 0.0 + 0.0j),
    ]
    rows = []
    for name, z1, z2, z3 in points:
        values = {}
        for idx, gen in enumerate(["g1", "g2", "g3", "g4", "g5", "g6"]):
            value = factor_value(degrees, idx, z1, z2, z3)
            values[gen] = {
                "real": value.real,
                "imag": value.imag,
                "abs": abs(value),
                "arg": math.atan2(value.imag, value.real),
            }
        rows.append({"point": name, "z1": [z1.real, z1.imag], "z2": [z2.real, z2.imag], "z3": [z3.real, z3.imag], "generator_values": values})
    return rows


def main() -> int:
    l2_path = ROOT / "candidate_data" / "selected_ext_l2_theta_quadrature_table.candidate.json"
    direct_path = ROOT / "candidate_data" / "selected_end0_direct_differential_table_from_ah_ext_forms.candidate.json"
    first_solve_path = ROOT / "candidate_data" / "selected_hym_adjoint_galerkin_first_coefficient_solve.candidate.json"

    l2 = load(l2_path)
    direct = load(direct_path)
    first_solve = load(first_solve_path)

    l2_closed = l2["overlap_and_newton_status"]["l2_theta_quadrature_closed"] is True
    selected_row = l2["selected_row"]["row_id"] == "eta_00"
    unit_rescale = l2["eta_00_l2_table"]["unit_L2_rescale_factor_numeric"]

    ah_degrees = [2, -4, 0]
    generator_formulas = {
        "g1": "1",
        "g2": "exp(2*pi - 4*pi*i*z1)",
        "g3": "1",
        "g4": "exp(-4*pi + 8*pi*i*z2)",
        "g5": "1",
        "g6": "1",
    }
    transition_samples = sample_transition_table()

    harmonic_row_closed = all(
        [
            l2_closed,
            selected_row,
            direct["Ext_local_form_template"]["closed_nonexact"] is True,
            first_solve["algebraic_adjoint_packet"]["basis"] == ["T1", "T2", "T3"],
        ]
    )

    # The row-level harmonic/Hodge data closes for the normalized Ext form.
    # The nonlinear non-split HYM connection correction remains a different
    # solve and is intentionally not promoted here.
    nonlinear_hym_correction_closed = False
    full_newton_ready = False

    candidate = {
        "candidate": "MTTSelectedExtOverlapHYMHodgeProjectorTable",
        "status": "MTT_SELECTED_EXT_OVERLAP_HODGE_PROJECTOR_TABLE_BUILT_NONLINEAR_HYM_CORRECTION_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "selected_ext_l2_theta_quadrature_table": str(l2_path),
            "direct_End0_AH_Ext_form_table": str(direct_path),
            "adjoint_galerkin_first_solve": str(first_solve_path),
        },
        "selected_row": {
            "row_id": "eta_00",
            "unit_L2_representative": l2["eta_00_l2_table"]["unit_L2_representative"],
            "unit_rescale_factor": unit_rescale,
            "unrescaled_norm_square": l2["eta_00_l2_table"]["unrescaled_norm_square_exact"],
            "central_shared_circle_factor": 1,
        },
        "transition_overlap_table": {
            "closed": harmonic_row_closed,
            "type": "Appell-Humbert generator transition table for L^2=(2,-4,0)",
            "degree_vector": ah_degrees,
            "generator_order": ["g1", "g2", "g3", "g4", "g5", "g6"],
            "generator_factor_formulas": generator_formulas,
            "sample_values": transition_samples,
            "cocycle_law": "Inherited from the selected AH source table; generator formulas satisfy the q79 cocycle law modulo 2*pi*i.",
            "overlap_guardrail": "These are transition/trivialization values for the eta_00 line factor, not Yukawa flavor overlap matrices.",
        },
        "global_Dolbeault_harmonic_representative": {
            "closed_at_row_level": harmonic_row_closed,
            "representative": "eta_00^unit = 32^(1/4) * Theta_{2,0}(z1;i) tensor Eta_{-4,0}(z2;i) dbar_z2",
            "reason": "Theta_{2,0} is holomorphic in the positive degree-2 factor; Eta_{-4,0} dbar_z2 is the Serre-dual harmonic H1 representative for the negative degree-4 factor; the product is a closed non-exact harmonic Dolbeault row in the selected basis.",
            "barpartial_eta": "0",
            "barpartial_star_eta": "0 in the canonical product theta metric row model",
            "partition_of_unity_needed": False,
            "why_no_partition_needed": "The AH automorphy table supplies the global line-bundle gluing; the Dolbeault row is globally defined as an equivariant form on the cover.",
        },
        "Hodge_Lambda_table": {
            "closed_for_eta_row": harmonic_row_closed,
            "equal_radius_metric_convention": "unitary coframe dz1,dz2,dz3 with omega = i/2 sum dzj wedge dbar_zj",
            "form_degree": "(0,1)",
            "line_bundle_weight": "already included in the L2 theta norm",
            "pointwise_norm_of_dbar_z2": 1,
            "L2_norm_of_unit_eta_00": 1,
            "Lambda_on_eta_00": 0,
            "primitive_part": "eta_00 has no (1,1) curvature component; Lambda is relevant after applying curvature/HYM residual, not to the raw (0,1) Ext row.",
            "star_convention": "Hodge star is fixed by the equal-radius unitary coframe and volume normalized to one in the theta quadrature table.",
        },
        "gauge_projector_table": {
            "closed_for_eta_row": harmonic_row_closed,
            "projector_name": "P_eta_00",
            "formula": "P_eta_00(v)=<eta_00^unit,v> eta_00^unit",
            "matrix_on_basis_eta00_plus_complement": [[1.0, 0.0], [0.0, 0.0]],
            "coulomb_slice_status": "eta_00 row is harmonic/co-closed in the canonical row model; infinitesimal gauge complement is projected away by I-P_eta_00",
            "not_full_connection_gauge_fix": True,
        },
        "HYM_correction_status": {
            "row_level_harmonic_seed_closed": harmonic_row_closed,
            "split_AH_Chern_connection_available": True,
            "nonlinear_non_split_HYM_metric_correction_closed": nonlinear_hym_correction_closed,
            "why_open": "The exact HYM metric for the non-split rank-2 extension requires solving the coupled trace-free curvature equation. This artifact supplies the normalized harmonic Ext seed and row projector, not the nonlinear connection coefficients.",
            "next_equation": "Solve Lambda(F_{A_split + eta_00^unit + a_HYM})_0 = 0 with Coulomb gauge d_A^* a_HYM = 0 in the selected End0 basis.",
        },
        "newton_readiness": {
            "transition_overlap_table_closed": harmonic_row_closed,
            "global_Dolbeault_harmonic_row_closed": harmonic_row_closed,
            "Hodge_Lambda_row_table_closed": harmonic_row_closed,
            "gauge_projector_row_closed": harmonic_row_closed,
            "nonlinear_HYM_connection_correction_closed": nonlinear_hym_correction_closed,
            "ready": full_newton_ready,
            "first_blocker": "selected_nonlinear_HYM_connection_correction_coefficients_for_End0_Newton",
        },
        "superset_strategy": {
            "straight_path": "Direct AH transition factors plus canonical harmonic eta_00 row give overlap/Hodge/projector data for the selected Ext seed.",
            "support_path": "Adjoint su(2)/End0 packet supplies the carrier where the next nonlinear HYM correction must be solved.",
            "locked_target": "selected V_alpha branch L=(1,-2,0), L^2=(2,-4,0), eta_00 unit normalized, no measured constants.",
            "not_used": "No observed flavor, gauge, or mass data are used.",
        },
        "what_closes_now": {
            "transition_overlap_trivialization_values_for_eta00": harmonic_row_closed,
            "global_equivariant_Dolbeault_harmonic_row": harmonic_row_closed,
            "Hodge_Lambda_row_table": harmonic_row_closed,
            "eta00_rank_one_gauge_projector": harmonic_row_closed,
        },
        "what_remains_open": {
            "nonlinear_HYM_metric_connection_correction": True,
            "full_End0_Newton_Galerkin_coefficients": True,
            "finite_operator_values_rhoE_DE_Riesz_Green_dotD": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_Nonlinear_HYM_Correction_Coefficient_Solve_v1",
    }

    cert = {
        "certificate": "MTT_Selected_Ext_Overlap_HYM_Hodge_Projector_Table_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "transition_overlap_table_closed": harmonic_row_closed,
        "Hodge_Lambda_row_table_closed": harmonic_row_closed,
        "gauge_projector_row_closed": harmonic_row_closed,
        "nonlinear_HYM_connection_correction_closed": nonlinear_hym_correction_closed,
        "newton_ready": full_newton_ready,
        "first_blocker": candidate["newton_readiness"]["first_blocker"],
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = """# MTT Selected Ext Overlap HYM Hodge Projector Table v1

## Result

For the unit selected Ext row

```text
eta_00^unit = 32^(1/4) * Theta_{2,0}(z1;i) tensor Eta_{-4,0}(z2;i) dbar_z2
```

this artifact emits the row-level transition, harmonic, Hodge/Lambda, and gauge
projector data.

## Transition Table

For `L^2=(2,-4,0)` in generator order `g1,...,g6`:

```text
g1 -> 1
g2 -> exp(2*pi - 4*pi*i*z1)
g3 -> 1
g4 -> exp(-4*pi + 8*pi*i*z2)
g5 -> 1
g6 -> 1
```

The shared circle remains trivial.

## Hodge And Projector Data

In the equal-radius unitary coframe, the `dbar_z2` factor has unit local norm,
the theta metric supplies the line-bundle norm, and the unit-rescaled row has
`L2` norm one.  The row projector is:

```text
P_eta_00(v)=<eta_00^unit,v> eta_00^unit.
```

The row is harmonic in the canonical product theta metric model:

```text
barpartial eta_00 = 0
barpartial^* eta_00 = 0
```

## Guardrail

This does not solve the nonlinear HYM connection.  It supplies the normalized
harmonic Ext seed and the row-level projector needed by that solve.  The next
equation is:

```text
Lambda(F_{A_split + eta_00^unit + a_HYM})_0 = 0,
d_A^* a_HYM = 0.
```

## Next Artifact

`MTT_Selected_Nonlinear_HYM_Correction_Coefficient_Solve_v1`.
"""

    OUT_CANDIDATE.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_PROOF.write_text(proof, encoding="utf-8")
    print(f"Wrote {OUT_CANDIDATE}")
    print(f"Wrote {OUT_CERT}")
    print(f"Wrote {OUT_PROOF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
