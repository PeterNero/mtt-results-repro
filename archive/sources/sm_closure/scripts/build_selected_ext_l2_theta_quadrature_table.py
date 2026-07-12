"""Build the selected L2 theta quadrature table for the eta_00 Ext row."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_CANDIDATE = ROOT / "candidate_data" / "selected_ext_l2_theta_quadrature_table.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_ext_l2_theta_quadrature_table_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_Ext_L2_Theta_Quadrature_Table_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def theta_tau_i(degree: int, index: int, z: complex, cutoff: int) -> complex:
    """Canonical degree-d theta basis at tau=i in the AH convention."""
    total = 0j
    for n in range(-cutoff, cutoff + 1):
        shifted = n + index / degree
        total += cmath.exp(-math.pi * degree * shifted * shifted + 2j * math.pi * degree * shifted * z)
    return total


def theta_l2_norm_square(degree: int, index: int, mesh: int, cutoff: int) -> float:
    """Midpoint quadrature for int_[0,1]^2 |theta|^2 exp(-2*pi*d*y^2) dx dy."""
    total = 0.0
    for ix in range(mesh):
        x = (ix + 0.5) / mesh
        for iy in range(mesh):
            y = (iy + 0.5) / mesh
            z = complex(x, y)
            metric_weight = math.exp(-2.0 * math.pi * degree * y * y)
            total += abs(theta_tau_i(degree, index, z, cutoff)) ** 2 * metric_weight
    return total / (mesh * mesh)


def convergence_row(degree: int, index: int) -> dict:
    exact = 1.0 / math.sqrt(2.0 * degree)
    samples = []
    for mesh in [16, 32, 64, 96, 128]:
        value = theta_l2_norm_square(degree, index, mesh=mesh, cutoff=12)
        samples.append(
            {
                "mesh": mesh,
                "cutoff": 12,
                "value": value,
                "absolute_error_against_exact": abs(value - exact),
            }
        )
    return {
        "degree": degree,
        "index": index,
        "exact_norm_square": exact,
        "quadrature_samples": samples,
        "max_error": max(item["absolute_error_against_exact"] for item in samples),
        "final_error": samples[-1]["absolute_error_against_exact"],
    }


def main() -> int:
    previous_path = ROOT / "candidate_data" / "selected_normalized_ext_local_form_table.candidate.json"
    previous = load(previous_path)

    theta_20 = convergence_row(2, 0)
    theta_40_dual = convergence_row(4, 0)
    eta_norm_square = theta_20["exact_norm_square"] * theta_40_dual["exact_norm_square"]
    eta_unit_rescale = 1.0 / math.sqrt(eta_norm_square)
    eta_quadrature_final = (
        theta_20["quadrature_samples"][-1]["value"] * theta_40_dual["quadrature_samples"][-1]["value"]
    )

    exact_closed = all(
        [
            previous["selected_ext_identity"]["local_form_row_id"] == "eta_00",
            previous["what_closes_now"]["cohomological_scalar_normalization_fixed_to_one"] is True,
            abs(eta_norm_square - 1.0 / math.sqrt(32.0)) < 1e-14,
            abs(eta_unit_rescale - 32.0 ** 0.25) < 1e-14,
        ]
    )

    candidate = {
        "candidate": "MTTSelectedExtL2ThetaQuadratureTable",
        "status": "MTT_SELECTED_EXT_L2_THETA_QUADRATURE_TABLE_BUILT_OVERLAP_HYM_PROJECTOR_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "selected_normalized_ext_local_form_table": str(previous_path),
        },
        "selected_row": {
            "row_id": "eta_00",
            "symbolic_Cech_label": "theta_plus_0_tensor_eta_minus_0",
            "symbolic_Dolbeault_representative": "Theta_{2,0}(z1; i) tensor Eta_{-4,0}(z2; i) dbar_z2",
            "serre_dual_convention": "Eta_{-4,0} is paired by Serre duality with the canonical positive degree-4 theta basis element Theta_{4,0}; the one-form dbar_z2 has unit equal-radius local norm in this table.",
            "central_shared_circle_factor": 1,
        },
        "canonical_theta_metric": {
            "base": "E_tau = C/(Z+iZ)",
            "tau": "i",
            "hermitian_weight_for_degree_d": "h_d(y)=exp(-2*pi*d*y^2)",
            "theta_basis_formula": "Theta_{d,k}(z)=sum_{n in Z} exp(-pi*d*(n+k/d)^2 + 2*pi*i*d*(n+k/d)*z)",
            "norm_identity": "int_0^1 int_0^1 |Theta_{d,k}(x+iy)|^2 exp(-2*pi*d*y^2) dx dy = 1/sqrt(2*d)",
            "derivation": "The x integral kills all off-diagonal Fourier terms. The remaining Gaussian integral over y after completing the square unfolds the shifted lattice sum to the real-line Gaussian integral 1/sqrt(2*d) in this Appell-Humbert metric convention.",
        },
        "factor_norms": {
            "Theta_2_0_E1": theta_20,
            "Serre_dual_Eta_minus4_0_E2_via_Theta_4_0": theta_40_dual,
        },
        "eta_00_l2_table": {
            "cohomological_coefficient": 1,
            "unrescaled_norm_square_exact": eta_norm_square,
            "unrescaled_norm_square_exact_expression": "1/sqrt(32)",
            "unrescaled_norm_exact": math.sqrt(eta_norm_square),
            "unit_L2_rescale_factor_exact_expression": "32^(1/4)",
            "unit_L2_rescale_factor_numeric": eta_unit_rescale,
            "unit_L2_representative": "32^(1/4) * Theta_{2,0}(z1; i) tensor Eta_{-4,0}(z2; i) dbar_z2",
            "final_mesh_product_value": eta_quadrature_final,
            "final_mesh_product_error": abs(eta_quadrature_final - eta_norm_square),
            "quadrature_rule": {
                "type": "tensor midpoint/trapezoid on [0,1]^2 for each elliptic factor",
                "mesh_values_tested": [16, 32, 64, 96, 128],
                "theta_series_cutoff": 12,
                "normalization": "unit area on each elliptic factor; central shared circle contributes factor 1",
            },
        },
        "overlap_and_newton_status": {
            "l2_theta_quadrature_closed": exact_closed,
            "analytic_overlap_trivialization_values_closed": False,
            "global_partition_of_unity_or_harmonic_representative_closed": False,
            "selected_HYM_metric_connection_correction_closed": False,
            "Hodge_Lambda_table_closed": False,
            "gauge_projector_closed": False,
            "newton_ready": False,
            "first_blocker": "selected_overlap_trivialization_and_HYM_Hodge_projector_table_for_eta_00",
        },
        "superset_strategy": {
            "straight_path": "Direct AH theta metric gives exact eta_00 L2 normalization on the selected row.",
            "support_path": "Numerical midpoint quadrature is only a reproducibility check of the exact Gaussian-theta identity.",
            "locked_target": "eta_00 in selected q79/F,m=1 V_alpha branch, L^2=(2,-4,0), neutral shared circle, no measured constants.",
            "not_used": "No observed masses, mixings, couplings, or benchmark matrices enter this normalization.",
        },
        "what_closes_now": {
            "canonical_tau_i_theta_metric_declared": True,
            "theta_factor_norms_exact": exact_closed,
            "eta_00_unrescaled_L2_norm_square_exact": exact_closed,
            "eta_00_unit_L2_rescale_factor_exact": exact_closed,
            "reproducible_quadrature_convergence_table_emitted": True,
        },
        "what_remains_open": {
            "transition_overlap_trivialization_values": True,
            "global_Dolbeault_partition_or_harmonic_representative": True,
            "selected_HYM_metric_connection_correction": True,
            "Hodge_Lambda_and_gauge_projector_tables": True,
            "selected_Newton_Galerkin_coefficients": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_Ext_Overlap_HYM_Hodge_Projector_Table_v1",
    }

    cert = {
        "certificate": "MTT_Selected_Ext_L2_Theta_Quadrature_Table_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "l2_theta_quadrature_closed": exact_closed,
        "eta_00_unrescaled_norm_square": eta_norm_square,
        "eta_00_unrescaled_norm_square_expression": "1/sqrt(32)",
        "eta_00_unit_rescale_factor_expression": "32^(1/4)",
        "newton_ready": False,
        "first_blocker": candidate["overlap_and_newton_status"]["first_blocker"],
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = """# MTT Selected Ext L2 Theta Quadrature Table v1

## Result

For the selected row

```text
eta_00 = Theta_{2,0}(z1; i) tensor Eta_{-4,0}(z2; i) dbar_z2
```

the canonical Appell-Humbert theta metric at `tau=i` gives:

```text
||Theta_{d,k}||^2 = 1/sqrt(2*d)
||eta_00||^2 = (1/sqrt(4))*(1/sqrt(8)) = 1/sqrt(32)
```

Therefore the unit `L2` representative is:

```text
eta_00^unit = 32^(1/4) * eta_00
```

## Derivation

Use the standard basis

```text
Theta_{d,k}(z)=sum_n exp(-pi*d*(n+k/d)^2 + 2*pi*i*d*(n+k/d)*z)
```

with Hermitian weight

```text
h_d(y)=exp(-2*pi*d*y^2).
```

The integral over `x in [0,1]` kills the off-diagonal Fourier terms. Completing
the square in `y` unfolds the remaining shifted lattice sum into the Gaussian
real-line integral, giving `1/sqrt(2*d)` in this metric convention.

The negative-degree factor is interpreted by Serre duality as the positive
degree-4 theta norm for the dual representative. The shared circle contributes
degree zero and factor `1`.

## What This Closes

This closes the exact `L2` theta normalization and emits a reproducible
quadrature convergence table for `eta_00`.

## Guardrail

This still does not emit transition-overlap trivialization values, a global
partition-of-unity or harmonic Dolbeault representative, the selected HYM
metric correction, Hodge/Lambda tables, or gauge projectors. The row is
normalized, but the End0 Newton/Galerkin solve is not yet ready.

## Next Artifact

`MTT_Selected_Ext_Overlap_HYM_Hodge_Projector_Table_v1`.
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
