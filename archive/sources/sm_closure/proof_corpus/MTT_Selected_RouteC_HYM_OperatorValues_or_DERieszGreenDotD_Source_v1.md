# MTT Selected Route-C HYM Operator Values or D_E/Riesz/Green/dotD Source v1

## Claim

The abstract HYM existence blocker is now removed, but concrete finite operator
values are not emitted yet.  The old Route-C files remain support data because
their selected-source flags are false, and the lifted-flag files remain
diagnostic because the flags are not theorem-derived.

## What Is Needed

The next theorem must extract finite data from the selected HYM connection:

```text
selected V_alpha + selected equal-radius metric + selected HYM connection
  -> selected cover/basis/quadrature
  -> rho_E, metric, D_E, Riesz/Green, dotD, C1/overlap matrices
```

The validators already define the acceptance boundary.  Passing matrices are
not enough; the source fields must be derived from the selected HYM connection
or an equivalent same-source Galerkin/Strominger extraction.

## Superset Status

This uses the straight HYM extraction path, with Route-C/Galerkin retained as
the execution route and diagnostic smoke retained only as support.  No observed
constants or target fitting are used.
