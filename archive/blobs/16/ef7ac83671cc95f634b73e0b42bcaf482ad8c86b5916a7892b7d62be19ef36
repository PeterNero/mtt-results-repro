# MTT Selected q79 Genus-Two Integral Surface-Cycle Presentation v1

Status: `MTT_U6_Q79_INTEGRAL_SURFACE_CYCLE_PRESENTATION_CLOSED_THIMBLE_PERIOD_EXECUTION_OPEN`

Supersession notice: A119 preserves the rank calculation below but replaces
the claimed primitive `86+4` integral splitting. Period continuation detects
the central lift `B_period=-B_braid`, for which the handle-only Fox quotient
has an index-three defect. The defect disappears only after the thimble tails
are attached to the handle relations. The final primitive primary basis is the
A119 coupled `82+8` basis, not the preliminary direct sum in this note.

## Why A117 is needed

A116 closes the integral `H1` Gauss-Manin representation, its 90 ordered
positive Picard-Lefschetz factors, and the punctured-torus surface relation.
It does not make the 90 meridian loops and the two handle loops into 92 closed
surface cycles.  They are path carriers for local-system transport.  Period
columns require the integral cellular presentation of `H2(C,Z)`.

This distinction removes an ambiguity in the A116 readiness shorthand without
reopening any A116 monodromy result.

## The saturated thimble kernel

Let `v_j in Z^4`, `j=1,...,90`, be the A116 ordered vanishing cycles and set

```text
delta: Z^90 -> H1(C_e,Z)=Z^4,
delta(n_1,...,n_90)=sum_j n_j v_j.
```

The exact Smith diagonal of the `4x90` matrix `V=(v_1 ... v_90)` is

```text
diag(1,1,1,1).
```

More strongly, the lexicographically first unimodular four-column block is
formed by distinguished factors `d001,d002,d003,d005`, with root labels
`a23,a56,a15,a10` and determinant `+1`.  Solving every other boundary against
this block gives an explicit `90x86` matrix `K` satisfying

```text
V K = 0.
```

The nonpivot rows of `K` are the `86x86` identity.  Therefore its columns are
an integral basis, not merely a rational basis, and

```text
ker(delta) = Z^86
```

is saturated in `Z^90`.

## The four handle classes

The saved matrices obey the anti-homomorphic path convention

```text
M(gamma then eta)=M(eta) M(gamma).
```

Thus `rho(g)=M(g)^-1` is the homomorphism used by the cellular chain complex.
For the punctured-torus boundary word

```text
r=A B A^-1 B^-1,
```

the Fox derivatives are

```text
d_A r = 1-A B A^-1,
d_B r = A-r.
```

Evaluation under `rho` gives the `8x4` relative boundary matrix

```text
D_Fox = [ I-rho(A)rho(B)rho(A)^-1 ]
        [ rho(A)-rho(r)              ].
```

A116 implies exactly

```text
rho(r)=(M_90 ... M_1)^-1.
```

The computed Smith diagonal of `D_Fox` is again

```text
diag(1,1,1,1).
```

Hence its image is primitive and

```text
((Z^4)_A direct_sum (Z^4)_B) / image(D_Fox) = Z^4.
```

The packet includes an explicit `8x4` complement `C`; the determinant of the
square completion `[D_Fox C]` is `+1`.  This certifies the four handle classes
integrally and excludes hidden torsion.

## Rank-92 reconciliation

A104 proves

```text
H1(C,Z)=Z^2,
b2(C)=92.
```

The Lefschetz cellular filtration now has

```text
86 closed thimble classes,
 4 punctured-torus handle classes,
 2 Leray edge classes,
--------------------------------
92 integral surface classes.
```

The first two summands form the rank-90 primary extension lattice.  The
remaining rank-two extension splits abstractly because all groups are free
abelian.  A concrete period basis still requires explicit geometric lifts of
those two edge classes; A117 does not silently identify them with the A/B path
carriers.

This is the genus-one-base analogue of the standard thimble-kernel,
boundary-loop quotient, fiber, and horizontal-class construction used in
effective Lefschetz period algorithms.  The implementation was checked against
the public `lefschetz-family` homology construction and the effective-period
framework of Lairez, Pichon-Pharabod, and Vanhove.

## Preliminary period assembly, superseded by A119

The next numerical calculation is now typed as follows:

```text
T: 8x90 primitive thimble integrals,
T K: 8x86 closed-thimble periods,
H: 8x8 primitive A/B handle-cylinder integrals,
H C: 8x4 handle periods, including the Fox boundary match,
E: 8x2 periods on explicit Leray edge lifts.
```

This was the A117 contract. A119 proves that `T K` and `H C` cannot be promoted
as separate primitive integral blocks. It replaces them by

```text
[T | H] B_coupled,   B_coupled in Mat(98,90;Z),
```

and then appends the two Leray columns. Only the A119 assembly gives the
integral `8x92` table on the selected period lifts. Only after that assembly
may one test

```text
z = Pi ell,  ell in Z^92,
```

or prove a separation bound.

## Exact scope

A117 closes at its retained scope:

- the saturated rank-86 thimble kernel;
- the preliminary projective-braid Fox calculation and rational rank count;
- the need for two Leray edge classes in the final rank `92`;
- the correction that transport paths are not automatically `H2` basis cycles.

A119 supersedes the old claims of a torsion-free handle-only quotient and exact
`86+4+2` integral column ownership.

A117 does not emit:

- any numerical period entry;
- the two explicit Leray edge lifts;
- the normal-function beta vector;
- an integral `Z^92` branch;
- a gerbe zero or no-go;
- a selected marked K3 or full U6 closure.

No measured Standard-Model value and no fitted parameter enters this theorem.

External algorithm references:

- https://github.com/ericpipha/lefschetz-family
- https://arxiv.org/abs/2306.05263

Next artifact: `MTT_Selected_q79GenusTwoCertifiedThimblePeriodExecution_v1`.
