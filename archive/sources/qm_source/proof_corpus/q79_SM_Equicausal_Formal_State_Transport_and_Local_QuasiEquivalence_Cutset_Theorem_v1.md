# q79 SM Equicausal Formal State Transport and Local Quasi-Equivalence Cutset Theorem v1

Date: 2026-07-24

## Status

**Closed for formal physical algebra and state-cone transport under
Hadamard-seed, admissible renormalization-prescription and admissible
gauge-fixing changes.**

**Literal interacting local quasi-equivalence remains open and is not yet a
well-typed conclusion at the present formal-power-series tier.**

The executable certificate is:

`certificates/q79_sm_equicausal_formal_state_transport.certificate.json`.

It passes 41 of 41 checks.

## 1. Input chain

This theorem consumes four previously closed local results:

1. the gauge-fixed Green-hyperbolic equicausal BV algebra;
2. renormalized Epstein-Glaser time ordering and the anomaly-free formal QME
   scheme;
3. nonempty local formal positive physical state spaces and formal
   pre-Hilbert representations;
4. the contravariant local physical state-space functor with common-parent
   finite compatibility.

It does not reopen their carrier, anomaly, positivity or gluing proofs.

## 2. Presentation objects

Fix one admissible q79 chart \(O\). A presentation is a triple

\[
\mathfrak p=(H,T,\Psi),
\]

where:

- \(H\) is a compatible graded Hadamard covariance;
- \(T\) is an admissible local covariant renormalized time-ordering
  prescription in the anomaly-free QME class;
- \(\Psi\) is an admissible gauge-fixing fermion.

Each presentation gives a formal physical algebra

\[
\mathfrak A_{\rm phys}^{\mathfrak p}(O)
=
H^0\!\left(
\widehat s_V^{\mathfrak p},
\mathfrak A_{\rm int}^{\mathfrak p}(O)
\right)
\tag{2.1}
\]

over the formal perturbative ring.

The question is whether changing \(\mathfrak p\) changes the physical formal
theory or only its coordinates.

## 3. Hadamard-seed arrows

For \(H'=H+w\), where \(w\) is smooth and symmetric, define

\[
\beta_w=\exp(\hbar\Gamma_w),
\qquad
\Gamma_w
=
\frac12
\left\langle
w,\frac{\delta^2}{\delta\phi^2}
\right\rangle.
\tag{3.1}
\]

The normal-ordering identities are

\[
\beta_w(F\star_HG)
=
\beta_w(F)\star_{H'}\beta_w(G),
\tag{3.2}
\]

\[
\beta_0=\operatorname{id},
\qquad
\beta_{w_2}\beta_{w_1}=\beta_{w_1+w_2},
\qquad
\beta_w^{-1}=\beta_{-w}.
\tag{3.3}
\]

Thus compatible Hadamard choices are objects of an exact star-isomorphism
groupoid. No preferred Hadamard seed is selected.

### Exact finite witness

On the polynomial basis

\[
(1,x,x^2,x^3,x^4),
\]

let

\[
\Gamma=\frac12\frac{d^2}{dx^2}.
\]

Because \(\Gamma\) is nilpotent on this space,

\[
\beta_t=\exp(t\Gamma)
\]

is a finite rational matrix. The certificate checks:

- \(\beta_0=I_5\);
- \(\beta_t^{-1}=\beta_{-t}\);
- \(\beta_s\beta_t=\beta_{s+t}\);
- \(\operatorname{rank}\beta_t=5\);
- exact star-product intertwining for all 15 monomial pairs whose total
  degree is at most four.

The witness uses rational covariances \(1/5\), \(2/7\) and \(-1/3\), so no
floating-point tolerance enters.

## 4. Renormalization-prescription arrows

The Main Theorem of perturbative renormalization states that two admissible
local prescriptions are related by a local analytic
Stueckelberg-Petermann map

\[
Z,\qquad Z(0)=0,\qquad Z'(0)=\operatorname{id}.
\tag{4.1}
\]

The map \(Z\) intertwines the corresponding formal S-matrices and induces a
formal algebra isomorphism. This is a relation between admissible
prescriptions, not a numerical prediction of a renormalization scale or
scheme.

The exact q79 anomaly vector is zero and the prior certificate supplies an
all-orders compatible QME scheme. Hence the prescription transport stays
inside the declared anomaly-free formal class.

## 5. Gauge-fixing arrows

For an admissible compactly supported change

\[
\Psi\longmapsto\Psi+\delta\Psi,
\]

the renormalized BV theorem and the closed q79 QME scheme induce a formal
cohomology isomorphism

\[
\mathfrak A_{\rm phys}^{(H,T,\Psi)}(O)
\cong
\mathfrak A_{\rm phys}^{(H,T,\Psi+\delta\Psi)}(O).
\tag{5.1}
\]

Equation (5.1) is gauge-fixing independence of the formal physical
cohomology. It is not selection of one preferred gauge and is not a
nonperturbative gauge-independence theorem.

## 6. Physical state transport

Let

\[
I:\mathfrak A\longrightarrow\mathfrak A'
\]

be any of the resulting unital star isomorphisms. A state \(\omega\) on
\(\mathfrak A\) transports to

\[
\omega'=\omega\circ I^{-1}.
\tag{6.1}
\]

Normalization is preserved:

\[
\omega'(1)=\omega(1)=1.
\tag{6.2}
\]

Formal positivity is preserved:

\[
\omega'(a'^*a')
=
\omega\!\left(
I^{-1}(a')^*I^{-1}(a')
\right)
\succeq0.
\tag{6.3}
\]

If the algebra maps intertwine the quantum BRST differentials, (6.1)
descends to ghost-number-zero physical cohomology.

### Exact finite witness

The certificate takes

\[
U=
\begin{pmatrix}
3/5&-4/5\\
4/5&3/5
\end{pmatrix},
\qquad
\rho=
\begin{pmatrix}
2/3&0\\
0&1/3
\end{pmatrix}
\]

and

\[
I(A)=UAU^T,\qquad
\rho'=U\rho U^T.
\]

It verifies exactly that:

- \(U^TU=UU^T=I_2\);
- \(I\) is unital and preserves products and involution on all matrix-unit
  pairs;
- both density matrices are positive and have trace one;
- \(\operatorname{Tr}(\rho A)=\operatorname{Tr}(\rho'I(A))\) on a matrix
  basis;
- positive-square expectations agree on six independent witnesses.

This finite witness checks the algebraic mechanism. The infinite-dimensional
existence statements continue to rest on the cited pAQFT/BV theorems and the
declared q79 hypotheses.

## 7. Compatibility with restriction

For an admissible chart embedding

\[
\chi:O\hookrightarrow O',
\]

the local algebra map \(\alpha_\chi\) intertwines the QME/BRST structures.
The presentation arrows are local and covariant. Therefore the square

\[
\begin{array}{ccc}
\mathfrak A_{\rm phys}^{\mathfrak p}(O)
&\xrightarrow{I_O}&
\mathfrak A_{\rm phys}^{\mathfrak p'}(O)\\
\downarrow\alpha_\chi&&\downarrow\alpha_\chi\\
\mathfrak A_{\rm phys}^{\mathfrak p}(O')
&\xrightarrow{I_{O'}}&
\mathfrak A_{\rm phys}^{\mathfrak p'}(O')
\end{array}
\]

commutes on the declared formal domain.

After pulling states back, presentation transport therefore commutes with
the contravariant local-state restriction functor.

## 8. Formal presentation-independence theorem

**Theorem.** For every declared q79 chart \(O\), admissible changes of:

1. Hadamard covariance;
2. renormalized time-ordering prescription;
3. gauge-fixing fermion

generate specified formal star/BV isomorphisms between the corresponding
physical algebras. These isomorphisms:

- compose and have inverses in their declared classes;
- descend to ghost-number-zero quantum-BRST cohomology;
- transport normalized formal positive physical states bijectively;
- commute with admissible local restriction.

Hence the local formal physical algebra/state-cone functor is
presentation-independent up to the specified formal isomorphisms.

No new physical parameter is introduced.

## 9. Why this is not local quasi-equivalence

Local quasi-equivalence is a representation-theoretic statement. For two
states \(\omega_1,\omega_2\) on a local C*-algebra
\(\mathfrak A(O)\), one compares their GNS representations and local von
Neumann closures. Equivalent formulations involve equality of normal folia
or quasi-equivalent normal representations.

The current q79 interacting object is instead:

- a formal power-series algebra;
- equipped with formal positive states;
- represented on formal pre-Hilbert modules.

It has no selected C*-norm at fixed nonzero physical coupling, no completed
local C*-net for the full gauge-BRST Standard Model, and no local von
Neumann closures. Therefore the expression

\[
\text{interacting local quasi-equivalence}
\]

has no completed representation-theoretic target yet.

Buchholz and Fredenhagen construct a dynamical interacting C*-net for scalar
Lagrangians and explicitly isolate suitable-state/representation existence
as a further problem. That is a useful benchmark, not a theorem that supplies
the missing full q79 SM gauge-BRST completion.

## 10. Cutset

Closed before literal local quasi-equivalence:

- equicausal free/BV functional carrier;
- formal interacting QME algebra;
- nonempty formal positive physical state spaces;
- local state-space restriction functor;
- Hadamard-seed transport;
- renormalization-prescription transport;
- gauge-fixing transport;
- formal physical state-cone presentation independence.

Still required:

1. construct a fixed-coupling local C*-net for the completed q79 SM
   gauge-BRST theory;
2. specify an admissible physical state class on that net;
3. construct its local GNS representations;
4. take local von Neumann closures;
5. compare their normal folia.

Only after these five objects exist is literal local quasi-equivalence a
well-typed exit theorem.

## 11. Blocker delta

Newly closed:

- `B.QFT.02_Hadamard_seed_transport`;
- `B.QFT.02_renormalization_scheme_transport`;
- `B.QFT.02_gauge_fixing_transport`;
- `B.QFT.02_formal_physical_state_cone_transport`.

Reclassified sharply:

- `B.QFT.02_literal_interacting_local_quasi_equivalence` is
  `not_yet_well_typed_without_fixed_coupling_Cstar_von_Neumann_completion`.

Still open:

- fixed-coupling local quasi-equivalence;
- one selected global interacting q79 state;
- numerical RG matching and uncertainty transport;
- nonperturbative completion;
- strict upper-MTT action/background selection.

## 12. Parameter ledger

\[
\begin{array}{l|c}
\text{new physical continuous parameters}&0\\
\text{new physical discrete selectors}&0\\
\text{new fits}&0\\
\text{new observed values}&0
\end{array}
\]

\(H\), \(T\) and \(\Psi\) label equivalent formal presentations. They are not
counted as physical fit parameters.
