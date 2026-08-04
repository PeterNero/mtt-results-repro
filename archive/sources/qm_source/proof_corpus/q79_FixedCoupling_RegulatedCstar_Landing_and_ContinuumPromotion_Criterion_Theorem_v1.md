# q79 Fixed-Coupling Regulated Cstar Landing and Continuum-Promotion Criterion Theorem v1

## Status

**The fixed-nonzero-coupling compact-gauge Cstar landing is closed at every
finite auxiliary external regulator. The Cstar reduced-product and
Banach-valued Borel promotion theorems are also closed. The selected, unique
q79 continuum limit is not closed.**

This theorem starts strictly after the direct Lorentzian
Stueckelberg-Petermann/QME/Cauchy bridge. It does not reopen that formal
result. Its purpose is to cross the first genuinely nonperturbative boundary:
construct an actual normed observable algebra at nonzero coupling, and state
exactly what is still required to remove the regulator.

The result has three logically separate parts:

1. an unconditional finite-regulator Cstar construction;
2. a Cstar reduced-product limit theorem;
3. an alternative Banach-valued Borel uniqueness theorem.

Only the first part is currently instantiated for q79 data. The latter two
are proved implication theorems whose analytic hypotheses are not yet
supplied by MTT.

## 1. Inherited Inputs

The following are used as closed inputs:

- the selected q79 compact gauge group
  \[
  G_{\rm SM}=(SU(3)\times SU(2)\times U(1))/\mathbb Z_6;
  \]
- the q79 gauge, Higgs and three-family chiral carrier;
- the classical BV master action at its declared coefficient tier;
- the Green-hyperbolic equicausal Lorentzian BV complex;
- all-orders local Epstein-Glaser time ordering;
- the zero local q79 gauge-anomaly class and formal QME restoration;
- the local normalized Stueckelberg-Petermann comparison;
- the exact free physical Cstar reference net at interaction coordinate
  zero.

The theorem does not assume that the upper q79 action, the physical
interaction vector or an external regulator family has already been selected.

## 2. Finite-Regulator Cstar Landing

Let \(n\) denote one finite external regulator. It may include:

- a finite spacetime cell complex or finite Cauchy graph;
- a finite volume;
- a finite gauge-covariant spectral cutoff;
- a finite Higgs oscillator cutoff;
- the finite q79 internal carrier.

Let \(\mathcal H_n(O)\) be the finite-dimensional regulated Hilbert space over
a finite region \(O\). Assume that the compact local gauge group \(G_n\) acts
continuously by a unitary representation \(U_n\), and that the regulator
projection commutes with this action and retains at least one gauge-singlet
vacuum vector.

Define

\[
\mathcal A_n(O)=B(\mathcal H_n(O)).
\]

This is a finite-dimensional unital Cstar algebra.

### Theorem 2.1: compact-gauge reduction

The Haar average

\[
E_n(A)=\int_{G_n}U_n(g)A U_n(g)^*\,dg
\]

is a unital completely positive faithful conditional expectation onto

\[
\mathcal A_n(O)^{G_n}
 =\{A\in\mathcal A_n(O):[A,U_n(g)]=0\ \forall g\in G_n\}.
\]

Hence \(\mathcal A_n(O)^{G_n}\) is a Cstar subalgebra.

Let

\[
\Pi_n=\int_{G_n}U_n(g)\,dg
\]

be the orthogonal projector onto the Gauss-neutral Hilbert space
\(\mathcal H_n(O)^{G_n}\). The neutral physical corner

\[
\mathcal A_n^{\rm phys}(O)
 =\Pi_n\mathcal A_n(O)^{G_n}\Pi_n
 \cong B(\mathcal H_n(O)^{G_n})
\]

is a Cstar algebra.

#### Proof

Every conjugation by \(U_n(g)\) is a Cstar automorphism. A normalized Haar
average of automorphisms is unital and completely positive. Haar invariance
gives \(E_n^2=E_n\), and its range is exactly the fixed-point algebra.
Faithfulness follows because \(E_n(A^*A)=0\) implies
\(\|A U_n(g)^*\xi\|=0\) for every \(g,\xi\). The invariant-vector average is
an orthogonal projector. Compression to its range gives the full matrix
algebra on the invariant Hilbert space. QED.

This neutral corner is the finite closed-region Gauss sector. It must not be
identified with full continuum BRST cohomology unless the constraint
reduction and regulator comparison have also been proved.

### Theorem 2.2: fixed nonzero coupling

Let

\[
H_n(\lambda_*)
 =P_n\left(H_{0,n}+\sum_j\lambda_{*,j}V_{j,n}\right)P_n,
\qquad \lambda_*\ne0,
\]

where the finite-rank projected operators are self-adjoint and gauge
invariant and the retained finite-rank range lies in their common operator
domain. Then

\[
\alpha_{n,t}(A)
 =e^{itH_n(\lambda_*)}A e^{-itH_n(\lambda_*)}
\]

is a strongly continuous Cstar automorphism group. It preserves both the
fixed-point algebra and the Gauss-neutral corner.

Every finite regulator also has:

- normalized positive states;
- gauge-invariant states obtained by composing with \(E_n\);
- a ground state because \(H_n(\lambda_*)\) has a lowest eigenvalue;
- faithful thermal states at every finite positive inverse temperature.

This is an actual fixed-coupling construction. No formal power series is
used in its definition.

### Theorem 2.3: finite-region net

For tensor-factor regulators, region inclusion is

\[
\iota_{O_1O_2}(A)=A\otimes 1,
\qquad O_1\subset O_2.
\]

The maps are injective unital star homomorphisms. Observables in disjoint
tensor factors commute. Gauge-equivariance of the embeddings implies that
isotony and this finite-regulator locality descend to the fixed-point
algebras.

Boundary-link conventions and charged edge sectors must be retained when
regions are not closed. The neutral compression theorem is asserted only on
the declared closed finite regulator.

## 3. Exact Executable Witness

The certificate contains a rational \(M_4\) witness with

\[
U_G=\operatorname{diag}(1,1,-1,-1),
\qquad
\Pi_G=\operatorname{diag}(1,1,0,0).
\]

The fixed-point algebra has dimension eight,
\[
M_4^{\mathbb Z_2}\cong M_2\oplus M_2,
\]
and the neutral corner is \(M_2\).

At the nonzero witness coordinate \(\lambda=1/3\),

\[
H(\lambda)=
\begin{pmatrix}
0&1/3&0&0\\
1/3&1&0&0\\
0&0&2&2/3\\
0&0&2/3&3
\end{pmatrix}
\]

is self-adjoint and gauge invariant. A separate exact rational
block-orthogonal step witnesses the star-automorphism and gauge-reduction
laws without approximating the generally transcendental matrix
\(\exp(itH)\). Existence of the actual \(H\)-generated unitary follows from
finite-dimensional functional calculus. The maximally mixed state is
faithful, normalized, gauge invariant and invariant under both evolutions.

The executable witness verifies:

- Haar idempotence on all 16 matrix units;
- the exact eight-dimensional fixed algebra;
- nonzero-coupling self-adjoint dynamics;
- star multiplicativity on all \(16^2\) matrix-unit pairs;
- gauge and Gauss-sector preservation;
- positive normalized finite-regulator state data;
- unital isotony and commutation of two tensor-local factors.

The number \(1/3\) is only an exact witness coordinate. It is not a physical
q79 coupling and is not counted as a parameter.

## 4. Cstar Reduced-Product Promotion

Let \(\{\mathcal A_n\}\) be Cstar algebras. Their bounded product is

\[
\prod\nolimits^\infty_n\mathcal A_n
=\{(A_n):\sup_n\|A_n\|<\infty\}.
\]

For a free ultrafilter \(\mathcal U\), define the closed two-sided ideal

\[
\mathcal I_{\mathcal U}
=\{(A_n):\lim_{\mathcal U}\|A_n\|=0\}.
\]

The quotient

\[
\mathcal A_{\mathcal U}
=\left(\prod\nolimits^\infty_n\mathcal A_n\right)/
  \mathcal I_{\mathcal U}
\]

is a Cstar algebra.

### Theorem 4.1: descent of a local net

Choose regulator regions \(O_n\) approximating each continuum region \(O\).
Let \(\mathcal A_{\mathcal U}(O)\) be generated by classes of uniformly
bounded sequences \(A_n\in\mathcal A_n(O_n)\).

Then:

1. regulator isotony descends to isotony;
2. if
   \[
   \|[A_n,B_n]\|\longrightarrow_{\mathcal U}0
   \]
   for every pair approximating spacelike-separated regions, the limit
   classes commute exactly;
3. gauge-fixed sequences descend to gauge-fixed limit classes;
4. regulator automorphisms descend if they preserve
   \(\mathcal I_{\mathcal U}\) and are uniformly norm-equicontinuous on the
   declared local sequence algebra;
5. regulator states \(\omega_n\) define a positive normalized state
   \[
   \omega_{\mathcal U}([A_n])
   =\lim_{\mathcal U}\omega_n(A_n).
   \]

#### Proof

The bounded product is a Cstar algebra in the supremum norm and
\(\mathcal I_{\mathcal U}\) is a closed star ideal, so the quotient is
Cstar. Isotony is componentwise. The commutator of two classes is the class
of the commutator sequence and vanishes exactly when its norm tends to zero
along \(\mathcal U\). Ideal-preserving automorphisms and positive normalized
functionals descend to the quotient. QED.

### Corollary 4.2: what a Lieb-Robinson estimate would close

Suppose a uniform estimate has the form

\[
\|[\alpha_{n,t}(A_n),B_n]\|
\le C\|A_n\|\|B_n\|
 \exp[-\mu(d_n-v|t|)]
\]

with \(C,\mu,v\) independent of the regulator and
\(d_n\to\infty\) for approximants of fixed spacelike-separated continuum
regions. Then the commutator norm tends to zero and exact continuum
microcausality follows in the reduced product.

Finite-range interactions alone do not provide this conclusion: the
constants must be uniform as gauge, Higgs, volume and lattice cutoffs are
removed.

### Theorem 4.3: existence is not uniqueness

An ultralimit exists for every bounded scalar sequence, but it can depend on
the ultrafilter. The exact witness

\[
0,1,0,1,\ldots
\]

has distinct even and odd cluster values. Therefore compactness, boundedness
or the existence of some scaling state does not select a unique physical
theory.

Ordinary convergence of every declared norm, correlation, dynamical and
state coordinate is sufficient for ultrafilter independence. An independently
selected scaling state could also define one branch, but that would be new
selection data and must be named as such.

## 5. Borel Promotion and the Flat Ambiguity

The prior nonpromotion theorem used a nonzero smooth function flat at
\(\lambda=0\) to prove that a formal jet does not determine a unique smooth
fixed-coupling theory.

That no-go is exact on the class of smooth coupling families. It does not
apply unchanged after a quasianalytic class has been proved.

Let \(\mathfrak B\) be a Banach star algebra and let

\[
\widehat F(\lambda)=\sum_{k\ge0}a_k\lambda^k
\]

be the certified formal jet. Assume that an analytic
\(F:\mathcal C_R\to\mathfrak B\) satisfies the uniform factorial remainder
bound

\[
\left\|F(\lambda)-\sum_{k=0}^{N-1}a_k\lambda^k\right\|
\le K\sigma^N N!|\lambda|^N
\]

on one Nevanlinna-Sokal domain \(\mathcal C_R\). Assume also that

\[
\mathcal BF(t)=\sum_{k\ge0}\frac{a_k}{k!}t^k
\]

continues along the positive ray with one common exponential growth bound.

### Theorem 5.1: Banach-valued Borel uniqueness

The Bochner integral

\[
F(\lambda)=\frac1\lambda
\int_0^\infty e^{-t/\lambda}\mathcal BF(t)\,dt
\]

is the unique member of the declared class with the given jet.

In particular, a nonzero function with zero jet cannot belong to that same
class. Thus the exact flat-deformation ambiguity is removed if the required
common summability class is actually proved. Other rigorously quasianalytic
completion classes could provide a different uniqueness route.

This is the Banach-valued form of the Nevanlinna-Sokal uniqueness argument;
continuous linear functionals reduce uniqueness to the scalar theorem.

### Theorem 5.2: algebraic identities

Suppose the Borel transforms obey uniform convolution estimates making the
chosen Borel class a Banach star algebra. Then absolutely convergent
Borel-Laplace summation preserves:

- addition and continuous linear maps;
- multiplication and involution;
- star-homomorphism and covariance identities;
- locality identities;
- polynomial Ward, master-equation and cocycle identities.

Coefficientwise formal QME closure supplies the jet of these identities, but
not the required norm estimates.

### Positivity boundary

Factorial bounds and scalar Borel summability do not imply positivity of a
state or the Cstar norm inequality. One still needs positive normalized
regulator states whose Borel transforms converge in a common weighted norm,
or another direct positivity theorem.

If

\[
\int_0^\infty e^{-t/\lambda}
\|\mathcal BF_n(t)-\mathcal BF(t)\|\,dt\to0,
\]

then the Borel-Laplace sums converge at that fixed coupling. This is the
correct weighted-Borel cutoff-removal condition. Uniform Gevrey bounds alone
are insufficient.

## 6. Current Acceptance Table

### Finite regulated landing: 5/5

| Row | Current state |
|---|---|
| finite local field Cstar algebras | accepted |
| compact-gauge fixed point and neutral Gauss corner | accepted |
| declared fixed-nonzero-coupling dynamics | accepted |
| positive gauge-invariant regulator state | accepted |
| finite-region isotony and tensor locality | accepted |

### Cstar continuum promotion: 0/9

| Row | Missing source |
|---|---|
| geometry-selected q79 external regulator family | upper action/regulator selection |
| full nonabelian chiral measure at fixed cutoff | nonperturbative full-SM theorem |
| cofinal embeddings or asymptotic morphisms | q79 regulator comparison functor |
| uniform asymptotic locality | regulator-independent Lieb-Robinson estimate |
| uniform phase-space/energy compactness | nuclearity or equivalent bound |
| vanishing norm-level Gauss/BRST/Ward defect | nonperturbative Ward estimate |
| formal EG tangent identification | regulator derivatives matched to the EG/SP jet |
| limit uniqueness | ordinary convergence or selected scaling state |
| selected positive global state | q79 state and spectrum condition |

### Borel promotion: 1/6

| Row | Current state |
|---|---|
| all-orders local formal QME jet | accepted |
| uniform factorial remainder bounds | open |
| common positive-ray continuation | open |
| Banach/Cstar convolution control | open |
| positivity after summation | open |
| weighted-Borel regulator convergence | open |

## 7. Relation to Existing Work

Buchholz and Fredenhagen construct fixed-coupling local Cstar algebras for
scalar Lagrangians, and the later extension includes Fermi fields:
[scalar construction](https://arxiv.org/abs/1902.06062),
[Fermi extension](https://arxiv.org/abs/2103.05740).
These are decisive benchmarks, but they do not by themselves prove the
nonabelian gauge-BRST physical descent for the full q79 carrier.

Grundling and Rudolph construct infinite-lattice QCD dynamics, enforce Gauss
law and obtain gauge-invariant ground states:
[lattice QCD dynamics](https://arxiv.org/abs/1512.06319).
This proves that the Cstar/Gauss strategy is mathematically viable, but not
that its continuum limit equals the q79 chiral Standard Model.

Buchholz and Verch show how scaling-limit nets arise operator algebraically
and explicitly allow nonunique scaling limits:
[scaling algebras](https://arxiv.org/abs/hep-th/9501063).
That is exactly why limit existence and branch selection are separate rows.

Luscher proves anomaly-free chiral lattice gauge symmetry at fixed lattice
spacing to all perturbative orders for compact gauge groups:
[chiral lattice regularization](https://arxiv.org/abs/hep-lat/0006014).
It does not provide a nonperturbative full Standard-Model continuum limit.

Uniform causal estimates can be organized through Lieb-Robinson bounds:
[Nachtergaele-Sims](https://arxiv.org/abs/1004.2086).
The relevant q79 constants must remain bounded as all regulators are removed.

The Borel uniqueness input is Sokal's improvement of Watson's theorem:
[Sokal](https://doi.org/10.1063/1.524408).

## 8. Exact Claim Boundary

### Closed

- an actual fixed-nonzero-coupling compact-gauge Cstar algebra at every
  finite auxiliary regulator;
- finite-regulator Gauss-neutral physical reduction;
- finite-regulator automorphic dynamics and positive states;
- a Cstar reduced-product promotion theorem under explicit asymptotic
  hypotheses;
- a Banach-valued Borel uniqueness theorem;
- exclusion of the prior flat ambiguity inside one proved common
  Nevanlinna-Sokal class.

### Open

- selection of the external q79 regulator family;
- selection of the upper q79 action and physical interaction vector;
- a nonperturbative full nonabelian chiral measure;
- uniform locality, energy, Ward and state estimates;
- matching the fixed-coupling regulator tangent to the certified
  Lorentzian EG/SP jet;
- a unique or independently selected continuum limit;
- a selected positive global interacting state;
- observable comparison and numerical RG/matching.

## 9. Frontier Delta

Before this theorem, MTT had:

- a physical Cstar net only at zero interaction coordinate;
- an all-orders interacting formal jet;
- an exact proof that this jet did not determine a unique smooth
  fixed-coupling completion.

After this theorem, MTT additionally has:

- an actual normed, positive, fixed-nonzero-coupling physical algebra at each
  finite auxiliary regulator;
- two exact routes that would promote it to a unique continuum theory;
- a minimal, nonduplicative list of the analytic and source rows still
  missing.

This is real progress across the normed-algebra boundary. It is not yet a
construction of the four-dimensional interacting Standard Model.
