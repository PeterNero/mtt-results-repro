# Selected q79 stable affine-Hessian growth bound (A380R)

The affine transport error satisfies

\[
  E(h)\le e^{Lh}E(0)+A\int_0^h e^{Ls}\,ds,
  \qquad L,A,h\ge 0.
\]

The earlier runtime evaluated the second term as
`A*(exp(L*h)-1)/L`. That formula is analytic at `L=0`, but literal interval
division is indeterminate whenever the certified interval for `L` contains
zero. The production runtime now uses

\[
  \int_0^h e^{Ls}\,ds \le h e^{Lh},
\]

and therefore adds the rigorous majorant `A*h*exp(L*h)`. This is finite at
`L=0`, contains the exact integral for every nonnegative `L`, and introduces
no fitted or measured input. Every returned lift and output radius is also
subject to an explicit finite-value gate.

The separately hashed inclusion audit checks the zero-containing interval case
and confirms on a full selected Hessian step that the stable endpoint centers
overlap the reference centers and that its radii contain the finite reference
radius scale. This repairs an execution singularity only; it does not alter the
selected geometry, path, cycle, source, Taylor order, or A384 precision budget.
