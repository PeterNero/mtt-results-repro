from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

OBSTRUCTION = ROOT / "certificates" / "same_circle_weight2_bundle_obstruction_certificate.json"
SPIN_PACKET = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "candidate_data"
    / "selected_q79signedsheetspinliftreduction"
    / "q79_signed_sheet_spin_lift_reduction.packet.json"
)
PROTOSPINOR = (
    TEXPAPERS
    / "10 ProtoSpinor"
    / "revised_tex_vnext"
    / "The_Proto_Spinor__Conditional_Spinorial_Closure_and_q79_Interface_v6"
    / "main.tex"
)
TERMINAL_RETURN = (
    TEXPAPERS
    / "18 Theta-Closure & Execution Program"
    / "_md_v3_corrected"
    / "Terminal_Spinorial_Return_Gate_for_Z64_Carry_v1.md"
)
MAJORANA = (
    TEXPAPERS
    / "18 Theta-Closure & Execution Program"
    / "_md_v3_corrected"
    / "Ambient_Z1344_Majorana_and_CP_Compatibility_Check_v1.md"
)

OUT_CERT = ROOT / "certificates" / "protospinor_odd_weight_lift_selector_dichotomy_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "ProtoSpinor_OddWeight_Lift_Selector_or_SpinC_Dichotomy_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def chi(k: int, j: int) -> complex:
    return cmath.exp(2j * math.pi * k * j / 64)


def main() -> None:
    obstruction = load(OBSTRUCTION)
    spin = load(SPIN_PACKET)
    proto = read(PROTOSPINOR)
    terminal = read(TERMINAL_RETURN)
    majorana = read(MAJORANA)

    root_a = 1
    root_b = 33
    weight_visibility: dict[str, dict] = {}
    for weight in range(9):
        ratio_label = (weight * (root_b - root_a)) % 64
        residual = max(
            abs(
                chi(weight * root_b, j)
                / chi(weight * root_a, j)
                - chi(ratio_label, j)
            )
            for j in range(64)
        )
        weight_visibility[str(weight)] = {
            "root_ratio_label": ratio_label,
            "roots_indistinguishable": ratio_label == 0,
            "ratio_identity_residual": residual,
        }

    global_fields = spin["global_spin_contract"]["fields"]
    checks = {
        "weight2_obstruction_theorem_available": (
            obstruction["status"]
            == "WEIGHT2_SAME_CIRCLE_REDUCED_TO_Z2_BUNDLE_OBSTRUCTION_ODD_LIFT_SELECTOR_OPEN"
        ),
        "all_even_weights_are_blind_to_root_ratio": all(
            weight_visibility[str(weight)]["roots_indistinguishable"]
            for weight in [0, 2, 4, 6, 8]
        ),
        "all_tested_odd_weights_detect_chi32": all(
            weight_visibility[str(weight)]["root_ratio_label"] == 32
            for weight in [1, 3, 5, 7]
        ),
        "weight_visibility_identities_exact_numerically": all(
            row["ratio_identity_residual"] < 1.0e-12
            for row in weight_visibility.values()
        ),
        "local_binary_preimage_is_Dic3": (
            spin["binary_spin_theorem"]["Spin3_preimage"]
            == "binary dihedral group Dic_3 of order 12"
        ),
        "local_extension_is_non_split": (
            spin["binary_spin_theorem"]["extension_splits"] is False
        ),
        "central_minus_one_is_generated": (
            spin["binary_spin_theorem"]["checks"]["central_minus_one_generated"] is True
        ),
        "global_spin_contract_has_no_closed_field": (
            spin["global_spin_contract"]["closed_count"] == 0
            and not any(global_fields.values())
        ),
        "revised_protospinor_requires_global_relator_signs": (
            "every relator" in proto
            and "central sign $+1$" in proto
            and "Local braid relations alone do not decide all" in proto
        ),
        "revised_protospinor_separates_SpinC": (
            "A shared $U(1)$ line can instead participate" in proto
            and "distinct theorem" in proto
        ),
        "terminal_parity_does_not_finish_operator_identification": (
            "extract concrete L_fl,MTT block and norm bound" in terminal
        ),
        "majorana_artifact_forbids_reusing_CP_character": (
            "chi_CP = chi_Majorana" in majorana
            and "must not identify" in majorana
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "even_odd_selector_theorem": {
            "statement": (
                "The two roots chi_1 and chi_33 differ by chi_32. In an associated "
                "weight-m representation their ratio is chi_(32m): it is trivial for "
                "even m and chi_32 for odd m. Therefore no even-weight observable, "
                "including TT helicity two, can select the root; any compatible odd-weight "
                "observable can detect the distinction."
            ),
            "finite_table": weight_visibility,
            "continuous_analogue": "the kernel of z -> z^2 is {+1,-1}",
        },
        "bundle_lift_statement": {
            "premise": "a weight-two isomorphism phi_2:L_sh^2 -> L_perp^2 on the correspondence base Z",
            "obstruction": "D=L_sh tensor L_perp^{-1} is an order-two flat line",
            "weight_one_lift_exists_iff": "D is trivial as a flat unitary line system",
            "remaining_sign_after_existence": (
                "a chosen square root of phi_2 still differs from the other by the central sign; "
                "the physical theory must declare whether that sign is gauge, spin-structure data, "
                "or a distinct superselection/initial-condition choice"
            ),
        },
        "strict_Spin_route": {
            "required": [
                "a presentation of the q79 branch-complement fundamental group",
                "positive central sign for every lifted relator, equivalently the relevant w2=0",
                "extension across ramification or replacement by a smooth selected HYM carrier",
                "an explicit identification of the Spin central -1 with the shared-circle chi_32",
                "a selected odd-weight/spinorial source map compatible with the TT weight-two map",
            ],
            "consequence_if_all_hold": (
                "the odd sector can distinguish the two roots and can promote a chosen root "
                "without adding a continuous fitted parameter"
            ),
            "current_status": "OPEN",
        },
        "SpinC_route": {
            "required": [
                "a selected determinant line L_det",
                "c1(L_det) mod 2 equals the signed-sheet w2 obstruction",
                "connection/holonomy compatibility with the order-two mismatch",
                "branch/HYM extension of the combined SpinC carrier",
            ],
            "warning": (
                "The existence of an abstract order-two holonomy character alone does not "
                "prove the integral-lift condition c1(L_det) mod 2=w2."
            ),
            "consequence_if_all_hold": (
                "a combined SpinC carrier may close even when a separate strict Spin root does not"
            ),
            "current_status": "OPEN",
        },
    }

    corpus_result = {
        "same_Z2_representation_type": (
            "The TT root quotient, the central element of Dic_3, the terminal spinorial "
            "return parity, and the ambient self-conjugate Z64 residue are each order-two."
        ),
        "cross_identification_status": (
            "No current source proves that these four order-two objects are the same line, "
            "the same holonomy, or the same central extension class."
        ),
        "strongest_current_status": "EVEN_TT_AMBIGUITY_PROVED_SHARED_Z2_SPIN_SELECTOR_CUTSET_ISOLATED_NO_ROOT_SELECTED",
        "next_single_artifact": "MTT_Selected_q79SheetRelators_SharedCircleCentralIdentification_and_OddSource_v1",
        "must_emit": [
            "the common correspondence base and pullback lines",
            "actual q79 relator central signs or w2 class",
            "the shared-circle differential character including its order-two restriction",
            "the central-kernel comparison map",
            "an odd-weight source/intertwiner or a selected SpinC determinant line",
        ],
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "protospinor_odd_weight_lift_selector_dichotomy",
        "date": "2026-07-15",
        "status": corpus_result["strongest_current_status"],
        "inputs": {
            "same_circle_obstruction": str(OBSTRUCTION),
            "q79_spin_packet": str(SPIN_PACKET),
            "revised_protospinor": str(PROTOSPINOR),
            "terminal_spinorial_return": str(TERMINAL_RETURN),
            "ambient_majorana_check": str(MAJORANA),
        },
        "checks": checks,
        "theorem": theorem,
        "corpus_result": corpus_result,
        "guardrails": {
            "claims_equal_group_order_proves_same_geometric_object": False,
            "claims_local_Dic3_lift_is_global_q79_Spin": False,
            "claims_order2_holonomy_alone_proves_SpinC": False,
            "claims_terminal_return_selects_chi1_or_chi33": False,
            "claims_gravity_TT_can_observe_root_sign": False,
            "adds_fitted_parameter": False,
            "uses_observed_particle_or_GR_data": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# ProtoSpinor Odd-Weight Lift Selector or SpinC Dichotomy v1

Date: 2026-07-15

## The gravity and proto-spinor gates meet at one Z2 problem

The two `Z64` roots of the TT character are `chi_1` and `chi_33`. Their ratio
is `chi_32`. In a weight-`m` representation the ratio becomes

```text
chi_(32m) = 1       for m even,
chi_(32m) = chi_32  for m odd.
```

This proves a sharp division:

```text
TT/helicity 2: cannot see the root sign,
odd/spinorial weight: can see the root sign.
```

Thus the same-circle QG clause and the proto-spinor global-lift clause are not
independent. They share an order-two lifting problem.

## What the local q79 result supplies

The signed sheet action has local binary preimage `Dic_3`, and its central
`-1` is generated. The extension is non-split: lifted transpositions square to
`-1`. This proves that a central sign is genuinely present in the local
spinorial carrier.

It does not prove that this central `-1` is the same geometric object as the
shared-circle `chi_32`. Equal group order is not a bundle or connection
intertwiner. The q79 packet has zero of five global Spin fields closed, and the
revised proto-spinor paper correctly requires all actual branch-complement
relators to close with sign `+1`.

## Strict Spin route

A strict root selection requires all of the following:

1. the actual q79 branch-complement presentation and lifted relator signs;
2. vanishing of the relevant `w2` and extension through ramification;
3. an explicit map identifying Spin central `-1` with shared-circle `chi_32`;
4. an odd-weight/spinorial source map whose square is the computed TT map.

If these hold, the odd sector can distinguish the two roots without adding a
continuous fitted parameter.

## SpinC route

If strict Spin does not close, a combined SpinC carrier is possible only after
selecting a determinant line `L_det` and proving

```text
c1(L_det) mod 2 = w2
```

together with connection, holonomy, branch, and HYM compatibility. An abstract
order-two sign character is not by itself this proof.

## What the other artifacts contribute

The terminal return paper and the ambient Majorana check both exhibit the
correct order-two representation type. They do not select `chi_1` or `chi_33`,
and they do not identify their sign line with the gravity mismatch. The
Majorana paper also correctly forbids reusing the CP character as the neutral
self-conjugate character.

## Exact current frontier

The next artifact is no longer another TT matrix calculation. It must emit:

```text
common pullback base and lines
+ q79 global relator signs/w2
+ shared-circle differential character
+ central-kernel comparison map
+ odd source or SpinC determinant line.
```

Current status:

```text
EVEN_TT_AMBIGUITY_PROVED_SHARED_Z2_SPIN_SELECTOR_CUTSET_ISOLATED_NO_ROOT_SELECTED
```
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
