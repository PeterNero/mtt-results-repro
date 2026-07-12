---
title: "Selected Qa/SU3 C-Twist Transgression Pairing Computation"
---

# Selected `Qa/SU3` C-Twist Transgression Pairing Computation

This note computes the invariant Iwasawa transgression candidate.

Use the real frame:

```text
omega1 = (e1+i e2)/r1,
omega2 = (e3+i e4)/r2,
omega3 = (e5+i e6)/r3.
```

The flux paper gives:

```text
H = -r3^2/2 (bar(omega3) omega1 omega2 - omega3 bar(omega1) bar(omega2)).
```

Suppressing the common positive scale `A = r3/(r1 r2)`, the real slants are
nonzero and purely central:

```text
i_(e1,e3) H -> central e6,
i_(e1,e4) H -> central e5,
i_(e2,e3) H -> central e5,
i_(e2,e4) H -> central e6.
```

This is not the raw nil commutator table:

```text
[g1,g3] = g5,
[g1,g4] = g6,
[g2,g3] = g6,
[g2,g4] = g5^-1.
```

Instead, the transgressed flux appears in the complex-rotated central
polarization. That is precisely the kind of orthogonal nesting expected if the
`c`-twist is selected through the complex structure rather than through the
literal central line-bundle axis.

## Result

This avoids the zero-pairing no-go. The selected Iwasawa/Strominger `H` is not
orthogonal to the monad `c` direction: its base-pair slants are nonzero and
central.

## Still Open

This does not yet promote the gerbe route to full closure. The remaining
normalization and polarization question is:

```text
Does the selected flux/integrality normalization, together with the complex
central polarization, make this one finite c-twist generator, i.e. c = +/-1?
```

The next artifact is:

```text
Selected_Qa_SU3_Complex_Rotated_CTwist_Normalization_v1
```
