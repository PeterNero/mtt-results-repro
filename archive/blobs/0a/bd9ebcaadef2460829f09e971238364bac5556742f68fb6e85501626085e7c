from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

SHARED_BRIDGE = ROOT / "certificates" / "q79_shared_circle_spinc_determinant_bridge_certificate.json"
SELECTED_SPINC = ROOT / "certificates" / "q79_selected_side_spin_spinc_decision_certificate.json"
Q79_TRACE_PACKET = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "candidate_data"
    / "selected_q79tracesplitclncarrierandworldinworldbridge"
    / "q79_trace_split_cln_carrier_and_bridge_cutset.packet.json"
)

OUT_CERT = ROOT / "certificates" / "q79_shared_z64_same_source_monodromy_map_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "q79_Shared_Z64_Same_Source_Monodromy_Map_v1.md"


Permutation = tuple[int, int, int]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(3))  # type: ignore[return-value]


def parity(permutation: Permutation) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return inversions % 2


def cycle_type(permutation: Permutation) -> str:
    if permutation == (0, 1, 2):
        return "identity"
    if parity(permutation) == 1:
        return "transposition"
    return "three_cycle"


def main() -> None:
    bridge = load(SHARED_BRIDGE)
    selected_spinc = load(SELECTED_SPINC)
    trace_packet = load(Q79_TRACE_PACKET)

    modulus = 64
    central_label = bridge["finite_data"]["unique_nontrivial_generator_image"]
    roots = [1, 33]
    permutations = list(itertools.permutations(range(3)))

    monodromy_map = {
        "".join(str(entry) for entry in permutation): central_label * parity(permutation) % modulus
        for permutation in permutations
    }
    homomorphism_check = all(
        monodromy_map["".join(str(entry) for entry in compose(left, right))]
        == (
            monodromy_map["".join(str(entry) for entry in left)]
            + monodromy_map["".join(str(entry) for entry in right)]
        )
        % modulus
        for left in permutations
        for right in permutations
    )

    class_table = []
    for permutation in permutations:
        key = "".join(str(entry) for entry in permutation)
        image = monodromy_map[key]
        class_table.append(
            {
                "permutation": list(permutation),
                "cycle_type": cycle_type(permutation),
                "parity": parity(permutation),
                "Z64_image": image,
                "chi1_phase_exponent_mod64": image % modulus,
                "chi33_phase_exponent_mod64": (33 * image) % modulus,
                "chi2_phase_exponent_mod64": (2 * image) % modulus,
            }
        )

    order_two_images = [value for value in range(modulus) if (2 * value) % modulus == 0]
    presentation_homomorphisms = []
    for image_s in order_two_images:
        for image_t in order_two_images:
            if (3 * (image_s + image_t)) % modulus == 0:
                presentation_homomorphisms.append([image_s, image_t])

    transposition_rows = [row for row in class_table if row["cycle_type"] == "transposition"]
    three_cycle_rows = [row for row in class_table if row["cycle_type"] == "three_cycle"]
    expected_sign_exponent = lambda row: 32 * row["parity"]

    checks = {
        "q79_cover_has_selected_S3_monodromy": (
            selected_spinc["SpinC_theorem"]["projection"]
            == "the signed-sheet S3 representation rho_plus"
        ),
        "same_shared_line_twists_all_q79_lanes": (
            "same rank-one local-system factor L_shared twists all three lanes"
            in trace_packet["exact_q79_carrier_theorem"]["shared_circle_statement"]
        ),
        "shared_Z64_half_turn_is_32": central_label == 32,
        "all_six_S3_elements_enumerated": len(class_table) == 6,
        "map_is_a_group_homomorphism": homomorphism_check,
        "all_transpositions_map_to_32": all(
            row["Z64_image"] == 32 for row in transposition_rows
        ),
        "all_three_cycles_map_to_zero": all(
            row["Z64_image"] == 0 for row in three_cycle_rows
        ),
        "S3_to_Z64_homomorphisms_are_trivial_or_unique_sign_map": (
            presentation_homomorphisms == [[0, 0], [32, 32]]
        ),
        "chi1_composite_is_sheet_sign": all(
            row["chi1_phase_exponent_mod64"] == expected_sign_exponent(row)
            for row in class_table
        ),
        "chi33_composite_is_sheet_sign": all(
            row["chi33_phase_exponent_mod64"] == expected_sign_exponent(row)
            for row in class_table
        ),
        "chi2_composite_is_trivial": all(
            row["chi2_phase_exponent_mod64"] == 0 for row in class_table
        ),
        "SpinC_determinant_is_sheet_sign": (
            selected_spinc["SpinC_theorem"]["determinant_character"]
            == "z^2=sign(sheet permutation)"
        ),
        "finite_bridge_added_no_parameter": (
            bridge["guardrails"]["adds_fitted_parameter"] is False
        ),
        "final_integral_branch_not_promoted": (
            selected_spinc["guardrails"]["claims_integral_gerbe_branch_selected"]
            is False
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "name": "SelectedFiniteQ79SharedZ64MonodromySourceTheorem",
        "source_objects": [
            "the selected q79 signed-sheet monodromy rho_sheet:pi1(X)->S3",
            "the exact shared-circle terminal half-turn x5=32 in Z64",
        ],
        "emitted_map": "h_S3:S3->Z64, h_S3(sigma)=32*parity(sigma)",
        "uniqueness": (
            "The S3 presentation s^2=t^2=(st)^3=1 has only the Z64 image pairs "
            "(0,0) and (32,32). Requiring the nontrivial SpinC determinant excludes "
            "the trivial pair, so h_S3 is forced."
        ),
        "branch_complement_map": "h_X=h_S3 o rho_sheet:pi1(X)->Z64",
        "determinant_identity": (
            "For either shared root r in {1,33}, chi_r o h_X equals the SpinC "
            "determinant sheet-sign character; chi_2 o h_X is trivial."
        ),
        "parameter_count": 0,
        "selection_scope": (
            "This closes the finite monodromy/holonomy source map once the selected "
            "q79 SpinC carrier and exact shared Z64 branch are required to be the same "
            "carrier. It does not derive the differential HYM connection or the "
            "external transverse-frame identification."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "q79_shared_z64_same_source_monodromy_map",
        "date": "2026-07-15",
        "status": "Q79_SHARED_Z64_FINITE_MONODROMY_SOURCE_MAP_CLOSED_UNIQUE_HYM_TRANSVERSE_ACTION_OPEN",
        "inputs": {
            "shared_determinant_bridge": str(SHARED_BRIDGE),
            "selected_side_spin_spinc": str(SELECTED_SPINC),
            "q79_trace_shared_line_packet": str(Q79_TRACE_PACKET),
        },
        "checks": checks,
        "finite_data": {
            "Z64_order_two_images": order_two_images,
            "S3_presentation_homomorphism_generator_images": presentation_homomorphisms,
            "class_table": class_table,
        },
        "theorem": theorem,
        "claim_tiers": {
            "finite_same_source_q79_to_Z64_monodromy_map": "CLOSED_UNIQUE",
            "SpinC_determinant_shared_character_identity": "CLOSED_ROOT_INDEPENDENT",
            "differential_HYM_emission_of_shared_connection": "OPEN",
            "physical_transverse_frame_connection_identification": "OPEN",
            "selected_action_uses_combined_SpinC_metric_carrier": "OPEN",
            "ramification_extension": "OPEN",
            "final_integral_branch_selection": "OPEN",
        },
        "guardrails": {
            "claims_full_differential_same_source_theorem": False,
            "claims_external_transverse_frame_identified": False,
            "claims_selected_action_closed": False,
            "claims_HYM_extension_closed": False,
            "claims_final_integral_branch_selected": False,
            "uses_observed_physics_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Shared-Z64 Same-Source Monodromy Map v1

Date: 2026-07-15

## Selected finite inputs

Two previously separate selected objects now meet:

```text
rho_sheet:pi1(X)->S3                 q79 sheet monodromy,
x5=32 in Z64                         shared-circle terminal half-turn.
```

The q79 trace packet states that the same rank-one `L_shared` factor twists all
three sheet lanes. Define

```text
h_S3(sigma)=32 parity(sigma) mod 64.
```

This is a homomorphism. It maps every transposition to `32`, every three-cycle
to `0`, and emits the branch-complement holonomy

```text
h_X=h_S3 o rho_sheet:pi1(X)->Z64.
```

## Exact uniqueness

For the presentation `S3=<s,t | s^2=t^2=(st)^3=1>`, a homomorphism to the
abelian group `Z64` must send both generators to order-two elements. Direct
enumeration gives only

```text
(h(s),h(t))=(0,0) or (32,32).
```

The SpinC determinant is the nontrivial sheet-sign character, so the trivial
map cannot supply it. The nontrivial map is therefore forced; it is not a new
binary choice or continuous parameter.

For both admissible shared-circle roots,

```text
chi_1 o h_X = chi_33 o h_X = det(SpinC)=sheet sign,
chi_2 o h_X = 1.
```

This closes the finite same-source monodromy/holonomy map and preserves the
root-independent determinant result.

## Remaining differential theorem

The result is finite and topological. It does not yet emit a smooth unitary
connection from the selected HYM solution, identify that connection with the
external transverse-frame line, prove that the selected action uses the
combined SpinC metric carrier, or extend through ramification. The final
integral/gerbe branch remains unselected.

Current status:

```text
Q79_SHARED_Z64_FINITE_MONODROMY_SOURCE_MAP_CLOSED_UNIQUE_HYM_TRANSVERSE_ACTION_OPEN
```
"""

    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed same-source monodromy checks: {failed}")

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
