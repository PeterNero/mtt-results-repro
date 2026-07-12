# Sourced Compact Nil Scalar Spectrum v1

This artifact imports one missing mathematical datum for the `Qa/SU3-Nil`
route: the scalar spectrum and multiplicities of the compact three-dimensional
Heisenberg nilmanifold.

The source is:

```text
Laplacian spectrum on a nilmanifold, truncations and effective theories
arXiv:1806.05156
https://arxiv.org/abs/1806.05156
```

The executable calculation is:

```text
scripts/compute_sourced_compact_nil_scalar_spectrum.py
```

and the audit is:

```text
proof_corpus/sourced_compact_nil_scalar_spectrum_audit.py
```

## Imported Scalar Spectrum

For the compact Heisenberg nilmanifold with metric radii `r1,r2,r3` and
structure constant `f`, the scalar spectrum has two pieces:

```text
mu_{m,n}^2 = (2*pi*m/r1)^2 + (2*pi*n/r2)^2
```

and

```text
M_{k,l,n}^2 = k^2*(2*pi/r3)^2 + (2n+1)*|k|*2*pi*|f|/r3.
```

The integer ranges include

```text
k in Z*, n in N, l=0,...,|k|-1.
```

Therefore, after summing the two signs of `k` and the `l` sector, the compact
scalar p != 0 multiplicity is:

```text
2|k|.
```

## MTT Map

The selected MTT convention used here is

```text
r1 = r2 = 1
r3 = c_nil
N_lattice = 1
f = c_nil
c_nil = 1.439 * R1_z64_normalized
```

with

```text
R1_z64_normalized(N=79) = 0.5397189300902845
c_nil = 0.7766555403999195
```

So the sourced scalar formula becomes

```text
M_{k,n}^2 = (2*pi*k/c_nil)^2 + (2n+1)*|k|*2*pi.
```

This matches the eigenvalue schema used in the earlier diagnostic oscillator
attempt, but it changes the compact multiplicity: the old sign-pair-unit branch
is not the compact scalar spectrum.  The compact scalar branch is the
`2|k|` branch.

## Boundary

This is useful progress, but it is not the selected Qa determinant.

It closes:

```text
compact scalar eigenvalue formula
compact scalar p != 0 multiplicity
```

It does not close:

```text
selected Qa/SU3 gauge-threshold operator
BRST/ghost quotient
analytic zeta determinant finite part
numeric electroweak closure
```

The next required artifact remains:

```text
Exact_Selected_Nil_Gauge_Threshold_Zeta_Determinant_v1
```
