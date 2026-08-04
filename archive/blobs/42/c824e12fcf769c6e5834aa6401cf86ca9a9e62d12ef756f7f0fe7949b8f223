# Shared-Circle Marked-Poisson Actualization One-Primitive Theorem

Date: 2026-07-23

Status:
`SHARED_CIRCLE_MARKED_POISSON_ACTUALIZATION_EXACT_ONE_PRIMITIVE_NOT_SELECTED`

## Result

The already-derived normalized detector hazards can be promoted to objective
capture times and record labels by one explicit stochastic primitive:

```text
A_PRM: one independently scattered Poisson random measure on
       noncompact physical time x the shared mark circle.
```

The construction gives:

- exact exponential capture time;
- exact cause-specific quadratic hazards;
- an actual record-valued sample path;
- coarse-graining by union of mark arcs;
- common-rate cancellation from record probabilities; and
- SecondMomentCaptureDescent and the Born trace weights.

It uses zero numerical selectors, fits or observed probabilities. It is
stronger and more constructive than the abstract `A_Born` candidate because it
also supplies event trajectories.

It is not a zero-primitive derivation. Current MTT has not selected Poisson
independent increments, and normalized shared-circle Haar phase alone is
insufficient.

## 1. Typed Input

Fix a physical preparation \(z\) and context \(C\). Let the already selected
finite detector maps obey
\[
\sum_a M_{C,a}^*M_{C,a}=I.
\]
Define
\[
r_{C,a}(z)=\|M_{C,a}z\|^2.
\]
For normalized \(z\),
\[
r_{C,a}(z)\geq0,
\qquad
\sum_a r_{C,a}(z)=1.
\]

Let \(\gamma_C>0\) be the one dimensional physical context rate. This theorem
does not derive its value.

The temporal carrier is noncompact physical time \(\mathbb R_+\). The compact
shared circle \(S^1_{\rm shared}\) is used only as a mark and holonomy carrier,
with normalized Haar measure \(m_{\rm H}\). It is not identified with time.

## 2. One Stochastic Primitive

Adopt the candidate structural primitive:

\[
N_C(dt,du)
\quad\text{is Poisson on}\quad
\mathbb R_+\times S^1_{\rm shared}
\]
with intensity
\[
\gamma_C\,dt\otimes m_{\rm H}(du).
\]

Choose the ordering supplied by the stable physical record algebra and
partition the mark circle into disjoint measurable arcs
\[
S^1_{\rm shared}=\bigsqcup_a A_{C,a}(z),
\qquad
m_{\rm H}(A_{C,a}(z))=r_{C,a}(z).
\]
The pointer phase fixes the beginning of the first arc. Rotating all arcs by
the same phase is gauge.

Let \((T,U)\) be the first point of \(N_C\) after the apparatus coupling is
enabled. The realized record is the unique \(a\) for which
\[
U\in A_{C,a}(z).
\]

## 3. Marked-Poisson Actualization Theorem

The capture time is exponential:
\[
\Pr(T>t\mid z)=e^{-\gamma_Ct}.
\]
The restrictions of \(N_C\) to the disjoint sets
\(\mathbb R_+\times A_{C,a}(z)\) are independent Poisson processes with rates
\[
\gamma_{C,a}(z)
=\gamma_Cm_{\rm H}(A_{C,a}(z))
=\gamma_Cr_{C,a}(z).
\]
Consequently,
\[
\Pr(\text{record}=a\mid z)
=\frac{\gamma_{C,a}(z)}
       {\sum_b\gamma_{C,b}(z)}
=r_{C,a}(z)
=\|M_{C,a}z\|^2.
\]

### Proof

A Poisson random measure assigns a Poisson count with mean equal to the
intensity of each measurable set, and counts on disjoint sets are independent.
The no-point probability on
\([0,t]\times S^1_{\rm shared}\) is therefore
\[
\exp\left[-\gamma_Ct\,m_{\rm H}(S^1_{\rm shared})\right]
=e^{-\gamma_Ct}.
\]
Restriction to one mark arc multiplies the rate by its Haar length. The
standard first-arrival race of independent exponential clocks then gives the
displayed label probability.

This is also the exact marked-point-process form of the competing-clock
theorem. A common change in \(\gamma_C\) changes the waiting-time distribution
but cancels from all record labels.

The theorem is exact on finite-dimensional normalized detector families when
the preparation and hazards are fixed until the first capture, the total rate
is finite and positive, and the stable-record arcs are measurable. There is no
discretization or asymptotic error. A genuinely time-dependent preparation
requires predictable thinning with hazards emitted by the same physical
action; that extension is not claimed here.

## 4. Second-Moment Descent

Let a physical preparation protocol supply a normalized upper ensemble
\(\lambda\), and define
\[
\rho_\lambda
=\int |z\rangle\langle z|\,d\lambda(z).
\]
For
\[
E_{C,a}=M_{C,a}^*M_{C,a},
\]
the actualized record probability is
\[
\begin{aligned}
\Pr_\lambda(\text{record}=a)
&=\int r_{C,a}(z)\,d\lambda(z)\\
&=\int\langle z,E_{C,a}z\rangle\,d\lambda(z)\\
&=\operatorname{Tr}(\rho_\lambda E_{C,a}).
\end{aligned}
\]
Thus `A_PRM` implies `A_Born: SecondMomentCaptureDescent`.

The implication is strict in operational content: `A_Born` fixes the
probability functional, while `A_PRM` also gives an objective event time,
record label and complete marked counting path.

It is not stricter in the sense of requiring fewer assumptions. The clause
that assigns stochastic intensity
\(\gamma_C\|M_{C,a}z\|^2\) is the explicit quadratic-response coupling inside
`A_PRM`; marked-Poisson mathematics propagates that clause into trajectories
but does not derive it. Thus this theorem improves constructive and path-space
closure, not the zero-primitive source count.

## 5. Coarse-Graining and Gauge

If outcomes in \(B\) are combined, their mark region is
\[
A_{C,B}(z)=\bigcup_{a\in B}A_{C,a}(z).
\]
Disjoint additivity of Haar measure gives
\[
m_{\rm H}(A_{C,B}(z))
=\sum_{a\in B}r_{C,a}(z).
\]
Hence coarse-graining is automatic.

A simultaneous rotation of all arcs preserves every Haar length. Permuting
the stable record labels and their arcs together only permutes the probability
coordinates. The mark anchor and record ordering introduce no numerical
parameter.

## 6. Why Haar Phase Alone Does Not Work

Consider constant-speed traversal
\[
U_t=U_0+\omega t\pmod 1
\]
with \(U_0\) Haar distributed, and let the target arc have length \(a\), where
\(0<a<1\).

Unconditionally, the first-entry law has an atom of mass \(a\) at \(t=0\),
because the initial point may already lie in the target. Conditional on
starting outside the target, the entry time has bounded support: for unit
speed it lies in
\[
(0,1-a].
\]
A positive-rate exponential law has no atom at zero and has unbounded support.
Therefore deterministic shared-circle traversal is not the required
memoryless clock.

This also explains why a uniform phase and a threshold partition are not a
source theorem. They can replay any probability vector after it is known.
Independent Poisson increments are the additional physical content in
`A_PRM`.

## 7. Exact q79 Binary Specialization

For the first q79 carrier basis state,
\[
r_P=\langle e_1,Pe_1\rangle=\frac13,
\qquad
r_Q=\langle e_1,Qe_1\rangle=\frac23.
\]
At total rate \(\gamma_C=15\), the two restricted point processes have rates
\[
\gamma_P=5,
\qquad
\gamma_Q=10.
\]
Their first-record probabilities are exactly \(1/3\) and \(2/3\). The value
15 is only an exact rational witness here; it is not asserted as the physical
rate.

## 8. Parameter and Primitive Ledger

If `A_PRM` is adopted:

```text
new structural stochastic primitives:  1
new universal continuous parameters:   0
new discrete numerical selectors:      0
new fitted parameters:                 0
new observed construction inputs:      0
inherited physical context rates:       1
```

A realized random sample is an event, not a theory parameter.

## 9. Frontier Delta

Before this theorem, the q79 recorder action supplied exact jump operators and
quadratic hazards, but no objective law selecting one outgoing record.

After this theorem, one explicit standard stochastic primitive is proved
sufficient for:

- exact memoryless capture;
- quadratic record labels;
- realized trajectories;
- coarse-graining; and
- second-moment/Born descent.

This is a concrete one-primitive completion, not a selected-source closure.
`B.QM.01` remains open because current MTT has not derived or adopted `A_PRM`
and has not yet emitted the full same-action physical apparatus map for every
allowed context.

## External Alignment

The exponential race and channel restriction used here are the same
marked-Poisson mathematics underlying exact stochastic simulation:

- [D. T. Gillespie, A general method for numerically simulating the stochastic
  time evolution of coupled chemical reactions](https://doi.org/10.1016/0021-9991(76)90041-3)

That established mathematics does not select `A_PRM` for MTT. It only verifies
the consequences once the stochastic primitive and action-selected hazards
are supplied.
