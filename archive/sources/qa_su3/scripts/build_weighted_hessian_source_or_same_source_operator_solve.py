"""Build the weighted Hessian source / same-source operator solve artifact."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

PROMOTION = DATA / "finite_galerkin_to_smooth_operator_promotion_or_nogo.candidate.json"
PACKET = DATA / "hessian_kernel_central_cocycle_finite_galerkin_candidate.packet.json"
OUTPUT_DATA = DATA / "weighted_hessian_source_or_same_source_operator_solve.candidate.json"
OUTPUT_CERT = CERTS / "weighted_hessian_source_or_same_source_operator_solve_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Weighted_Hessian_Source_or_Same_Source_Operator_Solve_v1.md"


def det2(m: list[list[Fraction]]) -> Fraction:
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def inv2(m: list[list[Fraction]]) -> list[list[Fraction]]:
    d = det2(m)
    return [[m[1][1] / d, -m[0][1] / d], [-m[1][0] / d, m[0][0] / d]]


def serial_fraction(x: Fraction) -> int | str:
    if x.denominator == 1:
        return x.numerator
    return f"{x.numerator}/{x.denominator}"


def weighted_hessian(charges: dict[str, list[int]], weights: dict[str, Fraction]) -> list[list[Fraction]]:
    labels = list(charges)
    return [
        [sum(weights[label] * charges[label][i] * charges[label][j] for label in labels) for j in range(3)]
        for i in range(3)
    ]


def block_inverse_for_decoupled(h: list[list[Fraction]]) -> list[list[Fraction]]:
    base_inv = inv2([[h[0][0], h[0][1]], [h[1][0], h[1][1]]])
    return [
        [base_inv[0][0], base_inv[0][1], Fraction(0)],
        [base_inv[1][0], base_inv[1][1], Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1, 1) / h[2][2]],
    ]


def build() -> tuple[dict[str, object], dict[str, object], str]:
    promotion = json.loads(PROMOTION.read_text(encoding="utf-8"))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    charges: dict[str, list[int]] = packet["twist_projection"]["charge_table"]

    # Product-pair symmetric weights: w(F_i)=w(G_i)=x_i, w(P)=p.
    # H13=H23=0 reduces to:
    #   -5*x1 + 3*x2 - x4 + 3*x5 = 0
    #   -x1 - x2 + x4 + x5 = 0
    # hence x2=3*x1-2*x5 and x4=4*x1-3*x5.
    family = {
        "variables": ["x1", "x3", "x5", "p"],
        "derived": {
            "x2": "3*x1 - 2*x5",
            "x4": "4*x1 - 3*x5",
        },
        "positivity_region": [
            "x1 > 0",
            "x3 > 0",
            "x5 > 0",
            "p > 0",
            "x5 < 4*x1/3",
        ],
        "orthogonality_equations": {
            "H13": "-5*x1 + 3*x2 - x4 + 3*x5 = 0",
            "H23": "-x1 - x2 + x4 + x5 = 0",
        },
        "meaning": "Any source-selected weights in this family keep the c-axis orthogonal to the K1/K2 block, so the central twist selector remains +e3 after positive orientation.",
    }

    examples = {
        "unit_counting_metric": {
            "x1": Fraction(1),
            "x2": Fraction(1),
            "x3": Fraction(1),
            "x4": Fraction(1),
            "x5": Fraction(1),
            "p": Fraction(1),
        },
        "nontrivial_positive_metric": {
            "x1": Fraction(1),
            "x2": Fraction(3, 2),
            "x3": Fraction(7, 5),
            "x4": Fraction(7, 4),
            "x5": Fraction(3, 4),
            "p": Fraction(6, 5),
        },
    }
    example_payload: dict[str, object] = {}
    for name, xs in examples.items():
        weights = {
            "F1": xs["x1"],
            "G1": xs["x1"],
            "F2": xs["x2"],
            "G2": xs["x2"],
            "F3": xs["x3"],
            "G3": xs["x3"],
            "F4": xs["x4"],
            "G4": xs["x4"],
            "F5": xs["x5"],
            "G5": xs["x5"],
            "P": xs["p"],
        }
        h = weighted_hessian(charges, weights)
        g = block_inverse_for_decoupled(h)
        example_payload[name] = {
            "weights": {key: serial_fraction(value) for key, value in weights.items()},
            "H": [[serial_fraction(v) for v in row] for row in h],
            "G": [[serial_fraction(v) for v in row] for row in g],
            "c_axis_decoupled": h[0][2] == 0 and h[1][2] == 0,
            "positive_block_conditions": {
                "H33_positive": h[2][2] > 0,
                "base_det_positive": det2([[h[0][0], h[0][1]], [h[1][0], h[1][1]]]) > 0,
            },
            "Pi_tw_stable": h[0][2] == 0 and h[1][2] == 0 and h[2][2] > 0,
        }

    strong_unit_uniqueness = {
        "assumptions": [
            "product-pair symmetry w(F_i)=w(G_i)",
            "the smooth projected Hessian equals the validated unweighted finite block entry-by-entry",
        ],
        "result": "x1=x2=x3=x4=x5=p=1",
        "meaning": "If the source supplies the already validated block plus pair symmetry, the unit counting metric is forced. This is not an independent source theorem yet.",
    }
    selector_stability_theorem = {
        "statement": "For any positive product-pair symmetric weight metric satisfying H13=H23=0, the central-cocycle selector Pi_tw=+e3 and tau table are unchanged.",
        "proof": [
            "The weighted Hessian is block diagonal between the K1/K2 block and the c-axis.",
            "The retarded Green kernel is therefore also block diagonal.",
            "Any P-annihilator covector has form ell=(a,a,c).",
            "The retarded norm splits into a positive base term in a and a positive c term in c.",
            "The primitive twisted minimizers are +/-e3, and the selected positive orientation gives +e3.",
        ],
        "tau_values": promotion["finite_result_reused"]["tau"],
    }
    candidate = {
        "candidate": "SelectedQaSU3WeightedHessianSourceOrSameSourceOperatorSolve",
        "status": "QA_SU3_WEIGHTED_HESSIAN_SOLVE_SELECTOR_STABLE_SOURCE_ORTHOGONALITY_OPEN",
        "input_promotion_gate": str(PROMOTION.relative_to(ROOT)),
        "key_result": "Full W=I is not necessary for the central-cocycle selector; c-axis orthogonality of the selected weighted Hessian is sufficient.",
        "product_pair_symmetric_family": family,
        "selector_stability_theorem": selector_stability_theorem,
        "strong_unit_uniqueness_if_full_block_selected": strong_unit_uniqueness,
        "examples": example_payload,
        "source_status": {
            "pair_symmetry_source_selected": "OPEN",
            "orthogonality_H13_H23_source_selected": "OPEN",
            "unit_counting_metric_source_selected": "OPEN",
            "same_source_operator_packet_selected": "OPEN",
            "determinant_finite_part_selected": "OPEN",
        },
        "decision": {
            "central_tau_can_be_closed_conditionally_under_orthogonality": True,
            "full_threshold_closure_now": False,
            "reason": "The weighted calculation proves stability of Pi_tw/tau for a broad source-selectable family, but the current source record does not yet select a member of that family or the same-source determinant operator.",
            "next_required_artifact": "Selected_Qa_SU3_CAxis_Orthogonality_Source_or_Weighted_Operator_Packet_v1",
        },
        "what_this_closes": [
            "weighted Hessian family for product-pair symmetric sources",
            "proof that unit weights are stronger than necessary",
            "selector stability theorem for Pi_tw and tau",
            "strong uniqueness of W=I if the full validated block is independently selected",
        ],
        "what_remains_open": [
            "source-selection of product-pair symmetry or H13=H23=0",
            "source-selected weighted metric W",
            "same-source smooth D_E/rho_E/operator packet",
            "determinant finite part",
        ],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3WeightedHessianSourceOrSameSourceOperatorSolve",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "weighted_family_derived": True,
            "unit_weights_not_required_for_tau": True,
            "selector_stability_theorem_built": True,
            "unit_metric_uniqueness_under_full_block_selection": True,
        },
        "what_remains_open": {
            "c_axis_orthogonality_source_selection": True,
            "selected_weight_metric": True,
            "same_source_operator_packet": True,
            "determinant_finite_part": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["decision"]["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = render_note(candidate)
    return candidate, certificate, note


def render_note(candidate: dict[str, object]) -> str:
    return f"""# Selected Qa/SU3 Weighted Hessian Source or Same-Source Operator Solve v1

## Main Discovery

The previous gate asked for `W=I` or an exact selected weight metric.  This pass
shows that full `W=I` is stronger than necessary for the central-cocycle
selector.

What is sufficient is:

```text
H13 = H23 = 0
```

for the selected weighted Hessian.  Then the `c` axis decouples from the
`K1/K2` block, the Green kernel also decouples, and the primitive twisted
selector remains:

```text
Pi_tw = +e3
```

so the existing `tau` table survives.

## Product-Pair Symmetric Family

Assume:

```text
w(F_i)=w(G_i)=x_i,  w(P)=p
```

Then `H13=H23=0` is equivalent to:

```text
x2 = 3*x1 - 2*x5
x4 = 4*x1 - 3*x5
x1,x3,x5,p > 0
x5 < 4*x1/3
```

This is a broad positive family.  Unit counting weights are one member, not the
only member.

## Selector Stability Theorem

{candidate["selector_stability_theorem"]["statement"]}

The proof is now finite and exact: the weighted Hessian is block diagonal
between `K1/K2` and `c`, so the retarded norm splits.  A `P`-annihilator has
form `ell=(a,a,c)`, and the primitive twisted minimizers are `+/-e3`.  Positive
orientation selects `+e3`.

## Stronger Unit Result

If, in addition, a future source proves that the smooth projected Hessian equals
the already validated block entry-by-entry, then product-pair symmetry forces:

```text
x1=x2=x3=x4=x5=p=1
```

So `W=I` is unique under that stronger assumption.

## Current Status

```text
source-selected H13=H23=0: open
source-selected W: open
same-source operator packet: open
determinant finite part: open
full Qa/SU3 closure: no
```

Next artifact:

```text
{candidate["decision"]["next_required_artifact"]}
```
"""


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
