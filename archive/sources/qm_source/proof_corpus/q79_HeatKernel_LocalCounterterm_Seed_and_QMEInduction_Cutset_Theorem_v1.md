# q79 Heat-Kernel Local-Counterterm Seed and QME-Induction Cutset Theorem

Date: 2026-07-26

## 1. Purpose

The cofinal sharp spectral cutoff is already closed for the free BV complex,
and the formal Epstein-Glaser/QME continuum scheme is already available. Raw
interacting cutoff removal is impossible because local coincident-point
traces diverge.

This theorem does not repeat those results. It constructs:

1. an exact smooth heat-semigroup BV regulator seed;
2. an exact normalized local-counterterm cocycle seed;
3. the coefficientwise zero-anomaly QME induction;
4. a reduction of the former six-row bridge to three independent q79 work
   packages.

The finite witnesses below test algebraic identities. They are not the
short-time heat coefficients of the selected q79 Standard-Model operator.

## 2. Exact heat-semigroup seed

Take three acyclic two-term blocks with differentials of weights \(1,2,3\).
In the ordered basis
\[
(a_1,b_1,a_2,b_2,a_3,b_3),
\]
let \(Qb_j=j\,a_j\) and \(Qa_j=0\). Then
\[
Q^2=0,\qquad
\Delta=QQ^\dagger+Q^\dagger Q
=\operatorname{diag}(1,1,4,4,9,9).
\tag{2.1}
\]

At the exact dyadic heat times \(t_k=k\log 2\), define
\[
H_k=e^{-t_k\Delta}=2^{-k\Delta}.
\tag{2.2}
\]
Every matrix entry is rational and
\[
H_kH_\ell=H_{k+\ell},\qquad [Q,H_k]=0.
\tag{2.3}
\]

For \(k<\ell\), define the regulated contracting propagator
\[
P_k^\ell
=Q^\dagger\Delta^{-1}(H_k-H_\ell).
\tag{2.4}
\]
Direct exact matrix multiplication gives
\[
P_k^\ell+P_\ell^m=P_k^m,
\qquad
QP_k^\ell+P_k^\ell Q=H_k-H_\ell.
\tag{2.5}
\]

These are the scale-composition and BV homotopy identities needed by a smooth
Wilsonian regulator. They close the finite algebraic seed only.

## 3. Exact counterterm-cocycle seed

Reuse the exact four-dimensional scaling divergence
\[
D_N=\sum_{n=1}^N n=\frac{N(N+1)}2.
\tag{3.1}
\]
Model a local order-\(\hbar g^2\) divergence by \(+\hbar D_Ng^2\), and set
\[
Z_N(g)=g-\hbar D_Ng^2.
\tag{3.2}
\]
Then, exactly,
\[
Z_N(0)=0,\qquad Z_N'(0)=1,
\tag{3.3}
\]
and the order-\(\hbar g^2\) renormalized coefficient is zero.

Between two cutoffs the coefficient difference obeys
\[
(D_M-D_N)+(D_L-D_M)=D_L-D_N.
\tag{3.4}
\]
Thus the comparison counterterms form an exact additive scale cocycle.

This witness proves that locality, Stueckelberg-Petermann normalization and
scale composition are mutually compatible. It does not calculate a q79
gauge, Higgs, Yukawa or boundary counterterm.

## 4. All-orders QME induction

Assume the selected heat-kernel regularization obeys a local quantum action
principle. Suppose the QME has been solved through order
\(\hbar^{n-1}\). The consistency condition makes the order-\(n\) defect
\(A_n\) a local ghost-number-one cocycle:
\[
sA_n=0.
\tag{4.1}
\]

If its local BRST class vanishes, there is a local ghost-number-zero
functional \(B_n\) such that
\[
A_n=sB_n.
\tag{4.2}
\]
Replacing the interaction by
\[
I\longmapsto I-\hbar^nB_n
\tag{4.3}
\]
cancels the order-\(n\) defect. Induction gives a formal QME scheme to all
orders.

The existing q79 anomaly theorem supplies the vanishing cohomological
obstruction. It does not emit the regulator-specific \(B_n\). The remaining
task is constructive rather than anomaly-theoretic.

## 5. What the external theorems do and do not supply

Albert extends Costello's heat-kernel renormalization procedure to a class of
manifolds with boundary. This supplies a legitimate theorem route once the
selected mixed q79 BV operator and its boundary conditions are proved to meet
the hypotheses. It does not perform that q79 verification.

The perturbative algebraic renormalization-group theorem identifies two
admissible local prescriptions up to a finite local
Stueckelberg-Petermann map. Therefore Epstein-Glaser target identification is
not an independent coefficient calculation after both prescriptions have
been constructed and shown admissible.

Primary references:

- B. I. Albert, *Heat Kernel Renormalization on Manifolds with Boundary*,
  <https://arxiv.org/abs/1609.02220>.
- R. Brunetti, M. Duetsch and K. Fredenhagen, *Perturbative Algebraic Quantum
  Field Theory and the Renormalization Groups*,
  <https://arxiv.org/abs/0901.2038>.
- G. Barnich, F. Brandt and M. Henneaux, *Local BRST Cohomology in Gauge
  Theories*, <https://arxiv.org/abs/hep-th/0002245>.

## 6. Reduction of the six rows

The six original requirements remain valid, but they are not six independent
frontiers.

| Original row | Current status | Work package |
|---|---|---|
| locality/support | conditional theorem route; q79 hypotheses open | HK |
| normalization | exact seed closed; full q79 map open | CT |
| QME/Ward | anomaly obstruction closed; coefficient primitives open | CT |
| microlocal Cauchy | requires q79 heat asymptotics and remainders | HK |
| EG identification | follows after the other packages | derived |
| BV-BFV gluing | phase cancellation closed; coefficient gluing open | GLUE |

The independent work is therefore:

### HK

Prove that the full selected mixed gauge-Higgs-chiral BV heat operator and its
boundary conditions have a local polyhomogeneous heat expansion with the
uniform microlocal remainder bounds required by the renormalization theorem.

### CT

Compute the local bulk and boundary heat coefficients and solve the
coefficientwise BRST primitive equations for the actual
\(Z_\epsilon\).

### GLUE

Prove that the resulting bulk and boundary counterterms commute with
restriction and cancel or pair correctly under the existing BV-BFV dual-line
gluing map.

After HK, CT and GLUE, the comparison with the already closed Epstein-Glaser
scheme is fixed up to one finite local Stueckelberg-Petermann map.

## 7. Theorem

**Theorem.** The exact finite Hodge model satisfies the heat-semigroup,
scale-additivity and BV contracting-homotopy identities. The quadratic local
counterterm witness satisfies \(Z(0)=0\), \(Z'(0)=1\), exact subtraction and
the additive scale-cocycle identity. Under a local quantum action principle,
vanishing of the local ghost-number-one anomaly class gives the stated
all-orders formal QME induction.

Consequently,

```text
B.QFT.02_exact_smooth_heat_regulator_seed
  = closed_exact;

B.QFT.02_exact_normalized_counterterm_cocycle_seed
  = closed_exact_at_quadratic_single_local_monomial_tier;

B.QFT.02_QME_anomaly_obstruction
  = closed_cohomologically_in_existing_formal_scheme;

B.QFT.02_spectral_cutoff_to_EG_counterterm_bridge
  = open_three_independent_q79_work_packages_HK_CT_GLUE.
```

## 8. Claim boundary

Still open:

- the selected q79 mixed-boundary heat-kernel theorem;
- actual bulk and boundary heat coefficients;
- uniform microlocal remainder estimates;
- actual coefficientwise q79 BRST primitives;
- counterterm compatibility under BV-BFV gluing;
- fixed-coupling or nonperturbative convergence.

No physical parameter, fit or observed value is added.

## 9. Reproduction

```powershell
python -m unittest tests.test_qm_source.QmSourceTestCase.test_heat_kernel_counterterm_seed_reduces_bridge_to_three_jobs -v
python scripts/verify.py
```

Certificate:

```text
certificates/q79_heat_kernel_counterterm_seed_and_qme_induction_cutset.certificate.json
```
