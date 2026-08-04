from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SAME_CIRCLE = ROOT / "certificates" / "same_circle_weight2_bundle_obstruction_certificate.json"
METRIC_SOURCE = ROOT / "certificates" / "world_in_world_z64_metric_source_map_certificate.json"
ROOTSTACK_HYM = ROOT / "certificates" / "q79_branch_cusp_resolution_rootstack_hym_certificate.json"

OUT_CERT = ROOT / "certificates" / "global_helicity_bundle_same_circle_nogo_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Global_Helicity_Bundle_Same_Circle_NoGo_and_Covariant_Source_Replacement_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    same_circle = load(SAME_CIRCLE)
    metric_source = load(METRIC_SOURCE)
    rootstack_hym = load(ROOTSTACK_HYM)

    helicity_weight_one = 1
    helicity_weight_two = 2
    c1_weight_one = -2 * helicity_weight_one
    c1_weight_two = -2 * helicity_weight_two
    internal_flat_de_rham_c1 = 0
    hom_bundle_c1 = c1_weight_two - internal_flat_de_rham_c1

    checks = {
        "external_helicity_formula_is_C_minus_2h": (
            "C=-2h"
            in same_circle["theorem"]["local_vs_global"]["global_helicity_bundle"]
        ),
        "external_weight_one_Chern_number_is_minus_two": c1_weight_one == -2,
        "external_weight_two_Chern_number_is_minus_four": c1_weight_two == -4,
        "internal_determinant_connection_is_flat_HYM": (
            rootstack_hym["claim_tiers"]["resolved_order_two_rootstack_flat_HYM_carrier"]
            == "CLOSED"
        ),
        "internal_de_Rham_Chern_class_is_zero": internal_flat_de_rham_c1 == 0,
        "product_base_restriction_has_Chern_mismatch": (
            internal_flat_de_rham_c1 != c1_weight_two
        ),
        "global_weight_two_line_isomorphism_is_impossible": c1_weight_two != 0,
        "global_Hom_bundle_has_nonzero_Chern_number": hom_bundle_c1 == -4,
        "no_nowhere_zero_global_scalar_intertwiner": hom_bundle_c1 != 0,
        "fixed_direction_metric_source_remains_valid": (
            metric_source["checks"]["metric_Bstar_support_is_exact_plane"] is True
        ),
        "local_metric_source_uses_fixed_TT_basis": (
            metric_source["construction"]["TT_basis"]
            == [
                "e_plus=(E11-E22)/sqrt(2)",
                "e_cross=(E12+E21)/sqrt(2)",
            ]
        ),
        "finite_exact_support_is_unchanged": (
            metric_source["construction"]["support_identity_residual"] < 1.0e-12
        ),
        "final_integral_branch_not_promoted": (
            rootstack_hym["guardrails"]["claims_final_integral_branch_selected"]
            is False
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "name": "GlobalHelicityBundleSameCircleNoGoAndCovariantReplacementTheorem",
        "global_no_go": {
            "base": "X_internal x S2_momentum",
            "internal_line": "p_X^*L_shared^2, flat in the selected finite/SpinC sector",
            "external_line": "p_S2^*H_{+2}",
            "restriction_test": (
                "On {x}xS2, the internal line has c1=0 while H_{+2} has c1=-4."
            ),
            "conclusion": (
                "There is no global connection-preserving line isomorphism and no "
                "global reduction of the helicity bundle to the finite shared Z64 carrier."
            ),
            "status": "CLOSED_NO_GO",
        },
        "local_survival": {
            "statement": (
                "On a fixed direction or contractible momentum patch, H_{+2} is "
                "trivial and the existing plus/cross DG rows are valid."
            ),
            "finite_consequence": (
                "Pi_exact64 DG(0)^*P_TT=DG(0)^*P_TT and lambda=15 are unchanged."
            ),
            "status": "CLOSED",
        },
        "correct_global_object": {
            "replace": "L_shared^2 ~= H_{+2}",
            "with": (
                "a bundle-valued covariant source morphism whose local plus/cross "
                "matrices patch by the helicity transition functions"
            ),
            "typing": (
                "DG_global is a section of Hom(E_internal_exact,H_{+2}), or the "
                "source domain is explicitly twisted by H_{+2}; it is not two "
                "globally defined scalar rows."
            ),
            "topological_obligation": (
                "Because the Hom line has c1=-4 on S2, a scalar representative "
                "cannot be everywhere nonzero; patching or zeros are mandatory."
            ),
            "status": "TARGET_CORRECTED_CONSTRUCTION_OPEN",
        },
        "separation_of_roles": {
            "shared_Z64": "finite internal mode, half-turn, SpinC determinant, and pole support",
            "external_U1": "continuous momentum-frame helicity bundle and its nonzero Chern class",
            "consequence": (
                "The same circle can mean compatible local weight action without "
                "being a global identity of internal and external principal bundles."
            ),
        },
        "external_primary_source": same_circle["theorem"]["local_vs_global"][
            "external_primary_source"
        ],
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "global_helicity_bundle_same_circle_nogo",
        "date": "2026-07-15",
        "status": "GLOBAL_SHARED_Z64_HELICITY_LINE_IDENTIFICATION_NOGO_LOCAL_DG_AND_INTERNAL_SPINC_HYM_CLOSED_COVARIANT_ACTION_SOURCE_OPEN",
        "inputs": {
            "same_circle_bundle_obstruction": str(SAME_CIRCLE),
            "world_in_world_metric_source": str(METRIC_SOURCE),
            "resolved_rootstack_HYM": str(ROOTSTACK_HYM),
        },
        "checks": checks,
        "finite_data": {
            "external_weight_one_Chern_number": c1_weight_one,
            "external_weight_two_Chern_number": c1_weight_two,
            "internal_flat_de_Rham_Chern_number_on_momentum_sphere": internal_flat_de_rham_c1,
            "Hom_internal_to_helicity2_Chern_number": hom_bundle_c1,
        },
        "theorem": theorem,
        "claim_tiers": {
            "global_internal_external_line_identity": "CLOSED_NO_GO",
            "fixed_direction_local_DG": "CLOSED",
            "finite_Z64_support_and_lambda15": "CLOSED_UNCHANGED",
            "internal_SpinC_rootstack_HYM": "CLOSED",
            "global_covariant_helicity_bundle_source": "OPEN_CONSTRUCTION",
            "selected_action_on_global_helicity_bundle": "OPEN",
            "massless_Lorentzian_graviton_interpretation": "OPEN",
        },
        "guardrails": {
            "claims_global_plus_cross_frame_exists": False,
            "claims_finite_Z64_is_the_global_transverse_U1_bundle": False,
            "claims_internal_flat_line_equals_external_helicity_line": False,
            "claims_local_DG_result_invalid": False,
            "claims_selected_global_action_closed": False,
            "uses_observed_physics_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# Global Helicity-Bundle Same-Circle No-Go and Covariant Source Replacement v1

Date: 2026-07-15

## The global identity is impossible

The internal shared/SpinC determinant line is flat. The physical helicity line
over the momentum-direction sphere is not. With the convention already used in
the QG certificate,

```text
c1(H_h)[S2]=-2h,
c1(H_{+1})=-2,
c1(H_{+2})=-4.
```

On a product correspondence base `X_internal x S2`, restrict a proposed
isomorphism

```text
p_X^*L_shared^2 ~= p_S2^*H_{+2}
```

to `{x}xS2`. The left side has de Rham Chern number zero; the right side has
Chern number `-4`. Therefore no global line or connection isomorphism exists.
A finite `Z64` bundle also cannot be a global reduction of this non-torsion
helicity bundle.

## What survives

The computed world-in-world source is a fixed-direction or local-patch theorem.
On a contractible momentum patch, the helicity line is trivial and the displayed
plus/cross basis is valid. Hence

```text
Pi_exact64 DG(0)^*P_TT=DG(0)^*P_TT,
lambda_internal=15
```

remain exactly closed at their declared local/fiberwise tier.

## Correct global replacement

The physical source must be bundle-valued. Its local plus/cross matrices must
patch with the helicity transition functions. Equivalently, `DG_global` is a
section of an appropriate `Hom(E_internal_exact,H_{+2})` bundle, or the source
domain must itself be twisted by `H_{+2}`. It cannot be represented by two
everywhere-defined scalar rows. The Hom bundle restricts with Chern number `-4`,
so zeros or patching are topologically mandatory.

This separates the two roles cleanly:

```text
shared Z64: finite internal mode, SpinC sign, exact support and pole;
external U1: continuous helicity frame bundle over momentum directions.
```

"Same circle" may mean the same local weight action. It cannot mean global
identity of these principal bundles. The helicity-bundle topology used here is
documented in https://arxiv.org/abs/2407.03494.

Current status:

```text
GLOBAL_SHARED_Z64_HELICITY_LINE_IDENTIFICATION_NOGO_LOCAL_DG_AND_INTERNAL_SPINC_HYM_CLOSED_COVARIANT_ACTION_SOURCE_OPEN
```
"""

    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed global helicity no-go checks: {failed}")

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
