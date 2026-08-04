# Fixed-Point Damping Capture-Clock No-Go

## Question

Does the exact normalized fixed-point semigroup itself provide the exponential
capture clock needed by the Quadratic-Hazard First-Capture Theorem?

## Calculation

On the finite q79 carrier,

\[
S_t=P_{\rm Haar}+e^{-t}Q.
\]

For the first basis vector, whose coherent and strain weights are `1/3` and
`2/3`, the squared surviving norm is

\[
s(t)=1/3+(2/3)e^{-2t}.
\]

Choose `t` so that `e^{-2t}=1/2`. Then

\[
s(t)=2/3,
\qquad
s(2t)=1/2,
\qquad
s(t)^2=4/9.
\]

Hence `s(2t) != s(t)^2`: the survival law is not memoryless and is not the
normalized competing-exponential clock assumed by the constructive hazard
theorem.

## Positive Residue

The asymptotic split is nevertheless exact:

\[
\lim_{t\to\infty}s(t)=1/3,
\qquad
1-\lim_{t\to\infty}s(t)=2/3.
\]

Thus fixed-point damping contains the canonical `P/Q` response values as
surviving and lost norm. What it does not supply is a probability law saying
that norm loss is an individual capture event, or a second outcome clock for
the coherent component.

## Consequence

Free stabilization selects response geometry but not measurement dynamics. A
physical apparatus coupling must convert the `P/Q` quadratic responses into a
marked jump process, an instrument, or another source-derived capture law.
Interpreting squared norm directly as probability would simply assume the step
being derived.
