---
title: "Selected Qa/SU3 Full Nil-Theta Cocycle Equations"
---

# Selected `Qa/SU3` Full Nil-Theta Cocycle Equations

The ordinary line-bundle route must now use the complex Heisenberg group law:

```text
(z1,z2,z3)*(w1,w2,w3)
= (z1+w1, z2+w2, z3+w3+z1*w2).
```

With Gaussian integer generators:

```text
g1=(1,0,0),  g2=(i,0,0),
g3=(0,1,0),  g4=(0,i,0),
g5=(0,0,1),  g6=(0,0,i),
```

the nontrivial central commutators are:

```text
[g1,g3]=g5
[g1,g4]=g6
[g2,g3]=g6
[g2,g4]=g5^-1
```

So a selected factor must solve:

```text
a_q(gamma,z)=exp(2*pi*i*Phi_q(gamma,z))
```

with:

```text
Phi_q(gamma1*gamma2,z)
= Phi_q(gamma1,gamma2.z) + Phi_q(gamma2,z) mod Z.
```

The target Chern cocycle schema is:

```text
q=(a,b,c)
-> a [g1,g2] + b [g3,g4] + c [g5,g6].
```

This is only a schema, not closure.  The next step is to solve for `Phi_q` or
prove that ordinary factors are obstructed and the projective gerbe route is
required.

## Why This Matters

Eight of the eleven required charges have a central `c` component, and seven
require a mixed nil response.  That is the reason base-torus factors cannot be
the full answer.  The missing packet lives precisely in the nonabelian lattice
data.
