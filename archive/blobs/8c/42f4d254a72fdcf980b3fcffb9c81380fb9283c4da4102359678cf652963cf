# Selected Qa/SU3 C-Axis Orthogonality Source or Weighted Operator Packet v1

## Result

This proves the `c`-axis orthogonality theorem under a clean source condition:
central-twist orbit democracy.

The required weight partition is:

```text
|tau|=1 labels: common weight a
tau=0 pair F3/G3: common weight b
P: weight p
a,b,p > 0
```

Then the weighted Hessian is:

```text
[['25*a + b + p', '-3*a - 2*b - p', 0], ['-3*a - 2*b - p', '4*a + 5*b + p', 0], [0, 0, '8*a']]
```

So:

```text
H13 = H23 = 0
```

identically.  The `c` axis decouples, `G_ret` is block diagonal, and the central
twist selector remains:

```text
Pi_tw = +e3
```

## Why This Is Better Than W=I

Unit weights are sufficient but not necessary.  The non-unit sample in the
candidate packet has:

```text
H = [['133/5', -4, 0], [-4, '61/5', 0], [0, 0, 8]]
G = [['305/7713', '100/7713', 0], ['100/7713', '665/7713', 0], [0, 0, '1/8']]
```

and still preserves the same `Pi_tw` and `tau`.

## Source Status

```text
central twist orbit partition: CLOSED_FROM_TAU_TABLE
opposite twist product cancellation: CLOSED_FROM_TYPED_MONAD_PRODUCTS
block diagonal internal bundle context: SUPPORTED_BY_STROMINGER_CORPUS
orbit-democracy operator weight: CONDITIONAL_NOT_SOURCE_SELECTED_AS_OPERATOR_WEIGHT
same-source operator packet: OPEN
determinant finite part: OPEN
```

## Verdict

The orthogonality is now proved as a theorem with an exact remaining source
condition.  It is not yet unconditional Qa/SU3 closure, because the current
source record does not yet prove that this orbit-democratic weight is the
selected smooth/operator determinant weight.

Next artifact:

```text
Selected_Qa_SU3_Central_Twist_Orbit_Democracy_Source_or_Determinant_Operator_v1
```
