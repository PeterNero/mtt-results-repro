# Antiunitary DEDotD Equivalence Test v1

## Result

The current finite q79 and q369 candidate packets are equivalent under
antiunitary conjugation at the operator-packet layer:

```text
D_E action slots: pass
Green/Riesz/projector slots: pass
dotD_alpha1 source and horizontal response slots: pass
branch metadata as global conjugate pair: pass
```

This closes the current finite-packet equivalence test.  The q79 and q369
branches are not independent operator knobs at this layer; they are one global
conjugate pair.

## Inputs

```text
q79:
  current_q79_orientation/de_action.candidate.json
  current_q79_orientation/reduced_green.candidate.json
  current_q79_orientation/dotd_response.candidate.json

q369:
  conjugate_q369_orientation/de_action.candidate.json
  conjugate_q369_orientation/reduced_green.candidate.json
  conjugate_q369_orientation/dotd_response.candidate.json
```

The test imports the previous C6 reduction certificate:

```text
selected_source_origin_or_antiunitary_dedotd_equivalence_attempt_certificate.json
```

## What Closed

```text
branch metadata is a q79/q369 global conjugate pair: yes
D_E action slots match under antiunitary conjugation: yes
Green/Riesz/projector slots match under antiunitary conjugation: yes
dotD_alpha1 and horizontal responses match under antiunitary conjugation: yes
current finite operator packets are antiunitarily equivalent: yes
```

## What Did Not Close

The result does not select q79 over q369.  Both branches still have open source
flags:

```text
selected source origin: open
selected D_E/dotD source flags: open
retarded/source boundary selector for one representative: open
primitive C1 contractions: open
selected Yukawa matrices: open
full SM closure: open
```

## Meaning

This is a useful reduction, not yet the final selection theorem.  It shows that
the D_E/Green/Riesz/dotD data do not give two separately tunable branches in the
current finite packets.  They give one antiunitary pair.  Therefore the next
true gate is a non-observed MTT source-origin or retarded-boundary rule that
chooses one representative, while treating the partner as the complex-conjugate
convention.

## Next Closing Object

```text
Retarded_Source_Boundary_Selector_or_Selected_Source_Origin_v1
```

It must prove one of:

```text
a non-observed MTT retarded/source boundary condition chooses one global
conjugate representative,

or

a selected visible source origin turns one branch's selected source flags on.
```

## Boundary

This test does not use observed CP sign, observed masses, benchmark flavor
entries, or lifted selected flags.  It does not claim full SM closure.
