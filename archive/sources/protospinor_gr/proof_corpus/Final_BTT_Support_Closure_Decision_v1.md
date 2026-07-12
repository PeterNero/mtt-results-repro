# Final BTT Support Closure Decision v1

## Decision

The remaining exact-support identity cannot be closed unconditionally from the
current corpus:

```text
Pi_exact64 B^* P_TT = B^* P_TT.
```

The reason is now precise. The central-circle paper contains the needed physical
idea, but it explicitly labels the gravity/shared-circle identification as
interpretive synthesis, not as a standalone theorem. The exact-support no-go
then proves that this identity is independent of the assumptions currently
sourced in the proof repo.

## What Is Closed

The proof state is no longer vague. We have closed:

```text
correct object: J_TT := Pi_exact64 B^* P_TT,
nonzero TT adjoint support,
TT weight 2,
BRST/diffeomorphism quotient compatibility,
exact Z64 branch availability,
uniqueness of the k=2 real character plane,
independence of exact support from current assumptions.
```

## The Unique Missing Theorem

Full closure now requires exactly this theorem:

```text
CentralCircleTTAdjointSupportTheorem:
For the selected GR/QG exact branch, the physical TT adjoint support B^*P_TT
is exhausted by the exact central-circle Z64 projector, and the sampled
central-circle coordinate is the same coordinate used by the exact Z64 shift.
```

Equivalently:

```text
Pi_exact64 B^* P_TT = B^* P_TT.
```

If that theorem is supplied, existing certificates immediately give:

```text
support(J_TT)=|d_*> tensor span{c_2,s_2},
lambda_GR,TT=15
```

in normalized internal exact-branch units.

## What Would Be Overclaiming

It would be overclaiming to use the current central-circle synthesis text as
the proof of exact support. It is excellent physical guidance, but the paper
itself tells us not to treat that synthesis as a new technical theorem.
