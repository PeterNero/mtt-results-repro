# MTT Selected q79 Validated Beta Transport and Finite-Flat Contour Homotopy

## Purpose

A125 certified the transverse Picard-Lefschetz wall, proved its local jump
nonzero, and supplied the selected-side Abel-Jacobi base lift as an ACB ball.
It did not certify the endpoint beta vector. A126 closes that endpoint problem
for the frozen A124 selected carrier and its `ell=0` representative.

The proof has two independent parts:

1. a complex argument-principle certificate showing that a local lower contour
   preserves the smooth genus-two family and the symmetric splitting divisor;
2. a defect-corrected order-28 Taylor-model integration from the A125 base ball
   to the endpoint.

No observed Standard-Model value or desired beta endpoint enters either part.

## Why the full lower contour is retired

The first validated transport used the broad contour

```text
0 -> -0.1 i -> 1-0.1 i -> 1.
```

Its endpoint agrees numerically with the selected result, but endpoint
agreement does not establish a common analytic branch. A 3,231-leaf interval
cover of the full rectangle gives clockwise boundary windings

```text
reduction determinant  -4
q leading coefficient   0
G-on-Q norm             -1.
```

Thus the broad strip encloses four zeros of the reduction determinant and one
zero of the divisor norm. It is not homotopic to the straight contour through
the smooth marked family. A126 keeps this as a negative diagnostic and does not
use the broad transport in its theorem.

## The selected local contour

The contour actually promoted is

```text
0
 -> 0.65
 -> 0.65-0.1 i
 -> 0.82-0.1 i
 -> 0.82
 -> 1.
```

Only its middle detour differs from the straight path. The homotopy rectangle
is

```text
0.65 <= Re(lambda) <= 0.82,
-0.1 <= Im(lambda) <= 0.
```

For `w=1/4+i/4+i lambda`, the real part of `w` is separated from the real
coordinates of the square-lattice poles. The elliptic uniformization is
therefore holomorphic on the closed rectangle.

## Interval argument-principle execution

Each of the four oriented boundary edges is divided into initial chunks. On
every chunk, order-10 Taylor models enclose the elliptic coordinates and the
following five holomorphic or quotient-algebraic obstruction functions:

```text
Delta_F   = determinant of the 11 x 11 genus-two reduction system,
ell_1     = active y-chart scale,
q_2       = leading coefficient of Q2,
Delta_Q   = q_1^2-4 q_2 q_0,
N_G       = Norm_{O[t]/(Q2)}(G3).
```

Taylor-model LU elimination encloses `Delta_F`. Each accepted leaf supplies a
disk that excludes zero and an argument sector of half-width below the frozen
radius gate. Adjacent sectors overlap and have unique argument transitions.
Summing those transitions around the clockwise boundary gives an integer
winding without sampling an unbounded interior grid.

The final cover has

```text
accepted leaves                         1541
maximum bisection depth                   14
minimum |Delta_F| lower bound       2.02009e20
minimum |ell_1| lower bound          1.57359256
minimum |q_2| lower bound            0.01337001
minimum |Delta_Q| lower bound        1.59945799
minimum |N_G| lower bound         7194.05761707.
```

The certified clockwise windings are

```text
Delta_F    0
ell_1      0
q_2        0
Delta_Q   -1
N_G        0.
```

Consequently the reduction system is regular everywhere in the rectangle,
the `y` chart is global there, and `Q2` remains a genuine degree-two finite
family. The only interior event is one zero of `Delta_Q`, counted with
multiplicity.

## Finite-flat symmetric-divisor theorem

The discriminant zero exchanges the two roots of `Q2`; it does not destroy the
degree-two divisor used by MTT.

After division by the unit `q_2`, write

```text
A = O_S[t]/(t^2-S t+P).
```

This is a free rank-two `O_S` algebra with basis `(1,t)`, including at
`S^2-4P=0`. For `g=g_0+g_1 t`, multiplication by `g` has determinant

```text
N_A(g)=g_0^2+S g_0 g_1+P g_1^2.
```

The interval winding of `N_G` is zero, so `G3` is a unit in `A` throughout the
rectangle. On the hyperelliptic family

```text
U^2=G3^2+Q2 H4,
```

the ideal `(Q2,U-G3)` is then a finite flat relative divisor of degree two.
Locally, `U+G3` is a unit and

```text
U-G3 = Q2 H4/(U+G3),
```

so the divisor is Cartier even when its two points coalesce. Its image in the
relative symmetric square and relative Picard scheme is holomorphic. The two
individual root labels braid once, but their unordered divisor and Abel-Jacobi
class do not acquire a branch ambiguity.

This is also why A126 evaluates the source by the exact finite-algebra trace.
For a quadratic polynomial `Q=q_0+q_1 t+q_2 t^2`, the potentially singular
rootwise velocity terms combine into quotient-algebra expressions; in
particular the relevant quadratic trace reduces exactly to its coefficient
formula rather than dividing by the root separation. The source therefore
extends through the discriminant zero certified above.

**Q79FiniteFlatSymmetricDivisorHomotopyTheorem.** On the selected local
rectangle, the genus-two family is smooth and the splitting divisor is a
finite flat symmetric Cartier divisor. The straight and local lower contours
are homotopic for the normal function, despite one exchange of the individual
`Q2` roots. Analytic continuation along both contours reaches the same selected
endpoint branch.

## Validated endpoint transport

Starting from the A125 five-component ACB base lift and eight zero beta rows,
A126 integrates the triangular 13-component system. Its principal safeguards
are:

- order-28 Taylor models for the elliptic, Gauss-Manin and source fields;
- a Taylor-polynomial right inverse with a strict contraction certificate;
- exact finite-quadratic quotient traces instead of rootwise singular bounds;
- a moving five-dimensional fundamental frame for lift-error coordinates;
- separate lift and beta defect budgets;
- adaptive rejection and bisection with an atomic checkpoint;
- six independent ACB-versus-floating point audits.

The execution records

```text
accepted steps                         160
rejected trial steps                    69
minimum accepted step          4.7568179e-5
total contour length                   1.2
maximum lift component radius   0.00227353
maximum beta component radius   0.03789568.
```

Every accepted step satisfies

```text
transformed lift correction < 1e-6,
beta increment error         < 1e-3,
global beta radius           < 0.5.
```

The independent point audit has maximum relative differences

```text
connection  1.62532461e-10
source      1.62539166e-10
residue     4.65654576e-15.
```

The endpoint center is approximately

```text
(-0.2676528621 +0.7559116502 i,
 -0.3638213017 +0.3499763594 i,
  0.2956617857 -0.0507264157 i,
 -0.5354816657 -0.1170627760 i,
 -0.5830710763 -0.5989566497 i,
  1.0267955254 +0.9650686641 i,
  0.5041697622 -0.8881641643 i,
 -0.7292243636 -0.0941686529 i).
```

The serialized center differs from the internal Arb center by at most
`9.1127779293812082e-17` per component. After adding that conversion radius,
the self-contained packet has `r<=0.037895684949451225` and

```text
||beta_center||_2                 2.3571952407293737
||beta||_2 lower bound            2.2500100575075090
maximum component absolute lower  1.3712411349795079.
```

The endpoint ball therefore excludes zero by a wide margin.

## Selected-side theorem and strict scope

**Q79FiniteFlatContourAndSelectedSideBetaNonzeroTheorem.** The validated local
lower contour is in the same smooth-family and symmetric-divisor homotopy class
as the selected straight contour. Its endpoint beta enclosure excludes zero.
Therefore `beta(1)=0`, equivalently the frozen selected `ell=0` representative,
is impossible on this A124 selected-side carrier.

A126 closes:

- a rigorous local contour homotopy in the smooth genus-two family;
- finite-flat continuation through one `Q2` root collision;
- collision-safe exact quotient-trace source transport;
- the selected-side endpoint beta nonzero interval;
- exclusion of the frozen selected `ell=0` branch.

A126 does not close:

- a global `ell=0` no-go over all PGL3 carriers;
- interval certification of the full `8 x 92` period lattice;
- selection or exclusion of a nonzero integral `ell in Z^92`;
- the normalized Deligne-pairing zero/no-go decision;
- the remaining K3, gerbe, HYM, Bianchi or full U6/SM closure gates.

The next proof object is an interval period-lattice certificate: enclose the
selected `8 x 92` period map in the same marking and prove a positive distance
from the endpoint beta ball to its integral image, or exhibit and certify the
unique nonzero integral branch that meets it.
