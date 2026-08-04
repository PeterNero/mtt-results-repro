# MTT Selected q79 Normalized Poincare Gerbe and PGL3-Prym Reduction v1

Status: `MTT_U6_Q79_GERBE_RESIDUE_REDUCED_TO_8X8_PGL3_PRYM_SYSTEM_JACOBIAN_VALUES_OPEN`

## Why this is a new step

A104 proved that the integral Dixmier-Douady class vanishes on the q79
spectral surface and isolated a topologically trivial holomorphic residue in
a nine-dimensional ambient space. A105 uses the degree-three spectral
equation and its determinant-zero condition. The active residue is only
eight-dimensional, and those eight directions are canonically dual to the
eight previously unfixed `PGL(3)` alignment directions.

## Trace decomposition

For `p:C->K3`, the divisor sequence is

```text
0 -> O(-H,-3[0]) -> O -> O_C -> 0.
```

On the elliptic curve, `h0(O(-3[0]))=0` and `h1(O(-3[0]))=3`. Pushing the
sequence to K3 gives the evaluation kernel

```text
0 -> K -> O(-H)^3 -> O -> 0.
```

The three sections are the genus-two map `phi_H:K3->P2`, so the Euler
sequence identifies

```text
K = phi_H^* Omega^1_P2.
```

The unit and one-third of the trace split the finite degree-three algebra:

```text
p_*O_C = O_K3 direct_sum K.
```

Consequently

```text
H^2(C,O_C) = H^2(K3,O) direct_sum H^2(K3,K),
9 = 1 + 8.
```

## Normalize the Poincare gerbe

The obstruction gerbe lifting the Fu-Yau torsor can be shifted by a gerbe
pulled back from K3. The relative Jacobian has a zero section `z`, so

```text
alpha_0 = alpha - p_J^* z^*alpha
```

is the unique lift with `z^*alpha_0=0`; uniqueness follows from
`z^*p_J^*=identity`. This removes a genuine base-Brauer ambiguity before any
numerical or period calculation.

The normalized Poincare object is a biextension and is additive in the
elliptic coordinate. If the three spectral points are `y1,y2,y3`, then

```text
Nm(alpha_0|C)
  = alpha_0(y1)+alpha_0(y2)+alpha_0(y3)
  = alpha_0(y1+y2+y3).
```

The A103 cover is determinant-zero, so `y1+y2+y3=0`, and normalization gives
`alpha_0(0)=0`. Therefore

```text
Nm(alpha_0|C)=0,
Tr(beta_C)=0.
```

This does not prove `beta_C=0`. It proves that its one-dimensional trace
component is zero and places the remaining class in the eight-dimensional
Prym/trace-free component.

## The 8 by 8 theorem

Serre duality and the genus-two double-cover formula give

```text
H^2(K)^* = H^0(phi_H^*T_P2),
phi_H*O_K3 = O_P2 direct_sum O_P2(-3).
```

Since `h0(T_P2)=8` and `h0(T_P2(-3))=0`,

```text
H^2(K)^* = pgl3,
dim H^2(K) = dim PGL(3) = 8.
```

Thus the exact remaining problem is the square holomorphic system

```text
B is a section of T_Prym -> PGL(3),
B(iota)=beta_C_iota=0,
dB_iota is 8 by 8 after local Gauss-Manin/holomorphic trivialization.
```

This dimension match is not itself an existence theorem. It gives a decisive
finite calculation:

- a zero with nonzero determinant of `dB` selects an isolated local alignment
  and turns the former eight moduli into solved geometric coordinates;
- no zero rules out this smooth rank-one degree-three spectral route;
- a positive-dimensional zero locus leaves a smaller selector problem.

No observed Standard-Model value appears in this system, and no alignment
coordinate is yet counted as a fitted parameter.

## Required execution

The generated Jacobian template requires a marked lattice-polarized K3
sextic/period point, the elliptic period, a base alignment, the normalized
Poincare Cech cocycle, a local Gauss-Manin/holomorphic Prym trivialization,
eight Prym coordinates and their eight-by-eight alignment derivative. Current
repositories contain none of those numerical same-branch entries, so A105
does not fabricate the determinant or a zero.

After a transverse zero, the ordered chain remains: twisted rank-one spectral
sheaf, inverse Fourier-Mukai local freeness and determinant, balanced HYM,
then the full differential Bianchi identity.

Next artifact: `MTT_Selected_q79PGL3ToPrymGerbeJacobianExecution_v1`.

## Primary references

- [Brinzanescu, Halanay and Trautmann, Vector bundles on non-Kahler elliptic principal bundles](https://arxiv.org/abs/1008.3365)
- [Caldararu, Derived categories of twisted sheaves on elliptic threefolds](https://arxiv.org/abs/math/0012083)
- [Friedman, Morgan and Witten, Vector bundles over elliptic fibrations](https://arxiv.org/abs/alg-geom/9709029)
