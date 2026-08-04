#!/usr/bin/env python3
"""Render the q79 space-6 u1=2,u2=21 finite-Groebner D-closure theorem."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = (
    ROOT / "candidate_data" / "q79_Ronly_u1_002_symbolic_exception_D_closure"
    / "space6_class1_u1_002_a_028_symbolic_t_finite_groebner.D_unit.certificate.json"
)
DEFAULT_OUTPUT = ROOT / "proof_corpus" / "Q79_Ronly_U1_002_Space6_U2_021_Finite_Groebner_D_Closure_v1.md"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    require(
        certificate.get("status")
        == "EXACT_R_ONLY_FINITE_GROEBNER_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D",
        "finite Groebner D certificate",
    )
    coordinates = certificate["fixed_coordinates"]
    require(
        certificate.get("space_index") == 6
        and coordinates == {
            "u1": 2,
            "a_equals_v_times_u3": 28,
            "selected_u0": 76,
            "selected_u2": 21,
        },
        "selected u2=21 coordinates",
    )
    quotient = certificate["quotient_algebra"]
    witness = certificate["unit_witness"]
    buchberger = quotient["Buchberger_pair_certificate"]
    coordinate_map = certificate["coordinate_isomorphism"]
    y_determinants = {
        name: row["pivot_multiplication_determinant"]
        for name, row in quotient["reconstructed_y_rows"].items()
    }
    D_determinants = {
        row: data["multiplication_determinant"]
        for row, data in certificate["D_terminal_data"].items()
    }
    text = f"""# q79 `u1=2`, Space-6 `u2=21` Finite-Groebner D Closure

## Status

`EXACT_R_ONLY_FINITE_GROEBNER_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D`

## Selected Line

```text
field:          F_101
space:          {certificate['space_index']}
u0,u1,u2:       {coordinates['selected_u0']},{coordinates['u1']},{coordinates['selected_u2']}
scalar class:   {certificate['scalar_square_class_representative']}
a=v*u3:         {coordinates['a_equals_v_times_u3']}
coordinate map: {coordinate_map['parent_assignment']}
```

The exact source relation `{coordinate_map['source_relation']}` and
`{coordinate_map['parent_assignment']}` give
`{coordinate_map['canonical_relation']}` with inverse
`{coordinate_map['inverse_assignment']}`. The source verifier also checks
that parent R rows 1 through 12 restrict exactly to the 12 line rows. Thus
the finite quotient and D terminal come from the same selected parent
operator.

## Finite Quotient

The complete `{quotient['reduced_basis_rows']}`-row reduced Groebner basis
presents a `{quotient['dimension']}`-dimensional quotient with standard
monomials

```text
{', '.join(quotient['standard_basis'])}
```

Buchberger's criterion is checked for all `{buchberger['total_pairs']}` row
pairs: `{buchberger['product_criterion_pairs']}` by the exact
coprime-leading-monomial product criterion and
`{buchberger['explicit_zero_reductions']}` by explicit S-polynomial
reduction to zero.

All `{quotient['basis_product_rows']}` commutative basis products are reduced
exactly. Their canonical table hash is

```text
{quotient['basis_product_table_sha256']}
```

All `{quotient['associativity_basis_triple_checks']}` basis-triple
associativity identities pass. No locality, reducedness, or point count is
assumed.

## Parent Lift And Unit Witness

The four triangular `y` rows reconstruct with multiplication determinants

```text
{y_determinants}
```

Both endpoint rows, all 12 R rows, and all four `y` rows then vanish in the
quotient. The selected D-terminal determinants are

```text
{D_determinants}
```

In particular, parent row `D{witness['parent_row']}` has determinant
`{witness['D_multiplication_determinant']}`. Its displayed
`{len(witness['D_inverse_coefficients'])}`-coordinate inverse multiplies its
remainder to

```text
{witness['product_coefficients']}.
```

Therefore `D{witness['parent_row']}` is a unit in the complete R-only
quotient. Adjoining this selected D row makes the full R/`y`/D ideal the unit
ideal over `F_101` and after every field extension.

## Boundary

This closes exactly space 6, `u1=2`, `u2=21`, equivalently the canonical
line `(class,a)=(1,28)`. It does not classify another line or `u1` value,
prove a characteristic-zero statement, close either mirror zero-zero chart,
or promote the finite obstruction to physical HYM/QG data. The global
symbolic chart count remains `138/140`. New continuous fit parameters: `0`.

## Reproduce

```text
python proof_corpus/q79_Ronly_u1_002_space6_u2_021_finite_groebner_D_closure_audit.py
```
"""
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print("Q79_U1_002_SPACE6_U2_021_FINITE_GROEBNER_D_THEOREM_RENDERED")
    print(
        f"dimension={quotient['dimension']}; D={witness['parent_row']}; "
        f"det={witness['D_multiplication_determinant']}"
    )
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
