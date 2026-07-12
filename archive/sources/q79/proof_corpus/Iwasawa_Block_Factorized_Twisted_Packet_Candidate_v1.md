---
abstract: |
  We turn the block-factorized Iwasawa twist route into an executable packet
  candidate.  The rank-three family block is the existing qutrit projective
  carrier and passes finite projective rho_E gluing with a nontrivial zeta_3
  central twist.  The Higgs block is kept as a separate ordinary rank-one line
  with strict trivial gluing.  This closes the finite architecture and sector
  partition check, while leaving MTT selection, the full Bianchi/Freed-Witten
  checks, D_E/dotD, C1 contractions, and Yukawa weights open.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Block-Factorized Twisted Packet Candidate
---

# Statement

The direct-sum repair

```text
diag(X,1), diag(Z,1)
```

is rejected because its corner ratio is `diag(zeta_3 I_3,1)`, not a scalar
multiple of the rank-four identity.

The finite replacement is a block-factorized packet:

```text
family block: rank-three qutrit projective rho_E carrier,
Higgs block: ordinary rank-one line,
coupling: tensor/block rule, with selected D_E/dotD still open.
```

# Validated Candidate

The executable packet is:

```text
candidate_data/iwasawa_block_factorized_twisted_packet.candidate.json
```

The validator checks:

```text
family sectors = {Q,u,d,L,e,N},
Higgs sectors = {H},
sector union = full SM slot list,
sector overlap = empty,
family projective gluing = pass,
family central twist = nontrivial,
Higgs line strict gluing = pass,
Higgs projector rank = one.
```

The coupling rule is now carried only at the finite selection-rule level:

```text
s_left+s_right=0 mod 3 for trivial-Higgs SM pairs,
same-twist all-family assignment = blocked,
conjugate orientation pairing = required,
selected sector orientation assignment = open.
```

The family block keeps the known projective rho_E result:

```text
central_phase_histogram = {zeta_1^0: 631, zeta_3^2: 274}
strict_vector_bundle_gluing_passes = false
projective_gerbe_gluing_passes = true
```

The Higgs line has:

```text
rho_H(g_i) = 1 for i=1,...,6,
P_H = [1].
```

So the Higgs block is a genuine ordinary rank-one carrier and does not try to
absorb the qutrit twist.

# What Is Closed

This closes the missing finite packet schema:

```text
block-factorized packet schema,
family projective block validation,
separate Higgs line validation,
SM sector partition across blocks,
rank-four shortcut rejection carried forward.
```

# What Is Not Closed

This is not a selected-source theorem.  The following are still open:

```text
selected Deligne/Cech gerbe or B-field representative,
fixed Iwasawa topological sector for that representative,
full Green-Schwarz Bianchi check,
Freed-Witten check,
selected D_E and dotD on the factorized blocks,
primitive C1 contractions,
Yukawa overlap weights.
```

# Consequence

The projective route is now cleaner.  We no longer need to choose between an
irreducible qutrit block with no Higgs projector and a rank-four block with bad
scalar gluing.  The correct finite architecture validates as a factorized
candidate.  The hard remaining work is selection and differential geometry:
replace the candidate gerbe holonomy map with an MTT-selected representative,
then compute the factorized D_E/dotD and C1 response values.
