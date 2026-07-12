# Final Internal rho_UV Selected-Radius Theorem v1

## Purpose

This theorem consolidates the rho_UV branch after selecting the
Bianchi-constrained horizontal scale law.

It is the internal no-knob endpoint for this branch.

## Theorem

On the selected character-channel Iwasawa/Strominger branch in internal
`alpha'=1` units, with the H2 horizontal scale law selected, the internal
radius and rho_UV value are:

```text
R_*     = 4.440528182269818,
rho_UV  = 0.164530397543639.
```

The associated branch quantities are:

```text
r3      = 4.440028979122532,
v1      = 0.405623467693425,
s_*     = 1.464646774701829.
```

## Proof

The final selected-character theorem gives:

```text
rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2.
```

The selected horizontal scale-law theorem rejects the extra `R^-4` factor as
double-counting, because `rho_UV(R)` is already the evaluated squared UV
response on the Bianchi-constrained branch:

```text
R -> (R,R,r3(R)).
```

Thus the selected functional is:

```text
F_H2(R) = rho_UV(R) + R^2/30.
```

Let:

```text
a = 64(2pi)^2,
x = R^2.
```

Then:

```text
F_H2 = a^2/(16x^2+8)^2 + x/30.
```

The Euler equation is:

```text
dF_H2/dx = 1/30 - 64 a^2 x/(16x^2+8)^3 = 0,
```

or:

```text
(16x^2+8)^3 = 1920 a^2 x.
```

The small positive stationary point is a local maximum:

```text
R = 0.0002043829462837498.
```

The large positive stationary point is the global minimum:

```text
R_* = 4.440528182269818.
```

Evaluating the closed rho_UV branch function at `R_*` gives:

```text
rho_UV = 0.164530397543639.
```

## What Is Closed

```text
selected character-channel covariance       CLOSED
rho_UV(R) branch function                   CLOSED
horizontal scale-law selection              CLOSED
selected internal radius R_*                CLOSED
selected internal rho_UV                    CLOSED
primitive R fallback for this branch        NOT NEEDED
```

## What Is Not Claimed

This theorem does not claim:

```text
1. a dimensionful SI constant;
2. an electroweak prediction;
3. a Standard Model closure result;
4. a measured-value comparison;
5. a universal primitive constant of the whole theory.
```

Those require separate audits.

## Next Step

The correct next program is the electroweak no-knob audit using this internally
selected branch value as an input only if the audit can justify the bridge.

## Verdict

The rho_UV internal branch is closed:

```text
R_* = 4.440528182269818,
rho_UV = 0.164530397543639.
```

This is a derived internal dimensionless branch result, not a fitted parameter.
