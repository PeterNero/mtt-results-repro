---
abstract: |
  The ordinary sector-map validator puts all SM slots inside one rank-three
  family carrier.  That is not the correct architecture for the qutrit
  projective route because the irreducible qutrit block has no rank-one Higgs
  projector.  This note validates the corrected block-factorized sector maps:
  Q,u,d,L,e,N occupy the full rank-three projective family block, while H
  occupies a separate ordinary rank-one line.  The finite sector-map problem
  is therefore closed for the block-factorized architecture, while selected
  gerbe/source promotion and selected D_E/dotD remain open.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Block-Factorized Sector Maps
---

# Purpose

The previous obstruction was:

```text
the irreducible qutrit carrier has no rank-one H projector.
```

The corrected architecture is:

```text
rank-three qutrit family block: Q,u,d,L,e,N,
separate rank-one ordinary Higgs line: H.
```

Equivalently, Q,u,d,L,e,N occupy the full rank-three projective family
block, and H occupies a separate ordinary rank-one line.

# Validator

The validator:

```text
scripts/validate_iwasawa_block_factorized_sector_maps.py
```

checks:

```text
projective qutrit rho_E mesh passes,
rho_E metric compatibility passes,
Q,u,d,L,e,N are full rank-three projectors on the family block,
H is a rank-one projector on the separate Higgs line,
H is not forced into the irreducible qutrit carrier.
```

# Result

The candidate packet:

```text
candidate_data/iwasawa_block_factorized_sector_maps.candidate.json
```

passes the validator.

This closes:

```text
finite block-factorized sector-map schema,
family-sector projector consistency,
separate Higgs-line projector consistency,
the old rank-one-H-inside-qutrit obstruction.
```

# What Remains Open

This is still not selected source promotion.  It does not supply:

```text
selected Deligne/Cech gerbe representative,
selected B-field period table,
selected D_E,
selected dotD,
Yukawa values,
full SM closure.
```

The sector maps are now ready for the block-factorized twisted-source
promotion attempt, but the selected gerbe/source representative remains the
next hard missing datum.
