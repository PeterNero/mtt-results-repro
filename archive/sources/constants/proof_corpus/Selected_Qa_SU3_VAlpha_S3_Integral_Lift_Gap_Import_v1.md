# Selected Qa/SU3 VAlpha/S3 Integral-Lift Gap Import

## Result

The q79 integral-lift and selector-obstruction results are imported as the next
gate after finite mod-3 compatibility.

The important update is:

```text
explicit Appell-Humbert model for L^2=(2,-4,0): exists
ordinary integral c1 matrix: realized
conditional pullback Cech cohomology: h1=8
conditional promoted packet after a selected source: validator exit 0
```

So the blocker is no longer ordinary integral automorphy existence, and it is
not a cohomology-dimension problem.  If a selected source supplies the ordered
integral Cech/automorphy data, the existing h1=8 packet can promote.

## Obstruction

The finite mod-3 bridge cannot be the selector.  The target branch
`L=(1,-2,0)` and the swapped branch remain indistinguishable under the current
closed finite, topological, cohomological, and Appell-Humbert data.

This imports the source-selector theorem:

```text
No current closed selector can uniquely select L=(1,-2,0).
```

It also imports the Pic0 obstruction: neutral flat Pic0 data are invisible to
the current curvature/topology/cohomology tests and require either a
holonomy-sensitive source or an explicit quotient/gauge-fixing rule.

## Frontier

The next source must break the target-vs-swapped and Pic0 degeneracies.  The
live options are:

```text
selected target Gauduchon wall r1:r2=sqrt(2):1
selected ordered integral Cech/automorphy/D_E source
same-source D_E/dotD/Hessian term ordering the base factors
holonomy-sensitive source selecting or quotienting Pic0 characters
```

This is a useful tightening.  We should stop treating the finite qutrit bridge
or h1 calculation as the missing magic piece.  The missing piece is a selected
symmetry-breaking source.
