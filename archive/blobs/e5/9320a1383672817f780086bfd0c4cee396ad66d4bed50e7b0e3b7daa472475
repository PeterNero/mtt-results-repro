# MTT CONST EW 02 Weak Mixing B9 Profile Reduction and Universal Parameter Gate v1

Status: `MTT_CONST_EW_02_B9_PROFILE_REDUCED_UNIVERSAL_PARAMETER_GATE_READY_VALUES_OPEN`

Label: `CONST-EW-02 / WEAK-MIXING / B9-PROFILE-REDUCTION-AND-PRIMITIVE-GATE`

## Result

B9 does not close the physical weak mixing angle.  It does something narrower
and useful: it reduces the remaining one-loop problem to source-selected
profile combinations.

General one-loop lane:

```text
u1 = x*(b1*L/(8*pi^2) + T1)
u2 = x*(b2*L/(8*pi^2) + T2)
sin2 = 3*(1+u2)/(3*(1+u2)+5*(1/r12+u1))
```

No-threshold lane:

```text
y = x*L/(8*pi^2)
sin2(y)=3*(1+b2*y)/(3*(1+b2*y)+5*(1/r12+b1*y))
```

with:

- `r12 = 0.56027`,
- `b1 = 4.1`,
- `b2 = -3.1666666666666665`,
- `sin2(0) = 0.2515877565744274`.

The high-scale value exactly replays B5.  The low-scale/effective value still
requires a source-selected `y` or source-selected `(u1,u2)`.

## Superset Import

The SM-parity T1/T2 covariant Green result is imported as operator support:
the coupled diagonal End0 `T1/T2` Green is closed, but sector routing,
off-diagonal Ext/HYM control, and physical amplitudes are not.

## Universal Parameter Policy

A one-universal-parameter extension is admissible as a labeled non-no-knob lane
if the primitive is selected once upstream and shared across sectors.  It is
forbidden to choose that primitive from the weak angle, alpha_EM, or any target
constant while claiming no-knob closure.

## Next

`CONST-EW-02 / WEAK-MIXING / B10-SOURCE-y-OR-u1u2`
