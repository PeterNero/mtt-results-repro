# q79 SM Local Formal BRST Physical State and Positivity Theorem v1

Date: 2026-07-24

## Status

**Closed as an existence theorem for formal positive interacting states and
formal physical pre-Hilbert representations on a basis of bounded,
causally complete, \(H^1=0\) q79 regions.**

The executable certificate is:

`certificates/q79_sm_local_formal_physical_state.certificate.json`.

It passes 74 of 74 checks.

This result is deliberately local and perturbative. It does not select a
preferred vacuum, glue the local states into one global cosmological state,
construct a Hilbert space at fixed nonzero coupling, prove an infrared
scattering limit, or provide a nonperturbative Standard Model.

## 1. Anti-loop boundary

The preceding q79 Standard-Model certificates already establish:

1. the selected framed globally hyperbolic q79 spacetime;
2. the faithful compact group
   \[
   G=(SU(3)\times SU(2)\times U(1))/\mathbb Z_6;
   \]
3. the three-family rank-48 left-Weyl bundle and one Higgs doublet;
4. the nonlinear classical BRST/BV complex;
5. the gauge-fixed Green-hyperbolic free complex;
6. its microcausal free star algebra;
7. renormalized Epstein-Glaser time ordering;
8. the exact local anomaly vector
   \[
   (0,0,0,0,0);
   \]
9. an all-orders formal QME prescription;
10. a nilpotent interacting quantum-BV differential.

This theorem does not rebuild those layers. It discharges the next named
clause: existence of a positive physical interacting state or
representation.

The old corpus route from transverse-traceless reflection positivity to full
BRST positivity is not used. Positivity of a smaller TT sector does not imply
positivity of the gauge, ghost, Higgs, and matter quotient.

## 2. Local domain

Let \(U\) be a bounded open subset of a q79 Cauchy surface with smooth
boundary and compact closure. Require

\[
H^1(U;\mathbb R)=0,
\tag{2.1}
\]

and let

\[
O=D(U)
\tag{2.2}
\]

be its domain of dependence. A sufficiently small coordinate ball satisfies
(2.1), so regions of this form give a local basis inside every smooth q79
background chart.

On gauge one-forms use the mixed boundary conditions employed in the local
Yang-Mills construction:

- tangential Dirichlet data;
- normal Neumann data;
- compatible scalar and ghost conditions.

Together with (2.1), these conditions remove the one-form and scalar zero
modes needed for the local charge construction.

The local principal bundle is trivial. This is a statement about a
contractible chart, not a claim that the full q79 gauge bundle is globally
trivial.

Use a symmetric on-shell local background and split the action so that the
free gauge, Higgs, and Weyl operators are the previously certified
Green-hyperbolic operators. Put the gauge, Yukawa, and scalar-potential
interactions into

\[
V_\lambda=\lambda V.
\tag{2.3}
\]

The single \(\lambda\) is a bookkeeping variable. The distinct Standard-Model
couplings remain coefficients of \(V\); no physical relation among them is
introduced.

## 3. Exact one-mode BRST quartet

For one nonzero spatial eigenmode and one gauge generator, take the ordered
graded basis

\[
(\epsilon_1,\epsilon_2,x,y,c,\bar c),
\tag{3.1}
\]

with ghost numbers

\[
(0,0,0,0,+1,-1)
\tag{3.2}
\]

and parities

\[
(\mathrm{even},\mathrm{even},\mathrm{even},\mathrm{even},
\mathrm{odd},\mathrm{odd}).
\tag{3.3}
\]

Here \(\epsilon_1,\epsilon_2\) are transverse polarizations, \(x\) is the
longitudinal gauge direction, \(y\) is the auxiliary/Nakanishi direction,
and \(c,\bar c\) are the ghost and antighost directions.

Define

\[
Q_0x=c,\qquad Q_0\bar c=y,
\tag{3.4}
\]

with \(Q_0\) zero on the other four basis vectors. In the basis (3.1),

\[
Q_0=
\begin{pmatrix}
0&0&0&0&0&0\\
0&0&0&0&0&0\\
0&0&0&0&0&0\\
0&0&0&0&0&1\\
0&0&1&0&0&0\\
0&0&0&0&0&0
\end{pmatrix}.
\tag{3.5}
\]

Use the Krein form

\[
J=
\begin{pmatrix}
1&0&0&0&0&0\\
0&1&0&0&0&0\\
0&0&0&1&0&0\\
0&0&1&0&0&0\\
0&0&0&0&0&1\\
0&0&0&0&1&0
\end{pmatrix}.
\tag{3.6}
\]

The certificate checks over exact rationals that

\[
Q_0^2=0,\qquad Q_0^\dagger J=JQ_0.
\tag{3.7}
\]

Define the degree-minus-one homotopy

\[
hc=x,\qquad hy=\bar c
\tag{3.8}
\]

and let \(P_{\mathrm{phys}}\) project onto
\(\operatorname{span}\{\epsilon_1,\epsilon_2\}\). Then

\[
Q_0h+hQ_0=I-P_{\mathrm{phys}}.
\tag{3.9}
\]

Equation (3.9) proves contractibility of every nonphysical direction. It is
stronger than a rank count.

At ghost number zero,

\[
\ker Q_0
=
\operatorname{span}\{\epsilon_1,\epsilon_2,y\},
\qquad
\operatorname{im}Q_0
=
\operatorname{span}\{y\}.
\tag{3.10}
\]

The restricted Gram matrix is exactly

\[
\left.J\right|_{\ker Q_0,\ \mathrm{gh}=0}
=
\operatorname{diag}(1,1,0).
\tag{3.11}
\]

Therefore it is positive semidefinite, and its null space is exactly the
BRST-exact subspace. The physical quotient is

\[
\mathcal H_{\mathrm{phys},0}^{(1)}
=
\frac{\ker Q_0\cap\{\mathrm{gh}=0\}}
{\operatorname{im}Q_0\cap\{\mathrm{gh}=0\}}
\cong\mathbb C^2
\tag{3.12}
\]

with Gram matrix \(I_2\).

## 4. Full free q79 Standard-Model representation

The Lie-algebra dimensions are

\[
\dim su(3)+\dim su(2)+\dim u(1)=8+3+1=12.
\tag{4.1}
\]

Repeating the quartet over the 12 generators gives, per nonzero spatial
eigenmode:

\[
72\ \text{graded gauge/ghost directions},
\qquad
24\ \text{physical transverse directions}.
\tag{4.2}
\]

The local compact-gauge-group mode construction supplies compatible vector
and scalar Hadamard two-point functions on \(D(U)\). Its Fock/Krein
representation repeats (3.5)-(3.12) over all eigenmodes and gauge
generators. Thus the ghost-number-zero gauge quotient is positive.

At zeroth order in \(\lambda\), the Higgs and Weyl fields are BRST closed.
Choose:

1. a positive quasifree Hadamard scalar state for the four real Higgs
   components;
2. a positive quasifree CAR Hadamard state for the rank-48 chiral internal
   bundle, whose rank-two left-Weyl spin factor gives 96 complex local field
   components.

The Weyl state can be obtained locally by restricting a compatible Dirac
Hadamard state to the chiral subspace. Tensoring these factors with the gauge
physical quotient gives

\[
\omega_0
=
\omega_{\mathrm{gauge,phys}}
\otimes
\omega_H
\otimes
\omega_{\mathrm{Weyl}}.
\tag{4.3}
\]

It is a normalized positive free physical Hadamard state. This proves
nonemptiness; it does not select one distinguished \(\omega_0\).

## 5. Interacting BRST charge

The anomalous Master Ward identity relates the divergence of the
renormalized interacting BRST current to the local QME anomaly. In the
preceding certificate, the complete nontrivial anomaly class is exactly zero,
and BRST-exact remainders are removed by a finite local normalization.
Consequently one may choose the renormalized prescription so that

\[
dJ_I=0.
\tag{5.1}
\]

The unitarity normalization makes the current hermitian. Smearing across a
Cauchy surface inside \(D(U)\), with the boundary conditions of Section 2,
defines

\[
Q_I=\int\gamma\wedge J_I
=Q_0+\lambda Q_1+\lambda^2Q_2+\cdots.
\tag{5.2}
\]

The Ward hierarchy and QME give

\[
Q_I^\dagger=Q_I,\qquad Q_I^2=0,
\tag{5.3}
\]

and

\[
[Q_I,A]_{\mathrm{gr}}
=
i\widehat s_V(A)
\tag{5.4}
\]

on the local interacting algebra.

This is the step for which anomaly cancellation is essential. A nonzero
ghost-number-one anomaly could obstruct (5.1) or (5.3).

The local Yang-Mills theorem proves the current/charge construction for a
compact gauge group. The deformation-stability lemma is algebraic once
(5.2)-(5.3) hold. Adding the Higgs and chiral matter changes the coefficients
of \(Q_n\), but not that lemma. The SM-specific possible obstruction is the
gauge anomaly, which the preceding exact certificate removes.

## 6. Formal deformation stability

Let \(\mathcal K[[\lambda]]\) be the free Krein space extended by formal
power series. Set

\[
\mathcal K_I^0
=
\ker Q_I\cap\{\mathrm{gh}=0\},
\qquad
\mathcal N_I
=
\operatorname{im}Q_I\cap\{\mathrm{gh}=0\}.
\tag{6.1}
\]

For a hermitian scalar formal series, use the square cone

\[
\mathbb C[[\lambda]]_+
=
\{c(\lambda)^*c(\lambda):c(\lambda)\in\mathbb C[[\lambda]]\}.
\tag{6.2}
\]

This is formal positivity. It is not a claim that the perturbation series
converges to a positive number at a fixed coupling.

The Duetsch-Fredenhagen deformation theorem applies to (5.2)-(5.3) because
the zeroth-order representation satisfies (3.11). It gives:

\[
\langle\Psi_I,\Psi_I\rangle
\in\mathbb C[[\lambda]]_+
\quad
\text{for every }\Psi_I\in\mathcal K_I^0,
\tag{6.3}
\]

\[
\Psi_I\in\mathcal K_I^0,\quad
\langle\Psi_I,\Psi_I\rangle=0
\quad\Longrightarrow\quad
\Psi_I\in\mathcal N_I,
\tag{6.4}
\]

and every free physical vector has at least one formal \(Q_I\)-closed lift.

Hence

\[
\mathcal H_{\mathrm{phys},I}(O)
=
\frac{\mathcal K_I^0}{\mathcal N_I}
\tag{6.5}
\]

is a formal pre-Hilbert space, and the ghost-number-zero interacting
cohomology acts on it.

Choose a positive-norm free physical vector \(\Psi_0\), a formal lift
\(\Psi_I\), and normalize its invertible formal norm. Then

\[
\omega_I([A])
=
\frac{
\langle\Psi_I,\pi_I([A])\Psi_I\rangle
}{
\langle\Psi_I,\Psi_I\rangle
}
\tag{6.6}
\]

is a normalized formal positive state on

\[
H^0(\widehat s_V,\mathfrak A_{\mathrm{int}}(O)).
\tag{6.7}
\]

The state is well defined on cohomology because exact operators act trivially
between closed physical classes.

## 7. Theorem

**Theorem.** Let \(O=D(U)\) satisfy Section 2, and use the anomaly-free
renormalized-QME prescription already certified for the q79 Standard-Model
field stack. Then:

1. the free gauge/ghost sector has the exact graded quartet (3.5);
2. its ghost-number-zero cohomology has positive Gram matrix \(I_2\) per
   gauge generator and nonzero spatial eigenmode;
3. the full free gauge-Higgs-Weyl physical representation has a nonempty
   positive Hadamard state space;
4. the zero local anomaly class permits a conserved hermitian interacting
   BRST current and a nilpotent charge \(Q_I\);
5. free physical positivity and null-equals-exactness are stable under the
   formal interaction deformation;
6. the local interacting quantum-BV cohomology has a nonempty family of
   normalized formal positive states and formal pre-Hilbert
   representations.

No new physical parameter, fit, or observed value is used.

## 8. Exact scope of the closure

This closes:

`B.QFT.02_positive_physical_interacting_state`

at the following tier:

```text
local + bounded H1-zero chart + formal perturbation series + existence
```

It does not close:

- selection of a preferred q79 state;
- compatibility of independently constructed local states on overlaps;
- a single global interacting cosmological state;
- a completed Hilbert representation at fixed physical couplings;
- selected RG running, threshold matching, or uncertainties;
- observable comparison;
- an infrared scattering state or S-matrix;
- convergence or nonperturbative completion;
- the upper-MTT action and vacuum source.

Thus `B.QFT.02` remains open overall.

## 9. Why the old positivity claim is not being revived

The earlier conditional quantum-gravity papers assumed a physical
Osterwalder-Schrader or TT positivity statement. No implication from that
assumption is used here.

The present proof instead uses:

1. a Lorentzian local Green-hyperbolic construction;
2. an explicit graded BRST quartet;
3. exact null-equals-exactness at ghost number zero;
4. the already proved anomaly-free interacting charge;
5. an algebraic deformation-stability theorem.

The ghost-extended BV algebra remains indefinite. Positivity appears only
after taking physical ghost-number-zero BRST cohomology.

## 10. Parameter ledger

\[
\begin{array}{l|c}
\text{new physical continuous parameters}&0\\
\text{new physical discrete selectors}&0\\
\text{new fits}&0\\
\text{new observed inputs}&0.
\end{array}
\]

The Hadamard seed, free physical vector, and formal lift label states. They
are state choices, not action parameters and not an MTT state-selection
theorem.

## 11. Primary mathematical context

Formal deformation stability of BRST positivity:

- M. Duetsch and K. Fredenhagen,
  *Deformation stability of BRST-quantization*,
  <https://arxiv.org/abs/hep-th/9807215>.

Local compatible Hadamard functions, positive BRST quotient, interacting
charge, and nonabelian Yang-Mills deformation:

- S. Hollands,
  *Renormalized Quantum Yang-Mills Fields in Curved Spacetime*,
  <https://arxiv.org/abs/0705.3340>.

Case-by-case positivity boundary for linear gauge theories:

- T.-P. Hack and A. Schenkel,
  *Linear bosonic and fermionic quantum gauge theories on curved
  spacetimes*, <https://arxiv.org/abs/1205.3484>.

The renormalized-QME, anomaly, and faithful-group sources are those cited in
the preceding q79 SM QME theorem.

## 12. Reproduction

```powershell
python scripts\verify.py
python -m unittest discover -s tests -v
```
