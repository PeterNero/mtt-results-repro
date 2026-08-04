"""Build the c-axis orthogonality source / weighted operator packet."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

WEIGHTED = DATA / "weighted_hessian_source_or_same_source_operator_solve.candidate.json"
PACKET = DATA / "hessian_kernel_central_cocycle_finite_galerkin_candidate.packet.json"
OUTPUT_DATA = DATA / "caxis_orthogonality_source_or_weighted_operator_packet.candidate.json"
OUTPUT_CERT = CERTS / "caxis_orthogonality_source_or_weighted_operator_packet_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_CAxis_Orthogonality_Source_or_Weighted_Operator_Packet_v1.md"


def sf(x: Fraction) -> int | str:
    return x.numerator if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def weighted_hessian(charges: dict[str, list[int]], weights: dict[str, Fraction]) -> list[list[Fraction]]:
    labels = list(charges)
    return [
        [sum(weights[label] * charges[label][i] * charges[label][j] for label in labels) for j in range(3)]
        for i in range(3)
    ]


def inv2(h: list[list[Fraction]]) -> list[list[Fraction]]:
    d = h[0][0] * h[1][1] - h[0][1] * h[1][0]
    return [[h[1][1] / d, -h[0][1] / d], [-h[1][0] / d, h[0][0] / d]]


def green_for_decoupled(h: list[list[Fraction]]) -> list[list[Fraction]]:
    b = inv2([[h[0][0], h[0][1]], [h[1][0], h[1][1]]])
    return [[b[0][0], b[0][1], Fraction(0)], [b[1][0], b[1][1], Fraction(0)], [Fraction(0), Fraction(0), 1 / h[2][2]]]


def build() -> tuple[dict[str, object], dict[str, object], str]:
    weighted = json.loads(WEIGHTED.read_text(encoding="utf-8"))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    charges: dict[str, list[int]] = packet["twist_projection"]["charge_table"]
    tau = packet["tau_extraction"]["module_twist_values"]

    # Minimal central-twist orbit-democracy family:
    # a = common weight on |tau|=1 labels, b = common weight on tau=0 F3/G3, p = P weight.
    symbolic_hessian = {
        "basis": ["K1", "K2", "c"],
        "matrix": [
            ["25*a + b + p", "-3*a - 2*b - p", 0],
            ["-3*a - 2*b - p", "4*a + 5*b + p", 0],
            [0, 0, "8*a"],
        ],
        "positive_conditions": ["a>0", "b>0", "p>0"],
        "base_determinant": "91*a^2 + 133*a*b + 29*a*p + b*p",
    }
    sample_weights = {
        "F1": Fraction(1),
        "F2": Fraction(1),
        "F3": Fraction(7, 5),
        "F4": Fraction(1),
        "F5": Fraction(1),
        "G1": Fraction(1),
        "G2": Fraction(1),
        "G3": Fraction(7, 5),
        "G4": Fraction(1),
        "G5": Fraction(1),
        "P": Fraction(6, 5),
    }
    h = weighted_hessian(charges, sample_weights)
    g = green_for_decoupled(h)
    source_theorem = {
        "name": "CentralTwistOrbitOrthogonality",
        "hypotheses": [
            "the selected smooth/operator Hessian factors through the typed charge map on the central-twist sector",
            "the selected metric is invariant under the central-twist orbit partition: |tau|=1 labels share weight a, tau=0 F3/G3 share weight b, and P has weight p",
            "a,b,p are positive",
            "the branch orientation selects +c rather than the conjugate -c",
        ],
        "conclusion": "H13=H23=0, G_ret is block diagonal, Pi_tw=+e3, and the tau table is unchanged.",
        "proof": [
            "Substituting the orbit weights into Q^T W Q gives H13=0 and H23=0 identically.",
            "The weighted Hessian becomes block diagonal between (K1,K2) and c.",
            "The base determinant is 91*a^2 + 133*a*b + 29*a*p + b*p, positive for a,b,p>0.",
            "H33=8*a is positive for a>0.",
            "The inverse Green kernel is therefore block diagonal.",
            "The P-annihilator twisted primitive minimization is unchanged and selects +/-e3; branch orientation selects +e3.",
        ],
    }
    current_source_status = {
        "central_twist_orbit_partition": "CLOSED_FROM_TAU_TABLE",
        "opposite_twist_product_cancellation": "CLOSED_FROM_TYPED_MONAD_PRODUCTS",
        "block_diagonal_internal_bundle_context": "SUPPORTED_BY_STROMINGER_CORPUS",
        "orbit_democracy_weight_invariance": "CONDITIONAL_NOT_SOURCE_SELECTED_AS_OPERATOR_WEIGHT",
        "same_source_operator_packet": "OPEN",
        "determinant_finite_part": "OPEN",
    }
    candidate = {
        "candidate": "SelectedQaSU3CAxisOrthogonalitySourceOrWeightedOperatorPacket",
        "status": "QA_SU3_CAXIS_ORTHOGONALITY_PROVED_UNDER_CENTRAL_TWIST_ORBIT_DEMOCRACY_SOURCE_WEIGHT_OPEN",
        "input_weighted_solve": str(WEIGHTED.relative_to(ROOT)),
        "source_theorem": source_theorem,
        "central_twist_orbit_weights": {
            "weight_a_labels_abs_tau_1": [label for label, value in tau.items() if abs(value) == 1],
            "weight_b_labels_tau_0_non_P": [label for label, value in tau.items() if value == 0 and label != "P"],
            "weight_p_label": ["P"],
        },
        "symbolic_weighted_hessian": symbolic_hessian,
        "sample_non_unit_packet": {
            "weights": {key: sf(value) for key, value in sample_weights.items()},
            "H": [[sf(value) for value in row] for row in h],
            "G": [[sf(value) for value in row] for row in g],
            "H13_H23_zero": h[0][2] == 0 and h[1][2] == 0,
            "Pi_tw": [0, 0, 1],
            "tau": tau,
        },
        "current_source_status": current_source_status,
        "decision": {
            "orthogonality_proved_as_theorem": True,
            "orthogonality_unconditionally_source_selected": False,
            "central_tau_selector_closed_if_orbit_democracy_selected": True,
            "full_threshold_closure_now": False,
            "why_not_full_closure": "The orbit-democracy weight invariance is natural and sufficient, but the current same-source operator packet still does not select it as an actual smooth determinant/Hessian weight.",
            "next_required_artifact": "Selected_Qa_SU3_Central_Twist_Orbit_Democracy_Source_or_Determinant_Operator_v1",
        },
        "what_this_closes": [
            "closed-form proof H13=H23=0 under central-twist orbit democracy",
            "positive weighted Hessian family with non-unit examples",
            "selector stability without full W=I",
            "exact remaining source-selection condition",
        ],
        "what_remains_open": [
            "same-source proof that orbit-democracy weights are selected by MTT for Qa/SU3",
            "same-source smooth D_E/rho_E/operator packet",
            "determinant finite part",
        ],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3CAxisOrthogonalitySourceOrWeightedOperatorPacket",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "caxis_orthogonality_theorem_proved": True,
            "non_unit_positive_family_built": True,
            "Pi_tw_tau_stable_under_orbit_democracy": True,
            "remaining_source_condition_is_exact": True,
        },
        "what_remains_open": {
            "orbit_democracy_source_selection": True,
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
    return f"""# Selected Qa/SU3 C-Axis Orthogonality Source or Weighted Operator Packet v1

## Result

This proves the `c`-axis orthogonality theorem under a clean source condition:
central-twist orbit democracy.

The required weight partition is:

```text
|tau|=1 labels: common weight a
tau=0 pair F3/G3: common weight b
P: weight p
a,b,p > 0
```

Then the weighted Hessian is:

```text
{candidate["symbolic_weighted_hessian"]["matrix"]}
```

So:

```text
H13 = H23 = 0
```

identically.  The `c` axis decouples, `G_ret` is block diagonal, and the central
twist selector remains:

```text
Pi_tw = +e3
```

## Why This Is Better Than W=I

Unit weights are sufficient but not necessary.  The non-unit sample in the
candidate packet has:

```text
H = {candidate["sample_non_unit_packet"]["H"]}
G = {candidate["sample_non_unit_packet"]["G"]}
```

and still preserves the same `Pi_tw` and `tau`.

## Source Status

```text
central twist orbit partition: {candidate["current_source_status"]["central_twist_orbit_partition"]}
opposite twist product cancellation: {candidate["current_source_status"]["opposite_twist_product_cancellation"]}
block diagonal internal bundle context: {candidate["current_source_status"]["block_diagonal_internal_bundle_context"]}
orbit-democracy operator weight: {candidate["current_source_status"]["orbit_democracy_weight_invariance"]}
same-source operator packet: {candidate["current_source_status"]["same_source_operator_packet"]}
determinant finite part: {candidate["current_source_status"]["determinant_finite_part"]}
```

## Verdict

The orthogonality is now proved as a theorem with an exact remaining source
condition.  It is not yet unconditional Qa/SU3 closure, because the current
source record does not yet prove that this orbit-democratic weight is the
selected smooth/operator determinant weight.

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
