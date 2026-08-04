# Massless TT Pole versus Positive Internal Gap: No-Go v1

Date: 2026-07-15

## Exact contradiction

The explicit metric source calculation has

```text
lambda_gap = 15,
DG_metric = 2 I,
DG_strain = I.
```

Consequently, at zero external momentum,

```text
Delta_metric(0) = 4/15 I,
Delta_strain(0) = 1/15 I.
```

Those are exactly the matrices already emitted by the metric-source packet.
They are finite.  In contrast, a normalized massless graviton propagator has

```text
Delta_TT(E) = F(E)/E,
F(0)=1,
```

and hence a nonzero `1/E` pole.

## General no-go theorem

Let the compressed positive Stieltjes measure be supported in
`[lambda_gap,infinity)` with `lambda_gap>0`. Then

```text
0 <= E/(E+s) <= E/lambda_gap.
```

After integration,

```text
lim_(E->0) E Delta_TT(E) = 0.
```

Therefore no bounded source map supported only on the positive `lambda=15`
eigenspace can produce a massless graviton pole.  This is independent of basis
normalization and does not depend on a numerical approximation.

## Necessary repair

A positive Stieltjes propagator has a massless pole precisely when its
compressed measure contains a zero atom:

```text
nu_TT = r0 delta_0 + nu_gap,
Delta_TT(E) = r0/E + integral (E+s)^(-1) nu_gap(ds).
```

Canonical normalized fields set `r0=1`.  The corrected carrier is therefore

```text
massless channel: E_TT tensor |0_int>,
gapped channel:   E_TT tensor |d_*>,  lambda(d_*)=15.
```

The external associated bundle `E_TT` carries helicity two and its Chern
class.  The internal factor of the massless channel can consequently be the
trivial coherent zero mode; helicity no longer has to be encoded by an internal
positive-gap character.

## What survives

The `d_*` Fourier rows, exact `Z64` support, and `lambda=15` calculation remain
correct. Their physical role changes: they describe a gapped correction or
suppression channel, not the location of the graviton pole.  The old statement
`lambda_GR,TT=15` is superseded only as a physical pole identification.

The next executable object is now unambiguous: compute the coherent-zero-mode
TT source row and its normalized residue from the same selected action.  The
full physical source cannot obey the old exhaustion statement
`Pi_exact64 B^*P_TT=B^*P_TT`; that identity remains valid only for its gapped
`d_*` component.
