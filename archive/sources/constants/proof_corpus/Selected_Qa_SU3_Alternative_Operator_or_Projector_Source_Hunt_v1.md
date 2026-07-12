# Selected Qa/SU3 Alternative Operator or Projector Source Hunt

## Purpose

The compact-Nil Hodge/BRST branch is now fully computed and obstructed:

```text
selected Qa = 4.8430192935084335
required Qa = 4.648486359430842
excess      = 0.19453293407759187
```

Any successful next branch must therefore provide a selected response

```text
Delta logdet = -0.19453293407759187
```

before target comparison. This note searches the corpus for legal sources of
such a response.

## Routes Ruled Out as Extra Corrections

The local Faddeev-Popov/BRST quotient Jacobian is a real source, but it has
already been counted in the selected `p=0` and `p != 0` Qa/SU3 quotient rules.
Using it again would double-count the same quotient measure.

The soft gauge-tube width is also not a no-knob physical correction by itself.
It is a representative-selection width or regulator unless the corpus supplies
an independent physical selection theorem for that width.

Complex nesting and the shared circle remain important for phase and weak-split
structure, but the present source search does not find a direct selected
SU3/Nil determinant correction from them.

## Remaining Legal Routes

The finite coherent filter

```text
B_adm = P chi(A) exp(-tau A) chi(A) P
```

is corpus-native. It can affect determinant weights only after `A`, `tau`,
`chi`, and the physical quotient domain are selected before comparison. The
current corpus does not yet select the needed numerical factor.

A global non-Abelian section obstruction is also legal in principle. The
gauge-fixing corpus identifies Gribov/global-section failure as a real
projection issue. Since the local FP quotient has already been counted, this
route would have to be a separate selected fundamental-domain or global-section
measure, not another local ghost determinant.

The best next route is a genuinely different selected SU3 threshold operator:
a nontrivial SU3 color bundle connection, curvature, flux twist, or associated
endomorphism. The prior Weitzenbock calculation used the canonical Nil tangent
bundle data and should not be double-counted. A selected color-bundle
connection would be new operator data, not a fitted projector factor.

The mathematically adjacent route is analytic torsion. The `p != 0` Nil Hodge
complex is acyclic, so Ray-Singer/Reidemeister torsion is the natural invariant
to audit. This is legal only after selecting the local system, lattice
character, and color trace independently.

## Ranking

```text
best next route:
  nontrivial SU3 color-bundle connection / endomorphism

second route:
  global section / Gribov / fundamental-domain measure

mathematical invariant route:
  Ray-Singer or Reidemeister torsion for the selected acyclic local system

do not use as extra:
  local FP/BRST quotient Jacobian
  soft gauge-tube width
  complex nesting/shared-circle phase correction without a direct SU3 source
```

## Verdict

The next rigorous gate is not to hunt for a small numerical factor. It is to
construct the selected SU3 color-bundle threshold operator, or else the selected
global-section measure, and compute its determinant without using the target.

Next artifact:

```text
Selected_Qa_SU3_Color_Bundle_Connection_or_Global_Section_Determinant_v1
```
