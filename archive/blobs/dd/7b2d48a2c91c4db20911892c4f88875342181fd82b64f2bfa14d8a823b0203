---
title: "Visible Rank-Two L2 Ordered Source Promotion Gate"
version: v1
---

# Visible Rank-Two `L^2` Ordered Source Promotion Gate

## Purpose

The target Appell-Humbert representative now exists, but existence is not
selection.  This packet makes the remaining ordered-source promotion problem
machine-checkable.

This is the ordered-source promotion gate for the visible rank-two `L^2`
route.

The target ordered ordinary matrix is:

```text
L=(1,-2,0),
L^2=(2,-4,0),
E(g1,g2)=2,
E(g3,g4)=-4,
E(g5,g6)=0.
```

## Validator

The validator is:

```text
scripts/validate_visible_rank2_l2_ordered_source_packet.py
```

It consumes:

```text
certificates/visible_rank2_l2_ordered_source.template.json
```

and accepts only a packet with one of the selected statuses:

```text
VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED
VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED
```

## Why the Current Appell-Humbert Packet Fails Promotion

The current Appell-Humbert packet is mathematically correct as an automorphy
formula.  It is written into:

```text
candidate_data/visible_rank2_l2_ordered_source.current_attempt.json
```

The validator refuses it as:

```text
UNSELECTED_FIXTURE.
```

The refusal is intentional.  The current packet has:

```text
explicit non-flat formula: yes,
cocycle check: yes,
ordinary c1 matrix: yes,
selected source status: no,
selected base ordering: no,
target-vs-swapped source breaking: no,
Pic0 selected or quotiented: no.
```

Thus it is not enough that the Appell-Humbert formula exists.

## Promotion Contract

A future source packet must supply:

```text
selected source status,
standard lattice or equivalent selected geometry,
base ordering with E1/g1g2 carrying +2 and E2/g3g4 carrying -4,
target-vs-swapped base-swap breaking,
evidence that the source is not only finite mod-3 qutrit data,
evidence that the source is not the equal-radius constants import,
Pic0 resolution.
```

The `Pic0` resolution may be one of:

```text
neutral_character_selected,
pic0_quotient_rule,
specific_flat_character_selected.
```

## What This Closes

This closes the executable promotion gate:

```text
ordered source packet schema: closed,
validator: closed,
current Appell-Humbert fixture refusal: closed,
future selected-source status names: fixed.
```

## What Remains

The actual selected source is still open:

```text
selected ordered integral source certificate,
standard lattice or equivalent source selection,
base ordering source selection,
Pic0 selection or quotient rule,
nonzero Ext class selection,
non-split extension stability,
same-source D_E/dotD/Riesz/Green.
```

## Verdict

The ordered integral branch has moved from a vague missing source to an
executable pass/fail packet.  A future proof must fill the template and pass
the validator; the current Appell-Humbert formula is correctly refused until
MTT selection and `Pic0` resolution are supplied.
