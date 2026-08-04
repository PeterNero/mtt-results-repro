# MTT Selected q79 Genus-Two Critical-Value and Node Isolation v1

Status: `MTT_U6_Q79_90_CRITICAL_VALUES_AND_NODAL_POINTS_CERTIFIED_MONODROMY_PATHS_OPEN`

## Certified critical values

A112 feeds A111's exact degree-90 integer polynomial `N90` to MPSolve 3.2.3
with the isolation goal and exact integer input. The full output contains `90`
entries, each with status

```text
Status: Isolated, None, In
```

and a guaranteed inclusion radius. All `4005` disk pairs are disjoint by an
exact decimal-rational squared-distance check. Eight disks meet the real axis;
independent Sturm isolation gives eight simple rational real intervals. The
other 82 disks form 41 conjugate pairs. Thus every discriminant root now has a
machine-checkable individual carrier rather than only a square-free count.

The exact integer discriminant is square-free:

```text
gcd(N90,N90') = 1.
```

Thus no certified disk can hide a repeated critical value.

## Exact lift to the elliptic base

For the unique root `a_j` in disk `D_j`, define

```text
b_j=-P45(a_j)/Q43(a_j).
```

The A111 coprimality certificate proves `Q43(a_j)!=0`. The equation
`N90(a_j)=0` then gives `b_j^2=a_j^3-a_j`, while construction gives
`P45(a_j)+b_j Q43(a_j)=0`. Therefore every `a_j` has exactly one lift to a
critical point of the genus-two family on `E_i`.

## Exact nodal points

The subresultant sequence of `f_ab` and `d_t f_ab` has degrees

```text
6,5,4,3,2,1,0.
```

Reduce the degree-one member modulo `b^2-a^3+a`:

```text
S1_red=c1(a,b)t+c0(a,b).
```

After substituting `b=-P45/Q43`, the numerator of `c1` is coprime to `N90`.
Hence `c1` is nonzero at all 90 critical values and

```text
t_j=-c0(a_j,b_j)/c1(a_j,b_j),  u_j=0
```

is the unique double root and the exact node of the singular fiber. A112 thus
closes all 90 critical values and all 90 nodal points algebraically.

## What remains

No monodromy matrix or beta period is inferred from root isolation. The next
execution must choose a regular genus-two fiber and certified path tree on the
punctured elliptic base, track the colliding branch pair along every path, and
emit the 90 integral Picard-Lefschetz transvections in `Sp(4,Z)`. Only then can
the rank-92 surface homology and A106 beta periods be assembled.

The trial carrier remains unselected, zero strict source moduli are removed,
and U6 is not declared closed.

## Solver semantics

MPSolve's official polynomial-file and output documentation defines exact
integer input, the isolate goal, full output error bounds, and `Isolated`
status. The raw input and output are retained and hashed in the packet.

Next artifact: `MTT_Selected_q79GenusTwoPicardLefschetzMonodromyExecution_v1`.
