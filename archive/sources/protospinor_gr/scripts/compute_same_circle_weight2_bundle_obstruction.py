from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

HELICITY = ROOT / "certificates" / "tt_helicity2_z64_carrier_functor_certificate.json"
METRIC = ROOT / "certificates" / "world_in_world_z64_metric_source_map_certificate.json"
SPIN_PACKET = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "candidate_data"
    / "selected_q79signedsheetspinliftreduction"
    / "q79_signed_sheet_spin_lift_reduction.packet.json"
)
TRACE_PACKET = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "candidate_data"
    / "selected_q79tracesplitclncarrierandworldinworldbridge"
    / "q79_trace_split_cln_carrier_and_bridge_cutset.packet.json"
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

OUT_CERT = ROOT / "certificates" / "same_circle_weight2_bundle_obstruction_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Same_Circle_Weight2_Bundle_Obstruction_and_Z2_Lift_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def chi(n: int, k: int, j: int) -> complex:
    return cmath.exp(2j * math.pi * k * j / n)


def order(n: int, k: int) -> int:
    return n // math.gcd(n, k)


def main() -> None:
    helicity = load(HELICITY)
    metric = load(METRIC)
    spin = load(SPIN_PACKET)
    trace = load(TRACE_PACKET)
    terminal = read(TERMINAL_RETURN)
    majorana = read(MAJORANA)

    n = 64
    k_tt = 2
    kernel = [j for j in range(n) if (k_tt * j) % n == 0]
    square_root_labels = [k for k in range(n) if (2 * k) % n == k_tt]
    root_ratio_label = (square_root_labels[1] - square_root_labels[0]) % n

    factorization_residual = max(
        abs(chi(64, 2, j) - chi(32, 1, j % 32)) for j in range(64)
    )
    weight2_kernel_residual = max(
        abs(chi(64, 2, j + 32) - chi(64, 2, j)) for j in range(64)
    )
    weight1_sign_residual = max(
        abs(chi(64, 1, j + 32) + chi(64, 1, j)) for j in range(64)
    )
    root_square_residual = max(
        abs(chi(64, root, j) ** 2 - chi(64, 2, j))
        for root in square_root_labels
        for j in range(64)
    )
    root_ratio_residual = max(
        abs(
            chi(64, square_root_labels[1], j)
            / chi(64, square_root_labels[0], j)
            - chi(64, root_ratio_label, j)
        )
        for j in range(64)
    )

    crt_order_two = {
        "Z64": 672 % 64,
        "Z7": 672 % 7,
        "Z3": 672 % 3,
    }

    checks = {
        "helicity_functor_uses_weight2": (
            helicity["numerical_checks"]["character_label_k"] == 2
        ),
        "helicity_character_has_order32": (
            helicity["numerical_checks"]["character_order"] == 32
        ),
        "actual_DG_rows_land_in_weight2_plane": (
            metric["checks"]["metric_Bstar_support_is_exact_plane"] is True
        ),
        "weight2_kernel_is_exactly_order2": kernel == [0, 32],
        "weight2_factors_through_Z32": factorization_residual < 1.0e-12,
        "weight2_cannot_distinguish_two_lifts": weight2_kernel_residual < 1.0e-12,
        "weight1_distinguishes_two_lifts_by_sign": weight1_sign_residual < 1.0e-12,
        "weight2_has_exactly_two_character_roots": square_root_labels == [1, 33],
        "both_character_roots_square_to_weight2": root_square_residual < 1.0e-12,
        "root_ratio_is_order2_character": (
            root_ratio_label == 32 and order(64, root_ratio_label) == 2
        ),
        "root_ratio_identity_checked": root_ratio_residual < 1.0e-12,
        "q79_shared_line_holonomy_not_selected": (
            "not selected here"
            in trace["exact_q79_carrier_theorem"]["shared_circle_statement"]
        ),
        "q79_global_spin_lift_still_open": (
            spin["global_spin_contract"]["global_Spin_lift_closed"] is False
        ),
        "terminal_return_supplies_order2_type_not_root": (
            "terminal selected residue is a spinorial return parity" in terminal
            and "extract concrete L_fl,MTT block and norm bound" in terminal
        ),
        "ambient_order2_is_Z64_label32_under_CRT": (
            crt_order_two == {"Z64": 32, "Z7": 0, "Z3": 0}
            and "k = 672" in majorana
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "common_base_typing": {
            "base": "a correspondence base Z carrying maps p_sh:Z->X_q79 and p_perp:Z->B_perp",
            "shared_line": "L_sh=p_sh^* L_shared with its pulled-back unitary connection",
            "transverse_line": "L_perp=p_perp^* H_{+1}, the complex weight-one transverse-frame line",
            "positive_helicity_TT_line": "H_{+2}=L_perp tensor L_perp (up to the stated helicity sign convention)",
            "warning": "Without Z and both pullbacks, an internal line and an external helicity line cannot be compared globally.",
        },
        "weight2_equivalence": {
            "statement": (
                "A connection-preserving same-circle identification visible to the TT sector "
                "is an isomorphism L_sh^2 ~= L_perp^2. With D=L_sh tensor L_perp^{-1}, "
                "this exists if and only if D^2 is connection-trivial."
            ),
            "mismatch_line": "D=L_sh tensor L_perp^{-1}",
            "equivalent_obstruction": "[D] belongs to the order-two flat unitary line systems H^1(Z;Z2)",
            "curvature_consequence": "F_D=0, hence F_sh=F_perp",
            "holonomy_consequence": "Hol_D(gamma) is in {+1,-1} for every loop gamma",
            "chern_consequence": "2(c1(L_sh)-c1(L_perp))=0 in H^2(Z;Z)",
            "important_nonconverse": (
                "The Chern equation alone does not prove connection-preserving equality; "
                "flat holonomy data must also match."
            ),
            "unique_root_condition": "H^1(Z;Z2)=0, or an independently selected odd-weight trivialization of D",
        },
        "local_vs_global": {
            "fixed_wave_direction": (
                "The existing plus/cross construction is a valid local or fixed-direction trivialization."
            ),
            "global_helicity_bundle": (
                "Over the momentum-direction sphere, helicity h is a generally nontrivial line bundle; "
                "with convention C=-2h, helicity +2 has Chern number -4."
            ),
            "external_primary_source": "https://arxiv.org/abs/2407.03494",
        },
    }

    corpus_decision = {
        "closed_now": [
            "the exact finite kernel of the Z64 weight-two action is {0,32}",
            "the TT character factors through Z32",
            "the only two Z64 character square roots are chi_1 and chi_33",
            "their quotient is the order-two character chi_32",
            "the global same-circle problem is exactly an order-two flat mismatch after proper pullback typing",
            "the terminal-return and Majorana artifacts contain the same order-two representation type",
        ],
        "not_closed": [
            "a selected correspondence base and maps relating internal q79 and external transverse-frame data",
            "the differential Chern/holonomy equality L_sh^2 ~= L_perp^2 on that base",
            "selection of chi_1 versus chi_33 by an odd-weight or spinorial observable",
            "identification of the terminal/Majorana chi_32 with the gravity mismatch line D",
            "the q79 global Spin relator signs or a valid SpinC determinant-line cancellation",
            "branch-locus and selected HYM connection compatibility",
        ],
        "current_status": "WEIGHT2_SAME_CIRCLE_REDUCED_TO_Z2_BUNDLE_OBSTRUCTION_ODD_LIFT_SELECTOR_OPEN",
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "same_circle_weight2_bundle_obstruction",
        "date": "2026-07-15",
        "status": corpus_decision["current_status"],
        "inputs": {
            "helicity_functor": str(HELICITY),
            "metric_source": str(METRIC),
            "q79_spin_packet": str(SPIN_PACKET),
            "q79_trace_packet": str(TRACE_PACKET),
            "terminal_spinorial_return": str(TERMINAL_RETURN),
            "ambient_majorana_check": str(MAJORANA),
        },
        "checks": checks,
        "finite_Z64_result": {
            "N": n,
            "TT_character_label": k_tt,
            "TT_character_order": order(n, k_tt),
            "kernel": kernel,
            "square_root_character_labels": square_root_labels,
            "root_ratio_character_label": root_ratio_label,
            "root_ratio_order": order(n, root_ratio_label),
            "factorization_residual": factorization_residual,
            "weight2_kernel_residual": weight2_kernel_residual,
            "weight1_sign_residual": weight1_sign_residual,
            "root_square_residual": root_square_residual,
            "root_ratio_residual": root_ratio_residual,
            "ambient_Z1344_order2_CRT_residues": crt_order_two,
        },
        "theorem": theorem,
        "corpus_decision": corpus_decision,
        "guardrails": {
            "claims_internal_and_external_lines_already_live_on_same_base": False,
            "claims_weight2_data_selects_a_unique_weight1_root": False,
            "claims_terminal_spinorial_return_is_already_the_gravity_mismatch": False,
            "claims_global_q79_Spin_or_SpinC_closed": False,
            "claims_global_helicity_bundle_is_trivial": False,
            "uses_observed_GR_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# Same-Circle Weight-2 Bundle Obstruction and Z2 Lift Theorem v1

Date: 2026-07-15

## Result

The phrase "the same circle" has to be typed before it can be proved. Let `Z`
be a correspondence base with maps to the internal q79 base and to the physical
transverse-frame base. Pull both lines to `Z`:

```text
L_sh   = p_sh^* L_shared,
L_perp = p_perp^* H_(+1).
```

The positive-helicity TT line is the weight-two line `L_perp^2`. Therefore the
TT sector can identify the two circle actions precisely when

```text
L_sh^2 ~= L_perp^2
```

as unitary line bundles with connection. With

```text
D = L_sh tensor L_perp^(-1),
```

this is equivalent to `D^2` being connection-trivial. Thus `D` is an
order-two flat line system:

```text
[D] in H^1(Z;Z2),
Hol_D(gamma) in {+1,-1}.
```

It follows that

```text
2(c1(L_sh)-c1(L_perp))=0,
F_sh=F_perp.
```

The Chern equation alone is not enough: connection-preserving equality also
requires the flat holonomies to agree. A unique weight-one root follows if
`H^1(Z;Z2)=0` or if an independent odd-weight/spinorial observable trivializes
`D`.

## Exact finite calculation

For `Z64`, the TT representation is

```text
chi_2(j)=exp(2*pi*i*2*j/64).
```

Its exact kernel and order are

```text
ker(chi_2)={0,32},
ord(chi_2)=32.
```

Hence the spin-2 action factors through `Z32`. It cannot distinguish `j` from
`j+32`. The two and only two character square roots are

```text
chi_1^2=chi_2,
chi_33^2=chi_2,
chi_33/chi_1=chi_32,
ord(chi_32)=2.
```

Weight one changes sign under `j -> j+32`; weight two does not. No calculation
using only the TT representation can choose between `chi_1` and `chi_33`.

## Corpus comparison

The terminal spinorial-return paper supplies an order-two parity type, and the
ambient `Z1344` Majorana check identifies its nontrivial self-conjugate label
`672`, whose CRT residues are `(32,0,0)` in `Z64 x Z7 x Z3`. These are exact
matches to the representation type `chi_32`.

They do not yet prove that this parity is the gravity mismatch line `D`, and
they do not choose `chi_1` rather than `chi_33`. The terminal paper still leaves
its concrete MTT operator extraction open; the q79 packet still leaves every
global Spin/SpinC contract field false.

## Local and global scope

The existing plus/cross map is valid at a fixed propagation direction. It must
not be silently promoted to a global polarization frame. Over the sphere of
momentum directions, a helicity-`h` line has first Chern number `C=-2h` in the
convention of Palmerduca and Qin; helicity `+2` therefore has `C=-4`. See the
primary result [Helicity is a topological invariant of massless particles](https://arxiv.org/abs/2407.03494).

## What advanced

The first clause of the QG compatibility theorem is no longer the unstructured
request "prove the circles are the same." It is now the following finite
cutset:

1. construct the correspondence base `Z` and both pullbacks;
2. compute the differential line class and prove `D^2` is trivial;
3. use an odd-weight/spinorial source to decide whether `D` itself is trivial;
4. extend that decision through the q79 branch locus with the selected HYM
   connection.

Current status:

```text
WEIGHT2_SAME_CIRCLE_REDUCED_TO_Z2_BUNDLE_OBSTRUCTION_ODD_LIFT_SELECTOR_OPEN
```
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
