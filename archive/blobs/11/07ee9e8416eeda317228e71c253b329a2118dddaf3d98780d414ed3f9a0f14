# Post-Invariant Obstruction Way Forward for Iwasawa SM Closure

## Purpose

The recent Iwasawa audits close a tempting shortcut:

```text
literal printed A^(0,1): not integrable,
one-index repair: integrable but h1=2,
three-entry torsion-support invariant ansatz: integrable branches all have h1=2,
closed-form h1=3 sparse branches: not selected and drop e3.
```

Therefore the way forward is not another sparse invariant connection guess.
The proof must now construct the selected cohomology data by a stronger method.

## Decision

The primary path is:

```text
typed monad sections -> finite Cech/Dolbeault monad cohomology -> H^1(X,E)
```

The fallback path is:

```text
selected non-invariant HYM/Strominger spectral Galerkin computation
```

The corrected-A01 path remains open only if a corrected selected connection is
supplied from the source theory.  The finite invariant scans cannot select it.

## Primary Route: Monad/Cech Cohomology

The source monad is

```text
0 -> K1 -> B := direct_sum_i L_i -> K2 -> 0,
E = ker(g) / im(f).
```

The missing data are the typed maps

```text
f_i in H^0(X, L_i tensor K1^{-1}),
g_i in H^0(X, K2 tensor L_i^{-1}).
```

Once those are supplied, split the monad into two short exact sequences:

```text
0 -> K := ker(g) -> B -> K2 -> 0,
0 -> K1 -> K -> E -> 0.
```

Then compute the induced long exact cohomology maps.  The required output is:

```text
h^0(E), h^1(E), h^2(E), h^3(E),
anti-family middle cohomology,
three selected representatives Psi_1,Psi_2,Psi_3,
Yoneda/cup product for the E6 cubic,
sector projection maps into Q,u,d,L,e,N,H.
```

This route is the best one because it directly answers the gap between
`int c3(E)=6` and actual family representatives.  It also gives exact symbolic
support data for Yukawa entries before physical normalization.

## Fallback Route: Non-Invariant Spectral Galerkin

If the typed monad sections cannot be recovered from the corpus or corrected
source, move to a controlled spectral calculation:

```text
choose the selected HYM/Strominger operator D_E,
build a finite basis beyond left-invariant forms,
compute the low spectrum and Riesz projector,
verify exactly three family zero modes and anti-family vanishing,
bound the complement gap and truncation error,
compute G, dotD_alpha1, and horizontal responses.
```

This route is more numerical, but it matches the existing C1 response
interface.  It also naturally admits non-invariant family modes, which the
corpus already leaves open as a retained channel.

## Why This Is Credible

The path is credible because it removes all proxy knobs:

```text
no benchmark Yukawa entries,
no observed masses or mixings as inputs,
no silent A01 repair,
no use of c3 index as a zero-mode basis,
no free dotD.
```

The selected data must produce the representatives, metrics, projectors,
Green operators, and response blocks before any comparison with observed SM
data.

## Success Criterion

The next proof step is successful only if it produces a certificate with:

```text
selected integrable bundle/sheaf data,
typed maps f,g or selected D_E,
g o f = 0 if using monad,
exactness/local-freeness or controlled sheaf substitute,
h^1(E)=3,
anti-family middle cohomology = 0,
explicit Psi_i representatives,
L2 metric and projector data,
sector maps Q,u,d,L,e,N,H,
dotD_alpha1 and reduced Green operators.
```

Only then can the existing primitive C1 response calculator be fed honest
inputs.

## Practical Next Artifact

Create:

```text
Iwasawa_Selected_Cohomology_Data_Certificate
```

with two mutually exclusive completion modes:

```text
mode = "typed_monad_cech"
mode = "non_invariant_spectral_galerkin"
```

The certificate should be allowed to remain `OPEN` until the actual maps or
operator data are supplied, but its schema should be strict enough that a
future pass can be audited mechanically.

## Verdict

The way forward is now clear:

```text
stop trying to repair the sparse invariant A01;
build the selected cohomology by typed monad/Cech methods;
fall back to non-invariant spectral Galerkin only if monad sections are absent;
then feed the resulting zero modes into the dotD/C1 response interface.
```

This is the shortest route that can still reach full SM matrix closure without
losing rigor.
