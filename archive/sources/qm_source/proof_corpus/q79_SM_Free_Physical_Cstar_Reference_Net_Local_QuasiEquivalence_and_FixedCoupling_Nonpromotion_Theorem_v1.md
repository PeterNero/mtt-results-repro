# q79 SM Free Physical C*-Reference Net, Local Quasiequivalence, and Fixed-Coupling Nonpromotion Theorem v1

## 1. Status

This packet advances `B.QFT.02` beyond the formal state-transport tier without
promoting the interacting formal series to a nonperturbative theory.

It proves two distinct statements.

1. At the exact free reference coordinate `lambda=0`, the selected q79
   Standard-Model carrier defines a representation-independent local physical
   C*-net. Its declared Hadamard state class has literal GNS
   representations, local von Neumann closures, and locally quasiequivalent
   normal folia.
2. The all-orders formal interacting jet at `lambda=0` cannot, by itself,
   select a unique fixed-nonzero-coupling dynamics or state. The obstruction
   is exact: the smooth jet map has a nontrivial flat kernel.

The executable certificate is
`certificates/q79_sm_free_physical_cstar_reference_and_nonpromotion.certificate.json`.

## 2. Inputs and domain

Let `q79Chart_0` be the category used by the prior hyperbolic and formal-state
packets. An object is a bounded causally complete q79 region

\[
  O=D(U)
\]

with compact closure, \(H^1(U;\mathbb R)=0\), and trivial local gauge bundle.
The background is one of the declared on-shell q79 SM charts.

The inherited exact data are:

- the faithful compact gauge group
  \[
  G_{\rm SM}=({\rm SU}(3)\times {\rm SU}(2)\times {\rm U}(1))/\mathbb Z_6;
  \]
- twelve gauge generators and two positive physical polarizations per
  generator and spatial mode;
- one Higgs doublet, hence four real scalar components;
- the rank-48 three-family chiral internal carrier;
- a Green-hyperbolic gauge-fixed free BV complex;
- positive ghost-zero free BRST cohomology on the declared charts.

The gauge Hadamard part is restricted to backgrounds and covariances for
which the prior compatible construction admits a
Gerard-Wrochna-type pseudodifferential Cauchy-data realization. This is a
declared state-class condition, not a claim about every Yang-Mills
background.

## 3. The free physical C*-net

### 3.1 Gauge factor

For a region \(O\), let

\[
 {\cal V}_{g,\mathrm{phys}}(O)
 =
 \ker K^*/\operatorname{ran}P
\]

be the real physical linearized gauge phase space, with symplectic form
\(\sigma_g\) induced by the causal propagator. Equivalently, this is the
positive ghost-zero cohomology of the exact free BRST complex.

The prior one-mode calculation gives

\[
 \ker Q_0|_{\mathrm{gh}=0}/\operatorname{im}Q_0
 \cong \mathbb R^2,
 \qquad
 G_{\mathrm{phys}}=I_2.
\]

Repeating this quotient over the twelve compact gauge generators and all
local modes gives the physical gauge Weyl algebra

\[
 {\mathfrak W}_g(O)
 =
 {\rm CCR}({\cal V}_{g,\mathrm{phys}}(O),\sigma_g).
\]

This is a C*-algebra defined by the universal Weyl relations. The linear
gauge quotient and its positivity are the domain where
[Hack-Schenkel](https://arxiv.org/abs/1205.3484) applies.

### 3.2 Higgs and chiral matter factors

Let \({\cal V}_H(O)\) be the direct sum of the four real Higgs
Klein-Gordon phase spaces. Define

\[
 {\mathfrak W}_H(O)
 =
 {\rm CCR}({\cal V}_H(O),\sigma_H).
\]

Let \({\cal K}_\psi(O)\) be the self-dual one-particle space of the selected
rank-48 chiral carrier, with conjugation \(\Gamma\). Define

\[
 {\mathfrak C}_\psi(O)
 =
 {\rm CAR}({\cal K}_\psi(O),\Gamma).
\]

The prior framed free-Dirac packet supplies the CAR functor, graded locality,
time-slice, and the Hadamard state class. Restriction to the selected chiral
subcarrier and then to the even algebra does not introduce a new action
coefficient.

### 3.3 Field and observable nets

Define the free field net

\[
 {\mathfrak F}_0(O)
 =
 {\mathfrak W}_g(O)
 \otimes_{\min}
 {\mathfrak W}_H(O)
 \otimes_{\min}
 {\mathfrak C}_\psi(O).
\]

The selected internal group and fermion parity act continuously by
C*-automorphisms. The local physical observable algebra is

\[
 {\mathfrak A}_0(O)
 =
 {\mathfrak F}_0(O)^{
   G_{\rm SM}\times\mathbb Z_2^F
 }.
\]

Because a fixed-point set of a C*-algebra under a continuous compact-group
action is a C*-subalgebra, \({\mathfrak A}_0(O)\) is well defined. The causal
maps of the three free field functors induce isotonic maps on
\({\mathfrak F}_0\), and restriction to fixed points induces the maps on
\({\mathfrak A}_0\). Locality and time-slice are inherited sectorwise.

This is a literal C*-net at the exact free coordinate \(\lambda=0\). It is
not the interacting C*-net at measured nonzero couplings.

## 4. Literal local quasiequivalence

Two states \(\omega_1,\omega_2\) on a local C*-algebra are locally
quasiequivalent when their restricted GNS representations generate the same
normal folium, equivalently when there is a normal isomorphism

\[
 \Theta_O:
 \pi_{\omega_1}({\mathfrak A}_0(O))''
 \longrightarrow
 \pi_{\omega_2}({\mathfrak A}_0(O))''
\]

with
\(\Theta_O(\pi_{\omega_1}(A))=\pi_{\omega_2}(A)\).

### 4.1 Higgs sector

Verch proved local quasiequivalence of quasifree Hadamard
representations of the Klein-Gordon Weyl algebra on globally hyperbolic
spacetimes. Applying the theorem to each of the four real Higgs components,
and taking the finite tensor product, closes the Higgs sector.

Primary source:
[Verch, Commun. Math. Phys. 160 (1994)](https://doi.org/10.1007/BF02173427).

### 4.2 Chiral CAR sector

D'Antoni and Hollands proved local quasiequivalence of quasifree Hadamard
representations of the free Dirac CAR algebra. The normal intertwiner
restricts to the selected chiral carrier and its even subalgebra.

Primary source:
[D'Antoni-Hollands](https://arxiv.org/abs/math-ph/0106028).

### 4.3 Gauge implementable Hadamard orbit

Gerard and Wrochna construct positive gauge-invariant Hadamard
two-point functions for linearized Yang-Mills theory under their stated
background hypotheses:
[Gerard-Wrochna](https://arxiv.org/abs/1403.7153).

Fix one such covariance \(S_g\) on the physical quotient. Let
\({\cal O}_{\rm impl}(S_g)\) contain the covariances obtained by
constraint-preserving, compactly localized symplectic transformations whose
off-diagonal part is Hilbert-Schmidt in the \(S_g\) one-particle topology.
The identity is in this orbit. Nontrivial finite-rank symplectic rotations on
smooth physical mode pairs are also in it, so the class is not a singleton.

For every pair in this orbit:

1. the induced one-particle topologies agree;
2. the square-root covariance difference is Hilbert-Schmidt;
3. the covariance difference is smooth, so the Hadamard wavefront set is
   unchanged;
4. the transformations preserve the gauge constraint and physical quotient.

The first two clauses are precisely the Araki-Yamagami criterion:
[Araki-Yamagami](https://doi.org/10.2977/prims/1195183576).
Thus all states in \({\cal O}_{\rm impl}(S_g)\) are quasiequivalent. In fact,
the defining transformations are unitarily implementable, so this statement
is stronger than merely local quasiequivalence.

This does not prove that two arbitrary gauge Hadamard covariances lying in
different implementability classes are locally quasiequivalent.

### 4.4 Tensor and fixed-point descent

Take two product Hadamard states whose three sector states satisfy the
preceding conditions. The tensor product of the three normal intertwining
isomorphisms is normal and intertwines the local field algebras. Therefore
the two product representations of \({\mathfrak F}_0(O)\) are
quasiequivalent.

If \(B\subset {\mathfrak F}_0(O)\) is any C*-subalgebra, the same normal
isomorphism maps
\(\pi_1(B)''\) onto \(\pi_2(B)''\). Apply this to

\[
 B={\mathfrak A}_0(O)
 =
 {\mathfrak F}_0(O)^{G_{\rm SM}\times\mathbb Z_2^F}.
\]

Hence the restricted physical observable representations are locally
quasiequivalent.

The theorem closes literal GNS/von-Neumann folia at the free reference tier
and on the declared Hadamard class. It does not close interacting local
quasiequivalence.

## 5. Exact finite C*-mechanism witness

The executable packet separately checks the finite model

\[
 M_2^{(g)}
 \otimes
 M_2^{(H)}
 \otimes
 M_2^{(\psi)}
 \cong M_8.
\]

It verifies over exact rational arithmetic that:

- the 64 elementary tensors have rank 64 in \(M_8\);
- the three factor embeddings are unital and commute pairwise;
- the product density matrix has trace one and full support;
- restriction of the product state gives each factor state exactly;
- two distinct faithful product densities have the same finite-dimensional
  normal folium.

This is an exact witness for the algebraic mechanisms in Sections 3 and 4.
It is not a truncation asserted to equal the continuum q79 field theory.

## 6. Fixed-coupling nonpromotion theorem

### 6.1 Noninjectivity of the smooth jet map

Let

\[
 J^\infty_0:
 C^\infty([-1,1])
 \longrightarrow
 \mathbb R[[\lambda]]
\]

send a smooth function to its complete Taylor jet at \(\lambda=0\).
Define

\[
 f(0)=0,
 \qquad
 f(\lambda)
 =
 \frac12\exp\left(1-\frac1{\lambda^2}\right)
 \quad (0<|\lambda|\leq 1).
\]

Set \(x=1/\lambda\). By induction,

\[
 f^{(n)}(\lambda)
 =
 P_n(x)e^{1-x^2},
\]

where

\[
 P_0(x)=\frac12,
 \qquad
 P_{n+1}(x)
 =
 -x^2P_n'(x)+2x^3P_n(x).
\]

Each \(P_n\) is a polynomial. Gaussian decay dominates every polynomial, so

\[
\lim_{\lambda\to0}f^{(n)}(\lambda)=0
\]

for every \(n\). Consequently \(f\) is smooth at zero and

\[
 J^\infty_0(f)=0.
\]

But \(f(1)=1/2\), so \(f\neq0\). Therefore \(J^\infty_0\) is not injective.

### 6.2 Exact dynamics witness

On the fixed C*-algebra \(M_2\), compare

\[
 H_0(\lambda)=
 \begin{pmatrix}0&0\\0&1\end{pmatrix},
 \qquad
 H_f(\lambda)=
 \begin{pmatrix}f(\lambda)&0\\0&1\end{pmatrix}.
\]

The two Hamiltonian families have identical formal jets at zero. At
\(\lambda=1\),

\[
 H_0(1)=\operatorname{diag}(0,1),
 \qquad
 H_f(1)=\operatorname{diag}(1/2,1).
\]

For \(E_{12}\), their exact dynamical derivations are

\[
 [H_0(1),E_{12}]=-E_{12},
 \qquad
 [H_f(1),E_{12}]=-\frac12E_{12}.
\]

Thus the fixed-coupling C*-dynamics differ even though every perturbative
coefficient agrees.

### 6.3 Exact state witness

Compare

\[
 \rho_0(\lambda)
 =
 \operatorname{diag}(2/3,1/3)
\]

and

\[
 \rho_f(\lambda)
 =
 \operatorname{diag}
 \left(
   2/3-f(\lambda)/6,\,
   1/3+f(\lambda)/6
 \right).
\]

Since \(0\leq f(\lambda)\leq1/2\), both are faithful normalized states for
\(\lambda\in[-1,1]\). Their complete jets agree at zero. At one,

\[
 \rho_0(1)=\operatorname{diag}(2/3,1/3),
 \qquad
 \rho_f(1)=\operatorname{diag}(7/12,5/12).
\]

Their expectations of \(E_{11}\) are \(2/3\) and \(7/12\), respectively.

### 6.4 Corollary

No reconstruction rule whose only input is the formal all-orders jet can
return the unique fixed-coupling smooth dynamics and state for every
admissible family. If such a rule existed, it would have to assign the same
output to the two equal jets above, while also reproducing two unequal
fixed-coupling families.

This no-go does not exclude a q79 completion. It proves that the completion
must use additional data, for example:

- a convergent analytic or rigorously summable class with a uniqueness
  theorem;
- a constructive regulator and controlled continuum limit;
- nonperturbative boundary, positivity, spectral, or state conditions;
- a genuinely MTT-selected geometric completion rule.

## 7. Two honest nonperturbative routes

### 7.1 Dynamical local-S-matrix C*-route

Buchholz and Fredenhagen construct a fixed-coupling local C*-net for scalar
Lagrangians:
[Buchholz-Fredenhagen](https://arxiv.org/abs/1902.06062).
The construction has a Fermi-field extension:
[Brunetti-Duetsch-Fredenhagen-Rejzner](https://arxiv.org/abs/2103.05740).

What is not imported is a nonabelian gauge-BRST physical C*-descent for the
full chiral SM together with a selected suitable physical state.

### 7.2 Lattice gauge C*-route

An infinite-lattice QCD C*-algebra with Gauss-law observables and descended
dynamics exists:
[Grundling-Rudolph](https://arxiv.org/abs/1512.06319).

What is not imported is:

- an MTT-selected regulator for the complete chiral electroweak-Higgs theory;
- a controlled continuum limit;
- equivalence of that limit to the q79 continuum branch.

These are two distinct exits. Neither can be replaced by evaluating the
formal series at a numerical coupling.

## 8. Parameter and claim ledger

New physical continuous parameters: `0`.

New physical discrete selectors: `0`.

New fits or observed inputs: `0`.

The coordinate \(\lambda\) is the existing formal interaction coordinate.
It is fixed to zero for the free reference net. The choice of one gauge
Hadamard base covariance labels an implementable folium; it is not an
MTT-selected vacuum and is not counted as an action parameter.

Closed:

- free q79 physical C*-field and observable nets;
- literal free GNS and local von Neumann closures;
- local quasiequivalence on the declared Hadamard folia;
- exact all-orders nonuniqueness of formal-to-fixed-coupling promotion.

Open:

- comparison of inequivalent gauge Hadamard orbits;
- interacting nonabelian gauge-BRST C*-completion;
- literal interacting local quasiequivalence;
- one selected global q79 state;
- selected RG matching, observable comparison, and nonperturbative
  completion.

## 9. Frontier delta

Before this packet, literal local quasiequivalence was not well typed because
no C*-net, GNS representation, or local von Neumann algebra had been
constructed in the q79 SM chain.

After this packet, those objects exist and local quasiequivalence is proved at
the exact free reference tier on a nontrivial declared Hadamard class. The
remaining interacting obstruction is no longer merely "find a completion":
formal data alone are proved insufficient, and the missing information is
isolated to a nonperturbative selection bridge.
