# Canonical q79 Hessian-Square-Root to Minimal Recorder Source Theorem

Date: 2026-07-23

Status:
`Q79_HESSIAN_RESIDUAL_AND_SPECTRAL_RECORDER_SOURCE_EXACT_CONTEXT_AND_ACTUALIZATION_OPEN`

## Result

The accepted finite q79 action already selects more of the recorder than the
previous `A_rec` packaging made visible. It canonically emits:

1. a linear closure-defect residual;
2. its Gram operator \(Q=I-P_{\rm Haar}\);
3. the unique positive square-root defect amplitude \(Q\);
4. the binary spectral projectors \(P_{\rm Haar}\) and \(Q\); and
5. the minimal ideal \(P/Q\) record isometry.

Thus `A_rec` is not needed as a new universal MTT axiom for a declared
apparatus whose physical purpose is to read this q79 closure defect. It can be
reclassified as an apparatus-context and calibration contract.

This does not derive that such an apparatus is physically present, its
dimensional rate, or the realized-outcome law. The Hessian also does not by
itself force equal sector rates. Equal rates follow exactly if the declared
capture clock is required to be preparation blind.

## 1. Selected Finite Action

Let the selected real root-stack symbol be
\[
W_{\rm fin}^{\mathbb R}=\mathbb R^3_D\oplus\mathbb R^3_E
\]
carry the diagonal permutation representation \(\rho\) of \(G=S_3\). The
shared differential line extends this action complex-linearly to the
fiberwise complex-six quantum carrier. All identities below hold first on the
real symbol and then on that complexification. The accepted finite q79
closure-defect action, with \(\kappa_{\rm fin}>0\), is
\[
S_{\rm fin}(w)
=\frac{\kappa_{\rm fin}}{4|G|}
  \sum_{g\in G}\|(I-\rho(g))w\|^2.
\]
Define the normalized residual map
\[
\mathcal D_{\rm fin}:W_{\rm fin}\longrightarrow
\bigoplus_{g\in G}W_{\rm fin},
\qquad
\mathcal D_{\rm fin}w
=\frac1{\sqrt{2|G|}}
 \bigl((I-\rho(g))w\bigr)_{g\in G}.
\]
Then
\[
S_{\rm fin}(w)
=\frac{\kappa_{\rm fin}}2\|\mathcal D_{\rm fin}w\|^2.
\]

### Theorem 1: exact residual Gram

Writing
\[
P=P_{\rm Haar}=\frac1{|G|}\sum_{g\in G}\rho(g),
\qquad Q=I-P,
\]
one has
\[
\mathcal D_{\rm fin}^{*}\mathcal D_{\rm fin}=Q.
\]

### Proof

Every \(\rho(g)\) is unitary and \(G\) is closed under inversion. Hence
\[
\begin{aligned}
\sum_g(I-\rho(g))^*(I-\rho(g))
&=\sum_g\left(2I-\rho(g)-\rho(g)^*\right)\\
&=2|G|I-2\sum_g\rho(g)\\
&=2|G|(I-P).
\end{aligned}
\]
Multiplication by \(1/(2|G|)\) proves the identity. Consequently
\[
\operatorname{Hess}S_{\rm fin}
=\kappa_{\rm fin}\mathcal D_{\rm fin}^*\mathcal D_{\rm fin}
=\kappa_{\rm fin}Q,
\]
exactly matching the accepted q79 Hessian.

The same calculation gives
\[
\mathcal D_{\rm fin}P=0,
\qquad
\mathcal D_{\rm fin}Q=\mathcal D_{\rm fin},
\qquad
\operatorname{rank}\mathcal D_{\rm fin}=4.
\]

## 2. Positive Square Root and Minimal Defect Amplitude

Because \(Q=Q^*=Q^2\), its spectrum is contained in \(\{0,1\}\). Therefore
\[
H_{\rm fin}^{1/2}=\sqrt{\kappa_{\rm fin}}\,Q
\]
is the unique positive square root of \(H_{\rm fin}\).

The polar decomposition of the residual is
\[
\mathcal D_{\rm fin}=VQ,
\]
where \(V\) is an isometry from \(\operatorname{Ran}Q\) into the residual
codomain. If \(B^*B=Q\) and \(B\) has minimal support, polar decomposition gives
\[
B=UQ
\]
for an isometry \(U\) on \(\operatorname{Ran}Q\). Thus every minimal amplitude
with the action-selected Gram differs only by an output isometry. There is no
relative dimensionless response coefficient to fit.

The spectral projectors are recovered from the same Hessian:
\[
P=\chi_{\{0\}}(H_{\rm fin}),
\qquad
Q=\chi_{(0,\infty)}(H_{\rm fin}).
\]
They are not separately guessed detector effects.

## 3. Canonical Closure-Defect Meter

Declare a physical context \(C_{\rm def}\) whose apparatus interrogates the
q79 closure residual, is nondemolition on the \(P/Q\) sectors, and has one
ready state and one defect record. The preceding theorem fixes the system
amplitude to \(Q\), up to output-record phase gauge.

For \(c^2+s^2=1\), the minimal ready-to-defect isometry is
\[
V_{c,s}z
=(P+cQ)z\otimes|r\rangle
+sQz\otimes|d\rangle.
\]
Indeed,
\[
(P+cQ)^*(P+cQ)+(sQ)^*(sQ)=P+(c^2+s^2)Q=I.
\]
It is generated on the ready subspace by
\[
H_2=\kappa_C Q\otimes Y_{rd},
\]
which is the two-state recorder obtained previously. At
\[
c=\frac7{25},
\qquad
s=\frac{24}{25},
\]
it gives the already certified q79 defect instrument exactly.

The q79 action supplies the amplitude \(Q\). The statement that an external
apparatus interrogates that amplitude is context data, just as the choice of
which observable an experiment measures is context data.

## 4. Canonical Ideal Spectral Meter

The ideal minimally disturbing record isometry for the Hessian spectrum is
\[
W_{PQ}z
=Pz\otimes|p\rangle+Qz\otimes|q\rangle.
\]
It is an isometry because
\[
W_{PQ}^*W_{PQ}=P+Q=I,
\]
and its two pulled-back record projectors are exactly \(P\) and \(Q\).

Under the additional ideal-meter requirements that the interaction:

1. is repeatable on each spectral sector;
2. acts trivially within each sector apart from record phase; and
3. uses the minimum number of orthogonal records,

this isometry is unique up to phases and a unitary re-encoding of the output
record basis. Two nonzero records require a two-dimensional record output. If
one orthogonal prepared ready state is retained in the same pointer, the
minimum pointer dimension is three.

To see the uniqueness, perfect record separation sends the \(P\) input sector
only to the \(p\) record block and the \(Q\) input sector only to the \(q\)
record block. Repeatability keeps their system components inside the same
sectors. Minimal disturbance makes the two restricted system maps scalar
multiples of \(P\) and \(Q\). Isometry fixes both scalar moduli to one, and
record-phase changes absorb their phases. The displayed \(W_{PQ}\) is the
remaining representative.

The common-angle ready/\(P\)/\(Q\) action from the previous theorem is a
partial-record implementation of this spectral meter:
\[
H_3=\kappa_C\left(P\otimes Y_{rp}+Q\otimes Y_{rq}\right).
\]

## 5. Preparation-Blind Clock Rigidity

The most general sector-uniform nondemolition jump pair has the form
\[
L_P=\sqrt{\gamma_P}\,P,
\qquad
L_Q=\sqrt{\gamma_Q}\,Q.
\]
For a normalized preparation \(\psi\), its total hazard is
\[
h(\psi)
=\gamma_P\|P\psi\|^2+\gamma_Q\|Q\psi\|^2.
\]

### Theorem 2: common-rate uniqueness

The total waiting-time hazard is independent of every normalized preparation
if and only if
\[
\gamma_P=\gamma_Q.
\]

### Proof

If the rates are equal to \(\gamma_C\), then
\[
h(\psi)=\gamma_C\langle\psi,(P+Q)\psi\rangle=\gamma_C.
\]
Conversely, evaluate \(h\) on one unit vector in \(\operatorname{Ran}P\) and
one in \(\operatorname{Ran}Q\). Preparation independence gives
\(\gamma_P=\gamma_Q\).

Thus a preparation-blind waiting clock forces
\[
L_P=\sqrt{\gamma_C}P,
\qquad
L_Q=\sqrt{\gamma_C}Q
\]
and removes an otherwise free relative rate. The record label then carries the
spectral information while the waiting time does not.

## 6. Exact Nonselection No-Go

The Hessian alone does not impose the preparation-blind-clock requirement.
For arbitrary angles \(\alpha,\beta\), define
\[
\begin{aligned}
K_r&=\cos\alpha\,P+\cos\beta\,Q,\\
K_P&=\sin\alpha\,P,\\
K_Q&=\sin\beta\,Q.
\end{aligned}
\]
Then
\[
K_r^*K_r+K_P^*K_P+K_Q^*K_Q=I
\]
for every \(\alpha,\beta\), including \(\alpha\ne\beta\). These are distinct
normalized nondemolition instruments built from the same Hessian projectors.

Therefore \(H_{\rm fin}\) cannot by itself:

- decide which apparatus is physically present;
- impose equal sector rates;
- select the dimensional rate \(\gamma_C\);
- select a fresh-ancilla or continuum realization; or
- actualize one record.

This no-go is why the result is a source theorem for the canonical defect
observable and its minimal record geometry, not a claim of full measurement
closure.

## 7. Classification and Parameter Ledger

The previous compact label

```text
A_rec: minimal unbiased nondemolition q79 recorder
```

is now decomposed as follows.

Selected by the accepted q79 action:

- the closure-defect residual and its Gram;
- the unique positive-square-root defect amplitude;
- the \(P/Q\) spectral projectors;
- the minimally disturbing ideal spectral record isometry.

Declared physical context:

- that this apparatus measures the q79 closure defect or its spectrum;
- its ready/record architecture and boundary conditions;
- minimal disturbance; and
- a preparation-blind waiting clock, when the common-rate capture model is
  used.

Still unsourced:

- the same-action map from a physical apparatus configuration to this
  coupling;
- the profile-dependent dimensional value of \(\gamma_C\);
- a controlled fresh-ancilla/Fock continuum realization;
- the stochastic realized-record law without importing Born weights; and
- arbitrary non-q79 apparatus contexts.

The updated ledger is

```text
new universal structural axioms for this context: 0
new universal dimensionless parameters:            0
new fitted parameters:                             0
new observed construction inputs:                  0
declared categorical apparatus contexts:           1
inherited physical context rates:                   1
```

## 8. Frontier Delta

Before this theorem, sector control, minimal records, equal response and no
bias were packaged as one candidate universal principle `A_rec`.

After this theorem, the accepted q79 sum-of-squares action itself supplies the
defect amplitude and the binary spectral record geometry. Equal sector rates
are not assumed silently: they are uniquely forced by the explicit
preparation-blind-clock condition. The remaining context choice and physical
source obligations are exposed rather than counted as a new universal law.

`B.QM.01` remains open. The theorem removes the universal recorder-axiom
interpretation for the canonical q79 context, but it does not derive the
physical system-apparatus map or the realized-outcome law required by the
blocker exit certificate.
