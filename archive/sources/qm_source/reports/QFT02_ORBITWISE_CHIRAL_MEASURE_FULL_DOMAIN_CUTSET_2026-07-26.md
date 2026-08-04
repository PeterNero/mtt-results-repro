# QFT.02 Orbitwise Chiral Measure and Full-Domain Cutset

**Date:** 2026-07-26
**Blocker:** `B.QFT.02`
**Result:** genuine frontier advance without continuum promotion

## Result

The existing q79 finite-shell, based gauge/frame orbit, anomaly-line and Ward
reduction results jointly imply an actual chiral Berezin measure on each
certified connected gapped finite-spectral presentation component with
trivial loop holonomy. The actual q79 instance is the based faithful
internal-gauge suborbit with the frame held fixed. Canonical transport along
an open frame path is not promoted to a theorem about every frame-loop
holonomy.

One unit determinant vector at a basepoint is transported along the
determinant line. Zero curvature and trivial faithful gauge-loop holonomy make
the transported section path independent. Its dual top exterior form is the
finite fermion measure.

On this domain:

```text
orbitwise measure contract:       7/7
gauge Jacobian:                   exactly 1
Jacobian norm defect:             exactly 0
Cstar reduced-product defect:     exactly 0
new physical parameters:          0
```

This is nonperturbative at finite spectral cutoff: no formal coupling
expansion is used in the measure identity.

## Exact Witness

The generated certificate checks:

- two noncommuting rational realifications of quaternionic `SU(2)`
  generators;
- determinant `+1` for eight nonabelian group words;
- an eight-term exact-zero Jacobian-defect sequence;
- rational constant-rank projector transport;
- an orthonormal transported chiral basis; and
- top-wedge Gram determinant exactly `1`.

The witness verifies the finite algebra. Faithful-SM anomaly cancellation and
determinant holonomy are supplied by the pinned q79/MLD theorem chain, not by
the `SU(2)` witness.

## What Remains

The full nonabelian chiral-measure row is still false. Its remaining work is
now a four-part full-domain extension:

```text
open  selected physical projector/connection/Hessian family
open  local measure current on quotient moduli
open  crossing-strata and disconnected-sector gluing
open  uniform cutoff locality and fixed-coupling norm control
```

The overall continuum table remains `1/9`. The Ward row remains dependent on
the full chiral-measure row, and seven independent continuum exits remain.

## Frontier Delta

Before this result, the repository had determinant-line trivializability and
canonical transport but had not assembled them into a measure.

After this result, the finite chiral measure and its exact Jacobian are closed
on the actual connected gapped q79 presentation orbit. The unresolved object
is no longer "some fermion measure." It is a selected **local full-domain
extension** transverse to that orbit, with controlled gluing and uniform
estimates.

## Next Target

The highest-value next object is the selected smooth physical q79
projector/connection/Hessian family. It is upstream of the other three rows:
without it there is no domain on which to formulate the local current,
crossing extension or uniform estimates. Once supplied, the next theorem is
the integrability/locality theorem for the determinant-line measure current.
