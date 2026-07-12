# Superset Rho-UV Cross-Encoding Gate v1

## Purpose

The remaining scale-normalization coefficient is

```text
rho_UV := C_UV^2 / delta,
s_* = (60 rho_UV)^(1/6).
```

This note tests whether `rho_UV` can be closed from another MTT/MMT encoding
instead of separately computing `C_UV` and `delta` in the heterotic branch.

## No-Knob Rule

A cross-encoding closure is allowed only if it has the form

```text
selected MTT/MMT data
-> encoding dictionary
-> rho_UV
```

It is not allowed to use

```text
observed G_N, M_Pl, H0, rho_DE, absolute f_a,
observed masses or mixings,
or fitted threshold coefficients
```

as inputs for `rho_UV`.

## Candidate A: Theta Overlap Normalization

The Theta closure corpus gives independent Route A/Route B normalizations for
leading massless gauge-sector overlaps. In particular it supplies:

```text
I_2/I_1 ~= 0.560,
I_3/I_1 ~= 0.229,
canonical twistor fiber normalization,
Route A/Route B agreement for leading nonabelian overlaps.
```

This is a strong normalization scaffold, but it does not yet compute the object
needed here. `rho_UV` compares:

```text
first omitted higher-alpha-prime curvature correction
/
selected unresolved disturbance covariance.
```

The current Theta overlap notes normalize leading massless gauge overlaps. They
do not supply either the `O(alpha'^2)` curvature correction norm or the induced
finite-memory covariance of the discarded branch modes.

Verdict:

```text
FORMULATED, NOT CLOSED.
```

## Candidate B: Superset Harmonic-Weight Ratio

The superset paper writes

```text
alpha_r^(-1)(Lambda_MTT) = K zeta_r,
```

so the ratios of `zeta_r` are intrinsic after the chosen matching scheme. The
overall normalization cancels in ratios.

This suggests a possible route:

```text
rho_UV = ||selected UV response row||^2 / ||selected disturbance row||^2
```

where both rows are expressed in the same harmonic-weight inner product. If
that construction is supplied, the common `K`-normalization cancels and the
result would be a no-knob dimensionless ratio.

But the current superset paper does not identify:

```text
UV response row,
disturbance covariance row,
or a theorem equating those rows to the heterotic C_UV and delta.
```

Verdict:

```text
BEST STRUCTURAL ROUTE, NOT CLOSED.
```

## Candidate C: Fluctuation-Dissipation / Retarded-Kernel Route

The white-noise paper proves that white noise is the zero-memory limit of a
finite-memory disturbance kernel. The exact Z64 branch supplies a retarded
kernel:

```text
K_ret,64 = S^-1.
```

A closure theorem of the following form would finish the ratio:

```text
selected finite-memory covariance = F(K_ret, Hess_Xi),
selected UV correction norm       = G(K_ret, Hess_Xi),
rho_UV = G^2 / F.
```

This is attractive because it would use the same branch kernel for both sides.
However, the current corpus does not state the finite-memory covariance
functional `F` nor the UV correction norm functional `G`.

Verdict:

```text
PROMISING THEOREM ROUTE, NOT CLOSED.
```

## Candidate D: C1 Finite-Response Matrix Route

The C1 response theorem closes a finite-dimensional reduction:

```text
selected primitive contractions -> C1 response matrices.
```

That machinery is relevant because `C_UV` is also a selected correction norm.
One could define `C_UV` as the norm of the selected higher-order response vector
after passing through the same Hessian inverse and projector.

The current C1 corpus, however, explicitly leaves the primitive contractions
open. Therefore it cannot yet supply a numeric `rho_UV`.

Verdict:

```text
EXECUTABLE ONCE PRIMITIVES EXIST, NOT CLOSED.
```

## Bad Shortcut: Threshold Delta

The Tier-3 and Execution-I threshold papers contain a coefficient written

```text
delta = -25.2 +/- 0.5.
```

This is not the OU disturbance covariance `delta` in

```text
Var(a) = delta/(2 gamma).
```

It is a bulk threshold-profile coefficient. It has the wrong role, wrong sign,
and different source construction. Importing it into `rho_UV` would be a symbol
collision, not a derivation.

Verdict:

```text
FORBIDDEN.
```

## Cross-Encoding Conclusion

The superset route does not close `rho_UV` numerically from the present corpus.
It does something useful: it identifies the cleanest possible closure target.

The strongest next theorem is:

```text
Selected Rho-UV Response-Ratio Theorem

Given the selected branch Hessian H, retarded kernel K_ret, and finite-memory
disturbance kernel C_mem, the first omitted UV correction row U and disturbance
row D are evaluated in the same selected inner product, and

rho_UV = ||U||^2 / ||D||^2.
```

This would be a genuine superset closure because:

```text
1. the same selected branch data define both numerator and denominator;
2. common normalization cancels;
3. no physical target constant is used;
4. the result can be checked independently in heterotic, Theta, and C1 encodings.
```

## Status

```text
kappa = 1 is closed.
rho_UV is not numerically closed.
superset route is formulated and narrowed to a response-ratio theorem.
```

The next artifact should compute or define the shared primitive pair:

```text
U = selected O(alpha'^2) UV response row,
D = selected finite-memory disturbance covariance row.
```

Once those two rows are source-certified, the remaining ratio is executable.
