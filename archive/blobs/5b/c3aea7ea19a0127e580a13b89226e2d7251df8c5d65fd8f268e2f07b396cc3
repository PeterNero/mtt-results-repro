# Selected Qa/SU3 Projector and Endomorphism Pathways

## Purpose

The compact Nil scalar determinant gives a stable near miss for the Qa/SU3
block.  The co-closed one-form quotient then tests the most direct gauge
fluctuation source, but its natural zeta-finite candidates do not close the
remaining determinant gap.

The exact open quantity is:

```text
unweighted Qa/SU3 gap = 0.7944423933963232
lambda_12 gap         = 0.06620353278302693
```

This note evaluates the two remaining structurally legal paths:

```text
Path A: physical coherent-sector projector / harmonic norm / Jacobian
Path B: bundle curvature or Weitzenbock endomorphism in the selected gauge block
```

It is a gate artifact.  It does not select a correction by target matching.

## Corpus Constraints

The prior gauge-threshold theorem says that the selected block must state the
principal Laplace-type part, bundle representation, ghost/subtraction rule,
endomorphism or curvature term, physical quotient/projector, domain,
normalization, and spectral or heat data before numerical comparison.

The gauge finite-coherent corpus imposes the sharper rule:

```text
filter after quotienting, or filter covariantly before quotienting
```

Equivalently, the admissibility filter must act on physical gauge content and
must preserve BRST cohomology, Ward identities, and Slavnov-Taylor identities.

The Route B SU3 twistor note adds the projector-specific completion condition:
to make SU3 independent of the earlier route, one must specify the canonical
twistor/color bundle and compute the corresponding L2 harmonic norm directly on
that bundle.

## Path A: Physical Coherent-Sector Projector

A unit L2 harmonic representative is enough to define the physical massless
sector, but it does not by itself add a zeta-finite determinant contribution.
An idempotent normalized projector selects a subspace.  A numerical gap appears
only if the construction supplies a nontrivial selected Jacobian, fiber norm, or
physical-measure determinant.

If this path alone closes the gap, the required projector data are:

```text
required log-Jacobian               = 0.7944423933963232
required multiplicative factor      = exp(0.7944423933963232)
factor per color dimension, if equal = exp(0.7944423933963232 / 3)
```

These are not free parameters.  They must be computed from the canonical
twistor/color bundle or from a selected physical quotient measure.

## Path B: Weitzenbock / Curvature Endomorphism

The legal operator form is:

```text
D_Qa = -(connection Laplacian on physical SU3 gauge content) + E_Qa
```

where `E_Qa` is not an adjustable mass term.  It must be the endomorphism forced
by the selected SU3 bundle, connection, representation, quotient, and ghost
subtraction.

If this path alone closes the gap, the required log-determinant response is:

```text
Delta logdet(E_Qa) = 0.7944423933963232
```

The corpus has curvature-as-consistency-response material, but the current
Qa/SU3 determinant proof still lacks the actual selected Weitzenbock
endomorphism.  Therefore this route is promising but open.

## Diagnostic Structural Factor Scan

The script computes several natural-looking Nil factors.  This scan is useful
because it exposes tempting near misses, but none of these values is accepted as
closure without an independent selection theorem.

Important examples:

```text
unit L2 projector alone        -> 0
best co-closed quotient        -> 0.9889753274739147
-log(c_nil), -2log(c_nil), ... -> diagnostic Nil volume-like factors
log(1 + f_struct^2)            -> diagnostic curvature-scale factor
```

The closest structural diagnostic is reported in the certificate.  It is not
promoted to a proof.

## Verdict

Both legal paths have now been separated cleanly.

Path A can close only if the canonical SU3 twistor/color bundle supplies the
required projector norm or Jacobian.

Path B can close only if the selected SU3 physical gauge block supplies a
curvature/Weitzenbock endomorphism whose determinant response is then computed.

The next proof artifact is:

```text
Selected_Qa_SU3_Canonical_Twistor_Bundle_Projector_or_Weitzenbock_E_Term_v1
```

