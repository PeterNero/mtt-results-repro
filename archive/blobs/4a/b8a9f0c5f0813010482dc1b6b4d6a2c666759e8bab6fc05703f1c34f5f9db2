# q79 Standard-Model Local Formal Physical State-Space Compatibility and Gluing Theorem v1

## Status

This theorem is proved on the declared local formal perturbative tier.

It closes the compatibility question left by
`q79_SM_Local_Formal_BRST_Physical_State_and_Positivity_Theorem_v1` in the
strongest form that quantum-state geometry permits:

1. the local formal physical state spaces form a nonempty contravariant
   state-space functor;
2. any finite collection of admissible regions contained in one admissible
   parent has a compatible family obtained by restricting one parent state;
3. arbitrary independently chosen states that agree on overlaps need not
   glue, and an exact Bell-pair witness proves this obstruction.

The theorem does not select a preferred state, construct a single state on
the full noncompact q79 branch, prove interacting local quasi-equivalence, or
complete the theory at fixed nonzero couplings.

## 1. Imported results

The theorem uses the following already certified local results.

1. On every bounded causally complete q79 region
   \[
   O=D(U),\qquad \overline U\ \text{compact},\qquad H^1(U;\mathbb R)=0,
   \]
   the gauge-fixed free BV complex is Green hyperbolic and its microcausal
   algebra is defined.
2. Renormalized Epstein-Glaser products satisfy locality and background
   covariance on the selected q79 background category.
3. The exact local anomaly vector is zero, the faithful-\(\mathbb Z_6\)
   global obstruction is zero, and a compatible all-orders formal QME
   prescription exists.
4. The interacting quantum BRST operator \(\widehat s_O\) is nilpotent.
5. The physical local algebra is
   \[
   \mathcal A_{\mathrm{phys}}(O)
   =
   H^0\!\left(\widehat s_O,\mathcal A_{\mathrm{int}}(O)\right).
   \]
6. The exact free quartet has positive ghost-number-zero cohomology, and
   deformation stability gives a nonempty family of normalized formal
   positive states on \(\mathcal A_{\mathrm{phys}}(O)\).

No measured value, fitted coupling, new physical parameter, preferred
Hadamard seed, or global vacuum is imported.

## 2. The admissible chart category

Define \(\mathsf{q79Chart}_0\) as follows.

### Objects

An object is a region \(O=D(U)\) in the bounded \(H^1=0\) q79 chart basis used
by the preceding positivity theorem, equipped with:

- the selected Lorentzian q79 background restricted to \(O\);
- its orientation and chosen spin lift;
- the faithful \((SU(3)\times SU(2)\times U(1))/\mathbb Z_6\) bundle data;
- the local gauge trivialization;
- the declared compatible auxiliary boundary and cutoff data; and
- the fixed locally covariant renormalization prescription.

For a finite cover used below, every retained nonempty intersection, or each
of its connected components, is required to remain in this basis.

### Morphisms

A morphism
\[
\psi:O\longrightarrow O'
\]
is a causally convex embedding that preserves the background, orientation,
spin lift, faithful bundle data, renormalization prescription and compatible
auxiliary data. The induced map
\[
\alpha_\psi:
\mathcal A_{\mathrm{int}}(O)
\longrightarrow
\mathcal A_{\mathrm{int}}(O')
\]
is a continuous unital star homomorphism on the declared microcausal
topology. The theorem does not require its induced map on physical
cohomology to be injective.

Local covariance of the QME prescription gives the intertwining identity
\[
\alpha_\psi\circ\widehat s_O
=
\widehat s_{O'}\circ\alpha_\psi.
\tag{2.1}
\]
Therefore \(\alpha_\psi\) descends to a unital star homomorphism on
ghost-number-zero physical cohomology, also denoted by \(\alpha_\psi\).

This is a selected-background category. It is not a claim that the same MTT
theory has already been constructed on every globally hyperbolic spacetime.

## 3. The local formal physical state spaces

Let \(\mathbb C[[\lambda,\hbar]]\) denote the declared formal perturbative
coefficient ring. For each \(O\), define
\(\mathcal S_{\mathrm{form}}(O)\) to be the set of functionals
\[
\omega_O:\mathcal A_{\mathrm{phys}}(O)
\longrightarrow
\mathbb C[[\lambda,\hbar]]
\]
with the following properties:

1. \(\omega_O(1)=1\);
2. \(\omega_O(A^*)=\overline{\omega_O(A)}\);
3. \(\omega_O(A^*A)\) is formally positive in the square-cone sense used by
   the preceding BRST deformation theorem;
4. \(\omega_O\) is continuous in the local microcausal topology; and
5. its free gauge-Higgs-Weyl restrictions are in the declared compatible
   Hadamard/microlocal class.

The prior local physical-state theorem proves
\[
\mathcal S_{\mathrm{form}}(O)\ne\varnothing
\tag{3.1}
\]
for every object \(O\).

Hollands-Ruan characterizes continuous states on the scalar perturbative
Wick algebra by a Hadamard two-point function and smooth higher truncated
functions. Here that result is used only as structural support for the
continuity and microlocal state-space condition. It is not promoted into a
standalone theorem for the full Standard-Model gauge-BRST system. The latter
uses the already certified Hollands and Duetsch-Fredenhagen gauge-BRST
construction.

## 4. Restriction theorem

For a morphism \(\psi:O\to O'\), define
\[
\alpha_\psi^*:
\mathcal S_{\mathrm{form}}(O')
\longrightarrow
\mathcal S_{\mathrm{form}}(O),
\qquad
\alpha_\psi^*(\omega')
=
\omega'\circ\alpha_\psi.
\tag{4.1}
\]

### Lemma 4.1: normalization

Because \(\alpha_\psi\) is unital,
\[
\alpha_\psi^*(\omega')(1)
=
\omega'(\alpha_\psi(1))
=
\omega'(1)
=1.
\tag{4.2}
\]

### Lemma 4.2: formal positivity

For every \(A\in\mathcal A_{\mathrm{phys}}(O)\),
\[
\alpha_\psi^*(\omega')(A^*A)
=
\omega'\!\left(
\alpha_\psi(A)^*\alpha_\psi(A)
\right).
\tag{4.3}
\]
The right side is formally positive. Hence restriction preserves the formal
positive cone.

### Lemma 4.3: physical BRST descent

Equation (2.1) sends closed elements to closed elements and exact elements to
exact elements. Thus (4.1) depends only on the physical cohomology class.

### Lemma 4.4: microlocal admissibility

Hadamard and microlocal wavefront conditions are local and are preserved
under the admitted causally convex embeddings. Continuity is preserved by
composition with the continuous algebra map. Therefore
\[
\alpha_\psi^*(\omega')\in\mathcal S_{\mathrm{form}}(O).
\tag{4.4}
\]

### Lemma 4.5: functor identities

For composable morphisms
\[
O\xrightarrow{\psi}O'\xrightarrow{\chi}O'',
\]
covariance of the algebra maps gives
\[
\alpha_{\chi\circ\psi}
=
\alpha_\chi\circ\alpha_\psi.
\]
Consequently,
\[
\alpha_{\chi\circ\psi}^*
=
\alpha_\psi^*\circ\alpha_\chi^*.
\tag{4.5}
\]
The identity embedding gives the identity restriction.

### Theorem 4.6

The assignment
\[
O\longmapsto\mathcal S_{\mathrm{form}}(O),
\qquad
\psi\longmapsto\alpha_\psi^*
\tag{4.6}
\]
is a nonempty contravariant state-space functor on
\(\mathsf{q79Chart}_0\).

This is the formal physical analogue of the Brunetti-Fredenhagen-Verch
state-space functor. The physical algebra is covariant; its state space is
contravariant.

## 5. Common-parent finite compatibility

Let \(O_1,\ldots,O_n\) be finitely many objects with admissible embeddings
\[
\iota_i:O_i\longrightarrow\widetilde O
\]
into one object \(\widetilde O\). Choose any
\(\widetilde\omega\in\mathcal S_{\mathrm{form}}(\widetilde O)\), whose
existence follows from (3.1), and set
\[
\omega_i=\alpha_{\iota_i}^*(\widetilde\omega).
\tag{5.1}
\]

For every retained intersection \(O_{ij}=O_i\cap O_j\), functoriality gives
\[
\omega_i|_{O_{ij}}
=
\widetilde\omega\circ
\alpha_{\iota_i}\circ\alpha_{ij,i}
=
\widetilde\omega\circ\alpha_{ij}
=
\widetilde\omega\circ
\alpha_{\iota_j}\circ\alpha_{ij,j}
=
\omega_j|_{O_{ij}}.
\tag{5.2}
\]

### Theorem 5.1

Every finite admissible family with one admissible common parent has at
least one exactly compatible formal physical state family.

This is a genuine existence and compatibility theorem. It does not assert
that arbitrary independently selected local states extend to a common
parent.

## 6. Exact common-parent witness

The executable certificate represents a common parent by three qubits
\(A,B,C\). Let
\[
\rho_{ABC}
=
|\mathrm{GHZ}\rangle\langle\mathrm{GHZ}|,
\qquad
|\mathrm{GHZ}\rangle
=
\frac{|000\rangle+|111\rangle}{\sqrt2}.
\tag{6.1}
\]
Its density matrix is rational:
\[
\rho_{ABC}
=
\frac12
\left(
|000\rangle\langle000|
+|000\rangle\langle111|
+|111\rangle\langle000|
+|111\rangle\langle111|
\right).
\tag{6.2}
\]

The verifier checks exactly that:

- \(\rho_{ABC}^2=\rho_{ABC}\);
- \(\operatorname{rank}\rho_{ABC}=1\);
- \(\operatorname{tr}\rho_{ABC}=1\);
- \(\rho_{AB}=\operatorname{tr}_C\rho_{ABC}\) and
  \(\rho_{BC}=\operatorname{tr}_A\rho_{ABC}\) are positive and normalized;
- both restriction paths to \(B\) agree with direct restriction:
  \[
  \operatorname{tr}_A\rho_{AB}
  =
  \operatorname{tr}_C\rho_{BC}
  =
  \operatorname{tr}_{AC}\rho_{ABC}
  =
  \frac12I_2.
  \tag{6.3}
  \]

All entries are exact rational numbers.

## 7. Why arbitrary state gluing is impossible

A presheaf restriction law does not make quantum states a sheaf. This is not
an unfinished technicality; it fails in finite-dimensional quantum theory.

Let
\[
\rho_{AB}=|\Phi^+\rangle\langle\Phi^+|,
\qquad
\rho_{BC}=|\Phi^+\rangle\langle\Phi^+|,
\qquad
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
\tag{7.1}
\]
Both overlap marginals are
\[
\operatorname{tr}_A\rho_{AB}
=
\operatorname{tr}_C\rho_{BC}
=
\frac12 I_B.
\tag{7.2}
\]
Thus the two states agree exactly on the overlap algebra of \(B\).

### Lemma 7.1: rank-one marginal factorization

If a positive density matrix \(\rho_{ABC}\) has rank-one marginal
\(\rho_{AB}=|\Phi^+\rangle\langle\Phi^+|\), positivity forces its support into
\[
\operatorname{span}\{|\Phi^+\rangle\}_{AB}\otimes\mathcal H_C.
\]
Therefore
\[
\rho_{ABC}
=
\rho_{AB}\otimes\rho_C
\tag{7.3}
\]
for some density matrix \(\rho_C\).

### Contradiction

Equation (7.3) forces
\[
\rho_{BC}
=
\frac12I_B\otimes\rho_C.
\tag{7.4}
\]
Let \(X\) be the Pauli \(X\) matrix. Every state of the form (7.4) satisfies
\[
\operatorname{tr}\!\left[
\rho_{BC}(X_B\otimes X_C)
\right]
=
\operatorname{tr}\!\left[\frac12I_BX_B\right]
\operatorname{tr}[\rho_CX_C]
=0.
\tag{7.5}
\]
But the Bell state required in (7.1) satisfies
\[
\operatorname{tr}\!\left[
|\Phi^+\rangle\langle\Phi^+|
(X_B\otimes X_C)
\right]
=1.
\tag{7.6}
\]
This contradiction proves that no \(\rho_{ABC}\) has both requested
marginals.

### Theorem 7.2

Agreement of arbitrary local quantum states on overlap algebras is
insufficient for global gluing.

The obstruction is exact, finite-dimensional and independent of infrared,
renormalization or MTT-specific assumptions. It is the quantum marginal
problem in its simplest monogamy form.

## 8. Preferred-state boundary

A compatible state-space functor is not a natural choice of one state.
Selecting a family
\[
O\longmapsto\omega_O
\]
that is invariant under every admissible embedding would be a much stronger
claim. The Fewster-Verch natural-state no-go shows that dynamically local
theories under standard assumptions do not admit a generally covariant
preferred state across all spacetimes.

The present theorem respects that boundary:

- it constructs nonempty sets of states;
- it proves exact restriction maps between those sets;
- it constructs compatible families by choosing a parent state; but
- it does not select one parent state or one cosmological state.

The selected q79 background category is narrower than the universal category
in the no-go theorem, so the no-go is a guard rather than a proof that no
special q79 global state can ever exist. Such a state would require a separate
same-source selection theorem.

## 9. Local quasi-equivalence boundary

Free quasifree Hadamard state spaces have strong local quasi-equivalence
results. Hollands-Ruan explicitly treats the corresponding general
interacting-state statement as a conjectural extension in its scalar
setting. This packet therefore does not claim that every pair of interacting
formal physical q79 states has locally equivalent GNS folia.

The closed object is a state-space functor. An interacting local-folium or
local-quasi-equivalence theorem remains a separate target.

## 10. Parameter ledger

\[
\begin{array}{c|c}
\text{new physical continuous parameters} & 0\\
\text{new physical discrete selectors} & 0\\
\text{new fits} & 0\\
\text{new observed inputs} & 0
\end{array}
\]

The selected common-parent state is state data, not an action parameter and
not a preferred-state theorem.

## 11. Final theorem

On \(\mathsf{q79Chart}_0\):

1. the formal interacting physical observable algebras form a covariant
   functor;
2. their normalized continuous formal positive Hadamard-admissible state
   spaces form a nonempty contravariant functor;
3. restriction preserves normalization, formal positivity, microlocal
   admissibility and physical BRST cohomology;
4. every finite family contained in one admissible parent has an exactly
   compatible restriction family;
5. arbitrary overlap-agreeing local states do not admit a general gluing
   theorem, as proved by the exact Bell-pair obstruction.

Therefore the former local-compatibility gap is closed at the correct
state-space-functor and common-parent tier. The remaining state targets are:

- a selected global q79 state, if one exists;
- interacting local quasi-equivalence;
- a fixed-coupling Hilbert completion;
- numerical RG, matching, uncertainty and observable comparison;
- infrared and nonperturbative completion; and
- strict upper-MTT action and state selection.

## 12. Executable certificate

The exact certificate is generated by:

```text
python scripts/verify.py
```

and written to:

```text
certificates/q79_sm_local_formal_state_space_gluing.certificate.json
```

It checks the common-parent partial traces and the Bell no-gluing
contradiction over exact rational arithmetic.

## References

- R. Brunetti, K. Fredenhagen and R. Verch, *The generally covariant
  locality principle -- A new paradigm for local quantum physics*,
  arXiv:math-ph/0112041.
- S. Hollands and W. Ruan, *The State Space of Perturbative Quantum Field
  Theory in Curved Spacetimes*, arXiv:gr-qc/0108032.
- S. Hollands, *Renormalized Quantum Yang-Mills Fields in Curved
  Spacetime*, arXiv:0705.3340.
- M. Duetsch and K. Fredenhagen, *Deformation stability of
  BRST-quantization*, arXiv:hep-th/9807215.
- C. J. Fewster and R. Verch, *Dynamical locality and covariance: What
  makes a physical theory the same in all spacetimes?*, arXiv:1106.4785.
