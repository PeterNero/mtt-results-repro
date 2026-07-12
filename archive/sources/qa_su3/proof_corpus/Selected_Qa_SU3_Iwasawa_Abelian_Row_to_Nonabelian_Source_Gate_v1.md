# Selected Qa/SU3 Iwasawa Abelian Row to Nonabelian Source Gate v1

## Purpose

This checks whether the explicit Iwasawa abelian Chern/Bianchi row can be used
as the missing selected Qa/SU3 source packet.

## Result

The row has real same-branch support:

```text
L_(1,2,0) plus L_(-1,-2,0)
c1 cancels in L + L^-1 + O
the Chern/Bianchi row remains on the Iwasawa branch
```

But the split determinant-one embedding

```text
E_split = L_(1,2,0) + L_(-1,-2,0) + O
```

is still reducible abelian support. It is not a selected nonabelian SU3
color-threshold source and it does not supply `endomorphism_E` or a finite
determinant part.

## Best Live Promotion

The best current route is a non-split extension:

```text
0 -> L_(1,2,0) -> E -> L_(-1,-2,0) + O -> 0
```

This is the right kind of move because it could preserve the same Chern/Bianchi
shadow while replacing the split abelian packet by a genuine SU3 bundle. It is
not closed yet, because the current source record does not select:

```text
extension class eta,
stability or HYM certificate,
transition matrices with det=1,
Chern connection or rho_E response,
endomorphism_E,
heat/spectrum/torsion finite part.
```

## Guardrail

Arbitrary invariant `su(3)` matrices are not allowed as a shortcut. They would
turn the construction into a knob unless the same MTT branch selects them.

## Status

```text
det-one topological embedding tested: yes
split embedding accepted as closure: no
non-split extension route identified: yes
selected extension class found: no
selected transition/operator data found: no
determinant computable now: no
Qa/SU3 closed: no
full SM closure achieved: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Ext_Stability_Source_Search_v1
```
