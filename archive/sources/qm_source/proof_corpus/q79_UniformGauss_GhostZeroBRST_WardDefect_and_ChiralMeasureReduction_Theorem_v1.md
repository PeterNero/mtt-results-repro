# q79 Uniform Gauss and Ghost-Zero BRST Defect and Chiral-Measure Reduction Theorem v1

## Status

**Closed for the compact-gauge and BRST differential on ghost-number-zero
physical observables, at every admitted finite auxiliary regulator and in
every Cstar reduced product.**

The full quantum Ward row is not closed. On the physical observable algebra,
its remaining term is exactly the chiral fermion-measure or determinant
Jacobian. Consequently, that row is now a dependency of the already open
full nonabelian chiral-measure row rather than an independent norm-estimate
problem.

The physical continuum-promotion table remains \(1/9\). The number of
independent open exits falls from eight to seven.

## 1. Inputs and Scope

For each admitted finite auxiliary regulator \(N\), let:

1. \(\mathcal K_N\) be the finite regulator space;
2. \(G_{\rm SM}\) be the compact faithful Standard-Model gauge group acting
   continuously by a finite-dimensional unitary representation \(U_N\);
3. \(\mathcal A_N=B(\mathcal K_N)\);
4. \(\gamma_{N,g}(A)=U_N(g)AU_N(g)^*\);
5. \(E_N\) be the normalized Haar expectation;
6. \(P_N^0\) be the Gauss-neutral projector, where that closed-region
   compression is used;
7. \(H_N\) be a bounded gauge-invariant finite-regulator Hamiltonian.

The finite physical algebra is

\[
\mathcal A_N^{\rm phys}=E_N(\mathcal A_N)
\]

or its Gauss-neutral corner

\[
P_N^0E_N(\mathcal A_N)P_N^0.
\]

These objects are supplied by the prior fixed-coupling Cstar certificate.
This theorem does not select the regulator family, the upper action, or a
physical coupling value.

The BRST claim in this theorem concerns the differential induced on
ghost-number-zero observables by the infinitesimal compact-gauge action. It
does not construct a positive Hilbert representation of the full
indefinite ghost sector, nor does it identify fixed points with unrestricted
BV cohomology.

## 2. Exact Compact-Gauge Norm Defect

Define

\[
d_N^G(A)=\sup_{g\in G_{\rm SM}}
\left\|\gamma_{N,g}(A)-A\right\|.
\]

### Theorem 2.1

For every \(A\in\mathcal A_N^{\rm phys}\),

\[
d_N^G(A)=0.
\]

### Proof

Normalized Haar averaging gives

\[
E_N(B)=\int_{G_{\rm SM}}\gamma_{N,g}(B)\,dg.
\]

Left invariance of Haar measure implies

\[
\gamma_{N,h}(E_N(B))
=\int_{G_{\rm SM}}\gamma_{N,hg}(B)\,dg
=E_N(B)
\]

for every \(h\in G_{\rm SM}\). Thus every element in the range of \(E_N\)
is fixed pointwise. The difference inside the norm is the zero operator for
every \(g\), so its supremum is exactly zero. Compression by an invariant
Gauss projector preserves the identity. \(\square\)

This is stronger than a cutoff estimate. There is no sequence
\(\varepsilon_N\to0\): the bound is \(0\) at every cutoff.

## 3. BRST Differential on Ghost-Number-Zero Observables

Let \(X_a\) be a basis of the Lie algebra of the connected component of
\(G_{\rm SM}\), and write

\[
T_{N,a}=dU_N(X_a).
\]

For ghost generators \(c^a\), define the differential on an even observable
by

\[
s_NA=\sum_a[T_{N,a},A]c^a.
\]

The faithful Standard-Model gauge group is connected. More generally, the
argument below treats its identity component infinitesimally, while Haar
fixed points already impose any additional discrete invariance exactly.

### Theorem 3.1

For every \(A\in\mathcal A_N^{\rm phys}\),

\[
s_NA=0,
\qquad
d_N^{\rm BRST}(A):=\|s_NA\|=0.
\]

### Proof

For \(A\) in the Haar fixed-point algebra,

\[
U_N(\exp(tX_a))A
U_N(\exp(tX_a))^*=A
\]

for every \(t\). Differentiating at \(t=0\) gives

\[
[T_{N,a},A]=0.
\]

Every coefficient of \(s_NA\) therefore vanishes. Hence the BRST
differential and every norm of it are exactly zero. The same conclusion
holds in the Gauss-neutral corner. \(\square\)

This result is about the physical observable algebra. It does not say that
the full gauge-fixed field algebra has zero BRST differential. In fact, the
executable witness below includes a nonphysical probe with nonzero Gauss and
BRST defects.

## 4. Preservation by Fixed-Coupling Dynamics

Let

\[
\alpha_{N,t}(A)=e^{itH_N}Ae^{-itH_N},
\qquad
\gamma_{N,g}(H_N)=H_N.
\]

Then

\[
\gamma_{N,g}\circ\alpha_{N,t}
=\alpha_{N,t}\circ\gamma_{N,g}.
\]

Therefore

\[
\alpha_{N,t}\bigl(\mathcal A_N^{\rm phys}\bigr)
\subseteq\mathcal A_N^{\rm phys}.
\]

For every physical \(A\),

\[
d_N^G(\alpha_{N,t}(A))=0,
\qquad
d_N^{\rm BRST}(\alpha_{N,t}(A))=0.
\]

No locality, energy, Lieb-Robinson, or nuclearity estimate is needed for
this conclusion. Those estimates remain necessary for other continuum
rows, but not for an algebraic defect that is already identically zero at
each finite regulator.

## 5. Cstar Reduced-Product Descent

Let

\[
\mathcal A_{\mathcal U}
=
\left(\prod_N\mathcal A_N^{\rm phys}\right)
\big/
\mathcal I_{\mathcal U},
\]

where

\[
\mathcal I_{\mathcal U}
=
\left\{(A_N):
\lim_{\mathcal U}\|A_N\|=0
\right\}.
\]

For every uniformly bounded physical sequence \((A_N)\),

\[
d_N^G(A_N)=d_N^{\rm BRST}(A_N)=0
\]

for all \(N\). Both defect sequences belong to the norm-null ideal for
every ultrafilter and also converge ordinarily to zero. Thus the induced
Gauss and ghost-zero BRST defects vanish exactly in every reduced product.

This statement does not select an ultrafilter, prove that distinct
ultrafilters yield the same state, or establish the remaining locality and
phase-space estimates.

## 6. The Quantum Ward Functional

The combined Ward functional at a finite regulator has two logically
different sources:

\[
\mathfrak W_N(A)
=
\omega_N(s_NA)+\mathcal J_N(A).
\]

Here:

- \(\omega_N(s_NA)\) is the algebraic observable/action variation;
- \(\mathcal J_N(A)\) is the chiral fermion-measure or determinant
  Jacobian, including the finite-cutoff quantum-measure contribution to the
  QME.

On \(\mathcal A_N^{\rm phys}\), Theorem 3.1 gives

\[
\omega_N(s_NA)=0.
\]

Consequently,

\[
\boxed{\mathfrak W_N(A)=\mathcal J_N(A)}
\qquad
(A\in\mathcal A_N^{\rm phys}).
\]

This is the decisive reduction. The previously listed
`vanishing_Gauss_BRST_Ward_defect` row mixed an already exact algebraic
statement with a separate quantum-measure statement.

### What the formal anomaly result supplies

The selected three-family carrier has exact zero coefficients for all five
local four-dimensional gauge-anomaly channels. The registered
Adler-Bardeen and renormalized-BV results therefore provide a formal
counterterm scheme in which the local QME and Ward identities are restored
order by order.

This proves coefficientwise formal cancellation. It does not construct a
single nonperturbative chiral determinant measure at fixed coupling and does
not give a norm bound for its Jacobian.

### External constructive boundary

Luscher's anomaly-free \(U(1)\) lattice construction is genuinely
nonperturbative, exactly gauge invariant, and includes all finite-volume
topological sectors. His theorem for general compact gauge groups proves
exact anomaly cancellation at fixed lattice spacing to all orders of
perturbation theory.

The first theorem does not cover the full nonabelian Standard Model, and the
second is not a nonperturbative fixed-coupling measure theorem. Therefore
neither source fills \(\mathcal J_N\) for the present target.

## 7. Exact Rational Witness

Take

\[
G=
\operatorname{diag}(0,0,1,1),
\qquad
u=
\operatorname{diag}(1,1,-1,-1).
\]

The \(u\)-fixed algebra and the commutant of \(G\) are both

\[
M_2(\mathbb C)\oplus M_2(\mathbb C),
\]

of complex dimension \(8\). The zero-charge Gauss projector is

\[
P_0=\operatorname{diag}(1,1,0,0).
\]

Use the nilpotent ghost matrix

\[
c=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad c^2=0,
\]

and set

\[
Q=G\otimes c.
\]

Then \(Q^2=0\). For an even field observable,

\[
s(A)=[Q,A\otimes I_2]=[G,A]\otimes c.
\]

Thus all eight fixed matrix units are BRST closed. The graded second
differential is

\[
s^2(A)
=
\{Q,[Q,A\otimes I_2]\}
=
[Q^2,A\otimes I_2]
=0.
\]

The off-block matrix unit \(E_{02}\) has

\[
[G,E_{02}]=-E_{02}\ne0
\]

and hence a nonzero BRST defect. This confirms that the executable test is
not vacuous.

The rational block-diagonal dynamical unitary

\[
R=
\begin{pmatrix}
3/5&-4/5\\
4/5&3/5
\end{pmatrix},
\qquad
U=R\oplus R,
\]

commutes with \(G\), as does the finite fixed-coupling Hamiltonian. The
certificate checks exact closure before and after this dynamics on every
fixed matrix unit.

## 8. Promotion Table and Dependency Graph

The accepted rows remain:

| layer | count |
|---|---:|
| finite fixed-coupling Cstar landing | 5/5 |
| physical continuum promotion | 1/9 |
| Borel source | 1/6 |

The only accepted continuum row remains
`formal_EG_tangent_identification`.

The combined Ward row remains unaccepted, but now has the dependency

```text
vanishing_Gauss_BRST_Ward_defect
    -> full_nonabelian_chiral_measure_at_fixed_cutoff
```

The seven independent open continuum exits are:

1. geometry selection of the external q79 regulator;
2. a nonperturbative full nonabelian chiral measure;
3. cofinal embeddings or an asymptotic-morphism package;
4. a uniform locality or asymptotic-microcausality bound;
5. a uniform phase-space, energy, or nuclearity bound;
6. an ultrafilter-independent or independently selected limit;
7. a selected positive global interacting state.

The Ward row is an eighth false table entry, but it is no longer an eighth
independent construction.

## 9. Claim Boundary

This theorem closes:

- exact compact-gauge norm defect zero on finite physical observables;
- exact BRST defect zero on ghost-number-zero physical observables;
- preservation under gauge-invariant finite dynamics;
- descent of both zero defects through every Cstar reduced product;
- reduction of the full physical quantum Ward functional to the chiral
  measure Jacobian;
- elimination of one independent continuum blocker.

It does not close:

- the nonperturbative full nonabelian chiral fermion measure;
- a fixed-coupling determinant-Jacobian norm theorem;
- the full quantum Ward row;
- the interacting q79 continuum Cstar theory;
- `B.QFT.02` or `B.ACTION.01` overall.

No physical continuous parameter, discrete selector, fit, or observed value
is introduced.

## 10. Executable Certificate

The exact certificate is:

```text
certificates/q79_uniform_gauss_ghostzero_brst_ward_defect_reduction.certificate.json
```

It is generated by:

```text
mtt_qm_source.build.q79_uniform_gauss_ghostzero_brst_ward_defect_reduction
```

and is included in the canonical verifier.

## References

1. M. Luscher, *Abelian chiral gauge theories on the lattice with exact
   gauge invariance*, arXiv:hep-lat/9811032.
2. M. Luscher, *Lattice regularization of chiral gauge theories to all
   orders of perturbation theory*, arXiv:hep-lat/0006014.
3. G. Barnich, F. Brandt and M. Henneaux, *Local BRST cohomology in gauge
   theories*, arXiv:hep-th/0002245.
