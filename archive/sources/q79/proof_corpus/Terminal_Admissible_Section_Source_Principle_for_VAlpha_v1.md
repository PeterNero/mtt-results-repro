---
title: "Terminal Admissible-Section Source Principle for VAlpha"
author: "MTT proof reproduction program"
---

# Question

Can the terminal `g3` VAlpha source be selected without using measured masses,
mixings, benchmark Yukawa entries, or another arithmetic proxy?

# Result

The sharp solution is not another finite-sign search. The missing selector is
an admissible-section theorem:

```text
TerminalAdmissibleSectionSourcePrinciple.v1
```

This principle says that once an MTT quotient/degeneracy class has been reduced
to a terminal representative section, the selected source is the unique
refinement-stable admissible section that:

```text
resolves the active obstruction data with minimal added responsibility,
preserves the shared central-circle constraint,
realizes the required visible Chern class,
uses no observed or benchmark flavor inputs.
```

# Corpus Basis

This is a synthesis of already present MTT rules:

```text
gauge fixing as admissible section selection,
nil boundaries selecting refinement-stable survivors,
minimal extension required by saturation,
duality identifying equivalent obstruction-resolution data.
```

The audit treats this as an explicit principle that must either be promoted into
the MTT axiomatic spine or proved from the projection-admissibility formalism
before the result is called unconditional.

# Derivation

Under this principle, the terminal monad lane is scanned as `L_i-K2`. The
shared-circle/central-neutral filter has exactly one survivor:

```text
L3-K2 = (1,-2,0).
```

The visible Chern condition gives the same unique survivor:

```text
c2(V_alpha) = -L^2 = +4 alpha_1.
```

The printed terminal map type is the dual:

```text
g3 has Hom type K2-L3 = (-1,2,0),
physical extension line L = L3-K2 = (1,-2,0),
L^2 = (2,-4,0).
```

So the selected terminal source label is:

```text
g3 / L3-K2.
```

# Executable Consequence

The script writes two selected-under-principle packets:

```text
candidate_data/terminal_admissible_section_source/visible_rank2_l2_ordered_source.selected_under_section_principle.json
candidate_data/terminal_admissible_section_source/visible_rank2_l2_cohomology.selected_under_section_principle.json
```

Both validators pass:

```text
ordered L2 source: PASS,
h1=8 cohomology and nonzero closed non-exact Ext vector: PASS.
```

Thus, under this principle, the sign/order source selector and selected Ext
promotion are closed.

# What Remains

This is not full SM closure. It does not prove:

```text
non-split stability/HYM,
raw good-cover or smooth Dolbeault transitions,
same-source Chern-Weil/GS/D_E/Riesz/Green/dotD data,
operator-layer Pic0 blindness,
primitive C1 contractions,
Yukawa/CKM/PMNS magnitudes.
```

# Verdict

The solution is to stop hunting for another sign selector. The terminal `g3`
route is selected by an admissible-section source principle. If we accept or
prove that principle as part of MTT, the remaining frontier moves past
`L=(1,-2,0)` and `h1=8`; it becomes the stability/HYM and same-source operator
packet.
