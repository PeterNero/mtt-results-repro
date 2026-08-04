"""Toy Smith-normal-form checks for nested circle-lens-nil carrier options.

These matrices are diagnostic templates only.  They test what follows from
possible carrier labels such as circle-on-1, lens-on-4, nil-on-7.  They are not
MTT derivations unless the corresponding relation rows are extracted from the
corpus geometry, flux, projector, or orbifold data.
"""

from __future__ import annotations

from recursive_quotient_snf_template import invariant_factors


def report(name: str, matrix: list[list[int]]) -> None:
    factors, free_rank = invariant_factors(matrix)
    print(name)
    print("  torsion factors:", factors if factors else "none")
    print("  free rank:", free_rank)
    print()


def main() -> None:
    # Generators:
    # e_c, e_l, e_n, e_12, e_23, e_31

    phase_sum = [0, 0, 0, 1, 1, 1]

    nested_labels_only = [
        [-4, 1, 0, 0, 0, 0],  # e_l = 4 e_c
        [0, -7, 1, 0, 0, 0],  # e_n = 7 e_l
        phase_sum,
    ]
    report(
        "Nested labels only: e_l=4e_c, e_n=7e_l, plus phase sum",
        nested_labels_only,
    )

    naive_lens_nil_closures = [
        [-4, 1, 0, 0, 0, 0],  # e_l = 4 e_c
        [0, -7, 1, 0, 0, 0],  # e_n = 7 e_l
        [0, 4, 0, 0, 0, 0],   # 4 e_l = 0, toy lens-level closure
        [0, 0, 7, 0, 0, 0],   # 7 e_n = 0, toy nil-level closure
        phase_sum,
    ]
    report(
        "Naive nested 4/7 closures: containment plus 4e_l=0 and 7e_n=0",
        naive_lens_nil_closures,
    )

    dyadic_circle_with_nil_seven = [
        [64, 0, 0, 0, 0, 0],  # 64 e_c = 0, toy dyadic circle lift
        [0, 0, 7, 0, 0, 0],   # 7 e_n = 0, toy nil sevenfold closure
        phase_sum,
    ]
    report(
        "Separated source rows: 64e_c=0 and 7e_n=0, plus phase sum",
        dyadic_circle_with_nil_seven,
    )

    dyadic_with_naive_containment = [
        [-4, 1, 0, 0, 0, 0],  # e_l = 4 e_c
        [0, -7, 1, 0, 0, 0],  # e_n = 7 e_l
        [64, 0, 0, 0, 0, 0],  # 64 e_c = 0
        [0, 0, 7, 0, 0, 0],   # 7 e_n = 0
        phase_sum,
    ]
    report(
        "Dyadic circle plus nil seven with naive 1-4-7 containment rows",
        dyadic_with_naive_containment,
    )

    lens_quarter_phase_and_nil_seven = [
        [0, 4, 0, 0, 0, 0],   # 4 e_l = 0, exact quarter-turn lens phase
        [0, 0, 7, 0, 0, 0],   # 7 e_n = 0, nil sevenfold closure
        phase_sum,
    ]
    report(
        "Lens quarter-turn plus nil seven, no dyadic lift",
        lens_quarter_phase_and_nil_seven,
    )


if __name__ == "__main__":
    main()
