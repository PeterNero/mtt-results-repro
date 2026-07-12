# Iwasawa rho_E Validator

## Purpose

The previous recovery attempt proved that the current corpus does not supply
the selected transition matrices:

```text
rho_E(g1,z), ..., rho_E(g6,z).
```

This note adds an executable validator for future candidate `rho_E` data.  It
does not construct the selected transitions.  It makes sure that when such data
are proposed, they can be checked before being used in the finite-element
Galerkin calculation.

The validator is:

```text
scripts/validate_iwasawa_rhoE.py
```

## Supported v1 Format

Version 1 supports constant generator matrices:

```json
{
  "rank": 3,
  "generator_data": {
    "g1": {"matrix": [...]},
    "g2": {"matrix": [...]},
    "g3": {"matrix": [...]},
    "g4": {"matrix": [...]},
    "g5": {"matrix": [...]},
    "g6": {"matrix": [...]}
  }
}
```

Each matrix must be `3 x 3`.  Each entry is either:

```text
real_number
```

or:

```text
[real_part, imaginary_part].
```

Coordinate-dependent or node-dependent `rho_E(g,z)` data are not validated by
v1.  They require a later evaluator extension.

## Implemented Checks

The validator checks:

```text
all six generator entries are present,
all matrices are 3 x 3,
all determinants are nonzero,
the constant matrices satisfy the Iwasawa group relations.
```

The nonabelian relations checked are:

```text
g1 g2 = g2 g1,
g3 g4 = g4 g3,
g1 g3 = g5 g3 g1,
g1 g4 = g6 g4 g1,
g2 g3 = g6 g3 g2,
g5 g2 g4 = g4 g2,
g5 and g6 commute with all generators.
```

The fourth mixed relation encodes:

```text
g2 g4 = g5^{-1} g4 g2
```

without explicitly computing an inverse.

## Exit Codes

The script returns:

```text
0: complete candidate passes implemented checks,
1: complete candidate fails an algebraic check,
2: candidate is incomplete/open.
```

The open template:

```text
certificates/iwasawa_bundle_rhoE_data.template.json
```

therefore returns exit code `2`, not `0`.

## Smoke Tests

The audit verifies three cases:

```text
open template -> exit 2,
identity matrices -> exit 0 as schema smoke test,
bad noncommuting matrices -> exit 1.
```

The identity case is not selected data. It only proves the validator and
constant-matrix schema behave correctly.

## Guardrail

Passing this validator is necessary but not sufficient for physical use.

A candidate must still prove:

```text
it comes from the selected bundle E,
it has Hermitian metric compatibility,
it supplies sector projections Q,u,d,L,e,N,H,
it works with the selected D_E action.
```

Do not use identity `rho_E`, benchmark matrices, observed masses, or q79 labels
as substitutes for selected bundle transition data.

## Verdict

We have moved from:

```text
rho_E is missing
```

to:

```text
future constant rho_E candidates have an executable algebraic acceptance test.
```

Actual selected `rho_E` remains open.

