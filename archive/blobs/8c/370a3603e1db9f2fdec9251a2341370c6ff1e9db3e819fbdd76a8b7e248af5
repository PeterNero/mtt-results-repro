"""Target Smith-normal-form templates for the Z_64 x Z_7 flavor CP program."""

from recursive_quotient_snf_template import invariant_factors


def report(name: str, matrix: list[list[int]]) -> None:
    factors, free_rank = invariant_factors(matrix)
    print(name)
    print(f"  torsion factors: {factors}")
    print(f"  free rank: {free_rank}")
    print()


def main() -> None:
    # Generators:
    # e_64, e_7, e_12, e_23, e_31
    product_target = [
        [64, 0, 0, 0, 0],  # 64 e_64 = 0
        [0, 7, 0, 0, 0],  # 7 e_7 = 0
        [0, 0, 1, 1, 1],  # phase-sum row
    ]
    report("Target product quotient Z_64 x Z_7 plus phase sum", product_target)

    # If the future geometry produces a diagonal cyclic relation instead,
    # this is the corresponding cyclic target.
    cyclic_target = [
        [448, 0, 0, 0],  # 448 e = 0
        [0, 1, 1, 1],
    ]
    report("Target cyclic quotient Z_448 plus phase sum", cyclic_target)

    # Independent binary memories are not enough.
    six_binary = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
    ]
    report("Six independent Z_2 memories plus phase sum", six_binary)


if __name__ == "__main__":
    main()

