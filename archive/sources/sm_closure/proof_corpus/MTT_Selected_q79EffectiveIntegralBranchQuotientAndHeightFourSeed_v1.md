# MTT Selected q79 Effective Integral Branch Quotient and Height-Four Seed v1

## Scope

This is successor **A132** to A131. It does not reconstruct the selected
period matrix; A131 is consumed as closed authority. A132 removes the exact
Leray-null redundancy from the integral branch and emits one deterministic
same-carrier continuation seed.

## Exact effective branch quotient

A130 gives the primitive integral decomposition

```text
H2(C_A,Z) = <primary_1,...,primary_90,Leray_F,Leray_Gamma0>.
```

A131 proves all `8x2=16` periods of the final Leray pair vanish exactly for
the eight trace-free residue forms. Hence

```text
Pi(m,u,v)=Pi_primary*m
```

for every `(m,u,v) in Z^90 x Z^2`. The branch equation therefore factors
exactly through

```text
Z^92/<Leray_F,Leray_Gamma0> = Z^90,
F(A,m)=beta(A)-Pi_primary(A)m.
```

The canonical representative is `(m,0,0)`. This proves that the two Leray
coefficients cannot be selected by these period equations and are not branch
parameters. It does not assert that the displayed pair is the entire exact
kernel of `Pi`.

## Fixed discrete search

The fixed Kannan grid uses scale `1000000`, coefficient weights
`900,910,...,1600`, and marker multipliers `[1, 2, 3, 5, 8]`. It emits
`575` distinct target-coefficient-one vectors. The smallest
coefficient height entering the current beta-center component balls in this
fixed search is `4`. The selected continuation seed has:

```text
height                 = 4
support                = 71
l1 norm                = 120
max center residual    = 0.005506387455406569
beta component radius  = 0.0070601942733186695
primitive support      = 71
primitive handle row   = [-1, 0, 1, 1, 0, 0, 0, 0]
```

The height is a bound on integer cycle multiplicities, not a count of fitted
parameters. The height-three result is outside the current beta enclosure in
this fixed search. This is not a global height-minimality theorem because the
Kannan grid is not exhaustive over `Z^90`.

## What the numerical overlap means

The beta enclosure is rigorous, but A131's nonzero period entries currently
have independent two-run convergence envelopes rather than interval bounds.
Therefore the height-four center residual is a lawful continuation seed and a
nonseparation diagnostic, not a proof of exact lattice membership. A small
residual is not promoted to equality.

## Next theorem

Hold the integer vector fixed and execute the same-source covariant system

```text
F(A,m)=beta(A)-Pi_primary(A)m,
J_rs=nabla_s beta_r-sum_I m_I nabla_s Pi_rI.
```

An interval Newton/Krawczyk zero with `det J != 0` would select an isolated
alignment on this branch. A separation certificate would reject it. Either
outcome advances the exact branch decision.

No observed Standard Model value is used.
