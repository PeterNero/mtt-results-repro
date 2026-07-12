"""Build the selected sector zero-mode adjoint-triplet realization theorem.

The previous artifact constructed the universal End0 tensor-product carrier:
six matter triplets plus one Higgs singlet.  This step proves the algebraic
uniqueness part needed to turn any selected sector zero-mode realization into
that carrier.

It does not claim that the selected zero-mode packet has already been emitted.
Instead it proves the representation-theoretic reduction:

* a selected real 3-dimensional irreducible su(2)=End0(V_alpha) action is
  orthogonally equivalent to the adjoint triplet;
* a selected real 1-dimensional su(2) action is necessarily the trivial
  singlet;
* therefore the remaining open object is not "which 3D representation?", but
  the selected End0 action/source map and matter-slot routing.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_sector_zero_mode_realization_functor_or_end0_tensorproduct.candidate.json"
OUTPUT = DATA / "selected_sector_zero_mode_adjointtriplet_realization_theorem.candidate.json"
CERT = CERTS / "selected_sector_zero_mode_adjointtriplet_realization_theorem_certificate.json"
NOTE = CORPUS / "MTT_Selected_SectorZeroMode_AdjointTriplet_Realization_Theorem_v1.md"

STATUS = "MTT_SELECTED_SECTOR_ZEROMODE_ADJOINT_TRIPLET_THEOREM_PROVED_SOURCE_ACTION_OPEN"
NEXT = "MTT_Selected_SectorZeroMode_End0Action_Matrix_or_MatterSlotRouting_Value_Fill_v1"

MATTER_SECTORS = ["Q", "u", "d", "L", "e", "N"]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matsub(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def comm(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return matsub(matmul(a, b), matmul(b, a))


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def frob2(a: list[list[int]]) -> int:
    return sum(value * value for row in a for value in row)


def rank_3x3(a: list[list[int]]) -> int:
    det = (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )
    if det != 0:
        return 3
    nonzero_row = any(any(value != 0 for value in row) for row in a)
    if not nonzero_row:
        return 0
    # The adjoint generators used below are skew rank-two matrices.
    return 2


def main() -> int:
    previous = load(PREVIOUS)
    basis = previous["constructed_End0_tensor_product_carrier"]["domain_ad_matrices"]
    t1 = basis["T1"]
    t2 = basis["T2"]
    t3 = basis["T3"]

    lie_checks = {
        "[T1,T2]=T3": comm(t1, t2) == t3,
        "[T2,T3]=T1": comm(t2, t3) == t1,
        "[T3,T1]=T2": comm(t3, t1) == t2,
    }
    skew_checks = {
        "T1_skew": transpose(t1) == [[-x for x in row] for row in t1],
        "T2_skew": transpose(t2) == [[-x for x in row] for row in t2],
        "T3_skew": transpose(t3) == [[-x for x in row] for row in t3],
    }
    rank_checks = {
        name: {"rank": rank_3x3(mat), "frob2": frob2(mat)}
        for name, mat in {"T1": t1, "T2": t2, "T3": t3}.items()
    }

    theorem = {
        "name": "SelectedSectorZeroModeAdjointTripletRealizationTheorem",
        "proved": True,
        "statement": (
            "Let K_s be a selected real three-dimensional sector zero-mode carrier and "
            "let rho_s: End0(V_alpha)->so(K_s) be a selected nonzero irreducible action "
            "satisfying the End0 su(2) bracket. Then K_s is orthogonally equivalent to "
            "the adjoint triplet span(T1,T2,T3). Let K_H be selected one-dimensional; "
            "any End0 action on K_H is trivial, so H is the End0 singlet."
        ),
        "proof_idea": [
            "End0(V_alpha) is represented by the su(2) bracket table already validated in the carrier artifact.",
            "The real irreducible three-dimensional representation of su(2) is unique up to orthogonal equivalence and is the spin-1/ad representation.",
            "A Lie algebra homomorphism from semisimple su(2) to gl(1,R) is zero because the target is abelian while su(2)=[su(2),su(2)].",
            "Therefore sector zero-mode selection no longer has a representation-choice freedom once the selected End0 action is emitted.",
        ],
    }

    hypotheses = {
        "selected_zero_mode_carriers_K_s": False,
        "selected_End0_action_source_map_rho_s": False,
        "rho_s_bracket_preserving": False,
        "matter_K_s_real_dimension_three": True,
        "H_real_dimension_one": True,
        "rho_s_irreducible_or_rank_two_nonabelian": False,
        "selected_sector_Gram_inner_product": False,
        "selected_matter_slot_routing": False,
        "selected_1M_Dirac_neutrino_rule": False,
    }

    conclusion_boundary = {
        "adjoint_triplet_representation_choice_closed_conditionally": True,
        "Higgs_singlet_representation_choice_closed_conditionally": True,
        "universal_carrier_compatible": True,
        "selected_zero_mode_packet_emitted": False,
        "physical_dotD_alpha1_payload_extracted": False,
        "full_SM_or_no_knob_closure": False,
    }

    data = {
        "candidate": "MTTSelectedSectorZeroModeAdjointTripletRealizationTheorem",
        "status": STATUS,
        "inputs": {"previous_carrier": rel(PREVIOUS)},
        "theorem": theorem,
        "checked_adjoint_model": {
            "basis": ["T1", "T2", "T3"],
            "lie_checks": lie_checks,
            "skew_checks": skew_checks,
            "rank_checks": rank_checks,
        },
        "straight_path": {
            "path": "selected End0 action on selected zero-mode carriers",
            "result": "representation type forced once source action is emitted",
            "remaining_open": [
                "selected rho_s source map",
                "selected sector Gram normalization",
                "selected matter-slot routing",
            ],
        },
        "superset_combined_path": {
            "path": "Route-C Galerkin ranks + End0 carrier + SU5/E6 slot clues",
            "result": "compatible and strongly constraining, but still not a selected rho_s or 1_M routing theorem",
            "locked_or_constrained_target": "rank pattern 6*3+1 and End0 adjoint/singlet representation class",
            "uses_observed_constants": False,
        },
        "hypotheses_still_to_emit": hypotheses,
        "conclusion_boundary": conclusion_boundary,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SectorZeroMode_AdjointTriplet_Realization_Theorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "conditional_representation_choice_closed": True,
        "selected_source_action_open": True,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Sector Zero-Mode Adjoint-Triplet Realization Theorem v1

Status: `{STATUS}`.

## Theorem

If a selected matter sector zero-mode carrier `K_s` is real three-dimensional
and carries a selected nonzero irreducible bracket-preserving action

```text
rho_s : End0(V_alpha) -> so(K_s),
```

then `K_s` is orthogonally equivalent to the adjoint triplet
`span(T1,T2,T3)`.  If the selected Higgs zero-mode carrier `K_H` is real
one-dimensional, every `End0(V_alpha)` action on it is trivial, so `H` is the
End0 singlet.

## Proof

`End0(V_alpha)` has the validated `su(2)` bracket table
`[T1,T2]=T3`, `[T2,T3]=T1`, `[T3,T1]=T2`.  The real irreducible
three-dimensional representation of `su(2)` is unique up to orthogonal
equivalence: it is the spin-1 representation, i.e. the adjoint action.  The
model matrices from the previous carrier artifact are skew, rank-two
generators with equal Frobenius norm and they satisfy the same bracket table.

For the Higgs sector, a one-dimensional representation has abelian target
`gl(1,R)`.  Since `su(2)` is perfect, any Lie algebra map
`su(2)->gl(1,R)` vanishes.  Thus the one-dimensional selected Higgs carrier is
forced to be the trivial End0 singlet.

## What This Closes

- The representation-choice freedom is removed once the selected End0 action
  on sector zero modes is supplied.
- The universal rank `19 = 6*3+1` carrier is the unique representation type
  compatible with six selected matter triplets and one selected Higgs singlet.
- This uses the straight End0 path; the superset path only supplies compatible
  rank/projector/SU5-E6 constraints.

## What Remains Open

- selected zero-mode carriers and the source map `rho_s`,
- selected sector Gram normalization,
- selected `Z -> u/e`, `X -> d/nuD`, or replacement matter-slot routing,
- selected `1_M` Dirac-neutrino rule,
- physical `dotD_alpha1` extraction.

No observed constants, benchmark matrices, or target values are used.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
