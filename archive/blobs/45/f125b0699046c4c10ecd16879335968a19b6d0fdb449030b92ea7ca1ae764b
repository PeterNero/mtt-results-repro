from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADJOINT = ROOT / "certificates" / "btt_adjoint_shape_map_typing_theorem_certificate.json"

OUT_CERT = ROOT / "certificates" / "btt_exact_support_independence_no_go_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "BTT_Exact_Support_Independence_NoGo_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def matvec(mat: list[list[float]], vec: list[float]) -> list[float]:
    return [sum(row[i] * vec[i] for i in range(len(vec))) for row in mat]


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def propagator_scalar(b_star_support: list[float]) -> float:
    # Toy model: one TT test direction, A^{-1}=I on a two-dimensional coherent
    # internal support. Delta_TT = B A^{-1} B^* = ||B^* TT||^2.
    return dot(b_star_support, b_star_support)


def main() -> None:
    adjoint = load(ADJOINT)

    exact_projector = [[1.0, 0.0], [0.0, 0.0]]
    exact_support = [1.0, 0.0]
    other_support = [0.0, 1.0]

    model_exact = {
        "Bstar_PTT": exact_support,
        "Delta_TT": propagator_scalar(exact_support),
        "Pi_exact_Bstar_PTT": matvec(exact_projector, exact_support),
        "exact_support_identity": matvec(exact_projector, exact_support) == exact_support,
    }
    model_other = {
        "Bstar_PTT": other_support,
        "Delta_TT": propagator_scalar(other_support),
        "Pi_exact_Bstar_PTT": matvec(exact_projector, other_support),
        "exact_support_identity": matvec(exact_projector, other_support) == other_support,
    }

    shared_assumptions = {
        "B_is_shape_map_internal_to_TT": True,
        "Delta_TT_equals_B_Ainv_Bstar_nonzero": model_exact["Delta_TT"] > 0 and model_other["Delta_TT"] > 0,
        "TT_weight2_and_BRST_closed": (
            adjoint["closed_now"]["B_TT_weight2"] is True
            and adjoint["closed_now"]["B_TT_BRST_compatible"] is True
        ),
        "exact_Z64_branch_available": adjoint["closed_now"]["exact_Z64_branch_available_and_coherent"] is True,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "btt_exact_support_independence_no_go",
        "status": "EXACT_SUPPORT_IDENTITY_INDEPENDENT_OF_CURRENT_SOURCED_ASSUMPTIONS",
        "input_certificate": str(ADJOINT),
        "shared_assumptions": shared_assumptions,
        "toy_models": {
            "model_A_exact_support": model_exact,
            "model_B_other_coherent_support": model_other,
        },
        "logical_result": {
            "current_assumptions_force_nonzero_TT_adjoint_support": True,
            "current_assumptions_force_exact_dstar_support": False,
            "reason": (
                "Both toy models have nonzero BA^{-1}B^* on the TT quotient and preserve the "
                "already closed weight/BRST conditions, while only one satisfies "
                "Pi_exact64 B^* P_TT = B^* P_TT. Therefore exact support is an independent "
                "selection datum unless DG(Psi*) or an equivalent central-circle selection "
                "principle is supplied."
            ),
        },
        "next_required_source_or_computation": {
            "option_1_direct": "compute DG(Psi*) on the TT quotient and project B^*P_TT against Pi_exact64",
            "option_2_selection_axiom": (
                "prove a central-circle selection theorem saying physical TT adjoint support "
                "is exhausted by the selected exact Z64 branch"
            ),
            "forbidden_shortcut": "do not infer exact support merely from existence of BA^{-1}B^* or from Z64 branch availability",
        },
        "guardrails": {
            "claims_final_lambda_GR_TT_15": False,
            "claims_exact_support_sourced": False,
            "uses_observed_GR_data": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# BTT Exact Support Independence No-Go v1

## Result

The exact-support identity

```text
Pi_exact64 B^* P_TT = B^* P_TT
```

is independent of the currently sourced assumptions.

The current corpus and certificates close:

```text
B = DG(Psi*) Pi_coh,
Delta_TT = B A^{-1} B^* is nonzero on the physical TT quotient,
TT weight = 2,
BRST/diffeomorphism quotient compatibility,
the exact Z64 branch is coherent and available.
```

But these assumptions do not force the TT adjoint support to lie in the exact
`d_*` branch.

## Countermodel

Use a two-dimensional coherent internal toy support:

```text
e_exact = (1,0),
e_other = (0,1),
Pi_exact = diag(1,0),
A^{-1}=I.
```

Both choices

```text
B^*P_TT = e_exact
B^*P_TT = e_other
```

give the same kind of nonzero TT propagator:

```text
Delta_TT = ||B^*P_TT||^2 = 1.
```

Only the first satisfies `Pi_exact B^*P_TT = B^*P_TT`. Therefore nonzero TT
coupling plus exact-branch availability does not imply exact-branch support.

## Consequence

The final theorem cannot be proved from the current source set by algebraic
compression alone. One new ingredient is necessary:

```text
direct computation of DG(Psi*) on TT,
```

or

```text
a central-circle selection theorem proving TT adjoint support is exhausted by
the exact Z64 branch.
```

Once that ingredient is supplied, the existing uniqueness theorem immediately
returns `|d_*> tensor span{c_2,s_2}` and internal `lambda_GR,TT=15`.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
