# MTT q79 Height-Four Asymmetric Precision Budget Lemma (A382B) v1

Write the certified target Hessian as

\[
H_d=H_d^{\mathrm{main}}+H_d^{\mathrm{tail}}.
\]

The A382 splice constructs every full-entry radius directly as the sum of the
corresponding nonnegative main and tail radii. Its recorded product-box
Frobenius radius is therefore the controlling certified norm for the complete
target. Requiring each component norm to use at most one half of the target
budget is sufficient, but it is not necessary.

Consequently, a target is accepted exactly when both component certificates
and their authorities are current, the A382 packet hashes those exact
components, and the recorded full product-box Frobenius radius is no larger
than

\[
B_d=\frac{0.6}{76\left(|c_d|+3\,\mathbf 1_{d=65}\right)}.
\]

The global triangle estimate is unchanged:

\[
\sum_d \left(|c_d|+3\,\mathbf 1_{d=65}\right)
\operatorname{rad}_F(H_d)\le 0.6.
\]

Thus asymmetric main/tail allocations do not weaken the A384 input bound.
They remove only an artificial bookkeeping restriction. Target `d074` is the
first concrete witness: its main radius exceeds `B_d/2`, while its independently
spliced full radius is below `B_d`.

For unfinished targets, the execution queue may therefore assign the main run
the remaining certified allowance `B_d-r_tail` whenever a current tail packet
already exists. This changes only the adaptive stopping threshold; final
acceptance still depends exclusively on the independently spliced A382 radius.
