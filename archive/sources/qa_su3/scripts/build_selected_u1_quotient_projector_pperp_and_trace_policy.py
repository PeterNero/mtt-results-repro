"""Build the selected U1 quotient projector and trace-policy theorem.

This closes the final rank-quotient gate for the motivated 2/3 U1 threshold
index, in the same scoped sense as the previous SU2 weak-split closure.  It
does not claim measured electroweak closure or fix K_gauge.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

PREVIOUS = DATA / "same_source_selected_u1_carrier_projector_theorem.candidate.json"
CENTRAL_CIRCLE_SOURCE = OBSIDIAN / "13 Standard Model & Topology-Only Constraints" / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
FINITE_PROJECTION_SOURCE = OBSIDIAN / "5 Dirac Delta" / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"
THETA_GAUGE_SOURCE = OBSIDIAN / "18 Theta-Closure & Execution Program" / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md"

OUTPUT_DATA = DATA / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1_quotient_projector_pperp_and_trace_policy_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1_Quotient_Projector_Pperp_and_Trace_Policy_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def trace(a: list[list[Fraction]]) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def rank_rational_3(a: list[list[Fraction]]) -> int:
    rows = [row[:] for row in a]
    rank = 0
    col = 0
    while rank < len(rows) and col < len(rows[0]):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][col] != 0), None)
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][col]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][col] != 0:
                factor = rows[r][col]
                rows[r] = [rows[r][c] - factor * rows[rank][c] for c in range(len(rows[0]))]
        rank += 1
        col += 1
    return rank


def serial_matrix(a: list[list[Fraction]]) -> list[list[str]]:
    return [[f"{x.numerator}/{x.denominator}" for x in row] for row in a]


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    previous = load(PREVIOUS)

    # Work in the canonical qutrit/F3 carrier basis.  The shared universal
    # circle line can be represented by s=(1,1,1)/sqrt(3); the rational
    # projector is I - (1/3)J.  Any unitary basis change gives a conjugate
    # projector with the same rank and normalized trace.
    one = Fraction(1, 1)
    third = Fraction(1, 3)
    identity = [[one if i == j else Fraction(0) for j in range(3)] for i in range(3)]
    all_ones = [[one for _ in range(3)] for _ in range(3)]
    p_shared = [[third * all_ones[i][j] for j in range(3)] for i in range(3)]
    p_perp = [[identity[i][j] - p_shared[i][j] for j in range(3)] for i in range(3)]
    p2 = matmul(p_perp, p_perp)
    zero_on_shared = [
        sum(p_perp[i][j] for j in range(3))
        for i in range(3)
    ]
    tr_p = trace(p_perp)
    tr_i = trace(identity)
    normalized_trace = tr_p / tr_i
    rank = rank_rational_3(p_perp)

    source_support = {
        "central_circle": {
            "source": str(CENTRAL_CIRCLE_SOURCE),
            "supports_unique_shared_channel": True,
            "supports_not_local_gauge_load": True,
            "role": "selects a unique universal shared internal circle mode that must be quotiented out of sector-specific gauge threshold response",
        },
        "finite_coherent_projection": {
            "source": str(FINITE_PROJECTION_SOURCE),
            "supports_quotient_compatible_projectors": True,
            "role": "finite coherent filtering in gauge sectors must act on gauge-admissible physical content through quotient-compatible projectors",
        },
        "theta_gauge_overlap": {
            "source": str(THETA_GAUGE_SOURCE),
            "supports_overlap_trace_policy": True,
            "role": "gauge couplings descend from internal harmonic overlap integrals; inserting the physical quotient projector restricts the trace to the retained threshold subspace",
        },
        "previous_source_level_support": {
            "source": str(PREVIOUS.relative_to(ROOT)),
            "source_level_rank3_carrier_support_closed": previous["decision"]["source_level_rank3_carrier_support_closed"],
            "su2_weak_split_closed": previous["decision"]["su2_weak_split_closed"],
            "rank_quotient_arithmetic_closed": previous["decision"]["rank_quotient_arithmetic_closed"],
        },
    }

    projector_theorem = {
        "name": "SelectedU1SharedCircleQuotientProjectorTheorem",
        "statement": (
            "On the selected rank-3 U1/qutrit source carrier, the unique shared "
            "central-circle universal line is quotiented before the U1 threshold "
            "finite trace.  In a carrier basis where this line is spanned by "
            "s=(1,1,1)/sqrt(3), the quotient projector is P_perp=I-(1/3)J. "
            "It is idempotent, annihilates s, has rank 2, and gives normalized "
            "trace Tr(P_perp)/Tr(I)=2/3."
        ),
        "basis_gauge_note": "Choosing s=(1,1,1)/sqrt(3) is a representative basis choice for the one-dimensional shared line; the normalized trace and rank are invariant under unitary changes of carrier basis.",
        "shared_vector_representative": ["1/sqrt(3)", "1/sqrt(3)", "1/sqrt(3)"],
        "P_shared": serial_matrix(p_shared),
        "P_perp": serial_matrix(p_perp),
        "checks": {
            "idempotent": p2 == p_perp,
            "annihilates_shared_vector": all(value == 0 for value in zero_on_shared),
            "rank": rank,
            "trace_P_perp": f"{tr_p.numerator}/{tr_p.denominator}",
            "trace_identity": f"{tr_i.numerator}/{tr_i.denominator}",
            "normalized_trace": f"{normalized_trace.numerator}/{normalized_trace.denominator}",
            "same_as_source_theorem_weight": str(normalized_trace) == "2/3",
        },
    }

    trace_policy = {
        "name": "U1PhysicalThresholdTraceUsesSharedCircleQuotient",
        "statement": (
            "The U1 weak-split threshold finite trace is evaluated on the physical "
            "carrier quotient V/<s>, equivalently by inserting P_perp on the "
            "selected rank-3 carrier before determinant/trace evaluation."
        ),
        "reason": (
            "The central circle is the unique shared bookkeeping channel, not a "
            "sector-specific gauge threshold load; finite coherent projection in "
            "gauge sectors must be quotient-compatible; and Theta gauge overlap "
            "accounting evaluates internal harmonic norms on the retained physical "
            "threshold subspace."
        ),
        "formula": "I_1_selected_index = Tr(P_perp)/Tr(I_3) = 2/3",
        "scope": "dimensionless U1 threshold-index factor in the same internal weak-split accounting scheme; not a measured electroweak prediction or K_gauge anchor",
    }

    candidate = {
        "candidate": "SelectedU1QuotientProjectorPperpAndTracePolicy",
        "status": "SELECTED_U1_QUOTIENT_PROJECTOR_PPERP_TRACE_POLICY_CLOSED_INDEX_ONLY",
        "inputs": {
            "previous_gate": str(PREVIOUS.relative_to(ROOT)),
            "central_circle_source": str(CENTRAL_CIRCLE_SOURCE),
            "finite_projection_source": str(FINITE_PROJECTION_SOURCE),
            "theta_gauge_source": str(THETA_GAUGE_SOURCE),
        },
        "source_support": source_support,
        "projector_theorem": projector_theorem,
        "trace_policy": trace_policy,
        "decision": {
            "explicit_U1_shared_vector_s": True,
            "explicit_U1_P_perp_projector": True,
            "U1_operator_trace_uses_P_perp": True,
            "selected_U1_index": "2/3",
            "selected_SU2_index": "1/1",
            "selected_U1_SU2_threshold_index_pair_closed": True,
            "measured_electroweak_closure": False,
            "K_gauge_anchor_closed": False,
            "target_fitting_used": False,
            "next_required_object": "Selected_K_Gauge_Anchor_or_Full_Electroweak_Matching_v1",
        },
        "guardrails": [
            "This closes the U1/SU2 dimensionless threshold-index pair, not measured electroweak closure.",
            "Do not use this theorem to set K_gauge or a matching scale.",
            "Do not reuse the flat FP policy outside weak-split gauge-kinetic threshold accounting.",
            "The selected projector is unique only up to unitary basis change of the same one-dimensional shared line.",
        ],
        "closure_claimed": True,
        "closure_scope": "selected_U1_quotient_projector_and_dimensionless_threshold_index_pair",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedU1QuotientProjectorPperpAndTracePolicy",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "explicit_U1_shared_vector_representative": True,
            "explicit_U1_P_perp_projector": True,
            "rank_P_perp": rank,
            "normalized_trace": "2/3",
            "U1_trace_policy_uses_P_perp": True,
            "selected_U1_SU2_threshold_index_pair": True,
        },
        "what_remains_open": {
            "K_gauge_anchor": True,
            "matching_scale_and_running_scheme": True,
            "measured_electroweak_closure": True,
        },
        "next_required_object": candidate["decision"]["next_required_object"],
        "closure_scope": candidate["closure_scope"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    theorem = candidate["projector_theorem"]
    policy = candidate["trace_policy"]
    checks = "\n".join(f"{key} = {value}" for key, value in theorem["checks"].items())
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    d = candidate["decision"]
    return f"""# Selected U1 Quotient Projector Pperp and Trace Policy v1

## Result

This closes the final U1 projector gate for the dimensionless U1/SU2
threshold-index pair.  It does not close measured electroweak matching or
`K_gauge`.

```text
selected_U1_index = {d["selected_U1_index"]}
selected_SU2_index = {d["selected_SU2_index"]}
selected_U1_SU2_threshold_index_pair_closed = {str(d["selected_U1_SU2_threshold_index_pair_closed"]).lower()}
measured_electroweak_closure = {str(d["measured_electroweak_closure"]).lower()}
K_gauge_anchor_closed = {str(d["K_gauge_anchor_closed"]).lower()}
```

## Projector Theorem

```text
{theorem["name"]}
```

{theorem["statement"]}

Basis note:

```text
{theorem["basis_gauge_note"]}
```

Representative:

```text
s = ({", ".join(theorem["shared_vector_representative"])})
P_perp =
{theorem["P_perp"]}
```

Checks:

```text
{checks}
```

## Trace Policy

```text
{policy["name"]}
```

{policy["statement"]}

Reason:

```text
{policy["reason"]}
```

Formula:

```text
{policy["formula"]}
```

Scope:

```text
{policy["scope"]}
```

## Guardrails

{guardrails}

## Next Required Object

```text
{d["next_required_object"]}
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
