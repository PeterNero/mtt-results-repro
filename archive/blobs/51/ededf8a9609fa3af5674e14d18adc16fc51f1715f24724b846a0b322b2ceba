# Iwasawa Diagnostic H1 Three Spectral Pipeline

## Purpose

The spectral fallback now needs a selected operator `D_E`. The corpus does not
yet provide one. However, the sparse scan found integrable `h1=3` diagnostic
candidates. We can use one of those candidates to test the finite
Hodge/Galerkin extraction machinery.

This is not a proof-source substitution. The candidate below is not selected,
is not non-invariant, and does not retain the torsion `e3` support. It is a
calibration target for the code path:

```text
valid D supplied -> build L_1 -> construct kernel projector -> extract 3 modes.
```

## Diagnostic Operator

Use the first sparse `h1=3` example:

```text
A_12 = e1,
A_13 = e1,
A_23 = e1.
```

All other entries vanish. With the Iwasawa rule

```text
dbar e1 = 0,
dbar e2 = 0,
dbar e3 = e1 wedge e2,
```

this candidate is integrable:

```text
D^2 = 0.
```

The finite invariant complex has:

```text
rank(D0) = 2,
rank(D1) = 4,
rank(D2) = 2,
(h0,h1,h2,h3) = (1,3,3,1).
```

## Hodge/Galerkin Test

On degree one, define the finite Hodge Laplacian:

```text
L_1 = D0 D0^* + D1^* D1.
```

Using the standard invariant-basis inner product, the script constructs:

```text
ker(L_1),
P_ker = N (N^T N)^(-1) N^T,
```

where `N` is an exact rational nullspace matrix.

The exact checks are:

```text
dim ker(L_1) = 3,
P_ker^2 = P_ker,
P_ker^T = P_ker,
L_1 P_ker = 0.
```

So the finite extraction machinery works: when a valid finite `D` with `h1=3`
is supplied, the pipeline recovers three harmonic representatives and an exact
projector.

## What This Does Not Prove

This does not close the MTT branch. It does not prove:

```text
the candidate is selected,
the HYM/Strominger branch supplies this D,
the non-invariant spectral truncation is controlled,
the sector projections Q,u,d,L,e,N,H are known,
dotD_alpha1 is known,
SM matrices are computed.
```

It is only a successful dry run of the finite Hodge extraction.

## Consequence

The next real move is now operationally clear:

```text
replace this diagnostic candidate by a selected D_E,
then rerun the same pipeline.
```

The selected `D_E` must still come from one of:

```text
corrected non-invariant Dolbeault data,
typed monad sections,
direct selected HYM/Strominger solve.
```

Once that happens, the pipeline can fill the spectral Galerkin data template
instead of merely proving that the machinery works.
