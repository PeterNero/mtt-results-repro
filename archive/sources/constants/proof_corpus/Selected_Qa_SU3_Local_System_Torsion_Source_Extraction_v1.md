# Selected Qa/SU3 Local-System Torsion Source Extraction v1

## Purpose

This artifact tries to execute the local-system torsion route selected by the
previous decision gate.

The route is legal only if the local system or lattice character is selected
before comparison with the Qa/SU3 residual.

## Extraction Result

The current corpus supplies:

```text
p != 0 compact Nil acyclicity,
p0 and p != 0 BRST/zero-mode rules,
compact Nil scalar spectrum data,
scalar Hurwitz-zeta diagnostic,
general holonomy/character language,
Z64 q64=15 selected character in the rho_UV/CP branch.
```

But it does not supply:

```text
a selected Qa/SU3 compact-Nil or Iwasawa local-system character,
degree-wise Ray-Singer/Reidemeister torsion finite parts for that character,
Qa/SU3 representation/color trace weights for torsion,
a bridge theorem identifying the q64=15 CP/rho_UV character with Qa/SU3 torsion.
```

Therefore the torsion route is not closed under the current corpus.

## Candidate Outcomes

```text
trivial local system:
  rejected as a nontrivial acyclic torsion correction.

compact Nil p != 0 central-momentum tower:
  selected as an acyclic Hodge sector, but not as a single upstream local-system
  character with torsion weights.

Z64 q64=15 character:
  selected for rho_UV/CP, not currently bridged to Qa/SU3 local-system torsion.

SU3 fundamental/adjoint color holonomy:
  representation language exists, but no lattice character or torsion finite
  part is selected.

heterotic Lens-Nil flux integers:
  anomaly/flux data exist, but they are not a selected compact-Nil torsion
  character.
```

## Verdict

```text
Qa/SU3 closed: no
full SM closure achieved: no
target fitting used: no
Ray-Singer torsion computable now: no
torsion route mathematically retired: no
torsion route underdetermined under current corpus: yes
```

## Next Routes

The best next route is now:

```text
prove or import a selected compact-Nil/Iwasawa local-system character theorem.
```

If that fails, the parallel route is:

```text
source-certify a full endomorphism_E / threshold operator not inherited from
the retired explicit HYM matrix.
```
