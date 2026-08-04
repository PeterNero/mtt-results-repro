# q79 Euclidean Reflection, Free Physical OS Positivity, and EL Source Cutset Theorem v1

Date: 2026-07-26

## 1. Scope

This theorem advances the remaining Euclidean-to-Lorentzian package `EL`
after the separate `HK` and `CT` packages were closed.

It does not repeat the pointwise Wick companion already constructed in the
Mathematical Language Discovery repository. That packet already gives, for
an unoriented unit timelike line `[n]`,

```text
P_n(v) = -g_L(n,v)n,
W_n = I+(i-1)P_n,
R_n = W_n^2 = I-2P_n,
g_E = g_L+2 n_flat tensor n_flat.
```

The new work is:

1. connect `R_n` exactly to the selected q79 Cauchy-normal certificates;
2. distinguish the fiberwise involution from a global reflection isometry;
3. state the complete global reflection contract;
4. prove reflection positivity on a nontrivial free physical gauge algebra
   whenever that contract holds;
5. prove that current smooth q79 data do not automatically supply the
   global contract;
6. type the analytic Calderon-projector alternative;
7. prove that formal all-orders counterterms alone cannot decide
   fixed-coupling reflection positivity.

`B.QFT.02` and `EL` remain open overall.

## 2. Inputs

The local inputs are the current certificates for:

- the q79 globally hyperbolic Lorentzian coframe;
- Cauchy-normal companion-metric rigidity;
- temporal-companion homotopy and free shell independence;
- the free positive BRST physical quotient and free physical C-star net;
- the Lorentzian hyperbolic/equicausal BV algebra;
- the first-order Costello BV complex and graphwise counterterms.

The primary external comparison results are:

- [Jaffe and Ritter, reflection positivity on Riemannian manifolds](https://arxiv.org/abs/0705.0712);
- [Gerard and Wrochna, analytic Cauchy Wick rotation and Calderon projectors](https://arxiv.org/abs/1706.08942);
- [Wrochna, Wick rotation of time variables on analytic backgrounds](https://arxiv.org/abs/1808.03859);
- [Gerard and Wrochna, Hadamard states for linearized Yang-Mills](https://arxiv.org/abs/1403.7153).

These theorems are used only on their stated domains. In particular, the
analytic scalar continuation theorem is not silently promoted to the full
mixed q79 gauge-Higgs-Weyl BV system.

## 3. The tangent reflection

Let `(Y4,g_L)` have signature `(-+++)`, and let `n` be a future unit timelike
normal:

```text
g_L(n,n)=-1.
```

Define

```text
P_n(v)=-g_L(n,v)n,
R_n=I-2P_n,
g_E=g_L+2 n_flat tensor n_flat.
```

### Proposition 3.1

`P_n` is a rank-one projector, `R_n^2=I`, and `R_n` reverses `n` while
fixing `n_perp`.

### Proof

For `v=a n+x` with `x` orthogonal to `n`,

```text
P_n(v)=a n,
R_n(v)=-a n+x.
```

The projector and involution identities follow immediately. The temporal and
spatial eigenspaces have dimensions one and three. QED.

### Proposition 3.2

`R_n` preserves both `g_L` and `g_E`.

### Proof

In the orthogonal decomposition `v=a n+x`,

```text
g_L(v,v)=-a^2+g_L(x,x),
g_E(v,v)= a^2+g_L(x,x).
```

Changing `a` to `-a` preserves both forms. QED.

The executable certificate verifies these identities over the rationals in
both the adapted q79 frame and the prior boosted temporal-companion endpoint.
It also verifies `R_(-n)=R_n`. Thus the construction depends on the temporal
line, not its orientation.

This remains a fiberwise statement. It does not yet give a diffeomorphism of
spacetime.

## 4. Global reflection contract

For Osterwalder-Schrader reflection positivity, a pointwise involution is not
enough. A selected collar of a Cauchy surface `Sigma` must supply:

| Row | Required object |
|---|---|
| ELR1 | An involution `theta` with `theta^2=id`, fixed set `Sigma`, and `d theta=R_n` on `Sigma` |
| ELR2 | `theta^*g_E=g_E` |
| ELR3 | A lift of `theta` to the faithful q79 principal bundle |
| ELR4 | Reflection invariance of the selected gauge connection, up to one based gauge transformation |
| ELR5 | Reflection parity of the Higgs background and Yukawa bundle maps |
| ELR6 | A compatible spin/chiral lift on Weyl and conjugate-Weyl rows |
| ELR7 | Equivariance of the first-order BV differential, pairing, `QGF`, and heat covariance |
| ELR8 | Invariance of the positive physical BRST projector, a tested-shell transfer form `-partial_tau^2+A^2` with `A>0` self-adjoint, and the boundary/renormalization prescription |

Current q79 data select a future causal component but no unique temporal
function, lapse, shift, normal field, or companion metric before the
auxiliary quotient. None of ELR1-ELR8 is presently emitted as selected global
data.

## 5. Free physical reflection positivity

Assume ELR1-ELR8 on a reflection collar. Remove harmonic zero modes and
BRST-exact rows. ELR8 supplies the positive physical transfer operator
`-partial_tau^2+A^2`. On a positive finite spatial spectral shell, let `A`
have frequencies `omega_j>0`. Its Euclidean covariance is

```text
C_j(tau,sigma)
  = exp(-omega_j |tau-sigma|)/(2 omega_j).
```

Let `f` have support in the positive half-collar. Reflection sends `tau` to
`-tau`, so

```text
C_j(-tau,sigma)
  = exp(-omega_j(tau+sigma))/(2 omega_j).
```

### Theorem 5.1

On the linear free physical observable space,

```text
<Theta f,Cf>
  = sum_j (2 omega_j)^(-1)
      |int_0^infinity exp(-omega_j tau) f_j(tau) d tau|^2
  >= 0.
```

### Proof

Insert the reflected kernel and apply Fubini on each finite spectral mode:

```text
int_0^infinity int_0^infinity
  conjugate(f_j(tau))
  exp(-omega_j(tau+sigma))
  f_j(sigma)
  d tau d sigma

= |int_0^infinity exp(-omega_j tau)f_j(tau)d tau|^2.
```

Every coefficient `(2 omega_j)^(-1)` is positive. Summing preserves
nonnegativity. QED.

The observables are gauge-invariant curvature/transverse classes in the free
BRST cohomology. The theorem does not assign a positive metric to ghosts,
antifields, gauge-fixing auxiliaries, or the full indefinite BV presentation.

For the free Gaussian theory, Wick factorization extends the positive
two-point form to the polynomial algebra generated by these physical
observables. This is the standard Gaussian OS step and agrees with the
Riemannian reflection framework of Jaffe-Ritter.

### Exact witness

Take two physical frequencies

```text
omega=(1,2), Delta=log(2),
exp(-omega Delta)=(1/2,1/4),
```

and positive times `(Delta,2Delta,3Delta)`. The exact reflected Gram matrix is

```text
[
  [9/64,    17/256,   33/1024],
  [17/256,  33/1024,  65/4096],
  [33/1024, 65/4096, 129/16384]
].
```

It factorizes as

```text
V diag(1/2,1/4) V^T,
V_(a,j)=exp(-omega_j t_a),
```

has rank two, has nonnegative principal minors, and gives the exact positive
norm

```text
(1,-2,3) G (1,-2,3)^T = 1273/16384.
```

The witness time step is a proof coordinate, not a physical q79 scale.

## 6. Smooth global-promotion obstruction

The selected q79 coframe theorem is smooth. Smooth Cauchy data do not imply
reflection symmetry.

Consider the smooth Lorentzian collar

```text
g_L=-d tau^2+(1+tau)dx1^2+dx2^2+dx3^2,
|tau|<1/2.
```

Its Cauchy-normal companion is

```text
g_E=+d tau^2+(1+tau)dx1^2+dx2^2+dx3^2.
```

At `tau=0`, the metric, normal, and tangent reflection agree with the adapted
q79 witness. The natural candidate

```text
theta(tau,x)=(-tau,x)
```

has the correct fixed slice and derivative. Nevertheless, at `tau=1/4`,

```text
(g_E)_11=5/4,
(theta^*g_E)_11=3/4.
```

Hence `theta` is not an isometry.

There is also a coordinate-free obstruction. The slice extrinsic curvature is

```text
K=diag(1/2,0,0).
```

A slice-fixing reflection isometry fixes tangent vectors and reverses the
normal, so it sends `K` to `-K`. Invariance would require `K=0`. More
generally, the full collar coefficients must be even under `tau -> -tau`.

### Corollary 6.1

The current smooth q79 Cauchy-normal data do not automatically integrate
`R_n` to a global reflection isometry.

This is a nonpromotion theorem. It does not prove that the actual selected
physical branch cannot possess additional reflection symmetry.

## 7. Analytic Calderon route

Global reflection symmetry is not the only possible bridge. On analytic
spacetimes near an analytic Cauchy surface, Gerard-Wrochna and Wrochna
construct elliptic Wick-rotated operators, Calderon projectors, and analytic
Hadamard boundary values under additional inverse, boundary, and positivity
hypotheses.

For q79 this route requires:

| Row | Required object |
|---|---|
| ELA1 | Analytic Lorentzian metric and analytic Cauchy surface |
| ELA2 | Analytic selected gauge, Higgs, and Yukawa coefficients |
| ELA3 | One elliptic mixed-BV Wick operator with inverse and boundary domain |
| ELA4 | Calderon-projector descent and positivity on BRST cohomology |
| ELA5 | Equality with the selected Lorentzian Hadamard/equicausal two-point functions |
| ELA6 | Equality of Euclidean Costello and Lorentzian Epstein-Glaser counterterms in one BRST-compatible scheme |

Current q79 sources are smooth, not analytic. The local generalized-Laplace
and heat-kernel theorem is support for ELA3, but does not supply its global
domain or ELA4-ELA6. The existing Lorentzian Yang-Mills Hadamard-state theorem
closes the free Lorentzian state existence problem; it is not itself a Wick
comparison.

## 8. Formal interacting positivity no-go

OS positivity is a numerical inequality at a fixed coupling. A formal
all-orders jet does not determine that inequality.

Use the already certified flat function

```text
f(lambda)=(1/2)exp(1-1/lambda^2), lambda>0,
f(0)=0.
```

Every derivative at zero vanishes, but `f(1)=1/2`. Therefore

```text
q0(lambda)=1,
q1(lambda)=1-3f(lambda)
```

have identical formal Taylor series at zero, while

```text
q0(1)=1,
q1(1)=-1/2.
```

### Theorem 8.1

The formal Costello counterterm series and all-orders QME scheme cannot by
themselves establish an interacting fixed-coupling OS inequality.

This does not show that a completed q79 theory is nonpositive. It proves that
a summation, regulator-limit, or other fixed-coupling selection is necessary.

## 9. EL decision

The remaining `EL` package has alternative exits:

1. supply ELR1-ELR8 and a fixed-coupling reflection-positive completion;
2. supply ELA1-ELA6 and prove the analytic Euclidean-to-Lorentzian
   counterterm comparison;
3. bypass global Wick rotation with a smooth Lorentzian BV regulator and
   prove direct equality with the existing Lorentzian Epstein-Glaser/QME
   prescription.

Only one successful route is required. After it, renormalized equicausal
Cauchy transport must still be proved for the selected prescription.

## 10. Claim boundary

Closed here:

- exact q79-normal tangent reflection;
- conditional free physical finite-shell OS positivity;
- exact obstruction to automatic global reflection promotion;
- exact obstruction to formal-to-fixed-coupling OS promotion;
- typed reflection, analytic Calderon, and direct Lorentzian exits.

Still open:

- a selected global q79 reflection contract;
- analytic selected q79 background data;
- mixed-BV Calderon projectors and BRST positivity;
- Euclidean Costello versus Lorentzian EG counterterm equality;
- renormalized equicausal Cauchy transport for that equality;
- fixed-coupling interacting reflection positivity;
- numerical RG matching and nonperturbative completion.

No physical parameter, fit, observed value, or new selector is added.

## 11. Verification

```powershell
python -m unittest tests.test_qm_source.QmSourceTestCase.test_q79_reflection_closes_free_physical_OS_and_sharpens_EL -v
python scripts/verify.py
```
