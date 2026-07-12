---
abstract: |
  We run the four proposed routes for the missing qutrit flat-torsion gerbe
  label: corpus evidence, finite topological computation, projector/zero-mode
  constraints, and orientation consistency.  All four routes reject the
  trivial label m=0 and converge on the same nontrivial conjugate pair
  m in {1,2}.  None of the four routes, without an extra selected orientation
  convention or fixed differential-cohomology representative, selects m=1
  rather than m=2.  Thus the last source datum is narrowed from "find a gerbe"
  to "choose the nontrivial conjugate orientation".
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Torsion Label Four-Route Selector
---

# Purpose

The remaining qutrit gerbe label is:

```text
m in Z3.
```

The labels mean:

```text
m=0: trivial flat torsion,
m=1: current qutrit zeta_3^2 orientation,
m=2: conjugate zeta_3^1 orientation.
```

We test four independent routes to see whether they select the same label.

# Route 1: Corpus

The corpus contains a nontrivial `Z3` family-holonomy mechanism:

```text
baseline Z3 family mechanism,
central-circle Z3 family holonomy,
three-family holonomy sectors,
ProtoSpinor three survivor basins.
```

This rejects the trivial label:

```text
m != 0.
```

But the corpus evidence does not specify the representative orientation, so it
leaves:

```text
m in {1,2}.
```

# Route 2: Topological Computation

The finite flat gerbe arithmetic checks:

```text
B_m((a,b),(a',b')) = m*(-a' b)/3 mod Z.
```

All labels have zero finite Bianchi residual and leave `Hhat` unchanged.  The
trivial label has commutator rank zero.  The two nontrivial labels have
rank-two alternating commutator form:

```text
m=1,2 are the two nontrivial qutrit/conjugate torsion generators.
```

So topology also gives:

```text
m in {1,2}.
```

# Route 3: Projector And Zero-Mode Constraints

The block-factorized finite architecture validates:

```text
family central twist nontrivial,
projective gerbe gluing passes,
strict ordinary gluing fails,
sector maps validate with H on a separate line.
```

That rejects `m=0`, because `m=0` would remove the nontrivial projective family
twist.  The SU(5) qutrit transport packet also validates finite algebra, but it
remains an unselected fixture.  So this route gives:

```text
m in {1,2},
selected zero-mode/projector retention still open.
```

# Route 4: Orientation Consistency

The C6/q79 orientation certificates reduce the branch freedom to a global
conjugate pair:

```text
[79,79,79,79] or [369,369,369,369].
```

The pure C6 phase block computes the two conjugate phases.  The SU(5) qutrit
transport attempt has finite orientation `F`, but it is explicitly not selected
MTT data.  Therefore orientation consistency removes independent per-channel
phase choices but does not choose the physical conjugate convention.

So the orientation route also gives:

```text
m in {1,2}.
```

# Consensus

All four routes agree:

```text
m != 0,
m in {1,2}.
```

They do not prove:

```text
m=1
```

or:

```text
m=2.
```

Conditionally, if we fix the current qutrit orientation convention, then
`m=1` is the current representative and `m=2` is the conjugate.  But that is a
representative convention, not yet a selected physical datum.

# Verdict

The four routes arrive at the same conclusion, but that conclusion is the
nontrivial conjugate pair rather than a unique label.  The remaining source
problem is now:

```text
select the conjugate orientation m=1 vs m=2.
```

Equivalently, supply a fixed differential-cohomology representative or selected
orientation convention.  After that, the twisted-source promotion gate can be
rerun with selected projector retention, selected `D_E`, selected `dotD`, and
primitive C1 contractions.

In short: a selected orientation convention is the remaining datum.
