# TT Helicity-2 Z64 Carrier Functor v1

## Construction

The TT plus/cross plane is the real form of the complex helicity-2 character.
On the finite central circle `Z64`, this gives the real character pair:

```text
c_2(j) = sqrt(2/64) cos(2 * 2*pi*j/64)
s_2(j) = sqrt(2/64) sin(2 * 2*pi*j/64)
```

Define:

```text
U_TT(TT_plus)  = |d_*> tensor c_2
U_TT(TT_cross) = |d_*> tensor s_2
```

where `d_*=(2,2,2,2,2)` is the selected exact central-circle tower with
`C(d_*)=15`.

## Computed Checks

The pair `(c_2,s_2)` is orthonormal in the canonical group-algebra inner
product on `C[Z64]`. The retarded kernel `S^-1` preserves this plane, acting as
a rotation by the sampled helicity-2 angle.

Since `L_64=L_tower` and `L_tower |d_*> = 15 |d_*>`, compression gives:

```text
U_TT^* L_64 U_TT = 15 I_2.
```

## Important Caveat

This is the canonical helicity-2 carrier functor, but it is not yet a full
source-certified GR identity. The character label is `k=2`, so it has order
`32`, not primitive order `64`. That is exactly what spin-2 periodicity predicts,
but the corpus still needs to state that this helicity-2 fiber over the selected
exact tower is the selected GR TT `A_int` projector/window.

## Status

Closed:

```text
canonical TT helicity-2 -> Z64 carrier functor
compression to 15 I_2
retarded-kernel invariance of the polarization plane
```

Still open:

```text
source-certified identification of this carrier functor with the selected GR TT Aint projector/window
```
