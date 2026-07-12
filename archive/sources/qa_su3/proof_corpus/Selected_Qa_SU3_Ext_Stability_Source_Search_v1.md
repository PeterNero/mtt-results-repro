# Selected Qa/SU3 Ext Stability Source Search v1

## Purpose

This searches the current corpus for the missing non-split/stable SU3 source
after the abelian Iwasawa row was rejected as closure.

## Finding

The wider strings/flux corpus does contain an explicit Iwasawa SU3 monad in:

```text
C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md
```

The printed structure is:

```text
0 -> K1 -> direct_sum_i L_i -> K2 -> 0
E = ker(g) / im(f)
```

with:

```text
ell1 = (-2, 0, 1)
ell2 = (-1, 1,-1)
ell3 = ( 1,-1, 0)
ell4 = ( 1, 0,-1)
ell5 = ( 2, 1, 1)
kappa1 = (1,0,0)
kappa2 = (0,1,0)
```

## Recomputed Chern Data

Using:

```text
(x a + y b + z c)^2 = 2(xy alpha1 + xz alpha2 + yz alpha3)
(x a + y b + z c)^3 = 6xyz a b c
```

the script recomputes:

```text
sum ell_i = (1,1,0) = kappa1+kappa2
c1(E)=0
c2(E)=0
integral c3(E)=6
```

So this closes the blank-source part of the search: the corpus has a real
indecomposable/HYM-flavored SU3 monad on the Iwasawa branch.

## Why This Is Not Closure

The decisive nuance is:

```text
c2(E)=0
Tr F_E wedge F_E=0
```

The alpha1 Chern/Bianchi support row still comes from the abelian flux plus
gravitational/torsion contribution, not from this monad determinant.

Therefore the monad and abelian row complement each other:

```text
monad: non-split SU3/HYM-flavored source candidate
abelian row: explicit alpha1 Bianchi support
missing: selected Qa/SU3 threshold representation and operator packet
```

## Status

```text
explicit Iwasawa SU3 monad found: yes
integer Chern character recomputed: yes
HYM existence claim present: yes
same paper contains abelian Bianchi row: yes
Qa/SU3 threshold representation identified: no
same-source rho_E or D_E supplied: no
endomorphism_E computed: no
finite determinant part computed: no
Qa/SU3 closed: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Monad_to_Operator_Packet_Transfer_Gate_v1
```
