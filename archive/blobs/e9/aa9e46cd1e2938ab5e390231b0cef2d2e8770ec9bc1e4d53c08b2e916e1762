# q79 S3 Strain Intertwiner and Local Q Source v1

## Exact construction

Write the q79 trace-split carrier without its common line factor as

```text
F_q79 = (O direct-sum A0) direct-sum A = A direct-sum A.
```

In a local sheet chart let `a=(a1,a2,a3)` denote the first copy, already split
canonically into trace and trace-zero parts, and let `b=(b1,b2,b3)` denote the
reused full rank-three lane. Define

```text
J(a,b) =
[
  a1          b3/sqrt(2)  b2/sqrt(2)
  b3/sqrt(2)  a2          b1/sqrt(2)
  b2/sqrt(2)  b1/sqrt(2)  a3
].
```

The second copy is sent from vertices to opposite edges. The `1/sqrt(2)` is
forced by the Frobenius norm of a symmetric off-diagonal matrix unit.

The exact symbolic audit proves:

```text
J^* J = I6,
J rho_source(sigma) = Ad_{rho_plus(sigma)} J for every sigma in S3,
rank(P_trace, P_trace-zero, P_offdiag) = (1,2,3).
```

Since `rho_plus(sigma)=sign(sigma) P_sigma`, its sign cancels under conjugation.
The opposite-edge rule is equivariant under every sheet relabeling. Therefore
the formula descends on the unbranched q79 `S3` local system and does not choose
a global ordering of sheets.

## Actual local Q and metric map

On the orientation-fixed polar slice define

```text
S(f) = J f,
Q(f) = exp(S(f)),
G(f) = Q(f)^T Q(f) = exp(2 S(f)).
```

At the zero-strain background `f_*=0`,

```text
Q_*=I,
G_*=I,
DG(0)[delta f] = 2 J(delta f),
D[(1/2) log G](0)[delta f] = J(delta f).
```

This is the first explicit, monodromy-compatible local metric derivative in
the q79/world-in-world chain. It is a calculation from a displayed nonlinear
observable, not acceptance of a prefilled `B0` matrix.

## What this closes

- the real `1+2+3` fiber intertwiner on the unbranched `S3` local system;
- transition compatibility without ordered sheets;
- the canonical Frobenius metric and all three lane projectors;
- an orientation-fixed nonlinear `Q` source and its exact local derivative.

## What remains

The theorem does not yet turn this carrier into the physical spacetime metric.
It still requires extension through the branch locus, compatibility with the
selected HYM connection/metric and Hessian, and an identification with the
physical spatial frame bundle.

There is also a typing point hidden by earlier rank notation. The exact twisted
map is

```text
id_L tensor J:
L_shared tensor (O direct-sum A0 direct-sum A)
  -> L_shared tensor Sym(V).
```

An untwisted real metric requires a selected real structure, phase-neutral
pairing, or trivialization. The common complex line cannot simply disappear.
