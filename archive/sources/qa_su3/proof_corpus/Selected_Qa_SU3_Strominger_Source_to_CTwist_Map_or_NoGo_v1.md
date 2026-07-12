---
title: "Selected Qa/SU3 Strominger Source to C-Twist Map or No-Go"
---

# Selected `Qa/SU3` Strominger Source to C-Twist Map or No-Go

The best same-branch source family is now clear:

```text
selected Strominger/Iwasawa fixed differential-cohomology sector
with global Green-Schwarz gerbe curvature Hhat/H.
```

The needed target is also clear:

```text
tau_QaSU3 -> central c-twist quotient,
pairing(tau_QaSU3, central quotient) = generator 1,
T_+1 tensor T_-1 -> T_0.
```

## Candidate Maps

Four map routes were tested.

```text
direct central restriction:
  cleanest, but not supplied.

Hhat curvature transgression:
  live, because Hhat/H is selected and integral,
  but no slant product or cycle pairing has been computed.

finite Z3 torsion extraction:
  works as q79/S3 guardrail only,
  not same-branch Qa/SU3 proof.

Bianchi alpha1 support:
  useful source row,
  but Bianchi four-form support is not by itself a DD/twist class.
```

## Result

```text
closure: no
no-go: no
gerbe route: live
A01/D_E fallback: should run in parallel
```

The current corpus proves the existence of the right source family, but not the
map from that family to the `c = +/-1` monad twist.

## Next Computation

The next artifact should compute the missing pairing:

```text
Selected_Qa_SU3_CTwist_Transgression_Pairing_Computation_v1
```

It must construct a cover-independent restriction, slant product, or
transgression:

```text
Hhat or tau_QaSU3
paired with selected Iwasawa base/central cycles
-> finite central c-twist generator.
```

If the pairing is zero or incompatible for the selected source, the gerbe
route retires and the proof must use:

```text
Selected_Qa_SU3_A01_DE_Operator_Exit_v1.
```
