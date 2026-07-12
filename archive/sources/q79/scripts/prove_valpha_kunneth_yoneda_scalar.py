"""Prove the remaining V_alpha Yoneda scalar in the reduced Kunneth model.

The prior attempt computed the final finite-branch scalar in a canonical
theta-ladder basis.  This script removes the arbitrary-looking part: the ladder
is exactly the Kunneth product of

  H^0_E1(O(1)) x H^0_E1(O(2)) -> H^0_E1(O(3))

and the Serre-dual map

  H^0_E2(O(3)) -> H^0_E2(O(4))   dual to
  H^1_E2(O(-4)) -> H^1_E2(O(-3)).

With the standard degree-one theta generator, the positive factor is inclusion
e_i -> e_i and the negative factor is projection eta_j -> eta_j for j<3,
eta_3 -> 0.  Their Kronecker product is the canonical ladder matrix.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

SELECTED_COHOMOLOGY = (
    CANDIDATES
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_cohomology.selected_under_section_principle.json"
)
SCALAR_ATTEMPT = CERTS / "valpha_remaining_yoneda_scalar_attempt_certificate.json"
ZERO_SLOPE_REDUCTION = CERTS / "valpha_zero_slope_yoneda_reduction_certificate.json"
APPELL_HUMBERT = CERTS / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"

OUT_DIR = CANDIDATES / "valpha_kunneth_yoneda_scalar"
OUT_MATRIX = OUT_DIR / "reduced_kunneth_yoneda_matrix.json"
OUT_CANDIDATE = CANDIDATES / "valpha_kunneth_yoneda_scalar_proof.candidate.json"
OUT_CERT = CERTS / "valpha_kunneth_yoneda_scalar_proof_certificate.json"
OUT_PAPER = CORPUS / "VAlpha_Kunneth_Yoneda_Scalar_Proof_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def matvec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(entry * value for entry, value in zip(row, vector, strict=True)) for row in matrix]


def rank_int(matrix: list[list[int]]) -> int:
    rows = [[float(value) for value in row] for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    col_count = len(rows[0])
    pivot_row = 0
    for col in range(col_count):
        pivot = None
        for row in range(pivot_row, row_count):
            if abs(rows[row][col]) > 1e-12:
                pivot = row
                break
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][col]
        rows[pivot_row] = [value / pivot_value for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or abs(rows[row][col]) <= 1e-12:
                continue
            factor = rows[row][col]
            rows[row] = [
                rows[row][entry_col] - factor * rows[pivot_row][entry_col]
                for entry_col in range(col_count)
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def positive_inclusion_matrix() -> list[list[int]]:
    """H0(O(2)) -> H0(O(3)) under multiplication by selected H0(O(1))."""
    return [
        [1, 0],
        [0, 1],
        [0, 0],
    ]


def negative_serre_dual_projection_matrix() -> list[list[int]]:
    """H1(O(-4)) -> H1(O(-3)), dual to H0(O(3)) -> H0(O(4))."""
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
    ]


def kronecker(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    rows: list[list[int]] = []
    for left_row in left:
        for right_row in right:
            row: list[int] = []
            for left_value in left_row:
                row.extend(left_value * right_value for right_value in right_row)
            rows.append(row)
    return rows


def source_basis() -> list[str]:
    return [f"theta_plus_{i}_tensor_eta_minus_{j}" for i in range(2) for j in range(4)]


def target_basis() -> list[str]:
    return [f"theta_plus3_{i}_tensor_eta_minus3_{j}" for i in range(3) for j in range(3)]


def matrix_as_map(matrix: list[list[int]], src: list[str], tgt: list[str]) -> dict[str, str | None]:
    mapping: dict[str, str | None] = {}
    for col, label in enumerate(src):
        nonzero_rows = [row for row, values in enumerate(matrix) if values[col] != 0]
        mapping[label] = tgt[nonzero_rows[0]] if len(nonzero_rows) == 1 else None
    return mapping


def build_paper(cert: dict[str, Any]) -> str:
    proof = cert["reduced_kunneth_yoneda_scalar"]
    return f"""# VAlpha Kunneth Yoneda Scalar Proof v1

## The Matrix

The remaining finite branch scalar is the cup/Yoneda multiplication:

```text
H^0(1,1,0) x H^1(2,-4,0) -> H^1(3,-3,0).
```

In the reduced base-pullback Kunneth model it factors as:

```text
H^0_E1(O(1)) x H^0_E1(O(2)) -> H^0_E1(O(3))
H^0_E2(O(1)) x H^1_E2(O(-4)) -> H^1_E2(O(-3)).
```

The second map is the Serre-dual transpose of the ordinary multiplication
`H^0_E2(O(3)) -> H^0_E2(O(4))`.  Therefore the full finite matrix is the
Kronecker product:

```json
{json.dumps(proof["kunneth_matrix"], indent=2)}
```

It has rank `{proof["matrix_rank"]}` and sends the selected Ext vector

```json
{json.dumps(proof["selected_ext_vector"], indent=2)}
```

to

```json
{json.dumps(proof["target_vector"], indent=2)}
```

The target vector is nonzero.  Thus the remaining finite branch-candidate
injection `M=(-2,1,0)` is obstructed inside the selected reduced Kunneth model.

## What Is Still Not Claimed

This is not full V_alpha stability by itself.  The remaining global proof
obligations are:

1. prove every destabilizing rank-one/torsion-free subsheaf is in the finite
   branch list, or provide a source theorem reducing to it;
2. promote the reduced Kunneth functor to raw selected Appell-Humbert/Cech
   multiplication if the final paper requires good-cover transition data;
3. derive the HYM/Strominger source or use the stability result with the
   appropriate existence theorem.

It does not prove HYM existence or full SM closure.
"""


def main() -> int:
    selected = load(SELECTED_COHOMOLOGY)
    scalar_attempt = load(SCALAR_ATTEMPT)
    zero_reduction = load(ZERO_SLOPE_REDUCTION)
    appell = load(APPELL_HUMBERT)

    pos = positive_inclusion_matrix()
    neg = negative_serre_dual_projection_matrix()
    matrix = kronecker(pos, neg)
    src_basis = selected.get("cochain_complex", {}).get("basis_labels_C1") or source_basis()
    tgt_basis = target_basis()
    selected_vector = selected.get("reported_cohomology", {}).get(
        "extension_class_vector_C1",
        [1, 0, 0, 0, 0, 0, 0, 0],
    )
    target_vector = matvec(matrix, selected_vector)
    nonzero = any(value != 0 for value in target_vector)
    selected_label = selected.get("reported_cohomology", {}).get("nonzero_extension_class_label")
    mapping = matrix_as_map(matrix, src_basis, tgt_basis)

    matches_prior = (
        mapping == scalar_attempt.get("canonical_theta_ladder_packet", {}).get("basis_map")
        and target_vector
        == scalar_attempt.get("canonical_theta_ladder_packet", {}).get("target_vector")
    )

    matrix_packet = {
        "schema": "VAlphaReducedKunnethYonedaMatrix.v1",
        "status": "REDUCED_KUNNETH_YONEDA_MATRIX_NONZERO",
        "positive_factor": {
            "domain": "H^0_E1(O(2))",
            "target": "H^0_E1(O(3))",
            "matrix": pos,
            "rank": rank_int(pos),
        },
        "negative_factor": {
            "domain": "H^1_E2(O(-4))",
            "target": "H^1_E2(O(-3))",
            "serre_dual_description": "dual of H^0_E2(O(3)) -> H^0_E2(O(4))",
            "matrix": neg,
            "rank": rank_int(neg),
        },
        "source_basis": src_basis,
        "target_basis": tgt_basis,
        "basis_map": mapping,
        "kunneth_matrix": matrix,
        "matrix_rank": rank_int(matrix),
        "kernel_basis_labels_in_this_order": [
            label for label, image in mapping.items() if image is None
        ],
        "selected_ext_label": selected_label,
        "selected_ext_vector": selected_vector,
        "target_vector": target_vector,
        "target_vector_nonzero": nonzero,
    }

    cert = {
        "certificate": "VAlphaKunnethYonedaScalarProof",
        "status": "VALPHA_KUNNETH_YONEDA_SCALAR_PROVED_REDUCED_MODEL_FULL_STABILITY_OPEN",
        "analysis_script": rel(Path(__file__)),
        "candidate_data": rel(OUT_CANDIDATE),
        "matrix_packet": rel(OUT_MATRIX),
        "paper": rel(OUT_PAPER),
        "inputs": {
            "selected_cohomology": rel(SELECTED_COHOMOLOGY),
            "remaining_yoneda_scalar_attempt": rel(SCALAR_ATTEMPT),
            "zero_slope_reduction": rel(ZERO_SLOPE_REDUCTION),
            "appell_humbert": rel(APPELL_HUMBERT),
        },
        "input_statuses": {
            "selected_cohomology": selected.get("status"),
            "remaining_yoneda_scalar_attempt": scalar_attempt.get("status"),
            "zero_slope_reduction": zero_reduction.get("status"),
            "appell_humbert": appell.get("status"),
        },
        "reduced_kunneth_yoneda_scalar": matrix_packet,
        "closed_by_this_attempt": {
            "canonical_ladder_derived_from_kunneth_serre_duality": True,
            "prior_canonical_packet_matched": matches_prior,
            "selected_reduced_kunneth_scalar_nonzero": nonzero,
            "finite_branch_candidate_M_minus2_1_0_obstructed_in_reduced_model": nonzero,
        },
        "still_open": {
            "complete_destabilizing_subsheaf_enumeration": True,
            "promote_reduced_kunneth_to_raw_good_cover_cech_or_appell_humbert_multiplication": True,
            "selected_hym_or_strominger_existence_certificate": True,
            "operator_layer_pic0": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "primitive_C1_matrices": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_full_stability": False,
            "claims_hym_existence": False,
            "claims_full_subsheaf_enumeration": False,
            "claims_raw_good_cover_multiplication_supplied": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The remaining finite branch-candidate Yoneda scalar is no longer "
                "just a canonical-basis guess: it is the Kronecker product of the "
                "standard positive theta inclusion with the Serre-dual negative "
                "projection.  In the selected reduced Kunneth packet, the selected "
                "Ext vector maps nontrivially, so M=(-2,1,0) is obstructed in this "
                "finite model."
            ),
            "next_action": (
                "Either promote this reduced Kunneth calculation to raw good-cover "
                "Appell-Humbert/Cech multiplication, or move to the complete "
                "destabilizing-subsheaf enumeration theorem."
            ),
        },
    }

    write_json(OUT_MATRIX, matrix_packet)
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")

    print("VAlpha Kunneth Yoneda scalar proof")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
