# Primitive Constant Discipline for No-Knob Program v1

## Purpose

The no-knob program should not pretend that every possible constant must be
derived from nothing. A physical theory may contain primitive universe data.

The key distinction is:

```text
primitive constant != adjustable fit knob.
```

This note states when a surviving free parameter is acceptable and when it
would damage the program.

## Forbidden Fit Knob

A parameter is a forbidden knob if it is chosen after looking at the target
observable.

Examples:

```text
choose R to match rho_UV,
choose G10 to match G_N,
choose alpha' to match M_Pl,
choose epsilon_adm to match H0,
choose threshold coefficients to match observed gauge couplings.
```

These are not predictions. They are backsolves.

## Acceptable Primitive Constant

A surviving constant may be acceptable only if all of the following hold:

```text
1. Universality:
   the same value is used across several unrelated sectors.

2. Prior selection:
   the value is fixed before evaluating the target observable.

3. Source role:
   it appears as part of the theory's definition, branch selection, topology,
   flux sector, action normalization, or coherence tolerance.

4. Auditability:
   the repo can state exactly where the constant enters and which predictions
   depend on it.

5. Non-redundancy:
   it cannot be removed by a unit convention, quotient, or normalization.

6. Predictive surplus:
   once set, it constrains more observables than the one used to identify it.
```

If a parameter fails these tests, it remains an open gate or a fit knob.

## Candidate Primitive Classes

The current corpus suggests a few possible primitive classes if no-knob closure
fails:

```text
finite branch data:
  N, q_64, selected character/tower sector.

coherence/admissibility data:
  epsilon_adm, C_Q, leakage tolerance.

action-unit data:
  alpha_int, G10_int, string-length normalization.

topological/flux data:
  selected integral fluxes, gerbe periods, Chern classes.

global branch scale:
  a single dimensionless internal normalization shared by MTT/MMT sectors.
```

The strongest kind would be finite branch data, because it is discrete. The
most dangerous kind would be a continuous scale chosen independently for each
target.

## Application to rho_UV

For the rho_UV branch, a surviving `R` would be acceptable only if it is not a
bespoke rho_UV knob.

Acceptable:

```text
R selected by the same Flux/Strominger branch used for other predictions,
R forced by a fixed-point condition,
R derived from shared Lens/Nil/circle compatibility,
R inherited from a universal internal scale used elsewhere.
```

Not acceptable:

```text
R chosen to make rho_UV numerically attractive,
R chosen after comparing to electroweak data,
R separately chosen for the rho_UV branch only.
```

## Current Best Status

The current best route remains no-knob:

```text
prove the Selected Horizontal-Scale Lemma
-> R is internally selected
-> rho_UV becomes a derived dimensionless number.
```

If the lemma fails, the next-best credible path is not to hide `R`; it is to
classify `R` as either:

```text
1. a universal primitive internal scale, if it passes the tests above; or
2. an open normalization parameter, if it does not.
```

## Verdict

Having one or a few primitive constants would not automatically make the
program unscientific. It would still be much stronger than a many-knob fit if
those constants are universal, prior, audited, and prediction-rich.

But the rho_UV branch is close enough that the right next move is still to try
to remove `R`, not to declare it primitive.
