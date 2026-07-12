---
title: "Constants and GR Cross-Repo Clue Ledger"
version: v1
---

# Constants and GR Cross-Repo Clue Ledger

## Question

Do the local constants and GR repositories contain anything that can help the
current q79 / visible-source / SM-closure branch?

## Result

Yes, but as proof discipline rather than as direct numerical or cohomological
data.

The constants repo contains a passing Qa/SU3 color-bundle operator packet
interface and a partial packet-fill attempt.  The useful part is the checklist:

```text
source certificate,
selected bundle, sheaf, or twist,
Chern/Mukai/Bianchi/Freed-Witten data,
connection or residual,
endomorphism_E or equivalent operator block,
heat table, spectrum, or analytic/Reidemeister torsion,
trace/action normalization.
```

The fill attempt explicitly refuses to promote Strominger/HYM templates into
selected operator data.  That is directly relevant to `V_alpha`: the rank-two
topological class and the Ext/H1 validator do not by themselves construct the
visible source.

The newest constants-side source-packet search sharpens the next move.  It
finds general Strominger/HYM templates and a visible-sector analogue, but still
does not find a same-branch Qa/SU3 source packet.  Its methodological lesson for
the visible branch is: stop searching generic prose once the templates are
known; start enumerating candidate Chern/Bianchi source packets with an
independent selection rule.

The GR repo contains a clean target/source separation.  The TT/Lichnerowicz
target and the Hessian form are reduced, but the selected source map and
normalization remain open.  This is the same shape as our current situation:
target constraints are strong, but source data must still be supplied.

The Qa/SU3 packet repo now adds a sharper status item: under the
GR-surface/internal-quantum separation theorem, the selected internal reduced
Qa/SU3 determinant is `log(2008)`.  This may be imported only as internal
reduced determinant status.  It is not a full gauge-threshold value, not a
Yukawa/CKM input, and not full SM closure.

## What We May Import

```text
operator/source packet discipline,
same-branch source requirement,
explicit Chern/Bianchi candidate-packet search pattern,
target-versus-source separation,
normalization guardrail,
symmetry-can-force-form-without-coefficient lesson.
internal reduced Qa/SU3 determinant status log(2008), scoped only to that packet.
```

## What We Must Not Import

```text
H^1(X,L^2) value,
nonzero Ext class,
selected V_alpha source,
same-source D_E/dotD/Riesz/Green data,
Yukawa or CKM magnitudes,
GR TT Hessian as a visible bundle operator,
Qa/SU3 operator packet as a visible V_alpha packet.
log(2008) as full threshold, Yukawa, CKM, or full SM closure data.
```

## Consequence

The next q79-side artifact should be a visible `V_alpha` selected-source packet
interface tied to the new `L^2` cohomology validator.  It should require the
cohomology packet, non-split stability, Chern/Bianchi data, HYM/Strominger or
Route-C residual, operator block, and same-source `D_E/dotD` data before any
SM-closure promotion.
