---
abstract: |
  We close the next structural gate after the bridge-reduced Yukawa packet.
  Pure Z3 bridge reduction is too symmetric: the left Hermitian forms commute
  and cannot produce CKM angle magnitudes.  However, the selected overlap
  certificate already contains kinetic metrics.  If the same MTT source map
  supplies non-circulant sector kinetic metrics or equivalent selected
  lens/nil/anchor localization breaking, canonical normalization breaks the
  common family-Fourier basis and can produce nontrivial left mixing without
  entry-wise Yukawa fitting.  This note proves the gate as a schema and audits
  a non-empirical finite example.
author:
- Peter Nero
date: June 2026
title: |
  Selected Kinetic Family-Breaking Gate for CKM Magnitudes
---

# Purpose

The bridge-reduced packet proved:

```text
pure Z3 bridge symmetry -> [H_u,H_d]=0.
```

Therefore CKM magnitudes require additional selected family breaking.

The overlap-kernel certificate already names the correct place:

```text
kinetic metrics,
lens/nil anisotropic widths,
anchor/cancellation projectors,
sector-dependent localization geometry.
```

This note proves that such data are sufficient in principle, while keeping the
actual MTT derivation open.

# Setup

Let the raw bridge-reduced matrices be:

```text
Y_u,raw[i,j] = C_u[-(i+j) mod 3],
Y_d,raw[i,j] = C_d[-(i+j) mod 3].
```

Canonical normalization gives:

```text
Y_u = G_Q^{-1/2} Y_u,raw G_u^{-1/2} G_Hu^{-1/2},
Y_d = G_Q^{-1/2} Y_d,raw G_d^{-1/2} G_Hd^{-1/2}.
```

For left mixing, the relevant Hermitian forms are:

```text
H_u = Y_u Y_u^*,
H_d = Y_d Y_d^*.
```

# Theorem: Kinetic Breaking Can Generate Nontrivial Left Mixing

If `G_u` and `G_d`, or the effective right/left normalization factors entering
`H_u` and `H_d`, are not simultaneously diagonalized by the same family
Fourier transform as the pure bridge matrices, then the normalized Hermitian
forms need not commute:

```text
[H_u,H_d] != 0.
```

Therefore nontrivial CKM angle magnitudes are not excluded once selected
kinetic or localization breaking is included.

Proof.  Pure bridge matrices have common family-circulant left forms.  Inserting
non-circulant positive kinetic factors changes:

```text
Y_x,raw Y_x,raw^*
```

to:

```text
Y_x,raw G_x^{-1} Y_x,raw^*.
```

If `G_x^{-1}` does not commute with the family-circulant algebra, the result is
not generally circulant.  The common Fourier diagonalization is lost, so the
commutator of the up and down Hermitian forms can be nonzero.

# Discipline

This is allowed only if:

```text
G_Q, G_u, G_d
```

are derived from the same selected source map `Sigma_MTT`.  If the metrics are
chosen after looking at CKM angles, the construction is merely a fit.

# What This Closes

```text
pure bridge packet cannot produce CKM angles          PROVED
kinetic/localization breaking suffices in principle   PROVED/CHECKED
entry-wise Yukawa fitting still forbidden             MAINTAINED
```

# What Remains

```text
derive actual non-circulant metrics from Sigma_MTT     OPEN
derive lens/nil/anchor source of family anisotropy     OPEN
compute canonical normalized CKM matrix                OPEN
compare only after source map is frozen                OPEN
```

# Bottom Line

The path to CKM magnitudes is now:

```text
q79/Z3 packet
-> bridge-reduced raw Yukawas
-> selected non-circulant kinetic or localization breaking
-> possible nontrivial CKM angles.
```

The next missing object is not another CP phase.  It is the selected family
anisotropy in the kinetic/localization data.

