---
title: "Visible Rank-Two L2 Pullback Selection Attempt"
version: v1
---

# Visible Rank-Two `L^2` Pullback Selection Attempt

## Question

Can we now prove that MTT selects the base-pullback `L^2` representative used
in the conditional Cech packet?

## Short Answer

Not unconditionally from the currently audited sources.

But the remaining gap is now smaller than before.  The same matrices already
give:

```text
c1(L^2)=(2,-4,0),
h1=8,
a closed non-exact Ext vector.
```

If a source certificate selecting the base-pullback L^2 representative is
supplied, the unchanged packet validates as `SELECTED_DATA` and promotes the
rank-two route to a non-split `V_alpha` input.

## The Check Performed

The script validates two packets:

```text
1. the actual packet:
   candidate_role = UNSELECTED_FIXTURE

2. the same matrices with only source metadata changed:
   candidate_role = SELECTED_DATA
   source.selected_by_mtt = true
   source.fixture_only = false
```

The matrices, basis labels, `d0`, `d1`, and Ext vector are not changed.

The result is:

```text
actual packet validates: yes,
actual packet promotes selected V_alpha: no,
hypothetical selected packet validates: yes,
hypothetical selected packet promotes selected V_alpha: yes,
h1 remains: 8.
```

So the algebraic and cohomological part is no longer the blocker.

## Relative Theorem

**Theorem.** If MTT supplies a source certificate selecting the base-pullback
typed Cech line bundle with the already-computed transition class, then the
existing finite packet is selected data, computes `H^1(X,L^2)` with `h1=8`,
and supplies a nonzero class in:

```text
Ext^1(L^{-1},L)=H^1(X,L^2).
```

That class promotes the rank-two extension route at the Ext gate.

## Why This Is Not Yet The Full Theorem

The current corpus still says:

```text
selected L^2 source data absent,
standard Iwasawa deck scaffold selection open,
line-bundle section-ring / automorphy source data open,
the constants-repo Iwasawa automorphy attempt is symbolic-only.
```

The selected gerbe and S3 pullback closures are real adjacent evidence, but
they select twisted/gerbe data, not this visible `L^2` line-bundle
representative.

Therefore the unconditional selection theorem is not proved.

## Exact Missing Object

The missing object is now:

```text
Selected_Pullback_L2_Source_Certificate
```

It must prove:

```text
MTT selects pi^*M on the standard Iwasawa branch,
M has degrees (2,-4) on the base elliptic factors,
no extra flat or torsion twist is selected,
the automorphy/transition data are the same branch as visible V_alpha,
the packet can be promoted from UNSELECTED_FIXTURE to SELECTED_DATA.
```

## Verdict

We did not yet prove unconditional MTT selection.  We did prove that selection
is the only remaining gap for the `L^2` Ext packet.  Once the source
certificate is supplied, no new cohomology calculation is needed: the `h1=8`
packet already promotes.
