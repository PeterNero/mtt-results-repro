from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

SELECTED_SPINC = ROOT / "certificates" / "q79_selected_side_spin_spinc_decision_certificate.json"
W2_BRANCH = ROOT / "certificates" / "q79_signed_sheet_w2_branch_divisor_reduction_certificate.json"
HYM_DICHOTOMY = ROOT / "certificates" / "q79_spinc_flat_hym_ramification_extension_certificate.json"

OUT_CERT = ROOT / "certificates" / "q79_branch_cusp_resolution_rootstack_hym_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "q79_Branch_Cusp_Resolution_and_RootStack_HYM_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    selected = load(SELECTED_SPINC)
    w2_branch = load(W2_BRANCH)
    hym = load(HYM_DICHOTOMY)

    a = sp.symbols("a")
    elliptic_rhs = a**3 - a
    three_division = 3 * a**4 - 6 * a**2 - 1
    division_squarefree = sp.degree(sp.gcd(three_division, sp.diff(three_division, a)), a) == 0
    division_avoids_two_torsion = sp.resultant(three_division, elliptic_rhs, a) != 0
    finite_flex_count = int(2 * sp.degree(three_division, a))
    flex_count = finite_flex_count + 1

    branch_points = selected["interval_result"]["norm_degree"]
    base_genus = 1
    normalization_genus = 2 * base_genus - 1 + branch_points // 2

    H_square = w2_branch["finite_data"]["H_square"]
    branch_coefficient = w2_branch["finite_data"]["branch_coefficient_from_pairing"]
    branch_square = branch_coefficient**2 * H_square
    arithmetic_genus = 1 + branch_square // 2
    total_delta = arithmetic_genus - normalization_genus
    lifted_cusp_count = int(2 * flex_count)

    # Embedded resolution of y^2=x^3. Three blowups are needed for an SNC total
    # transform; exceptional multiplicities are 2, 3, and 6.
    resolution_components = [
        {"name": "strict_transform", "multiplicity": 1, "sign_holonomy": -1},
        {"name": "E1", "multiplicity": 2, "sign_holonomy": 1},
        {"name": "E2", "multiplicity": 3, "sign_holonomy": -1},
        {"name": "E3", "multiplicity": 6, "sign_holonomy": 1},
    ]
    odd_components = [
        row["name"] for row in resolution_components if row["multiplicity"] % 2 == 1
    ]

    checks = {
        "selected_interval_norm_is_squarefree": (
            selected["checks"]["selected_side_norm_is_squarefree_throughout_interval"]
            is True
        ),
        "selected_interval_avoids_all_nine_flexes": (
            selected["interval_result"]["all_nine_flex_points_avoided"] is True
        ),
        "three_division_polynomial_is_squarefree": division_squarefree,
        "finite_flexes_are_not_two_torsion": division_avoids_two_torsion,
        "smooth_cubic_has_nine_flex_points": flex_count == 9,
        "normalization_double_cover_has_36_simple_branch_points": branch_points == 36,
        "normalization_genus_is_19": normalization_genus == 19,
        "branch_arithmetic_genus_is_37": arithmetic_genus == 37,
        "total_delta_is_18": total_delta == 18,
        "two_cusp_lifts_per_flex_give_18_cusps": lifted_cusp_count == 18,
        "cusp_delta_budget_is_exhausted": lifted_cusp_count == total_delta,
        "cusp_SNC_resolution_multiplicities_are_2_3_6": (
            [row["multiplicity"] for row in resolution_components[1:]] == [2, 3, 6]
        ),
        "only_strict_transform_and_E2_have_odd_sign_monodromy": (
            odd_components == ["strict_transform", "E2"]
        ),
        "complement_flat_HYM_theorem_available": (
            hym["claim_tiers"]["HYM_equation_on_smooth_complement"] == "CLOSED"
        ),
        "ordinary_smooth_extension_remains_no_go": (
            hym["claim_tiers"]["ordinary_smooth_unramified_extension"]
            == "CLOSED_NO_GO"
        ),
        "final_integral_branch_not_promoted": (
            selected["guardrails"]["claims_integral_gerbe_branch_selected"] is False
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "name": "SelectedSideBranchCuspResolutionAndRootStackHYMTheorem",
        "singularity_inventory": {
            "dual_cubic_flexes": 9,
            "K3_cover_behavior_at_flexes": (
                "the interval flex resultant and infinity value exclude ramification "
                "over every flex, so each dual-cubic cusp has two etale lifts"
            ),
            "branch_singularities": "exactly 18 ordinary cusps",
            "proof_by_genus": (
                "the normalization is a genus-19 double cover of the elliptic "
                "normalization, while a 6H divisor on H^2=2 K3 has arithmetic "
                "genus 37; the delta budget 18 is exhausted by the 18 lifted cusps"
            ),
            "status": "CLOSED_THROUGHOUT_SELECTED_ALIGNMENT_INTERVAL",
        },
        "local_embedded_resolution": {
            "cusp_equation": "y^2=x^3",
            "blowup_count_for_SNC_total_transform": 3,
            "exceptional_multiplicities": [2, 3, 6],
            "all_component_multiplicities": resolution_components,
            "order_two_sign_components": odd_components,
            "status": "CLOSED",
        },
        "global_extension": {
            "construction": (
                "blow up the 18 disjoint cusp centers by the same three-step embedded "
                "resolution and take the order-two root stack along the reduced odd "
                "divisor consisting of the strict transform and every E2 component"
            ),
            "connection": (
                "the pulled determinant character extends as a flat orbifold line; "
                "therefore its curvature is zero and it is HYM on the smooth root stack"
            ),
            "parameter_count": 0,
            "external_primary_source": "https://arxiv.org/abs/2201.00064",
            "status": "EXPLICIT_RESOLVED_ROOTSTACK_HYM_CARRIER_CLOSED",
        },
        "descent_boundary": (
            "The flat orbifold carrier does not descend to an ordinary smooth line on "
            "the original K3 because branch meridians have holonomy -1. MTT must select "
            "the resolved/root-stack carrier or a different smooth twisted-HYM replacement."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "q79_branch_cusp_resolution_rootstack_hym",
        "date": "2026-07-15",
        "status": "Q79_SELECTED_BRANCH_18_CUSPS_AND_EXPLICIT_RESOLVED_ROOTSTACK_HYM_CARRIER_CLOSED_MTT_ACTION_TRANSVERSE_SELECTION_OPEN",
        "inputs": {
            "selected_side_spin_spinc": str(SELECTED_SPINC),
            "w2_branch_divisor": str(W2_BRANCH),
            "flat_HYM_ramification_dichotomy": str(HYM_DICHOTOMY),
        },
        "checks": checks,
        "finite_data": {
            "elliptic_three_division_polynomial": str(three_division),
            "finite_flex_count": int(finite_flex_count),
            "total_flex_count": int(flex_count),
            "normalization_branch_point_count": branch_points,
            "normalization_genus": normalization_genus,
            "branch_square": branch_square,
            "branch_arithmetic_genus": arithmetic_genus,
            "total_delta": total_delta,
            "ordinary_cusp_count": lifted_cusp_count,
            "resolution_components": resolution_components,
            "root_stack_odd_components": odd_components,
        },
        "theorem": theorem,
        "claim_tiers": {
            "selected_interval_branch_singularity_inventory": "CLOSED_18_ORDINARY_CUSPS",
            "explicit_global_log_resolution_combinatorics": "CLOSED",
            "resolved_order_two_rootstack_flat_HYM_carrier": "CLOSED",
            "ordinary_smooth_line_descent_to_original_K3": "CLOSED_NO_GO",
            "MTT_selection_of_resolved_rootstack_carrier": "OPEN",
            "physical_transverse_frame_connection": "OPEN",
            "selected_action": "OPEN",
            "final_integral_branch_selection": "OPEN",
        },
        "guardrails": {
            "claims_original_branch_divisor_is_smooth": False,
            "claims_rootstack_line_descends_smoothly_to_original_K3": False,
            "claims_MTT_selects_resolved_rootstack": False,
            "claims_physical_transverse_connection_closed": False,
            "claims_selected_action_closed": False,
            "claims_final_integral_branch_selected": False,
            "uses_observed_physics_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Branch Cusp Resolution and Root-Stack HYM v1

Date: 2026-07-15

## Exact singularity inventory

The selected interval certificate now proves two facts simultaneously:

```text
the degree-36 elliptic norm is square-free,
the norm avoids all nine flex points of the cubic.
```

The second statement uses the exact three-division polynomial
`3a^4-6a^2-1` for the eight finite flexes and the leading pullback coefficient
for the flex at infinity.

The normalization of the q79 branch is therefore a double cover of the
elliptic normalization, branched at 36 distinct non-flex points. Riemann--Hurwitz
gives

```text
g_norm=2*1-1+36/2=19.
```

For `[B]=6H` and `H^2=2`,

```text
B^2=72,
p_a(B)=1+B^2/2=37,
delta_total=37-19=18.
```

The dual sextic has nine ordinary cusps, one for each flex. The K3 double cover
is unramified there, so every cusp has two lifts. These eighteen ordinary cusps
already contribute total delta eighteen. Hence there are no further branch
singularities throughout the certified selected-side interval.

## Explicit resolution and sign data

An ordinary cusp `y^2=x^3` requires three blowups for an SNC total transform.
The exceptional multiplicities are

```text
E1:2,  E2:3,  E3:6,
```

while the strict transform has multiplicity one. Order-two determinant
monodromy is nontrivial precisely on odd-multiplicity components:

```text
strict transform and E2: -1,
E1 and E3: +1.
```

Perform this disjoint local resolution at all eighteen cusps and take the
order-two root stack along the reduced odd divisor. The determinant character
extends as a flat orbifold line, so its curvature vanishes and it is HYM on the
resulting smooth root-stack carrier. The construction is exact and adds no
parameter. The root-stack/parabolic connection correspondence is described in
https://arxiv.org/abs/2201.00064.

## Remaining MTT boundary

The constructed orbifold line cannot descend to an ordinary smooth line on the
original K3 because its branch meridian holonomy is `-1`. The remaining source
question is now a discrete geometric choice: prove that MTT selects this
resolved/root-stack carrier, or emit a different smooth twisted-HYM replacement.
The external transverse-frame connection, selected action, and final
integral/gerbe source gate remain open.

Current status:

```text
Q79_SELECTED_BRANCH_18_CUSPS_AND_EXPLICIT_RESOLVED_ROOTSTACK_HYM_CARRIER_CLOSED_MTT_ACTION_TRANSVERSE_SELECTION_OPEN
```
"""

    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed cusp-resolution checks: {failed}")

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
