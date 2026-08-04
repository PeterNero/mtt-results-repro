# q79 Temporal-Companion Homotopy and Normalized Free-Shell Regulator-Independence Theorem v1

## Status

This theorem closes the q79 Cauchy-normal/Euclideanization coordinate for
normalized free finite-shell BV observables on one rounded chart, relative to
a fixed boundary collar.

It does not select a preferred Wick metric. It does not identify the shared
circle with time. It does not close an absolute determinant phase, a change of
boundary polarization, the interacting cutoff-removal limit or a fixed
coupling C*-completion.

## 1. Inputs

The theorem composes four already certified inputs.

1. The q79 Lorentzian coframe certificate says that `A_causal` selects one
   time orientation, the retarded boundary class and the `q79/F`
   representative. Its selected coframe remains defined up to diffeomorphism
   and local Lorentz gauge.
2. The Mathematical Language temporal-polarization packet proves existence of
   Euclidean companions after choosing a temporal line, records the convex
   homotopy of future timelike lines and explicitly denies that time
   orientation selects a unique temporal function.
3. The q79 sign-flip rigidity theorem proves that, once a future unit timelike
   normal \(n\) is fixed,
   \[
   g_E(n)=g_L+2n^\flat\otimes n^\flat
   \tag{1.1}
   \]
   is the unique positive companion preserving the spatial metric.
4. The q79 finite-shell theorem constructs the Hodge Lagrangian cycle and
   free QME-preserving BV pushforward. The renormalized-QME theorem separately
   closes formal gauge-fixing independence on the declared on-shell charts.

The new work is to connect these inputs through an actual collar-relative
temporal path and to remove positive cutoff crossings rather than assuming a
global spectral gap.

## 2. Admissible local temporal companions

Let \(M\) be one rounded compact q79 chart with a fixed boundary collar
\(U_{\partial}\). Let \(\tau_0,\tau_1\) be smooth functions such that:

1. \(d\tau_0\) and \(d\tau_1\) lie in the same connected timelike cotangent
   cone at every point;
2. their first jets agree on \(U_{\partial}\);
3. the Lorentzian metric, physical bundles and BV differential are fixed.

Define

\[
\tau_s=(1-s)\tau_0+s\tau_1,\qquad 0\leq s\leq 1.
\tag{2.1}
\]

The timelike cone is convex, so

\[
d\tau_s=(1-s)d\tau_0+s\,d\tau_1
\tag{2.2}
\]

remains timelike and in the same component. Normalize its Lorentzian gradient
to obtain \(n_s\), with the future sign fixed by `A_causal`, and set

\[
g_E(s)=g_L+2n_s^\flat\otimes n_s^\flat.
\tag{2.3}
\]

Equation (1.1) proves that every \(g_E(s)\) is positive. Smoothness follows
because the normalization denominator never vanishes.

Since the first jets of the endpoints agree on the collar, (2.1) is constant
there. Consequently \(n_s\), \(g_E(s)\), the induced boundary operator and the
chosen relative/generalized-APS domain are fixed on the collar. No moving
boundary polarization or BV-BFV flux is introduced.

This is a local rounded-chart theorem. For a global spacetime, Bernal-Sanchez
provides smooth Cauchy temporal functions and an orthogonal splitting.
Preservation of the global Cauchy property under a proposed interpolation
requires the usual global steepness/properness hypotheses and is not inferred
from the local argument.

## 3. What `A_causal` selects

The selected q79 causal packet contains:

\[
\text{time orientation}
 +\text{retarded boundary class}
 +\text{q79/F representative}.
\tag{3.1}
\]

It contains no preferred \(\tau\), lapse, shift, unit normal or positive
companion metric. Therefore a unique temporal function cannot be derived from
`A_causal` as currently stated.

This is not a new physical deficit. Equations (2.1)-(2.3) place all admissible
collar-relative temporal companions in one auxiliary path component. The
question is regulator independence along that component, not selection of an
additional constant.

## 4. Exact rational path

In the Lorentz frame

\[
\eta=\operatorname{diag}(-1,1,1,1),
\tag{4.1}
\]

consider

\[
n(r)=
\left(
\frac{1+r^2}{1-r^2},
\frac{-2r}{1-r^2},
0,0
\right),
\qquad 0\leq r\leq \frac12.
\tag{4.2}
\]

The polynomial identity

\[
-(1+r^2)^2+4r^2=-(1-r^2)^2
\tag{4.3}
\]

gives \(\eta(n(r),n(r))=-1\) exactly. The zeroth component is positive, so the
whole path is future directed.

At the three certified rational samples,

\[
\begin{aligned}
n(0)&=(1,0,0,0),\\
n(1/4)&=(17/15,-8/15,0,0),\\
n(1/2)&=(5/3,-4/3,0,0).
\end{aligned}
\tag{4.4}
\]

The first endpoint is the adapted q79 normal and the last is the exact boost
endpoint from the preceding rigidity theorem. Their companions are

\[
g_E(0)=I_4
\tag{4.5}
\]

and

\[
g_E(1/2)=
\begin{pmatrix}
41/9&40/9&0&0\\
40/9&41/9&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
\tag{4.6}
\]

Every sampled companion has positive Sylvester minors and determinant one.
The path is not pointwise regulator invariant: the scalar principal symbol
from the preceding theorem changes from \(1\) to \(41/9\). The result below is
therefore a BV-pushforward equivalence, not equality or isospectrality of raw
regulators.

## 5. Positive cutoff crossings are contractible

Let \((\mathcal E,Q,\omega)\) be the free linear BV complex on the fixed chart,
and let

\[
\Delta_s=Q Q_s^\dagger+Q_s^\dagger Q
\tag{5.1}
\]

be the positive Hodge operator defined by \(g_E(s)\) and the fixed
collar-relative domain. The underlying \(Q\) and physical Lorentzian action
are unchanged; the adjoint, Hodge decomposition and spectral cutoff vary.

For a positive eigenspace

\[
\Delta_s v=\lambda v,\qquad \lambda>0,
\tag{5.2}
\]

define

\[
h_\lambda=\lambda^{-1}Q_s^\dagger.
\tag{5.3}
\]

Because \(Q\) commutes with its Hodge Laplacian,

\[
Qh_\lambda+h_\lambda Q
=\lambda^{-1}(Q Q_s^\dagger+Q_s^\dagger Q)
=I
\quad\text{on }E_\lambda.
\tag{5.4}
\]

Thus every positive eigenspace is an acyclic BV shell. If a positive
eigenvalue crosses a finite cutoff, the raw spectral projector changes rank,
but the entering or leaving shell has an explicit contraction. Inclusion or
removal is a strong deformation retract and cannot change BV/BRST
cohomology.

This is different from a zero-mode crossing. At \(\lambda=0\), (5.3) does not
exist and cohomology, determinant and boundary data require separate control.

## 6. Executable crossing witness

The certificate uses the four-dimensional contractible block

\[
Q_a=
\begin{pmatrix}
0&0&0&0\\
a&0&0&0\\
0&0&0&-a\\
0&0&0&0
\end{pmatrix},
\qquad
\Delta_a=a^2I_4.
\tag{6.1}
\]

It adjoins two physical cohomology rows and checks

\[
Qh+hQ=I-ip,\qquad pi=I_2.
\tag{6.2}
\]

For

\[
a=1,\quad \frac32,\quad 2,
\qquad
\Lambda^2=\frac94,
\tag{6.3}
\]

the four shell rows cross the cutoff at the middle sample. The raw low-mode
projector rank changes from six to two. At all three samples:

1. \(Q_a^2=0\);
2. \(\Delta_a=a^2I_4>0\);
3. \(h_a=a^{-2}Q_a^\dagger\) satisfies (5.4);
4. the total cohomology dimension remains two;
5. the shell Gaussian determinant is \(-a^2\neq0\).

The crossing is therefore a positive contractible-shell event, not spectral
flow through zero.

## 7. Normalized free-shell independence

The free finite-shell QME certificate supplies a BV-closed half-density and a
Hodge Lagrangian integration cycle. Schwarz gauge-fixing independence and BV
pushforward quasi-isomorphism then imply:

\[
\mathcal E_{\mathrm{IR}}\oplus E_\lambda
\ \simeq_{\mathrm{BV}}\
\mathcal E_{\mathrm{IR}}
\tag{7.1}
\]

for each positive crossing shell. Subdivide a temporal path into gapped
segments and positive crossing events. Kato transport applies on the gapped
segments, while (5.3)-(5.4) remove every crossing shell. Composition gives
the same normalized free physical cohomology observables at the two
endpoints.

The unnormalized pushforward may be multiplied by a determinant-line scalar.
For a normalized expectation value, that common scalar cancels between
numerator and denominator. The theorem therefore does not choose or erase an
absolute determinant phase.

## 8. Theorem

Under the hypotheses in Section 2, any two collar-relative temporal
companions in the selected q79 future component yield canonically
quasi-isomorphic free finite-shell BV complexes. Positive cutoff crossings
are contractible by (5.3), and normalized free physical cohomology observables
agree after BV pushforward.

Accordingly,

```text
B.QFT.02_Cauchy_normal_Euclideanization_source
  = closed_as_auxiliary_quotient_for_normalized_free_finite_shell_observables.
```

No preferred temporal function and no new physical parameter are required at
this tier.

## 9. Boundaries

Still open:

1. an absolute unnormalized determinant-line phase or partition function;
2. temporal deformations that alter the boundary collar or BFV polarization;
3. noncontractible global paths with independent determinant holonomy;
4. uniform interacting estimates across cutoff removal;
5. the interacting fixed-coupling gauge-BRST C*-limit;
6. nonperturbative completion.

In an interacting pushforward, an ultraviolet shell can generate nonconstant
local effective vertices rather than only a scalar. The free contraction
therefore cannot be promoted to the interacting limit without the required
uniform renormalization and convergence control.

## 10. Parameter ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed inputs:                0
```

The temporal function is auxiliary proof data quotiented at the normalized
free finite-shell tier.

## 11. Reproduction

Run:

```powershell
python scripts/verify.py
python -m unittest discover -s tests -v
```

The generated certificate is:

```text
certificates/q79_temporal_companion_free_shell_independence.certificate.json
```

## 12. References

- A. N. Bernal and M. Sanchez, *Smoothness of time functions and the metric
  splitting of globally hyperbolic spacetimes*, arXiv:gr-qc/0401112.
- A. Schwarz, *Geometry of Batalin-Vilkovisky quantization*,
  arXiv:hep-th/9205088.
- A. S. Cattaneo, P. Mnev and N. Reshetikhin, quantum BV-BFV pushforward,
  arXiv:1507.01221.
- A. S. Cattaneo and P. Mnev, BV pushforward quasi-isomorphism,
  arXiv:2605.30558.
