from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SAME_CIRCLE = ROOT / "certificates" / "same_circle_weight2_bundle_obstruction_certificate.json"
SELECTED_SPINC = ROOT / "certificates" / "q79_selected_side_spin_spinc_decision_certificate.json"

OUT_CERT = ROOT / "certificates" / "q79_shared_circle_spinc_determinant_bridge_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "q79_Shared_Circle_SpinC_Determinant_Bridge_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def character_exponent(label: int, element: int, modulus: int) -> int:
    """Return the exact phase exponent modulo modulus for chi_label(element)."""
    return (label * element) % modulus


def is_homomorphism(table: list[int], source_order: int, target_order: int) -> bool:
    return all(
        table[(left + right) % source_order]
        == (table[left] + table[right]) % target_order
        for left in range(source_order)
        for right in range(source_order)
    )


def main() -> None:
    same_circle = load(SAME_CIRCLE)
    selected_spinc = load(SELECTED_SPINC)

    source_order = 6
    target_order = same_circle["finite_Z64_result"]["N"]
    roots = same_circle["finite_Z64_result"]["square_root_character_labels"]
    tt_label = same_circle["finite_Z64_result"]["TT_character_label"]
    root_ratio_label = same_circle["finite_Z64_result"]["root_ratio_character_label"]

    hom_generator_images = [
        image for image in range(target_order) if (source_order * image) % target_order == 0
    ]
    nontrivial_images = [image for image in hom_generator_images if image != 0]
    central_image = nontrivial_images[0]
    central_map = [(central_image * value) % target_order for value in range(source_order)]
    branch_sign_exponents = [0 if value % 2 == 0 else target_order // 2 for value in range(source_order)]

    root_restrictions = {
        str(root): [character_exponent(root, image, target_order) for image in central_map]
        for root in roots
    }
    tt_restriction = [
        character_exponent(tt_label, image, target_order) for image in central_map
    ]
    root_ratio_restriction = [
        character_exponent(root_ratio_label, image, target_order)
        for image in central_map
    ]

    checks = {
        "selected_side_branch_complement_is_Z6": (
            selected_spinc["decision"]["current_executed_selected_side"][
                "branch_complement_H1"
            ]
            == "Z6"
        ),
        "selected_side_strict_Spin_is_obstructed": (
            selected_spinc["decision"]["current_executed_selected_side"]["strict_Spin"]
            == "NO_GO"
        ),
        "selected_side_SpinC_determinant_is_sheet_sign": (
            selected_spinc["SpinC_theorem"]["determinant_character"]
            == "z^2=sign(sheet permutation)"
        ),
        "shared_carrier_is_Z64": target_order == 64,
        "weight_two_roots_are_chi1_and_chi33": roots == [1, 33],
        "all_C6_to_C64_homomorphism_images_enumerated": hom_generator_images == [0, 32],
        "unique_nontrivial_C6_to_C64_map": nontrivial_images == [32],
        "central_map_is_homomorphism": is_homomorphism(
            central_map, source_order, target_order
        ),
        "central_image_has_order_two": (
            central_image != 0 and (2 * central_image) % target_order == 0
        ),
        "chi1_restricts_to_branch_sign": root_restrictions["1"] == branch_sign_exponents,
        "chi33_restricts_to_branch_sign": root_restrictions["33"] == branch_sign_exponents,
        "both_roots_have_identical_restriction": (
            root_restrictions["1"] == root_restrictions["33"]
        ),
        "TT_weight_two_is_trivial_on_central_image": tt_restriction == [0] * source_order,
        "root_ratio_is_trivial_on_central_image": (
            root_ratio_restriction == [0] * source_order
        ),
        "final_integral_branch_not_promoted": (
            selected_spinc["guardrails"]["claims_integral_gerbe_branch_selected"]
            is False
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "name": "RootIndependentSharedCircleSpinCDeterminantBridgeTheorem",
        "base": "the executed selected-side branch complement X with H1(X;Z)=Z6",
        "branch_sign": "a:Z6->Z2, a(mu)=1",
        "central_embedding": "iota:Z2->Z64, iota(1)=32",
        "canonical_map": "h=iota o a:Z6->Z64, h(mu)=32",
        "uniqueness": (
            "Hom(Z6,Z64) has exactly two elements because gcd(6,64)=2; h is "
            "the unique nontrivial one."
        ),
        "character_identity": (
            "For r in {1,33}, chi_r o h=(-1)^a=det(SpinC sheet lift), "
            "whereas chi_2 o h=1 and chi_32 o h=1."
        ),
        "flat_line_consequence": (
            "For either admissible shared-circle weight-one root L_r, the flat "
            "Hermitian line with connection h^*L_r is connection-isomorphic to "
            "the SpinC determinant sign line L_det."
        ),
        "root_independence": (
            "The determinant bridge does not select chi_1 versus chi_33 and does "
            "not need to: their quotient chi_32 is trivial after restriction along h."
        ),
        "conditional_selection": (
            "If the selected MTT q79 carrier is required to obtain its nontrivial "
            "SpinC determinant from the shared Z64 channel, h is forced and adds no "
            "discrete or continuous parameter."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "q79_shared_circle_spinc_determinant_bridge",
        "date": "2026-07-15",
        "status": "Q79_SPINC_DETERMINANT_SHARED_Z64_TWO_TORSION_BRIDGE_CLOSED_ROOT_INDEPENDENT_SAME_SOURCE_HYM_OPEN",
        "inputs": {
            "same_circle_weight2_obstruction": str(SAME_CIRCLE),
            "selected_side_spin_spinc_decision": str(SELECTED_SPINC),
        },
        "checks": checks,
        "finite_data": {
            "source_group": "Z6",
            "target_group": "Z64",
            "hom_generator_images": hom_generator_images,
            "unique_nontrivial_generator_image": central_image,
            "central_map_table": central_map,
            "branch_sign_phase_exponents_mod64": branch_sign_exponents,
            "root_restriction_phase_exponents_mod64": root_restrictions,
            "TT_restriction_phase_exponents_mod64": tt_restriction,
            "root_ratio_restriction_phase_exponents_mod64": root_ratio_restriction,
        },
        "theorem": theorem,
        "claim_tiers": {
            "finite_Z6_to_Z64_central_bridge": "CLOSED_EXACTLY",
            "SpinC_determinant_shared_line_flat_connection_identification": (
                "CLOSED_FOR_THE_UNIQUE_NONTRIVIAL_CENTRAL_MAP"
            ),
            "chi1_vs_chi33_selection_needed_for_determinant": "NO",
            "MTT_same_source_emission_of_central_map": "OPEN",
            "physical_transverse_line_connection_identification": "OPEN",
            "branch_locus_HYM_extension": "OPEN",
            "final_integral_branch_selection": "OPEN",
        },
        "remaining": [
            "derive h as the selected same-source shared-circle holonomy map rather than only the unique compatible map",
            "compare the internal shared line with the physical transverse weight-one line on the selected correspondence base",
            "extend or replace the SpinC sheet carrier through ramification using the selected HYM geometry",
            "retain the final integral/gerbe source gate unless independently promoted",
        ],
        "guardrails": {
            "claims_chi1_or_chi33_uniquely_selected": False,
            "claims_MTT_action_emits_h": False,
            "claims_physical_transverse_line_identified": False,
            "claims_branch_locus_HYM_extension_closed": False,
            "claims_final_integral_branch_selected": False,
            "uses_observed_physics_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Shared-Circle SpinC Determinant Bridge v1

Date: 2026-07-15

## Exact finite theorem

On the executed selected-side branch complement,

```text
H1(X;Z)=Z6.
```

Let `a:Z6->Z2` be the sheet-sign character and embed the unique order-two
group into the selected shared carrier by

```text
iota:Z2->Z64,  iota(1)=32.
```

Then

```text
h=iota o a:Z6->Z64,  h(mu)=32
```

is the unique nontrivial homomorphism from `Z6` to `Z64`. Indeed a generator
image `x` must obey `6x=0 mod 64`, whose only solutions are `0` and `32`.

The two weight-one roots of the TT character obey

```text
chi_1 o h = chi_33 o h = (-1)^a,
chi_2 o h = 1,
chi_32 o h = 1.
```

The first equality is exactly the determinant character of the signed-sheet
SpinC lift. Since flat Hermitian lines with flat unitary connection are
classified by their holonomy characters, for either root `r=1,33`,

```text
h^*L_r ~= L_det
```

as flat lines with connection.

## Why this matters

The determinant bridge is independent of the unresolved `chi_1/chi_33` choice.
Their quotient is invisible not only to TT weight two but also after restriction
to the unique central map. Thus quantum-gravity SpinC cancellation does not need
to choose between the two roots and adds no parameter.

This also explains the division of labor:

```text
weight one restricted to the central image -> determinant sign,
weight two restricted to the central image -> trivial.
```

Strict Spin remains obstructed; the shared-circle channel supplies the
determinant line of the SpinC repair instead.

## Remaining source boundary

The theorem constructs and uniquely characterizes the compatible central map.
It does not yet prove that the selected MTT action emits that map from the same
HYM source, identify the internal shared line with the external transverse
weight-one connection, or extend the carrier through ramification. The input
packet also retains `integral_branch_selected=false`.

Current status:

```text
Q79_SPINC_DETERMINANT_SHARED_Z64_TWO_TORSION_BRIDGE_CLOSED_ROOT_INDEPENDENT_SAME_SOURCE_HYM_OPEN
```
"""

    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed determinant-bridge checks: {failed}")

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
