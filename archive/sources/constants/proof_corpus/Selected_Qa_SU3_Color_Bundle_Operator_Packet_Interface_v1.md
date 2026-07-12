# Selected Qa/SU3 Color-Bundle Operator Packet Interface v1

## Purpose

The previous source hunt showed that the missing object is not another
correction factor.  It is a selected Qa/SU3 color-bundle operator packet.

This interface defines what that packet must contain before any determinant
or torsion finite part can be claimed.

## Required Packet

The packet must supply:

```text
selected branch and source certificate,
operator domain after selected p0 and p!=0 quotient rules,
selected color bundle, sheaf, or twist,
connection/curvature/HYM or Strominger residual data,
Laplace-type principal symbol,
endomorphism_E or equivalent zero-order heat block,
heat coefficient table, spectrum, or analytic/Reidemeister torsion,
trace normalization and gauge quotient scheme.
```

The interface is stored as:

```text
certificates/selected_qa_su3_color_bundle_operator_packet.template.json
```

## What Is Already Imported

The interface imports the already selected quotient structure:

```text
p0 ghost-measure normalization,
p != 0 physical quotient determinant domain,
projective clock-shift route decision,
endomorphism source-hunt result.
```

These are domain constraints, not determinant values.

## What Is Still Open

The template is intentionally unfilled:

```text
selected Qa/SU3 operator packet available: no
determinant computable now: no
Qa/SU3 closed: no
full SM closure achieved: no
target fitting used: no
```

## Forbidden Inputs

Do not fill this packet using:

```text
observed Qa/SU3 residual,
retired explicit HYM matrix entries,
rank-one q64 compact-Nil local-system character,
SU3 scalar-center q64 phase,
visible qutrit/F3^2 source as direct q64/U64 Qa/SU3 source,
local FP/BRST quotient counted a second time.
```

## Verdict

This closes the interface problem, not the determinant problem.

The next artifact must attempt to fill the packet from source-certified MTT,
Strominger, Fu-Yau, bundle, gerbe, or operator data:

```text
Selected_Qa_SU3_Color_Bundle_Operator_Packet_Fill_Attempt_v1
```
