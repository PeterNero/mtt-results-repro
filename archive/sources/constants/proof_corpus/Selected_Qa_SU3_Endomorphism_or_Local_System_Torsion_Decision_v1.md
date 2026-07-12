# Selected Qa/SU3 Endomorphism or Local-System Torsion Decision v1

## Purpose

This records the route decision after retiring the displayed explicit HYM matrix
as a current proof source.

There are two different notions of "best" here:

```text
best physical source if filled:
  selected SU3 endomorphism_E or color threshold operator

best current executable route:
  selected acyclic local-system torsion extraction
```

The distinction matters.  A sourced `endomorphism_E` would be the cleanest SU3
threshold mechanism, but the current record has `endomorphism_E = null`, no
selected spectrum, and the explicit HYM matrix route is retired.  Therefore the
next computation should not keep pushing the same matrix under a new name.

## Decision

The next executable artifact is:

```text
Selected_Qa_SU3_Local_System_Torsion_Source_Extraction_v1
```

Its job is to try to source-select the local system or lattice character before
any comparison with the Qa/SU3 residual.

It must either compute or refute:

```text
selected Nil/Iwasawa compact quotient and lattice character,
representation/color trace weight,
BRST degree weights and zero-mode rule,
Ray-Singer/Reidemeister torsion finite part.
```

If these data are not selected upstream, the torsion route remains open but
underdetermined.

## Route Status

```text
selected endomorphism_E / color threshold operator:
  physically primary if a source-certified full operator appears,
  not currently computable.

acyclic local-system torsion:
  best current executable test,
  not currently a closed numeric prediction.

global section / fundamental-domain measure:
  secondary open route,
  legal only if distinct from already counted local FP/BRST quotient.
```

## Guardrails

Do not use:

```text
the retired printed HYM matrix or A/B repairs,
the observed Qa/SU3 residual to choose a torsion character,
local FP/BRST determinant as an extra global factor,
soft gauge-tube width or regulator as physical threshold data.
```

## Verdict

```text
Qa/SU3 closed: no
full SM closure achieved: no
target fitting used: no
torsion selected as next executable test: yes
```
