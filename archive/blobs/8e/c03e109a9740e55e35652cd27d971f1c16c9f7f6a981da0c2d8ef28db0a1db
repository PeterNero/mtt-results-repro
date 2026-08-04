# q79 Orbitwise Finite-Spectral Chiral Measure and Full-Domain Locality Cutset Theorem v1

**Date:** 2026-07-26
**Repository:** `mtt-qm-source-proof`
**Blocker:** `B.QFT.02`
**Certificate:** `certificates/q79_orbitwise_finite_spectral_chiral_measure_cutset.certificate.json`

## Status

This theorem is **closed** on each certified connected, gapped,
anomaly-free q79 finite-spectral presentation component.

It does **not** close the full nonabelian Standard-Model chiral-measure row.
That row is reduced to a local and global extension problem on the full
admissible background domain.

## Controlling Inputs

The result composes four previously verified packages:

1. a positive finite BV-Hodge shell has a canonical Lagrangian integration
   cycle and an exact free finite-shell QME pushforward;
2. the actual boundary-identity based q79 gauge/frame orbit has constant
   spectral rank, zero APS flow, zero BFV flux and canonical determinant-line
   transport;
3. the faithful q79 Standard-Model determinant line has zero certified local
   curvature obstruction and zero faithful gauge-loop obstruction; and
4. the compact-gauge and ghost-number-zero BRST observable defects are
   exactly zero, so the remaining physical Ward functional is the
   fermion-measure Jacobian.

The local and global anomaly statements are supplied by the pinned q79/MLD
sources. The finite matrix witness below is not substituted for them.

For the actual q79 application of the path-independence lemma, \(B_0\) is the
based faithful **internal-gauge suborbit**, with the frame held fixed. The
larger certificate also gives canonical transport along liftable frame paths,
but open-path transport is not by itself a proof of trivial holonomy around
every frame or diffeomorphism loop.

## Lemma: Parallel Unit Section

Let \(L\to B_0\) be a Hermitian line bundle over a connected component.
Suppose:

1. every admitted path \(\gamma\) has unitary parallel transport
   \(T_\gamma\);
2. transport is functorial under path concatenation and reversal; and
3. the holonomy of every admitted loop in \(B_0\) is the identity.

Choose a basepoint \(b_0\in B_0\) and a unit vector
\(s_0\in L_{b_0}\). For \(b\in B_0\), choose a path from \(b_0\) to \(b\)
and define

\[
s(b)=T_\gamma s_0.
\]

If \(\gamma'\) is another such path, then following \(\gamma\) and returning
along \(\gamma'\) is a loop. Functoriality and trivial holonomy give

\[
T_{\gamma'}^{-1}T_\gamma=1,
\qquad\text{hence}\qquad
T_\gamma=T_{\gamma'}.
\]

Hence \(s\) is path independent. Unitarity makes it a unit section, and its
definition makes it parallel.

Any second basepoint unit vector has the form \(u s_0\) for one constant
\(u\in U(1)\). Its transported section is therefore \(u s\). The possible
unit sections form a \(U(1)\) torsor, not a canonically pointed set.

## Theorem: Orbitwise Chiral Berezin Measure

Let \(B_0\) be one certified connected q79 presentation component on which:

1. the finite chiral spectral projector has constant rank and a common gap;
2. the finite BV-Hodge integration cycle exists;
3. determinant-line open-path transport is unitary;
4. the determinant-line curvature obstruction vanishes; and
5. faithful gauge-loop holonomy is trivial.

Then one basepoint unit determinant vector produces, by the lemma, a unique
parallel unit section up to one constant \(U(1)\) phase. The dual top exterior
form of this section defines a finite Grassmann/Berezin measure on the chiral
spectral subspace.

For every admitted based gauge/frame transport in \(B_0\), the measure is
carried into itself. Its measure Jacobian is therefore

\[
J_N(g)=1,\qquad \|J_N(g)-1\|=0.
\]

This is an exact identity at every admitted finite spectral cutoff. It does
not use an expansion in the interaction coordinate. Consequently, the
zero-Jacobian-defect sequence belongs to the norm-null ideal and remains zero
in every Cstar reduced product.

Changing the basepoint section multiplies numerator and denominator of every
defined normalized observable by the same constant phase. It therefore does
not introduce a physical parameter.

## Exact Finite Witness

The certificate checks two independent algebraic parts over the rationals.

First, left multiplication by quaternion units \(i\) and \(j\) gives two
noncommuting real \(4\times4\) representatives of \(SU(2)\). They are
orthogonal, square to \(-I\), anticommute and have determinant \(+1\).
Eight words, including their group commutator, all have determinant \(+1\);
their exact orientation-Jacobian defect sequence is

\[
(0,0,0,0,0,0,0,0).
\]

Second, the rank-two projector

\[
P_0=\operatorname{diag}(1,1,0,0)
\]

is transported by the rational orthogonal matrix built from the
\(3/5,4/5\) rotation. The resulting \(P_1=UP_0U^T\) is again a
self-adjoint rank-two projector. Its transported basis is orthonormal and
the Gram determinant of its top wedge is exactly one.

This witness tests noncommutativity, orientation and constant-rank transport.
It is not a finite proof of faithful-SM anomaly cancellation or of
full-domain locality.

## Full-Domain Cutset

Four independent extension rows remain open:

1. **Selected physical family.** Construct one selected smooth q79 chiral
   projector, connection and Hessian family on the full admitted physical
   background domain.
2. **Local measure current.** Construct a local gauge-covariant measure
   current satisfying the integrability condition in directions transverse
   to the certified presentation orbit.
3. **Strata and sector gluing.** Extend through zero-mode crossings,
   reducible and small-instanton strata, and select relative phases and
   finite counterterms between disconnected sectors.
4. **Uniform control.** Prove cutoff-uniform locality and fixed-coupling norm
   estimates on that full domain.

The orbitwise contract is `7/7`; the full-domain extension contract is `0/4`.
The continuum table remains `1/9`, and the full chiral-measure and full Ward
rows remain false.

## Claim Boundary

The theorem proves a nonperturbative finite-spectral measure on the certified
connected q79 presentation orbit. It does not prove:

- a local lattice measure for a general nonabelian chiral gauge theory;
- coverage of the full Standard-Model quotient-moduli space;
- trivial determinant holonomy for uncertified frame or diffeomorphism loops;
- gluing across spectral crossings or disconnected sectors;
- a selected physical q79 regulator family;
- uniform interacting cutoff removal; or
- the fixed-coupling continuum Standard Model.

The distinction agrees with the registered external boundary: Luscher's
exact nonperturbative construction covers anomaly-free abelian chiral lattice
theories, while the registered general compact-group construction is
perturbative. The present q79 result is different: exact and
nonperturbative, but only on a finite-spectral connected presentation orbit.

## Parameter Ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:     0
new fits:                            0
new observed values:                 0
basepoint phase:                     one U(1) convention per component
physical count of that convention:  0
```

## Version Delta

Version 1 converts the previously available determinant-line
trivializability and orbit transport into an explicit finite chiral Berezin
measure. It closes the orbitwise measure-Jacobian norm defect exactly and
replaces the undifferentiated measure blocker by the four-row full-domain
cutset above. No continuum row is promoted.
