# Selected Character-Channel Covariance Closure for Rho-UV v1

## Purpose

The carrier covariance computation reduced the remaining finite-memory
disturbance scalar to

```text
d = p^T Q_tau p.
```

Under Z64-equivariance and deck-coordinate projection this was

```text
d = (Q_tau)_{00}.
```

That left multiple natural equivariant normalizations. This note tests a
stronger selection: the physical carrier is not the whole deck register averaged
over all 64 positions, but the selected CP character line.

## Character Carrier Source

The Z64 carrier corpus states:

```text
K_64 = C[Z_64],
U_64 |q> = exp(2 pi i q/64) |q>,
E_q = (1/64) sum_{r=0}^{63} exp(-2 pi i q r/64) U_64^r,
K_64 = direct_sum_{q in Z_64} E_q K_64.
```

It also states that the physical CP labels are the character projectors. The
exact branch certificate closes:

```text
selected component: q_64 = 15.
```

Thus the selected dyadic CP carrier is the one-dimensional character line

```text
E_15 K_64.
```

## Covariance on the Selected Character Line

On a one-dimensional selected character line, the coefficient Hilbert norm fixes
the unit vector `|15>_char` by

```text
<15|15> = 1.
```

The selected character-channel covariance is therefore the rank-one projector

```text
Q_char = E_15 = |15><15|
```

when written on the retained character channel. In that selected coordinate,

```text
p = <15|,
d = p Q_char p^* = 1.
```

This differs from the deck-basis diagonal value of the same projector. In the
deck basis, `E_15` has diagonal entries `1/64`; that number answers a different
question: "what is the variance at one deck position if the selected character
projector is spread over the regular representation?" The physical selected
channel is the character coordinate, not a single deck-position coordinate.

## Retarded Kernel Check

The selected retarded kernel is

```text
K_ret,64 = S^-1.
```

In the character basis,

```text
S^-1 |q> = exp(-2 pi i q/64) |q>.
```

Therefore on the selected line `q=15`, the retarded kernel is a unit complex
phase. It does not change the norm:

```text
||K_ret,64 |15>||^2 = || |15> ||^2 = 1.
```

Hence

```text
||D_raw||_coeff^2
  = <15| K_ret Q_char K_ret^* |15>
  = 1.
```

## Rho-UV Closure on the Character-Channel Branch

The previous coefficient-normalization result closed

```text
G_11 = 1,
U_raw = (v1_tilde,0,0),
v1_tilde(R)=64(2pi)^2/(16R^4+8).
```

Combining with `d=1` gives

```text
rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2,
s_* = (60 rho_UV)^(1/6).
```

Evaluated values:

| R | rho_UV | s_* |
|---:|---:|---:|
| 1 | 11082.9899132021 | 9.34260594395577 |
| 2 | 91.5949579603476 | 4.20084963151094 |
| 5 | 0.0637360035033962 | 1.25051626958438 |

## What This Closes and What It Does Not

This closes the covariance scalar for the selected character-channel branch:

```text
d_char = 1.
```

It does not prove that every possible unresolved Z64/Strominger disturbance must
be character-channel supported. The remaining identification premise is:

```text
the non-SM rho_UV disturbance channel is the same selected q_64=15 character
channel, not a full-register deck-position covariance or a trace-one mixed
state over all 64 characters.
```

That premise is strongly aligned with the CP corpus, because physical CP labels
are explicitly character projectors and the selected component is `q_64=15`.
But it should be named whenever the result is used.

## Verdict

The strongest rigorous closure currently available is:

```text
Selected character-channel branch:
  ||D_raw||_coeff^2 = 1,
  rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2.
```

The result is no-knob on that branch: the value comes from rank-one character
projector normalization, the unitary retarded kernel, and the already selected
`q_64=15` character line.
