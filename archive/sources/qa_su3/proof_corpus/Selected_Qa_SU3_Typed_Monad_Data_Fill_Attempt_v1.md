# Selected Qa/SU3 Typed Monad Data Fill Attempt v1

## Purpose

This artifact attempts the next fill step for the selected Qa/SU3 typed monad
interface. It asks exactly what can be filled from the corpus before any
comparison with the Qa/SU3 residual.

## Source Result

The heterotic flux source supplies the Iwasawa monad topology:

```text
0 -> K1 -> direct_sum_i L_i -> K2 -> 0
E = ker g / im f
rank(E) = 3
ell_i = [(-2,0,1), (-1,1,-1), (1,-1,0), (1,0,-1), (2,1,1)]
kappa_a = [(1,0,0), (0,1,0)]
c1(E) = 0
c2(E) = 0
integral c3(E) = 6
```

The source also says that generic holomorphic maps `f,g` exist as constant
matrices in the left-invariant frame and that the resulting bundle has a
Li-Yau/HYM existence claim. This is useful, but it is not yet the missing typed
packet: the actual matrices are not printed.

## Failed Fill Slots

```text
f_map.matrix: open
g_map.matrix: open
g*f=0 machine check: open
locally-free certificate for the exact maps: open
Cech/Dolbeault cochain matrices: open
representation and trace normalization: open
D_E packet: open
rho_E packet: open
finite determinant/threshold response: open
```

The existing validator still refuses the open template:

```text
validator exit code: 2
validator output: OPEN: packet status is open
```

## Guardrails

The fill attempt deliberately does not use generic existence of `f,g` as a
typed matrix packet. It also does not use the printed or repaired `A01` matrix
as source-certified operator data, and it does not replace an operator packet
with Chern classes, identity `rho_E`, or the observed Qa/SU3 residual.

## Verdict

```text
topological monad data filled: yes
typed maps filled: no
cochain/Dolbeault packet filled: no
D_E operator packet filled: no
rho_E packet filled: no
determinant computable now: no
Qa/SU3 closed: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Monad_Map_Construction_or_Source_Augmentation_v1
```
