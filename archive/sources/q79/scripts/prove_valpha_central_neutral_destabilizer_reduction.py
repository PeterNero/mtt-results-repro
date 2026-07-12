"""Reduce and obstruct central-neutral V_alpha line destabilizers.

This is the next stability layer after the reduced Kunneth Yoneda scalar.
It does not try to prove that every rank-one torsion-free subsheaf in the
ambient geometry is central-neutral/base-pullback.  Instead it proves the
complete statement inside that lane:

  * no nonnegative-slope central-neutral class can map into L;
  * the classes that can map into Q=L^{-1} and have nonnegative slope are
    exactly six;
  * the selected extension boundary map is injective on each of those Hom
    spaces in the reduced Kunneth model.

Thus every central-neutral base-pullback line-bundle destabilizer is obstructed
in the selected reduced model.  The global stability theorem still needs the
source theorem reducing all destabilizing torsion-free rank-one subsheaves to
this lane, or raw good-cover data that proves the same result directly.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
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
KUNNETH_SCALAR = CERTS / "valpha_kunneth_yoneda_scalar_proof_certificate.json"
ZERO_SLOPE_REDUCTION = CERTS / "valpha_zero_slope_yoneda_reduction_certificate.json"
STABILITY_FILTER = CERTS / "valpha_extension_stability_filter_attempt_certificate.json"

OUT_DIR = CANDIDATES / "valpha_central_neutral_destabilizer_reduction"
OUT_TABLE = OUT_DIR / "reduced_destabilizer_table.json"
OUT_CANDIDATE = CANDIDATES / "valpha_central_neutral_destabilizer_reduction.candidate.json"
OUT_CERT = CERTS / "valpha_central_neutral_destabilizer_reduction_certificate.json"
OUT_PAPER = CORPUS / "VAlpha_Central_Neutral_Destabilizer_Reduction_v1.md"

L = (1, -2, 0)
Q = (-1, 2, 0)
POLARIZATION_WEIGHTS = (1, 2, 0)
EXPECTED_CANDIDATES = [
    (-4, 2, 0),
    (-3, 2, 0),
    (-2, 1, 0),
    (-2, 2, 0),
    (-1, 1, 0),
    (-1, 2, 0),
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sub(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a - b for a, b in zip(left, right, strict=True))  # type: ignore[return-value]


def slope(line: tuple[int, int, int]) -> int:
    return sum(value * weight for value, weight in zip(line, POLARIZATION_WEIGHTS, strict=True))


def h0_elliptic(degree: int) -> int:
    if degree > 0:
        return degree
    if degree == 0:
        return 1
    return 0


def h1_elliptic(degree: int) -> int:
    if degree < 0:
        return -degree
    if degree == 0:
        return 1
    return 0


def h0_reduced_base_pair(degrees: tuple[int, int, int]) -> int:
    if degrees[2] != 0:
        return 0
    return h0_elliptic(degrees[0]) * h0_elliptic(degrees[1])


def h1_reduced_base_pair(degrees: tuple[int, int, int]) -> int:
    if degrees[2] != 0:
        return 0
    a, b, _ = degrees
    return h1_elliptic(a) * h0_elliptic(b) + h0_elliptic(a) * h1_elliptic(b)


def rank_int(matrix: list[list[int]]) -> int:
    rows = [[Fraction(value) for value in row] for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    col_count = len(rows[0])
    pivot_row = 0
    for col in range(col_count):
        pivot = None
        for row in range(pivot_row, row_count):
            if rows[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][col]
        rows[pivot_row] = [value / pivot_value for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or rows[row][col] == 0:
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


def theta_h0_basis(prefix: str, degree: int) -> list[str]:
    if degree == 0:
        return [f"{prefix}_one"]
    return [f"{prefix}_{degree}_{idx}" for idx in range(degree)]


def eta_h1_basis(prefix: str, degree: int) -> list[str]:
    if degree == 0:
        return [f"{prefix}_zero_0"]
    if degree < 0:
        return [f"{prefix}_minus{-degree}_{idx}" for idx in range(-degree)]
    return []


def hom_basis(degrees: tuple[int, int, int]) -> list[tuple[int, int, str]]:
    first = theta_h0_basis("hom_theta", degrees[0])
    second = theta_h0_basis("hom_phi", degrees[1])
    basis: list[tuple[int, int, str]] = []
    for i, j in product(range(len(first)), range(len(second))):
        basis.append((i, j, f"{first[i]}_tensor_{second[j]}"))
    return basis


def target_h1_basis(degrees: tuple[int, int, int]) -> list[tuple[int, int, str]]:
    first = theta_h0_basis("theta_plus", degrees[0])
    second = eta_h1_basis("eta", degrees[1])
    basis: list[tuple[int, int, str]] = []
    for i, j in product(range(len(first)), range(len(second))):
        basis.append((i, j, f"{first[i]}_tensor_{second[j]}"))
    return basis


def boundary_map_for_candidate(
    line: tuple[int, int, int],
    selected_ext_is_lowest_basis: bool,
) -> dict[str, Any]:
    """Boundary Hom(M,Q) -> Ext^1(M,L) by cup product with selected e.

    In the selected reduced Kunneth model, e is the lowest basis vector in
    H^1(2,-4,0).  Multiplication by a Hom basis vector in H^0(Q-M) therefore
    lands in the matching low-index target slot of H^1(L-M).
    """

    hom_degrees = sub(Q, line)
    target_degrees = sub(L, line)
    source = hom_basis(hom_degrees)
    target = target_h1_basis(target_degrees)
    matrix = [[0 for _ in source] for _ in target]
    target_index = {(i, j): idx for idx, (i, j, _label) in enumerate(target)}

    if selected_ext_is_lowest_basis:
        for col, (i, j, _label) in enumerate(source):
            row = target_index.get((i, j))
            if row is not None:
                matrix[row][col] = 1

    image_labels = []
    for col, (_i, _j, label) in enumerate(source):
        rows = [row for row, values in enumerate(matrix) if values[col] != 0]
        image_labels.append(
            {
                "source": label,
                "target": target[rows[0]][2] if len(rows) == 1 else None,
                "coefficient": matrix[rows[0]][col] if len(rows) == 1 else 0,
            }
        )

    rank = rank_int(matrix)
    return {
        "hom_degrees_Q_minus_M": list(hom_degrees),
        "target_degrees_L_minus_M": list(target_degrees),
        "source_basis": [label for _i, _j, label in source],
        "target_basis": [label for _i, _j, label in target],
        "matrix": matrix,
        "rank": rank,
        "injective_on_hom": rank == len(source),
        "basis_images": image_labels,
        "selected_ext_assumption": "theta_plus_0_tensor_eta_minus_0 in H^1(2,-4,0)",
    }


def central_neutral_hom_to_q_candidates() -> list[tuple[int, int, int]]:
    candidates: list[tuple[int, int, int]] = []
    for b in (1, 2):
        for a in range(-2 * b, 0):
            candidates.append((a, b, 0))
    return sorted(candidates)


def bounded_scan_check(radius: int = 12) -> dict[str, Any]:
    hom_to_l_nonnegative: list[list[int]] = []
    hom_to_q_nonnegative: list[list[int]] = []
    for a in range(-radius, radius + 1):
        for b in range(-radius, radius + 1):
            line = (a, b, 0)
            if slope(line) < 0:
                continue
            if h0_reduced_base_pair(sub(L, line)) > 0:
                hom_to_l_nonnegative.append(list(line))
            if h0_reduced_base_pair(sub(Q, line)) > 0:
                hom_to_q_nonnegative.append(list(line))
    return {
        "radius": radius,
        "hom_to_L_nonnegative_slope_hits": hom_to_l_nonnegative,
        "hom_to_Q_nonnegative_slope_hits": sorted(hom_to_q_nonnegative),
        "matches_inequality_candidate_list": sorted(hom_to_q_nonnegative)
        == [list(item) for item in EXPECTED_CANDIDATES],
    }


def candidate_status(line: tuple[int, int, int], boundary: dict[str, Any]) -> str:
    if line == Q:
        return "EXCLUDED_BY_NON_SPLIT_EXTENSION_BOUNDARY"
    if line == (-2, 1, 0):
        return "EXCLUDED_BY_PROVED_REDUCED_KUNNETH_YONEDA_SCALAR"
    if boundary.get("injective_on_hom") is True:
        return "EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY"
    return "OPEN_BOUNDARY_NOT_INJECTIVE"


def build_table(selected_ext_is_lowest_basis: bool) -> dict[str, Any]:
    candidates = central_neutral_hom_to_q_candidates()
    rows = []
    for line in candidates:
        hom_l_degrees = sub(L, line)
        hom_q_degrees = sub(Q, line)
        ext_degrees = sub(L, line)
        boundary = boundary_map_for_candidate(line, selected_ext_is_lowest_basis)
        row = {
            "M_abc": list(line),
            "slope_p_1_2_1": slope(line),
            "hom_to_L_degrees": list(hom_l_degrees),
            "hom_to_L_dim": h0_reduced_base_pair(hom_l_degrees),
            "hom_to_Q_degrees": list(hom_q_degrees),
            "hom_to_Q_dim": h0_reduced_base_pair(hom_q_degrees),
            "Ext1_M_to_L_degrees": list(ext_degrees),
            "Ext1_M_to_L_dim": h1_reduced_base_pair(ext_degrees),
            "boundary_map": boundary,
            "status": candidate_status(line, boundary),
        }
        rows.append(row)

    extras_relative_to_prior_branch_list = [
        list(line)
        for line in candidates
        if line not in {Q, (-2, 1, 0), (2, -1, 0), L}
    ]

    return {
        "schema": "VAlphaCentralNeutralDestabilizerReduction.v1",
        "status": "CENTRAL_NEUTRAL_BASE_PULLBACK_DESTABILIZERS_OBSTRUCTED_REDUCED_KUNNETH_MODEL",
        "extension_sequence": "0 -> L -> V_alpha -> Q=L^{-1} -> 0",
        "L_abc": list(L),
        "Q_abc": list(Q),
        "polarization_weights": list(POLARIZATION_WEIGHTS),
        "selected_ext_basis": "theta_plus_0_tensor_eta_minus_0",
        "selected_ext_is_lowest_basis": selected_ext_is_lowest_basis,
        "inequality_reduction": {
            "central_neutral_assumption": "M=(a,b,0)",
            "slope": "mu(M)=a+2b",
            "hom_to_L_condition": "a<=1 and b<=-2, hence mu<=-3; no nonnegative-slope Hom(M,L) candidate",
            "hom_to_Q_condition": "a<=-1, b<=2, and a+2b>=0, hence b in {1,2} and a=-2b,...,-1",
            "candidate_list": [list(item) for item in candidates],
        },
        "bounded_scan_check": bounded_scan_check(),
        "prior_branch_list_diagnostic": {
            "explanation": (
                "The older finite branch list was a target/topological branch list, "
                "not by itself a complete Hom-destabilizer enumeration. The Hom "
                "cone adds four central-neutral nonnegative-slope candidates, all "
                "of which are obstructed here in the reduced Kunneth model."
            ),
            "extra_hom_destabilizer_candidates": extras_relative_to_prior_branch_list,
        },
        "candidate_rows": rows,
        "all_candidate_boundaries_injective": all(
            row["boundary_map"]["injective_on_hom"] for row in rows
        ),
        "all_candidates_obstructed": all(row["status"].startswith("EXCLUDED") for row in rows),
    }


def build_paper(cert: dict[str, Any]) -> str:
    table = cert["central_neutral_destabilizer_table"]
    rows = table["candidate_rows"]
    rows_text = "\n".join(
        "| `{}` | `{}` | `{}` | `{}` | `{}` | `{}` |".format(
            tuple(row["M_abc"]),
            row["slope_p_1_2_1"],
            row["hom_to_Q_dim"],
            row["Ext1_M_to_L_dim"],
            row["boundary_map"]["rank"],
            row["status"],
        )
        for row in rows
    )
    return f"""# VAlpha Central-Neutral Destabilizer Reduction v1

## Statement

Work in the selected reduced base-pullback Kunneth model for

```text
0 -> L -> V_alpha -> Q=L^-1 -> 0,
L=(1,-2,0), Q=(-1,2,0), mu(a,b,c)=a+2b.
```

Assume the rank-one line test class is central-neutral, so `M=(a,b,0)`.  Then
every nonnegative-slope central-neutral base-pullback line class with a possible
map to `V_alpha` is one of exactly six classes, and each is obstructed by the
selected extension boundary map in the reduced Kunneth model.

## Reduction

From the long exact Hom sequence

```text
0 -> Hom(M,L) -> Hom(M,V_alpha) -> Hom(M,Q) -> Ext^1(M,L),
```

we first test the two possible channels.

For `Hom(M,L)` one needs `L-M=(1-a,-2-b,0)` to be effective in the reduced
base-pullback model.  Thus `a<=1` and `b<=-2`, so `mu(M)=a+2b<=-3`.  No such
class can destabilize a slope-zero rank-two extension.

For `Hom(M,Q)` one needs `Q-M=(-1-a,2-b,0)` effective and `mu(M)>=0`.  Thus
`a<=-1`, `b<=2`, and `a+2b>=0`.  These inequalities force `b in {{1,2}}`, and
therefore the finite list:

```json
{json.dumps(table["inequality_reduction"]["candidate_list"], indent=2)}
```

The bounded scan recorded in the certificate agrees with this inequality
proof.

## Boundary Table

The connecting map is cup/Yoneda multiplication by the selected extension class
`theta_plus_0_tensor_eta_minus_0 in H^1(2,-4,0)`.

| M | slope | dim Hom(M,Q) | dim Ext^1(M,L) | boundary rank | status |
|---|---:|---:|---:|---:|---|
{rows_text}

The boundary map has full column rank in every row.  Hence no nonzero
`Hom(M,Q)` section lifts through `V_alpha`, and the `Hom(M,L)` channel is
already negative-slope only.  Therefore all central-neutral base-pullback
line-bundle destabilizers are obstructed in the selected reduced Kunneth model.

## Important Diagnostic

This sweep shows that the old finite branch list was not itself a complete
destabilizer enumeration.  It was a target/topological branch list.  The Hom
destabilizer cone adds four central-neutral nonnegative-slope candidates:

```json
{json.dumps(table["prior_branch_list_diagnostic"]["extra_hom_destabilizer_candidates"], indent=2)}
```

Those four are not a failure of the route; they are precisely the rows this
packet now kills by injective reduced Kunneth boundary maps.

## What Remains Open

This is still not the full V_alpha stability theorem.  The remaining global
step is to prove that every destabilizing rank-one/torsion-free subsheaf has a
central-neutral base-pullback reflexive hull covered by this calculation, or to
replace that reduction with raw selected good-cover Appell-Humbert/Cech
multiplication and a direct HYM/Strominger source theorem.

No HYM existence, raw good-cover multiplication, primitive C1 matrices, or full
SM closure is claimed here.
"""


def main() -> int:
    selected = load(SELECTED_COHOMOLOGY)
    scalar = load(KUNNETH_SCALAR)
    zero_reduction = load(ZERO_SLOPE_REDUCTION)
    stability_filter = load(STABILITY_FILTER)

    selected_vector = selected.get("reported_cohomology", {}).get("extension_class_vector_C1", [])
    selected_label = selected.get("reported_cohomology", {}).get("nonzero_extension_class_label")
    selected_ext_is_lowest_basis = (
        selected_label == "theta_plus_0_tensor_eta_minus_0"
        and selected_vector == [1, 0, 0, 0, 0, 0, 0, 0]
    )

    table = build_table(selected_ext_is_lowest_basis)
    expected_list = [list(item) for item in EXPECTED_CANDIDATES]
    actual_list = table["inequality_reduction"]["candidate_list"]
    all_closed = (
        selected_ext_is_lowest_basis
        and actual_list == expected_list
        and table["all_candidate_boundaries_injective"]
        and table["all_candidates_obstructed"]
    )

    cert = {
        "certificate": "VAlphaCentralNeutralDestabilizerReduction",
        "status": (
            "VALPHA_CENTRAL_NEUTRAL_DESTABILIZERS_OBSTRUCTED_REDUCED_MODEL_GLOBAL_ENUMERATION_OPEN"
            if all_closed
            else "VALPHA_CENTRAL_NEUTRAL_DESTABILIZER_REDUCTION_OPEN"
        ),
        "analysis_script": rel(Path(__file__)),
        "candidate_data": rel(OUT_CANDIDATE),
        "table_packet": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "inputs": {
            "selected_cohomology": rel(SELECTED_COHOMOLOGY),
            "kunneth_scalar": rel(KUNNETH_SCALAR),
            "zero_slope_reduction": rel(ZERO_SLOPE_REDUCTION),
            "stability_filter": rel(STABILITY_FILTER),
        },
        "input_statuses": {
            "selected_cohomology": selected.get("status"),
            "kunneth_scalar": scalar.get("status"),
            "zero_slope_reduction": zero_reduction.get("status"),
            "stability_filter": stability_filter.get("status"),
        },
        "central_neutral_destabilizer_table": table,
        "closed_by_this_attempt": {
            "central_neutral_hom_to_L_destabilizers_empty": True,
            "central_neutral_hom_to_Q_nonnegative_candidates_finite_six": actual_list
            == expected_list,
            "selected_ext_lowest_basis_confirmed": selected_ext_is_lowest_basis,
            "all_six_candidate_boundaries_injective": table["all_candidate_boundaries_injective"],
            "all_six_candidates_obstructed_in_reduced_kunneth_model": table[
                "all_candidates_obstructed"
            ],
            "central_neutral_base_pullback_line_destabilizers_obstructed": all_closed,
        },
        "still_open": {
            "global_rank_one_torsion_free_subsheaf_enumeration": True,
            "prove_all_destabilizers_have_central_neutral_base_pullback_reflexive_hull": True,
            "central_non_neutral_or_recursive_topology_lift_exclusion": True,
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
            "claims_full_torsion_free_subsheaf_enumeration": False,
            "claims_raw_good_cover_multiplication_supplied": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "Inside the central-neutral base-pullback line-bundle lane, the "
                "destabilizer problem is now finite and closed in the selected "
                "reduced Kunneth model. The Hom cone contains six nonnegative-slope "
                "candidates, not just the old finite branch list; the four extra "
                "rows are all killed by injective Yoneda boundary maps."
            ),
            "next_action": (
                "Prove the source theorem that every destabilizing rank-one "
                "torsion-free subsheaf reduces to this central-neutral "
                "base-pullback lane, or promote these reduced Kunneth boundary "
                "maps to raw selected Appell-Humbert/Cech multiplication."
            ),
        },
    }

    write_json(OUT_TABLE, table)
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")

    print("VAlpha central-neutral destabilizer reduction")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
