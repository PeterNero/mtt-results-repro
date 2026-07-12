# Selected Qa/SU3 Color Bundle Connection or Global Section Determinant

## Purpose

The previous source hunt chose the next legal gate after the compact-Nil
Hodge/BRST branch overshot Qa/SU3:

```text
selected Qa = 4.8430192935084335
required Qa = 4.648486359430842
needed new selected response = -0.19453293407759187
```

This note builds the determinant interface for that response.  It does not
choose the response from the residual.

## Exhausted Inputs

Two tempting shortcuts are now forbidden.

First, the canonical Nil Weitzenbock term cannot be added again.  The sourced
co-closed one-form determinant is already a Hodge determinant, so it already
contains the canonical Nil Ricci/Weitzenbock term.

Second, the local Faddeev-Popov/BRST quotient Jacobian cannot be reused.  The
`p=0` and `p != 0` quotient rules already count the local quotient measure.

Thus any successful next determinant must be genuinely new selected operator or
global-section data.

## Route A: Selected SU3 Color Connection

The legal operator form is:

```text
D_Qa,color = -(nabla_A^* nabla_A on BRST physical SU3 color bundle)
             + E(A,R_+,F)
```

This route is corpus-supported in structure: the heterotic/Strominger material
contains torsional connections, flux curvature, and left-invariant finite
systems; the NCG material contains inner fluctuations and finite connections;
the topology-only material treats SU3 anomaly/global-section constraints.

But the selected data are not yet present.  We still need:

```text
explicit SU3 color bundle or local system,
selected connection A or flux-twisted connection,
curvature endomorphism E(A,R_+,F),
BRST physical quotient domain,
zeta/heat/analytic-torsion finite part.
```

This is the best next route because it changes the actual selected threshold
operator rather than appending a fitted projector factor.

## Route B: Global Section / Gribov Measure

The gauge-fixing corpus supports global-section failure as a real projection
phenomenon.  A selected fundamental modular region could, in principle, supply
a finite measure ratio beyond the local FP determinant.

This is legal only if it supplies:

```text
selected SU3/Nil configuration space and gauge action,
selected global-section atlas or fundamental domain,
finite measure ratio,
proof that this is not the already-counted local FP determinant.
```

At present the structure is supported, but the measure is not selected.

## Route C: Acyclic Local-System Torsion

The `p != 0` Nil Hodge complex is acyclic, so analytic torsion is the natural
mathematical invariant to audit.  This route is legal only after selecting:

```text
lattice character or flat local system,
color trace/representation weight,
torsion normalization compatible with BRST,
closed formula or computable spectrum for compact Nil.
```

This should be developed in parallel with Route A, because it may be the same
data expressed as a local-system determinant.

## Verdict

The next gate is reduced to selected operator data:

```text
best next computation:
  selected SU3 color connection

parallel mathematical computation:
  acyclic local-system torsion

fallback:
  global-section / Gribov fundamental-domain measure
```

No new numeric closure is certified here.  That is the rigorous conclusion:
the corpus gives the right mechanisms, but not yet the selected SU3 color
connection/local-system/global-measure data needed to compute the determinant.

Next artifact:

```text
Selected_Qa_SU3_Color_Connection_Local_System_Torsion_Interface_v1
```
