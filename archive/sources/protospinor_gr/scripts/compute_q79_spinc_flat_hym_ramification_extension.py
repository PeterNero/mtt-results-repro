from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SAME_SOURCE = ROOT / "certificates" / "q79_shared_z64_same_source_monodromy_map_certificate.json"
SELECTED_SPINC = ROOT / "certificates" / "q79_selected_side_spin_spinc_decision_certificate.json"
W2_BRANCH = ROOT / "certificates" / "q79_signed_sheet_w2_branch_divisor_reduction_certificate.json"

OUT_CERT = ROOT / "certificates" / "q79_spinc_flat_hym_ramification_extension_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "q79_SpinC_Flat_HYM_and_Ramification_Extension_Dichotomy_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    same_source = load(SAME_SOURCE)
    selected_spinc = load(SELECTED_SPINC)
    w2_branch = load(W2_BRANCH)

    branch_coefficient = w2_branch["finite_data"]["branch_coefficient_from_pairing"]
    half_branch_coefficient = branch_coefficient // 2
    transposition_rows = [
        row
        for row in same_source["finite_data"]["class_table"]
        if row["cycle_type"] == "transposition"
    ]
    meridian_phases = [row["chi1_phase_exponent_mod64"] for row in transposition_rows]

    checks = {
        "finite_same_source_map_available": (
            same_source["claim_tiers"]["finite_same_source_q79_to_Z64_monodromy_map"]
            == "CLOSED_UNIQUE"
        ),
        "branch_meridian_has_minus_one_determinant_holonomy": meridian_phases == [32, 32, 32],
        "SpinC_determinant_is_sheet_sign": (
            selected_spinc["SpinC_theorem"]["determinant_character"]
            == "z^2=sign(sheet permutation)"
        ),
        "branch_is_an_even_divisor_class": branch_coefficient % 2 == 0,
        "branch_half_class_is_3H": half_branch_coefficient == 3,
        "strict_Spin_is_obstructed": (
            selected_spinc["decision"]["current_executed_selected_side"]["strict_Spin"]
            == "NO_GO"
        ),
        "ordinary_smooth_flat_extension_is_locally_obstructed": all(
            phase == 32 for phase in meridian_phases
        ),
        "order_two_root_stack_matches_holonomy_order": (
            same_source["finite_data"]["Z64_order_two_images"] == [0, 32]
        ),
        "final_integral_branch_not_promoted": (
            selected_spinc["guardrails"]["claims_integral_gerbe_branch_selected"]
            is False
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "name": "SpinCFlatHYMAndRamificationExtensionDichotomy",
        "complement": {
            "space": "X=Y\\B, the executed selected-side branch complement",
            "line": "L_det with holonomy sign o rho_sheet",
            "connection": "the unitary flat connection classified by this character",
            "curvature": "F_det=0",
            "HYM": (
                "F_det^(0,2)=0 and Lambda_omega F_det=0 for every compatible "
                "Hermitian form on the smooth complement"
            ),
            "status": "CLOSED",
        },
        "ordinary_extension_no_go": {
            "local_model": "punctured transverse disk Delta* around a smooth point of B",
            "meridian_holonomy": "-1",
            "proof": (
                "A smooth unramified line with smooth connection on the filled disk has "
                "holonomy tending to +1 on shrinking contractible meridians. Therefore "
                "the -1 flat local system cannot extend as that object."
            ),
            "status": "CLOSED_LOCAL_NO_GO",
        },
        "canonical_ramified_extension": {
            "carrier": "the order-two root stack sqrt[2]{(Y,B)}",
            "line": "the tautological mu2-sign line",
            "parabolic_description": "weight 1/2 logarithmic/parabolic line along B",
            "local_connection": (
                "flat on the order-two uniformizing chart and therefore orbifold HYM "
                "over the smooth branch locus"
            ),
            "root_relation": "T^2=O(B)",
            "external_primary_source": "https://arxiv.org/abs/2201.00064",
            "status": "CANONICAL_EXTENSION_OBJECT_CLOSED_SMOOTH_LOCUS_HYM_CLOSED",
        },
        "double_cover_route": {
            "branch_class": "[B]=6H",
            "square_root_line_class": "O(B)^(1/2)=O(3H)",
            "consequence": (
                "the discriminant double-cover line data exist and trivialize the sign "
                "local system after pullback away from ramification"
            ),
            "status": "LINE_CLASS_EXISTENCE_CLOSED_GLOBAL_SMOOTHNESS_OPEN",
        },
        "global_boundary": (
            "Reduced irreducibility does not prove that B is smooth or simple normal "
            "crossing. Analytic HYM extension through all singular branch points needs "
            "an explicit root-stack chart, log resolution, or selected smooth HYM "
            "replacement, and MTT must select that carrier."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "q79_spinc_flat_hym_ramification_extension",
        "date": "2026-07-15",
        "status": "Q79_SPINC_FLAT_HYM_COMPLEMENT_AND_ROOTSTACK_EXTENSION_CLOSED_ORDINARY_SMOOTH_NOGO_GLOBAL_SINGULAR_HYM_SELECTION_OPEN",
        "inputs": {
            "same_source_monodromy_map": str(SAME_SOURCE),
            "selected_side_spin_spinc": str(SELECTED_SPINC),
            "w2_and_branch_divisor": str(W2_BRANCH),
        },
        "checks": checks,
        "finite_data": {
            "branch_class_coefficient": branch_coefficient,
            "half_branch_class_coefficient": half_branch_coefficient,
            "transposition_meridian_phase_exponents_mod64": meridian_phases,
            "meridian_holonomy": "-1",
            "root_stack_order": 2,
            "parabolic_weight": "1/2",
        },
        "theorem": theorem,
        "claim_tiers": {
            "flat_unitary_determinant_connection_on_complement": "CLOSED",
            "HYM_equation_on_smooth_complement": "CLOSED",
            "ordinary_smooth_unramified_extension": "CLOSED_NO_GO",
            "order_two_root_stack_parabolic_extension_object": "CLOSED",
            "orbifold_HYM_on_smooth_branch_locus": "CLOSED",
            "global_singular_branch_HYM_resolution": "OPEN",
            "MTT_selection_of_rootstack_or_smooth_replacement": "OPEN",
            "physical_transverse_frame_connection": "OPEN",
            "selected_action": "OPEN",
            "final_integral_branch_selection": "OPEN",
        },
        "guardrails": {
            "claims_ordinary_smooth_extension_exists": False,
            "claims_branch_divisor_is_smooth": False,
            "claims_global_singular_HYM_extension_closed": False,
            "claims_MTT_selects_root_stack": False,
            "claims_physical_transverse_connection_closed": False,
            "claims_final_integral_branch_selected": False,
            "uses_observed_physics_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 SpinC Flat HYM and Ramification-Extension Dichotomy v1

Date: 2026-07-15

## Complement theorem

The selected q79-to-`Z64` monodromy map gives the SpinC determinant line on
the branch complement `X=Y\B` as a finite unitary character. It therefore has
the canonical flat unitary connection

```text
F_det=0.
```

Consequently `F_det^(0,2)=0` and `Lambda_omega F_det=0`: the determinant line
is HYM on the smooth complement for every compatible Hermitian form. No
Galerkin solve or continuous parameter is needed for this rank-one sector.

## Ordinary extension no-go

A branch meridian has determinant holonomy `-1`. Near a smooth point of `B`,
this is a flat line on a punctured transverse disk. It cannot extend as an
ordinary unramified smooth line with smooth connection on the filled disk:
holonomy around shrinking contractible loops would tend to `+1`, contradicting
the fixed value `-1`.

Thus "extend through ramification" has a definite answer:

```text
ordinary smooth base-line extension: impossible.
```

## Canonical ramified extension

The correct local/global object is the order-two root stack

```text
sqrt[2]{(Y,B)}.
```

Its tautological `mu2` sign line restricts to the determinant local system and
corresponds to parabolic weight `1/2` along `B`. On order-two uniformizing
charts over the smooth branch locus, the connection is flat and hence orbifold
HYM. This is the standard root-stack/parabolic-connection correspondence; see
https://arxiv.org/abs/2201.00064.

The q79 divisor class supplies an independent global compatibility check:

```text
[B]=6H,  O(B)^(1/2)=O(3H).
```

Therefore the discriminant double-cover line data exist and trivialize the
sign local system after pullback away from ramification.

## Honest remaining boundary

The current proof establishes reduced irreducibility, not smoothness or a
normal-crossings model of `B`. A global analytic HYM statement through all
singular branch points still needs an explicit root-stack chart/log resolution
or a selected smooth HYM replacement. MTT must also select that carrier and
connect it to the physical transverse frame and action. The final
integral/gerbe source flag remains false.

Current status:

```text
Q79_SPINC_FLAT_HYM_COMPLEMENT_AND_ROOTSTACK_EXTENSION_CLOSED_ORDINARY_SMOOTH_NOGO_GLOBAL_SINGULAR_HYM_SELECTION_OPEN
```
"""

    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed HYM/ramification checks: {failed}")

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
