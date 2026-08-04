# q79 Aggregate TLSM Anomaly and Odd-Bundle Monad No-Go

**Status:** `Q79_AGGREGATE_TLSM_LOCAL_ANOMALY_AND_RANK12_FERMI_MONAD_EXISTENCE_CLOSED_EXACT_CONDITIONAL_ODD_SU3_SU9_PICARD_LINE_MONAD_NOGO_PHYSICAL_NONABELIAN_EJ_SPLIT_AND_IR_SCFT_OPEN`

## Exact local anomaly

In the incidence Picard basis `(H,L)`,

```text
I = [[ 2,  2],
     [ 2, -2]],

C_T = sum_i Q_i Q_i^T - sum_alpha d_alpha d_alpha^T
    = [[-12, -6],
       [ -6,  0]].
```

Thus `integral ch2(TK3)=-24`. The aggregate bundle charge table below has

```text
D_V = sum_j m_j m_j^T - sum_r q_r q_r^T
    = [[14, 4],
       [ 4, 2]],
```

so `integral ch2(V12)=-20`. The quantum gauge anomaly is therefore

```text
A = C_T - C_V = C_T + D_V
  = [[ 2, -2],
     [-2,  2]]
  = 2 delta delta^T,       delta=(1,-1).
```

The general TLSM equation of Adams-Ernebjerg-Lapan is

```text
(1/2) sum_l N_l M_l^T = A,
N_l = 2 k_l^2 M_l.
```

It closes over the integers with

```text
M1=(1,-1),  N1=(4,-4),  k1^2=2,
M2=(0,0),   N2=(0,0).
```

The second, shared circle is therefore unshifted and unfluxed. Its radius is
not selected by this equation. The apparent factor-of-two ambiguity is also
fixed: `-delta^2=4`, the radius-weighted norm is `8`, and the `ch2` convention
contributes half of it. Hence the integrated equation is exactly

```text
c2(V12) + 8/2 = 20 + 4 = 24 = c2(TK3).
```

## Aggregate Fermi monad

An exact anomaly-equivalent charge presentation is

```text
B = O^7 + O(H+L)^4 + O(H)^4 + O(2H)^2,
C = O(2H+2L) + O(2H+L)^2 + O(3H)^2,
0 -> V12 -> B --J--> C -> 0.
```

The charge sums agree, the kernel rank is `17-5=12`, and its Chern data are
`c1=0,c2=20`. Each target line bundle is globally generated. Since `C` has
rank five on a surface, seven general global sections have rank five
everywhere: the rank-drop locus has expected codimension `7-5+1=3>2`.
Consequently a surjective `J` exists and its kernel is locally free. Taking
all `E` maps to zero gives `E.J=0` exactly.

This is an aggregate anomaly witness. It is not the physical stable splitting
`V3 + W9`, and no `E8 x E8` embedding is inferred from it.

## Exact obstruction for the odd sectors

For `D=aH+bL`,

```text
D^2/2 = a^2+2ab-b^2 = a+b (mod 2).
```

For any finite virtual complex of line bundles from this Picard lattice,
`c1=0` makes the signed sums of `a` and `b` vanish. Its `ch2`, hence its `c2`,
is therefore even. Separate bundles with `c2=9` and `c2=11` cannot be emitted
by any Picard-only line-bundle charge complex on this GLSM.

This is not a no-go for the A102 bundles themselves: stable locally free
`SU(3)` and `SU(9)` bundles with those Chern classes exist. It says their UV
presentation must contain genuinely non-Abelian, point/ideal-sheaf, or
spectral-sheaf data (or a separately selected larger Picard source).

## Frontier

Closed here:

1. the complete local `2x2` TLSM anomaly matrix;
2. integral torsion shift and axial rows;
3. the selected active radius `k1^2=2` at this conditional tier;
4. an aggregate locally free rank-12 Fermi monad;
5. an exact no-go explaining why that aggregate cannot be split into the two
   physical odd sectors using only the current line-bundle charge lattice.

Still required for UV-complete q79 quantum gravity:

1. physical non-Abelian `SU(3)` and `SU(9)` Fermi `E/J` data;
2. global R-current/left-current anomaly cancellation and a chiral GSO;
3. the exact IR `(0,2)` SCFT and seven analytic seed characters;
4. the differential non-pullback Bianchi identity;
5. all-genus factorization and a nonperturbative definition.

## Sources

- [Linear Models for Flux Vacua](https://arxiv.org/abs/hep-th/0611084)
- [Anomaly Cancellation and Smooth Non-Kahler Solutions](https://arxiv.org/abs/hep-th/0604137)
- [Hull-Strominger solutions with torus symmetry](https://arxiv.org/abs/1901.10322)
