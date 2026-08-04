# QFT.02 Physical-Family Source Dependency

**Date:** 2026-07-26
**Result:** first full-domain extension row dependency-reduced

## What Closed

The analytic part of the missing physical family is complete as an
implication:

```text
selected HYM/action source
    -> smooth chiral Dirac family
    -> physical Hessian family
    -> local Riesz spectral bundles
    -> Kato connection
    -> analytic determinant line.
```

The conditional analytic contract is `8/8` and adds zero physical
parameters.

An exact rational Walsh witness also proves that the current finite projected
q79 rows cannot select the smooth lift. Two distinct connection rows have the
same rank-four finite projection but produce different Dirac operators and
positive Hessians.

## What Did Not Close

The actual physical source payload remains `0/3`:

```text
open  B.HS.01      visible/hidden HYM endpoints
open  B.GEO.01     physical HYM-to-symbol Hessian intertwiner
open  B.ACTION.01  selected upper action and BV Hessian
```

Consequently, the selected-family row and full chiral measure remain false.
The full-domain contract stays `0/4`, and the continuum table stays `1/9`.

## Frontier Change

Before this theorem, the first full-domain row looked like an independent
request to invent a smooth projector/connection/Hessian construction inside
the QFT repository.

After this theorem, no analytic invention is missing. Standard
elliptic-family, Riesz/Kato and determinant-line machinery supplies the whole
package once the physical source exists. Conversely, finite projected q79
data cannot supply that source. The row is now exactly dependency-reduced to
`B.HS.01 + B.GEO.01 + B.ACTION.01`.

Within the full-domain measure problem, the independent rows are now:

1. local quotient-moduli measure current;
2. crossing-strata and disconnected-sector gluing; and
3. cutoff-uniform locality and fixed-coupling norm control.

## Best Next Move

Do not add another auxiliary projector family here. The decisive physical
work is upstream:

1. finish the selected visible/hidden HYM endpoints;
2. construct the symbol-level unitary parallel Hessian intertwiner; and
3. import the selected action Hessian.

Once those arrive, this theorem turns them directly into the full analytic
family package. The next independent QFT theorem can meanwhile formulate the
local determinant-line measure-current integrability condition on an
abstract supplied family, without claiming the physical source exists.
