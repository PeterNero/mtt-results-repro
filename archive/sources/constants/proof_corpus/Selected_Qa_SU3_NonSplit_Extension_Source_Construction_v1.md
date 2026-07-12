# Selected Qa/SU3 NonSplit Extension Source Construction v1

## Purpose

The previous gate selected the non-split rank-3 SU3 extension route as the best
path forward.  A wider corpus scan found an explicit Iwasawa source in:

```text
C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md
```

That paper gives an indecomposable SU3 monad on the complex Iwasawa threefold.

## Printed Monad Data

The bundle is defined by:

```text
0 -> K1 -> direct_sum_i L_i -> K2 -> 0,
E = ker(g) / im(f).
```

The line classes are:

```text
ell1 = (-2, 0, 1)
ell2 = (-1, 1,-1)
ell3 = ( 1,-1, 0)
ell4 = ( 1, 0,-1)
ell5 = ( 2, 1, 1)
kappa1 = (1,0,0)
kappa2 = (0,1,0)
```

Using:

```text
(x a + y b + z c)^2 = 2(xy alpha1 + xz alpha2 + yz alpha3)
(x a + y b + z c)^3 = 6xyz a b c
```

we recompute:

```text
sum ell_i = (1,1,0) = kappa1+kappa2
c1(E) = 0
sum ell_i^2 - sum kappa_a^2 = (0,0,0)
c2(E) = 0
sum ell_i^3 - sum kappa_a^3 = 18
ch3(E) = 3
integral c3(E) = 6
```

So the printed integer Chern-character claims check out.

## What This Closes

```text
non-split rank-3 SU3 source candidate found in the wider corpus: yes
integer Chern-character recomputed: yes
c1=0, c2=0, integral c3=6 verified from printed line data: yes
HYM existence source claim present: yes
same Iwasawa paper also contains the abelian alpha1 Bianchi support row: yes
```

This is genuine progress.  The source problem is no longer only a blank
template: the corpus contains a concrete Iwasawa SU3 monad with the right
indecomposable/HYM flavor.

## What Remains Open

```text
Qa/SU3 threshold representation identified: no
same-source rho_E transition packet: no
operator packet filled: no
endomorphism_E computed: no
finite determinant computed: no
Qa/SU3 closed: no
```

The key nuance is that the monad has:

```text
c2(E) = 0
Tr F_E wedge F_E = 0
```

while the alpha1 component Bianchi row comes from the hidden abelian flux plus
gravitational/torsion terms:

```text
u1 = 8(2*pi)^2,
u2 = u3 = 0.
```

Thus the monad and the abelian Bianchi row complement each other, but neither
alone is the selected Qa/SU3 threshold determinant.

## Consequence

The right next step is no longer "find any non-split SU3 source."  We found one.
The new gate is sharper:

```text
Can the explicit Iwasawa monad be transferred into the Qa/SU3 operator packet?
```

That means deciding whether this `E` is the selected Qa/SU3 threshold source or
only a visible `E8 -> E6` benchmark, then deriving the representation trace,
rho_E transition data or left-invariant `D_E`, and the Weitzenbock
endomorphism_E.

Next artifact:

```text
Selected_Qa_SU3_Monad_to_Operator_Packet_Transfer_Gate_v1
```
