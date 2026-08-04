# Spectral Action Einstein IR Limit and Vacuum Obstruction v1

Date: 2026-07-15

## New result

The A51-A53 spectral route now has an explicit gravitational calculation rather
than a qualitative statement that it contains Einstein and Weyl terms.

The active A49 finite Dirac operator is `96x96` and has exactly

```text
Y_u, Y_d, Y_e, Y_nu.
```

Its neutral channel is Dirac. There is no particle-antiparticle Majorana block,
so the Majorana invariants `c_R,d_R` in the standard spectral-action gravity
formula vanish on this branch. This conclusion is exact for A49; adding a
Majorana block in a later model would reopen it.

The canonical 96-state coefficients are

```text
1/kappa_0^2 = (96 f2 Lambda^2-f0 c_R)/(12 pi^2),
alpha_0     = -3 f0/(10 pi^2),
gamma_0     = (48 f4 Lambda^4-f2 Lambda^2 c_R+(f0/4)d_R)/pi^2.
```

They come from Theorem 3.13 and equations (4.11)-(4.12) of
<https://arxiv.org/abs/hep-th/0610241>. In this repository's convention,

```text
2 kappa_h = 1/(2 kappa_0^2),
kappa_h   = (96 f2 Lambda^2-f0 c_R)/(48 pi^2).
```

## Exact Einstein/Weyl crossover

The primary weak-field calculation gives

```text
(Box-beta^2) Box h_TT = source,
beta^2 = -1/(32 pi G4 alpha_0) = -kappa_h/alpha_0.
```

See equations (13), (15), and (32) of
<https://arxiv.org/abs/1005.4276>. Since `alpha_0<0`, the extra scale is real.
At Euclidean momentum `p`, the retained TT kernel has shape

```text
K_TT(p) proportional to p^2(1+p^2/beta^2),
epsilon_W(p)=p^2/beta^2.
```

Under the A53 one-atom premise

```text
f2=f0/tau_int,
f4=f0/tau_int^2,
tau_int=log(448)/15=0.4069862154943323,
```

the fitted/profile normalization `f0` cancels completely from the dimensionless
gravity ratio:

```text
beta^2/Lambda^2 = 20/(3 tau_int)
                      = 16.3805711664441,
beta/Lambda       = 4.047291831143895.
```

Hence, for `p<=eta Lambda`,

```text
epsilon_W(p) <= (3 tau_int/20) eta^2.
```

Numerically the bound is `6.10479323%` at `eta=1`,
`1.52619831%` at `eta=0.5`, and
`0.06104793%` at `eta=0.1`. The meaningful theorem is the quadratic
infrared suppression as `eta` tends to zero. The value at the cutoff is only a
diagnostic because the heat-kernel expansion itself is asymptotic there.

This closes the Einstein-versus-Weyl ratio inside the retained `a4` action,
conditional on the A53 one-atom tier. It does not yet bound all omitted higher
heat-kernel terms and does not select the one-atom measure.

## Vacuum obstruction

The same calculation exposes rather than hides the cosmological problem. With
`c_R=d_R=0`, the bare geometric constant is

```text
gamma_0 = 48 f4 Lambda^4/pi^2.
```

Writing its curvature-equivalent magnitude relative to
`2 kappa_h(R-2 Lambda_bare)` gives

```text
|Lambda_bare|/Lambda^2
  = gamma_0/(4 kappa_h Lambda^2)
  = 6 f4/f2
  = 6/tau_int
  = 14.74251404979969.
```

Thus the one-atom law does not solve `Lambda_eff`; it produces an order-cutoff
bare term. The physical value still requires a selected Higgs-vacuum,
subtraction, cancellation, or renormalized source theorem, and its Lorentzian
sign requires the still-open Wick reconstruction.

## What advanced

Closed at the stated tier:

- `c_R=d_R=0` for the active A49 Dirac-only finite operator;
- the canonical Einstein/Weyl coefficient map into `kappa_h`;
- the exact crossover `beta^2/Lambda^2=20/(3 tau_int)`;
- a quantitative IR Weyl bound depending only on exact `tau_int`;
- a no-go for the A53 point measure solving the vacuum term by itself.

Still open:

- an unconditional MTT selection theorem for the A53 one-atom law;
- a controlled bound on the full asymptotic spectral remainder;
- the Lorentzian/Wick source map;
- one absolute Newton scale, `Lambda_eff`, and q79 zero/gap matching;
- selection of this spectral action over the direct two-derivative exit.

The next honest target is
`MTT_Selected_OneAtomProperTimeLaw_and_SpectralRemainderBound_or_DirectTwoDerivativeActionSource_v1`.
