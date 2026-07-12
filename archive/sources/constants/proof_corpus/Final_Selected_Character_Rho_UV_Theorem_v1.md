# Final Selected-Character Rho-UV Theorem v1

## Purpose

This theorem consolidates the rho_UV branch after the selected character-channel
covariance closure.

It answers exactly what is now proved and what remains outside this branch.

## Theorem

On the symmetric Iwasawa/Strominger branch in internal `alpha'=1` units, with
the unresolved disturbance channel identified with the selected Z64 character
line `q_64=15`, the remaining scale ratio is

```text
rho_UV(R) = [64(2pi)^2/(16 R^4 + 8)]^2.
```

Consequently the reduced scale minimizer is

```text
s_*(R) = (60 rho_UV(R))^(1/6).
```

## Proof

The heterotic curvature source gives

```text
Tr_grav R_+^2 = v1_tilde alpha_1,
U_raw = (v1_tilde,0,0).
```

On the symmetric Iwasawa slice `r1=r2=R`,

```text
r3^2 = 8(2pi)^2/(16+8/R^4),
v1_tilde(R) = 8 r3^2/R^4 = 64(2pi)^2/(16R^4+8).
```

The selected finite coefficient quotient closes the response-row metric:

```text
G_11 = 1,
||U_raw||_coeff^2 = v1_tilde(R)^2.
```

The Z64 CP carrier corpus supplies the finite character carrier

```text
K_64 = C[Z_64],
K_64 = direct_sum_{q in Z_64} E_q K_64,
```

with physical labels represented by character projectors. The exact branch
selects

```text
q_64 = 15.
```

Thus the selected character-channel covariance is

```text
Q_char = E_15 = |15><15|
```

on the one-dimensional selected character line. The retarded kernel is

```text
K_ret,64 = S^-1.
```

In the character basis, `S^-1` acts by a unit phase, so it preserves norm on
`E_15 K_64`. Therefore

```text
||D_raw||_coeff^2 = 1.
```

Hence

```text
rho_UV(R)
  = ||U_raw||_coeff^2 / ||D_raw||_coeff^2
  = v1_tilde(R)^2
  = [64(2pi)^2/(16R^4+8)]^2.
```

The scale-lifting extraction already proved

```text
s_* = (60 rho_UV)^(1/6),
```

so the stated expression for `s_*(R)` follows.

## Evaluated Values

These values are branch evaluations, not independent selections of `R`:

| R | r3 | rho_UV | s_* |
|---:|---:|---:|---:|
| 1 | 3.627598728468436 | 11082.9899132021 | 9.34260594395577 |
| 2 | 4.375048680836414 | 91.5949579603476 | 4.20084963151094 |
| 5 | 4.441106850564644 | 0.0637360035033962 | 1.25051626958438 |

## What Is Closed

```text
UV response row U_raw                         CLOSED
coefficient response metric G_11              CLOSED
retarded kernel action on selected character  CLOSED
selected-character disturbance norm           CLOSED
rho_UV(R) branch function                     CLOSED
s_*(R) branch function                        CLOSED
```

## Remaining Outside This Theorem

This theorem does not select a unique numeric `R`.

The present corpus supports the symmetric Iwasawa branch and the exact formula
above, but it does not source-certify one physical value of the Iwasawa radius
`R` for this non-SM scale branch. Therefore a single number for `rho_UV` or
`s_*` requires one additional branch-selection theorem:

```text
Selected Iwasawa radius theorem:
  derive R from the same MTT/Strominger branch data, without fitting rho_UV,
  electroweak data, or any target constant.
```

If a future source selects `R=R_*`, this theorem immediately gives

```text
rho_UV = [64(2pi)^2/(16R_*^4+8)]^2,
s_* = (60 rho_UV)^(1/6).
```

## Verdict

The rho_UV branch is closed as a selected-character branch theorem:

```text
rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2.
```

It is not yet a single absolute number, because `R` is not yet selected by a
source-certified no-knob theorem.
